import os
from .helper_functions import *
from collections import namedtuple, OrderedDict
from .text_formats import *


class CreatorInternals(object):

    STATIC_SUBFOLDERS = ("css", "img", "font", "scripts")

    def _get_apps(self, path):
        """gets only all the apps"""

        apps = list()
        for app in os.listdir(path):
            if not app.startswith("__") and "admin" not in app:
                apps.append(app)
        return apps

    def _update_init_file(self, project_location, project_name, apps):
        """removes original init and creates a new one for updated apps and pages"""

        old_py_file = os.path.join(project_location,
                                   project_name, "__init__.py")
        new_py_file = os.path.join(project_location,
                                   project_name, "__init__new.py")
        with open(old_py_file, "r") as old_file:
            with open(new_py_file, "w") as new_file:
                for line in old_file:
                    if "from .apps." not in line:
                        new_file.write(line)
                    else:
                        break
                for app in apps:
                    new_file.write(app_init_page_imports(app))
                for app in apps:
                    if app == "main":  #loop repeated twice to achieve an certain format in __init__.py file
                        new_file.write(blueprint_register(app))
                    else:
                        new_file.write(blueprint_register_with_url_prefix(app))
                new_file.write("""    return app""")
        os.remove(old_py_file)
        os.rename(new_py_file, old_py_file)

    def _create_forms_and_models(self, apps_folder_location, app):
        create_file(file_path=(apps_folder_location, app, "models.py"),
                    text_format=models)
        create_file(file_path=(apps_folder_location, app, "forms.py"),
                    text_format=forms)


    def _create_contents_of_static_folder(self, project_location, project_name,
                                          app_name):
            """ creates the sub folders of the static folder"""

            for static_folder in self.STATIC_SUBFOLDERS:
                        create_directory((project_location, project_name, "static", 
                                         app_name, static_folder))

    def _create_static_template_folder(self, project_location, project_name, app_name):
        """creates the static and templates folder including all it's sub folder"""

        self._create_contents_of_static_folder(project_location, project_name,
                                               app_name)
        create_directory(directory_path=(project_location, project_name, "templates", app_name))

    def _make_initial_directories(self, project_location, project_name,
                                  apps_folder_location, parent_directory,
                                  **app_names_and_pages):

        """creates the initial directories"""
        
        


        for directory in [(project_location, project_name), (apps_folder_location,),
                          (parent_directory, "config")]:
            create_directory(directory_path=directory)

        for app in app_names_and_pages.keys():
            create_directory(directory_path=(apps_folder_location, app))
            #create_directory(directory_path=(apps_folder_location, app, "routes"))
            self._create_static_template_folder(project_location, project_name, app)

        create_directory(directory_path=(project_location, project_name, "templates", "base"))

    @staticmethod
    def _create_static_template_files(project_location, project_name,
                                      app_name, page):
        """creates the files inside the static and templates folder"""

        create_file(file_path=(project_location, project_name, "static",
                               app_name, "css", page + ".css"),
                    text_format="text")
        create_file(file_path=(project_location, project_name, "templates", app_name,
                               page + ".html"),
                    text_format=html_template(app_name, page))

    def _make_initial_files(self, project_location, apps_folder_location,
                            parent_directory, project_name, **app_names_and_pages):
        """ creates initial files """

        project_init_file = (project_location, project_name, "__init__.py")

        create_file(file_path=(parent_directory, "config", "config.py"), 
                    text_format=configuration_file)
        create_file(file_path=(parent_directory, "run.py"),
                    text_format=run_pyfile(project_name))
        create_file(file_path=(project_location, project_name, "__init__.py"),
                    text_format=main_init_file("config"))

        for app, pages in app_names_and_pages.items():

            create_file(file_path=(apps_folder_location, app, "models.py"),
                        text_format=models)
            create_file(file_path=(apps_folder_location, app, "forms.py"),
                        text_format=forms)

            create_file(file_path=(apps_folder_location, app, "__init__.py"),
                        text_format=app_blueprint(app))

            create_file(file_path=(apps_folder_location, app, "views.py"),
                        text_format=view_imports(app, project_name))


            
            append_to_file(file_path=project_init_file,
                           text_format=app_init_page_imports(app))

            for page in pages:
                

                append_to_file(file_path=(apps_folder_location, app, "views.py"),
                               text_format=class_template(app, page))
             
                self._create_static_template_files(project_location,
                                                   project_name, app, page)
            for page in pages:
                if page == "index":
                    append_to_file(file_path=(apps_folder_location,
                                              app, "views.py"),
                                   text_format=add_url_rule_index(app, page))
                else:
                    append_to_file(file_path=(apps_folder_location,
                                   app, "views.py"),
                                   text_format=add_url_rule(app, page))

        for app in app_names_and_pages.keys():

            create_file(file_path=(project_location, project_name,
                                   "templates", "base", app + "_base.html"),
                        text_format=view_imports(app, project_name))



            if app == "main":
                append_to_file(file_path=project_init_file,
                               text_format=blueprint_register(app))
            else:
                append_to_file(file_path=project_init_file,
                               text_format=blueprint_register_with_url_prefix(app))

        append_to_file(file_path=project_init_file,
                       text_format="""    return app """)


