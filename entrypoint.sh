#!/bin/bash
python manage.py makemigrations
python manage.py migrate
python manage.py create_groups_and_users
python manage.py create_posts
python manage.py runserver 0.0.0.0:8000