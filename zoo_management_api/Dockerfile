# Base image
FROM python:3.12-slim-bookworm

# Set working directory
WORKDIR /app

# Copy project files
COPY . .
COPY db.json* ./

# Install Poetry and project dependencies
RUN pip install --no-cache-dir poetry && \
    poetry config virtualenvs.create false && \
    poetry install --only main

# Set environment variables
ENV PYTHONPATH=/app
ENV FLASK_APP=app.py
ENV FLASK_RUN_HOST=0.0.0.0

# Expose port
EXPOSE 5000

# Run the application
CMD ["python", "app.py"]
