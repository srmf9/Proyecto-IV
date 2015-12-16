## Creación de un entorno de pruebas para la aplicación

Lo primero que debemos de hacer es crear el fichero Dockerfile para el despliegue de la aplicación dicho fichero contiene:  
- Sistema operativo que se usa.  
- Creador de la aplicación.  
- Actualización de paquetes.  
- Instalación de las herramientas git.  
- Instalar python versión 2.7.  
- Bajarse la aplicación de GitHub.  
- Instalar las dependencias.  
- Migrar la base de datos.  
- Instalar el curl para comprobar las direcciones IP  .

El contenido del fichero puede ser visto [aquí](https://github.com/srmf9/Proyecto-IV/blob/master/Dockerfile).  

Debe estar en la carpeta raiz de nuestra aplicación.

Ahora procedemos a registrarnos en [Docker hub](https://hub.docker.com/) y sincronizarmos nuestra cuenta con la de GitHub:   
![imagen](http://i1028.photobucket.com/albums/y349/Salva_Rueda/Captura%20de%20pantalla%20de%202015-12-16%20100439_zpsj8ehbyjc.png)

Una vez enlazado creamos en el apartado Create Automated Build la imagen del proyecto que queramos en nuestro caso la aplicación de IV. Recordar que cada cambio que se realize en el repositorio será integrado en DockerHub.  
[Aquí](https://hub.docker.com/r/srmf9/proyecto-iv/) se puede ver la imagen en DockerHub.  
La imagen para descargarla deberemos escribir `docker pull srmf9/proyecto-iv`.  
Para automatizar este proceso he creado un script que ejecutandolo estaremos dentro del contenedor. El contenido del script puede ser visto [aquí](https://github.com/srmf9/Proyecto-IV/blob/master/docker.sh).  
![imagen](http://i1028.photobucket.com/albums/y349/Salva_Rueda/Captura%20de%20pantalla%20de%202015-12-16%20120619_zpsyr99k27e.png)

Para comprobar su funcinamiento hago lo mismo que el ejercicio 10 ejecutando la aplicación y viendo la dirección ip:  
![imagen](http://i1028.photobucket.com/albums/y349/Salva_Rueda/Captura%20de%20pantalla%20de%202015-12-16%20121329_zps8qaoen8t.png)
 