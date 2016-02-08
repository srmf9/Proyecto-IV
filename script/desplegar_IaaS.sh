#!/bin/bash
sudo apt-get install npm
sudo apt-get install fabric
sudo apt-get install nodejs-legacy
sudo npm install -g azure-cli
sudo apt-get install -y python-pip
sudo pip install paramiko PyYAML jinja2 httplib2 ansible
sudo apt-get install -y vagrant
vagrant plugin install vagrant-azure
sudo vagrant up --provider=azure
sudo fab -p 'Clave#salva#1' -H vagrant@mundo-bares.cloudapp.net ejecutar_app

