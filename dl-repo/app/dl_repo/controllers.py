import subprocess
import requests
from flask import Blueprint, request, render_template, \
        url_for, make_response

def git(*args):
	return subprocess.check_call(['git'] + list(args))

dl_repo = Blueprint('dl_repo', __name__, url_prefix='/')

@dl_repo.route('/', methods=['GET'])
def index():    
    return render_template("dl_repo/index.html")

@dl_repo.route('download', methods=['GET'])
def download():
    url = request.args.get('url')
    compression = request.args.get('compression')

    #git('clone', 'git@github.com:gareth-ferneyhough/jbcb-2015.git', '/var/gitjbcb-2015')
    
    file = requests.get(url)    
    response = make_response(file.content)    
    response.headers["Content-Disposition"] = "attachment; filename=file.html"
    return response    
