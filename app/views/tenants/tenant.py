from flask_restx import Resource, Namespace
from app.schema.tenant import tenant_model, create_tenant_model
from app.utilities.response import response, validationModel, responseModel
from flask_jwt_extended import create_access_token, create_refresh_token, \
    get_jwt_identity, jwt_required
from werkzeug.security import check_password_hash
from werkzeug.exceptions import Unauthorized
from app.database.tenant import Tenant
from werkzeug.exceptions import Conflict
from werkzeug.exceptions import InternalServerError
from app.database.tenant_manager import all_tenants, create_database, create_session
from flask import current_app


tenant_namespace = Namespace("Tenant", description="Tenant routes")
create_tenant_model = validationModel("CreateTenantModel", tenant_namespace, create_tenant_model)
tenant_model = validationModel("TenantModel", tenant_namespace, tenant_model)
tenant_list_model = responseModel("TenantListModel", tenant_namespace, tenant_model)


@tenant_namespace.route("/")
class CreateGetTenant(Resource):
    
    @tenant_namespace.marshal_list_with(tenant_list_model)
    def get(self):
        """Get all tenants"""
        
        tenants = Tenant.getAll()
        return response(data=tenants)
    
    @tenant_namespace.expect(create_tenant_model)
    def post(self):
        """Create a new tenant"""
        data = tenant_namespace.payload
        tenant_exist = Tenant.getOrNone(name=data['name'])
        if tenant_exist is not None :
            raise Conflict("Ce tenant exist deja !")
        
        
        create_database(data['name'])
        
        
        try:
            create_database(data['name'])
        except Exception as e:
            raise InternalServerError(f"Erreur lors de la création de la base de données : {str(e)}")
        
        new_tenant = Tenant(**data)
        new_tenant.save()
        
        return response(data="Tenant Created")