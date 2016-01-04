### CONFIGURATION FILE ##################################
from functools import partial

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



#------------------------------#

###############################
######    SQLALCHEMY ##########
###############################


SQALCHEMY_DATABASE_URI = "sqlite:/// + os.path.join(os.path.dirname(__file__), ../data-dev.sqlite3 "


###############################

#------------------------------#

################################
#######  FlASK-MAIL  ###########
################################

MAIL_SERVER = 'smtp.gmail.com'
MAIL_PORT = 587
MAIL_USE_TLS = True
MAIL_USE_SSL = False
MAIL_USERNAME = 'your username here'
MAIL_PASSWORD = 'your password here'

##################################


################################
##########  CELERY  ############
################################

CELERY_BROKER_URL = "redis://localhost:6379/0"
CELERY_RESULT_BACKEND = "redis://localhost:6379/0"


################################

################################
########## SECURITY  ###########
################################

SECRET_KEY = "secret123456"
SECURITY_PASSWORD_SALT = "securitysalt1234"

################################
"""

############################################################



#########################################################
#--------------------RUN PYFILE-------------------------#
#########################################################


run_pyfile = lambda project_name: """
### Standard Library Imports ###

################################

### 3rd Party Imports ###
from flask.ext.admin import Admin
#################################

### Local Imports ###
from {project_name} import create_app, db
from {project_name}.misc_files.socketio import socketio
from {project_name}.apps.admin.admin_views import IndexView
from register_helpers.admin_register import register_admin_views
#################################

if __name__ == "__main__":
    app = create_app("developement_config")
    admin = Admin(app, index_view=IndexView())
    with app.app_context():
        db.create_all()
        register_admin_views(admin)
    socketio.run(app)""".format(project_name=project_name)


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
from celery import Celery
################################

### 3rd Party Imports ###
from flask import Flask 
from flask_mail import Mail
from flask.ext.sqlalchemy import SQLAlchemy
from flask.ext.bootstrap import Bootstrap
from flask.ext.login import LoginManager
from flask.ext.socketio import SocketIO
from flask_restful import Api
#################################

### Local Imports ###

#################################


bootstrap = Bootstrap()
mail = Mail()
db = SQLAlchemy()
celery = Celery(__name__, broker="redis://localhost:6379/0")
socketio = SocketIO()
api = Api()
lm = LoginManager()
lm.login_view = "/"

def create_app(config_name):
    app = Flask(__name__)
    cfg = os.path.join(os.getcwd(), "{config_folder}", config_name + ".py")
    app.config.from_pyfile(cfg)
    mail.init_app(app)
    bootstrap.init_app(app)
    celery.conf.update(app.config)
    socketio.init_app(app, async_mode='eventlet')
    api.init_app(app)
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
#------------------BASE TEMPLATE-------------------------#
##########################################################

base_template = lambda app_name, folder: """
<!Doctype html>
<html>
  <head>
    <title></title>
    <meta charset='utf-8'>
    <link rel="stylesheet" href="{{{{url_for('static',filename='{app}/css/{app}_{css_file}')}}}}">
  </head>
  <body>
    <h1>Hooray it works! this is your {app} {page_name} base_template</h1>
  </body>
</html>""".format(app=app_name, css_file=folder + ".css", page_name=folder)




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
        return render_template('/{app}/{app}_{page}.html')

""".format(view_class="".join(item.capitalize() for item in page.partition("page")),
           app=app, page=page)



add_url_rule_index = lambda app, page: """{app}.add_url_rule('/', view_func={view_class}.as_view('{view_class}'), methods=['GET', 'POST'])
""".format(
  view_class="".join(item.capitalize() for item in page.partition("page")), 
  app=app)

add_url_rule = lambda app, page: """{app}.add_url_rule('/{page}', view_func={view_class}.as_view('{view_class}'), methods=['GET', 'POST'])
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

blueprint_register_with_url_prefix = lambda app_name: """    app.register_blueprint({app}, url_prefix ='/{app}')\n""".format(
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
    <link rel="stylesheet" href="{{{{url_for('static',filename='{app}/css/{app}_{css_file}')}}}}">
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
from wtforms import (TextField,
                    PasswordField,
                    SubmitField,
                    FileField,
                    HiddenField,
                    StringField,
                    TextAreaField)
from wtforms.widgets import TextArea
from wtforms.validators import Required
################################

### Local Imports ###

################################

class CKTextAreaWidget(TextArea):
    def __call__(self, field, **kwargs):
        if kwargs.get('class'):
            kwargs['class'] += ' ckeditor'
        else:
            kwargs.setdefault('class', 'ckeditor')
        return super().__call__(field, **kwargs)


class CKTextAreaField(TextAreaField):
    widget = CKTextAreaWidget()

class UserForm(Form):
    username = TextField("username")
    password = PasswordField("password")
    role = StringField("role")



"""


