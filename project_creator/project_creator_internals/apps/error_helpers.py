import os
from .helper_functions import create_directory, copy_files_to, get_files_from_directory

class ErrorHelpers:

    # def __init__(self, project_location, project_name):
    #     """
    #
    #     :param project_location: absolute path of the project
    #     :param project_name: name of given to the project
    #     :return: None
    #
    #     Class description:
    #         This class is responsible for creating the error templates for each app
    #
    #         error templates being the 404, 405, 500 templates
    #         all apps will each have it's own 404, 405, 500 templates
    #     """
    #     self.project_location = project_location
    #     self.project_name = project_name

    def _create_error_templates_files(self, *apps):
        """

        :param apps: name of the apps
        :return:  None

        Method description:
            creates the error templates for each app as mentioned on the Class description
            all apps will have their own 404, 405, 500 templates

        """
        self._create_error_templates(*apps)

    def _create_error_templates_folder(self, app):
        """

        :param app: name of the app
        :return: None

        Method description:
            creates the error templates folders for each app
        """

        create_directory(directory_path=(self.project_location,
                                         self.project_name,
                                         "templates",
                                         "error_templates",
                                         "{app}_error_templates".format(app=app)))

    def _create_error_templates(self, *apps):
        """

        :param apps: apps to add error templates to
        :return: None

        Method description:
            copies the error templates on the internal templates/error_templates folder in
            flask-project-creator for each app


        """
        project_creator_path = os.path.dirname(os.path.dirname(os.path.dirname(__file__)))
        error_templates_path = os.path.join(project_creator_path,
                                            "templates",
                                            "error_templates")
        destination_error_templates_path = lambda app: os.path.join(self.project_location,
                                                                    self.project_name,
                                                                    "templates",
                                                                    "error_templates",
                                                                    "{app}_error_templates".format(app=app)
                                                                    )
        error_templates = get_files_from_directory(error_templates_path)
        for app in apps:
            copy_files_to(sources=error_templates, destination=destination_error_templates_path(app))








