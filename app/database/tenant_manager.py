from sqlalchemy import create_engine, text
from sqlalchemy.orm import sessionmaker
from .tenantmodels.models import Task, User
from app.database.tenant import Tenant
from . import TenantBase
# from . import engine, SessionLocal as TenantDBSession

def create_database(db_uri: str):
    """
    Crée une base de données donnée selon son URI
    """
    get_session = create_session(db_uri)
    session = get_session["session"]
    engine = get_session["engine"]
    
    from .tenantmodels import User, Task
    
    TenantBase.metadata.create_all(engine)
    
    
def create_session(tenant_name):
    """Etablir une connexion avec une base de donnees"""
    if tenant_name not in all_tenants() : return None
    engine = create_engine(f"sqlite:///tenants_databases/{tenant_name}.db")        
    Session = sessionmaker(bind=engine)
        
    db_session = Session()
    return {
        "session": db_session,
        "engine": engine
    }


# @simple_cache
def all_tenants():
    """La liste de tous les tenants"""
    tenants = Tenant.query.all()
    return [i.name for i in tenants]