# module imports
# %%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
# %%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%

#import Flask
from flask import Flask, render_template, redirect, url_for, session, flash
    # flash is for showing messages to the user
    # in this case after adding forms to the page
import render_template
    #import Bootstrap
from flask_bootstrap import Bootstrap
from flask_sqlalchemy import SQLAlchemy
from config import config

# setting up the instance of the bootstrap application
# %%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
# %%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
# this is a packages file

    #an instance of a bootstrap application
bootstrap = Bootstrap()

        #initialising the database object
db = SQLAlchemy()

def create_app(config_name='default'):
        #an instance of a Flask object
    app = Flask(__name__)

    app.config.from_object(config[config_name])
    config[config_name].init_app(app)

    bootstrap.init_app(app)
    db.init_app(app)

    from .main import main as main_blueprint
    app.register_blueprint(main_blueprint)

    return app

