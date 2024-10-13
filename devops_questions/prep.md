# bash:
- check if a file exist:
    test -e file_name && echo TRUE
- Rename all .txt files to .log in a path:
```bash
    ls *.txt | cut -d. -f1 | xargs -i mv {}.txt {}.log
```
- command line args:
    ```bash
    #!/bin/sh
        echo "Script Name: $0"
        echo "First Parameter of the script is $1"
        echo "The second Parameter is $2"
        echo "The complete list of arguments is $@"
        echo "Total Number of Parameters: $#"
        echo "The process ID is $$"
        echo "Exit code for the script: $?"
    ```
- check if a file exist using the if else condition:
    ```bash
    #!/bin/sh

        if [ -f file_name ]
        then
            echo "TRUE"
        fi
    ```

- using the special exit status variable:

    ```bash
    #!/bin/bash

    # execute a command
    cp path/file path2

    #check exit status

    if [ @? -eq 0 ]
    then
        echo "command executed correctly"
    else
        echo "command failed"
    fi
    ```

# GIT:

- git pull = git fetch + git merge

- revert a commit :
    * git log / git reflog
    * git revert <commmit_hash>
    * make changes
    * git commit 
    * git push origin <branch-name>

- git reset (--soft, --reset, --hard)
- git stash/ git pop
- git log/ git reflog

- make an existing GIT branch track a remote branch:

```bash
git branch --set-upstream-to=<remote-name>/<branch-name>
git branch -u <remote-name>/<branch-name>
```

# Docker:

- critical docker commands:
    * build, create, run, commit, kill

- stored docker volumes:
    * /var/lib/docker/volumes

- check docker client and server version:
    * docker version

- create a container from an image and run it in interactive mode and in the background:
    * docker run -it -d <docker_image>

- stop a container:
    * docker stop <container_name>

- list all the running containers:
    * docker ps
    * docker container ls

- clean docker system:
    * docker system prune

- show info about docker:
    * docker info

- download an image:
    * docker pull

- container info:
    * docker stats

- show images:
    * docker images

- remove a container:
    * docker stop <container_name>
    * docker rm -f <container_name>

- show all containers (running and stoped):
    * docker ps -a

- delete an image:
    * docker image rm <image_name>

- remove all stopped containers:
    * docker container prune

- stop a container:
    * docker stop

- restart a container:
    * docker restart

- The following command is used to know number of container are in running state:

    * docker ps -q | wc -l

- The following command is used to know number of container are in paused state:

    * docker ps -aq -f  "status=paused" | wc -l

- The following command is used to know number of containers are in stopped state:

    * docker ps -aq -f  "status=exited" | wc -l

- docker compose questions:
    * https://github.com/Farouk-Echaref/42_Inception/blob/master/srcs/docker-compose.yml
    * https://github.com/mrbardia72/docker-Interview-Questions-and-Answers/blob/main/docker-compose.md
    * https://www.geeksforgeeks.org/docker-interview-questions/

# Kubernetes:

* Pod : collection of one or more Linux Containers, smallest unit in k8s.
* get pods in a namespace:
    - kubectl get pods -n <namespace_name>
