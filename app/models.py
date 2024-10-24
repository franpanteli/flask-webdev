#imports
from . import db
from werkzeug.security import check_password_hash, generate_password_hash

#defining a model (database) for user roles
class Role(db.Model):
    __tablename__ = 'roles'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(64), unique=True)
        #dynamic stops the query from automatically running
    users = db.relationship('User', backref='role', lazy='dynamic')

    def __repr__(self):
        return f"<Role {self.name}>"

class User(db.Model):
    __tablename__ = 'users'
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(64), unique=True, index=True)
    role_id = db.Column(db.Integer, db.ForeignKey('roles.id'))

    #adding password hashing into the database
    password_hash = db.Column(db.String(128))

    @property
    def password(self):
        raise AttributeError('password is not a readable attribute')

    @password.setter
    def password(self, password):
        self.password_hash = generate_password_hash(password)

    def verify_password(self, password):
        return check_password_hash(self.password_hash, password)

    #to add an age collumn to the database
    # age = db.Column(db.Integer)

    def __repr__(self):
        return f"<User {self.username}>"
