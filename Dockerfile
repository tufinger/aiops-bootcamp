# Use official Python 3.8 image from Docker Hub
FROM python:3.8-slim

# Set working directory inside the container
WORKDIR /app

# Copy the Python script into the container
COPY app.py .

# Run the script when the container starts
CMD ["python", "app.py"]