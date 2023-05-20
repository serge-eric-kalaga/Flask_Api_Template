from flask_restx import fields



user_model = {
    "username": fields.String(),
    "password": fields.String()
} 


create_user_model = {
    "username": fields.String(),
    "password": fields.String()
} 
