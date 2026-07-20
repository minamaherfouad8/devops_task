# Task 2: Multi-Node Kubernetes Cluster Setup & Application Exposure

This repository contains the deployment configuration and setup instructions for building a multi-node local Kubernetes cluster using **KinD** (Kubernetes in Docker), deploying an **NGINX Ingress Controller**, and exposing the **OWASP Juice Shop** web application.

---

## 🏗 Architecture Overview

* **Cluster Topology**: 1 Control-Plane Node (Master) + 2 Worker Nodes.
* **Ingress Controller**: NGINX Ingress Controller listening on HTTP (80) and HTTPS (443).
* **Application**: OWASP Juice Shop (`bkimminich/juice-shop:latest`).
* **Service Type**: `ClusterIP` exposed externally via NGINX Ingress rules.

---
## 📁 Repository Structure

```text
.
├── kind-config.yaml    # KinD multi-node cluster topology & host port mappings
├── deployment.yaml     # Kubernetes Deployment manifest for OWASP Juice Shop
├── service.yaml        # Kubernetes ClusterIP Service routing definition
├── ingress.yaml        # NGINX Ingress rule routing HTTP traffic to Service
└── README.md           # Detailed task documentation and architectural guidelines

```


[ User / Browser ]
          │
          ▼  (HTTP / Port 80)
┌─────────────────────────────────────────────────────────────┐
│  Host Machine (Local Computer)                              │
│         │                                                   │
│         ▼  (ExtraPortMapping: hostPort 80 -> containerPort 80)
│  Control Plane Node (KinD Container)                        │
│         │                                                   │
│         ▼                                                   │
│  NGINX Ingress Controller Pod (Namespace: ingress-nginx)   │
│         │                                                   │
│         ▼  (Matches path '/' -> juice-shop-service:80)      │
│  Juice Shop Service (ClusterIP: Port 80)                    │
│         │                                                   │
│         ▼  (TargetPort mapping: 80 -> 3000)                  │
│  Juice Shop Application Pod (ContainerPort: 3000)           │
└─────────────────────────────────────────────────────────────┘
