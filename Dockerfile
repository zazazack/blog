FROM python:alpine

WORKDIR /usr/src/app
RUN apk upgrade && apk add git
ENV PYTHONUNBUFFERED 1
COPY requirements.txt ./
# TODO: add Makefile command to update requirements before building
RUN pip install --no-cache-dir -r requirements.txt
COPY . .
ENV FLASK_APP blog
ENV FLASK_ENV production
RUN flask init-db
EXPOSE 5000
CMD ["flask", "run", "--host", "0.0.0.0"]
