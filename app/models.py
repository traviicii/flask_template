from . import db

# this is where we can create the skeleton for our database structure i.e, tables and relationships

class Task(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    title = db.Column(db.String, nullable= False)
    description = db.Column(db.String, nullable = False)
    completed = db.Column(db.Boolean, nullable = True, default = False)

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        
    def save(self):
        db.session.add(self)
        db.session.commit()