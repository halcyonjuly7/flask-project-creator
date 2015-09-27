import os
import re
import shutil
from project_creator.text_format import *
from project_creator.helpers_css import CssHelper
from project_creator.helpers_templates import TemplatesHelper 


class ClassBasedProject(CssHelper,TemplatesHelper):

    def __init__(self,folder_location,folder_name):
        self.folder_location = os.path.join(folder_location,folder_name)
        self.folder_name = folder_name
        self._main = os.path.join(self.folder_location,"apps")

    def create_project(self,*pages,config_folder = "config",FunctionBased = False):
        """creates a skeleton for a flask project and an initial app called main """

        self._make_initial_directories()
        self._make_initial_files(*pages,FunctionBased = FunctionBased)

    def add_app(self,**app_names_and_pages):
        """adds additional apps and pages inside apps to existing project"""

        for app,pages in app_names_and_pages.items():
            os.makedirs(os.path.join(self._main,app))
            with open(os.path.join(self._main,app,"__init__.py"),"w") as app_file:
                for page in pages:
                    app_file.write(app_init())
                    os.makedirs(os.path.join(self._main,app,page))
                    for py_file in ("__init__.py","routes.py"):
                        with open(os.path.join(self._main,app,page,py_file),"w") as file:
                            if py_file == "__init__.py":
                                file.write(app_init())
                            else:
                                file.write(nonindex_templates(page))

        self._update_add_app_or_page()
      
    def add_page(self,**app_names_and_pages):
        """adds a page to specified app/apps and updates templates & static folder as well ass the __init__ to reflect changes"""
        
        for app,pages in app_names_and_pages.items():
            if os.path.exists(os.path.join(self._main,app)):
                for page in pages:
                    os.makedirs(os.path.join(self._main,app,page))
                    self._create_init_routes(self._main,app,page)
            else:
                print("that app does not exist")

        self._update_add_app_or_page()

    def delete_app(self,*app_names):
        """deletes an app and updates __init__ to reflect changes"""

        for app in app_names:
            shutil.rmtree(os.path.join(self._main,app))
        
        self._remove_extra_css_apps()
        self._remove_extra_templates_apps()
        self._update_delete_app_or_page()
       
    
    def delete_page(self,**app_names_and_pages):
        """deletes a page to specified app and updates templates & static folder as well ass the __init__ to reflect changes"""
        
        page_location = lambda app_name,app_page : os.path.join(self._main,app_name,app_page)
        css_path = os.path.join(self.folder_location,"static","css")
        for app,pages in app_names_and_pages.items():
            for page in pages:
                shutil.rmtree(page_location(app,page))

        self._update_delete_app_or_page()






