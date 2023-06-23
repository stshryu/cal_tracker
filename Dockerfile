# Base Image
FROM python:3.11

# Working DIR
WORKDIR /app

# Requirements
COPY requirements.txt .

# Install Dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Copy application code
COPY . .

# Set env variables
ENV FLASK_APP=base.py
ENV FLASK_RUN_HOST=0.0.0.0

# Ports
EXPOSE 5000

# Run app
CMD ["flask", "run"]
