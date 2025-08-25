# Domain 3: Cloud Technology and Services - Theory

This domain covers the wide range of services AWS offers, including compute, storage, networking, and databases, as well as the AWS global infrastructure.

## 1. AWS Global Infrastructure

-   **Regions:** Physical locations around the world composed of multiple Availability Zones.
-   **Availability Zones (AZs):** One or more discrete data centers with redundant power, networking, and connectivity. They are isolated from each other to provide fault tolerance.
-   **Edge Locations:** A network of data centers used by services like CloudFront to cache content closer to end-users, reducing latency.

## 2. Core Compute Services

-   **Amazon EC2 (Elastic Compute Cloud):**
    -   Provides secure, resizable compute capacity in the cloud (virtual servers).
    -   **Instance Types:** Optimized for different tasks (e.g., General Purpose, Compute Optimized, Memory Optimized).
    -   **Amazon Machine Image (AMI):** A template that contains the software configuration (OS, application server, and applications) required to launch your instance.

-   **AWS Lambda:**
    -   A **serverless** compute service that lets you run code without provisioning or managing servers.
    -   You pay only for the compute time you consume.
    -   Ideal for event-driven architectures (e.g., processing an image after it's uploaded to S3).

-   **Container Services:**
    -   **Amazon ECS (Elastic Container Service):** A highly scalable, high-performance container orchestration service that supports Docker containers.
    -   **Amazon EKS (Elastic Kubernetes Service):** A managed service that makes it easy to run Kubernetes on AWS.

## 3. Core Storage Services

-   **Amazon S3 (Simple Storage Service):**
    -   **Object storage** service offering industry-leading scalability, data availability, security, and performance.
    -   Stores data as objects within resources called "buckets".
    -   **Use Cases:** Website hosting, data archiving, application data, backup and restore.
    -   **Storage Classes:** Different tiers for different needs (e.g., S3 Standard for frequent access, S3 Glacier for long-term archive).

-   **Amazon EBS (Elastic Block Store):**
    -   **Block storage** service for use with Amazon EC2. It's like a virtual hard drive for your EC2 instance.
    -   It persists independently from the life of an EC2 instance.

-   **Amazon EFS (Elastic File System):**
    -   **File storage** service for use with Amazon EC2. It provides a simple, scalable, elastic file system that can be shared across multiple EC2 instances.

## 4. Core Networking Services

-   **Amazon VPC (Virtual Private Cloud):**
    -   Lets you provision a logically isolated section of the AWS Cloud where you can launch AWS resources in a virtual network that you define.
    -   **Subnets:** A range of IP addresses in your VPC.
    -   **Security Groups:** A virtual firewall for your EC2 instances to control inbound and outbound traffic (stateful).
    -   **Network ACLs (NACLs):** A firewall for controlling traffic in and out of one or more subnets (stateless).

-   **Amazon Route 53:**
    -   A highly available and scalable cloud Domain Name System (DNS) web service.

-   **Amazon CloudFront:**
    -   A fast **Content Delivery Network (CDN)** service that securely delivers data, videos, applications, and APIs to customers globally with low latency and high transfer speeds.

-   **Elastic Load Balancing (ELB):**
    -   Automatically distributes incoming application traffic across multiple targets, such as EC2 instances.

## 5. Core Database Services

-   **Amazon RDS (Relational Database Service):**
    -   A managed service that makes it easy to set up, operate, and scale a relational database in the cloud (e.g., MySQL, PostgreSQL, Oracle).
    -   AWS manages the work involved in patching, backups, and high availability.

-   **Amazon DynamoDB:**
    -   A fast and flexible **NoSQL** database service for all applications that need consistent, single-digit millisecond latency at any scale.
    -   It is a fully managed, serverless database.

-   **Amazon Redshift:**
    -   A fully managed, petabyte-scale **data warehouse** service in the cloud.