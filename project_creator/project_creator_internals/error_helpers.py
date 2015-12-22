import os
from .helper_functions import create_directory, copy_files_to, get_files_from_directory

class ErrorHelpers:

    def _create_error_templates_files(self, project_location, project_name, *apps):
        self._create_error_templates(project_location, project_name, *apps)

    @staticmethod
    def _create_error_templates_folder(project_location, project_name, app):

        create_directory(directory_path=(project_location,
                                         project_name,
                                         "templates",
                                         "error_templates",
                                         "{app}_error_templates".format(app=app)))

    @staticmethod
    def _create_error_templates(project_location, project_name, *apps):
        project_creator_path = os.path.dirname(os.path.dirname(__file__))
        error_templates_path = os.path.join(project_creator_path,
                                            "static_files",
                                            "templates",
                                            "error_templates")
        destination_error_templates_path = lambda app: os.path.join(project_location,
                                                                    project_name,
                                                                    "templates",
                                                                    "error_templates",
                                                                    "{app}_error_templates".format(app=app)
                                                                    )
        error_templates = get_files_from_directory(error_templates_path)
        for app in apps:
            copy_files_to(sources=error_templates, destination=destination_error_templates_path(app))








