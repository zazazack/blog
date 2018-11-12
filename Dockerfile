FROM python:alpine

ENV PYTHONUNBUFFERED 1
WORKDIR /usr/src
COPY . .
RUN apk upgrade --no-cache && \
  apk add --no-cache git
# TODO: add Makefile command to update requirements before building
RUN pip install --no-cache -r requirements.txt
EXPOSE 5000
