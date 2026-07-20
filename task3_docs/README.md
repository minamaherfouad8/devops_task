# Task 3: Custom Newman Docker Image with System Utilities & Custom CSV Reporter

A custom Alpine-based Docker container image extending `postman/newman:5.3-alpine`. It incorporates updated system packages, network diagnostic tools (`curl`, `zip`, `ping`), explicitly configured DNS servers, and the `newman-reporter-csvallinone` global NPM module.

---

## 📌 Features & Image Specifications

* **Base Image**: `postman/newman:5.3-alpine`
* **Package Updates**: System packages updated and upgraded to the latest security versions using Alpine's `apk` package manager.
* **System Utilities Installed**:
  * `curl`: For HTTP request testing and endpoint verification.
  * `zip`: For archiving test reports and artifacts.
  * `iputils`: Provides standard `ping` network diagnostics.
* **Custom NPM Reporter**: Installed `newman-reporter-csvallinone` globally for aggregated CSV report generation.
* **DNS Resolution**: Configured custom public DNS resolvers (`8.8.8.8` and `1.1.1.1`).
* **Cache Management**: Cleaned package indexes (`--no-cache`) and NPM cache (`npm cache clean --force`) to ensure a minimal final image footprint.
* **Environment Variable**: `NODE_PATH` set to `/usr/local/lib/node_modules`.
* **Working Directory**: Default set to `/etc/newman`.
* **Entrypoint**: `newman`.

---
