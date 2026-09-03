# Engineering Challenges

This document records selected Website Phase 1 challenges using a consistent format: **problem → options → decision → implementation → result → lesson**.

## WEB-18 — Replace the browser-only visitor counter

### Problem

The first visitor counter used browser storage. It could increment a number for an individual browser, but it was not a genuine site-wide visitor count and could not persist a shared value across users and devices.

### Options considered

- Keep the browser-local implementation as a visual-only feature.
- Use a third-party counter service.
- Build a small AWS serverless backend.

### Decision

Build the counter using **API Gateway + Python Lambda + DynamoDB**.

### Why this choice

The serverless approach solved the persistence problem while staying appropriate for a low-traffic portfolio. It also created useful hands-on experience with a real API, IAM permissions, Lambda and DynamoDB without introducing a permanently running server.

### Implementation

1. Created a DynamoDB table using on-demand capacity.
2. Created a Python Lambda function to read/update the stored count.
3. Granted the Lambda function the required DynamoDB permissions.
4. Exposed the function through an API Gateway HTTP API.
5. Replaced the localStorage frontend logic with a JavaScript `fetch()` call to the API endpoint.
6. Added graceful frontend error handling so a temporary API issue does not break the page.
7. Tested the live site to verify the count persists outside the local browser.

### Result

The homepage now displays a persistent count backed by AWS rather than a per-browser approximation.

### Lesson

A feature can look correct while still having the wrong underlying data model. Checking what a metric actually represents is as important as making the UI work.

---

## WEB-13 — HTTPS, CloudFront and custom-domain behaviour

### Problem

A custom domain is only useful if the apex domain, `www` domain and HTTP/HTTPS behaviour resolve consistently and securely.

### Decision

Use **CloudFront** as the delivery layer, **ACM** for the certificate and **Route 53** for DNS.

### Implementation

- Confirmed the CloudFront viewer policy redirects HTTP to HTTPS.
- Confirmed the ACM certificate in `us-east-1` covers both the apex and `www` hostnames.
- Confirmed both alternate domain names are configured on the CloudFront distribution.
- Added the Route 53 apex A Alias to the existing CloudFront distribution.
- Tested the final domain behaviour from the public site.

### Result

The public portfolio resolves through the intended CloudFront distribution and uses HTTPS consistently.

### Lesson

Domain problems often span several services at once. Troubleshooting is easier when DNS, certificate scope, distribution aliases and redirect policy are checked as one end-to-end request path.

---

## WEB-07 / WEB-16 / WEB-17 — Contact form reliability and presentation

### Problem

The contact capability needed to be easy to find, work reliably and visually match the rest of the site without making another project page feel overloaded.

### Options considered

- Keep the form embedded on an existing long page.
- Use a mailto link only.
- Give contact a dedicated page while retaining an external form-processing service.

### Decision

Create a dedicated `contact.html` page and retain **Formspree** as the submission backend.

### Implementation

- Created a dedicated Contact page.
- Updated site navigation to point directly to it.
- Kept the working Formspree endpoint.
- Applied the site's existing CSS patterns so the form feels native to the portfolio.
- Retained success and error handling for submissions.
- Removed the old embedded form from the Cloud Resume page.

### Result

Contact is now easier to discover, cleaner in the overall information architecture and visually consistent with the portfolio.

### Lesson

Not every improvement requires more technology. Sometimes the best fix is better information architecture and reuse of a reliable managed service.

---

## WEB-20 — Certification badges and verification

### Problem

The certification page needed to distinguish verified, earned credentials from certifications that are only planned or in progress. It also needed room to grow as new badges are earned.

### Decision

Use a featured credential grid for earned certifications, with each badge linking to a public verification page. Keep planned/in-progress certifications visually separate.

### Result

The page now provides evidence for existing credentials without implying that future certifications have already been earned.

### Lesson

A portfolio is more credible when it is explicit about what is complete, what is underway and what is only planned.

---

## WEB-21 — Projects index and delivery board

### Problem

As projects and project notes grew, a single long page became harder to navigate and did not clearly communicate delivery status.

### Decision

Turn Projects into a portfolio index, give projects dedicated destinations and rebuild Project 01 around a Kanban-style Project Delivery Board.

### Implementation

- Converted Projects into a linked project index.
- Added dedicated project destinations.
- Linked the Cloud Resume Challenge as its own project area.
- Rebuilt Project 01 around the `WEB-01` to `WEB-21` delivery history.
- Marked Cloud Resume & Portfolio Website Phase 1 complete while keeping the wider Cloud Resume Challenge ongoing.

### Result

Visitors can scan the portfolio quickly, then drill into the level of detail they want.

### Lesson

Good project documentation needs navigation and status clarity just as much as technical detail.

---

## Navigation and responsive-layout growth

### Problem

Adding dedicated Education, Certifications, Projects, Cloud Resume Challenge and Contact destinations increased the width and complexity of the main navigation.

### Decision

Keep the full navigation, but tune spacing and responsive behaviour instead of removing useful destinations purely to make the header smaller.

### Result

The navigation remains complete while behaving more reliably across desktop and mobile layouts.

### Lesson

Responsive design needs to be revisited as information architecture changes. A layout that worked for five links may not work for eight.

---

## Production source-of-truth and cache troubleshooting

### Problem

Continued website development had caused the local and production versions of the portfolio to diverge. Some pages contained newer local changes while others contained newer production content, meaning neither version could safely be treated as the complete source of truth.

### Decision

Perform a page-by-page reconciliation before making any further production changes, establish the reviewed local repository as the canonical source and then deploy the complete reconciled website.

### Implementation

- Compared the local and production versions of the portfolio page by page.
- Preserved the newest valid content from each side.
- Established the reconciled local website as the canonical source of truth.
- Uploaded the reviewed website files to the production S3 bucket.
- Invalidated the CloudFront distribution.
- Verified the S3 objects and AWS delivery path.
- Investigated apparent stale content on the `www` domain.
- Used cache-busting requests to distinguish cached browser responses from the actual deployed content.

### Result

The local repository, S3-hosted production content and public website were brought back into alignment. The apparent post-deployment mismatch was confirmed to be caching behaviour rather than an incorrect S3 upload, CloudFront origin or Route 53 configuration.

### Lesson

Production troubleshooting should verify each layer before infrastructure is changed. A stale response does not necessarily mean a failed deployment, and maintaining a clearly defined source of truth significantly reduces deployment risk.
