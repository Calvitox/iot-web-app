#! /bin/bash
/usr/bin/mongod &
python manage.py runserver 0.0.0.0:8000