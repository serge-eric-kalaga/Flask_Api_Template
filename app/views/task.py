from app.utilities.response import response, responseListModel, responseModel, baseModel

from ..schema.task import task_model, create_task_model

from flask_restx import Resource, Namespace

from app.database.task import Task

from flask import jsonify

from typing import List


task_namespace = Namespace(name="Task", description="Task routes")



task_base_model = baseModel("TaskBaseModel", task_namespace, task_model)

create_task_model_ = baseModel("TaskBaseModel", task_namespace, create_task_model)

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

