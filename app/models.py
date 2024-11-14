#imports
from . import db
from flask_login import UserMixin
from werkzeug.security import check_password_hash, generate_password_hash
from flask_login import LoginManager
from . import db, login_manager
from flask_login import login_required

#defining a model (database) for user roles
class Role(db.Model):
    __tablename__ = 'roles'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(64), unique=True)
        #dynamic stops the query from automatically running
    users = db.relationship('User', backref='role', lazy='dynamic')

    def __repr__(self):
        return f"<Role {self.name}>"

class User(UserMixin, db.Model):
    __tablename__ = 'users'
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(64), unique=True, index=True)
    role_id = db.Column(db.Integer, db.ForeignKey('roles.id'))

    #adding password hashing into the database
    password_hash = db.Column(db.String(128))
    email = db.Column(db.String(64), unique=True, index=True)

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

# This is a later version of this file contents (after exercise 12.5)
# %%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%

# from flask import Flask
# from flask_bootstrap import Bootstrap
# from flask_sqlalchemy import SQLAlchemy
# from flask_migrate import Migrate
# from flask_login import LoginManager
# from config import config
# from yourapp import User

# bootstrap = Bootstrap()
# db = SQLAlchemy()
# migrate = Migrate()
# login_manager = LoginManager()
# login_manager.login_view = 'auth.login'

# def create_app(config_name='default'):
#     app = Flask(__name__)

#     # Load configuration
#     app.config.from_object(config[config_name])
#     config[config_name].init_app(app)

#     # Initialise extensions
#     bootstrap.init_app(app)
#     db.init_app(app)
#     migrate.init_app(app, db, render_as_batch=True)
#     login_manager.init_app(app)

#     # Register blueprints
#     from main import main as main_blueprint
#     app.register_blueprint(main_blueprint)

#     from auth import auth as auth_blueprint
#     app.register_blueprint(auth_blueprint)

#     return app

# login_manager = LoginManager()

# @login_manager.user_loader
# def load_user(user_id):
#     return User.query.get(int(user_id))

@app.route('/top-secret')
@login_required
def top_secret():
    return "Welcome, VIP member!"

