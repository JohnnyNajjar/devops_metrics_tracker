[![Build Status](https://github.com/JohnnyNajjar/devops_metrics_tracker/actions/workflows/docker-build.yml/badge.svg)](https://github.com/JohnnyNajjar/devops_metrics_tracker/actions/workflows/docker-build.yml)
[![GitHub last commit](https://img.shields.io/github/last-commit/JohnnyNajjar/devops_metrics_tracker.svg)](https://github.com/JohnnyNajjar/devops_metrics_tracker/commits/main)

# DevOps Metrics Tracker

This project is a simple, containerized Python application with a CI/CD pipeline.  
It's designed for deployment and testing in a DevOps environment using GitLab CI and Docker.

---

##  Tech Stack

- Python  
- Docker  
- GitLab CI/CD  
- Bash scripting

---

##  How to Run

Build the Docker container:

```bash
docker build -t devops-tracker .
```

Run the container:

```bash
docker run -p 8000:8000 devops-tracker
```

Then go to:  
http://localhost:8000

---

##  CI/CD

This repo includes a `.gitlab-ci.yml` file that handles:

- Docker image build
- Unit tests
- Deployment steps (extend to your environment)

---

##  Project Structure

```
├── app/
│   ├── main.py
│   └── ...
├── ci/
│   └── (pipeline scripts/config)
├── deploy.sh
├── Dockerfile
├── .gitlab-ci.yml
└── .gitignore
```

---

##  Maintainer

Johnny Najjar  
[johnny.najjar.dev@gmail.com](mailto:johnny.najjar.dev@gmail.com)

