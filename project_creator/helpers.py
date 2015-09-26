from project_creator.text_format import *
import os
import shutil
from collections import OrderedDict    

class HelperFunctions(object):

    def _update_add_app_or_page(self):
        self._update_init_file()
        self._update_css()
        self._remove_extra_css_files()
        self._update_templates()
        self._remove_extra_templates()
    
    def _update_delete_app_or_page(self):
        self._remove_extra_css_files()
        self._remove_extra_templates()
        self._update_init_file()

    def _update_init_file(self):
        """removes original init and creates a new one for updated apps and pages"""
        
        os.remove(os.path.join(self.folder_location,"__init__.py"))
        with open(os.path.join(self.folder_location,"__init__.py"),"w") as file:
            file.write(main_init_file("config_folder"))
            for app,pages in self._get_apps_and_pages(self._main).items():
                for page in pages:
                    file.write(app_init_page_imports(app,page))
            for app,pages in self._get_apps_and_pages(self._main).items():
                for page in pages: #loop repeated twice to achieve an certain format in __init__.py file
                    file.write(app_init_blueprint_register(page))
            file.write("""
    return app""")

    def _create_init_routes(self,main,app_name,folder,FunctionBased = False):
        """creates the __init__ and routes file inside each page"""
        
        if not FunctionBased:
            for file in ("__init__.py","routes.py"):       
                with open(os.path.join(main,app_name,folder,file),"w") as current_file:
                    if file == "__init__.py":
                        current_file.write(page_blueprint(folder))
                    else:
                        if "index" in folder:
                            current_file.write(index_route_template(folder))
                        else:
                            current_file.write(nonindex_templates(folder))
        else:
            pass

    def _get_apps_and_pages(self,path):
        """gets all the apps and it's pages"""

        apps_and_folders = OrderedDict()
        for app in os.listdir(os.path.join(path)):
            if not ".py" in app: 
                apps_and_folders.setdefault(app,list())
                for pages in os.listdir(os.path.join(path,app)):
                    if os.path.isdir(os.path.join(path,app,pages)) or "css" in pages or ".html" in pages:
                        apps_and_folders[app].append(pages)
        return apps_and_folders

    def _create_static_template_folder(self,app_name):
         """creates the static and templates folder including all it's sub folder"""

         for misc_folder in ("static","templates"):
            if misc_folder == "static":
                os.makedirs(os.path.join(self.folder_location,misc_folder))
                for static_folder in ("css","img","font"):
                    os.makedirs(os.path.join(self.folder_location,misc_folder,static_folder))
                os.makedirs(os.path.join(self.folder_location,misc_folder,"css",app_name))
            else:
                os.makedirs(os.path.join(self.folder_location,misc_folder,app_name))

    def _create_static_template_files(self,app_name,folder):
        """creates the files inside the static and templates folder"""

        for item in (("static","css"),("templates","html")):
            if "static" in item:
                with open(os.path.join(self.folder_location,item[0],item[1],app_name,folder + "." + item[1]), "w") as html:
                    pass
            else:
                with open(os.path.join(self.folder_location,item[0],app_name,folder + "." + item[1]), "w") as html:
                    html.write(html_template(app_name,folder))