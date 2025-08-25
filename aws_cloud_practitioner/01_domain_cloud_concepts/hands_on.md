# Domain 1: Cloud Concepts - Hands-On Labs

These hands-on exercises are designed to familiarize you with the basic environment and layout of AWS. You will need an AWS account to perform them. Most of these actions fall within the AWS Free Tier.

### Lab 1: Navigating the AWS Management Console

**Objective:** Get comfortable with the primary web interface for AWS.

1.  **Sign In:** Go to the [AWS Management Console](https://aws.amazon.com/console/) and sign in with your AWS account credentials.
2.  **Explore the Console Home:**
    -   Observe the main dashboard. You may see recently visited services, AWS Health status, and cost and usage information.
    -   Use the search bar at the top to find a service by name, such as `S3` or `EC2`.
3.  **Service Navigation:**
    -   Click on the "Services" dropdown in the top-left corner. Browse through the different categories (e.g., Compute, Storage, Database) to get a sense of the breadth of AWS offerings.
4.  **Region Selection:**
    -   In the top-right corner, you will see a Region selector (e.g., "N. Virginia", "Ohio"). Click on it.
    -   Observe the list of available AWS Regions.
    -   Switch to a different Region (e.g., from `us-east-1` to `eu-west-1`). Notice that the console reloads. Some resources are Region-specific, so what you see in one Region may not be present in another.
5.  **Find Your Account ID:**
    -   In the top-right corner, click on your account name.
    -   In the dropdown menu, you will see your **Account ID**, a 12-digit number. This is a unique identifier for your AWS account.

---

### Lab 2: Exploring the AWS Global Infrastructure

**Objective:** Visualize and understand the physical scale of AWS.

1.  **Use the AWS Infrastructure Map:**
    -   Visit the official [AWS Global Infrastructure](https://infrastructure.aws/) page.
    -   Interact with the map to see the different Regions, the number of Availability Zones in each, and upcoming Regions.
2.  **Identify Availability Zones in the Console:**
    -   Navigate to the **VPC (Virtual Private Cloud)** service from the AWS Management Console.
    -   In the VPC dashboard, click on **"Subnets"** in the left-hand navigation pane.
    -   When you create a new subnet (you don't have to complete the process), you will see a dropdown list for **"Availability Zone"**. This list shows the available AZs within your currently selected Region (e.g., `us-east-1a`, `us-east-1b`, etc.). This demonstrates how you can choose to place resources in specific, isolated locations for high availability.

---

### Lab 3: Using the AWS Pricing Calculator

**Objective:** Learn how to estimate the cost of an AWS workload.

1.  **Navigate to the Calculator:** Go to the [AWS Pricing Calculator](https://calculator.aws/).
2.  **Create an Estimate:**
    -   Click **"Create estimate"**.
    -   You will be prompted to search for a service. Search for **"EC2"** and click **"Configure"**.
    -   Enter a simple description, like "My Web Server".
    -   Under **Instance type**, search for and select a Free Tier eligible instance like `t2.micro`.
    -   Choose a pricing model (e.g., On-Demand).
    -   Scroll down to the **Storage (EBS)** section. You can leave the default values.
    -   Click **"Add to my estimate"**.
3.  **Review the Estimate:**
    -   You will now see an estimated monthly cost for the EC2 instance. The calculator shows you the breakdown of costs (compute, storage, etc.).
    -   This exercise helps you understand how the pay-as-you-go model works and how to forecast costs for your projects.