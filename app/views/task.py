from app.utilities.response import response, responseListModel, responseModel
from ..schema.task import task_model, create_task_model
from flask_restx import fields, Resource, Namespace
from app.database.task import Task
from flask import jsonify
from typing import List

task_namespace = Namespace(name="Task", description="Task routes")



create_task_model_ = responseModel("CreateTaskModel", task_namespace, create_task_model)

task_response_model = responseModel("TaskModel", task_namespace, task_model)

task_list_response_model = responseListModel("TaskListModel", task_namespace, task_model)


@task_namespace.route("/", )
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