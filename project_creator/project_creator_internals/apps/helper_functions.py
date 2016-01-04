import os
import shutil
from functools import partial


def create_file(file_path=None, text_format=None, file_operation="w"):
    """

    :param file_path: path of the file to create
    :param text_format: contents to write to the file
    :param file_operation: file operation either 'w' write or 'a' append
    :return: None

    Function description:
        this function is just an abstraction of creating a file
        because doing 'with open(os.path....); is hella ugly

    """
    with open(os.path.join(*file_path), file_operation) as file:
        file.write(text_format)

append_to_file = partial(create_file, file_operation="a")


def create_directory(directory_path=None):
    """

    :param directory_path: the path of the directory -> (tuple) e.g directory_path=("my_path, "another_path)
    :return: None

    Function description:
        an abstraction of os.makedirs because again it looks hella ugly
    """
    os.makedirs(os.path.join(*directory_path))


def remove_files(*files):
    """

    :param files: files to be removed. the files are file paths
    :return: None

    Function description:
        removes all the supplied file paths

    """
    for file in files:
        os.remove(file)


def remove_static_templates_app(project_location, project_name, app):
    """

    :param project_location: location of the project
    :param project_name: name of the project
    :param app: name of the app
    :return: None

    Method description:
        removes the app from the templates and the the static folders

    """
    if app != "admin":
        static_app_location = os.path.join(project_location,
                                           project_name,
                                           "static",
                                           app)
        templates_app_location = os.path.join(project_location,
                                              project_name,
                                              "templates",
                                              app)
        shutil.rmtree(static_app_location)
        shutil.rmtree(templates_app_location)
    else:
        raise ValueError("must delete admin app manually")


def copy_files_to(sources = None, destination= None):
    """

    :param sources: file paths of files to be copied to destination -> (tuple)
                    e.g sources = (file_path1, file_path2)
    :param destination: the destination folder of the files being copied
    :return: None


    Method description:
        copies a tuple of files to a folder destination
    """
    for source in sources:
        shutil.copy(source, destination)


def get_files_from_directory(directory_path=None):
    """

    :param directory_path: directory to get a list of files from
    :return: tuple of file paths of the files in the give directory path

    Method description:
        inspects the contents of a given directory and returns a tuple the path of th files
        in the directory
    """
    return tuple(os.path.join(directory_path, item) for item in os.listdir(directory_path))
