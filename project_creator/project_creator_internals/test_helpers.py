import os
from .helper_functions import append_to_file
from .text_formats import page_tests, test_bottom

class TestHelpers:

    def _create_test_pages(self, project_name, project_location, **app_names_and_pages):
        test_py_path = lambda app: os.path.join(project_location,
                                                project_name,
                                                "apps",
                                                app,
                                                "tests.py")
        for app, pages in app_names_and_pages.items():
            for page in pages:
                append_to_file(file_path=(test_py_path(app),),
                               text_format=page_tests(app, page))
            append_to_file(file_path=(test_py_path(app),),
                           text_format=test_bottom)

    def _update_test_page(self, apps_folder_location, **apps_names_and_pages):
        app_test_file = lambda app: os.path.join(apps_folder_location, app, "tests.py")
        new_app_test_file = lambda app: os.path.join(apps_folder_location, app, "_tests.py")
        for app, pages in apps_names_and_pages.items():
            with open(app_test_file(app), "r") as test_file:
                with open(new_app_test_file(app), "w") as new_test_file:
                    for line in test_file:
                        if not "__name__" in line and not "unittest.main()" in line:
                            new_test_file.write(line)
                    for page in pages:
                        new_test_file.write(page_tests(app, page))
                    new_test_file.write(test_bottom)
            os.remove(app_test_file(app))
            os.rename(new_app_test_file(app), app_test_file(app))












