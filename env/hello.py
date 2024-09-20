#importing FLask
#%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
#import Flask
from flask import Flask
import render_template
    #import Bootstrap
from flask_bootstrap import Bootstrap

#to create an instance of a Flask object
    #an instance of a Flask object
app = Flask(__name__)

    #an instance of a bootstrap application
bootstrap = Bootstrap(app)

#routing
#%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%

#this is a decorator - for when someone visits the route URL
    #route handling - calling the index function would triggered it to be run on the server
@app.route('/')
def index():
    # return "Hello Web World!"
        # below - the argument of this is the path to the template relative to the templates folder
            # using a Jinja2 template to do the same as the line above
    return render_template('index.html')

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