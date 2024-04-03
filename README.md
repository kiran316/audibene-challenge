# Backend Service with SQS and DynamoDB Integration
This project demonstrates how to create a simple backend service using Python, SQS (Simple Queue Service), and DynamoDB (Amazon Dynamo Database), and deploy it locally using Docker Compose and in a Kubernetes cluster.

# Setup Instructions
Follow these steps to set up and run the backend service:

### 1. Clone the Repository
git clone https://github.com/kiran316/audibene-challenge
cd audiene-challenge
### 2. Install Dependencies
Ensure you have Docker and Docker Compose installed on your system.

### 3. Configure LocalStack
Install LocalStack: Follow the instructions on the LocalStack GitHub page.
Update the docker-compose.yml file with any necessary configurations for LocalStack.
### 4. Build and Run Docker Compose
docker-compose up -d
### 5. Verify LocalStack Services
Access the LocalStack dashboard to ensure that SQS and DynamoDB services are running locally.
### 6. Deploy Backend Service Locally
The backend service is automatically deployed and running in the Docker container.
Ensure that the SQS queue and DynamoDB table are created by checking the LocalStack services.

### 7. Kubernetes Deployment
Ensure you have a Kubernetes cluster configured and kubectl installed on your system.

### 8. Configure Kubernetes Resources
Update the Kubernetes resource files (deployment.yaml, service.yaml, hpa.yaml, pdb.yaml) with the correct configurations for your backend service image and ports.
### 9. Deploy to Kubernetes Cluster
kubectl apply -f deployment.yaml
kubectl apply -f service.yaml
kubectl apply -f hpa.yaml
kubectl apply -f pdb.yaml
### 10. Verify Kubernetes Deployment
Ensure that the backend service is deployed and running in the Kubernetes cluster.
Check the status of the HorizontalPodAutoscaler and PodDisruptionBudget to confirm proper configuration.

# Assumption
We are assuming that docker registry is in place and image is being downloaded from there.
