

###STANDARD LIBRARY IMPORTS###
import os
import shutil
from functools import partial
##############################

##### 3RD PARTY IMPORTS  #####
##############################


###### LOCAL IMPORTS #########

##############################





def create_file(file_path=None, text_format=None, file_operation="w"):
    """

    :param file_path: path of the file to create -> tuple e.g file_path = (path)
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


def update_test_files(old_py_file,
                      bottom_info,
                      new_py_file,
                      test_format,
                      app_names_and_pages):
    """

    :param old_py_file: the old test file
    :param bottom_info: the lines below if __name__ == '__main__':
    :param new_py_file: the new updated test file
    :param test_format: the format to use when writing to the test file
    :param api_names_and_pages: a dictionary containing the names of the api and it's endpoints
    :return: None

     Function Description:
        updates the tests files


    """

    for api_name, endpoints in app_names_and_pages.items():
            bottom_of_page = False
            with open(new_py_file(api_name), "w") as new_test_file:
                with open(bottom_info(api_name), "w") as bottom_info_data:
                    with open(old_py_file(api_name), "r") as old_test_file:
                        for line in old_test_file:
                            if not bottom_of_page and "__main__" not in line:
                                new_test_file.write(line)
                            else:
                                bottom_of_page = True
                                bottom_info_data.write(line)
                        for endpoint in endpoints:
                            new_test_file.write(test_format(api_name, endpoint))

                with open(bottom_info(api_name), "r") as bottom_info_data:
                    # for endpoint in endpoints:
                    #     new_api_test_file.write(api_endpoint_test(api_name, endpoint))
                    for line in bottom_info_data:
                        new_test_file.write(line)

            remove_files(old_py_file(api_name), bottom_info(api_name))
            os.rename(new_py_file(api_name), old_py_file(api_name))


