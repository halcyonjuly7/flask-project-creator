import os
from .single_app_text_format import *

class Base(object):

	def _create_initial_single_app_directories(self):
		"""creates the initial single app directories"""

		folder_paths = lambda *folder_path :os.path.join(self.folder_location,self.project_name,*folder_path)
		list_of_folder_paths = [(self.app_name,),
								("static",),
								("static","css"),
								("static","font"),
								("templates",),
								("config",)]

		for folder in list_of_folder_paths:
			os.makedirs(folder_paths(*folder))


	def _create_initial_single_app_files(self,*pages):

		with open(os.path.join(self.folder_location,self.project_name,"config","config.py"),"w") as config_py:
			config_py.write(configuration_file)

		with open(os.path.join(self.folder_location,"run.py"),"w") as run_file:
			run_file.write(run(self.project_name))

		with open(os.path.join(self.folder_location,self.project_name,"__init__.py"),"w") as main_init:
			main_init.write(app_init())
		    
		with open(os.path.join(self.app_location,"__init__.py"),"w") as apps_init_file:
			apps_init_file.write(apps_init())

		with open(os.path.join(self.folder_location,self.project_name,"__init__.py"),"w") as location_init_file:
		    location_init_file.write(main_init_file("config"))
		    for folder in pages:
		        location_init_file.write(app_init_page_imports(self.app_name,folder))
		    for folder in pages:
		        location_init_file.write(app_init_blueprint_register(folder))
		    location_init_file.write("""
    return app""")                



	def _create_app_pages(self,*pages):
		"""creates the app pages"""
		
		app_page = lambda page: os.path.join(self.app_location,page)
		for page in pages:
			os.makedirs(app_page(page))
			

	def _create_init_routes(self,*pages):
		"""creates the __init__ and routes for the pages"""

		py_file_and_page = lambda page,py_file: os.path.join(self.app_location,page,py_file)

		for page in pages:#self._get_single_app_pages():
		    for py_file in ("__init__.py","routes.py"):
		        if py_file == "__init__.py":
		            with open(py_file_and_page(page,py_file),"w") as file:
		                file.write(page_blueprint(page))
		        else:
		            if "index" in page.lower():
		                with open(py_file_and_page(page,py_file),"w") as file:
		                        file.write(index_route_templates(self.app_name,page))
		            else:
		                with open(py_file_and_page(page,py_file),"w") as file:
		                        file.write(nonindex_templates(self.app_name,page))



	def _get_single_app_pages(self,app_location = None):
		"""gets all the pages inside the app"""

		return (page for page in os.listdir(self.app_location) if not "__" in page)

    
	def _update_main_init_file(self):
		"""updates main_init file for added pages"""

		main_init = os.path.join(self.folder_location,self.project_name,"__init__.py")

		os.remove(main_init)
		with open(main_init,"w") as file:
			file.write(main_init_file("config"))
			for page in self._get_single_app_pages():
				file.write(app_init_page_imports(self.app_name,page))
			for page in self._get_single_app_pages():
				file.write(app_init_blueprint_register(page))













