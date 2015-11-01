import shutil

from .creator_internals import CreatorInternals
from .css_helpers import CssHelpers
from .html_helpers import HtmlHelpers
from .admin_helpers import AdminHelpers
from .helper_functions import *
from .text_formats import *

class ClassBasedProject(CreatorInternals, CssHelpers,
                        HtmlHelpers, AdminHelpers):

    def create_project(self,
                       project_location=None,
                       apps_folder_location=None,
                       parent_directory=None,
                       config_folder="config",
                       project_name=None,
                       **app_names_and_pages):

        """creates a skeleton for a flask project and an initial app called main """

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

        self._create_admin_folder_and_files(apps_folder_location)

    def add_page(self,
                 project_name=None,
                 project_location=None,
                 apps_folder_location=None,
                 **app_names_and_pages):
        """adds a page to specified app/apps and updates templates & static folder as well ass the __init__ to reflect changes"""

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

        url_rules_path = lambda app: os.path.join(project_location,
                                                  project_name,
                                                  "apps",
                                                  app,
                                                  "url_rules.py")

        for app, pages in app_names_and_pages.items():
            with open(views_path(app), "r") as read_view:
                with open(new_view_path(app), "w") as write_view:
                    with open(url_rules_path(app), "w") as url_rules:
                        for line in read_view:
                            if "add_url_rule" in line:
                                url_rules.write(line)
                            else:
                                write_view.write(line)
                    if os.path.exists(os.path.join(project_location,
                                                   project_name,
                                                   "apps",
                                                   app)):
                        for page in pages:
                            write_view.write(class_template(app, page))
                            if page == "index":
                                append_to_file(file_path=(apps_folder_location,
                                                          app,
                                                          "views.py"),
                                               text_format=add_url_rule_index(app, page))
                            else:
                                append_to_file(file_path=(url_rules_path(app),),
                                               text_format=add_url_rule(app, page))
                            append_to_file(file_path=(apps_folder_location,
                                                      app,
                                                      "__init__.py"),
                                           text_format=import_page(page))
                            self._create_new_css_files(project_location,
                                                       project_name,
                                                       app,
                                                       page)

                            self._create_new_html_files(project_location,
                                                        project_name,
                                                        app,
                                                        page)

                        with open(url_rules_path(app), "r") as read_url_rules:
                                    for line in read_url_rules:
                                        write_view.write(line)
                    else:
                        print("that app does not exist")
            try:
                remove_files(url_rules_path(app), views_path(app))
                os.rename(new_view_path(app), views_path(app))
            except:
                pass

    def add_app(self,
                project_location=None,
                project_name=None,
                apps_folder_location=None,
                **app_names_and_pages):
        """adds additional apps and pages inside apps to existing project"""

        for app, pages in app_names_and_pages.items():
            create_directory((apps_folder_location, app))

            self._create_new_css_folders(project_location,
                                         project_name,
                                         app)

            self._create_new_html_folders(project_location,
                                          project_name,
                                          app)

            self._create_app_files(project_name,
                                   apps_folder_location,
                                   app)

            self._create_contents_of_static_folder(project_location,
                                                   project_name,
                                                   app)

            create_file(file_path=(project_location,
                                   project_name,
                                   "templates",
                                   "base_templates",
                                   app + "_base.html"),
                        text_format=view_imports(app, project_name))

            for page in pages:
                append_to_file(file_path=(apps_folder_location,
                                          app,
                                          "views.py"),
                               text_format=class_template(app, page))

                self._create_new_css_files(project_location,
                                           project_name,
                                           app, page)

                self._create_new_html_files(project_location,
                                            project_name,
                                            app,
                                            age)
            for page in pages:
                if page == "index":
                    append_to_file(file_path=(apps_folder_location,
                                              app, "views.py"),
                                   text_format=add_url_rule_index(app, page))
                else:
                    append_to_file(file_path=(apps_folder_location,
                                              app,
                                              "views.py"),
                                   text_format=add_url_rule(app, page))
        apps = app_names_and_pages.keys()
        self._update_init_file(project_location, project_name, *apps)

    def delete_app(self,
                   project_name,
                   project_location,
                   apps_folder_location,
                   *app_names):
        """deletes an app and updates __init__ to reflect changes"""

        for app in app_names:
            shutil.rmtree(os.path.join(apps_folder_location, app))
            remove_static_templates_app(project_location, project_name, app)

        self._update_init_for_deleted_apps(project_name,
                                           project_location,
                                           *app_names)
