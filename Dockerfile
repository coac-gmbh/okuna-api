FROM python:3.7.3

RUN apt-get -y update && apt-get -y upgrade &&  apt-get install -y ffmpeg && apt-get install -y supervisor

COPY requirements.txt /requirements.txt
RUN pip install -r /requirements.txt

# Setup workdir
RUN mkdir -p /opt/okuna-api
WORKDIR /opt/okuna-api

COPY . /opt/okuna-api
