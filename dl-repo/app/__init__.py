# Import flask and template operators
from flask import Flask, render_template
from flask.ext.sqlalchemy import SQLAlchemy

# Define WSGI application object
app = Flask(__name__)

app.config.from_object('config')

db = SQLAlchemy(app)

# Sample HTTP error handling
@app.errorhandler(404)
def not_found(error):
    return render_template('404.html'), 404

# Import a module / component using its blueprint handler variable (mod_auth)
from app.mod_auth.controllers import mod_auth as auth_module
from app.dl_repo.controllers import dl_repo as dl_repo_module

# Register blueprint(s)
app.register_blueprint(auth_module)
app.register_blueprint(dl_repo_module)

# Build db
db.create_all()
