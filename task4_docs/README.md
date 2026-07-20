# Task 4: Django E-Commerce CI/CD Pipeline & DevSecOps Integration

This repository contains the containerization configuration and complete **GitLab CI/CD pipeline** for a Python Django e-commerce application. The pipeline automates the software delivery lifecycle from code verification, static code security analysis, and containerization to image vulnerability gatekeeping and automated staging deployments.

---

## Pipeline Workflow & Architecture

The GitLab CI pipeline consists of 6 sequential stages:

```text
 ┌─────────────┐     ┌─────────┐     ┌─────────────┐     ┌─────────────┐     ┌──────────────┐     ┌───────────┐
 │  build_app  │ ──> │  test   │ ──> │  scan_app   │ ──> │ build_image │ ──> │  scan_image  │ ──> │  deploy   │
 └─────────────┘     └─────────┘     └─────────────┘     └─────────────┘     └──────────────┘     └───────────┘
   (App Build)        (pytest)        (DevSecOps)          (Docker)            (Trivy Gate)         (Staging)
