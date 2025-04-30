# Use a base image with Java (required for Spark)
FROM openjdk:11-jre-slim

# Install Python and pip
RUN apt-get update && \
    apt-get install -y python3 python3-pip && \
    apt-get clean

# Set working directory
WORKDIR /app

# Copy project files
COPY . .

# Install Python dependencies
RUN pip3 install --no-cache-dir -r requirements.txt

# Set environment variables for Spark
ENV PYSPARK_PYTHON=python3

# Default command to run your app
CMD ["python3", "main.py"]


