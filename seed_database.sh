#!/bin/bash

# Remove database and migrations if they exist
if [ -f db.sqlite3 ]; then
    rm db.sqlite3
fi

if [ -d ./OptimumAPI/migrations ]; then
    rm -rf ./OptimumAPI/migrations
fi

python3 manage.py migrate
python3 manage.py makemigrations OptimumAPI
python3 manage.py migrate OptimumAPI
python3 manage.py loaddata users
python3 manage.py loaddata tokens

