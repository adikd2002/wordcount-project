#!/bin/bash

# OWN wordcount directory
command sudo chown -R $USER:$USER /var/www/wordcount
command python3 --version

# CREATE PYTHON3 ENVIROMENT
isEnv=`ls /var/www/wordcount/  | grep 'venv'`
if [[ ! $isEnv ]];then
  cd /var/www/wordcount
  command python3 -m venv venv
  command ls
fi

# ACTIVATE ENVIROMENT AND INSTALL REQUIREMENTS
command source /var/www/wordcount/venv/bin/activate
command pip install -r /var/www/wordcount/requirements.txt
command pip list
cd /var/www/wordcount
command python manage.py makemigrations
command python manage.py migrate
