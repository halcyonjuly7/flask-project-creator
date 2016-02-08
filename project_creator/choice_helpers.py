import os
import re
import shutil
from .project_creator_internals.apps.create_project import ClassBasedProject
from .project_creator_internals.api.api_endpoints import ApiEndPoints
from .activate_venv import activate_venv_and_run_py_script


class ChoiceHelpers:

    def __init__(self, choice):
        """

        :param choice: the number the user has chosen

        Class Description:
            This class is responsible for determining the action to take based
            on the users choice

        """

        self.choice = choice


    @staticmethod
    def _split_app_and_pages(app_and_pages):
        """

        :param app_and_pages: a string in the format of app = [page1, page2] that is to be splitted
                              and formatted
        :return: Dict<string, string>

        Function Description:
            splits the app and pages and returns a dictionary where the key is the app and the value are
            it's pages

        """
        app_and_pages = re.split(r"(?<=\]),", app_and_pages)
        app_and_pages_dict = {}
        for item in app_and_pages:
            b = re.sub("[\[\]]", "", item).split("=")
            app_and_pages_dict[b[0].strip()] = b[1].replace(" ", "").split(",")
        return app_and_pages_dict


    def choice_action(self):
        """
        :return: None

        Function Description:
            Determines the action to take based on the given choice
            basically the main entry point of the entire program as what actions to take
            are decided here based on the users choice
        """
        if self.choice == 1:
            virtualenv_location = input(r"where is your venv activate script located? ")
            parent_directory = input(r"where would this folder be created?: ")
            project_name = input("what would you like to name this project? ")
            app_and_pages = input("what is the name of the app and what is the name of it's pages? ")
            app_names_and_pages = self._split_app_and_pages(app_and_pages)
            apps_folder_location = os.path.join(parent_directory, project_name, "apps")
            project = ClassBasedProject(project_location=parent_directory,
                                        apps_folder_location=apps_folder_location,
                                        project_name=project_name,
                                        **app_names_and_pages)
            project.create_project()
            activate_venv_and_run_py_script(parent_directory, virtualenv_location)

        elif self.choice == 3:
            self._delete_app()
        elif self.choice in (2, 4):
            self._add_delete_page_or_app_choice()
        elif self.choice == 5:
            self._add_api()
        else:
            self._add_endpoints()


    def _add_delete_page_or_app_choice(self):
        """
        :return: None

        Function Description:
            This function adds an app or deletes a page depending on the choice
        """

        folder_location = input(r"where is the folder be located?: ")
        project_name = input("what is the project name? ")
        app_and_pages = input("what is the name of the app and what is the name of it's pages? ")
        app_names_and_pages = self._split_app_and_pages(app_and_pages)
        apps_folder_location = os.path.join(folder_location, project_name, "apps")
        project = ClassBasedProject(project_name=project_name,
                                    project_location=folder_location,
                                    apps_folder_location=apps_folder_location,
                                    **app_names_and_pages)
        if self.choice == 2:
            project.add_app()
        elif self.choice == 4:
            project.add_page()



    def _delete_app(self):
        """

        :return: None

        Function Description:
            deletes an app and all it's associated static and templates folder

        """
        folder_location = input(r"where is the folder be located?: ")
        project_name = input("what is the project name?: ")
        apps_to_be_deleted = input("what are the apps you want to delete? separate the apps by a comma: ").replace(" ", "").split(",")
        apps_folder_location = os.path.join(folder_location, project_name, "apps")
        project = ClassBasedProject(project_name=project_name,
                                    project_location=folder_location,
                                    apps_folder_location=apps_folder_location)
        project.delete_app(*apps_to_be_deleted)



    def _add_api(self):
        """

        :return: None
        Function Description:
            creates an api for the project it also adds another folder called api in the
            project_name directory
        """
        project_location = input(r"where is the folder be located?: ")
        project_name = input("what is the project name?: ")
        apps_and_pages = input("what is the name of the app/apps and what is the name of it's page/pages? ")
        api_folder_location = os.path.join(project_location, project_name, "api")
        api_names_and_endpoints = self._split_app_and_pages(apps_and_pages)
        project = ApiEndPoints(project_name, project_location, api_folder_location, **api_names_and_endpoints)
        project._create_api_and_pages()


    def _add_endpoints(self):
        """

        :return: None

        Function Description:
            updates the views for the api app
            all the newly added endpoints will be inside the updated views.py
        """

        project_location = input(r"where is the folder be located?: ")
        project_name = input("what is the project name?: ")
        apps_and_pages = input("what is the name of the app/apps and what is the name of it's page/pages? ")
        api_folder_location = os.path.join(project_location, project_name, "api")
        api_names_and_endpoints = self._split_app_and_pages(apps_and_pages)
        project = ApiEndPoints(project_name,
                               project_location,
                               api_folder_location,
                               **api_names_and_endpoints)
        project._add_endpoints_and_tests()

