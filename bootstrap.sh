#!/bin/sh

django-admin migrate --no-input
django-admin create_vagrant_user
django-admin runserver 0.0.0.0:$SIMPL_GAMES_API_PORT
