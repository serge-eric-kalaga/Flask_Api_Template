from app.utilities.response import response, responseListModel, responseModel, baseModel
from app.schema.user import user_model, create_user_model
from flask_restx import Resource, fields, Namespace
from werkzeug.exceptions import Conflict
from app.database.user import User


user_namespace = Namespace(name="User", description="User routes")
user_response_model = baseModel("UserModel", user_namespace, user_model)
create_user_response_model = baseModel("UserModel", user_namespace, create_user_model)
user_list_response_model = responseModel("CreateUserModel", user_namespace, user_response_model)


@user_namespace.route("/")
class GetCreateUser(Resource):
    
    @user_namespace.marshal_with(user_list_response_model)
    def get(self):
        """Get all users list"""
        
        users = User.getAll()
        
        return response(data=users)
    
    
    @user_namespace.expect(create_user_response_model)
    def post(self):
        """Create user"""
        
        data = user_namespace.payload
        
        user_exist = User.getOrNone(username=data['username'])
        
        if user_exist :
            raise Conflict(description=f"User with username {data['username']} already exist !")
        
        user = User(**data)
        user.save()
        
        return response(data="User created !")

