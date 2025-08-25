# Domain 2: Security and Compliance - Key Services

This domain focuses on services that help you secure your AWS environment and maintain compliance.

-   **AWS Identity and Access Management (IAM):**
    -   **Description:** The heart of AWS security. Securely manage access to AWS services and resources. It is a global service (not Region-specific).
    -   **Components:**
        -   **Users:** An entity representing a person or application.
        -   **Groups:** A collection of users; a way to manage permissions for multiple users at once.
        -   **Roles:** An identity with temporary permissions, assumable by users, applications, or services. The most secure way to grant access.
        -   **Policies:** JSON documents that define permissions.

-   **AWS Organizations:**
    -   **Description:** An account management service that enables you to consolidate multiple AWS accounts into an organization that you create and centrally manage.
    -   **Use Case:** Applying policies (Service Control Policies - SCPs) to a group of accounts, simplifying billing for multiple accounts.

-   **AWS Shield:**
    -   **Description:** A managed Distributed Denial of Service (DDoS) protection service.
    -   **Tiers:** **Standard** (free, automatic protection) and **Advanced** (paid, enhanced protection for specific resources).

-   **AWS WAF (Web Application Firewall):**
    -   **Description:** Protects web applications from common web exploits (e.g., SQL injection, cross-site scripting). Operates at Layer 7 (the application layer).
    -   **Use Case:** Filtering malicious traffic before it reaches your web servers (e.g., on CloudFront or Application Load Balancer).

-   **Amazon Inspector:**
    -   **Description:** An automated vulnerability management service that continually scans your AWS workloads for software vulnerabilities and unintended network exposure.
    -   **Use Case:** Finding security vulnerabilities in your EC2 instances and container images.

-   **Amazon GuardDuty:**
    -   **Description:** A threat detection service that uses machine learning to continuously monitor for malicious or unauthorized behavior.
    -   **Use Case:** Detecting compromised EC2 instances, unusual API calls, or potential data theft.

-   **AWS Key Management Service (KMS):**
    -   **Description:** A managed service that makes it easy to create and control the encryption keys used to encrypt your data.
    -   **Use Case:** Managing the keys used for S3 server-side encryption or EBS volume encryption.

-   **AWS Artifact:**
    -   **Description:** A no-cost, self-service portal for on-demand access to AWS's compliance reports.
    -   **Use Case:** Providing auditors with proof of AWS's compliance with standards like PCI DSS, HIPAA, and SOC.