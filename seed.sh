#!/bin/bash
rm -rf nomadicityapi/migrations
rm db.sqlite3
python manage.py migrate
python manage.py makemigrations nomadicityapi
python manage.py migrate nomadicityapi
python manage.py loaddata users
python manage.py loaddata boards
python manage.py loaddata hikes

# Run chmod +x seed.sh in the terminal.
# run ./seed.sh in the terminal to run the commands
