web: gunicorn config.wsgi:application
worker: celery worker --app=serious_games_framework.taskapp --loglevel=info
