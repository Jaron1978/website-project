# Lessons Learned

## 1. A working UI is not proof that the underlying system is correct

The original visitor counter visibly changed a number, but the value existed only in browser storage. Replacing it with a shared backend reinforced the importance of validating what data actually represents.

## 2. Troubleshoot the whole request path

Custom-domain issues can involve DNS, CloudFront aliases, certificate coverage and redirect policy simultaneously. Treating the path end-to-end was more effective than looking at any single AWS service in isolation.

## 3. Do not over-engineer every feature

The visitor counter was worth building in AWS because it is part of the Cloud Resume learning objective. The contact form did not need another custom backend when Formspree already solved the requirement reliably.

## 4. Status accuracy matters

The completed website phase and the wider Cloud Resume Challenge are not the same thing. Keeping those statuses separate makes the portfolio more trustworthy and gives future work a clear place to go.

## 5. Documentation becomes more valuable when it records decisions

A list of technologies says what was used. A decision record explains why it was used, which alternatives were rejected and what trade-offs were accepted. That is much more useful in an interview or technical review.

## 6. Information architecture is part of engineering quality

As the site expanded, dedicated pages, clearer navigation and a project index became necessary. Technical portfolios still need strong UX: visitors should be able to find evidence without reading the entire site.

## 7. Build for extension, not hypothetical complexity

The site now has room for additional projects and certifications, but the architecture remains proportionate to today's requirements. Future capabilities can be added when they become real needs.

## 8. Establish and protect a clear source of truth

Continued development caused the local and production versions of the portfolio to diverge, with newer content existing on different sides. A page-by-page reconciliation was required before the site could be safely redeployed.

The local repository was re-established as the canonical source of truth and the complete reviewed site was deployed to S3. When some pages initially appeared stale after deployment, the delivery path was validated through S3, CloudFront and Route 53, with cache-busting requests confirming that the deployed content was correct.

This reinforced the importance of maintaining a clear source of truth, deploying from a controlled state and distinguishing deployment problems from caching behaviour before changing infrastructure.
