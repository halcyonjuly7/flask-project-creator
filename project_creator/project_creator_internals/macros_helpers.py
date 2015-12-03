
from .text_formats import wtform_render_field
from .helper_functions import create_file

class MacrosHelpers(object):
    def __init__(self, project_location, project_name):
        self.project_location = project_location
        self.project_name = project_name

    def _create_macros_files(self):
        self._create_render_field_macros()

    def _create_render_field_macros(self):

        create_file(file_path=(self.project_location,
                               self.project_name,
                               "templates",
                               "macros_templates",
                               "macros.html"),
                    text_format=wtform_render_field)


