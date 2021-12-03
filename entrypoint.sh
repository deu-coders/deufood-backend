#!/bin/bash

/wait-for-it.sh -t 0 $MARIADB_HOST:$MARIADB_PORT

python manage.py migrate
exec python manage.py runserver 0.0.0.0:8000