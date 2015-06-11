############################################################
# Dockerfile to build Python WSGI Application Containers
# Based on Ubuntu
############################################################

FROM ubuntu
MAINTAINER Gareth Ferneyhough

# Add the application resources URL
RUN echo "deb http://archive.ubuntu.com/ubuntu/ $(lsb_release -sc) main universe" >> /etc/apt/sources.list

# Update the sources list
RUN apt-get update

# Install basic applications
RUN apt-get install -y tar git curl nano wget dialog net-tools build-essential

# Install Python and Basic Python Tools
RUN apt-get install -y python python-dev python-distribute python-pip

ADD dl-repo /dl-repo
RUN pip install -r /dl-repo/requirements.txt
EXPOSE 8080
WORKDIR /dl-repo
CMD python run.py
