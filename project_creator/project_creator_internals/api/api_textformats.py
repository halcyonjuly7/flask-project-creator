
"""
this is where all the initial formats of the api endpoints are mad

"""







api_views = lambda api_name, project_name:"""

### Standard Library Imports ###

################################

### 3rd Party Imports ###
from flask import jsonify
from flask_restful import Resource

################################

### Local Imports ###
from . import api
################################

""".format(api_name=api_name,
           project_name=project_name)



api_page_imports = lambda api :"""    from .api.{api} import {api}_api\n""".format(api=api)
api_register_blueprint = lambda api: """    app.register_blueprint({api}_api, url_prefix ='/{api}/api')
""".format(api=api)


class_template = lambda app, page: """
class {view_class}(View):
    def dispatch_request(self):
        return render_template('/{app}/{app}_{page}.html')

""".format(view_class="".join(item.capitalize() for item in page.partition("page")),
           app=app, page=page)

api_template = lambda endpoint: """
class {endpoint}(MethodView):
    def get(self):
        pass

    def post(self):
        pass

    def put(self):
        pass

    def delete(self):
        pass

""".format(endpoint=endpoint)

flask_restful_api_template = lambda endpoint: """
class {endpoint_class}(Resource):
    def get(self):
        pass

    def post(self):
        pass

    def put(self):
        pass

    def delete(self):
        pass
""".format(endpoint_class=endpoint.title())


flask_restful_add_resource = lambda endpoint: """api.add_resource({endpoint_class}, '/{endpoint}')
""".format(endpoint_class=endpoint.title(),
           endpoint=endpoint)

add_url_rule = lambda api, endpoint: """{api}.add_url_rule('/{endpoint}', view_func={endpoint}.as_view('{endpoint}'), methods=['GET', 'POST', "PUT", "DELETE"])
""".format(endpoint="".join(item.capitalize() for item in endpoint.partition("page")),
           api=api)

api_test_format = lambda api, project_name:  """

### Standard Library Imports ###
import unittest
################################


### 3rd Party Imports ###
from flask import url_for
################################


### Local Imports ###
from {project_name} import create_app
################################


class {api}TestCase(unittest.TestCase):
    def setUp(self):
        self.app = create_app("tests_config")
        self.app_context = self.app.app_context()
        self.app_context.push()
        self.client = self.app.test_client(use_cookies=True)

    def tearDown(self):
        self.app_context.pop()
""".format(api=api, project_name=project_name)



api_endpoint_test = lambda app, page: """
    def test_{app}_{page}(self):
            response = self.client.get(url_for("{app}.{page}"))
"""


api_blueprint = lambda blueprint_name: """
### Standard Library Imports ###

################################

### 3rd Party Imports ###
from flask import Blueprint
from flask_restful import Api
################################

### Local Imports ###

################################


{blueprint_name}_api = Blueprint('{blueprint_name}_api', __name__)
api = Api({blueprint_name}_api)
from .views import *

""".format(blueprint_name=blueprint_name)
