from werkzeug.exceptions import NotFound
from . import db

class BaseModel():
    '''
        BaseModel which contain all used functions
    '''
    def save(self):
        '''
            save instance in the database
        '''
        db.session.add(self)
        db.session.commit()
        return True

    @classmethod
    def getOr404(cls, error="data not found", **kwargs):
        '''
            get one data, depends on the parameters
        '''
        data:cls = cls.query.filter_by(**kwargs).first()
        
        if data is None : raise NotFound(description=f"{cls.__name__} not found !")
        
        return data

    @classmethod
    def getOrNone(cls, **kwargs):
        '''
            get one data, depends on the parameters
        '''
        data:cls = cls.query.filter_by(**kwargs).first()
        
        return data
    
    @classmethod
    def getAllFilterBy(cls, **kwargs):
        """
            get Many data, depends on the parameters
        """
        all_data:list[cls] = cls.query.filter_by(**kwargs).all()
        return all_data
    
    @classmethod
    def getAll(cls):
        """
            get Many data
        """
        return cls.query.all()
        
    
    def delete(self):
        """Delete instance from the database"""
        
        db.session.delete(self)
        db.session.commit()
        return True
    
    
    @classmethod
    def add(cls,**kwargs):
        ''' 
            directly create and add in the database
        '''
        unite = cls(**kwargs)
        db.session.add(unite)
        db.session.commit()
        return unite
    
    