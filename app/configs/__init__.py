import os
from datetime import timedelta


class Config(object):
    DEBUG = True
    SECRET_KEY = '0987654321'
    SQLALCHEMY_DATABASE_URI = "sqlite:///principal_db.db"
    SQLALCHEMY_ECHO = False
    SQLALCHEMY_BINDS = {}
    SQLALCHEMY_TRACK_MODIFICATIONS=False