import os
from .helper_functions import append_to_file, create_directory, create_file
from .text_formats import page_tests, test_bottom, tests_format

class TestHelpers:
    def __init__(self,
                 project_name,
                 project_location,
                 apps_folder_location,
                 **app_names_and_pages):


        """

        :param project_name: name of the project
        :param project_location: absolute path of the project
        :param apps_folder_location: the locations of the apps folder in the project
        :param app_names_and_pages: the app names and pages -> (dict)
        :return: None

         Class description:
            this class is responsible for the creation of the tests.py
            inside every app in the apps folder

        """

        self.project_name = project_name
        self.project_location = project_location
        self.app_names_and_pages = app_names_and_pages
        self.apps_folder_location = apps_folder_location

    def _create_test_folder(self):
        """

        :return: None

        Method Description:
         creates the test folder directory in the project location

        """
        create_directory(directory_path=(self.project_location, "tests"))

    def _create_test_file(self):
        """

        :return: None

        Method Description:
         creates the test.py directory in the project location

        """

        app_to_test = lambda app: os.path.join(self.project_location,
                                               "tests",
                                               "{app}_tests.py".format(app=app))
        for app_name in self.app_names_and_pages.keys():
            create_file(file_path=(app_to_test(app_name),),
                        text_format=tests_format(app_name, self.project_name))

        self._create_test_pages()



    def _create_test_pages(self):
        """

        :return: None

         Method description:
            appends the added views into the tests.py file
        """
        
        test_py_path = lambda app: os.path.join(self.project_location,
                                                "tests",
                                                "{app}_tests.py".format(app=app))



        for app, pages in self.app_names_and_pages.items():
            for page in pages:
                append_to_file(file_path=(test_py_path(app),),
                               text_format=page_tests(app, page))
            append_to_file(file_path=(test_py_path(app),),
                           text_format=test_bottom)

    def _update_test_page(self):
        """

        :return: None

        Method description:
            updates the tests.py to accomodate the newly added views

        """

        app_test_file = lambda app: os.path.join(self.project_location,
                                                 "tests",
                                                 "{app}_tests.py".format(app=app))
        new_app_test_file = lambda app: os.path.join(self.project_location,
                                                     "tests",
                                                     "new_{app}_tests.py".format(app=app))

        for app, pages in self.app_names_and_pages.items():
            with open(app_test_file(app), "r") as test_file:
                with open(new_app_test_file(app), "w") as new_test_file:
                    for line in test_file:
                        if not "__name__" in line and not "unittest.main()" in line:
                            new_test_file.write(line)
                    for page in pages:
                        new_test_file.write(page_tests(app, page))
                    new_test_file.write(test_bottom)
            os.remove(app_test_file(app))
            os.rename(new_app_test_file(app), app_test_file(app))












