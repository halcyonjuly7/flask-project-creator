from flask_project_creator_function import folders_create

print("""
Welcome to the flask project creator. When asked about the pages to be created please 
use this format: home_page, profile_page, index_page, that is name whatever you want the page
to be followed by an underscore then page i.e. '_page'\n\n """)

folder_location = input("where would this folder be created?: ")
pages = tuple(input("what pages would you like to create? separate the pages by one space").split(" "))
folder_name = input("what would you like to name this project? ")
config_folder = input("what would you like to call your configuration folder? ") 


folders_create(*pages,folder_location = folder_location,folder_name = folder_name,config_folder = config_folder)


            
