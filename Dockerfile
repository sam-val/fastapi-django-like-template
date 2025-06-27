# syntax=docker/dockerfile:1

# Use official Python base image
FROM python:3.13-slim

# Install curl and poetry
RUN apt-get update \
    && apt-get install -y \
    build-essential \
    libpq-dev \
    curl \
    && curl -sSL https://install.python-poetry.org | python - \
    && apt-get clean \
    && rm -rf /var/lib/apt/lists/*

# Add Poetry to PATH
ENV PATH="/root/.local/bin:$PATH"

# Set working directory
WORKDIR /code

# Install project files
COPY pyproject.toml poetry.lock* ./

# Install dependencies
# no interaction: so asking question/prompt
# no root: poetry uses no packages 
RUN poetry install --no-interaction --no-root

# Copy files
COPY . .
COPY .env .env

# Run the app with uvicorn
CMD ["poetry", "run", "uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]
