from . import db
from .basemodel import BaseModel

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