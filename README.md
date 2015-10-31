# Proyecto-IV
## Salvador Rueda Molina
## Primer hito
Mi proyecto se basará en dar soporte y desplegar  una aplicación web que creare en la asignatura de DAI.

Seguramente en ella hago uso de varios servidores web y probablemente  utilice un balanceador de carga.

El objetivo será cubrir todos los requisitos de la aplicación de forma automática para que el usuario solo se tenga que preocuparse de usar la aplicación.
Las herramienas que he utiliado son:     
-De lenguaje de programación usado Python    
-Framework usado Django  
-Base de datosusada SQLite  

## Segundo hito

![Sin titulo](https://travis-ci.org/srmf9/Proyecto-IV.svg?branch=master)  
 Para superar este segundo hito he decidido crear una aplicación basandome en el tutorial de django. Más adelante cuando avancemos en la asignatura de DAI pondré la aplicación definitiva pero será usando django y con python. Mientras tanto utilizare esta aplicación para pasarle los test y realizar la integración continua.  
##Las herramienas que he utiliado han sido:  
-Lenguaje de programación->Python.  
-Framework -> Django.  
-Base de datos->SQLite

## Test 
Aqui dejo el enlace de los test que he decidido utilizar. [Test](aplicacion/encuestas/test.py)  
Para ejecutar los test basta con escribir:   
~~~
python manage.py test encuestas 
~~~
Con estos test puedo permitir encontrar fallos para su posterior programación y correción(TDD).
Test es un sistema que ofrece Django de muy fácil uso ya que viene integrado en el framework y con el que comodamente podemos ejecutar y comprobar nuestros test, es por eso que he decidido utilizar este metodo. 

##Herramientas de construción
He decido crear un makefile para realizar todas las tareas con una sola orden. Podeis consultar [aqui](aplicacion/encuestas/Makefile) el makefile.  
El funcionamiento del makefile es el siguiente:  
  
-make run: Ejecuta la aplacación.  

-make test: Lanza los test para comprobar el correcto funcionaiento de la aplicación.  

-make install: Se encarga de instalar todas las dependencias necesarias para el funcionamiento de la aplicación que se encuentran en el fichero setup.py.   

-make clean: Borra todos los .py y .pyc.
## Integración continua
Para conseguir la integración continua he decido usar Travis por su facilidad de uso y por poder conectarse directamente con GitHub.
Para que funcione correctamente he creado un fichero setup.py que contiene las dependencias de mi aplicación.  
setup.py 
~~~ 
from distutils.core import setup

setup(name='Encuestas',

      version='1.0',
      description='Aplicacion web sobre encuestas',
      author='Salvador Rueda Molina',
      author_email='salviwui@gmail.com',
      url='enlace',
      packages=['aplicacion'],
      install_requires=['django', 'wheel'],
     )
~~~

Tambíen necesitamos un fichero llamado .travis.yml que sera el encargado de instalar todas las dependencias y de ejecutar  los test, estas operaciones las realizo con el makefile que he creado. El objetivo de usar el makefile es poder realizar tareas con una sola orden. 
.travis.yml  
~~~
language: python
python:
 - "2.7"
before_install:
 - cd aplicacion
 install:
 - make install
 script:
 - make test
~~~

Si la ejecución tiene éxito tendremos la siguiente captura:
![Sin titulo](http://i1028.photobucket.com/albums/y349/Salva_Rueda/Eje8_zps3sfezoti.png)