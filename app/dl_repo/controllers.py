# Import flask dependencies
from flask import Blueprint, request, render_template, \
        flash, g, session, redirect, url_for


dl_repo = Blueprint('dl_repo', __name__, url_prefix='/')

# Set the route and accepted methods
@dl_repo.route('/', methods=['GET'])
def index():    
    return render_template("dl_repo/index.html")
