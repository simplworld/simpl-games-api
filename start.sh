#!/bin/bash
python manage.py migrate
python manage.py collectstatic --noinput
gunicorn -b 0.0.0.0:80 --keep-alive 10 -w 2 --name simpl 'config.wsgi'
