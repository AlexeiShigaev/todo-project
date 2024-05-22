#!/bin/sh
echo !!! start Django !!!

#python  --version
#uname -a
#whoami

if [ ! -f setup.ok ]; then
    echo Setup
    echo first start Postgresql can be restarted. wait please.
    sleep 5
    echo START python manage.py migrate
    python manage.py migrate
    echo START python manage.py createsuperuser --noinput
    python manage.py createsuperuser --noinput
    echo make marker file setup.ok
    touch setup.ok
fi

#python manage.py runserver 0.0.0.0:8000
echo START django via gunicorn. Check static files in DEBUG mode
gunicorn todo_app.wsgi:application --bind 0.0.0.0:8000
