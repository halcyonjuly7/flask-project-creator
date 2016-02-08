from .helper_functions import *
from .text_formats import html_template


class HtmlHelpers(object):
    """This class is responsible for creatig the html files and the html base templates"""
    # def __init__(self, project_location, project_name):
    #     """
    #
    #     :param project_location: absolute path of the project
    #     :param project_name: name of given to the project
    #     :return: None
    #     """
    #     self.project_location = project_location
    #     self.project_name = project_name


    def _create_html_files(self, app, page):
        """

        :param app: name of the app
        :param page: name of the page
        :return: None

        Method description:
            creates the html files for the given page of a given app

        """
        create_file(file_path=(self.project_location,
                               self.project_name,
                               "templates",
                               "{app}_templates".format(app=app),
                               "{app}_{page}.html".format(app=app, page=page)),
                    text_format=html_template(app, page))


    def _create_html_folders(self, app):
        """

        :param app: name of the app
        :return: None

        Method description:
            creates the template folder for a given app.
            e.g templates/app_name

        """
        """creates the templates folder for your apps"""

        create_directory(directory_path=(self.project_location,
                                         self.project_name,
                                         "templates",
                                         "{app}_templates".format(app=app)))

    def _create_base_templates(self, app):
        """

        :param app: name of the app
        :return: None

        Method description:
            creates a base template for each app on the templates/base_templates folder

        """
        """creates the base templates of apps"""
        create_file(file_path=(self.project_location,
                               self.project_name,
                               "templates",
                               "base_templates",
                               app + "_base.html"),
                    text_format=html_template(app, self.project_name))