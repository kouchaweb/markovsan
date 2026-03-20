# Use Python 3.12 slim image as base
FROM python:3.12-slim

# Set environment variables
ENV PYTHONUNBUFFERED=1 \
    PYTHONDONTWRITEBYTECODE=1 \
    PIP_NO_CACHE_DIR=1

# Install system dependencies
RUN apt-get update && apt-get install -y --no-install-recommends \
    git \
    curl \
    build-essential \
    && rm -rf /var/lib/apt/lists/*

# Install UV (fast Python package manager)
RUN pip install uv

# Install Python development tools
RUN pip install ruff black flake8

# Set working directory
WORKDIR /workspace

# Create a non-root user for development (optional but recommended)
RUN useradd -m -s /bin/bash devuser && \
    chown -R devuser:devuser /workspace

USER devuser
