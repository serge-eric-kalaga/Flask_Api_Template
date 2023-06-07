from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import create_engine
from sqlalchemy.orm import declarative_base
from sqlalchemy.orm import sessionmaker, Session
from app.configs import Config



# engine = create_engine(SQLALCHEMY_DATABASE_URL, connect_args={"check_same_thread":False}) # sqlite
# engine = create_engine(Config.SQLALCHEMY_DATABASE_URI, pool_pre_ping=True) #mysql

# SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

TenantBase = declarative_base()

from .tenantmodels import *


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


# def get_test_db():
#     db = SessionLocal()
#     try:
#         yield db
#     finally:
#         db.close()
#         db.rollback()
        

db = SQLAlchemy()

# from .models import User, Task
from .tenant import Tenant

