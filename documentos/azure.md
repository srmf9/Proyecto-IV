## Diseño del soporte virtual al desarrollo y despliegue de una aplicación.

Lo primero que deberemos realizar es instalar el plugin de vagrant:  
``sudo vagrant plugin install vagrant-azure``  
Ahora deberemos bajarnos nuestro certificado del enlace que nos facilita el siguiente comando:   
``azure account download``  
Importamos la credencial:    
``azure account import 2-6-2016-credentials.publishsettings ``  
Generamos la clave privada:  
``openssl req -x509 -nodes -days 365 -newkey rsa:2048 -keyout azurevagrant.key -out azurevagrant.key``  
Damos permiso a la clave:  
``chmod 600 ~/.ssh/azurevagrant.key``  
Y genero el .cer que será el certificado que debemos subir a azure:   
``openssl x509 -inform pem -in azurevagrant.key -outform der -out azurevagrant.cer``

![imagen](http://i1028.photobucket.com/albums/y349/Salva_Rueda/8_zpsn9fqzba8.png)    

Ahora generamos el archivo .pem al que hay que añadirle la llave privada:  
``openssl req -x509 -key ~/.ssh/id_rsa -nodes -days 365 -newkey rsa:2048 -out azurevagrant.pem``  
``cat azurevagrant.key > azurevagrant.pem``  
Este archivo será llamado desde Vagrantfile:  
```
VAGRANTFILE_API_VERSION = "2"

Vagrant.configure(VAGRANTFILE_API_VERSION) do |config|
  config.vm.box = 'azure' #tipo de donde proviene el SO de la caja
  config.vm.network "public_network"
  config.vm.network "private_network",ip: "192.168.56.10", virtualbox__intnet: "vboxnet0" #Si en lugar de acceder por localhost, queremos hacerlo por IP
  config.vm.network "forwarded_port", guest: 80, host: 80 #redireccionamiento de puertos 
  config.vm.define "localhost" do |l|
          l.vm.hostname = "localhost"
   end
#Creación de la máquina de azure
  config.config.vm.provider :azure do |azure, override|
      azure.mgmt_certificate = File.expand_path('~/.ssh/azurevagrant.pem') #ruta donde se encuentra el certificado
      azure.mgmt_endpoint = 'https://management.core.windows.net'
      azure.subscription_id = '327715f7-dcef-44ef-bf93-d88889e67cb3' #id del certificado que encontramos en la web
      azure.vm_image = 'b39f27a8b8c64d52b05eac6a62ebad85__Ubuntu-14_04_3-LTS-amd64-server-20151218-en-us-30GB' #imagen de la máquina virtual
      azure.vm_name = 'ubuntu-bares' #nombre de la máquina
      azure.vm_password = 'Clave#salva#1'#nombre de usuario y contraseña	
      azure.vm_location = 'Central US'  #localización
      azure.ssh_port = '22' #puerto por el que escucha ssh
      azure.tcp_endpoints = '80:80'
  end
  

  #ansible
  config.vm.provision "ansible" do |ansible|
        ansible.sudo = true #permiso de super usuario
        ansible.playbook = "provision.yml" #archivo con todos los comandos que debe ejecutarse
        ansible.verbose = "v"
        ansible.host_key_checking = false
  end
end
```
Y ahora  deberemos crear el archivo provision.yml que es el encargado de instalar todo lo necesario en nuestra máquina virtual para que se pueda levantar la aplicación. Su contenido es:  
```
- hosts: localhost
  sudo: yes
  remote_user: vagrant
  tasks:
  - name: Actualizando sistema
    apt: update_cache=yes upgrade=dist    
  - name: Instalando paquetes necesarios para la máquina virtual
    apt: name=python-setuptools state=present
    apt: name=build-essential state=present
    apt: name=python-dev state=present
    apt: name=python-pip state=present
    apt: name=git state=present
  - name: Instalando el paquete python-pip
    action: apt pkg=python-pip
  - name: Instalando postgresql
    command: sudo easy_install pip
    command: sudo apt-get install -y python-dev libpq-dev python-psycopg2  
  - name: Descargando la aplicación
    git: repo=https://github.com/srmf9/Proyecto-IV.git  dest=aplicacion-desplegada clone=yes force=yes
  - name: Dando permisos al directorio donde se descarga la aplicación
    command: chmod -R +x aplicacion-desplegada
  - name: Instalando los requisitos de la aplicación
    command: pip install -r aplicacion-desplegada/requirements.txt

```
Deberemos comunicar en el archivo ansible_host que vamos a trabajar como una máquina localhost.  
Ahora es el momento de usar Fabric para ello lo he instalado con el siguiente comando:  
``sudo apt-get install fabric``  
A continuación  creamos un fichero llamado fabfile.py con las funciones que queremos realizar que en mi caso son:  
```
from fabric.api import task, run, local, hosts, cd, env
# Ejecutar la aplicacion
def ejecutar_app():
	run(' sudo python aplicacion-desplegada/manage.py runserver 0.0.0.0:80 & ')
#Borrar la maquina creada
def borrar_app():
    run('sudo rm -r ubuntu-bares')
```
Con esto  ya tendremos todo lo necesario para desplegar la aplicación. Ahora ejecutamos:  
``sudo vagrant up --provider=azure``  
Este comando creará la máquina virtual y ejecutara el fichero de ansible que se encarga de provisionarla. Si ya la tenemos la máquina creada nos bastará con ejecutar:  
`` sudo vagrant provison``   
Por último ejecutaremos la aplicación con el siguiente comando para ejecutar la aplicación:  
``sudo fab -p 'Clave#salva#1' -H vagrant@mundo-bares.cloudapp.net ejecutar_app``   
Aquí podemos ver como se ha creado la máquina virtual en azure que crea en el archivo Vangrantfile y la aplicación corriendo gracias al archivo fabfile.py:  
![imagen](http://i1028.photobucket.com/albums/y349/Salva_Rueda/8_1_zpsgcz7zomy.png)  
![imagen](http://i1028.photobucket.com/albums/y349/Salva_Rueda/9_zpssb7l0duc.png)  
Para poder borrar todo lo que vagrant ha creado se hará con la siguiente línea:   
``vagrant box remove <ubuntu-bares>``  
Para automatizar todo este proceso he creado un script llamado desplegar_IaaS.sh que se encarga de instalar todo lo necesario para el despliege de nuestra aplicación, su contenido es el siguiente:  
```
#!/bin/bash
sudo apt-get install npm
sudo npm install -g azure-cli
sudo apt-get install fabric
sudo apt-get install -y python-pip
sudo pip install paramiko PyYAML jinja2 httplib2 ansible
sudo apt-get install -y vagrant
vagrant plugin install vagrant-azure
sudo vagrant up --provider=azure
sudo fab -p 'Clave#salva#1' -H vagrant@mundo-bares.cloudapp.net ejecutar_app 
```
Tras esto ya tendremos nuestra máquina virtual creada y puesta en marcha, con un solo comando.El enlace de la aplicación es [este](http://mundo-bares.cloudapp.net/).