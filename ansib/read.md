# building an inventory:

* An Ansible inventory is a file that defines the hosts (machines) and groups of hosts that Ansible will manage. It’s a crucial part of how Ansible works, as it specifies the systems where Ansible will run tasks or execute playbooks.

* Add a new [myhosts] group to the inventory.ini file and specify the IP address or fully qualified domain name.

    ```INI
        [myhosts]
        192.0.2.50
        192.0.2.51
        192.0.2.52
    ```
* Verify your inventory:
    - ansible-inventory -i inventory.ini --list
* Ping the [myhost] group in the inventory :
    - ansible myhost -m ping -i inventory.ini 
    => Inventory built.


# Ansible Playbook:

