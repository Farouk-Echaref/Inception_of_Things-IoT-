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

* scaling containers:

    - HPA is best for applications with varying traffic or workloads where scaling out helps distribute the load.(increase or decrease the numbers of pods)
    - VPA is useful for optimizing resource allocation to avoid over-provisioning or under-provisioning individual pods. (adds or limits the resources of the pods)


    ```yaml
    apiVersion: autoscaling/v2beta2  # Specifies the version of the HorizontalPodAutoscaler API
    kind: HorizontalPodAutoscaler    # Defines the resource type as a Horizontal Pod Autoscaler
    metadata:
      name: my-hpa                   # The name of the HPA resource, can be any unique identifier
    spec:
      scaleTargetRef:                # Defines which workload the HPA will target for scaling
        apiVersion: apps/v1          # API version of the workload being scaled (e.g., Deployment, StatefulSet)
        kind: Deployment             # The type of Kubernetes resource being scaled (could be Deployment, StatefulSet, etc.)
        name: my-deployment          # The specific name of the deployment being scaled by this HPA
      minReplicas: 3                 # The minimum number of pod replicas the HPA will maintain, even if resource usage is low
      maxReplicas: 5                 # The maximum number of pod replicas that the HPA can scale up to, regardless of resource usage
      metrics:                       # Defines the metrics that will be used to determine when to scale the workload
      - type: Resource               # Specifies that the metric used for scaling is a Kubernetes resource (CPU in this case)
        resource:                    
          name: cpu                  # Indicates the resource type being monitored, in this case, CPU usage
          target:                    
            type: Utilization        # Specifies that the target is based on CPU utilization percentage (how much of the requested CPU is being used)
            averageUtilization: 65   # The target average CPU utilization across all pods. The HPA will try to maintain 65% CPU utilization
    ```
    
    ### Explanation of Each Section:
    
    1. **apiVersion: `autoscaling/v2beta2`**:
       - Specifies the version of the Kubernetes API that defines how the **HorizontalPodAutoscaler** works. 
       - `v2beta2` includes support for multiple and custom metrics as well as more advanced scaling policies.
    
    2. **kind: `HorizontalPodAutoscaler`**:
       - Indicates that the type of object being defined is a **HorizontalPodAutoscaler**, which dynamically adjusts the number of pod replicas for a   workload based on resource utilization.
    
    3. **metadata**:
       - **name: `my-hpa`**: This is the unique name for the HPA object. You can reference this HPA by this name later.
    
    4. **spec**:
       - This section defines the behavior and metrics that the HPA will use to scale the target workload.
    
    5. **scaleTargetRef**:
       - **apiVersion: `apps/v1`**: Specifies the API version for the resource being scaled. In this case, it's the `apps/v1` API, which is used for    deployments, StatefulSets, and ReplicaSets.
       - **kind: `Deployment`**: Specifies the type of Kubernetes resource being scaled. Here it's a **Deployment**, but it could also be a     **StatefulSet** or **ReplicaSet** depending on your workload.
       - **name: `my-deployment`**: Refers to the specific workload (e.g., a deployment named `my-deployment`) that the HPA is responsible for scaling.     This name should match the name of the actual Kubernetes deployment (or StatefulSet/ReplicaSet).
    
    6. **minReplicas: `3`**:
       - This defines the minimum number of pod replicas that the HPA will maintain, even when the resource usage is low. The HPA will not scale down the   number of replicas below 3, even if the demand drops.
    
    7. **maxReplicas: `5`**:
       - Defines the maximum number of pod replicas that the HPA can scale up to, even if the resource usage is high. This prevents the HPA from    endlessly scaling up.
    
    8. **metrics**:
       - This section defines the metrics that will trigger scaling actions. In this case, it's CPU utilization.
    
       - **type: `Resource`**: Indicates that the metric being used is a Kubernetes resource. The most common resources are CPU and memory.
    
       - **resource**:
         - **name: `cpu`**: Specifies that the HPA should monitor CPU usage.
         - **target**:
           - **type: `Utilization`**: Specifies that the HPA should scale based on the percentage of the requested CPU being used.
           - **averageUtilization: `65`**: This means that the HPA will attempt to maintain an average CPU utilization of 65% across all pods in the    target deployment. If the average CPU utilization goes above 65%, the HPA will scale up (add more pods). If it falls below 65%, it will scale  down (reduce the number of pods), but never below the minimum number of replicas.
    
    ### Summary:
    
    This configuration ensures that:
    - The **`my-deployment`** deployment will always run between 3 and 5 pods.
    - Kubernetes will automatically adjust the number of replicas to keep the average CPU usage across all pods at around **65%**.
    - If CPU usage is low, the number of replicas will decrease, but not below 3 pods.
    - If CPU usage is high, more pods will be added, up to a maximum of 5.