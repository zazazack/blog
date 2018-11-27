update:
	pip freeze > requirements.txt

init:
	make update
	pip install -r requirements.txt

test:
	pytest

clean:
	rm -rf build/ dist/ instance/ *.egg-info .eggs/ **/__pycache__/

build:
	docker-compose build

shell:
	docker-compose run blog /bin/sh

up:
	docker-compose up

down:
	docker-compose down

destroy:
	docker-compose down --volumes --remove-orphans
	make clean

deploy:
	docker stack deploy -c stack.yml blog

.PHONY: init test clean build shell up down destroy
