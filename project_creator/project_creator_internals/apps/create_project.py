import shutil

from .creator_internals import CreatorInternals
from .helper_functions import *
from .text_formats import *


class ClassBasedProject(CreatorInternals):

    def __init__(self,
                 project_location=None,
                 apps_folder_location=None,
                 project_name=None,
                 **app_names_and_pages):
        """

        :param project_location: absolute path of the project
        :param apps_folder_location: location of the apps folder in the project
        :param project_name: name of the project
        :param app_names_and_pages: the names of the apps and pages the user specified
        :return: None



        Class description:
            this class contains the heart of this program all the files and structure are being made
            inside this class. adding apps, adding pages and updating the root __init__ file are done here

            the structuring and design decisions made for the project scaffolding was inspired
            by Miguel Gringberg's scalable folder structure in his O'reilly video. 'an introduction to flask'

            this project aims to speed up flask development by removing the mundane and repititve parts
            and allowing the user to focus on the core business logic instead.

            this project aims to make use of flask to build scalable big websites and not just small web apps



        """

        self.project_location = project_location
        self.apps_folder_location = apps_folder_location
        self.project_name = project_name
        self.app_names_and_pages = app_names_and_pages

        super().__init__(
                          project_location,
                          apps_folder_location,
                          project_name,
                          **app_names_and_pages)

    def create_project(self):
        """

        :return: None
          Method description:
            creates the project. All of the initial structuring of the files and folders
            are done here.
        """

        self._make_initial_directories()
        self._make_initial_files()

    def add_page(self):
        """

        :return: None

        Method description:
            this function adds the pages for your app. The views.py of the app is also automatically updated and the
            new routes are added. for each added page an accompanying html and css is made with it. Tests are also
            automatically added to the app for that page. the tests can be seen on. the tests.py of the app.
        """

        views_path = lambda app: os.path.join(self.project_location,
                                              self.project_name,
                                              "apps",
                                              app,
                                              "views.py")

        new_view_path = lambda app: os.path.join(self.project_location,
                                                 self.project_name,
                                                 "apps",
                                                 app,
                                                 "new_views.py")

        for app, pages in self.app_names_and_pages.items():
            with open(views_path(app), "r") as read_view:
                with open(new_view_path(app), "w") as write_view:
                    for line in read_view:
                        write_view.write(line)
                    if os.path.exists(os.path.join(self.project_location,
                                                   self.project_name,
                                                   "apps",
                                                   app)):
                        for page in pages:
                            if page == "index":
                                write_view.write(function_template_index(app, page))
                            else:
                                write_view.write(function_template(app, page))

                            self._create_css_files(app, page)
                            self._create_html_files(app, page)
                    else:
                        print("that app does not exist")
            try:
                remove_files(views_path(app))
                os.rename(new_view_path(app), views_path(app))
            except:
                pass
        self._update_test_page()


    def add_app(self):
        """

        :return: None


        Method description:
        creates new apps in your project and automatically registers the app. All apps are blueprints and the blueprint
        names are the app names that are specified. this will also create a base_template for the app. The root
        __init__.py of the project is also updated to accomodate for the newly added apps.

        """

        for app, pages in self.app_names_and_pages.items():
            create_directory((self.apps_folder_location, app))
            self._create_css_folders(app)
            self._create_html_folders(app)
            self._create_app_files(app)
            self._create_contents_of_static_folder(app)
            self._create_base_templates(app)
            for page in pages:
                append_to_file(file_path=(self.apps_folder_location,
                                          app,
                                          "views.py"),
                               text_format=function_template(app, page))
                self._create_css_files(app, page)
                self._create_html_files(app, page)

        self._create_test_pages()
        self._update_init_file(*self.app_names_and_pages.keys())

    def delete_app(self, *apps):
        """

        :param apps: name of the apps to be deleted
        :return: None

        Method description:
        deletes an app and unregisters the blueprint of the app and automatically updates the root __init__.py
        to reflect the changes of the removed app


        """

        for app in apps:
            shutil.rmtree(os.path.join(self.apps_folder_location, app))
            remove_static_templates_app(self.project_location, self.project_name, app)

        self._update_init_for_deleted_apps(*self.app_names_and_pages.keys())






