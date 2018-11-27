---
  title: README
  author: Zachary Wilson
  date: 2018-11-14 13:38:00-6
  repository:
    url: https://github.com/zazazack/blog
---

# blog

A really simple containerized blogging application built with [python](https://www.python.org) and [Flask](http://flask.pocoo.org).

## Features

-  Authentication
-  Database
-  View, create, and edit posts

## Installation

### Prerequisites

-   [Docker CE](https://www.docker.com/get-started)

### Stable

```sh
$ docker pull zwilson/blog
```

### Development

```sh
$ git clone <https://github.com/zazazack/blog>
```

## Usage

### Deploy

```sh
$ docker stack deploy -c stack.yml blog
$ curl http://0.0.0.0
```

### Develop

```sh
$ docker-compose up
$ curl http://0.0.0.0:5000
```

### Test

```sh
$ docker-compose up
$ docker-compose exec blog pytest
```

## Documentation

## References
