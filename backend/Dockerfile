FROM python:3.8.7-slim

WORKDIR /app

RUN apt update \
  && apt install -y nmap \
  && adduser --no-create-home django \
  && rm -rf /var/lib/apt/lists/*

COPY requirements requirements
COPY requirements.txt .

RUN pip install -r requirements.txt

COPY . .

USER django

CMD [ "-c", "gunicorn config.wsgi" ]