import os
import shutil
from project_creator.helpers import HelperFunctions


class TemplatesHelper(HelperFunctions):
	

	def _create_new_templates(self):
	    """updates css when an app or page is added or deleted"""

	    templates_folder_path = os.path.join(self.folder_location,"templates")
	    app_path = os.path.join(self.folder_location,"apps")
	    apps_pages = self._get_apps_and_pages(app_path)
	    app_templates = self._get_apps_and_pages(templates_folder_path)

	    for app,pages in apps_pages.items():
	        for page in pages:
	        	with open(os.path.join(templates_folder_path,app,page +".html"),"w"):
	        		pass

	def _create_new_templates_folders(self):
	    """creates new app templates"""

	    app_path = os.path.join(self.folder_location,"apps")
	    templates_folder_path = os.path.join(self.folder_location,"templates")
	    apps = self._get_apps_and_pages(app_path)
	    app_templates = [app for app in self._get_apps_and_pages(templates_folder_path).keys()]
	    for app in apps:
	    	if app not in app_templates:
	    		os.makedirs(os.path.join(templates_folder_path,app))

	def _update_templates(self):
		
		self._create_new_templates_folders()
		self._create_new_templates()
		

	def _remove_extra_templates_folder(self,deleted_app):
		templates_path = lambda app : os.path.join(self.folder_location,"templates",app)
		shutil.rmtree(templates_path(deleted_app))
	    
	
	def _remove_extra_templates(self):
		"""removes extra templates incase there are any"""

		apps_location = os.path.join(self.folder_location,"apps")
		templates_location = os.path.join(self.folder_location,"templates")
		extra_template = lambda app,template: os.path.join(self.folder_location,"templates",app,template )

		apps_pages = self._get_apps_and_pages(apps_location)
		template_apps = self._get_apps_and_pages(templates_location)

		for app,pages in template_apps.items():
			for page in pages:
				page = page.replace(".html","")
				if page not in apps_pages[app]:
					os.remove(extra_template(app,page + ".html"))


	    