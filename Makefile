build:
	@docker-compose build

migration:
	@docker-compose run --rm web python ./manage.py makemigrations

migrate:
	@docker-compose run --rm web python ./manage.py migrate

start: build migration migrate
	@docker-compose up 

stop: 
	@docker-compose down

bash:
	@docker-compose run --rm web bash

test:
	@docker-compose run --rm web pytest