import os
import shutil
from project_creator.text_format import *
from project_creator.helpers_css import CssHelper
from project_creator.helpers_templates import TemplatesHelper 


class ClassBasedProject(CssHelper,TemplatesHelper):

    def __init__(self,folder_location,folder_name):
        self.folder_location = os.path.join(folder_location,folder_name)
        self.folder_name = folder_name
        self._main = os.path.join(self.folder_location,"apps")

    def create_project(self,*pages,config_folder = "config7",FunctionBased = False):
        """creates a skeleton for a flask project and an initial app called main """

        os.makedirs(self.folder_location)
        os.makedirs(self._main)
        os.makedirs(os.path.join(self._main,self.folder_name))
        with open(os.path.join(self.folder_location,"run.py"),"w") as run_file:
            run_file.write(run(self.folder_name))
        self._create_static_template_folder(self.folder_name)
        
        with open(os.path.join(self._main,self.folder_name,"__init__.py"),"w") as main_init:
            main_init.write(app_init())
            
        with open(os.path.join(self._main,"__init__.py"),"w") as apps_init_file:
            apps_init_file.write(apps_init())


        with open(os.path.join(self.folder_location,"__init__.py"),"w") as location_init_file:
            location_init_file.write(main_init_file(config_folder))
            for folder in pages:
                os.makedirs(os.path.join(self._main,self.folder_name,folder))
                location_init_file.write(app_init_page_imports(self.folder_name,folder))
            for folder in pages:
                location_init_file.write(app_init_blueprint_register(folder))
                self._create_static_template_files(self.folder_name,folder)
                self._create_init_routes(self._main,self.folder_name,folder,FunctionBased)
            location_init_file.write("""
return app""")



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
            for page in pages:
                os.makedirs(os.path.join(self._main,app,page))
                self._create_init_routes(self._main,app,page)

        self._update_add_app_or_page()

    def delete_app(self,*app_names):
        """deletes an app and updates __init__ to reflect changes"""

        for app in app_names:
            shutil.rmtree(os.path.join(self._main,app))
            self._remove_extra_css_folder(app)
            self._remove_extra_templates_folder(app)
        
        self._update_delete_app_or_page()
       
        

    
    def delete_page(self,**app_names_and_pages):
        """deletes a page to specified app and updates templates & static folder as well ass the __init__ to reflect changes"""
        
        page_location = lambda app_name,app_page : os.path.join(self._main,app_name,app_page)
        css_path = os.path.join(self.folder_location,"static","css")
        for app,pages in app_names_and_pages.items():
            for page in pages:
                shutil.rmtree(page_location(app,page))

        self._update_delete_app_or_page()