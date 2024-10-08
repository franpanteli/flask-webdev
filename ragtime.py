from flask_migrate import Migrate
from app import create_app, db
from app.models import Role, User

app = create_app()

# Initialise Flask-Migrate with render_as_batch=True if using SQLite
migrate = Migrate(app, db, render_as_batch=True)

# Define shell context for Flask CLI
@app.shell_context_processor
def make_shell_context():
    return dict(db=db, User=User, Role=Role)
