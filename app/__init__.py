from flask import Flask
from flask_restx import Api
from .views import api
from app.database import db
from app.configs import Config
from flask_jwt_extended import JWTManager


def start_app():
    
    app = Flask(__name__)
    
    app.config.from_object(Config)
    
    api.init_app(app)
    
    db.init_app(app) 
    
    jwt = JWTManager(app=app)
    
    with app.app_context():
        db.create_all()   
    
    return app
    
    
