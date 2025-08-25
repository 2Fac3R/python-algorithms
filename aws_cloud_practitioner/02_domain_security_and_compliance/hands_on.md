# Domain 2: Security and Compliance - Hands-On Labs

These labs focus on core security practices in AWS using IAM.

### Lab 1: Create a New IAM User with Limited Permissions

**Objective:** Understand the principle of least privilege by creating a user that can only perform specific actions.

1.  **Navigate to IAM:** In the AWS Management Console, search for and navigate to the **IAM** service.
2.  **Create a User Group:**
    -   In the left navigation pane, click **User groups**.
    -   Click **Create group**.
    -   Give the group a name, like `S3-Read-Only-Group`.
    -   In the "Permissions policies" section, search for the policy named `AmazonS3ReadOnlyAccess`. Select the checkbox next to it.
    -   Click **Create group**.
3.  **Create a User:**
    -   In the left navigation pane, click **Users**.
    -   Click **Add users**.
    -   Enter a **User name**, for example, `test-user`.
    -   Select **Provide user access to the AWS Management Console**.
    -   Choose **I want to create an IAM user**.
    -   Set a custom password and uncheck "User must create a new password at next sign-in".
    -   Click **Next**.
4.  **Set Permissions:**
    -   Select **Add user to group**.
    -   Check the box next to the `S3-Read-Only-Group` you created earlier.
    -   Click **Next**.
5.  **Review and Create:**
    -   Review the user details and permissions, then click **Create user**.
    -   **Important:** Download the `.csv` file containing the user's credentials. This is your only chance to retrieve the password.
6.  **Test the User:**
    -   Sign out of your current session.
    -   Sign back in using the credentials for the new `test-user`.
    -   Try to navigate to the **S3** service. You should be able to view buckets.
    -   Try to navigate to the **EC2** service. You should see access denied errors, demonstrating the principle of least privilege.

---

### Lab 2: Enable Multi-Factor Authentication (MFA) for Your Root User

**Objective:** Secure your most privileged account, the root user.

1.  **Sign In as Root:** Sign in to the AWS Management Console using your root user email and password.
2.  **Navigate to Security Credentials:**
    -   Click on your account name in the top-right corner and select **Security credentials**.
3.  **Assign MFA:**
    -   Find the **Multi-factor authentication (MFA)** section and click **Assign MFA**.
    -   Follow the on-screen instructions to set up a virtual MFA device using an authenticator app on your smartphone (like Google Authenticator or Authy).
    -   You will need to scan a QR code and enter two consecutive MFA codes to sync the device.
4.  **Verify:** Once complete, sign out and sign back in. You will now be prompted for your password and an MFA code from your virtual device.