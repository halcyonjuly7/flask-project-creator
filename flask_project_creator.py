from project_creator.flask_project_creator import *


print("""
Welcome to the flask project creator. When asked about the pages to be created please 
use this format: home_page, profile_page, index_page, that is name whatever you want the page
to be followed by an underscore then page i.e. '_page'\n\n """)



choice = int(input("""
What would you like to do today?
choose a number:

1.create a project?
2.add an app to an existing project?
3.delete an app of an existing project?
"""))

while choice not in (1,2,3):
	choice = int(input("""
It seems you did not choose a number.
choose a number:

1.create a project?
2.add an app to an existing project?
3.delete an app of an existing project?
"""))






if choice == 1:
	folder_location = input("where would this folder be created?: ")
	pages = tuple(input("what pages would you like to create? separate the pages by one space").split(" "))
	folder_name = input("what would you like to name this project? ")
	config_folder = input("what would you like to call your configuration folder? ") 
	project = ClassBasedProjectProject(folder_location = folder_location,folder_name = folder_name)
	project.create_project(*pages)

elif choice == 2:
	folder_location = input("where would is the absolute path of your project? ")
	pages = tuple(input("what pages would you like to create? separate the pages by one space").split(" "))
	folder_name = input("what would you like to name this project? ")
	config_folder = input("what would you like to call your configuration folder? ")
	project = ClassBasedProject(folder_location = folder_location,folder_name = folder_name)
        project.add_app(**pages)

project = ClassBasedProject(folder_location = folder_location,folder_name = folder_name)
project.create_project(*pages)
#folders_create(*pages,folder_location = folder_location,folder_name = folder_name,config_folder = config_folder)
