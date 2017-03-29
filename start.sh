#!/bin/bash
python manage.py migrate
python manage.py collectstatic --noinput
gunicorn --log-config=/code/config/logging.conf -b 0.0.0.0:80 -w 2 --name simpl 'config.wsgi'
