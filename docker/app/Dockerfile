FROM python:3.9.6-alpine

RUN apk add --no-cache bash
RUN apk add build-base

# By default, listen on port 5000
EXPOSE 5000/tcp

# Set the working directory in the container
WORKDIR /app

# Copy the dependencies file to the working directory
COPY temp_build/requirements.txt .

# Install any dependencies
RUN pip install -r requirements.txt

# Copy the content of the local src directory to the working directory
COPY temp_build/src ./src

#Specify the command to run on container start
CMD [ "flask", "run", "--host=0.0.0.0" ]
