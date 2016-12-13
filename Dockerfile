FROM python:3.5

LABEL Description="Image for simpl-games-api" Vendor="Wharton" Version="1.0"

ENV PYTHONUNBUFFERED 1
ENV DJANGO_SECRET_KEY u_%!79f@6su%xr9a!w_5#yib##i6!yzbo6%@n1rrrfz)*_5avf
ENV DATABASE_URL postgres://simpl@postgres/simpl
ENV DOCKERIZE_VERSION v0.2.0

RUN mkdir -p /root/.ssh \
    && chmod 700 /root/.ssh \
    && echo "Host *\n\tStrictHostKeyChecking no\n\n" > /root/.ssh/config

ADD keys/wharton_ll /root/.ssh/
RUN chmod 600 /root/.ssh/wharton_ll

RUN apt-get update && apt-get install -y wget \
    && wget https://github.com/jwilder/dockerize/releases/download/$DOCKERIZE_VERSION/dockerize-linux-amd64-$DOCKERIZE_VERSION.tar.gz \
    && tar -C /usr/local/bin -xzvf dockerize-linux-amd64-$DOCKERIZE_VERSION.tar.gz \
    && rm -rf /var/lib/apt/lists/* /var/cache/apt/*

RUN pip install --upgrade pip

RUN mkdir /code
ADD . /code/
WORKDIR /code
ENV PYTHONPATH /code:$PYTHONPATH

RUN eval "$(ssh-agent -s)" \
    && ssh-add /root/.ssh/wharton_ll \
    && pip install -r /code/requirements/gitlab.txt \
    && pip install -r /code/requirements/production.txt

EXPOSE 8100
CMD gunicorn config.wsgi -b 0.0.0.0:8100
