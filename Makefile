.PHONY: docker-build build serve bash run-bash

docker-build:
	docker compose build

build: docker-build
	docker compose run --rm jekyll bundle exec jekyll build
serve: docker-build
	docker compose up

bash:
	docker compose exec jekyll /bin/bash
run-bash:
	docker compose run --rm jekyll /bin/bash
