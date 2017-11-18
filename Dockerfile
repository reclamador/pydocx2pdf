FROM ubuntu:17.04

RUN apt-get update
RUN apt-get install -y python3 python3-pip
RUN apt-get install -y build-essential libssl-dev libffi-dev python-dev
RUN apt-get install -y libreoffice

ADD test.docx /app/
