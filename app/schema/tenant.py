from flask_restx import fields



tenant_model = {
    "id": fields.Integer(),
    "name": fields.String(),
} 


create_tenant_model = {
    "name": fields.String(required=True),
} 


