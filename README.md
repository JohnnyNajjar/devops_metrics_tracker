[!Build Status](https://github.com/JohnnyNajjar/devops_metrics_tracker/actions/workflows/docker-build.yml/badge.svg)](https://github.com/JohnnyNajjar/devops_metrics_tracker/actions/workflows/docker-build.yml)
[![GitHub last commit](https://img.shields.io/github/last-commit/JohnnyNajjar/devops_metrics_tracker.svg)](https://github.com/JohnnyNajjar/devops_metrics_tracker/commits/main)

# DevOps Metrics Tracker

This project is a simple, containerized Python application with a CI/CD pipeline.  
It's designed for deployment and testing in a DevOps environment using GitHub Actions, GitLab CI, Docker, and Spark.

---

## 🔧 Tech Stack

- Python  
- Docker  
- GitHub Actions & GitLab CI/CD  
- Bash scripting  
- Apache Spark (via PySpark)

---

## 🚀 How to Run

**Build the Docker container:**

```bash
docker build -t devops-tracker .
```

**Run the container:**

```bash
docker run devops-tracker
```

The container runs a simple Spark job, processes mock data, and exits.
You’ll see output like:

```
Filtered records: [Row(name='Alice', age=34), Row(name='Bob', age=45)]
✅ Spark job completed successfully
```

> Note: This is not a web app. There is no web server or `http://localhost:8000` page.

---

## 🔁 CI/CD Pipelines

### GitHub Actions (`.github/workflows/docker-build.yml`)

- Build and push Docker image to GitHub Container Registry  
- Run unit tests inside the container

### GitLab CI (`.gitlab-ci.yml`)

- Docker image build  
- Unit tests  
- Deployment steps (extend to your environment)

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
├── docker-compose.yml
└── README.md
```

---

## 🧽 .dockerignore

```
.git
.gitlab-ci.yml
.github
ci/
app/test_*.py
*.pyc
__pycache__/
docker-compose.yml
README.md
```

---

## ✅ Recommendations

1. **Split CI into multiple jobs** (build, lint, test, deploy)
2. **Add flake8 or black checks**
3. **Enable test coverage (Codecov or similar)**
4. **Add semantic versioning + GitHub release automation**
5. **Protect main branch + enable Dependabot**
6. **Add screenshots or output examples in README**
7. **Add badge for test coverage**

---

## 👤 Maintainer

**Johnny Najjar**  
[johnny.najjar.dev@gmail.com](mailto:johnny.najjar.dev@gmail.com)
