# Project Aegis: VAPT-Validated Blockchain SIEM 🛡️⛓️

## 🔬 Project Overview
**Project Aegis** is a comprehensive cybersecurity framework designed to bridge the gap between **Real-time Detection (SOC)** and **Data Integrity (Blockchain)**. By utilizing a deception-based honeypot, the system validates security postures through **VAPT (Vulnerability Assessment and Penetration Testing)** and ensures all resulting telemetry is stored in an immutable cryptographic ledger.

---

## 🏗️ System Architecture
The project follows a "Detect-Verify-Seal" pipeline:

1. **Reconnaissance & Attack (VAPT):** Simulating unauthorized access via Kali Linux.
2. **Threat Detection (SOC):** Wazuh Manager identifies the breach via custom XML rules.
3. **Cryptographic Sealing (Blockchain):** A Python engine hashes the alert into a SHA-256 linked-list.



---

## 📸 Execution Screenshots

### 1. The Breach (VAPT Phase)
*Description: Kali Linux successfully connecting to the Honeypot listener.*
> ![VAPT Attack](Screenshot%202026-04-06%20210156.png)

### 2. The Detection (SOC Phase)
*Description: Wazuh Dashboard triggering a Level 12 "Critical" alert.*
> ![Wazuh Alert](Screenshot%202026-04-06%20213700.png)

### 3. The Ledger (Integrity Phase)
*Description: The `ledger.json` file showing the hashed chain of events.*
> ![Blockchain Ledger](Screenshot%202026-04-06%20234339.png)

---

## 🛠️ Technical Stack
| Component | Technology | Role |
| :--- | :--- | :--- |
| **SIEM** | Wazuh (OSSEC) | Log Analysis & Alerting |
| **Attacker** | Kali Linux | VAPT Validation |
| **Integrity** | Python 3 (Hashlib) | SHA-256 Blockchain Logic |
| **Database** | JSON | Distributed Ledger Simulation |

---

## 🔐 Security Impact: The "Why"
Traditional logs are vulnerable to **Log Wiping** (where an attacker deletes `/var/log` entries). **Project Aegis** mitigates this by:
* **Non-Repudiation:** Every log is signed with a unique hash.
* **Tamper Detection:** If any historical block is edited, the hash chain breaks instantly.
* **Chain of Custody:** Provides a mathematically verifiable audit trail for digital forensics.
