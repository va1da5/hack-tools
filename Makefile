.PHONY: help, start, start-dev, restart

help:
	@echo "Available commands:"
	@echo "start                   : Starts all service container"
	@echo "restart                 : Restarts service containers [hard]"
	@echo "help                    : Shows this help information"

.env:
	cp sample.env .env

start:
	@docker-compose up -d

build-dev:
	@docker-compose --file docker-compose.dev.yml build

start-dev:
	@docker-compose --file docker-compose.dev.yml up -d

restart:
	@docker-compose rm -f -s proxy frontend api worker
	@docker-compose up -d proxy frontend api worker

restart-dev:
	@docker-compose --file docker-compose.dev.yml rm -f -s proxy frontend api worker
	@docker-compose --file docker-compose.dev.yml up -d proxy frontend api worker