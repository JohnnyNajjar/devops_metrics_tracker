[![Build Status](https://github.com/JohnnyNajjar/devops_metrics_tracker/actions/workflows/docker-build.yml/badge.svg)](https://github.com/JohnnyNajjar/devops_metrics_tracker/actions/workflows/docker-build.yml)
[![GitHub last commit](https://img.shields.io/github/last-commit/JohnnyNajjar/devops_metrics_tracker.svg)](https://github.com/JohnnyNajjar/devops_metrics_tracker/commits/main)

# DevOps Metrics Tracker

This project is a simple, containerized Python application with a CI/CD pipeline.  
It's designed for deployment, testing, and observability in a modern DevOps environment using GitHub Actions, GitLab CI, Docker, and Apache Spark.

---

## 🚀 Tech Stack

- Python
- Apache Spark (via PySpark)
- Docker
- GitHub Actions & GitLab CI/CD
- Bash scripting

---

## 🛠️ How to Run

### Build the Docker container:

```bash
docker build -t devops-tracker .
```

### Run the container:

```bash
docker run -p 8000:8000 devops-tracker
```

Then open: [http://localhost:8000](http://localhost:8000)

---

## ⚙️ CI/CD Pipelines

### GitHub Actions (`.github/workflows/docker-build.yml`)

Handles:

- Building and pushing Docker image to GitHub Container Registry
- Running Python unit tests inside the container

### GitLab CI (`.gitlab-ci.yml`)

Handles:

- Docker image build
- Unit tests
- Deployment steps (customizable)

---

## 📁 Project Structure

```
├── app/
│   ├── main.py
│   ├── test_main.py
│   └── requirements.txt
├── ci/
│   ├── build.yml
│   ├── test.yml
│   └── deploy.yml
├── deploy.sh
├── Dockerfile
├── .gitlab-ci.yml
├── .github/
│   └── workflows/
│       └── docker-build.yml
├── .gitignore
├── .dockerignore
├── docker-compose.yml
└── README.md
```

---

## 🧪 Testing & Quality

- Unit tests using `unittest`
- Future additions: linting with `flake8` or `black`, test coverage badge
- Extend pipelines to enforce code quality on PRs

---

## 🔐 Security

- Use Dependabot to monitor dependencies
- Branch protection enabled on `main`
- Secrets managed via GitHub/GitLab environments

---

## 📬 Maintainer

Johnny Najjar  
[johnny.najjar.dev@gmail.com](mailto:johnny.najjar.dev@gmail.com)

