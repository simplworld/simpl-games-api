#!/bin/sh

django-admin migrate --no-input
if [ -z ${INITIAL_FIXTURE+x} ]
then
  django-admin create_vagrant_user
else
  echo "loading $INITIAL_FIXTURE"
  django-admin loaddata $INITIAL_FIXTURE
fi
django-admin runserver 0.0.0.0:$SIMPL_GAMES_API_PORT
