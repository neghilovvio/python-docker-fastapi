# Use an official Python runtime as a parent image
FROM python:3-slim-buster

# Set the working directory to /code
WORKDIR /code

# Install any needed packages specified in requirements.txt
COPY requirements.txt .
RUN pip install -r requirements.txt

# COPY . .

# Command to run the app. Notice we keep the --reload flag to enable hot reloading
# CMD ["uvicorn", "main:app", "--host=0.0.0.0", "--port=80", "--reload"]
