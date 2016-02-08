
###STANDARD LIBRARY IMPORTS###
import os
##############################

##### 3RD PARTY IMPORTS  #####
##############################


###### LOCAL IMPORTS #########
from ..apps.helper_functions import (create_directory,
                                     create_file,
                                     append_to_file,
                                     remove_files)
from  .api_textformats import (flask_restful_api_template,
                               api_views,
                               flask_restful_add_resource,
                               api_page_imports,
                               api_blueprint,
                               api_register_blueprint)
from ..apps.creator_internals import CreatorInternals
from .api_test_helpers import ApiTestHelpers
##############################

class ApiEndPoints(ApiTestHelpers):
    """class for adding api"""

    API_VIEWS_PATH = lambda self, app, api_folder_location: os.path.join(api_folder_location, app, "views.py")
    API_INIT_PATH = lambda self, app, api_folder_location: os.path.join(api_folder_location, app, "__init__.py")

    def __init__(self,
                 project_name,
                 project_location,
                 api_folder_location,
                 **api_names_and_endpoints):
        """
        :param project_name: name of the project
        :param project_location: absolute path of project
        :param api_folder_location: location of the api folder in the project
        :param api_names_and_pages: api names and it's views
        :return: None

        """

        self.project_name = project_name
        self.project_location = project_location
        self.api_folder_location = api_folder_location
        self.api_names_and_endpoints = api_names_and_endpoints

    def _create_api_and_pages(self):
        """
        :return: None

        Method Description:
            Entry point for creating the api folders and it's contents as well as
            appending the specified endpoints to it's appropriate api
        """

        self._create_api_folders()
        self._create_test_files()
        self._create_api_folder_contents()
        self._write_initial_endpoints_to_views()
        self._write_initial_endpoints_to_tests()
        self._register_api_endpoints()

    def _add_endpoints_and_tests(self):
        """

        :return: None

        Method Description:
            convenience method that adds the endpoints to the views.py as well as the tests.py

        """
        self._add_api_endpoints()
        self._add_endpoints_to_tests()

    def _add_api_endpoints(self):
        """
        :return: None


        Method Description:
            reads all lines from views.py up to "api.add_resource" and writes it to a new views.py
            all lines after "api.add_resource" are written to a new api_resource file.
            this is done in order to preserve the order and things written on the views while appending
            the new endpoints. the old views  file will be deleted and the new views renamed to the old view
            and the new api_resource file wll also be deleted

        """

        new_view_path = lambda app: os.path.join(self.api_folder_location, "new_views.py")
        api_resource_path = lambda app: os.path.join(self.api_folder_location, "api_resources.py")
        api_folder = lambda app: os.path.join(self.api_folder_location, app)

        for api, endpoints in self.api_names_and_endpoints.items():
            bottom_of_page = False
            if os.path.exists(api_folder(api)):
                with open(self.API_VIEWS_PATH(api, self.api_folder_location), "r") as old_views:
                    with open(new_view_path(api), "w") as new_view:
                        with open(api_resource_path(api), "w") as api_resource:
                            for line in old_views:
                                if "api.add_resource(" in line or bottom_of_page:
                                    api_resource.write(line)
                                    bottom_of_page=True
                                else:
                                    new_view.write(line)
                            for endpoint in endpoints:
                                new_view.write(flask_restful_api_template(endpoint))
                                api_resource.write(flask_restful_add_resource(endpoint))

                        with open(api_resource_path(api), "r") as api_resource:
                            for line in api_resource:
                                new_view.write(line)
                remove_files(self.API_VIEWS_PATH(api, self.api_folder_location), api_resource_path(api))
                os.rename(new_view_path(api), self.API_VIEWS_PATH(api, self.api_folder_location))
            else:
                print("{api} does not exist".format(api=api))

    def _create_api_folders(self):
        """
        :return: None

        Method Description:
            Creates the api folders

        """

        for api_name in self.api_names_and_endpoints.keys():
            create_directory(directory_path=(self.api_folder_location, api_name))

    def _create_api_folder_contents(self):
        """
        :return: None

        Method Description:
            Creates the api contents includes the tests.py, views.py and __init__.py for the api

        """

        for api_name in self.api_names_and_endpoints.keys():
            create_file(file_path=(self.API_INIT_PATH(api_name, self.api_folder_location),),
                        text_format=api_blueprint(api_name))
            create_file(file_path=(self.API_VIEWS_PATH(api_name, self.api_folder_location), ),
                        text_format=api_views(api_name, self.project_name))

    def _write_initial_endpoints_to_views(self):
        """
        :return: None

        Method Description:
            appends the endpoints to the views.py of the api's

        """

        for api_name, endpoints in self.api_names_and_endpoints.items():
            for endpoint in endpoints:
                append_to_file(file_path=(self.API_VIEWS_PATH(api_name, self.api_folder_location),),
                               text_format=flask_restful_api_template(endpoint))

        for api_name, endpoints in self.api_names_and_endpoints.items():#Looped twice so "api.add_resource" would be at the bottom of the page"
            for endpoint in endpoints:
                append_to_file(file_path=(self.API_VIEWS_PATH(api_name, self.api_folder_location),),
                               text_format=flask_restful_add_resource(endpoint))

    def _register_api_endpoints(self):
        """
        :return: None


        Method Description:
            Updates the main project __init__.py file to register the newly added api's
            because the api's are registered as blueprints this method leverages the
            static methods of CreatorInternals (_format_main_init_file and _write_to_new_init_file_and update)
        """

        old_py_file = os.path.join(self.project_location,
                                   self.project_name,
                                   "__init__.py")

        new_py_file = os.path.join(self.project_location,
                                   self.project_name,
                                   "__init__new.py")

        imports_py_file = os.path.join(self.project_location,
                                       self.project_name,
                                       "__init__imports.py")

        app_register_py_file = os.path.join(self.project_location,
                                            self.project_name,
                                            "__init__register.py")
        CreatorInternals._format_main_init_file(old_py_file,
                                                new_py_file,
                                                imports_py_file,
                                                app_register_py_file,
                                                *self.api_names_and_endpoints.keys(),
                                                page_imports=api_page_imports,
                                                register_blueprint_with_url_prefix=api_register_blueprint)
        CreatorInternals._write_to_new_init_file_and_update(old_py_file,
                                                            new_py_file,
                                                            imports_py_file,
                                                            app_register_py_file)





















