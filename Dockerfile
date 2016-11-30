FROM python:3.5
ENV PYTHONUNBUFFERED 1

RUN mkdir -p /root/.ssh
RUN chmod 700 /root/.ssh
RUN echo "[stash.wharton.upenn.edu]:7999,[128.91.88.173]:7999 ssh-rsa AAAAB3NzaC1yc2EAAAADAQABAAABAQCQPk1f/qGyJuKO6l0o+0kYxmDxUavfpPyYfBanEzChJbQddPGqNgWWcP0WsTavLj2pUrXSvmJBuCOBtbP3alxnPT7sb3UcK7taVaKFyJxKxBtiEMqOLuezwjX0eSaI+fqTP5em7USLWyR2bBMxmwI+AU1lfbKlnMtHeLZ4+kgp2hXacab/TY6k/arf+khcZ8+5A/z3KZ7LTbJ4xho4BKnLvY1iFYUjoSP6sx7XQsDHLwAHvWvy7Qc8QlVsI7sIHcVjseZlPrJkjoPX9Q2h1dKSVYUmZJ9YtpFSVpkjBGbBZ1CWZ7h+eWrwP+NYyxpq4LV3SG/csUBdQHaFydufaVND" >> /root/.ssh/known_hosts

ADD keys/wharton_ll /root/.ssh/
RUN chmod 600 /root/.ssh/wharton_ll

RUN apt-get update && apt-get install -y wget
ENV DOCKERIZE_VERSION v0.2.0
RUN wget https://github.com/jwilder/dockerize/releases/download/$DOCKERIZE_VERSION/dockerize-linux-amd64-$DOCKERIZE_VERSION.tar.gz \
    && tar -C /usr/local/bin -xzvf dockerize-linux-amd64-$DOCKERIZE_VERSION.tar.gz

RUN pip install --upgrade pip

RUN mkdir /code
ADD . /code/
WORKDIR /code
ENV PYTHONPATH /code:$PYTHONPATH

RUN eval "$(ssh-agent -s)" && ssh-add /root/.ssh/wharton_ll && pip install -r /code/requirements.txt
