#!/bin/bash

# Iniciamos el servicio del docker
sudo service docker start
#Descargamos  la imagen de nuestra aplicación
sudo docker pull srmf9/proyecto-iv
#Entramos en la imagen de nuetra aplicación
sudo docker run -i -t srmf9/proyecto-iv /bin/bash 
