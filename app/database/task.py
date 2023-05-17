from . import db

class Task(db.Model):
    __tablename__='devices'
    
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(80), nullable=False)
    done = db.Column(db.Boolean, nullable=False)
    
    def __repr__(self):
        return f'<Task {self.id} {self.title} {self.done}>'
    
    def to_dict(self):
        return {
            'id': self.id,
            'title': self.title,
            'done': self.done
        }
    
    def from_dict(self, data):
        for field in ['title', 'done']:
            if field in data:
                setattr(self, field, data[field])