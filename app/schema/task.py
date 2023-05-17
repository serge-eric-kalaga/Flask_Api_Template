from flask_restx import fields

task_model = {
    "id": fields.Integer(),
    "title": fields.String(),
    "done": fields.Boolean()
} 