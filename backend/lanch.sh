#!/bin/bash
#python /code/src/manage.py makemigrations
#python /code/src/manage.py migrate
#python /code/src/manage.py collectstatic --no-input
DEFAULT_USER="test"
LAST_NAME="test"
COMPANY="CSAI"
DEFAULT_EMAIL="moussa.beji@solixy.com"
DEFAULT_PASS="csaiadmin"

#echo "from django.contrib.auth import get_user_model; User = get_user_model(); User.objects.filter(username='$DEFAULT_USER', is_superuser=True).delete(); User.objects.create_superuser('$DEFAULT_USER', '$DEFAULT_EMAIL', '$LAST_NAME', '$LAST_NAME', '$COMPANY', '$DEFAULT_PASS')" | python /code/src/manage.py shell


gunicorn --bind 0.0.0.0:8000 DjangoAPI.wsgi  --chdir /code/src --threads 10

