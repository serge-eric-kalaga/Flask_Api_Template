from . import db
from .basemodel import BaseModel
from werkzeug.security import generate_password_hash


class User(db.Model, BaseModel):
    __tablename__ = "user"
    
    username = db.Column(db.String(80), primary_key=True)
    password = db.Column(db.String(80), nullable=False)
    
    def __init__(self, username:str, password:str):
        self.username = username
        self.password = generate_password_hash(password=password)
        
        if " " in self.username : 
            raise ValueError("Le nom d'utilisateur ne peut contenir un espace !")
        


class Task(db.Model, BaseModel):
    __tablename__='task'
    
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(80), nullable=False, unique=True)
    done = db.Column(db.Boolean, default=False)
    
    def __repr__(self):
        return f'<Task {self.id} {self.title} {self.done}>'
    
    def to_dict(self):
        return {
            'id': self.id,
            'title': self.title,
            'done': self.done
        }
    