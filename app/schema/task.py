from marshmallow import Schema, fields

task_model = {
    "id": fields.Integer(),
    "title": fields.String(),
    "done": fields.Boolean()
} 


create_task_model = {
    "title": fields.String(required=True),
    "done": fields.Boolean(default=False)
} 


