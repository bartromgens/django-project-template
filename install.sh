#! /bin/bash

# will abort the script if any line fails
set -e

virtualenv -p python3 env

source env/bin/activate

pip install -r requirements.txt

python create_local_settings.py

python manage.py migrate
