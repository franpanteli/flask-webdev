#module import
#%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
#import Flask
from flask import Flask, render_template, redirect, url_for, session, flash
    # flash is for showing messages to the user
    # in this case after adding forms to the page
import render_template
    #import Bootstrap
from flask_bootstrap import Bootstrap

    #importing the base class for creating forms
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired
    #for SQLAlchemy
import os
from flask_sqlalchemy import SQLAlchemy
    #importing the migrate object into the app
from flask_migrate import Migrate

#to create a form
# %%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
class NameForm(FlaskForm):
    name = StringField("What is your name?", validators=[DataRequired()])
    submit = SubmitField("Submit")

basedir = os.path.abspath(os.path.dirname(__file__))

#to create an instance of a Flask object
# %%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
    #an instance of a Flask object
app = Flask(__name__)
    #a secret key for creating forms
app.config['SECRET_KEY'] = "keep it a secret, at all costs"

    #SQLAlchemy
app.config['SQLALCHEMY_DATABASE_URI'] = \
    f'sqlite:///{os.path.join(basedir, "data-dev.sqlite")}'

        #to supress a warning when doing this
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

        #initialising the database object
db = SQLAlchemy(app)
migrate = Migrate(app, db,  render_as_batch= True )

    #an instance of a bootstrap application
bootstrap = Bootstrap(app)

#routing
#%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%

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

    #to add an age collumn to the database
    age = db.Column(db.Integer)

    def __repr__(self):
        return f"<User {self.username}>"

    #so that you don't have to manually add objects to the application context when you begin a shell session
@app.shell_context_processor
def make_shell_context():
        return dict(db=db, User=User, Role=Role)

#this is a decorator - for when someone visits the route URL
    #route handling - calling the index function would triggered it to be run on the server
    #this includes arguments for forms (the second and third)

@app.route('/', methods=['GET', 'POST'], form=form)
def index():
    #for a form - this was initialised above
    form = NameForm()
    # name = None
    if form.validate_on_submit():
        name_entered = form.name.data
        user = User.query.filter_by(username=name_entered).first()
        if  user is None:
            user = User(username=name_entered)
            db.session.add(user)
            db.session.commit()
            session['known'] = False
        else:
            session['known'] = True

        # name = form.name.data  # Get the value from the form
        session['name'] = name_entered
        # session['name'] = form.name.data
        # form.name.data = ""  # Reset the form field to an empty string
        flash('Great! We hope you enjoy the community')
        return redirect(url_for('index'))

    # return "Hello Web World!"
        # below - the argument of this is the path to the template relative to the templates folder
            # using a Jinja2 template to do the same as the line above
            # the second argument for this is the template it is parsed into, to render

    return render_template('index.html', form=form, name=session.get('name'))
                # return render_template('index.html', form=form, name=name)
        known=session.get('known', False)

    """
        To run this:
        -> this is a .py file and can be run as a web app
        -> it was made with Flask
        -> functions being defined in .py files
        -> Flask can get applications running
            -> it has its own web development server
            -> this requires you to set the environment variable
            -> this tells you the name of the file where the application instance lives
            -> export FLASK_APP=hello.py <- entering this into the CLI, while it says (env) (base)...

        To launch the web app:
            -> flask run <- in the terminal
            -> this is what the CLI does:
                * Serving Flask app 'hello.py'
                * Debug mode: off
                WARNING: This is a development server. Do not use it in a production deployment. Use a production WSGI server instead.
                * Running on http://127.0.0.1:5000
                Press CTRL+C to quit
            -> it tells you it's running
            -> then you go to http://127.0.0.1:5000 in the URL of a browser and it opens
            -> when you do that the CLI tells you it's been opened

        To run Flask for development mode:
            -> this runs in production mode by default (the warning sign in the CLI)
            -> export FLASK_ENV=development <- this sets another environment variable, to run the app in development mode
            -> every time the browser is refreshed, it's making a new HTTP GET request
            -> flask run <- to start this in a development environment

        Debug mode
            -> export FLASK_DEBUG=1 <- to enable debug mode in the terminal
                -> when Flask run is not in the CLI
                -> that has to be running for the app to work in the browser
            -> reloader <- the server restarts if changes are made to the code
            -> debugger <- if changes made to the app will break it, this allows the source code to be interacted with
            -> flask --help <- for documentation

        Summary instructions
            -> write the .py file
            -> then run the app in the terminal <- flask run
            -> enable development and debugger mode
    """

# Route handling for errors
#%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
@app.errorhandler(403)
def forbidden(e):
    error_title = "Forbidden"
    error_msg = "You shouldn't be here!"
    return render_template('error.html',
                           error_title=error_title,error_msg=error_msg), 403


@app.errorhandler(404)
def page_not_found(e):
    error_title = "Not Found"
    error_msg = "That page doesn't exist"
    return render_template('error.html',
                           error_title=error_title,error_msg=error_msg), 404


@app.errorhandler(500)
def internal_server_error(e):
    error_title = "Internal Server Error"
    error_msg = "Sorry, we seem to be experiencing some technical difficulties"
    return render_template("error.html",
                           error_title=error_title,
                           error_msg=error_msg), 500

@app.route('/user/<id>')
def get_user(id):
    user = load_user(id)
    if not user:
        abort()(404)
    return f"<h1>Hello, {user}!</h1>"