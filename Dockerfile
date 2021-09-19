# syntax=docker/dockerfile:1

FROM python:3.8-slim-buster
MAINTAINER Mikhail Kudin 'watts-galeo@ya.ru'
WORKDIR /app
RUN apt-get update && apt-get install -y \
    git
COPY requirements.txt requirements.txt
RUN pip3 install -r requirements.txt
COPY . .
ENV FLASK_APP='./server/flask_app.py'
CMD ["python3", "-m" , "flask", "run", "--host=0.0.0.0"]