# from . import  Base
from . import db
from .basemodel import BaseModel
from sqlalchemy import Integer, String, Column

class Tenant(db.Model, BaseModel):
    __tablename__ = "tenant"

    id = Column(Integer, primary_key=True)
    name = Column(String(100), nullable=False)