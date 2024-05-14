# Containerized-Flask-App

## Overview
In this project, the overall goal was to create a flask application and containerise it using Docker. As a DevOps Engineer, it's not enough to know how to deploy web applications on the cloud, but also do it quickly and efficiently to ensure reliability - hence the reason I chose to containerise the application, so if anything goes south, I can easily run the `docker-compose` command to spin up the application again.  

## Docker Explanation

Docker is an open-source platform that enables devs to manage, build, deploy or update containerized applications, as well as pull container images from the Docker Hub. Containers are essentially a way to package your applications in an isolated environment, which improves efficiency.

## Main Features in this Project

The code is written in Python, as this is a flask-based application. I followed a tutorial from Tech with Tim's video on YouTube. I then created a Docker image of my app and ran a CI/CD job to launch the app in the production environment once it had successfully launched on the local/dev environment.


