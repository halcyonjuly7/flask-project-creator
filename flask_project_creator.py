import re
import os
from project_creator import *

clear = lambda: os.system("cls")

print("""
Welcome to the flask project creator. When asked about the pages to be created please 
use this format: home_page, profile_page, index_page, that is name whatever you want the page
to be followed by an underscore then page i.e. '_page'\n\n """)



print("""
What would you like to do today?
choose a number:

1.create a project?
2.add an app to an existing project?
3.delete an app of an existing project?
4.add a page or pages to an existing app?
5 delete a page or pages of an existing app?
""")

choice = int(input("choice: "))

while choice not in (1,2,3,4,5):
	choice = int(input("""

It seems you did not choose a number within th choices.

choose a number:

1.create a project?
2.add an app to an existing project?
3.delete an app of an existing project?
4.add a page or pages to an existing app?
5 delete a page or pages of an existing app?
"""))



clear()
choice_action(choice)
clear()



# if choice == 1:
# 	folder_location = input("where would this folder be created?: ")
# 	pages = tuple(input("what pages would you like to create? separate the pages by one space").split(" "))
# 	folder_name = input("what would you like to name this project? ")
	
# 	project = ClassBasedProjectProject(folder_location = folder_location,folder_name = folder_name)
# 	project.create_project(*pages)

# elif choice == 2:
# 	folder_location = input("where would is the absolute path of your project? ")
# 	pages = tuple(input("what pages would you like to create? separate the pages by one space").split(" "))
# 	folder_name = input("what would you like to name this project? ")
# 	project = ClassBasedProject(folder_location = folder_location,folder_name = folder_name)
#         project.add_app(**pages)

# project = ClassBasedProject(folder_location = folder_location,folder_name = folder_name)
# project.create_project(*pages)
#folders_create(*pages,folder_location = folder_location,folder_name = folder_name,config_folder = config_folder)


# def choice_action(choice):
# 	if choice == 1:
# 		folder_location = input("where would this folder be created?: ")
# 		pages = input("what pages would you like to create? separate the pages by a comma").split(","))
# 		project_name = input("what would you like to name this project? ")
		
# 		project = ClassBasedProjectProject(folder_location = folder_location,folder_name = project_name)
# 		project.create_project(*pages)
# 	else:
# 		add_delete_page_or_app_choice(choice)

	




# def split_app_and_pages(app_and_pages):
# 	app_and_pages = re.split(r"(?<=\]),",app_and_pages)
# 	app_and_pages_dict = {}
# 	for i in app_and_pages:
# 	    b = re.sub("[\[\]]","",i).split("=")
# 	    c[b[0]] = b[1].strip()
# 	return app_and_pages_dict




# def add_delete_page_or_app_choice(choice):
# 	folder_location = input("where is the folder be located?: ")
# 	project_name = input("what is the project name? ")
# 	app_and_pages =input("what is the name of the app and what is the name of it's pages? ") 
# 	app_and_pages = split_app_and_pages(new_app_and_pages)
# 	project = ClassBasedProject(folder_location = folder_location,folder_name = project_name)
	
# 	if choice == 2:
# 		project.add_app(**app_and_pages)
# 	elif choice == 4:
# 		project.add_page(**app_and_pages)
# 	elif choice == 5:
# 		project.delete_page(**app_and_pages)


# def delete_app_choice():
# 	folder_location = input("where is the folder be located?: ")
# 	project_name = input("what is the project name?: ")
# 	apps_to_delete = input("what are the apps you wan't to delete? separate each app by a comma: ").split(",")
# 	project = ClassBasedProject(folder_location = folder_location,folder_name = project_name)
# 	project.delete_app(*apps_to_delete)

# def add_page_choice():
# 	folder_location = input("where is the folder be located?: ")
# 	project_name = input("what is the project name?: ")
# 	apps_and_pages =input("what is the name of the app and what is the name of it's pages?: ")
# 	new_app_and_pages = split_app_and_pages(new_app_and_pages)
# 	project = ClassBasedProject(folder_location = folder_location,folder_name = project_name)
# 	project.add_page(**app_and_pages)

# def delete_page_choice():
# 	folder_location = input("where is the folder be located?: ")
# 	project_name = input("what is the project name?: ")
# 	apps_and_pages =input("what is the name of the app and what is the name of it's pages?: ")
# 	app_and_pages = split_app_and_pages(app_and_pages)
# 	project = ClassBasedProject(folder_location = folder_location,folder_name = project_name)
# 	project.delete_page(**app_and_pages)







	



    
