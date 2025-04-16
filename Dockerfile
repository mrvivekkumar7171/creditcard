# Use an official Python runtime as a parent image
FROM python:3.8-slim

# Set the working directory to /app
WORKDIR /app

# Copy the required files and directory into the container at /app
# COPY . /app # to copy everything
COPY app.py /app/app.py
# This is where we have to import model.joblib from the S3 or any model registry
# here i have kept the model.joblib in the same directory to test the docker image
# generlly, we are copying the model.joblib in the docker image. except, for deep learning models.
COPY model.joblib /app/model.joblib
COPY requirements.txt /app/requirements.txt

# Install any needed packages specified in requirements.txt
RUN pip install -r requirements.txt
# RUN pip install --upgrade awscli # upgrade the AWS CLI

# Copy files from S3 inside docker
# RUN mkdir /app/models
# RUN aws s3 cp s3://creditcard-project/models/model.joblib /app/models/model.joblib


# Run app.py when the container launches
CMD ["python", "app.py"]
