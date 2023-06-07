# from . import  Base
from .. import TenantBase
from werkzeug.security import generate_password_hash
from sqlalchemy import String, Integer, Boolean, Column
from ..tenant_basemodel import TenantsBaseModel


class User(TenantsBaseModel, TenantBase):
    __tablename__ = "user"
    
    username = Column(String(80), primary_key=True)
    password = Column(String(80), nullable=False)
    
    def __init__(self, username:str, password:str):
        self.username = username
        self.password = generate_password_hash(password=password)
        
        if " " in self.username : 
            raise ValueError("Le nom d'utilisateur ne peut contenir un espace !")
        


class Task(TenantsBaseModel, TenantBase):
    __tablename__='task'
    
    id = Column(Integer, primary_key=True)
    title = Column(String(80), nullable=False, unique=True)
    done = Column(Boolean, default=False)
    
    def __repr__(self):
        return f'<Task {self.id} {self.title} {self.done}>'
    
    def to_dict(self):
        return {
            'id': self.id,
            'title': self.title,
            'done': self.done
        }
    