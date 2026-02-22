Key Features:

100% Serverless: Built using AWS Lambda for cost-efficient, scalable compute.

Automated Scheduling: Triggered hourly via Amazon EventBridge.

Data Persistence: Historical tracking using Amazon DynamoDB.

Real-time Alerts: Integrated with Amazon SNS for instant email notifications.

Infrastructure: Configured via AWS CLI with environment variable security.

LESSONS LEARNED:

Handling Timeouts: Encountered a Sandbox.Timedout error; resolved by optimizing Lambda configuration and increasing timeout from 3s to 15s.

IAM Least Privilege: Configured custom execution roles to ensure the Lambda only had specific access to DynamoDB and SNS (Security Best Practice).

Environment Security: Used Lambda Environment Variables to store SNS ARNs, keeping the codebase generic and secure.
