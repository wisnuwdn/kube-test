# Use an official Python runtime as a parent image
FROM python:3.9-slim

# Set the working directory in the container
WORKDIR /app

# Copy the current directory contents into the container at /app
COPY . .

# Install pandas package
RUN pip install --no-cache-dir pandas

# Make port 80 available to the world outside this container
EXPOSE 80

# Run print_talent_name.py and redirect output to talent_output.log
CMD ["sh", "-c", "python app.py > talent_output.log"]
