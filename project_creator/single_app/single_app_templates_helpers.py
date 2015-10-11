from .base import Base
from .single_app_text_format import *
import os

class SingleAppsTemplatesHelpers(Base):



	def _create_html_templates(self):

		templates_file_path = lambda page: os.path.join(self.folder_location,self.project_name,"templates",page + ".html")

		for page in self._get_single_app_pages():
		    with open(templates_file_path(page),"a") as html_file:
		        html_file.write(html_template(page))

	def _delete_html_files(*pages):
		"""deletes css associated with the deleted page"""

		templates_path = lambda page : os.path.join(self.folder_location,self.project_name,"templates",page + ".html")

		for page in pages:
			os.remove(templates_path(page))


	def _delete_extra_css_files(self):
		"""deletes extra css files if there are any"""
		pass


	def _change_templates_folder_structure(self,project_name):
		templates_path = os.path.join(self.folder_location,project_name,"templates")
		templates_file_path = lambda templates_file: os.path.join(templates_path,templates_file)
		new_app_templates_path = os.path.join(templates_path,project_name)
		os.makedirs(new_app_templates_path)
		html_files =  (html_file for html_file in os.listdir(templates_path))
		for html_file in html_files:
			shutil.move(templates_path(html_file),os.path.join(templates_path,project_name))
