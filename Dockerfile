#Base Image
FROM python:3.12-slim

#Set the working directory in the container
WORKDIR /fast_api

# Install system dependencies
# RUN apt-get update && apt-get install -y build-essential

#Copy the requirements file into the container
COPY requirements.txt .

#Install the dependencies
RUN pip install --no-cache-dir -r requirements.txt

#copy the rest of the application code
COPY . .

#Expose the port the FastAPI app will run on
EXPOSE 8000

#Command to run the FastAPI app
CMD ["uvicorn", "index:app", "--host", "0.0.0.0", "--port", "8000"]
