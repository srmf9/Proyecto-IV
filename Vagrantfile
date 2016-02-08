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
  config.vm.provider :azure do |azure, override|
      azure.mgmt_certificate = File.expand_path('~/.ssh/azurevagrant.pem') #ruta donde se encuentra el certificado
      azure.mgmt_endpoint = 'https://management.core.windows.net'
      azure.subscription_id = '327715f7-dcef-44ef-bf93-d88889e67cb3' #id del certificado que encontramos en la web
      azure.vm_image = 'b39f27a8b8c64d52b05eac6a62ebad85__Ubuntu-14_04_3-LTS-amd64-server-20151218-en-us-30GB' #imagen de la máquina virtual
      azure.vm_name = 'ubuntu-bares' #nombre de la máquina
      azure.vm_password = 'Clave#salva#1'#nombre de usuario y contraseña
      azure.cloud_service_name = 'mundo-bares'	
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
