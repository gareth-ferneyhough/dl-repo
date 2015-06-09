import shutil
import os

def compress_repository(repo_path, method):	
	if method == 'zip':
		shutil.make_archive(repo_path, 'zip', repo_path)
		return repo_path + '.zip'

	# Should define our own exception class here
	raise Exception('unsupported compression method') 



