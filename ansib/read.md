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

* An Ansible playbook is a configuration management script written in YAML format, used to define a series of tasks that Ansible should execute on one or more managed hosts. Playbooks are the core of Ansible’s automation framework, allowing you to describe how systems should be configured, services deployed, and workflows orchestrated.

* Playbook = plays + modules + plugins, and it runs against inventory.


# running ansible playbook:

```bash
    ansible-playbook pb.yml -f 10
```

The command `ansible-playbook playbook.yml -f 10` is used to execute an Ansible playbook (`playbook.yml`) with **parallelism** control. Here’s a breakdown of each part of the command:

### 1. `ansible-playbook playbook.yml`
- **`ansible-playbook`**: This is the Ansible command to run a playbook, which is a YAML file that contains a series of tasks and instructions for configuring and managing remote hosts.
- **`playbook.yml`**: This is the playbook file you want to execute. It contains all the tasks, hosts, and roles defined for your automation.

### 2. `-f 10`
- **`-f` (or `--forks`)**: This option controls the number of **parallel processes** (or forks) that Ansible will use to execute tasks across multiple hosts.
  - By default, Ansible runs with `-f 5`, meaning it executes tasks on 5 hosts at a time in parallel.
  - In this case, `-f 10` tells Ansible to execute the playbook on up to 10 hosts simultaneously.
  
### Why Use `-f 10`?
- **Parallelism**: If you’re managing a large number of hosts, running tasks in parallel speeds up execution. For example, if you're deploying software or updating configurations on 50 servers, running in parallel allows Ansible to configure multiple hosts at once.
- **Efficiency**: By increasing the number of forks, you can make better use of system resources (CPU, network bandwidth) to process more hosts in parallel, reducing the overall time to complete the playbook.
  
### Example Scenario:
- Imagine you have 100 web servers that you want to update using your playbook. Without the `-f` flag, Ansible defaults to running the playbook on 5 servers at a time.
- By specifying `-f 10`, Ansible will run the playbook on 10 servers at once, significantly speeding up the process.

### Caveats:
- **System Resource Limits**: Running too many forks in parallel can overwhelm your system resources (e.g., CPU, memory, network bandwidth), especially if the tasks are resource-intensive. In practice, you should choose a number that balances speed and system load.
- **SSH Connection Limits**: If you’re using SSH to connect to remote hosts, keep in mind that some systems may limit the number of simultaneous SSH connections. Make sure your control node and managed nodes can handle the number of connections specified by `-f`.

### Summary:
The command `ansible-playbook playbook.yml -f 10` runs the playbook `playbook.yml` on up to 10 hosts at a time in parallel. This is useful for speeding up the execution of tasks when managing a large number of hosts.

# running a dry run of ansible:

```bash
    ansible-playbook --check pb.yml

```