FROM ubuntu:latest
LABEL authors="PrathamS"

# Use an official Python runtime as a parent image
FROM python:3.9-slim

# Set the working directory to /app
WORKDIR /app

# Copy the current directory contents into the container at /app
COPY . /app

# Install any needed packages specified in requirements.txt
RUN pip install --no-cache-dir -r requirements.txt

# Define environment variable (if needed)
# ENV NAME Value

# Run generate_price_producer.py when the container launches
CMD ["python", "temp_main.py"]

