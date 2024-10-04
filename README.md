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

## Vagrant course:
* creating a fully functional, ssh enabled ubuntu machine:
*vagrant init bento/ubuntu-16.04*
*vagrant up vagrant up --provider virtualbox*

## k8s vs k3s
https://www.civo.com/blog/k8s-vs-k3s
https://spacelift.io/blog/kubernetes

## vagrant tutorials
https://developer.hashicorp.com/vagrant/docs/cli/ssh
https://developer.hashicorp.com/vagrant/tutorials