from . import db
from .basemodel import BaseModel
from werkzeug.security import generate_password_hash


class User(db.Model, BaseModel):
    __tablename__ = "user"
    
    username = db.Column(db.String(80), primary_key=True)
    password = db.Column(db.String(80), default=False)
    
    def __init__(self, username:str, password:str):
        self.username = username
        
        if " " in self.password : 
            raise ValueError("Le nom d'utilisateur ne peut contenir un espace !")
        self.password = generate_password_hash(password=password)
    