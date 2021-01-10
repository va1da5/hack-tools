# Hacker Tools

## Motivation

This is a <u>toy project</u> to scratch a surface of the REST API and front-end technologies. It include simple yet possibly useful code examples that could later serve as a quick reference for other projects. The aim is to expand the project with more techniques and technologies overtime which would be relevant for WEB development and automation (metrics, logging, security, etc).

## Technology Stack

**Frontend**

- [Angular 11](https://angular.io/docs)
- [Clarity Design System UI Kit](https://next.clarity.design/)

**Backend**

- [Django 3](https://www.djangoproject.com/)
- [Django Rest framework](https://www.django-rest-framework.org/)
- [Celery](https://docs.celeryproject.org/en/stable/)

## Usage

Each of the services is separated within directories _frontend_ and _backend_. This allows working on each individually. However, all could be spin up using [docker-compose](https://docs.docker.com/compose/install/). The below can be used to start the service for testing.

```bash
# build service images
docker-compose build

# start services as a daemon
docker-compose up -d

# follow service logs
docker-compose logs -f
```

Furthermore, the project include Make utility commands:

```txt
make help
Available commands:
start                   : Starts all service container
restart                 : Restarts service containers [hard]
help                    : Shows this help information
```
