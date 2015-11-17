from .helper_functions import *
import shutil

class CssHelpers(object):
    def _create_new_css_files(self,
                              project_location,
                              project_name,
                              app,
                              page):

        create_file(file_path=(project_location,
                               project_name,
                               "static",
                               app,
                               "css",
                               "{app}_{page}.css".format(app=app,
                                                         page=page)),
                    text_format="{page}.css".format(page=page))

    def _create_new_css_folders(self,
                                project_location,
                                project_name,
                                app):

        create_directory(directory_path=(project_location,
                                         project_name,
                                         "static",
                                         app))

    def _remove_static_app(self, project_location, project_name, app):
        static_app_location = os.path.join(project_location,
                                           project_name,
                                           "static",
                                           app)
        shutil.rmtree(static_app_location)
