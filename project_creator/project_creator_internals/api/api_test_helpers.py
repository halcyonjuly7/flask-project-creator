
###STANDARD LIBRARY IMPORTS###
import os
##############################

##### 3RD PARTY IMPORTS  #####
##############################


###### LOCAL IMPORTS #########
from ..apps.helper_functions import (append_to_file,
                                     create_file,
                                     update_test_files)

from  .api_textformats import (api_endpoint_test,
                               api_test_bottom,
                               api_test_format)
##############################



class ApiTestHelpers:
    """
    Class Description:
        This class is responsible for the operations that are done with the api endpoint's tests
    """

    #

    API_TESTS_PATH = lambda self, app, api_folder_location: os.path.join(api_folder_location,
                                                                         app,
                                                                         "tests.py".format(app=app))

    def _create_test_files(self):
        """

        :return: None
        Method Description:
            creates the initial test files for the api
        """

        for api_name in self.api_names_and_endpoints.keys():
            create_file(file_path=(self.API_TESTS_PATH(api_name, self.api_folder_location),),
                        text_format=api_test_format(api_name, self.project_name, self.project_location))

    def _write_initial_endpoints_to_tests(self):
        """

        :return: None

        Method Description:
            appends the initial endpoints to the tests.py of the and initial endpoints
            simply means the endpoints that are given when the user chooses create an api
            in the choices
        """
        for api_name, endpoints in self.api_names_and_endpoints.items():
            for endpoint in endpoints:
                append_to_file(file_path=(self.API_TESTS_PATH(api_name, self.api_folder_location),),
                               text_format=api_endpoint_test(api_name, endpoint))
            append_to_file(file_path=(self.API_TESTS_PATH(api_name, self.api_folder_location),),
                           text_format=api_test_bottom)

    def _add_endpoints_to_tests(self):
        """

        :return: None

        Method Description:
            adds the newly added endpoint to the tests.py by creating 2 new files
            1. new_tests.py -> contains all the lines of the old tests.py file up until if __name__ == '__main__'
            2. bottom_info.py -> contains all the lines below, and including  if __name__ == '__main__'

            the old tests.py file will be deleted and the new_test.py file renamed to tests.py file where it contains
            all lines of the deleted tests.py file, the newly added and formatted endpoints, and all the lines in the
            bottom_info.py creating the illusion of updating the tests.py file
        """

        old_tests = lambda app:os.path.join(self.api_folder_location,
                                            app,
                                            "tests.py".format(app=app))
        new_tests = lambda app:os.path.join(self.api_folder_location,
                                            app,
                                            "new_tests.py")

        bottom_info = lambda app:os.path.join(self.api_folder_location,
                                              app,
                                              "bottom_info.py")
        update_test_files(old_tests,
                          bottom_info,
                          new_tests,
                          api_endpoint_test,
                          self.api_names_and_endpoints)

