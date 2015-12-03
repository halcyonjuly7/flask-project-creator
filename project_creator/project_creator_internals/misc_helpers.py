from .helper_functions import create_file, create_directory
from .text_formats import celery_task, socket_io, check_password_hash


class MiscHelpers:

    def _create_misc_files(self, project_location, project_name):
        self._create_socketio(project_location, project_name)
        self._create_tasks(project_location, project_name)
        self._create_helper_functions(project_location, project_name)

    @staticmethod
    def _create_misc_folder(project_location, project_name):
        create_directory(directory_path=(project_location,
                                         project_name,
                                         "misc_files"))
    @staticmethod
    def _create_tasks(project_location, project_name):
        create_file(file_path=(project_location,
                               project_name,
                               "misc_files",
                               "tasks.py"),
                    text_format=celery_task(project_name))
    @staticmethod
    def _create_socketio(project_location, project_name):
        create_file(file_path=(project_location,
                               project_name,
                               "misc_files",
                               "socketio.py"),
                    text_format=socket_io(project_name))


    @staticmethod
    def _create_helper_functions(project_location, project_name):
        create_file(file_path=(project_location,
                               project_name,
                               "misc_files",
                               "helper_functions.py"),
                    text_format=check_password_hash)
