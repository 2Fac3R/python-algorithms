# Domain 2: Security and Compliance - Cheatsheet

### AWS Shared Responsibility Model

-   **AWS Responsibility (Security OF the Cloud):**
    -   Physical security of data centers.
    -   Hardware, software, networking, and facilities that run AWS services.
    -   Managed services (e.g., patching OS on RDS, DynamoDB platform).

-   **Customer Responsibility (Security IN the Cloud):**
    -   **Data:** Securing your data, managing encryption.
    -   **Platform, Applications, Identity & Access Management:** Managing user permissions, OS, network, and firewall configuration.
    -   **Configuration:** Configuring Security Groups, Network ACLs, IAM policies.

---

### AWS Identity and Access Management (IAM)

-   **IAM is Global:** Not tied to a specific Region.
-   **Principle of Least Privilege:** Grant only the permissions required to perform a task.

-   **IAM Components:**
    -   **Users:** Long-term credentials for a person or application.
    -   **Groups:** A collection of users. Apply policies to groups for easier management.
    -   **Roles:** Temporary credentials. Assumed by users or services. **Most secure way to grant permissions.**
    -   **Policies:** JSON documents that define permissions (Allow/Deny).
-   **MFA (Multi-Factor Authentication):** Recommended for all accounts, **especially the root user**.

---

### Key Security Services

| Service           | Purpose                                                                 | Use Case                                            |
| :---------------- | :---------------------------------------------------------------------- | :-------------------------------------------------- |
| **AWS Shield**      | Managed DDoS protection service.                                        | Protects against infrastructure-layer DDoS attacks. |
| **AWS WAF**         | Web Application Firewall.                                               | Filters malicious web traffic (SQL injection, XSS). |
| **Amazon GuardDuty**| Intelligent threat detection service.                                   | Detects unusual API activity or compromised instances. |
| **Amazon Inspector**| Automated security assessment service.                                | Scans EC2 instances for vulnerabilities.            |
| **AWS KMS**         | Managed service for creating and controlling encryption keys.           | Encrypting S3 objects, EBS volumes.                 |
| **AWS Artifact**    | On-demand access to AWS compliance reports.                             | Provide compliance reports to auditors (PCI, SOC).  |
| **AWS Organizations**| Central governance and management for multiple AWS accounts.            | Apply security policies (SCPs) across all accounts. |