import os
import shutil
from functools import partial


def create_file(file_path=None, text_format=None, file_operation="w"):
    with open(os.path.join(*file_path), file_operation) as file:
        file.write(text_format)

append_to_file = partial(create_file, file_operation="a")

def create_directory(directory_path=None):
    os.makedirs(os.path.join(*directory_path))





def remove_files(*files):
    for file in files:
        os.remove(file)


def remove_static_templates_app(project_location, project_name, app):
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
    for source in sources:
        shutil.copy(source, destination)