from flask_restx import Api

api = Api(title="Hello world")

from .hello import hello_namespace
from .task import task_namespace

api.add_namespace(hello_namespace, path="/hello")
api.add_namespace(task_namespace, path="/task")