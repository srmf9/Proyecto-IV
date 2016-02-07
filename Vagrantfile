# -*- mode: ruby -*-
# vi: set ft=ruby :

# Vagrantfile API/syntax version. Don't touch unless you know what you're doing!
VAGRANTFILE_API_VERSION = "2"

Vagrant.configure(VAGRANTFILE_API_VERSION) do |config|
  # The most common configuration options are documented and commented below.
  # For a complete reference, please see the online documentation at
  # https://docs.vagrantup.com.

  # Every Vagrant development environment requires a box. You can search for
  # boxes at https://atlas.hashicorp.com/search.
  config.vm.box = 'azure'
  config.vm.network "public_network"
  config.vm.network "private_network",ip: "192.168.56.10", virtualbox__intnet: "vboxnet0"
  config.vm.network "forwarded_port", guest: 80, host: 80
  config.vm.define "localhost" do |l|
          l.vm.hostname = "localhost"
   end

  config.vm.provider :azure do |azure, override|
      azure.mgmt_certificate = File.expand_path('~/.ssh/azurevagrant.pem') 
      azure.mgmt_endpoint = 'https://management.core.windows.net'
      azure.subscription_id = '327715f7-dcef-44ef-bf93-d88889e67cb3'
      azure.vm_image = 'b39f27a8b8c64d52b05eac6a62ebad85__Ubuntu-14_04_3-LTS-amd64-server-20151218-en-us-30GB'
      azure.vm_name = 'ubuntu-iv-eje8'
      azure.vm_password = 'Clave#salva#1'	
      azure.vm_location = 'Central US' 
      azure.ssh_port = '22'
      azure.tcp_endpoints = '80:80'
  end
  
  
  config.vm.provision "ansible" do |ansible|
        ansible.sudo = true
        ansible.playbook = "provision.yml"
        ansible.verbose = "v"
        ansible.host_key_checking = false
  end
end
