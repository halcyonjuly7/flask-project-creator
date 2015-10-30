### CONFIGURATION FILE ##################################


configuration_file = """
### Standard Library Imports ###
import os
################################

### 3rd Party Imports ###

################################

### Local Imports ###

################################

DEBUG = True
UPLOAD_FOLDER =  ""
SQALCHEMY_DATABASE_URI = "sqlite:/// + os.path.join(os.path.dirname(__file__), ../data-dev.sqlite3 "
SECRET_KEY = "secret123456" 

"""

############################################################



#########################################################
#--------------------RUN PYFILE-------------------------#
#########################################################


run_pyfile = lambda project_name: """
### Standard Library Imports ###

################################

### 3rd Party Imports ###

#################################

### Local Imports ###
from {project} import create_app, db
#################################

if __name__ == "__main__":
    app = create_app("config")
    with app.app_context():
        db.create_all()
    app.run()""".format(project=project_name)


############################################################




##########################################################
#-------------------APP BLUEPRINT -----------------------#
##########################################################


app_blueprint = lambda blueprint_name: """
### Standard Library Imports ###

################################

### 3rd Party Imports ###
from flask import Blueprint
################################

### Local Imports ###

################################


{blueprint_name} = Blueprint('{blueprint_name}', __name__)
from .views import *

""".format(blueprint_name=blueprint_name)

############################################################



##########################################################
#---------------APP __init__.py FILES--------------------#
##########################################################


app_init = lambda: """
from .routes import * """


apps_init = """
from . import * """


##########################################################



##########################################################
#-------MAIN PROJECT __init__.py FILE--------------------#
##########################################################


main_init_file = lambda config_folder: """
### Standard Library Imports ###
import os
################################

### 3rd Party Imports ###
from flask import Flask 
from flask_mail import Mail
from flask.ext.sqlalchemy import SQLAlchemy
from flask.ext.bootstrap import Bootstrap
from flask.ext.login import LoginManager
#################################

### Local Imports ###

#################################


bootstrap = Bootstrap()
mail = Mail()
db = SQLAlchemy()
lm = LoginManager()
lm.login_view = "/"

def create_app(config_name):
    app = Flask(__name__)
    cfg = os.path.join(os.getcwd(), "{config_folder}", config_name + ".py")
    app.config.from_pyfile(cfg)
    bootstrap.init_app(app)
    db.init_app(app)
    lm.init_app(app)
""".format(config_folder=config_folder)


############################################################



############################################################
#--------------ROUTES __init__.py FILES--------------------#
############################################################


routes_init = lambda: """
from . import * """


############################################################



##########################################################
#------------------PAGE TEMPLATES------------------------#
##########################################################






########################################################


##########################################################
#------------------PAGE TEMPLATES------------------------#
##########################################################


view_imports = lambda app, project_name: """
### Standard Library Imports ###

################################

### 3rd Party Imports ###
from flask import render_template, redirect, url_for
from flask.views import View
################################

### Local Imports ###
from {project_name}.apps.{app} import {app}
from {project_name} import lm
################################

@lm.user_loader
def load_user(user):
  pass

""".format(project_name=project_name, app=app)


class_template = lambda app, page: """
class {view_class}(View):
    def dispatch_request(self):
        return render_template('/{app}/{page}.html')

""".format(view_class="".join(item.capitalize() for item in page.partition("page")),
           app=app, page=page)



add_url_rule_index = lambda app, page: """{app}.add_url_rule('/', view_func={view_class}.as_view('{view_class}'), methods =['GET', 'POST'])
""".format(
  view_class="".join(item.capitalize() for item in page.partition("page")), 
  app=app)

add_url_rule = lambda app, page: """{app}.add_url_rule('/{page}', view_func={view_class}.as_view('{view_class}'), methods =['GET', 'POST'])
""".format(
  view_class="".join(item.capitalize() for item in page.partition("page")),
  app=app,
  page=page)




##########################################################




##########################################################
#-----------------APP INIT PAGE IMPORTS------------------#
##########################################################


app_init_page_imports = lambda app: """    from .apps.{app} import {app}\n""".format(app=app)


########################################################



##########################################################
#---------------APP INIT BLUEPRINT IMPORTS---------------#
##########################################################

blueprint_register = lambda app_name: """    app.register_blueprint({app})\n""".format(app=app_name)

blueprint_register_with_url_prefix = lambda app_name: """    app.register_blueprint({app}, url_prefix = '/{app}')\n""".format(
  app=app_name)

########################################################


##########################################################
#-------------------HTML TEMPLATES-----------------------#
##########################################################


html_template = lambda app_name, folder: """
<!Doctype html>
<html>
  <head>
    <title></title>
    <meta charset='utf-8'>
    <link rel="stylesheet" href="{{{{url_for('static',filename='{app}/css/{css_file}')}}}}">
  </head>
  <body>
    <h1>Hooray it works! this is your {app} {page_name} page </h1>
  </body>
</html>""".format(app=app_name, css_file=folder + ".css", page_name=folder)

###########################################################



##########################################################
#-----------------------MODELS---------------------------#
##########################################################



models = """
### Standard Library Imports ###

################################

### 3rd Party Imports ###
from flask.ext.login import UserMixin
################################

### Local Imports ###

################################


class User(UserMixin):
    def __init__(self, username):
        self.username = username

    def get_id(self):
        return self.username
"""



###########################################################



##########################################################
#-----------------------FORMS---------------------------#
##########################################################

forms = """
### Standard Library Imports ###

################################

### 3rd Party Imports ###
from flask.ext.wtf import Form
from wtforms import TextField, PasswordField, SubmitField, FileField, HiddenField, StringField
################################

### Local Imports ###

################################


class UserForm(Form):
    username = TextField("username")
    password = PasswordField("password")



"""

###########################################################




##########################################################
#---------------------PAGE IMPORTS-----------------------#
##########################################################


import_page = lambda page: """
from .{page} import *""".format(page=page)



###########################################################


##########################################################
#---------------------ADMIN-------------------------#
##########################################################

admin_view = """
from flask import render_template, redirect, url_for
from flask.ext.admin import AdminIndexView, expose
from flask.ext.login import current_user, login_required

class IndexView(AdminIndexView):##A

    @expose('/')
    def index(self):
        pass

"""
admin_model = """
from .admin_forms import UserForm, ProductForm
from flask_admin.contrib.pymongo import ModelView

class UserModel(ModelView):
    column_list = ("user", "password")
    form = UserForm


class ProductModel(ModelView):
    column_list = ("name", "img_path", "category", "price", "quantity")
    form = ProductForm
"""



###########################################################