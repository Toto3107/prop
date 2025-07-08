# 🔧 Flask CI/CD DevOps Project using Docker, Kubernetes, Helm & GitHub Actions

This project demonstrates a full end-to-end DevOps pipeline for a containerized Flask application using lightweight and production-grade tools like Docker, Kubernetes, Helm, and GitHub Actions.

> ✅ Designed for real-world scenarios with limited hardware (8GB RAM), while retaining core DevOps concepts and automation.

---

## 📦 Tech Stack

| Tool            | Purpose                            |
|-----------------|-------------------------------------|
| **Flask**       | Lightweight Python web application  |
| **Docker**      | Containerization of the app         |
| **DockerHub**   | Image registry                      |
| **Kubernetes**  | Orchestration and deployment        |
| **Helm**        | Kubernetes package management       |
| **GitHub Actions** | CI/CD automation & GitOps-style deployment |
| **Ingress**     | Path-based HTTP routing             |
| **ConfigMap & Secret** | Environment-specific configurations |

---

## 🚀 Features

- ✅ Containerized Flask application
- ✅ Dynamic Helm chart with `values.yaml`
- ✅ ConfigMap for runtime config
- ✅ Kubernetes Secrets for secure values
- ✅ Ingress controller for `/flask` path-based access
- ✅ GitHub Actions CI: Builds and pushes Docker image on push to `main`
- ✅ GitHub Actions CD: Runs `helm upgrade` on push to deploy updated image
- ✅ Git SHA tagging for traceable deployments
- ✅ Fully Git-driven deployments (GitOps-like)

---

## 📁 Project Structure

