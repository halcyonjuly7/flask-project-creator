import os
import shutil
from .text_formats import (admin_view,
                           admin_model,
                           admin_forms,
                           admin_tests,
                           register_admin_views)
from .helper_functions import (create_directory,
                               copy_files_to,
                               get_files_from_directory,
                               create_file)


class AdminHelpers(object):

    def __init__(self, apps_folder_location, project_location, project_name):
        """

        :param project_location: absolute path of the project
        :param apps_folder_location: location of the apps folder in the project
        :param project_name: name of the project
        :return: None


        Class description:
            this class is responsible for all things admin related. like the creation of the admin files in the
            project_name/apps/admin folder


        """
        self.apps_folder_location= apps_folder_location
        self.project_location = project_location
        self.project_name = project_name

    def _create_all_admin_files(self):
        """

        :return: None

        Method description:
            the admin files, base css and html are copied from the root static_files

        """
        self._create_admin_files()
        self._create_admin_base_templates()
        self._create_admin_base_css()
        self._copy_master_html()


    def _create_admin_folder(self):
        """

        :return: None

        Method description:
            creates the admin folder inside the project_name/apps folder as well as the
            admin in the templates folder

        """
        create_directory(directory_path=(self.apps_folder_location, "admin"))
        create_directory(directory_path=(self.project_location, self.project_name, "templates", "admin"))


    def _create_admin_files(self):
        """

        :return: None
        Method description:
            creates the files inside the admin folder such as

            admin_views.py -> the views of the admin blueprint
            admin_models.py -> the models used in the admin blueprint
            admin_test.py -> the tests for your admin views

        """

        admin_files = ("admin_views.py", "admin_models.py", "admin_forms.py", "admin_tests.py")
        py_file_path = lambda py_file: os.path.join(self.apps_folder_location,
                                                    "admin",
                                                    py_file)
        for py_file in admin_files:
            with open(py_file_path(py_file), "w") as file:
                if "views" in py_file:
                    file.write(admin_view)
                elif "models" in py_file:
                    file.write(admin_model)
                elif "tests" in py_file:
                    file.write(admin_tests(self.project_name))
                else:
                    file.write(admin_forms)

    def _create_admin_base_templates(self):

        """

        :return: None
        Method description:
            creates the base templates for the admin app as well as the login template


        """

        project_creator_path = os.path.dirname(os.path.dirname(os.path.dirname(__file__)))
        path_of_admin_templates_in_project = os.path.join(self.project_location,
                                                          self.project_name,
                                                          "templates",
                                                          "admin_templates")
        base_template_path =  os.path.join(project_creator_path,
                                           "templates",
                                           "admin_templates",
                                           "admin_base.html")
        admin_login_template_path = os.path.join(project_creator_path,
                                                 "templates",
                                                 "admin_templates",
                                                 "admin_login.html")
        copy_files_to(sources=(base_template_path,
                               admin_login_template_path),
                      destination=path_of_admin_templates_in_project)


    def _create_admin_base_css(self):
        """

        :return: None
        Method description:
            Css files for the admin blueprint are copied from the internal static_files folder of
            flask-project-creator to override the default flask-admin interface. the sb-admin2 theme
            is used

        """
        project_creator_path = os.path.dirname(os.path.dirname(os.path.dirname(__file__)))
        path_of_admin_css_in_project = os.path.join(self.project_location,
                                                    self.project_name,
                                                    "static",
                                                    "admin",
                                                    "css")
        admin_css_path = os.path.join(project_creator_path,
                                      "static_files",
                                      "css")
        admin_css_files = get_files_from_directory(admin_css_path)
        copy_files_to(sources=admin_css_files,
                      destination=path_of_admin_css_in_project)


    def _copy_master_html(self):
        """

        :return: None
        Method description"
            the html file for the admin blueprint is copied  from the internal_static folder
            this overrides the default html layout of flask-admin
        """
        project_creator_path = os.path.dirname(os.path.dirname(os.path.dirname(__file__)))
        master_html_path = os.path.join(project_creator_path,
                                        "templates",
                                        "admin_templates",
                                        "master.html")
        master_html_destination = os.path.join(self.project_location,
                                               self.project_name,
                                               "templates",
                                               "admin")
        copy_files_to(sources=(master_html_path,), destination=master_html_destination)

    def _create_admin_register(self):
        """

        :return: None

        Method description:
            Creates the admin_register.py file on the register_helpers folder
            in the root directory of the project


        """
        create_file(file_path=(self.project_location,
                               "register_helpers",
                               "admin_register.py"),
                    text_format=register_admin_views(self.project_name))






