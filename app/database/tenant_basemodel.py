from werkzeug.exceptions import HTTPException
from sqlalchemy.orm import Session

class TenantsBaseModel():

    @classmethod
    def get(cls, db, **kwargs):
        result = db.query(cls).filter_by(**kwargs).first()
        db.close()
        if result == None:
            raise HTTPException(status_code=404, detail=f"{cls.__name__} not found")
        return result
    
    @classmethod
    def getOrNone(cls, db, **kwargs):
        result = db.query(cls).filter_by(**kwargs).first()
        db.close()
        return result
    
    @classmethod
    def getAll(cls, db) :
        data = db.query(cls).all()
        db.close()
        return data
    
    @classmethod
    def getAllFilterBy(cls,db, **kwargs) :
        data = db.query(cls).filter_by(**kwargs).all()
        db.close()
        return data

    def commit(self, db):
        db.commit()
        db.close()
        return self
    
    # def save(self, db):
    #     db.add(self)
    #     db.refresh(self)
    #     db.close()
    #     return self
    
    def save(self, db):
        db.add(self)
        db.commit()
        db.refresh(self)
        db.close()
        return self
    
    def delete(self, db) :
        db.delete(self)
        db.commit()
        db.close()
        return self
    
    def deleteWithCommit(self, db) :
        db.delete(self)
        db.close()
        return self
    
    @classmethod
    def getItemNumber(cls, db) :
        count = db.query(cls).count()
        db.close() 
        return count