from flask_restx import fields, Resource, Namespace
from app.database.task import Task
from ..schema.task import task_model
from app.utilities.response import response, responseListModel, responseModel

task_namespace = Namespace(name="Task", description="Task routes")

task_list_response_model = responseListModel(name="TaskListModel", namespace=task_namespace, dataModel=task_model)

@task_namespace.route("/", )
class GetCreateTask(Resource):
    
    # @task_namespace.marshal_list_with(task_list_response_model)
    def get(self):
        tasks = Task.query.all()
        return response(data=tasks)
        