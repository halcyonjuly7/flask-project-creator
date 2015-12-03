from .helper_functions import *


class HtmlHelpers(object):
    @staticmethod
    def _create_new_html_files(project_location,
                               project_name,
                               app,
                               page):
        create_file(file_path=(project_location,
                               project_name,
                               "templates",
                               app,
                               "{app}_{page}.html".format(app=app, page=page)),
                    text_format="<h1>hurray it worked this is your {app} {page} page </h1>".format(app=app, page=page))
    @staticmethod
    def _create_new_html_folders(project_location,
                                 project_name,
                                 app):
        create_directory(directory_path=(project_location,
                                         project_name,
                                         "templates",
                                         app))
