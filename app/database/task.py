from . import db

class Task(db.Model):
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
                
    @classmethod
    def get(cls, username):
        if id=="" or id==None :
            raise NotFound()
        return cls.query.filter_by(username=username).first_or_404("Account Not Found")
    
    @classmethod
    def delete(cls, username):
        user = cls.get(username)
        db.session.delete(user)
        db.session.commit()
        # return user
    
    @classmethod
    def getAll(cls):
        return cls.query.all()
    
    def add(self):
        db.session.add(self)
        db.session.commit()