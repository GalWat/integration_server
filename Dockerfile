FROM python:3.11-slim

WORKDIR .

COPY ./server ./server
COPY requirements.txt ./

RUN apt-get -y update &&\
    apt-get -y install build-essential python-dev &&\
    pip install -r requirements.txt