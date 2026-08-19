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
