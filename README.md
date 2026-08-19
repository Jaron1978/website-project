# Cloud Resume & Portfolio Website

A cloud-hosted portfolio website built as the first completed phase of my wider Cloud Resume Challenge journey.

**Live site:** https://www.ron-jackson.co.uk  
**Repository:** https://github.com/jaron78/website-project  
**Project status:** Website Phase 1 complete; wider Cloud Resume Challenge ongoing.

## Project overview

The goal of this project was to build more than a static CV. I wanted a live portfolio that demonstrates practical cloud skills, documents the engineering decisions behind the build, and gives me a platform that can grow alongside future cloud and AI projects.

The finished website includes a responsive multi-page portfolio, custom domain and HTTPS delivery, a persistent visitor counter backed by AWS services, a working contact form, certification verification links, and a project delivery board that records the work completed during Website Phase 1.

## Architecture

Current production services and components include:

- **Amazon S3** — static website assets
- **Amazon CloudFront** — content delivery and HTTPS front end
- **Amazon Route 53** — DNS for `ron-jackson.co.uk`
- **AWS Certificate Manager (ACM)** — TLS certificate for the apex and `www` domains
- **Amazon API Gateway (HTTP API)** — visitor counter API endpoint
- **AWS Lambda (Python)** — visitor counter application logic
- **Amazon DynamoDB** — persistent visitor count storage
- **Formspree** — contact form handling
- **HTML / CSS / JavaScript** — frontend

See [docs/architecture.md](docs/architecture.md) for the technical breakdown.

## What this repository is for

This repository is both the source location for the project and an engineering record of how it evolved. The website shows the polished outcome; this repository explains the decisions behind it.

The documentation focuses on:

1. The problem or requirement.
2. The options considered.
3. The trade-offs behind the chosen solution.
4. How the solution was implemented.
5. How the result was verified.
6. What I learned from the work.

## Selected engineering challenges

The most useful stories from Website Phase 1 are documented in [docs/challenges.md](docs/challenges.md). Examples include:

- Replacing a browser-only visitor counter with a persistent AWS-backed service.
- Correctly configuring HTTP-to-HTTPS, CloudFront, ACM and Route 53 domain behaviour.
- Separating the contact form into a dedicated page while retaining reliable submission handling.
- Restructuring the Projects area into a portfolio index with dedicated project pages and a Kanban-style delivery board.
- Building a certification page that separates earned credentials from in-progress goals and provides verification links.
- Improving navigation and responsive behaviour as the site expanded.

## Project status

### Completed: Cloud Resume & Portfolio Website — Phase 1

Website Phase 1 was managed through tasks `WEB-01` to `WEB-21` and is complete.

### Ongoing: Cloud Resume Challenge

The broader Cloud Resume Challenge remains in progress. Items that have not genuinely been completed will not be represented here as complete simply to make the project appear further along.

## Repository structure

```text
.
├── README.md
├── docs/
│   ├── architecture.md
│   ├── challenges.md
│   ├── decision-log.md
│   └── lessons-learned.md
├── website/
│   └── README.md
├── backend/
│   └── README.md
└── diagrams/
    └── README.md
```

The `website/` and `backend/` folders are intentionally prepared for the reviewed production source files. Before committing production code, secrets, credentials, account-specific values and deployment artefacts should be checked and excluded where appropriate.

## Key principle

The most important part of this project is not that every decision was perfect on the first attempt. The value is in identifying problems, evaluating sensible alternatives, implementing a proportionate solution, testing the result, and documenting what changed.

That is the engineering story this repository is designed to show.