###########################################################




##########################################################
#---------------------PAGE IMPORTS-----------------------#
##########################################################


import_page = lambda page: """
from .{page} import *""".format(page=page)


###########################################################


##########################################################
#------------------------ADMIN---------------------------#
##########################################################

admin_view = """
### Standard Library Imports ###

################################


### 3rd Party Imports ###
from flask import render_template, redirect, url_for, request
from flask.ext.admin import AdminIndexView, expose
from flask.ext.login import current_user, login_required
from flask.views import MethodView
################################


### Local Imports ###

################################


class IndexView(AdminIndexView):##A

    @expose('/')
    def index(self):
        return super().index()

    @expose('/login', methods=["GET", "POST"])
    def login(self):
        if request.method == "GET":
            return self.render("/admin_templates/admin_login.html")

        if request.method == "POST":
            pass

    @expose('/logout', methods=["GET", "POST"])
    def logout(self):
        pass

"""
admin_model = """

### Standard Library Imports ###

################################


### 3rd Party Imports ###
from flask_admin.contrib.pymongo import ModelView
################################


### Local Imports ###
from .admin_forms import UserForm
################################


class UserModel(ModelView):
    column_list = ("user", "password", "role")
    form = UserForm



"""

admin_forms = """
### Standard Library Imports ###

################################

### 3rd Party Imports ###
from flask.ext.wtf import Form
from wtforms import (TextField,
                     PasswordField,
                     SubmitField,
                     FileField,
                     HiddenField,
                     StringField,
                     TextAreaField)
from wtforms.widgets import TextArea
from wtforms.validators import Required
################################

### Local Imports ###

################################

class CKTextAreaWidget(TextArea):
    def __call__(self, field, **kwargs):
        if kwargs.get('class'):
            kwargs['class'] += ' ckeditor'
        else:
            kwargs.setdefault('class', 'ckeditor')
        return super().__call__(field, **kwargs)


class CKTextAreaField(TextAreaField):
    widget = CKTextAreaWidget()

class UserForm(Form):
    username = TextField("username")
    password = PasswordField("password")
    role = StringField("role")



"""


admin_tests = lambda project_name: """

import unittest
from {project_name} import create_app
from flask import url_for


class AdminTestCase(unittest.TestCase):
    def setUp(self):
        self.app = create_app("tests_config")
        self.app_context = self.app.app_context()
        self.app_context.push()
        self.client = self.app.test_client(use_cookies=True)

    def tearDown(self):
        self.app_context.pop()

""".format(project_name=project_name)






###########################################################

###########################################################
#-----------------------HELPER FUNCTIONS------------------#
###########################################################

misc_functions = lambda project_name : """

### Standard Library Imports ###
from functools import wraps
################################


### 3rd Party Imports ###
from werkzeug.security import check_password_hash, generate_password_hash
from werkzeug.security import check_password_hash, generate_password_hash
from flask import url_for, redirect, render_template, flash
from itsdangerous import URLSafeTimedSerializer
from flask.ext.login import current_user
from flask.ext.mail import Message
################################


### Local Imports ###
from {project_name} import mail
from config.developement_config  import SECRET_KEY, SECURITY_PASSWORD_SALT, MAIL_USERNAME
################################

def check_password(password_hash, password):
    return check_password_hash(password_hash, password)

def generate_password(password):
    return generate_password_hash(password)

def generate_confirmation_token(email):
    serializer = URLSafeTimedSerializer(SECRET_KEY)
    return serializer.dumps(email, salt=SECURITY_PASSWORD_SALT)

def confirm_token(token, expiration=3600):
    serializer = URLSafeTimedSerializer(SECRET_KEY)
    try:
        email = serializer.loads(
            token,
            salt=SECURITY_PASSWORD_SALT,
            max_age=expiration
        )
        return email
    except:
        return False

def generate_token_and_send_mail(email, route=None, template=None):
    token = generate_confirmation_token(email)
    url = url_for(route, token=token, _external=True)
    html = render_template(template, url=url)
    subject = "Please confirm your email"
    send_email(email, subject, html)

def send_email(to, subject, template):
    msg = Message(
        subject,
        recipients=[to],
        html=template,
        sender=MAIL_USERNAME
    )
    mail.send(msg)

def protect_admin_index_view(view):
    def wrap(*args, **kwargs):
        try:
            if "admin" in current_user.role:
                return view(*args, **kwargs)
            else:
                return redirect(url_for('admin.login'))
        except:
            return redirect(url_for('admin.login'))
    return wrap

def check_confirmation(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        if not current_user.confirmed:
            flash("Please confirm your account")
            return redirect(url_for("main.unconfirmed"))
        else:
            return func(*args, **kwargs)
    return wrapper

""".format(project_name=project_name)
###########################################################

