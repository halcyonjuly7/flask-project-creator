import os
from .text_formats import wtform_render_field_and_flash_message
from .helper_functions import create_file, copy_files_to, get_files_from_directory


class MacrosHelpers(object):



    def __init__(self, project_location, project_name):
        """

        :param project_location: absolute path of the project
        :param project_name: name of given to the project
        :return: None

        Class description:
            this class is responsible for the macros templates in the
            templates/macros_templates folder

        """
        self.project_location = project_location
        self.project_name = project_name


    def _create_render_field_macros(self):
        """
        deprecated
        :return: None

         Method description:
            creates the macros file inside the templates/macros_templates folder
            and writes the render field macros in it. the render field macros is a snippet
            taken from the flask docs

        """
        create_file(file_path=(self.project_location,
                               self.project_name,
                               "templates",
                               "macros_templates",
                               "macros.html"),
                    text_format=wtform_render_field_and_flash_message)

    def _create_macros_files(self):
        """

        :return: None

        Method description:
            an internal template in the static_files/templates/macros_templates
            is copied into the project

            templates/macros_templates directory

        """
        project_creator_path = os.path.dirname(os.path.dirname(os.path.dirname(__file__)))
        macros_templates_path = os.path.join(project_creator_path,
                                             "templates",
                                             "macros_templates")
        macros_templates_destination = os.path.join(self.project_location,
                                                    self.project_name,
                                                    "templates",
                                                    "macros_templates")
        macros = get_files_from_directory(macros_templates_path)
        copy_files_to(sources=macros, destination=macros_templates_destination)