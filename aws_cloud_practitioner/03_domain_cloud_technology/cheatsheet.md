# Domain 3: Cloud Technology - Cheatsheet

### Core Service Categories

| Category      | Description                               | Key Services                                  |
| :------------ | :---------------------------------------- | :-------------------------------------------- |
| **Compute**     | Provides virtual servers and serverless compute. | EC2, Lambda, ECS, EKS, Beanstalk              |
| **Storage**     | Stores data in different formats.         | S3, EBS, EFS, S3 Glacier                      |
| **Networking**  | Isolates and connects cloud resources.    | VPC, Route 53, CloudFront, ELB, Direct Connect |
| **Database**    | Offers managed relational and NoSQL databases. | RDS, DynamoDB, Redshift, ElastiCache          |
| **Management**  | Monitors and governs AWS resources.       | CloudWatch, CloudTrail, Trusted Advisor, Config |

---

### Storage Comparison

| Service       | Type            | Use Case                                      |
| :------------ | :-------------- | :-------------------------------------------- |
| **Amazon S3**   | **Object** Storage | Storing files, backups, static website hosting. |
| **Amazon EBS**  | **Block** Storage  | A virtual hard drive for a single EC2 instance. |
| **Amazon EFS**  | **File** Storage   | A shared network file system for multiple EC2s. |

---

### Networking Firewall Comparison

| Feature         | Security Group                               | Network ACL (NACL)                           |
| :-------------- | :------------------------------------------- | :------------------------------------------- |
| **Level**       | Instance level                               | Subnet level                                 |
| **State**       | **Stateful:** Return traffic is automatically allowed. | **Stateless:** Return traffic must be explicitly allowed. |
| **Rules**       | Allows **Allow** rules only.                 | Allows both **Allow** and **Deny** rules.    |
| **Default**     | Denies all inbound, allows all outbound.     | Allows all inbound and outbound traffic.     |

---

### Key Service Definitions

-   **EC2 (Elastic Compute Cloud):** A virtual server (instance) in the cloud.
-   **Lambda:** A serverless compute service that runs code in response to events.
-   **S3 (Simple Storage Service):** A highly scalable object storage service.
-   **VPC (Virtual Private Cloud):** A logically isolated section of the AWS Cloud.
-   **Route 53:** A scalable Domain Name System (DNS) web service.
-   **CloudFront:** A global Content Delivery Network (CDN).
-   **RDS (Relational Database Service):** A managed service for relational databases.
-   **DynamoDB:** A managed, serverless NoSQL database.
-   **CloudWatch:** A monitoring service for AWS resources and applications.
-   **CloudTrail:** A service that logs all API calls within your AWS account.