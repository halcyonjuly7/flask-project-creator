import os
import shutil
from .helpers import HelperFunctions


class CssHelper(HelperFunctions):

    def _update_css(self):
        """gets the difference between the app pages and css app pages"""

        css_path = os.path.join(self.folder_location, "static", "css")
        app_and_pages = self._get_apps_and_pages(self._main)
        css_app_pages = self._get_apps_and_pages(css_path)
        self._create_new_css_folders(css_path=css_path, apps_and_pages=app_and_pages, css_app_pages=css_app_pages)
        self._create_new_css_files(css_path=css_path, apps_and_pages=app_and_pages, css_app_pages=css_app_pages)

    def _remove_extra_css_apps(self):
        """removes extra_css folders if there are any"""

        css_path = os.path.join(self.folder_location, "static", "css")
        apps = self._get_apps(self._main)
        css_apps = self._get_apps(css_path)
        extra_css = css_apps.difference(apps)
        for extra_app in extra_css:
            shutil.rmtree(os.path.join(css_path, extra_app))

    def _create_new_css_folders(self, css_path=None, apps_and_pages=None, css_app_pages=None):
        """creates new css files for added apps and pages"""

        static_css_app_folder = lambda app: os.path.join(self.folder_location, "static", "css", app)
        app_css_pages = [app_static_folder for app_static_folder in os.listdir(css_path)]
        for app, pages in apps_and_pages.items():
            if app not in app_css_pages:
                os.makedirs(static_css_app_folder(app))

    def _create_new_css_files(self, css_path=None, apps_and_pages=None, css_app_pages=None):
        """creates new css files"""

        """try to edit redundant code"""

        apps_and_pages = self._get_apps_and_pages(self._main)
        css_app_pages = self._get_apps_and_pages(css_path)
        for app, pages in apps_and_pages.items():
            for page in pages:
                if page not in css_app_pages[app]:
                    with open(os.path.join(css_path, app, page) + ".css", "a") as file:
                        pass

    def _remove_extra_css_files(self, css_path=None, apps_and_pages=None, css_app_pages=None):
        """ removes extra css files if a page is removed """
        
        css_path = os.path.join(self.folder_location, "static", "css")
        apps_and_pages2 = self._get_apps_and_pages(self._main)
        css_app_pages2 = self._get_apps_and_pages(css_path)

        for app, pages in css_app_pages2.items():
            for page in pages:
                page = page.replace(".css", "")
                if page not in apps_and_pages2[app]:
                    os.remove(os.path.join(css_path, app, page + ".css"))
