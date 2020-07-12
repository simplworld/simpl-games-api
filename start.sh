#!/bin/bash
./wait-for-it.sh -h db -p 5432 -t 20 -- python manage.py migrate
python manage.py collectstatic --noinput
#gunicorn -c /code/gunicorn.conf.py 'config.wsgi'
python manage.py runserver 0.0.0.0:8000
