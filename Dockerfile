# Use Python base image
FROM python:3.11-slim

# Set working directory
WORKDIR /app

# Copy project files
COPY . .

# Upgrade pip (old pip can cause build errors)
RUN pip install --upgrade pip

# Install dependencies with extended timeout
RUN pip install --default-timeout=200 --no-cache-dir -r requirements.txt

# Expose port
EXPOSE 5000

# Run Flask app
CMD ["python", "src/app.py"]
