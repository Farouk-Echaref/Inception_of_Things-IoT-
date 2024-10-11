# k8s and docker commands

* A Pod is a group of one or more application containers (such as Docker) and includes shared storage (volumes), IP address and information about how to run them.
* A Deployment is responsible for creating and updating instances of your application.
* Applications need to be packaged into one of the supported container formats in order to be deployed on Kubernetes.
* Containers should only be scheduled together in a single Pod if they are tightly coupled and need to share resources such as disk.
* A node is a worker machine in Kubernetes and may be a VM or physical machine, depending on the cluster. Multiple Pods can run on one Node.

The common format of a kubectl command is: `kubectl action resource`

* minikube start --driver=docker --nodes 3 --memory 4g --cpus 2
    This command starts a Minikube cluster with 3 nodes using Docker as the driver, allocating 4GB of memory and 2 CPUs to each node.

* minkube start (start cluster)
* minikube start --driver=docker
* minikube stop
* minikube delete
* minikube dashboard --url
* docker ps (docker container ls)
* kubectl get nodes (returns active nodes)
* kubectl get po -A (retrieve a list of all Pods running across all namespaces in a cluster)
* kubectl exec -ti hello-node-66d457cb86-7fn26  -- bash 
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
* kubectl get all (infos about pods, deploys... in default namespace) 
* kubectl get all  -A (infos about pods, deploys... in default namespace) 
* kubectl get ns (get namespaces)
* kubectl get events (get events in default namespace)
* kubectl get events -A
* kubectl get events -w (watch for events)
* kubectl get pods -n default (get pods in specific namespace)
* kubectl get services
* minikube service hello-node
* kubectl get nodes
* kubectl describe resource_name
* kubectl config view (kubectl config)
* kubectl logs pod_name


```bash
kubectl expose deployment hello-node --type=LoadBalancer --port=8080
```

# Exposing a Kubernetes Deployment as a Service

The command is used to expose a Kubernetes deployment as a service, making the application accessible externally, typically via an external load balancer. Here’s a breakdown of what each part of the command does:

## Breakdown:

### **`kubectl expose`:**
- The `expose` command is used to create a Kubernetes **Service** that exposes a resource (such as a pod, deployment, or replica set) to make it accessible over the network.
- In this case, the resource being exposed is a **Deployment**.

### **`deployment hello-node`:**
- This specifies the **deployment** that you want to expose. The `hello-node` deployment refers to the set of pods created by the deployment you previously created.
- The service will route traffic to the pods managed by this deployment.

### **`--type=LoadBalancer`:**
- The `--type` flag specifies the type of service to create.
- `LoadBalancer` is a type of service that provisions an external load balancer to route traffic to the Kubernetes pods. This is typically used for exposing applications to the internet or external networks.
- When you create a `LoadBalancer` service in Kubernetes, the cloud provider (like AWS, GCP, Azure, etc.) will automatically create an external load balancer and assign an external IP address to the service.

### **`--port=8080`:**
- The `--port` flag specifies the port on which the service will be exposed.
- In this case, the service will be accessible on **port 8080** externally.
- Internally, the service will forward traffic on port 8080 to the containers running inside the pods. This is useful for web servers or applications that listen on specific ports.

## What Happens After Running the Command?
- A Kubernetes **Service** is created of type `LoadBalancer` that:
  - Exposes your deployment (`hello-node`) externally on port 8080.
  - Creates an external load balancer (provided by the cloud platform) to distribute incoming traffic across your pods.
  - The service will map the external port 8080 to the port on which your application (inside the pods) is running.

## Typical Use Case:
- You typically use this command when you want to expose an application running in your Kubernetes cluster to the outside world and allow external users or systems to access it.
- **`LoadBalancer`** type services are particularly useful in cloud environments where Kubernetes can automatically provision an external load balancer, making it easy to expose your application to external clients.

## Example Flow:
1. A user sends a request to the **external IP** provided by the cloud provider (via the Load Balancer).
2. The Load Balancer forwards this request to one of the pods running your `hello-node` application.
3. The request is processed by the pod, and the response is sent back to the user.

## Summary:
- **`kubectl expose`** creates a Kubernetes **Service** to expose a Deployment.
- **`--type=LoadBalancer`** makes the service accessible externally via a cloud-provided load balancer.
- **`--port=8080`** specifies that the service will be available on port 8080.
  
