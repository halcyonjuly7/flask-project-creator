from .single_app_text_format import *
from .single_app_css_helpers import *
from .single_app_templates_helpers import* 

import os

class SingleApp(SingleAppsTemplatesHelpers,SingleAppCssHelpers):
    def __init__(self,folder_location = None,project_name = None,app_name = None):
        self.folder_location = folder_location
        self.project_name = project_name
        self.app_name = app_name
        self.app_location = os.path.join(folder_location,project_name,app_name)



    def create_project(self,*pages):
        self._create_initial_single_app_directories()
        self._create_app_pages(*pages)
        self._create_init_routes(*pages)
        self._create_initial_single_app_files(*pages)
        self._create_css_files()
        self._create_html_templates()

    def add_pages(self,*pages):

        """adds a page to app"""

        self._create_app_pages(*pages)
        self._create_init_routes(*pages)
        self._create_css_files()
        self._create_html_templates()
        self._update_main_init_file()

    def delete_pages(self,*pages):
        """delete pages"""
        
        self._delete_css_files(*pages)
        self._delete_html_templates(*pages)
        self._update_main_init_file()


        