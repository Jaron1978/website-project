# Decision Log

A concise record of significant project decisions. This is intentionally selective rather than a transcript of every edit.

| Decision | Choice | Main reason |
|---|---|---|
| Static hosting | Amazon S3 | Simple, low-cost hosting for a static portfolio |
| Public delivery | Amazon CloudFront | HTTPS delivery, caching and custom-domain integration |
| TLS | AWS Certificate Manager | Native CloudFront certificate management |
| DNS | Amazon Route 53 | AWS-native routing to CloudFront |
| Visitor persistence | Amazon DynamoDB | Serverless persistence with very low operational overhead |
| Visitor backend | Python on AWS Lambda | Event-driven compute with no always-on server |
| Visitor API | API Gateway HTTP API | Small managed HTTP interface for the frontend |
| DynamoDB capacity | On-demand | Appropriate for low/unpredictable portfolio traffic |
| Contact handling | Formspree | Reliable form processing without unnecessary custom backend work |
| Project presentation | Portfolio index + dedicated pages | Better scanability and less page clutter |
| Delivery history | WEB-ID Kanban board | Makes completed work and project evolution visible |
| Credential presentation | Verified earned badges separated from planned items | Avoids overstating qualifications |

## Decision principles

When choosing between solutions, the project generally favours:

1. The simplest solution that genuinely solves the problem.
2. Low fixed cost for a personal portfolio.
3. Managed/serverless services where they reduce unnecessary operations work.
4. Learning value when two solutions are otherwise similarly appropriate.
5. Clear evidence and verification rather than claims that cannot be demonstrated.
