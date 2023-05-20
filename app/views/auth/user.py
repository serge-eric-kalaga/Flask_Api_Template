from app.utilities.response import response, responseListModel, responseModel, baseModel
from app.schema.user import user_model, create_user_model
from flask_restx import Resource, fields, Namespace
from app.database.user import User


user_namespace = Namespace(name="User", description="User routes")
user_response_model = baseModel("UserModel", user_namespace, user_model)
user_list_response_model = responseModel("CreateUserModel", user_namespace, user_response_model)


@user_namespace.route("/")
class GetCreateUser(Resource):
    
    @user_namespace.marshal_with(user_list_response_model)
    def get(self):
        """Get all users list"""
        
        users = User.getAll()
        
        return response(data=users)

