from app.utilities.response import response, responseListModel, responseModel, validationModel
from app.schema.user import user_model, create_user_model, update_user_model
from flask_restx import Resource, fields, Namespace
from werkzeug.exceptions import Conflict
from app.database.user import User


user_namespace = Namespace(name="User", description="User routes")

user_response_model = validationModel("user_response_model", user_namespace, user_model)
create_user_validation_model = validationModel("create_user_validation_model", user_namespace, create_user_model)
update_user_validation_model = validationModel("update_user_validation_model", user_namespace, update_user_model)
user_marshal_model = responseModel("user_marshal_model", user_namespace, user_response_model)
user_list_marshal_model = responseListModel("user_list_marshal_model", user_namespace, user_response_model)


@user_namespace.route("/")
class GetCreateUser(Resource):
    
    @user_namespace.marshal_with(user_list_marshal_model)
    def get(self):
        """Get all users list"""

        users = User.getAll()
        return response(data=users)


    @user_namespace.expect(create_user_validation_model)
    def post(self):
        """Create user"""

        data = user_namespace.payload
        user_exist = User.getOrNone(username=data['username'])

        if user_exist :
            raise Conflict(description=f"User with username {data['username']} already exist !")

        user = User(**data)
        user.save()
        return response(data="User created !")


@user_namespace.route("/<string:username>")    
class ShowDeleteUpdateUser(Resource):

    @user_namespace.marshal_with(user_marshal_model)
    def get(self, username:str) :
        """Get user details"""

        user = User.getOr404(username=username)
        return response(data=user)
    
    
    def delete(self, username):
        """Delete user"""
        
        user = User.getOr404(username=username)
        user.delete()
        
        return response(data="User deleted !")
    
    
    @user_namespace.expect(update_user_validation_model)
    def put(self, username):
        """Update user"""
        
        data = user_namespace.payload
        user = User.getOr404(username=username)
        
        user.username = data.get('username')
        user.password = data.get('password')
        user.save()
        
        return response(data=f"User {username} updated")
    
    

        
