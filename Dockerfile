FROM python:3.6


ENV PYTHONUNBUFFERED 1
ENV DOCKERIZE_VERSION v0.2.0

RUN mkdir -p /code/; apt update && apt -y upgrade; \
        apt -y install gnupg; \
        apt remove -y $( dpkg -l | cut -d" " -f3 | egrep '^(x11|tk|libice|gtk|imagemag|mysql)' ) ;\
        rm -rf /var/lib/apt/lists/* \
        \
    &&  ( cd /usr/local; \
            curl -s -LO https://nodejs.org/dist/${NODE_VERSION}/node-${NODE_VERSION}-linux-x64.tar.xz ;\
            tar xfJ node-${NODE_VERSION}-linux-x64.tar.xz ;\
            ( cd /usr/local/bin; ln -sf ../node*/bin/* . ); \
            rm node*xz \
        ) \
    && curl -sL -o /tini https://github.com/krallin/tini/releases/download/${TINI_VERSION}/tini  \
    && curl -sL -o /tini.asc https://github.com/krallin/tini/releases/download/${TINI_VERSION}/tini.asc \
    && gpg --keyserver ha.pool.sks-keyservers.net --recv-keys 595E85A6B1B4779EA4DAAEC70B588DFF0527A9B7 \
    && gpg --verify /tini.asc \
    && chmod 700 /tini \
    && mkdir /code \
    && pip install --upgrade pip

ADD ./requirements.txt ./code/requirements.txt

RUN pip install -r /code/requirements.txt; pip install python-memcached

ADD . /code/
WORKDIR /code
ENV PYTHONPATH /code:$PYTHONPATH

EXPOSE 80
ENTRYPOINT ["/tini", "--"]
CMD ["gunicorn", "-c", "/code/gunicorn.conf", "config.wsgi"]


LABEL Description="Image for simpl-games-api" Vendor="Wharton" Version="1.3.6"
