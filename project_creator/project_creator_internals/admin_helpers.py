import os
import shutil
from .text_formats import (admin_view,
                           admin_model,
                           admin_forms,
                           admin_tests)
from .helper_functions import (create_directory,
                               copy_files_to,
                               get_files_from_directory)


class AdminHelpers:

    def _create_all_admin_files(self, app_folders_path, project_location, project_name):
        self._create_admin_files(project_name, app_folders_path)
        self._create_admin_base_templates(project_location, project_name)
        self._create_admin_base_css(project_location, project_name)
        self._copy_master_html(project_location, project_name)

    @staticmethod
    def _create_admin_folder(app_folders_path, project_location, project_name):
        create_directory(directory_path=(app_folders_path, "admin"))
        create_directory(directory_path=(project_location, project_name, "templates", "admin"))



    @staticmethod
    def _create_admin_files(project_name, app_folders_path):
        admin_files = ("admin_views.py", "admin_models.py", "admin_forms.py", "admin_tests.py")
        py_file_path = lambda py_file: os.path.join(app_folders_path,
                                                    "admin",
                                                    py_file)
        for py_file in admin_files:
            with open(py_file_path(py_file), "w") as file:
                if "views" in py_file:
                    file.write(admin_view)
                elif "models" in py_file:
                    file.write(admin_model)
                elif "tests" in py_file:
                    file.write(admin_tests(project_name))
                else:
                    file.write(admin_forms)
    @staticmethod
    def _create_admin_base_templates(project_location, project_name):
        project_creator_path = os.path.dirname(os.path.dirname(__file__))
        path_of_admin_templates_in_project = os.path.join(project_location,
                                                          project_name,
                                                          "templates",
                                                          "admin_templates")
        base_template_path =  os.path.join(project_creator_path,
                                           "static_files",
                                           "templates",
                                           "admin_templates",
                                           "admin_base.html")
        admin_login_template_path = os.path.join(project_creator_path,
                                                 "static_files",
                                                 "templates",
                                                 "admin_templates",
                                                 "admin_login.html")
        copy_files_to(sources=(base_template_path,
                               admin_login_template_path),
                      destination=path_of_admin_templates_in_project)

    @staticmethod
    def _create_admin_base_css(project_location, project_name):
        project_creator_path = os.path.dirname(os.path.dirname(__file__))
        path_of_admin_css_in_project = os.path.join(project_location,
                                                    project_name,
                                                    "static",
                                                    "admin",
                                                    "css")
        admin_css_path = os.path.join(project_creator_path,
                                      "static_files",
                                      "css")
        admin_css_files = get_files_from_directory(admin_css_path)
        copy_files_to(sources=admin_css_files,
                      destination=path_of_admin_css_in_project)

    @staticmethod
    def _copy_master_html(project_location, project_name):
        project_creator_path = os.path.dirname(os.path.dirname(__file__))
        master_html_path = os.path.join(project_creator_path,
                                        "static_files",
                                        "templates",
                                        "admin_templates",
                                        "master.html")
        master_html_destination = os.path.join(project_location,
                                               project_name,
                                               "templates",
                                               "admin")
        copy_files_to(sources=(master_html_path,), destination=master_html_destination)






