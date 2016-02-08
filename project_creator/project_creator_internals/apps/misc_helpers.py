from .helper_functions import create_file, create_directory
from .text_formats import celery_task, socket_io, misc_functions


class MiscHelpers:

    # def __init__(self, project_location, project_name):
    #     """
    #     :param project_location: absolute path of the project
    #     :param project_name: name of the project
    #     :return: None
    #
    #     Class description:
    #         this class is responsible for the creation of the misc_files folder
    #         in the project_name/misc_files and the file contents in it
    #
    #
    #     """
    #     self.project_location = project_location
    #     self.project_name = project_name

    def _create_misc_files(self):
        """

        :return: None

        Method description:
            creates the all the files inside the misc_files folder
            such as:
                tasks.py
                socketio.py
                helper_functions.py
        """
        create_file(file_path=(self.project_location,
                               self.project_name,
                               "misc_files",
                               "tasks.py"),
                    text_format=celery_task(self.project_name))

        create_file(file_path=(self.project_location,
                               self.project_name,
                               "misc_files",
                               "socketio.py"),
                    text_format=socket_io(self.project_name))
        create_file(file_path=(self.project_location,
                               self.project_name,
                               "misc_files",
                               "helper_functions.py"),
                    text_format=misc_functions(self.project_name))

    def _create_misc_folder(self):
        """

        :return: None

        Method description:
            creates the misc_files folder


        """
        create_directory(directory_path=(self.project_location,
                                         self.project_name,
                                         "misc_files"))





