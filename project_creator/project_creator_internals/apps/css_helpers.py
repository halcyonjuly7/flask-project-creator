from .helper_functions import *
import shutil

class CssHelpers(object):

    def __init__(self, project_location, project_name):
        """

        :param project_location: absolute path of the project
        :param project_name: name of the project
        :return: None

        Class description:
            This class is responsible for the css part of the static folders
            all added pages will be given it's own css

        """
        self.project_locations = project_location
        self.project_name = project_name


    def _create_css_files(self, app, page):
        """

        :param app: name of the app
        :param page: the page to be added
        :return: None

        Method description:
            creates the css files for each newly added page
        """

        create_file(file_path=(self.project_location,
                               self.project_name,
                               "static",
                               app,
                               "css",
                               "{app}_{page}.css".format(app=app,
                                                         page=page)),
                    text_format="{page}.css".format(page=page))



    def _create_css_folders(self, app):
        """

        :param app: name of the app
        :return: None

        Method description:
            creates the new css folders for the added app
        """
        create_directory(directory_path=(self.project_location,
                                         self.project_name,
                                         "static",
                                         app))

    def _remove_static_app(self, app):
        """

        :param app: name of the app to be removed
        :return: None

        Method description:
            removes all the static files, folders and sub folders
            associated with that app
        """
        static_app_location = os.path.join(self.project_location,
                                           self.project_name,
                                           "static",
                                           app)
        shutil.rmtree(static_app_location)
