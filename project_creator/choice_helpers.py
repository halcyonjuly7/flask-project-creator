from project_creator.creator_experiment import ClassBasedProject



def choice_action(choice):
    if choice == 1:
        folder_location = input(r"where would this folder be created?: ")
        project_name = input("what would you like to name this project? ")
        pages = input("what pages would you like to create? separate the pages by a comma: ").split(",")
        project = ClassBasedProject(folder_location = folder_location,folder_name = project_name)
        project.create_project(*pages)
    
    elif choice == 3:
        _delete_app()
    
    else:
        _add_delete_page_or_app_choice(choice)


def _split_app_and_pages(app_and_pages):
    app_and_pages = re.split(r"(?<=\]),",app_and_pages)
    app_and_pages_dict = {}
    for i in app_and_pages:
        b = re.sub("[\[\]]","",i).split("=")
        app_and_pages_dict[b[0].strip()] = b[1].strip().split(",")
    return app_and_pages_dict


def _add_delete_page_or_app_choice(choice):
    folder_location = input(r"where is the folder be located?: ")
    project_name = input("what is the project name? ")
    app_and_pages =input("what is the name of the app and what is the name of it's pages? ") 
    app_and_pages = _split_app_and_pages(app_and_pages)
    project = ClassBasedProject(folder_location = folder_location,folder_name = project_name)
    
    if choice == 2:
        project.add_app(**app_and_pages)
    
    elif choice == 4:
        project.add_page(**app_and_pages)
    
    elif choice == 5:
        project.delete_page(**app_and_pages)

def _delete_app():
    folder_location = input(r"where is the folder be located?: ")
    project_name = input("what is the project name?: ")
    apps_to_be_deleted = input("what are the apps you want to delete? separate the apps by a comma: ").split(",")
    project = ClassBasedProject(folder_location = folder_location,folder_name = project_name)
    project.delete_app(*apps_to_be_deleted)

def _show_apps(folder_location = None,folder_name = None):
    for app in os.listdir(os.path.join(folder_location,folder_name,"apps")):
        if not ".py" in app:
            yield app
