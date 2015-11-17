import os
from .helper_functions import *
from collections import namedtuple, OrderedDict
from .text_formats import *


class CreatorInternals(object):

    STATIC_SUBFOLDERS = ("css", "img", "font", "scripts")

    @staticmethod
    def _format_main_init_file(old_py_file,
                               new_py_file,
                               imports_py_file,
                               app_register_py_file,
                               *apps):
        """formats the project init file"""

        with open(old_py_file, "r") as old_file:
            with open(new_py_file, "w") as new_file:
                with open(imports_py_file, "w") as imports_file:
                    with open(app_register_py_file, "w") as app_register_file:
                        for line in old_file:
                            if "from .apps." not in line and "app.register_blueprint" not in line and "return" not in line:
                                new_file.write(line)
                            elif "from .apps." in line:
                                imports_file.write(line)
                            elif "app.register_blueprint" in line:
                                app_register_file.write(line)
                        for app in apps:
                            imports_file.write(app_init_page_imports(app))
                        for app in apps:
                            if app == "main":  # loop repeated twice to achieve an certain format in __init__.py file
                                app_register_file.write(blueprint_register(app))
                            else:
                                app_register_file.write(blueprint_register_with_url_prefix(app))
    
    @staticmethod
    def _write_to_new_init_file_and_update(old_py_file,
                                           new_py_file,
                                           imports_py_file,
                                           app_register_py_file):
        """ when an app is added the init file is overwritten"""

        with open(new_py_file, "a") as new_file:
            with open(imports_py_file, "r") as imports_file:
                with open(app_register_py_file, "r") as app_register_file:
                    for line in imports_file:
                        new_file.write(line)
                    for line in app_register_file:
                        new_file.write(line)
            new_file.write("""    return app""")
        remove_files(old_py_file,
                     imports_py_file,
                     app_register_py_file)
        os.rename(new_py_file, old_py_file)

    @staticmethod
    def _create_base_template_and_register_blueprints(project_init_file,
                                                      project_location,
                                                      project_name,
                                                      **app_names_and_pages):
        """creates the base templates for each app and the register_blueprint to main_init_file"""

        for app in app_names_and_pages.keys():
            create_file(file_path=(project_location, project_name,
                                   "templates", "base_templates", app + "_base.html"),
                        text_format=view_imports(app, project_name))
            if app == "main":
                append_to_file(file_path=project_init_file,
                               text_format=blueprint_register(app))
            else:
                append_to_file(file_path=project_init_file,
                               text_format=blueprint_register_with_url_prefix(app))

    @staticmethod
    def _get_apps(path):
        """gets only all the apps"""

        apps = list()
        for app in os.listdir(path):
            if not app.startswith("__") and "admin" not in app:
                apps.append(app)
        return apps

    @staticmethod
    def _create_config_run_and_main_init_file(parent_directory,
                                              project_location,
                                              project_name):

        """ creates the config, main_init_file, and run file"""

        create_file(file_path=(parent_directory,
                               "config",
                               "config.py"),
                    text_format=configuration_file)

        create_file(file_path=(parent_directory, "run.py"),
                    text_format=run_pyfile(project_name))

        create_file(file_path=(project_location,
                               project_name,
                               "__init__.py"),
                    text_format=main_init_file("config"))

    @staticmethod
    def _update_init_for_deleted_apps(project_name,
                                      project_location,
                                      *app_names):
        """ updates the main_init_file to reflect changes with deleted app"""

        old_file = os.path.join(project_location,
                                project_name,
                                "__init__.py")

        new_file = os.path.join(project_location,
                                project_name,
                                "__init__new.py")

        with open(old_file, "r") as old_init_file:
            with open(new_file, "w") as new_init_file:
                for line in old_init_file:
                    if any(app for app in app_names if app in line):
                        continue
                    else:
                        new_init_file.write(line)
        remove_files(old_file)
        os.rename(new_file, old_file)

    @staticmethod
    def _create_app_files(project_name,
                          apps_folder_location,
                          app):
        """creates the files inside each app folder"""

        create_file(file_path=(apps_folder_location,
                               app,
                               "models.py"),
                    text_format=models)

        create_file(file_path=(apps_folder_location,
                               app,
                               "forms.py"),
                    text_format=forms)

        create_file(file_path=(apps_folder_location,
                               app,
                               "__init__.py"),
                    text_format=app_blueprint(app))

        create_file(file_path=(apps_folder_location,
                               app,
                               "views.py"),
                    text_format=view_imports(app, project_name))

    @staticmethod
    def _create_static_template_files(project_location,
                                      project_name,
                                      app_name,
                                      page):
        """creates the files inside the static and templates folder"""

        create_file(file_path=(project_location,
                               project_name,
                               "static",
                               app_name,
                               "css",
                               page + ".css"),
                    text_format="text")

        create_file(file_path=(project_location,
                               project_name,
                               "templates",
                               app_name,
                               page + ".html"),
                    text_format=html_template(app_name, page))

    def _update_init_file(self,
                          project_location,
                          project_name,
                          *apps):
        """removes original init and creates a new one for updated apps and pages"""

        old_py_file = os.path.join(project_location,
                                   project_name,
                                   "__init__.py")

        new_py_file = os.path.join(project_location,
                                   project_name,
                                   "__init__new.py")

        imports_py_file = os.path.join(project_location,
                                       project_name,
                                       "__init__imports.py")

        app_register_py_file = os.path.join(project_location,
                                            project_name,
                                            "__init__register.py")

        self._format_main_init_file(old_py_file,
                                    new_py_file,
                                    imports_py_file,
                                    app_register_py_file,
                                    *apps)

        self._write_to_new_init_file_and_update(old_py_file,
                                                new_py_file,
                                                imports_py_file,
                                                app_register_py_file)

    def _write_to_views_and_main_init_file(self, project_init_file,
                                           project_location,
                                           project_name,
                                           apps_folder_location,
                                           **app_names_and_pages):

        for app, pages in app_names_and_pages.items():
            self._create_app_files(project_name, apps_folder_location, app)
            append_to_file(file_path=project_init_file,
                           text_format=app_init_page_imports(app))
            for page in pages:
                append_to_file(file_path=(apps_folder_location,
                                          app,
                                          "views.py"),
                               text_format=class_template(app, page))

                self._create_static_template_files(project_location,
                                                   project_name,
                                                   app,
                                                   page)
            for page in pages:
                if page == "index":
                    append_to_file(file_path=(apps_folder_location,
                                              app,
                                              "views.py"),
                                   text_format=add_url_rule_index(app, page))
                else:
                    append_to_file(file_path=(apps_folder_location,
                                              app,
                                              "views.py"),
                                   text_format=add_url_rule(app, page))

    def _create_contents_of_static_folder(self, project_location, project_name,
                                          app_name):
            """ creates the sub folders of the static folder"""

            for static_folder in self.STATIC_SUBFOLDERS:
                        create_directory(directory_path=(project_location,
                                                         project_name,
                                                         "static",
                                                         app_name,
                                                         static_folder))

    def _create_static_template_folder(self,
                                       project_location,
                                       project_name,
                                       app_name):
        """creates the static and templates folder including all it's sub folder"""

        self._create_contents_of_static_folder(project_location,
                                               project_name,
                                               app_name)
        create_directory(directory_path=(project_location,
                                         project_name,
                                         "templates",
                                         app_name))

    def _make_initial_directories(self,
                                  project_location,
                                  project_name,
                                  apps_folder_location,
                                  parent_directory,
                                  **app_names_and_pages):

        """creates the initial directories"""

        for directory in [(project_location, project_name), (apps_folder_location,),
                          (parent_directory, "config")]:
            create_directory(directory_path=directory)
        for app in app_names_and_pages.keys():
            create_directory(directory_path=(apps_folder_location, app))
            self._create_static_template_folder(project_location,
                                                project_name,
                                                app)

        create_directory(directory_path=(project_location,
                                         project_name,
                                         "templates",
                                         "base_templates"))

        create_directory(directory_path=(project_location,
                                         project_name,
                                         "templates",
                                         "admin_templates"))

        self._create_contents_of_static_folder(project_location,
                                               project_name, "admin")

    def _make_initial_files(self,
                            project_location,
                            apps_folder_location,
                            parent_directory,
                            project_name,
                            **app_names_and_pages):
        """ creates initial files """

        project_init_file = (project_location, project_name, "__init__.py")
        self._create_config_run_and_main_init_file(parent_directory,
                                                   project_location,
                                                   project_name)

        self._write_to_views_and_main_init_file(project_init_file,
                                                project_location,
                                                project_name,
                                                apps_folder_location,
                                                **app_names_and_pages)

        self._create_base_template_and_register_blueprints(project_init_file,
                                                           project_location,
                                                           project_name,
                                                           **app_names_and_pages)
        append_to_file(file_path=project_init_file,
                       text_format="""    return app """)
