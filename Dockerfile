# Parent Image
FROM python:3.12-slim

## Essential Environment Variables
ENV PYTHONDONTWRITEBYTECODE=1 \
    PYTHONUNBUFFERED=1 

## Working Directory
WORKDIR /app

## Install dependencies
RUN apt-get update && apt-get install -y \
    build-essential \
    curl \
    && rm -rf /var/lib/apt/lists/*

## Copying your all content from local to app
COPY . .

## Run the setup
RUN pip install --no-cache-dir -e .

## Expose the port
EXPOSE 8501

## Run the app
CMD ["streamlit", "run", "main.py", "--server.port=8501", "--server.address=0.0.0.0", "--server.headless=true"]