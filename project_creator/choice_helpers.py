import os
import re
import shutil
from .project_creator_internals.apps.create_project import ClassBasedProject
from .project_creator_internals.api.api_endpoints import ApiEndPoints
from .activate_venv import activate_venv_and_run_py_script


def _split_app_and_pages(app_and_pages):
    app_and_pages = re.split(r"(?<=\]),", app_and_pages)
    app_and_pages_dict = {}
    for item in app_and_pages:
        b = re.sub("[\[\]]", "", item).split("=")
        app_and_pages_dict[b[0].strip()] = b[1].replace(" ", "").split(",")
    return app_and_pages_dict


def choice_action(choice):
    if choice == 1:
        virtualenv_location = input(r"where is your venv activate script located? ")
        #virtualenv_location = r"C:/Flask3.5/venv/Scripts"
        parent_directory = input(r"where would this folder be created?: ")
        project_name = input("what would you like to name this project? ")
        app_and_pages = input("what is the name of the app and what is the name of it's pages? ")
        app_names_and_pages = _split_app_and_pages(app_and_pages)
        apps_folder_location = os.path.join(parent_directory, project_name, "apps")
        project = ClassBasedProject(project_location=parent_directory,
                                    apps_folder_location=apps_folder_location,
                                    project_name=project_name,
                                    **app_names_and_pages)
        project.create_project()
        activate_venv_and_run_py_script(parent_directory, virtualenv_location)
    elif choice == 3:
        _delete_app()
    elif choice in (2, 4):
        _add_delete_page_or_app_choice(choice)

    elif choice == 5:
        _add_api()

    else:
        _add_endpoints()


def _add_delete_page_or_app_choice(choice):
    folder_location = input(r"where is the folder be located?: ")
    project_name = input("what is the project name? ")
    app_and_pages = input("what is the name of the app and what is the name of it's pages? ")
    app_names_and_pages = _split_app_and_pages(app_and_pages)
    apps_folder_location = os.path.join(folder_location, project_name, "apps")
    project = ClassBasedProject(project_name=project_name,
                                project_location=folder_location,
                                apps_folder_location=apps_folder_location,
                                **app_names_and_pages)

    if choice == 2:
        project.add_app()
    elif choice == 4:
        project.add_page()
    # elif choice == 5:
    #     project.delete_page(**app_and_pages)


def _delete_app():
    folder_location = input(r"where is the folder be located?: ")
    project_name = input("what is the project name?: ")
    apps_to_be_deleted = input("what are the apps you want to delete? separate the apps by a comma: ").replace(" ", "").split(",")
    apps_folder_location = os.path.join(folder_location, project_name, "apps")
    project = ClassBasedProject(project_name=project_name,
                                project_location=folder_location,
                                apps_folder_location=apps_folder_location)
    project.delete_app(*apps_to_be_deleted)



def _add_api():
    project_location = input(r"where is the folder be located?: ")
    project_name = input("what is the project name?: ")
    apps_and_pages = input("what is the name of the app/apps and what is the name of it's page/pages? ")
    api_folder_location = os.path.join(project_location, project_name, "api")
    api_names_and_endpoints = _split_app_and_pages(apps_and_pages)
    project = ApiEndPoints(project_name, project_location, api_folder_location, **api_names_and_endpoints)
    project._create_api_and_pages()


def _add_endpoints():
    project_location = input(r"where is the folder be located?: ")
    project_name = input("what is the project name?: ")
    apps_and_pages = input("what is the name of the app/apps and what is the name of it's page/pages? ")
    api_folder_location = os.path.join(project_location, project_name, "api")
    api_names_and_endpoints = _split_app_and_pages(apps_and_pages)
    project = ApiEndPoints(project_name, project_location, api_folder_location, **api_names_and_endpoints)
    project._add_api_endpoints()

# def _show_apps(folder_location=None, folder_name=None):
#     for app in os.listdir(os.path.join(folder_location, folder_name, "apps")):
#         if ".py" not in app:
#             yield app
