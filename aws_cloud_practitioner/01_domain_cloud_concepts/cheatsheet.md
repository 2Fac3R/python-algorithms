# Domain 1: Cloud Concepts - Cheatsheet

### The 6 Advantages of Cloud Computing

1.  **Trade CapEx for OpEx:** No upfront investment; pay for what you use.
2.  **Massive Economies of Scale:** Lower prices due to AWS's scale.
3.  **Stop Guessing Capacity:** Scale up or down as needed.
4.  **Increase Speed & Agility:** Deploy resources in minutes, not weeks.
5.  **Stop Maintaining Data Centers:** Focus on your business, not infrastructure.
6.  **Go Global in Minutes:** Deploy applications worldwide easily.

---

### AWS Global Infrastructure

-   **Region:** A physical, geographic area in the world.
    -   *Examples:* `us-east-1` (N. Virginia), `eu-west-1` (Ireland).
    -   Completely isolated from other Regions.
    -   Choose Regions based on latency, cost, service availability, and data residency.

-   **Availability Zone (AZ):**
    -   One or more discrete data centers within a Region.
    -   Physically separate and connected with low-latency networking.
    -   Designed for high availability and fault tolerance (e.g., run services across multiple AZs).

-   **Edge Location (Point of Presence - PoP):**
    -   A site where AWS caches content.
    -   More numerous than Regions.
    -   Used by **Amazon CloudFront** (CDN) to deliver content to users with low latency.

---

### AWS Well-Architected Framework (6 Pillars)

A framework for designing and operating reliable, secure, efficient, cost-effective, and sustainable systems in the cloud.

1.  **Operational Excellence:** Run and monitor systems to deliver business value.
    -   *Keywords:* Automation, performing operations as code, learning from failures.

2.  **Security:** Protect information, systems, and assets.
    -   *Keywords:* IAM, traceability, apply security at all layers, automation.

3.  **Reliability:** Recover from disruptions and meet demand.
    -   *Keywords:* High availability, fault tolerance, automatic recovery, testing.

4.  **Performance Efficiency:** Use resources efficiently.
    -   *Keywords:* Serverless, experiment more often, mechanical sympathy.

5.  **Cost Optimization:** Deliver business value at the lowest price.
    -   *Keywords:* Consumption model, measure efficiency, analyze spend.

6.  **Sustainability:** Minimize the environmental impacts of running cloud workloads.
    -   *Keywords:* Understand impact, maximize utilization, use managed services.