import os
from datetime import timedelta
from flask import session





class Config(object):
    DEBUG = True
    SECRET_KEY = '0987654321'
    SQLALCHEMY_DATABASE_URI = "sqlite:///principal_db.db"
    TENANT_DATABASE_URI = "sqlite:///{}.db"
    SQLALCHEMY_ECHO = False
    PERMANENT_SESSION_LIFETIME = timedelta(days=365)
    SQLALCHEMY_BINDS = {
        # 'tenant1': 'sqlite:///tenant1.db',
    }
    # SQLALCHEMY_ENGINE_OPTIONS = {
    #     'pool_pre_ping': True
    # }
    SQLALCHEMY_TRACK_MODIFICATIONS=False