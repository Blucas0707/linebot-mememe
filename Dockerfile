# syntax=docker/dockerfile:1

# Build stage
FROM python:3.9-slim as build
# Update
RUN apt-get update
# Allow statements and log messages to immediately appear in the Knative logs
ENV PYTHONUNBUFFERED True
# Assign work directory
WORKDIR /mememe
# Copy root directory to container
COPY . /mememe
# Download python packages
RUN pip install --no-cache-dir --upgrade pip && \
    pip install --no-cache-dir -r requirements.txt

EXPOSE 8080
CMD python3 app.py
