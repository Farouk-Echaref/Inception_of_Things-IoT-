# Inception_of_Things-IoT-
This project aims to introduce you to kubernetes from a developer perspective. You will have to set up small clusters and discover the mechanics of continuous integration. At the end of this project you will be able to have a working cluster in docker and have a usable continuous integration for your applications. 

## Vagrant Docs:

* install a box: *vagrant box add hashicorp/bionic64*
* initialize vagrant : *vagrant init hashicorp/bionic64*
* start the VM: *vagrant up*
* connect to the machine : *vagrant shh (default)*
* disconnect from the machine: *logout*
* list boxes: *vagrant box list*
* destroy the machine: *vagrant destroy*
* remove a box: *vagrant box remove hashicorp/bionic64*
* *Vagrant Share* (HTTP Sharing, SSH Sharing, General Sharing) (needs Ngrok)
* Suspending the virtual machine will stop it and save its current running state: *vagrant suspend*
* gracefully shut down the guest operating system and power down the guest machine: *vagrant halt*

## Vagrant provisioning:
Provisioning is the process of setting up the software and configuration on a VM or server automatically. In the context of Vagrant, provisioning can include:

* Installing necessary software (e.g., web servers like Apache or Nginx, databases like MySQL or PostgreSQL, programming languages, etc.).
* Configuring the operating system (e.g., setting environment variables, user permissions, network settings).
* Deploying code or running scripts to set up a working development environment.

1. *Shell Script Provisioner*: You can write bash scripts or any shell script and Vagrant will run them to install and configure software:

```ruby
config.vm.provision "shell", inline: <<-SHELL
  sudo apt-get update
  sudo apt-get install -y apache2
SHELL
```

2. *Ansible*: A provisioning tool that uses playbooks (scripts written in YAML) to configure the environment:

```ruby
config.vm.provision "ansible" do |ansible|
  ansible.playbook = "playbook.yml"
end
```

3. *Puppet*: A configuration management tool that Vagrant can use to apply configurations:

```ruby
config.vm.provision "puppet" do |puppet|
  puppet.manifests_path = "manifests"
  puppet.manifest_file  = "default.pp"
end
```

4. *Chef*: Another configuration management tool supported by Vagrant:

```ruby
config.vm.provision "chef_solo" do |chef|
  chef.add_recipe "nginx"
end
```

* https://developer.hashicorp.com/vagrant/tutorials/networking-provisioning-operations/getting-started-provisioning

## Vagrant course:
* creating a fully functional, ssh enabled ubuntu machine:
*vagrant init bento/ubuntu-16.04*
*vagrant up --provider virtualbox*

## k8s vs k3s
https://www.civo.com/blog/k8s-vs-k3s
https://spacelift.io/blog/kubernetes

## vagrant tutorials
https://developer.hashicorp.com/vagrant/docs/cli/ssh
https://developer.hashicorp.com/vagrant/tutorials