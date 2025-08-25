# Domain 4: Billing, Pricing, and Support - Key Services

This domain focuses on the tools and concepts related to managing costs and getting help from AWS.

### Core Concepts

-   **Pricing Models:**
    -   **On-Demand:** Pay by the hour/second. No commitment. Flexible but most expensive.
    -   **Reserved Instances (RIs):** 1- or 3-year commitment for a specific instance type. Significant discount.
    -   **Savings Plans:** 1- or 3-year commitment for a certain amount of compute usage ($/hour). More flexible than RIs.
    -   **Spot Instances:** Bid on spare capacity. Can be interrupted. Biggest discount (up to 90%).

-   **AWS Free Tier:**
    -   Provides a limited amount of free usage on many services to help you get started.

### Cost Management Tools

-   **AWS Pricing Calculator:**
    -   **Description:** A web-based tool to estimate the cost of your AWS architecture before you build it.
    -   **Use Case:** Creating a cost estimate for a new project to get budget approval.

-   **AWS Budgets:**
    -   **Description:** A tool for setting custom cost and usage budgets.
    -   **Use Case:** Creating an alert that notifies you via email when your monthly spending is forecasted to exceed $100.

-   **AWS Cost Explorer:**
    -   **Description:** A tool for visualizing, understanding, and managing your AWS costs and usage over time.
    -   **Use Case:** Analyzing your spending for the last three months to identify which service is costing the most.

-   **Cost Allocation Tags:**
    -   **Description:** Key-value pairs that you can attach to AWS resources.
    -   **Use Case:** Tagging all resources for a specific project (e.g., `Project:Blue`) to track the total cost of that project.

### Support

-   **AWS Support Plans:**
    -   **Basic:** Free. Access to documentation and forums.
    -   **Developer:** For testing/dev. Business-hours email support.
    -   **Business:** For production workloads. 24x7 phone/email/chat support.
    -   **Enterprise:** For mission-critical workloads. Includes a designated Technical Account Manager (TAM).