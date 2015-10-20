run = lambda folder_name:"""
from {0} import create_app, db
if __name__ == "__main__":
    app = create_app("config")
    with app.app_context():
        db.create_all()
    app.run()""".format(folder_name)

app_init = lambda :"""
from . import * """


apps_init = lambda:"""
from . import * """


main_init_file = lambda config_folder:"""
from flask import Flask 
from flask_mail import Mail
from flask.ext.sqlalchemy import SQLAlchemy
from flask.ext.bootstrap import Bootstrap
from flask.ext.login import LoginManager
import os

bootstrap = Bootstrap()
mail = Mail()
db = SQLAlchemy()
lm = LoginManager()
lm.login_view = "/"

def create_app(config_name):
    app = Flask(__name__)
    cfg = os.path.join(os.getcwd(), "{0}", config_name + ".py")
    app.config.from_pyfile(cfg)
    bootstrap.init_app(app)
    db.init_app(app)
    lm.init_app(app)
""".format(config_folder)

app_init_page_imports = lambda app, page_name: """    from .apps.{0}.{1} import {1}\n""".format(app, page_name)

app_init_blueprint_register = lambda page_name: """    app.register_blueprint({0})\n""".format(page_name)


html_template = lambda app_name, folder: """
<!Doctype html>
<html>
  <head>
    <title></title>
    <meta charset='utf-8'>
    <link rel="stylesheet" href="{{{{url_for('static',filename='css/{0}/{1}')}}}}">
  </head>
  <body>
    <h1>Hooray it works! this is your {2} </h1>
  </body>
</html>""".format(app_name, folder + ".css", folder)

page_blueprint = lambda blueprint_name: """
from flask import Blueprint
{0} = Blueprint('{0}', __name__)
from . import routes""".format(blueprint_name)



nonindex_templates = lambda app, folder: """
from flask import render_template, redirect, url_for
from flask.views import View
from . import {0}


class {1}(View):
    def dispatch_request(self):
        return render_template('/{3}/{0}.html')

{0}.add_url_rule('/{2}', view_func={1}.as_view('{1}'), methods =['GET', 'POST'])""".format(folder, "".join(item.capitalize() for item in folder.partition("page")), folder.split("_")[0], app)


index_route_template  = lambda app, folder: """

from flask import render_template, redirect, url_for
from flask.views import View
from . import {0}


class {1}(View):
    def dispatch_request(self):
      return render_template('/{3}/{0}.html')

{0}.add_url_rule('/', view_func={1}.as_view('{1}'), methods =['GET', 'POST'])""".format(folder, "".join(item.capitalize() for item in folder.partition("page")), folder.split("_")[0], app)


configuration_file = """
import os
DEBUG = True
UPLOAD_FOLDER =  ""
SQALCHEMY_DATABASE_URI = "sqlite:/// + os.path.join(os.path.dirname(__file__), ../data-dev.sqlite3 "
SECRET_KEY = "secret123456" 

"""