###########################################################
#------------------WTFORM RENDER FIELD--------------------#
###########################################################


wtform_render_field_and_flash_message = """
{% macro render_field(field) %}
  <dt>{{ field.label }}
  <dd>{{ field(**kwargs)|safe }}
  {% if field.errors %}
    <ul class=errors>
    {% for error in field.errors %}
      <li>{{ error }}</li>
    {% endfor %}
    </ul>
  {% endif %}
  </dd>
{% endmacro %}


{% with messages = get_flashed_messages() %}
  {% if messages %}
    <ul class=flashes>
    {% for message in messages %}
      <li>{{ message }}</li>
    {% endfor %}
    </ul>
  {% endif %}
{% endwith %}

"""
###########################################################

###########################################################
#-------------------STATIC FILE---------------------------#
###########################################################

html_file = lambda app_name=None, page=None, file_type="html": \
  """{app_name}_{page}.{file_type}""".format(app_name=app_name,
                                             page=page,
                                             file_type=file_type)
css_file = partial(html_file, file_type="css")

###########################################################

###########################################################
#--------------------CELERY WORKER------------------------#
###########################################################
celery_worker = lambda project_name: """
### Standard Library Imports ###

################################


### 3rd Party Imports ###

################################


### Local Imports ###

from {project_name} import celery, create_app

################################


app = create_app("developement_config")
app.app_context().push()
""".format(project_name=project_name)


celery_task = lambda project_name: """
### Standard Library Imports ###

################################


### 3rd Party Imports ###


################################


### Local Imports ###

from {project_name} import celery

################################


@celery.task
def sample_task():
    print("hi")
    return "hi"
""".format(project_name=project_name)
############################################################

###########################################################
#--------------------SOCKET-IO----------------------------#
###########################################################


socket_io = lambda project_name:"""
### Standard Library Imports ###

################################


### 3rd Party Imports ###
from flask_socketio import send, emit
################################


### Local Imports ###
from {project_name} import socketio
################################


@socketio.on("my_test")
def handle_message(message):
    emit("testing", {{"data": "hekko"}})
""".format(project_name=project_name)



############################################################
#--------------------------Tests---------------------------#
############################################################




tests_format = lambda app, project_name:  """

### Standard Library Imports ###
import unittest
################################


### 3rd Party Imports ###
from flask import url_for
################################


### Local Imports ###
from {project_name} import create_app
################################


class {app}TestCase(unittest.TestCase):
    def setUp(self):
        self.app = create_app("tests_config")
        self.app_context = self.app.app_context()
        self.app_context.push()
        self.client = self.app.test_client(use_cookies=True)

    def tearDown(self):
        self.app_context.pop()

""".format(app=app, project_name=project_name)


page_tests = lambda app, page: """
    def test_{app}_{page}(self):
            response = self.client.get(url_for("{app}.{page}"))

""".format(app=app, page=page.title())


test_bottom = """

if __name__ == '__main__':
    unittest.main()
"""

###########################################################

###########################################################
#################### Function Based View ##################

function_template = lambda app, page: """

@{app}.route('/{page}', methods=['GET', 'POST'])
def {page}():
    return render_template('/{app}_templates/{app}_{page}.html')
""".format(app=app, page=page)

function_template_index = lambda app, page: """

@{app}.route('/', methods=['GET', 'POST'])
def {page}():
    return render_template('/{app}_templates/{app}_{page}.html')
""".format(app=app, page=page)
###########################################################


register_admin_views = lambda project_name: """
### Standard Library Imports ###

################################


### 3rd Party Imports ###

################################


### Local Imports ###
from {project_name}.apps.admin.admin_models import UserModel # import your models here
################################


def register_admin_views(admin):
    pass
""".format(project_name=project_name)

