# Use a slim version of Python 3.9
FROM python:3.9-slim

# Set the working directory in the container
WORKDIR /app

# Copy the requirements file and install dependencies
COPY requirements.txt requirements.txt
RUN pip install --no-cache-dir -r requirements.txt

# Copy the rest of the application code
COPY . .

# Expose port 8080 for the application
EXPOSE 8080

# Command to run the Flask application
CMD ["python", "cloud_ai_app.py"]
