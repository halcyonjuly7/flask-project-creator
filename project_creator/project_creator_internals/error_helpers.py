import os
from .helper_functions import create_directory, copy_files_to, get_files_from_directory

class ErrorHelpers:

    def _create_error_templates_files(self, project_location, project_name):
        self._create_error_templates(project_location, project_name)

    @staticmethod
    def _create_error_templates_folder(project_location, project_name):

        create_directory(directory_path=(project_location,
                                         project_name,
                                         "templates",
                                         "error_templates"))

    @staticmethod
    def _create_error_templates(project_location, project_name):
        project_creator_path = os.path.dirname(os.path.dirname(__file__))
        error_templates_path = os.path.join(project_creator_path,
                                            "static_files",
                                            "templates",
                                            "error_templates")
        destination_error_templates_path = os.path.join(project_location,
                                                        project_name,
                                                        "templates",
                                                        "error_templates")
        error_templates = get_files_from_directory(error_templates_path)
        copy_files_to(sources=error_templates, destination=destination_error_templates_path)








