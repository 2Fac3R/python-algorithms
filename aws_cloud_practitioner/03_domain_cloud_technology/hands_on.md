# Domain 3: Cloud Technology - Hands-On Labs

These labs will give you practical experience with the most fundamental AWS services.

### Lab 1: Launch and Connect to an Amazon EC2 Instance

**Objective:** Understand the basics of launching a virtual server in AWS.

1.  **Navigate to EC2:** From the AWS Management Console, search for and go to the **EC2** service.
2.  **Launch Instance:**
    -   Click the **"Launch instance"** button.
    -   Give your instance a name, e.g., `My-Web-Server`.
    -   Under **Application and OS Images (AMI)**, select **Amazon Linux** (ensure the "Free tier eligible" label is visible).
    -   Under **Instance type**, select `t2.micro` (also marked as "Free tier eligible").
    -   Under **Key pair (login)**, proceed without a key pair for this simple lab, or create one if you wish to connect via SSH later.
3.  **Configure Network Settings:**
    -   Under **Network settings**, click **"Edit"**.
    -   For **Security group**, select **"Create security group"**.
    -   Add a rule to allow HTTP traffic: Click **"Add security group rule"**, select `HTTP` from the dropdown, and leave the source as `Anywhere` (0.0.0.0/0).
4.  **Launch:**
    -   Review the summary and click **"Launch instance"**.
5.  **Terminate the Instance:**
    -   After the instance state changes to "Running", select the instance from the list.
    -   Click **"Instance state"** and then **"Terminate instance"**. This is a crucial step to avoid incurring unexpected charges.

---

### Lab 2: Create an S3 Bucket and Upload an Object

**Objective:** Learn how to use AWS's object storage service.

1.  **Navigate to S3:** From the console, go to the **S3** service.
2.  **Create a Bucket:**
    -   Click **"Create bucket"**.
    -   Enter a **globally unique** bucket name (e.g., `my-unique-test-bucket-` followed by random numbers).
    -   Leave the Region and other settings as default.
    -   Click **"Create bucket"** at the bottom.
3.  **Upload an Object:**
    -   Click on the name of the bucket you just created.
    -   Click the **"Upload"** button.
    -   Click **"Add files"** and choose a small text or image file from your local computer.
    -   Click **"Upload"** at the bottom.
4.  **Clean Up:**
    -   Once the upload is complete, select the file you uploaded and click **"Delete"**.
    -   Go back to the S3 buckets list, select the bucket you created, and click **"Delete"**. You will need to type the bucket name to confirm the deletion.