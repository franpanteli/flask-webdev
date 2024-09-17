#importing FLask
#%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
#import Flask
from flask import Flask

#to create an instance of a Flask object
    #an instance of a Flask object
app = Flask(__name__)


#routing
#%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%

#this is a decorator - for when someone visits the route URL
    #route handling - calling the index function would triggered it to be run on the server
@app.route('/')
def index():
    return "Hello Web World!"

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
