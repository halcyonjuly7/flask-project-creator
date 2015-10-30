import os
from functools import partial


def create_file(file_path=None, text_format=None, file_operation="w"):
    with open(os.path.join(*file_path), file_operation) as file:
        file.write(text_format)


def create_directory(directory_path=None):
    os.makedirs(os.path.join(*directory_path))


append_to_file = partial(create_file, file_operation="a")
