# About The Project

This repository creates a website based on python flask that displays a static HTML page

## Folder Structure
/app: Contains the website source code

/docker: Contains **Dockerfile** to build the image and **docker-compose.yaml** to spin up docker container locally for development purposes

/eks: Contains **cluster.yaml** configuration file to deploy EKS cluster on AWS using **eksctl**

/k8s: Contains k8s manifest files to deploy the required workloads

## Installation

### There are 3 ways to deploy this website: 

### 1. Local Docker Container

**Pre-requisites:**
1. Make sure you have docker installed on your machine
2. Internet access to download the docker image

**Usage**

Execute the following command on your terminal
```
docker-compose -f ./docker/docker-compose.yaml up
```
Once done, you should be able to access the website on:

```
http://localhost:8080/
```

you can press Ctrl+C on your keyboard once you're done to stop the web server from running

### 2. Amazon EKS
**Pre-requisites:**

1. AWS Account
2. Have a working EKS cluster. 

**If you don't have an EKS cluster ready please refer to /eks/cluster.yaml for instructions**

3. Have the proper permission to spin up workloads on the EKS cluster

**Usage**

Execute the following command on your terminal:
```
kubectl apply -f "./k8s/*.yaml"
```

Once done, you can access the website by using the load balancer URL created by the LoadBalancer service

To clean up the environment, execute the following command on your terminal:
```
kubectl delete -f "./k8s/*.yaml"
```

### 3. Local Kubernetes Cluster
**Pre-requisites:**

1. Have a working EKS cluster locally.
2. Have the proper permission to spin up workloads on the local cluster
3. Change the service type on ./k8s/services.yaml to NodePort

**Usage**

Execute the following command on your terminal:
```
kubectl apply -f "./k8s/*.yaml"
```

Once done, you should be able to access the website on:
```
http://localhost:31590
```

To clean up the environment, execute the following command on your terminal:
```
kubectl delete -f "./k8s/*.yaml"
```

### Contact

Brian C.
