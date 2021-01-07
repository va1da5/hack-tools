.PHONY: dev, restart

.venv:
	python -m venv .venv

dev: .venv
	@. .venv/bin/activate; \
	pip install -r requirements/dev.txt

restart:
	docker-compose rm -f -s api worker
	docker-compose up -d api worker