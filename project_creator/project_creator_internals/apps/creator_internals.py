import os
from .helper_functions import *
from .text_formats import *
from .macros_helpers import MacrosHelpers
from .misc_helpers import MiscHelpers
from .error_helpers import ErrorHelpers
from .admin_helpers import AdminHelpers
from .html_helpers import HtmlHelpers
from .test_helpers import TestHelpers
from .css_helpers import CssHelpers


class CreatorInternals(MiscHelpers,
                       ErrorHelpers,
                       AdminHelpers,
                       MacrosHelpers,
                       HtmlHelpers,
                       TestHelpers,
                       CssHelpers):
    STATIC_SUBFOLDERS = ("css", "img", "font", "scripts")


    def __init__(self,
                 project_location=None,
                 apps_folder_location=None,
                 project_name=None,
                 **app_names_and_pages):

        self.project_location = project_location
        self.apps_folder_location = apps_folder_location
        self.project_name = project_name
        self.app_names_and_pages = app_names_and_pages

        MiscHelpers.__init__(self, project_location, project_name)
        ErrorHelpers.__init__(self, project_location, project_name)
        AdminHelpers.__init__(self, apps_folder_location, project_location, project_name)
        MacrosHelpers.__init__(self, project_location, project_name)
        HtmlHelpers.__init__(self, project_location, project_name)
        TestHelpers.__init__(self,
                             project_name,
                             project_location,
                             apps_folder_location,
                             **app_names_and_pages)
        CssHelpers.__init__(self, project_location, project_name)


    @staticmethod
    def _format_main_init_file(old_py_file,
                               new_py_file,
                               imports_py_file,
                               app_register_py_file,
                               *apps,
                               page_imports=app_init_page_imports,
                               register_blueprint_with_url_prefix=blueprint_register_with_url_prefix
                               ):
        """

        parameters:

            old_py_file: the path of the original  root directory __init__.py file
            new_py_file: the path of a new root directory __init__.py file where all the new blueprints
                         are registered
            imports_py_file: this is the part of the root directory __init__.py file that contains the relative
                             imports of the blueprints

            app_register_py_file: path of a new file where the registered blueprints from the root __init__.py are
            copied



        Method description:
            This static method is responsible for reformatting the root directory __init__.py file
            once an app or apps are added a new __init__.py is created and all lines of the old __init__.py
            are copied up until. The very first occurance of the line 'from .apps.{app_name} import {app_name}'
            after that ..
        """

        with open(old_py_file, "r") as old_file:
            with open(new_py_file, "w") as new_file:
                with open(imports_py_file, "w") as imports_file:
                    with open(app_register_py_file, "w") as app_register_file:
                        for line in old_file:
                            if all(flag not in line for flag in ("from .apps.", "app.register_blueprint", "return")):
                                new_file.write(line)
                            elif "from .apps." in line:
                                imports_file.write(line)
                            elif "app.register_blueprint" in line:
                                app_register_file.write(line)
                        for app in apps:
                            imports_file.write(page_imports(app))
                        for app in apps:
                            if app == "main":  # loop repeated twice to achieve an certain format in __init__.py file
                                app_register_file.write(blueprint_register(app))
                            else:
                                # app_register_file.write(register_blueprint(app))
                                app_register_file.write(register_blueprint_with_url_prefix(app))
    
    @staticmethod
    def _write_to_new_init_file_and_update(old_py_file,
                                           new_py_file,
                                           imports_py_file,
                                           app_register_py_file):
        """

        :param old_py_file: the original  root __init__.py file
        :param new_py_file: a copy of the original __init__.py file
        :param imports_py_file: a file containing all the lines with 'from.apps' in it
        :param app_register_py_file: a file containing all the lines of the original root __init__.py
                                     whose lines contain. 'app.register_blueprint'
        :return: None


        Method description:
            this method is responsible for updating the root __init__.py file


        """

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
    def _register_blueprint(project_init_file, app):

        """

        :param project_init_file: location of the root __init__.py
        :param app: name of the blueprint to register
        :return: None

        Method description:
            this method is responsible for registering the blueprints upon initial creation of the project
            e.i when the user chooses option 1. create project


        """

        if app.lower() == "main":
            append_to_file(file_path=project_init_file,
                           text_format=blueprint_register(app))
        else:
            append_to_file(file_path=project_init_file,
                           text_format=blueprint_register_with_url_prefix(app))


    @staticmethod
    def _get_apps(path):
        """

        :param path: path of the apps folder
        :return: None

        Method description:(deprecated)
            gets all the apps of the apps folder path

        """
        """gets only all the apps"""

        apps = list()
        for app in os.listdir(path):
            if not app.startswith("__") and "admin" not in app:
                apps.append(app)
        return apps


    def _create_config_run_and_main_init_file(self):
        """

        :return: None

        Method description:
            creates the config.py, run.py and the root __init__.py
            all the created files will be formatted according to the text_format
        """

        """ creates the config, main_init_file, and run file"""

        create_file(file_path=(self.project_location,
                               "config",
                               "developement_config.py"),
                    text_format=configuration_file)

        create_file(file_path=(self.project_location,
                               "config",
                               "production_config.py"),
                    text_format=configuration_file)

        create_file(file_path=(self.project_location, "run.py"),
                    text_format=run_pyfile(self.project_name))

        create_file(file_path=(self.project_location,
                               self.project_name,
                               "__init__.py"),
                    text_format=main_init_file("config"))


    def _update_init_for_deleted_apps(self, *app_names):
        """

        :param app_names: names of the apps to be deleted
        :return: None

        Method description:
             updates the main_init_file to reflect changes with deleted app
             once a user chooses delete an app. All the apps. The apps static and templates file
             the app if deleted will also be unregistered from the root __init_ file

        //Todo check the logic for this method

        """

        old_file = os.path.join(self.project_location,
                                self.project_name,
                                "__init__.py")

        new_file = os.path.join(self.project_location,
                                self.project_name,
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


    def _create_app_files(self, app):
        """

        :param app: the name of the folder of the app
        :return: None

        Method description:
            creates the files inside each app folder..
            each app will have it's own folder in the project_name/apps/app_name directory
            to make each app modular each app folder will have 4 files :

            models.py -> models used by that app
            forms.py -> forms used by that app
            views.py -> views/routes of the app
            __init__.py


        """


        create_file(file_path=(self.apps_folder_location,
                               app,
                               "models.py"),
                    text_format=models)

        create_file(file_path=(self.apps_folder_location,
                               app,
                               "forms.py"),
                    text_format=forms)

        create_file(file_path=(self.apps_folder_location,
                               app,
                               "__init__.py"),
                    text_format=app_blueprint(app))

        create_file(file_path=(self.apps_folder_location,
                               app,
                               "views.py"),
                    text_format=view_imports(app, self.project_name))

        # create_file(file_path=(self.apps_folder_location,
        #                        app,
        #                        "tests.py"),
        #             text_format=tests_format(app, self.project_name))


    def _create_celery_worker(self):
        """

        :return: None

         Method description:
            creates a celery worker template on the directory of the project for easy deployment
            of celery workers. contents of the celery_worker.py based off of Miguel Grinberg's blog
            on using celery with the app factory method

        """

        create_file(file_path=(self.project_location,
                               "celery_worker.py"),
                    text_format=celery_worker(self.project_name))




    def _create_static_template_files(self, app_name, page):

        """

        :param app_name: name of the app to determine it's location
        :param page: name of the page to be added
        :return: None

        Method description:
            creates the static and the template files for the app and it's pages.
            each page will have it's own html and css in the templates and static folders respectively


        """

        """creates the files inside the static and templates folder"""

        self._create_css_files(app_name, page)
        self._create_html_files(app_name, page)

    def _create_base_template_and_register_blueprints(self, project_init_file):

        """

        :param project_init_file: The location of the root __init__.py file of the project
        :return: None

        Method description:
            creates the base templates of each app in the templates/base_templates/ folder
             and then registers each app as a blueprint on the root __init__ file

        """




        for app in self.app_names_and_pages.keys():
            self._create_base_templates(app)
            self._register_blueprint(project_init_file, app)

    def _update_init_file(self, *apps):
        """

        :param apps: the individiual names of the apps to append to the updated init file
        :return: None

        Method description:
            updates the old root __init__ file of the project. how does it do that?

            it makes a new __init__ file and iterates over all the lines of the previous __init__ file
            only up to the very first time the line 'from .apps' appear it then appends the 'from .apps' line
            and any other line after that to a new  file. after all of that is done. the file containing
            the lines 'from .apps import {app_name}' will be appended to the new __init__ file

        """


        """removes original init and creates a new one for updated apps and pages"""

        old_py_file = os.path.join(self.project_location,
                                   self.project_name,
                                   "__init__.py")

        new_py_file = os.path.join(self.project_location,
                                   self.project_name,
                                   "__init__new.py")

        imports_py_file = os.path.join(self.project_location,
                                       self.project_name,
                                       "__init__imports.py")

        app_register_py_file = os.path.join(self.project_location,
                                            self.project_name,
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

    def _write_to_views_and_main_init_file(self, project_init_file):
        """

        :param project_init_file: location of the root __init__.py file
        :return: None

        Method description:
            adds the pages the appropriate views as well as create the files inside the apps folder
        """

        for app, pages in self.app_names_and_pages.items():
            self._create_app_files(app)
            append_to_file(file_path=project_init_file,
                           text_format=app_init_page_imports(app))
            for page in pages:
                if page == "index":
                    append_to_file(file_path=(self.apps_folder_location,
                                              app,
                                              "views.py"),
                                   text_format=function_template_index(app, page))
                else:
                    append_to_file(file_path=(self.apps_folder_location,
                                              app,
                                              "views.py"),
                                   text_format=function_template(app, page))
                self._create_static_template_files(app, page)

    def _create_contents_of_static_folder(self, app_name):
        """

        :param app_name: name of the app
        :return: None


        Method description:
            creates the sub-folders of the static folders for each app
            e.i
            static/
                app_name/
                    css/---------|
                    img/---------|-> these are the subfolders
                    scripts/-----|

        """

        for static_folder in self.STATIC_SUBFOLDERS:
            create_directory(directory_path=(self.project_location,
                                             self.project_name,
                                             "static",
                                             app_name,
                                             static_folder))

    def _create_static_template_folder(self, app_name):
        """

        :param app_name: the name of the individual app
        :return: None

        Method description:
            each app will have it's own static and templates folder for example. having
            2 apps with the following pages this method creates the contents within those folders

            cats = [lucy, marnie], dogs = [jeff, nino]

            the structural heirarchy for the static and templates folder would then be

            Project_Name/
                    templates/
                        cats/
                            cats_lucy.html
                            cats_marnie.html
                        dogs/
                            dogs_jef.html
                            dogs_nino.html
                    static/
                        cats/
                            css/

                            img/
                            font/
                            scripts/


                        dogs/
                            css/

                            img/
                            font/
                            scripts/

        """




        self._create_contents_of_static_folder(app_name)
        self._create_html_folders(app_name)

    def _make_initial_directories(self):
        """

        :return: None

        Method description:
            creates all the initial scaffolding of the project. e.g the folders and it's structural
            heirarchy

        """
        for directory in [(self.project_location, self.project_name),
                          (self.apps_folder_location,),
                          (self.project_location, "config"),
                          (self.project_location, "register_helpers")]:
            create_directory(directory_path=directory)
        
        for app in self.app_names_and_pages.keys():
            create_directory(directory_path=(self.apps_folder_location, app))
            self._create_static_template_folder(app)
            self._create_error_templates_folder(app)

        create_directory(directory_path=(self.project_location,
                                         self.project_name,
                                         "templates",
                                         "base_templates"))

        create_directory(directory_path=(self.project_location,
                                         self.project_name,
                                         "templates",
                                         "admin_templates"))

        create_directory(directory_path=(self.project_location,
                                         self.project_name,
                                         "templates",
                                         "macros_templates"))
        self._create_test_folder()
        self._create_admin_folder()
        self._create_misc_folder()
        self._create_contents_of_static_folder("admin")

    def _make_initial_files(self):
        """
        :return: None

        Method description:
            Creates all the initial files for the skeleton the project.
        """

        project_init_file = (self.project_location, self.project_name, "__init__.py")

        self._create_error_templates_files(*self.app_names_and_pages.keys())
        self._create_misc_files()
        self._create_macros_files()
        self._create_celery_worker()
        self._create_admin_register()
        self._create_all_admin_files()
        self._create_config_run_and_main_init_file()
        self._write_to_views_and_main_init_file(project_init_file)
        self._create_test_file()
        self._create_base_template_and_register_blueprints(project_init_file)
        append_to_file(file_path=project_init_file,
                       text_format="""    return app """)
