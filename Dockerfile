FROM python:3.5

LABEL Description="Image for simpl-games-api" Vendor="Wharton" Version="1.1.3"

ENV PYTHONUNBUFFERED 1
ENV DOCKERIZE_VERSION v0.2.0

RUN apt-get update && apt-get install -y wget \
    && wget https://github.com/jwilder/dockerize/releases/download/$DOCKERIZE_VERSION/dockerize-linux-amd64-$DOCKERIZE_VERSION.tar.gz \
    && tar -C /usr/local/bin -xzvf dockerize-linux-amd64-$DOCKERIZE_VERSION.tar.gz \
    && rm -rf /var/lib/apt/lists/* /var/cache/apt/*

RUN pip install --upgrade pip

ENV DJANGO_SECRET_KEY u_%!79f@6su%xr9a!w_5#yib##i6!yzbo6%@n1rrrfz)*_5avf
ENV DATABASE_URL postgres://simpl@postgres/simpl

RUN mkdir /code
ADD . /code/
WORKDIR /code
ENV PYTHONPATH /code:$PYTHONPATH

RUN pip install -r /code/requirements.txt \
    && pip install -r /code/requirements/production.txt

EXPOSE 80
CMD gunicorn config.wsgi -b 0.0.0.0:80
