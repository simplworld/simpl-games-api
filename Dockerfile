FROM python:3.6-slim


ENV PYTHONUNBUFFERED 1
ENV TINI_VERSION v0.14.0

RUN mkdir -p /code/; apt update && apt -y upgrade; \
    apt-get -y install netcat-openbsd curl git gnupg  \
    && curl -sL -o /tini https://github.com/krallin/tini/releases/download/${TINI_VERSION}/tini  \
    && curl -sL -o /tini.asc https://github.com/krallin/tini/releases/download/${TINI_VERSION}/tini.asc \
    && gpg --keyserver ha.pool.sks-keyservers.net --recv-keys 595E85A6B1B4779EA4DAAEC70B588DFF0527A9B7 \
    && gpg --verify /tini.asc \
    && chmod 700 /tini \
    && apt remove -y $( dpkg -l | cut -d" " -f3 | egrep '^(x11|tk|libice|gtk|imagemag|mysql|curl)' ) \
    && apt-get -y autoremove \
    && rm -rf /var/lib/apt/lists/* /usr/share/man /usr/local/share/man

ADD ./requirements.txt ./code/requirements.txt

RUN apt update \
        && apt-get -y install libjpeg62-turbo-dev zlib1g-dev gcc make \
        && apt-mark manual libjpeg62-turbo zlib1g \
    && pip install -r /code/requirements.txt; pip install python-memcached \
    && apt-get -y remove libjpeg62-turbo-dev zlib1g-dev gcc make \
    && apt-get -y autoremove \
    && rm -rf /var/lib/apt/lists/* /usr/share/man /usr/local/share/man \
    && find /usr -type f -regex "*.py[co]$" -exec rm -r {} +

ADD . /code/
WORKDIR /code
ENV PYTHONPATH /code:$PYTHONPATH

EXPOSE 8000

ENTRYPOINT ["/tini", "--"]

CMD ["gunicorn", "-c", "/code/gunicorn.conf", "config.wsgi"]


LABEL Description="Image for simpl-games-api" Vendor="Wharton" Version="1.3.12"
