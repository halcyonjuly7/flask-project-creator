from text_format import *
import os
import shutil
from collections import OrderedDict


class FlaskProject:

    def __init__(self,folder_location,folder_name):
        self.folder_location = os.path.join(folder_location,folder_name)
        self.folder_name = folder_name

    def create_project(self,*pages,config_folder = "config7"):
        """creates a skeleton for a flask project and an initial app called main """
        
        main = os.path.join(self.folder_location,"main")
        os.makedirs(self.folder_location)
        os.makedirs(main)
        with open(os.path.join(self.folder_location,"run.py"),"w") as run_file:
            run_file.write(run(self.folder_name))

        self.__create_static_templates_folder()
        with open(os.path.join(main,"__init__.py"),"w") as main_init:
            with open(os.path.join(self.folder_location,"__init__.py"),"w") as location_init_file:
                location_init_file.write(main_init_file(config_folder))
                for folder in pages:
                    os.makedirs(os.path.join(main,folder))
                    main_init.write(app_init(folder))
                    location_init_file.write(app_init_page_imports("main",folder))
                for folder in pages:
                    location_init_file.write(app_init_blueprint_register(folder))
                    location_init_file.write(app_init_blueprint_register(folder))
                   
                    self.__create_static_template_files(folder)
                    self.__create_init_routes(main,folder)
                location_init_file.write("""
        return app""")


    def add_app(self,**app_names_and_pages):
        """adds additional apps and pages inside apps to existing project"""

        for app,pages in app_names_and_pages.items():
            os.makedirs(os.path.join(self.folder_location,app))
            with open(os.path.join(self.folder_location,app,"__init__.py"),"w") as app_file:
                for page in pages:
                    app_file.write(app_init(page))
                    os.makedirs(os.path.join(self.folder_location,app,page))
                    for py_file in ("__init__.py","routes.py"):
                        with open(os.path.join(self.folder_location,app,page,py_file),"w") as file:
                            if py_file == "__init__.py":
                                file.write(app_init(page))
                            else:
                                file.write(nonindex_templates(page))
        self.__update_init_file()


    def delete_app(self,*app_names):
        """deletes an app and updates __init__ to reflect changes"""

        for app in app_names:
            shutil.rmtree(os.path.join(self.folder_location,app))
        self.__update_init_file()


    def __update_init_file(self):
        """removes original init and creates a new one for updated apps and pages"""
        os.remove(os.path.join(self.folder_location,"__init__.py"))
        with open(os.path.join(self.folder_location,"__init__.py"),"w") as file:
            file.write(main_init_file("config_folder"))
            for app,pages in self.__get_apps_and_pages().items():
                for page in pages:
                    file.write(app_init_page_imports(app,page))
            for app,pages in self.__get_apps_and_pages().items():
                for page in pages: #loop repeated twice to achieve an certain format in __init__.py file
                    file.write(app_init_blueprint_register(page))
            file.write("""
    return app""")
    

    def __create_init_routes(self,main,folder):
        """creates the __init__ and routes file inside each page"""

        for file in ("__init__.py","routes.py"):       
            with open(os.path.join(main,folder,file),"w") as current_file:
                if file == "__init__.py":
                    current_file.write(page_blueprint(folder))
                else:
                    if not "index" in folder:
                        current_file.write(index_route_template(folder))
                    else:
                        current_file.write(nonindex_templates(folder))


    def __get_apps_and_pages(self):
        """gets all the apps and it's pages"""

        apps_and_folders = OrderedDict()
        for app in os.listdir(self.folder_location):
            if os.path.isdir(os.path.join(self.folder_location,app)) and app not in ("static","templates"):
                apps_and_folders.setdefault(app,list())
                for pages in os.listdir(os.path.join(self.folder_location,app)):
                    if os.path.isdir(os.path.join(self.folder_location,app,pages)):
                        apps_and_folders[app].append(pages)
        return apps_and_folders


    def __create_static_templates_folder(self):
         """creates the static and templates folder including all it's sub folder"""

         for misc_folder in ("static","templates"):
            if misc_folder == "static":
                os.makedirs(os.path.join(self.folder_location,misc_folder))
                for static_folder in ("css","img","font"):
                    os.makedirs(os.path.join(self.folder_location,misc_folder,static_folder))
            else:
                os.makedirs(os.path.join(self.folder_location,misc_folder))


    def __create_static_template_files(self,folder):
        """creates the files inside the static and templates folder"""

        for item in (("static","css"),("templates","html")):
            if "static" in item:
                with open(os.path.join(self.folder_location,item[0],item[1],folder + "." + item[1]), "w") as html:
                    pass
            else:
                with open(os.path.join(self.folder_location,item[0],folder + "." + item[1]), "w") as html:
                    html.write(html_template(folder))