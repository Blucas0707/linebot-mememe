# syntax=docker/dockerfile:1

# Build stage
FROM python as build
# Update
RUN apt-get update
# Assign work directory
WORKDIR /gogolook
# Copy root directory to container
COPY . /gogolook
# Download python packages
RUN pip install --no-cache-dir --upgrade pip && \
    pip install --no-cache-dir -r requirements.txt

EXPOSE 8080
CMD python3 app.py
# Deploy stage
# FROM alpine:latest
# RUN apk update && apk add bash && apk --no-cache add ca-certificates
# WORKDIR /
# COPY --from=build . .
# # COPY --from=build /chatroom/.env .
# COPY --from=build /chatroom/. .
# EXPOSE 8080
# CMD ["./server"]