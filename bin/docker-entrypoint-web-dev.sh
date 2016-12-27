#!/bin/bash

echo "---------wait for postgres start -----------"
../bin/wait-for-it.sh postgres:5432
echo "---------postgres start success -----------"

echo "---------migrate django db  -----------"
yes "yes" | python manage.py migrate

echo "---------migrate django db success -----------"


echo "---------start django -----------"
python manage.py runserver 0.0.0.0:8000
