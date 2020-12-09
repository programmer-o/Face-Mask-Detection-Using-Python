FROM python:3.8

# Create app directory
WORKDIR / Face Mask Detection using Python

# Install app dependencies
COPY src/requirements.txt ./

RUN pip install -r requirements.txt

# Bundle app source
COPY src /app

EXPOSE 8080
CMD [ "python3", "app.py" ]