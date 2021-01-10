.PHONY: help, start, restart

help:
	@echo "Available commands:"
	@echo "start                   : Starts all service container"
	@echo "restart                 : Restarts service containers [hard]"
	@echo "help                    : Shows this help information"

.env:
	cp sample.env .env

start:
	@docker-compose up -d

restart:
	@docker-compose rm -f -s proxy frontend api
	@docker-compose up -d proxy frontend api