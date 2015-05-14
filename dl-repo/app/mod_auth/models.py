# Import the db object from the main application module

from app import db

# Define a base model for other database tables to inherit
class Base(db.Model):

    __abstract__ = True

    id            = db.Column(db.Integer, primary_key=True)
    date_created  = db.Column(db.DateTime, default=db.func.current_timestamp()),
    date_modified = db.Column(db.DateTime, default=db.func.current_timestamp(),
            onupdate=db.func.current_timestamp())

# Define a user model
class User(Base):

    __tablename__ = 'auth_user'

    # User name
    name = db.Column(db.String(128), nullable=False)
 
    # Id data
    email = db.Column(db.String(128), nullable=False, 
            unique=True)
    password = db.Column(db.String(192), nullable=False)

    # Authorization: role & status
    role = db.Column(db.SmallInteger, nullable=False)
    status = db.Column(db.SmallInteger, nullable=False)

    # New instance instantiation procedure
    def __init__(self, name, email, password):
        self.name = name
        self.email = email
        self.password = password

    def __repr__(self):
        return '<User %r>' % (self.name)
    
