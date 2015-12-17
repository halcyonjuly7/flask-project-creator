from .helper_functions import *
from .text_formats import html_template


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
                    text_format=html_template(app, page))
    @staticmethod
    def _create_new_html_folders(project_location,
                                 project_name,
                                 app):
        create_directory(directory_path=(project_location,
                                         project_name,
                                         "templates",
                                         app))
    @staticmethod
    def _create_base_templates(project_location,
                               project_name,
                               app):

        create_file(file_path=(project_location,
                               project_name,
                               "templates",
                               "base_templates",
                               app + "_base.html"),
                    text_format=html_template(app, project_name))