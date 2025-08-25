# Domain 4: Billing, Pricing, and Support - Hands-On Labs

These labs will help you get familiar with AWS's cost management tools.

### Lab 1: Create a Billing Alert with AWS Budgets

**Objective:** Learn how to proactively monitor your AWS spending.

1.  **Navigate to Billing Dashboard:** From the AWS Management Console, click on your account name in the top-right and select **"Billing & Cost Management"**.
2.  **Go to Budgets:** In the left navigation pane, click on **"Budgets"**.
3.  **Create a Budget:**
    -   Click **"Create budget"**.
    -   Select **"Cost budget - Recommended"** and click **Next**.
    -   **Budget details:**
        -   Give your budget a name, e.g., `My-Monthly-Budget`.
        -   Set the **Period** to `Monthly`.
        -   Set the **Budgeted amount** to a small value, for example, `5` (USD).
    -   Click **Next**.
4.  **Configure Alerts:**
    -   Click **"Add an alert threshold"**.
    -   Set the **Threshold** to `80`% of your budgeted amount.
    -   Under **Notification preferences**, enter your email address to receive the alert.
    -   Click **Next**.
5.  **Review and Create:**
    -   Review the budget configuration and click **"Create budget"**.
    -   You will now be notified if your costs are forecasted to exceed 80% of $5 for the month.

---

### Lab 2: Explore Costs with AWS Cost Explorer

**Objective:** Learn how to analyze your spending patterns.

1.  **Navigate to Cost Explorer:** From the Billing & Cost Management dashboard, click on **"Cost Explorer"** in the left navigation pane.
    -   *Note: If this is your first time, you may need to enable Cost Explorer and wait up to 24 hours for data to be populated.*
2.  **Analyze Costs:**
    -   The main graph shows your costs for the last several months.
    -   On the right-hand side, under **"Filters"**, you can group your costs by different dimensions.
    -   Select **"Service"** from the **"Group by"** dropdown.
    -   The graph and table will now update to show you a breakdown of your spending by each AWS service, helping you identify which services are contributing most to your bill.
    -   Experiment with other filters, such as **"Region"** or **"Usage Type"**.