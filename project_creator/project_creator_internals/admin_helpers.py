import os
from .text_formats import admin_view, admin_model, forms

class AdminHelpers:

    def _create_admin_folder_and_files(self, app_folders_path):
        self._create_admin(app_folders_path)
        self._create_admin_files(app_folders_path)

    def _create_admin(self, app_folders_path):
        os.makedirs(os.path.join(app_folders_path, "admin"))

    def _create_admin_files(self, app_folders_path):
        admin_files = ("admin_views.py", "admin_models.py", "admin_forms.py")
        py_file_path = lambda py_file: os.path.join(app_folders_path, "admin", py_file)
        for py_file in admin_files:
            with open(py_file_path(py_file), "w") as file:
                if "views" in py_file:
                    file.write(admin_view)
                elif "models" in py_file:
                    file.write(admin_model)
                else:
                    file.write(forms)