# Source Review — Website v26

Reviewed before the public source commit on 19 August 2026.

## Security checks

No AWS access keys, secret access keys, passwords, private keys, bearer tokens or API keys were found in the supplied Website Project v26 source.

The following public application endpoints are intentionally present in the frontend:

- Formspree contact endpoint: used by the public contact form.
- API Gateway visitor-counter endpoint: called directly by browser JavaScript.

These are public-facing endpoints rather than credentials. They should still be protected operationally through appropriate backend permissions, validation, throttling/rate controls where needed, and least-privilege IAM.

## Packaging correction

The supplied v26 ZIP referenced `styles.css` from every HTML page but did not include the stylesheet itself. The stylesheet was restored from the recent Website Project file set before preparing this GitHub source commit.

## Project-state corrections included

- Project 01 delivery board now records WEB-01 through WEB-21 as 21/21 complete.
- Project 01 includes a small link to the GitHub repository.
- Cloud Resume Challenge Step 12 (Source Control) is marked complete because this commit places the source under GitHub version control.
- Tests, Infrastructure as Code and CI/CD remain planned and are not represented as complete.

## Backend source

The deployed Python Lambda source was not part of the supplied website ZIP, so it has not been invented or reconstructed here. The `backend/` folder remains a documented placeholder until the real deployed function can be exported/reviewed and committed.
