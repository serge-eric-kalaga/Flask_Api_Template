from flask_restx import fields



user_model = {
    "username": fields.String(),
    "password": fields.String()
} 

create_user_model = {
    "username": fields.String(required=True),
    "password": fields.String(required=True)
} 

update_user_model = {
    "username": fields.String(required=False),
    "password": fields.String(required=False)
} 

login_model = {
    "username": fields.String(required=False),
    "password": fields.String(required=False)
}