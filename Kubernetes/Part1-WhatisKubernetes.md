Part 1 What is Kubernetes

What is kubernetes? 

Kubernetes is an open source container orchestration framework developed by google 
On the foundation it manages containers 
Kuberneets helps manage applications that is made of hundreds or thousands of containers and it helps u manage them in different environemnts like physical virtual or cloud env or hybrid 

What problem does Lubernetes solve? 

The rise of microservices cause increase usage of container technolgies 
Because containers offer the perfect host for small independednt applications liek microservices 

What features do orchestration tools offer?

Hih availability (in simple words the application is always accessible by users ) and no downtime 
Sacalability or high performence (loads fast and users have very high response rates from applocation )
Disastrer recovery - if infra has some probelm say data is lost or server explode or something bad happens with service center , the infra has some mechanism to pick up the data and to restore it to the latest state so the appn does not lose any data - backup and restore 

Kubernetes Basic Architectiure 

One master node and connected to it are worker nodes 
Each node has a kubelet process running on it . Kubelet is a process that makes it possible for the cluster to talk to each other 

Each worker node has docker containers of differnt applications 
