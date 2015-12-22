import shutil

from .creator_internals import CreatorInternals
from .helper_functions import *
from .text_formats import *


class ClassBasedProject(CreatorInternals):

    def create_project(self,
                       project_location=None,
                       apps_folder_location=None,
                       parent_directory=None,
                       project_name=None,
                       **app_names_and_pages):

        """creates a skeleton for a flask project

        parameters:
        project_location: Location of where the project should be made
        apps_folder_location: This  is set by choice_helpers.py no need to deal with this
        parent_directory: This  is set by choice_helpers.py no need to deal with this
        project_name: The name of of the project
        app_names_and_pages: A dictionary containing the apps and pages, also set by choice_helpers.py


        Method description:
        creates the project all of the initial structuring of the files and folders
        are done here.

        """

        self._make_initial_directories(project_location,
                                       project_name,
                                       apps_folder_location,
                                       parent_directory,
                                       **app_names_and_pages)

        self._make_initial_files(project_location,
                                 apps_folder_location,
                                 parent_directory,
                                 project_name,
                                 **app_names_and_pages)

    def add_page(self,
                 project_name=None,
                 project_location=None,
                 apps_folder_location=None,
                 **app_names_and_pages):
        """
        parameters:

        project_name: The name of of the project
        project_location: Location of where the project should be made
        apps_folder_location: This  is set by choice_helpers.py no need to deal with this
        app_names_and_pages: A dictionary containing the apps and pages, also set by choice_helpers.py


        this function adds the pages for your app. The views.py of the app is also automatically updated and the
        new routes are added. for each added page an accompanying html and css is made with it. Tests are also
        automatically added to the app for that page. the tests can be seen on. the tests.py of the app.

        """
        views_path = lambda app: os.path.join(project_location,
                                              project_name,
                                              "apps",
                                              app,
                                              "views.py")

        new_view_path = lambda app: os.path.join(project_location,
                                                 project_name,
                                                 "apps",
                                                 app,
                                                 "new_views.py")

        for app, pages in app_names_and_pages.items():
            with open(views_path(app), "r") as read_view:
                with open(new_view_path(app), "w") as write_view:
                    for line in read_view:
                        write_view.write(line)
                    if os.path.exists(os.path.join(project_location,
                                                   project_name,
                                                   "apps",
                                                   app)):
                        for page in pages:
                            if page == "index":
                                write_view.write(function_template_index(app, page))
                            else:
                                write_view.write(function_template(app, page))

                            self._create_css_files(project_location,
                                                   project_name,
                                                   app,
                                                   page)
                            self._create_html_files(project_location,
                                                    project_name,
                                                    app,
                                                    page)
                    else:
                        print("that app does not exist")

            try:
                remove_files(views_path(app))

                os.rename(new_view_path(app), views_path(app))
            except:
                pass
        self._update_test_page(apps_folder_location, **app_names_and_pages)


    def add_app(self,
                project_location=None,
                project_name=None,
                apps_folder_location=None,
                **app_names_and_pages):
        """

        parameters:

        project_name: The name of of the project
        project_location: Location of where the project should be made
        apps_folder_location: This  is set by choice_helpers.py no need to deal with this
        app_names_and_pages: A dictionary containing the apps and pages, also set by choice_helpers.py



        Method description:
        creates new apps in your project and automatically registers the app. All apps are blueprints and the blueprint
        names are the app names that are specified. this will also create a base_template for the app. The root
        __init__.py of the project is also updated to accomdate for the newly added apps.


        """

        for app, pages in app_names_and_pages.items():
            create_directory((apps_folder_location, app))
            self._create_css_folders(project_location,
                                     project_name,
                                     app)
            self._create_html_folders(project_location,
                                      project_name,
                                      app)
            self._create_app_files(project_name,
                                   apps_folder_location,
                                   app)
            self._create_contents_of_static_folder(project_location,
                                                   project_name,
                                                   app)
            self._create_base_templates(project_location, project_name, app)

            for page in pages:
                append_to_file(file_path=(apps_folder_location,
                                          app,
                                          "views.py"),
                               text_format=function_template(app, page))
                self._create_css_files(project_location,
                                       project_name,
                                       app,
                                       page)
                self._create_html_files(project_location,
                                        project_name,
                                        app,
                                        page)

        self._create_test_pages(project_name, project_location, **app_names_and_pages)
        self._update_init_file(project_location, project_name, *app_names_and_pages.keys())

    def delete_app(self,
                   project_name,
                   project_location,
                   apps_folder_location,
                   *app_names):
        """

        parameters:

        project_name: The name of of the project
        project_location: Location of where the project should be made
        apps_folder_location: This  is set by choice_helpers.py no need to deal with this
        app_names_and_pages: A dictionary containing the apps and pages, also set by choice_helpers.py



        Method description:
        deletes an app and unregisters the blueprint of the app and automatically updates the root __init__.py
        to reflect the changes of the removed app




        """

        for app in app_names:
            shutil.rmtree(os.path.join(apps_folder_location, app))
            remove_static_templates_app(project_location, project_name, app)

        self._update_init_for_deleted_apps(project_name,
                                           project_location,
                                           *app_names)
