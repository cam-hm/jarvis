# Use Python 3.11 slim image for a smaller footprint
FROM python:3.11-slim

# Install system dependencies required for Piper TTS and audio processing
# espeak-ng: often needed for phonemization
# libsndfile1: for audio file handling
RUN apt-get update && apt-get install -y \
    espeak-ng \
    libsndfile1 \
    && rm -rf /var/lib/apt/lists/*

# Set working directory
WORKDIR /app

# Copy requirements first to leverage Docker cache
COPY requirements.txt .

# Install Python dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Copy the rest of the application code
COPY . .

# Expose the port the app runs on
EXPOSE 8000

# Command to run the application
# Render provides the PORT environment variable, but we default to 8000
CMD ["sh", "-c", "uvicorn src.app.main:app --host 0.0.0.0 --port ${PORT:-8000}"]
