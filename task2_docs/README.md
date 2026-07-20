# Task 2: Multi-Node Kubernetes Cluster Setup & Application Exposure

This repository contains the deployment configuration and setup instructions for building a multi-node local Kubernetes cluster using **KinD** (Kubernetes in Docker), deploying an **NGINX Ingress Controller**, and exposing the **OWASP Juice Shop** web application.

---

## 🏗 Architecture Overview

* **Cluster Topology**: 1 Control-Plane Node (Master) + 2 Worker Nodes.
* **Ingress Controller**: NGINX Ingress Controller listening on HTTP (80) and HTTPS (443).
* **Application**: OWASP Juice Shop (`bkimminich/juice-shop:latest`).
* **Service Type**: `ClusterIP` exposed externally via NGINX Ingress rules.

---

