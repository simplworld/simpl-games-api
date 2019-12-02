From gladiatr72/just-tini:latest as tini

FROM revolutionsystems/python:3.6.5-wee-optimized-lto


ENV PYTHONUNBUFFERED 1

COPY ./requirements.txt ./code/requirements.txt

RUN apt update \
        && apt-get -y install libjpeg62-turbo-dev zlib1g-dev gcc make \
        && apt-mark manual libjpeg62-turbo zlib1g \
    && pip install -r /code/requirements.txt; pip install python-memcached \
    && apt-get -y remove libjpeg62-turbo-dev zlib1g-dev gcc make \
    && apt-get -y autoremove \
    && rm -rf /var/lib/apt/lists/* /usr/share/man /usr/local/share/man \
    && find /usr -type f -regex "*.py[co]$" -exec rm -r {} +

COPY --from=tini /tini /tini
ADD . /code/
WORKDIR /code
ENV PYTHONPATH /code:$PYTHONPATH

EXPOSE 8000

ENTRYPOINT ["/tini", "--"]

CMD ["gunicorn", "-c", "/code/gunicorn.conf", "config.wsgi"]


LABEL Description="Image for simpl-games-api" Vendor="Wharton" Version="0.7.18"
