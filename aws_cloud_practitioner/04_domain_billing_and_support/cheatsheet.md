# Domain 4: Billing, Pricing, and Support - Cheatsheet

### AWS Pricing Models

| Model                 | Best For                                               | Commitment      | Discount                            |
| :-------------------- | :----------------------------------------------------- | :-------------- | :---------------------------------- |
| **On-Demand**           | Short-term, spiky, or unpredictable workloads.         | None            | None (Highest cost)                 |
| **Reserved Instances**  | Steady-state, predictable usage.                       | 1 or 3 years    | Significant (up to 72%)             |
| **Savings Plans**       | Predictable usage, but need flexibility in instance type/region. | 1 or 3 years    | Good (less than RIs, more than On-Demand) |
| **Spot Instances**      | Fault-tolerant, interruptible workloads (e.g., batch jobs). | None            | Highest (up to 90%)                 |

---

### AWS Cost Management Tools

-   **AWS Pricing Calculator:**
    -   **Purpose:** Estimate the cost of your solution *before* you build it.
    -   **Use:** For planning and budgeting new projects.

-   **AWS Cost Explorer:**
    -   **Purpose:** Visualize and analyze your historical and current costs.
    -   **Use:** To understand spending patterns and identify cost drivers. Has forecasting capabilities.

-   **AWS Budgets:**
    -   **Purpose:** Set custom cost and usage budgets and receive alerts.
    -   **Use:** To be notified when you exceed or are about to exceed your budget.

-   **Cost Allocation Tags:**
    -   **Purpose:** Label resources to organize and track costs.
    -   **Use:** To categorize spending by project, department, or environment (e.g., `Project:Phoenix`).

---

### AWS Support Plans

| Feature               | Basic        | Developer    | Business                  | Enterprise                |
| :-------------------- | :----------- | :----------- | :------------------------ | :------------------------ |
| **Cost**                | Free         | Monthly fee  | Monthly fee (higher)      | Monthly fee (highest)     |
| **Technical Support**   | None         | Business hours email | 24x7 email, chat, phone   | 24x7 email, chat, phone   |
| **Response Time**       | N/A          | < 24 hours   | < 4 hours (prod down)     | < 15 mins (business-crit) |
| **TAM**                 | No           | No           | No                        | **Yes** (Technical Account Manager) |
| **Trusted Advisor**     | Core Checks  | Core Checks  | Full Checks               | Full Checks               |