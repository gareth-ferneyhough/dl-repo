# dl-repo
dl-repo is an example Flask application using Blueprints to provide modularity, as well as Vagrant and Docker to ease development and deployment across machines. It provides a simple service: a user enters the url of a sourcecode repository in an input field and selects a compression method. dl-repo then downloads the source, compresses it, and sends the file to the user as an attachment. 

Currently only `git` repositories are supported. If it is password protected, the user must enter the SSH url and have his or her SSH keys configured correctly. `zip` is currently the only supported compression method. Note: if you are using the provided Vagrant and Docker scripts you will have to configure your SSH keys manually inside the container, or enable SSH agent forwarding in your Vagrant and Docker files. 

##### To run locally without Docker and Vagrant: #####
`cd dl-repo`

`virtualenv env`

`source env/bin/activate`

`pip install -r requirements.txt`

`python run.py`
