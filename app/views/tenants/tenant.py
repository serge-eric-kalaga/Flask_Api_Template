from flask_restx import Resource, Namespace
from app.schema.tenant import tenant_model, create_tenant_model
from app.utilities.response import response, validationModel, responseModel
from flask_jwt_extended import create_access_token, create_refresh_token, \
    get_jwt_identity, jwt_required
from werkzeug.security import check_password_hash
from werkzeug.exceptions import Unauthorized
from app.database.tenant import Tenant


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