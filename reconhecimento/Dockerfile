FROM python:3.9.10-alpine as builder

RUN apk add cmake
RUN apk add musl-dev linux-headers g++
RUN apk add --update gfortran build-base
RUN apk add python3-dev

RUN pip3 install --upgrade pip

RUN pip3 install --user flask
RUN pip3 install --user cmake
RUN pip3 install --user gunicorn==20.1.0
RUN pip3 install --user face_recognition
RUN pip3 install --user opencv-python
RUN pip3 install --user numpy==1.14.4
