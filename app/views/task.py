from app.utilities.response import response, responseListModel, responseModel, validationModel
from ..schema.task import task_model, create_task_model
from flask_restx import Resource, Namespace
from app.database.models import Task

from flask import jsonify

from typing import List



task_namespace = Namespace(name="Task", description="Task routes")


task_base_model = validationModel("TaskBaseModel", task_namespace, task_model)
create_task_model_ = validationModel("TaskBaseModel", task_namespace, create_task_model)
task_response_model = responseModel(name="task_response_mode", namespace=task_namespace, dataModel=task_base_model)
task_list_response_model = responseListModel(name="task_list_response_model", namespace=task_namespace, dataModel=task_base_model)


@task_namespace.route("/")
class GetCreateTask(Resource):
    
    @task_namespace.marshal_list_with(task_list_response_model)
    def get(self):
        """Get all tasks"""

        tasks = Task.getAll()
        return response(data=tasks)
    
    
    @task_namespace.expect(create_task_model_)
    def post(self):
        """Create a new task"""
    
        data = task_namespace.payload
        task = Task(

            title = data['title'],

            done = data['done']
        )

        task.save()

        return response(data=task.to_dict())  
    
      



@task_namespace.route("/<int:id_task>")
class ShowUpdateDeleteTask(Resource):
    
    def get(self, id_task:int):
        """Get a task by id"""

        task = Task.getOr404(id=id_task)
        return response(data=task.to_dict())

    def delete(self, id_task:int):
        """Delete a task by id"""

        task = Task.getOr404(id=id_task)
        task.delete()
        return response(data=f"Task {id_task} deleted !")
    

    @task_namespace.expect(create_task_model_)
    def put(self, id_task:int):
        """Update a task by id"""

        task = Task.getOr404(id=id_task)
        data = task_namespace.payload
        task.title = data['title'] if data['title'] else None
        task.done = data['done'] if data['done'] else None
        task.save()
        
        return response(data=f"Task {id_task} updated !")

