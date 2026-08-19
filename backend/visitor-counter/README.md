# Visitor Counter Backend

This Lambda function implements the persistent visitor counter used by the live portfolio website.

## Architecture

```text
Portfolio Website
       |
       | HTTPS request
       v
API Gateway HTTP API
       |
       v
AWS Lambda (Python)
       |
       | Atomic ADD
       v
Amazon DynamoDB
website-visitor-counter
       |
       v
   {"count": 123}
       |
       v
Portfolio Website
```

## Why this backend exists

The original counter used browser `localStorage`. That made the value persist only within an individual browser, so it was not a true global visitor counter.

WEB-18 replaced that client-side approach with a small serverless AWS backend so all visitors share the same persistent count.

## Implementation details

- **AWS Lambda** runs the Python handler.
- **Amazon DynamoDB** stores the shared counter value.
- **API Gateway HTTP API** exposes the Lambda function to the website.
- **IAM execution roles** provide AWS permissions at runtime; no AWS credentials are embedded in the code.
- **CORS** is restricted to `https://www.ron-jackson.co.uk`.
- DynamoDB uses an atomic `ADD` update, avoiding a separate read-then-write sequence.
- Errors return a generic client message while the detailed exception is written to Lambda logs.

## DynamoDB record

The function expects a table named:

```text
website-visitor-counter
```

with a record keyed by:

```json
{
  "id": "visitor-count"
}
```

The `count` attribute is incremented automatically by the Lambda function.

## Security notes

No AWS access keys, secret keys, API keys, or passwords are stored in this source file. AWS SDK credentials are supplied automatically to `boto3` through the Lambda execution role.

The DynamoDB table name and allowed website origin are configuration values, not secrets.

## Possible future improvement

A future refinement would move the DynamoDB table name and allowed origin into Lambda environment variables. The current implementation is intentionally retained here because it reflects the deployed WEB-18 solution accurately.
