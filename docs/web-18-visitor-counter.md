# WEB-18 — Persistent Visitor Counter

## Problem

The original homepage visitor counter stored its value in browser `localStorage`. This meant the displayed value could survive a page refresh on one browser, but every visitor effectively had an independent counter.

That did not meet the intended behaviour of a real portfolio visitor counter.

## Options considered

### Client-side storage

Simple and free, but not shared between visitors and therefore unsuitable for a genuine global count.

### Traditional hosted backend

Would provide shared state, but adds unnecessary infrastructure and operational overhead for a very small workload.

### Serverless AWS backend

API Gateway, Lambda and DynamoDB provide shared persistent state with very little operational overhead and are well suited to low-volume portfolio traffic.

## Decision

Use a serverless AWS architecture:

```text
Browser -> API Gateway -> Lambda -> DynamoDB
```

## Implementation

The frontend calls an API Gateway HTTP API endpoint. API Gateway invokes a Python Lambda function. The Lambda function performs an atomic DynamoDB update:

```python
UpdateExpression="ADD #count :increment"
```

The updated count is returned to the browser as JSON.

The Lambda execution role supplies DynamoDB permissions, so credentials are not embedded in the application source.

## Result

The portfolio now displays a persistent shared visitor count rather than a browser-specific value.

## Why this was the better fit

The final design is small, inexpensive, easy to operate and directly aligned with the serverless AWS skills the Cloud Resume Challenge is intended to demonstrate.

## Lessons learned

A feature can appear to work correctly while still using the wrong persistence model. The important design question was not simply "does the number survive a refresh?" but "where should shared application state live?"
