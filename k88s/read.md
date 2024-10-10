# k8s and docker commands

* minkube start (start cluster)
* minikube start --driver=docker
* minikube stop
* minikube delete
* minikube dashboard --url
* docker ps (docker container ls)
* kubectl get nodes (returns active nodes)
* kubectl get po -A (retrieve a list of all Pods running across all namespaces in a cluster)
* create a deployment to manage a pod (the pod runs a container based on the provided docker image):
    - A deployment in Kubernetes manages a set of replicas (pods) and ensures that a specific number of instances of your application are running:

    ```bash
        kubectl create deployment hello-node --image=registry.k8s.io/e2e-test-images/agnhost:2.39 -- /agnhost netexec --http-port=8080
    ```

# Creates a Deployment and a Pod at the same time.

## Breakdown:

### **Deployment Creation:**
- The command starts by creating a Deployment named `hello-node`.
- The Deployment is responsible for managing the lifecycle of the application, which includes ensuring that the desired number of replicas of the pod are running, handling rolling updates, scaling, and self-healing.

### **Pod Creation:**
- Within the deployment definition, the image `registry.k8s.io/e2e-test-images/agnhost:2.39` is used.
- The command defines the container specification for the pod that will be created by the deployment, which runs the `netexec` tool on port 8080.

### **Deployment Automatically Creates Pods:**
- When the deployment is created, Kubernetes automatically creates a pod based on the specifications you provided (i.e., using the `agnhost` image and running the `netexec` command).
- The deployment ensures that the specified number of replicas (in this case, it defaults to 1 pod) are maintained and will handle restarting the pod if it crashes.

## What Happens Internally:
- The command **does not modify an existing pod**. Instead, it creates a new deployment (which is a higher-level resource) and the deployment then creates a pod (or multiple pods, if specified).
- The pod that is created is **managed by the deployment**, and if the pod were to fail or if you scaled the deployment, Kubernetes would automatically create new pods based on the deployment's definition.

## In Summary:
The command creates both:
- A **Deployment** (`hello-node`) to manage the application.
- A **Pod** (or pods, if you scale the deployment) running the `agnhost` container with the specified configuration.

This is typical in Kubernetes, where you generally work with deployments to manage pods efficiently, rather than creating pods directly.


* kubectl get deployments (view deployments)
* kubectl get pods
This command retrieves all the pods in the current namespace where the command is executed.
By default, kubectl works in a specific namespace (usually default unless otherwise configured).
* see cluster events:
    - kubectl get events
* kubectl apply -f <resource.yaml> (activate cluster by applying resources (deployment, servecis...))