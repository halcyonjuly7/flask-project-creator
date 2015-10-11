from .base import Base
from .single_app_text_format import *
import os

class SingleAppCssHelpers(Base):


	def _create_css_files(self):
		"""creates css files"""

		css_file_path = lambda page: os.path.join(self.folder_location,self.project_name,"static","css",page + ".css")
		for page in self._get_single_app_pages():
		    with open(css_file_path(page),"a") as css_file:
		        pass

	def _delete_css_files(self,*pages):
		"""deletes css associated with the deleted page"""

		css_path = lambda page : os.path.join(self.folder_location,self.project_name,"static","css",page)

		for page in pages:
			os.remove(css_path(page))

	def _delete_extra_css_files(self):
		"""deletes extra css files if there are any"""
		pass

	def _change_css_folder_structure(self,project_name):
		css_path = os.path.join(self.folder_location,project_name,"static","css")
		css_file_path = lambda css_file: os.path.join(self.folder_location,project_name,"static","css",css_file)
		new_app_cs_path = os.path.join(css_path,project_name)
		os.makedirs(new_app_cs_path)
		css_files =  (css_file for css_file in os.listdir(css_path))
		for css_file in css_files:
			shutil.move(css_path(css_file),os.path.join(css_path,project_name))








	

