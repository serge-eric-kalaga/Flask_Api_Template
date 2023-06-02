from . import db
from .basemodel import BaseModel

class Tenant(db.Model, BaseModel):

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)