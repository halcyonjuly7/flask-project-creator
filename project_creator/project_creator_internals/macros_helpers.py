
from .text_formats import wtform_render_field
from .helper_functions import create_file


class MacrosHelpers(object):

    def _create_macros_files(self, project_location, project_name):
        self._create_render_field_macros(project_location, project_name)

    @staticmethod
    def _create_render_field_macros(project_location, project_name):
        create_file(file_path=(project_location,
                               project_name,
                               "templates",
                               "macros_templates",
                               "macros.html"),
                    text_format=wtform_render_field)


