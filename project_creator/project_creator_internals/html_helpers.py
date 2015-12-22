from .helper_functions import *
from .text_formats import html_template


class HtmlHelpers(object):
    """This class is responsible for creatig the html files and the html base templates"""

    @staticmethod
    def _create_html_files(project_location,
                           project_name,
                           app,
                           page):
        """creates the html files for your apps"""

        create_file(file_path=(project_location,
                               project_name,
                               "templates",
                               "{app}_templates".format(app=app),
                               "{app}_{page}.html".format(app=app, page=page)),
                    text_format=html_template(app, page))

    @staticmethod
    def _create_html_folders(project_location,
                             project_name,
                             app):
        """creates the templates folder for your apps"""

        create_directory(directory_path=(project_location,
                                         project_name,
                                         "templates",
                                         "{app}_templates".format(app=app)))
    @staticmethod
    def _create_base_templates(project_location,
                               project_name,
                               app):
        """creates the base templates of apps"""
        create_file(file_path=(project_location,
                               project_name,
                               "templates",
                               "base_templates",
                               app + "_base.html"),
                    text_format=html_template(app, project_name))