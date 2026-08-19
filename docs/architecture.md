# Architecture

## Production architecture

The portfolio is delivered as a static website with a small serverless backend for the visitor counter.

```text
Visitor
  |
  v
Route 53
  |
  v
CloudFront  <---- ACM certificate
  |
  v
S3 static website assets

Browser JavaScript
  |
  v
API Gateway HTTP API
  |
  v
Python Lambda
  |
  v
DynamoDB

Contact page
  |
  v
Formspree
```

## Frontend delivery

### Amazon S3

S3 stores the static site assets: HTML, CSS, JavaScript and images.

### Amazon CloudFront

CloudFront is the public delivery layer. It provides the HTTPS-facing distribution for the website and redirects HTTP requests to HTTPS.

### AWS Certificate Manager

The ACM certificate is deployed in `us-east-1`, as required for CloudFront certificates, and covers both:

- `ron-jackson.co.uk`
- `www.ron-jackson.co.uk`

### Amazon Route 53

Route 53 directs the custom domain to the CloudFront distribution. The apex domain uses an Alias record to the distribution.

## Visitor counter backend

The original counter was browser-local and therefore did not represent real site-wide traffic. It was replaced with a persistent serverless backend.

### API Gateway

An HTTP API exposes the visitor-count endpoint to the website frontend.

### AWS Lambda

A Python Lambda function handles the visitor counter logic and communicates with DynamoDB.

### DynamoDB

DynamoDB stores the persistent count. On-demand capacity was chosen because the site has low and unpredictable traffic and does not need provisioned throughput.

## Contact form

The contact form is hosted on a dedicated `contact.html` page and submitted through Formspree. Moving it to its own page reduced clutter elsewhere in the site and made the contact path easier to find from navigation.

## Design priorities

The architecture favours:

- Low ongoing cost.
- Managed/serverless AWS services.
- Minimal operational overhead.
- Clear separation between the static frontend and the small dynamic backend.
- A structure that can be expanded later without over-engineering the initial portfolio.
