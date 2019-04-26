# # The first instruction is what image we want to base our container on
# # We Use an official Python runtime as a parent image
# FROM python:3.6

# # The enviroment variable ensures that the python output is set straight
# # to the terminal with out buffering it first
# ENV PYTHONUNBUFFERED 1

# # create root directory for our project in the container
# RUN mkdir /SauCI

# # Set the working directory to /music_service
# WORKDIR /SauCI

# # Copy the current directory contents into the container at /music_service
# ADD . /SauCI/

# # Install any needed packages specified in requirements.txt
# RUN pip install -r requirements.txt

FROM gcr.io/google_appengine/python

# Create a virtualenv for the application dependencies.
# # If you want to use Python 2, use the -p python2.7 flag.
RUN virtualenv -p python3 /env
ENV PATH /env/bin:$PATH

ADD requirements.txt /app/requirements.txt
RUN /env/bin/pip install --upgrade pip && /env/bin/pip install -r /app/requirements.txt
ADD . /app

CMD gunicorn -b :$PORT SauCI.wsgi