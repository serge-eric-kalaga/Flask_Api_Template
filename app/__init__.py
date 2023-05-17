from flask import Flask
from flask_restx import Api
from .views import api


def start_app():
    
    app = Flask(__name__)
    
    api.init_app(app)
    
    return app
    
    
