#!/bin/bash

rm db.sqlite3
rm -rf ./Optimumapi/migrations
python3 manage.py migrate
python3 manage.py makemigrations Optimumapi
python3 manage.py migrate Optimumapi
python3 manage.py loaddata users
python3 manage.py loaddata tokens

