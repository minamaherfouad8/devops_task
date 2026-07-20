# Task 1: User Data Validation & Parity Checking Script

A Python utility script that reads a user dataset from a CSV/text file, validates user email addresses and numerical IDs, determines whether each ID is odd or even, and filters out invalid or missing data with stderr warnings.

---

## 📌 Features

* **FQDN Email Validation**: Ensures email addresses follow standard fully qualified domain name (FQDN) rules (rejecting invalid formats and local domains like `localhost`).
* **ID Parity Calculation**: Identifies whether valid user IDs are `even` or `odd`.
* **Robust Error Handling**:
  * Emits warnings to `stderr` for missing parameters, malformed IDs, or non-routable emails.
  * Continues processing remaining lines without breaking execution.
  * Skips headers and blank lines automatically.

---
