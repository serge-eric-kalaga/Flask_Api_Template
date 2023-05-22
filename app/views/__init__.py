from flask_restx import Api, fields, Namespace
from werkzeug.exceptions import NotFound, InternalServerError, Unauthorized, BadRequest, Conflict
from flask_jwt_extended.exceptions import NoAuthorizationError
from jwt.exceptions import ExpiredSignatureError
from sqlalchemy.exc import IntegrityError


authorizations = {
        "Bearer Auth":
        {
            'type':"apiKey",
            'in':'header',
            'name':'Authorization',
            'description':'Add a JWT with a ** Bearer **\n add Bearer before adding the token'
        }
}

api = Api(title="Base Api Flask Template", authorizations=authorizations, security='Bearer Auth')

from .task import task_namespace
from .auth.user import user_namespace
from .auth.auth import auth_namespace


api.add_namespace(task_namespace, path="/task")
api.add_namespace(user_namespace, path="/user")
api.add_namespace(auth_namespace, path="/auth")


# Exceptions handling

error_model = api.model("error_model", 
{
    "status":fields.Boolean(),
    "status_code":fields.Integer(),
    "message":fields.String()
})


@api.errorhandler(NotFound)
@api.marshal_with(error_model)
def notFound(error):
    return {"status":False, "status_code": 404, "message":f"{error}"}

@api.errorhandler(InternalServerError)
@api.marshal_with(error_model)
def internalError(error):
    return {"status":False, "status_code": 500, "message":f"{error}"}
    
@api.errorhandler(NoAuthorizationError)
@api.marshal_with(error_model)
def noauthorization(error):
    return {'status':False, "status_code": 401, 'message':'missing JWT identification error'}

@api.errorhandler(ExpiredSignatureError)
@api.marshal_with(error_model)
def expiredSignature(error):
    return {'status':False, "status_code": 401, 'message': 'JWT signature Expired'}

@api.errorhandler(Unauthorized)
@api.marshal_with(error_model)
def unAuthorizedAccess(error):
    return {"status":False, "status_code": 401, "message":f"{error}"}

@api.errorhandler(BadRequest)
@api.marshal_with(error_model)
def badRequest(error):
    return {"status":False, "status_code": 400, "message":f"{error}"}

@api.errorhandler(IntegrityError)
@api.marshal_with(error_model)
def integrityError(error):
    return {"status":False, "status_code": 400,  "message":f"{error}"}

@api.errorhandler(Conflict)
@api.marshal_with(error_model)
def conflict(error):
    return {"status":False, "status_code": 409,  "message":f"{error}"}

@api.errorhandler(ValueError)
@api.marshal_with(error_model)
def valueError(error):
    return {"status":False, "status_code": 400,  "message":f"{error}"}