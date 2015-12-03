import os
import shutil
from .text_formats import admin_view, admin_model, admin_forms
from .helper_functions import create_directory, copy_files_to


class AdminHelpers:

    def _create_all_admin_files(self, app_folders_path, project_location, project_name):
        self._create_admin_files(app_folders_path)
        self._create_admin_base_templates(project_location, project_name)
        self._create_admin_base_css(project_location, project_name)

    @staticmethod
    def _create_admin_folder(app_folders_path):
        create_directory(directory_path=(app_folders_path, "admin"))

    @staticmethod
    def _create_admin_files(app_folders_path):
        admin_files = ("admin_views.py", "admin_models.py", "admin_forms.py")
        py_file_path = lambda py_file: os.path.join(app_folders_path,
                                                    "admin",
                                                    py_file)
        for py_file in admin_files:
            with open(py_file_path(py_file), "w") as file:
                if "views" in py_file:
                    file.write(admin_view)
                elif "models" in py_file:
                    file.write(admin_model)
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
        admin_index_css_path = os.path.join(project_creator_path,
                                            "static_files",
                                            "css",
                                            "index.css")
        admin_sb_admin_css_path = os.path.join(project_creator_path,
                                               "static_files",
                                               "css",
                                               "sb-admin-2.css")
        copy_files_to(sources=(admin_index_css_path,
                               admin_sb_admin_css_path),
                      destination=path_of_admin_css_in_project)







