import os
from .text_formats import wtform_render_field_and_flash_message
from .helper_functions import create_file, copy_files_to, get_files_from_directory


class MacrosHelpers(object):
    """this class is responisble for creating the macros files in the templates folder"""

    def _create_macros_files(self, project_location, project_name):
        self._copy_macros(project_location, project_name)

    @staticmethod
    def _create_render_field_macros(project_location, project_name):
        create_file(file_path=(project_location,
                               project_name,
                               "templates",
                               "macros_templates",
                               "macros.html"),
                    text_format=wtform_render_field_and_flash_message)

    @staticmethod
    def _copy_macros(project_location, project_name):
        project_creator_path = os.path.dirname(os.path.dirname(__file__))
        macros_templates_path = os.path.join(project_creator_path,
                                             "static_files",
                                             "templates",
                                             "macros_templates")
        macros_templates_destination = os.path.join(project_location,
                                                    project_name,
                                                    "templates",
                                                    "macros_templates")
        macros = get_files_from_directory(macros_templates_path)
        copy_files_to(sources=macros, destination=macros_templates_destination)