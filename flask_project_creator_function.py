import os




def folders_create(*args,folder_location = None, folder_name = None,config_folder = "config7"):
    """creates a flask project using blueprints and class based views"""
    
    root_folder = os.path.join(folder_location,folder_name)
    main = os.path.join(folder_location,folder_name,"main")
    os.makedirs(root_folder)
    os.makedirs(main)
    with open(os.path.join(root_folder,"run.py"),"w") as run_file:
        run_file.write("""
from {0} import create_app,db
if __name__ == "__main__":
	app = create_app("config")
	with app.app_context():
		db.create_all()
	app.run()""".format(folder_name))
    
    with open(os.path.join(main,"__init__.py"),"w") as init_file:
              for folder in args:
                  init_file.write("""
from . import {0}""".format(folder))

    with open(os.path.join(root_folder,"__init__.py"),"w") as init_file:
        init_file.write("""
from flask import Flask 
from flask.ext.sqlalchemy import SQLAlchemy
from flask.ext.bootstrap import Bootstrap
from flask.ext.login import LoginManager
import os

bootstrap = Bootstrap()
db = SQLAlchemy()
lm = LoginManager()
lm.login_view = "/"
def create_app(config_name):
    app = Flask(__name__)
    cfg = os.path.join(os.getcwd(),"{0}",config_name + ".py")
    app.config.from_pyfile(cfg)
    bootstrap.init_app(app)
    db.init_app(app)
    lm.init_app(app)""".format(config_folder))

        for folder in args:#Done to achieve a desired effect/look on the __init__.py
            init_file.write("""
    from .main.{0} import {0}""".format(folder))
        for folder in args:
            init_file.write("""
    app.register_blueprint({0})""".format(folder))
        init_file.write("""
    return app""")

    for misc_folder in ("static","templates"):
        if misc_folder == "static":
            os.makedirs(os.path.join(root_folder,misc_folder))
            for static_folder in ("css","img","font"):
                os.makedirs(os.path.join(root_folder,misc_folder,static_folder))
        else:
            os.makedirs(os.path.join(root_folder,misc_folder))
            
    for folder in args:
        os.makedirs(os.path.join(main,folder))
        for item in (("static","css"),("templates","html")):
            if "static" in item:
                with open(os.path.join(root_folder,item[0],item[1],folder + "." + item[1]), "w") as html:
                    pass
            else:
                with open(os.path.join(root_folder,item[0],folder + "." + item[1]), "w") as html:
                    html.write("""
<!Doctype html>
<html>
  <head>
    <title></title>
    <meta charset='utf-8'>
    <link href="{{url_for('static',filename='{0}')}}">
  </head>
  <body>
  </body>
</html>""".format(folder + ".css"))

        for file in ("__init__.py","routes.py"):
            with open(os.path.join(main,folder,file),"w") as current_file:
                if file == "__init__.py":
                    current_file.write("""
from flask import Blueprint
{0} = Blueprint('{0}',__name__)
from . import routes""".format(folder))
                    
                else:
                    if not "index" in folder:
                        current_file.write("""
from flask import render_template,redirect,url_for
from flask.views import View
from . import {0}

class {1}(View):
    def dispatch_request(self):
        return render_template('{0}.html')

{0}.add_url_rule('/{2}',view_func = {1}.as_view('{1}'),methods =['GET','POST'])""".format(folder,"".join([i.capitalize()for i in folder.split("_")]),folder.split("_")[0]))
                    else:
                        current_file.write("""
from flask import render_template,redirect,url_for
from flask.views import View
from . import {0}

class {1}(View):
    def dispatch_request(self):
        return render_template('{0}.html')

{0}.add_url_rule('/',view_func = {1}.as_view('{1}'),methods =['GET','POST'])""".format(folder,"".join([i.capitalize()for i in folder.split("_")]),folder.split("_")[0]))


   
    
                        





                    

       
                                       
                                       

