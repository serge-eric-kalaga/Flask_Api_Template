from app.utilities.response import response
from ..schema.task import task_model, create_task_model
from flask_restx import fields, Resource, Namespace
from app.database.task import Task

task_namespace = Namespace(name="Task", description="Task routes")

create_task_model_ = task_namespace.model(
    name="CreateTaskModel", 
    model=create_task_model)

task_response_model = task_namespace.model(
    name="TaskListModel",
    model=task_model
)

@task_namespace.route("/", )
class GetCreateTask(Resource):
    
    @task_namespace.marshal_list_with(task_response_model)
    def get(self):
        tasks = Task.getAll()
        return response(data=tasks)
    
    @task_namespace.expect(create_task_model_)
    def post(self):
        data = task_namespace.payload
        task = Task(
            title = data['title'],
            done = data['done']
        )
        task.add()
        
        return response(data=task.to_dict())        