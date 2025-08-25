# Domain 4: Billing, Pricing, and Support - Theory

This domain covers how AWS pricing works, how to manage costs, and the different support options available to customers.

## 1. AWS Pricing Models

AWS offers several pricing models to fit different use cases.

-   **On-Demand:**
    -   Pay for compute or database capacity by the hour or the second with no long-term commitments.
    -   **Best for:** Applications with short-term, spiky, or unpredictable workloads that cannot be interrupted.

-   **Reserved Instances (RIs):**
    -   Provide a significant discount (up to 72%) compared to On-Demand pricing in exchange for a commitment to a 1- or 3-year term.
    -   **Best for:** Applications with steady-state or predictable usage.

-   **Savings Plans:**
    -   A flexible pricing model that offers lower prices on EC2 and Fargate usage, in exchange for a commitment to a consistent amount of usage (measured in $/hour) for a 1- or 3-year term.
    -   More flexible than RIs as they apply across instance families and Regions.

-   **Spot Instances:**
    -   Request spare EC2 computing capacity for up to 90% off the On-Demand price.
    -   **Best for:** Applications that have flexible start and end times, or that are fault-tolerant to interruptions, as AWS can reclaim Spot Instances with a 2-minute warning.

## 2. AWS Free Tier

AWS provides a Free Tier to allow customers to gain hands-on experience with the platform. There are three types of free offers:

1.  **Always Free:** Offers that do not expire and are available to all AWS customers.
2.  **12 Months Free:** Offers that are free for 12 months following your initial AWS sign-up date.
3.  **Trials:** Short-term free trials for specific services.

## 3. AWS Cost Management Tools

-   **AWS Budgets:**
    -   Allows you to set custom budgets that alert you when your costs or usage exceed (or are forecasted to exceed) your budgeted amount.

-   **AWS Cost Explorer:**
    -   An easy-to-use interface that lets you visualize, understand, and manage your AWS costs and usage over time.

-   **AWS Cost and Usage Report (CUR):**
    -   The most comprehensive set of cost and usage data available. The CUR lists AWS usage for each service category used by an account and its IAM users in hourly or daily line items.

-   **Cost Allocation Tags:**
    -   Tags are labels that you can assign to AWS resources. By tagging resources with identifiers like `cost-center`, `project`, or `owner`, you can track and manage your costs on a detailed level.

## 4. AWS Support Plans

AWS offers a range of support plans to help you troubleshoot issues, lower costs, and improve performance.

-   **Basic Support:** Included for all AWS customers at no charge. Includes access to documentation, whitepapers, and support forums.
-   **Developer Support:** Recommended for testing or early development. Provides business-hours email access to Cloud Support Associates.
-   **Business Support:** Recommended for production workloads. Provides 24x7 phone, email, and chat access to Cloud Support Engineers, and a <1 hour response time for production system down cases.
-   **Enterprise Support:** Recommended for business-critical workloads. Provides all Business Support features plus a designated Technical Account Manager (TAM), proactive guidance, and a <15 minute response time for business-critical system down cases.