# sample-app

A small Flask API used as the demo workload for my Terraform, Kubernetes and CI/CD projects.

## Run locally with Docker
    docker build -t sample-app:0.1 .
    docker run --rm -p 8080:8080 sample-app:0.1
    curl localhost:8080/health

## Endpoints
- `/health` health check
- `/` basic info with the host name
- `/api/slots` sample appointment slots
