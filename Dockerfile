# Use an official Python runtime as a parent image
FROM python:3.6.4

# Set the working directory to /app
WORKDIR /urlSearcher

# Copy the current directory contents into the container at /app
ADD . /urlSearcher

# Install any needed packages specified in requirements.txt
RUN pip install --trusted-host pypi.python.org -r requirements.txt

# Make port 80 available to the world outside this container
EXPOSE 80

# Define environment variable
ENV NAME World

# Run app.py when the container launches
CMD ["python", "urlSearcher.py"]
