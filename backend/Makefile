.PHONY: dev, restart

.venv:
	@python3 -m venv .venv

.env:
	cp sample.env .env

dev: .venv .env
	@. .venv/bin/activate; \
	@pip install -r requirements/dev.txt

restart:
	docker-compose rm -f -s api worker
	docker-compose up -d api worker