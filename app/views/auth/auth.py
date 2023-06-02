from flask_restx import Resource, Namespace
from app.schema.user import login_model
from app.utilities.response import response, validationModel
from flask_jwt_extended import create_access_token, create_refresh_token, \
    get_jwt_identity, jwt_required
from werkzeug.security import check_password_hash
from werkzeug.exceptions import Unauthorized
from app.database.models import User, Task


auth_namespace = Namespace("Auth", description="Auth routes")
login_validation_model = validationModel("LoginModel", auth_namespace, login_model)

@auth_namespace.route("/login")
class Auth(Resource):
    
    @auth_namespace.expect(login_validation_model)
    def post(self):
        """User authentication"""
        
        data = auth_namespace.payload
        
        if not data.get("username") or not data.get("password"):
            raise ValueError("Username/password is required !")
        
        user_exist = User.getOrNone(username=data['username'])
        
        if user_exist is None or \
             not check_password_hash(user_exist.password, data.get('password')) :
                raise Unauthorized(description="Incorrect username/password !")
        
        token = create_access_token({"username":user_exist.username})
        
        return response(data={
            "username" : user_exist.username,
            "token" : token
        })
        
     

@auth_namespace.route("/current-user")
class AuthUserIdentity(Resource):
       
    @jwt_required()
    def get(self):
        """Actual user identity"""
        
        username = get_jwt_identity()
        
        return response(data=username)
            
        
        
        
        