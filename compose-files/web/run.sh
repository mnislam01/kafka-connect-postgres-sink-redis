#!/usr/bin/env bash
python manage.py wait_for_db
python manage.py migrate
python manage runserver 0.0.0.0:8001
