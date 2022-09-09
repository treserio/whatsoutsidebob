#!/bin/bash
service mysql start

pip install django
pip install django-cors-headers
pip install django-filter
pip install djangorestframework

echo "CREATE DATABASE IF NOT EXISTS bob_ross;" | mysql -uroot -proot

python3 load.py

cat mysql-fk-setup.sql | mysql -uroot -proot bob_ross

sleep 2
python3 ../tjop/manage.py migrate
