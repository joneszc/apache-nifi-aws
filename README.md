# Docker-compose Deployment for Apache NiFi

### Overview
This docker-compose stack deploys Apache NiFi, Apache NiFi-Registry (for version control + persistence), Apache NiFi-Toolkit (for creating certs), Nginx (load-balancer), Zookeeper, and also Kafka.

The container images for NiFi, NiFi-Registry, Nginx, Zookeeper, NiFi-Toolkit and Kafka:
 
	- apache/nifi:1.17.0
	
	- confluentinc/cp-zookeeper:7.2.1-1

	- apache/nifi-registry:1.16.3

	- nginx:1.23.1

	- confluentinc/cp-kafka

	- apache/nifi-toolkit:1.17.0

# Running the docker stack for the first time:

Use:
`cd docker`

Build images, use: 
`make`

Configure Environment Variables in files docker-compose-nifi.env, docker-compose-nifitoolkit.env and docker-compose-kafka.env

After executing `make` to build the NiFi and NiFi-Toolkit images, use the following command to run the docker-compose stack locally or on ec2 ("../cloudformation/ec2_mxsDataAppsTemplate-nifi.yaml")

`docker-compose up -d`

### Login to NiFi using Web UI
Open `https://localhost:8080/nifi` (or ec2 public DNS--edit env vars in .env files) in your local browser

### Login to NiFi-Registry using Web UI
Open `http://localhost:18080/nifi-registry` (or ec2 public DNS) in your local browser

### Connect NiFi to NiFi-Registry using URL
`http://nifi-registry:18080`
