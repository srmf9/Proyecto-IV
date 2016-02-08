from fabric.api import task, run, local, hosts, cd, env
# Ejecutar la aplicacion
def ejecutar_app():
	run(' sudo python aplicacion-desplegada/manage.py runserver 0.0.0.0:80 &')
#Borrar la maquina creada
def borrar_app():
    run('sudo rm -r ubuntu-bares')