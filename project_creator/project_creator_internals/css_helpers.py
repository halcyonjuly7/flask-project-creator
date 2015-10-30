from .helper_functions import *

class CssHelpers(object):
    def _create_new_css_files(self, project_location, project_name, app, page):
        create_file(file_path=(project_location, project_name,
                               "static", app, "css", page + ".css"),
                    text_format="{page}.css".format(page=page))

    def _create_new_css_folders(self, project_location, project_name, app):
        create_directory(directory_path=(project_location, project_name,
                                         "static", app))
