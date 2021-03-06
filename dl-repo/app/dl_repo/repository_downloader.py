import subprocess
import shutil
import os

def git(*args):
    return subprocess.check_call(['git'] + list(args))

# currently only supports git clone via ssh 
def download_repository(repository_url, temp_directory):
	# this is in no way ideal, as we are deleting
	# all the repos every time we run.
	destination_path = os.path.join(temp_directory, 'git')
	if os.path.isdir(destination_path):
		shutil.rmtree(destination_path) 
	git('clone', repository_url, destination_path)
	return destination_path
