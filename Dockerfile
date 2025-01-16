FROM gladiatr72/just-tini:latest AS tini

FROM revolutionsystems/python:3.8-wee-optimized-lto

ENV PYTHONUNBUFFERED=1
ENV PYTHONDONTWRITEBYTECODE=true

RUN apt update -y && apt upgrade -y && apt install -y ca-certificates

RUN pip install -U "pip<24.1"

COPY ./requirements.txt ./code/requirements.txt

RUN pip install --no-cache-dir -r /code/requirements.txt

COPY --from=tini /tini /tini

ADD . /code/
WORKDIR /code

ENV PYTHONPATH=/code

EXPOSE 8000

ENTRYPOINT ["/tini", "--"]

CMD ["gunicorn", "-c", "/code/gunicorn.conf.py", "config.wsgi"]


LABEL Description="Image for simpl-games-api" Vendor="Wharton" Version="0.8.5"
