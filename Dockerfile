# Official lightweight Python image.
FROM python:3.8-slim-buster

# Create and change to the app directory.
WORKDIR /python-docker

# Copy application dependency manifests to the container image.
COPY requirements.txt requirements.txt

# Install dependencies.
RUN pip3 install -r requirements.txt

# Copy local code to the container image.
COPY . .

# Run the web service on container startup.
CMD [ "python3", "-m" , "flask", "run", "--host=0.0.0.0"]
