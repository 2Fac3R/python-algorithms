# Domain 2: Security and Compliance - Theory

This domain is one of the most critical, as it covers how AWS handles security and how you, as a customer, are responsible for securing your own applications and data.

## 1. The AWS Shared Responsibility Model

This is a fundamental concept in AWS security. It defines the security responsibilities between AWS and the customer.

-   **AWS is responsible for Security OF the Cloud:** AWS manages and protects the physical infrastructure that runs all of the AWS services. This includes the hardware, software, networking, and facilities that run AWS Cloud services.
    -   *Analogy:* AWS is like the landlord of an apartment building. They are responsible for the building's security, the main doors, and the physical structure.

-   **The Customer is responsible for Security IN the Cloud:** The customer is responsible for managing and securing their data, applications, operating systems, and network configurations. The level of responsibility depends on the service being used.
    -   *Analogy:* You, as the tenant, are responsible for locking your apartment door, securing your belongings inside, and managing who has a key.

### Responsibility by Service Type:

-   **Infrastructure as a Service (IaaS)** (e.g., EC2): The customer has the most responsibility, including managing the guest operating system, applications, and security configurations.
-   **Platform as a Service (PaaS)** (e.g., RDS, Elastic Beanstalk): AWS manages the underlying platform and operating system, but the customer is still responsible for securing their data and application access.
-   **Software as a Service (SaaS)** (e.g., AWS Trusted Advisor, AWS Shield): AWS manages the entire stack, and the customer is only responsible for managing their data and user access.

## 2. AWS Identity and Access Management (IAM)

IAM is the service that allows you to securely manage access to AWS services and resources. It is a global service.

-   **Users:** An entity that you create in AWS to represent the person or application that uses it to interact with AWS. Users have long-term credentials (password for console access, access keys for programmatic access).
-   **Groups:** A collection of IAM users. You can apply permissions to a group, and all users in that group inherit those permissions. This is the preferred way to manage user permissions.
-   **Roles:** An identity that you can assume to gain temporary access to permissions. Roles do not have standard long-term credentials. They are meant to be assumed by users, applications, or services that need them. This is the most secure way to grant permissions.
-   **Policies:** JSON documents that define permissions. You attach policies to users, groups, or roles to grant them access to AWS resources. AWS follows the **Principle of Least Privilege**, meaning you should only grant the minimum permissions necessary to perform a task.
-   **Multi-Factor Authentication (MFA):** Provides an extra layer of security for your AWS account. It is highly recommended to enable MFA on your root user account.

## 3. AWS Security Services

-   **AWS Shield:** A managed Distributed Denial of Service (DDoS) protection service. **Shield Standard** is enabled automatically for all AWS customers at no additional cost. **Shield Advanced** provides enhanced protections for an additional fee.
-   **AWS WAF (Web Application Firewall):** Helps protect your web applications from common web exploits (like SQL injection and cross-site scripting) that could affect application availability, compromise security, or consume excessive resources.
-   **Amazon Inspector:** An automated security assessment service that helps improve the security and compliance of applications deployed on AWS. It automatically assesses applications for vulnerabilities or deviations from best practices.
-   **Amazon GuardDuty:** A threat detection service that continuously monitors for malicious activity and unauthorized behavior to protect your AWS accounts and workloads.
-   **AWS Key Management Service (KMS):** Makes it easy for you to create and manage cryptographic keys and control their use across a wide range of AWS services and in your applications.

## 4. AWS Compliance

-   **AWS Artifact:** Your go-to, central resource for compliance-related information. It provides on-demand access to AWS’s security and compliance reports and select online agreements. You can use these reports to demonstrate the security and compliance of the AWS infrastructure to your auditors.
-   **Compliance Programs:** AWS complies with many international standards and regulations, such as **PCI DSS** (for credit card processing), **HIPAA** (for healthcare data), **SOC 1/2/3**, and **ISO 27001**.