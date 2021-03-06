from repository_downloader import download_repository
from compressor import compress_repository
from flask import Blueprint, request, render_template, \
        url_for, make_response, send_from_directory, flash, redirect
from flask import current_app as app
import os

dl_repo = Blueprint('dl_repo', __name__, url_prefix='/')

@dl_repo.route('/', methods=['GET'])
def index():        
    return render_template("dl_repo/index.html")

@dl_repo.route('download', methods=['GET'])
def download():
    url = request.args.get('url')
    compression = request.args.get('compression')
    tmp_dir = os.path.join(app.config['BASE_DIR'], 'tmp')
    
    try:
        destination_path = download_repository(url, tmp_dir)
        filename = compress_repository(destination_path, compression)
    except Exception as e:
        flash(str(e))
        return redirect(url_for('.index'))
        
    return send_from_directory(tmp_dir, 'git.zip',
        as_attachment=True, attachment_filename='download.zip')
