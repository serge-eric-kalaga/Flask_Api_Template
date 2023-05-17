from flask_restx import Api

api = Api(title="Hello world")

from .hello import hello_namespace

api.add_namespace(hello_namespace, path="/hello")