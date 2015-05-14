import requests
from flask import Blueprint, request, render_template, \
        url_for, make_response

dl_repo = Blueprint('dl_repo', __name__, url_prefix='/')

@dl_repo.route('/', methods=['GET'])
def index():    
    return render_template("dl_repo/index.html")

@dl_repo.route('download', methods=['GET'])
def download():
    url = request.args.get('url')
    compression = request.args.get('compression')
        
    file = requests.get(url)
    response = make_response(file.content)    
    response.headers["Content-Disposition"] = "attachment; filename=file.html"
    return response
    #return render_template("dl_repo/index.html") 