This is commonly used for making web applications or APIs available to external clients.
* view services:
    - kubectl get services
     On minikube, the LoadBalancer type makes the Service accessible through the minikube service command.

Run the following command:

minikube service hello-node
This opens up a browser window that serves your app and shows the app's response

* kubectl apply -f <resource.yaml> (activate cluster by applying resources (deployment, servecis...))

## k8s services:

* A Kubernetes Service is an abstraction layer which defines a logical set of Pods and enables external traffic exposure, load balancing and service discovery for those Pods.
* A Service routes traffic across a set of Pods. Services are the abstraction that allows pods to die and replicate in Kubernetes without impacting your application. Discovery and routing among dependent Pods (such as the frontend and backend components in an application) are handled by Kubernetes Services.

* kubectl describe services/kubernetes-bootcamp

* services and labels and selectors

Create an environment variable called NODE_PORT that has the value of the Node port assigned:

export NODE_PORT="$(kubectl get services/kubernetes-bootcamp -o go-template='{{(index .spec.ports 0).nodePort}}')"
echo "NODE_PORT=$NODE_PORT"

Now we can test that the app is exposed outside of the cluster using curl, the IP address of the Node and the externally exposed port:

curl http://"$(minikube ip):$NODE_PORT"

### using labels:

* check infos about labels and selectors:
    - kubectl describe deployment/kubernetes-bootcamp

https://kubernetes.io/docs/tutorials/kubernetes-basics/expose/expose-intro/

## Scaling:

* Scaling is accomplished by changing the number of replicas in a Deployment.
* You can create from the start a Deployment with multiple instances using the --replicas parameter for the kubectl create deployment command.
* Running multiple instances of an application will require a way to distribute the traffic to all of them. Services have an integrated load-balancer that will distribute network traffic to all Pods of an exposed Deployment. Services will monitor continuously the running Pods using endpoints, to ensure the traffic is sent only to available Pods.
* see the ReplicaSet created by the deployment:
    - kubectl get rs
* scale the Deployment to 4 replicas(scale up):
    - kubectl scale deployments/kubernetes-bootcamp --replicas=4
* check all the infos about the new pods:
    - kubectl get pods -o wide

* scale down : 
    - kubectl scale deployments/kuberenetes-bootcamp --replicas=2

## rolling updates:

* Rolling updates allow Deployments' update to take place with zero downtime by incrementally updating Pods instances with new ones.
* The new Pods are scheduled on Nodes with available resources, and Kubernetes waits for those new Pods to start before removing the old Pods.

* To update the image of the application to version 2, use the set image subcommand, followed by the deployment name and the new image version:

    - kubectl set image deployments/kubernetes-bootcamp kubernetes-bootcamp=docker.io/jocatalin/kubernetes-bootcamp:v2.

* The command notified the Deployment to use a different image for your app and initiated a rolling update. Check the status of the new Pods, and view the old one terminating with the `get pods` subcommand.

* You can also confirm the update by running the rollout status subcommand:

    - kubectl rollout status deployments/kubernetes-bootcamp (output: deployment "kubernetes-bootcamp" successfully rolled out)

Roll back an update
Let’s perform another update, and try to deploy an image tagged with v10:

kubectl set image deployments/kubernetes-bootcamp kubernetes-bootcamp=gcr.io/google-samples/kubernetes-bootcamp:v10

Use get deployments to see the status of the deployment:

kubectl get deployments

Notice that the output doesn't list the desired number of available Pods. Run the get pods subcommand to list all Pods:

kubectl get pods

Notice that some of the Pods have a status of ImagePullBackOff.

To get more insight into the problem, run the describe pods subcommand:

kubectl describe pods

In the Events section of the output for the affected Pods, notice that the v10 image version did not exist in the repository.

To roll back the deployment to your last working version, use the rollout undo subcommand:

kubectl rollout undo deployments/kubernetes-bootcamp

The rollout undo command reverts the deployment to the previous known state (v2 of the image). Updates are versioned and you can revert to any previously known state of a Deployment.

Use the get pods subcommand to list the Pods again:

kubectl get pods

To check the image deployed on the running Pods, use the describe pods subcommand:

kubectl describe pods

The Deployment is once again using a stable version of the app (v2). The rollback was successful.

Remember to clean up your local cluster

kubectl delete deployments/kubernetes-bootcamp services/kubernetes-bootcamp

