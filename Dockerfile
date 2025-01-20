# Use an official Python image as the base
FROM python:3.9-slim

# Set the working directory to /app
WORKDIR /app

# Copy the requirements file
COPY requirements.txt .

# Install the dependencies
RUN pip install -r requirements.txt

# Copy the application code
COPY . .

# Set the environment variable for the OpenAI API key
ENV OPENAI_API_KEY=${OPENAI_API_KEY}

# Expose the port (optional, depends on the project's needs)
EXPOSE 8000

# Run the command to start the application using Uvicorn
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]