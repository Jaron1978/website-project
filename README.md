Cloud Resume & Portfolio Website

A cloud-hosted portfolio website built as the first completed phase of my wider Cloud Resume Challenge journey.

Live site: https://www.ron-jackson.co.uk
Repository: https://github.com/Jaron1978/website-project
Status: Website Phase 1 complete · Wider Cloud Resume Challenge ongoing

Project Overview

The goal of this project was to build more than a static CV.

I wanted a live portfolio that demonstrates practical cloud skills, documents the engineering decisions behind the build, and provides a platform that can grow alongside future Cloud and AI projects.

The finished website includes a responsive multi-page portfolio, custom domain and HTTPS delivery, a persistent AWS-backed visitor counter, a working contact form, certification verification links, and a project delivery board that records the work completed during Website Phase 1.

Key Features

* Responsive multi-page portfolio website
* Custom domain with HTTPS
* AWS-backed persistent visitor counter
* Dedicated contact page with working form submission
* Certification verification links
* Projects portfolio with dedicated project pages
* Kanban-style project delivery board
* Cloud Resume Challenge documentation
* Architecture, decision and lessons-learned records

Architecture

Current production services and components include:

* Amazon S3 — static website assets
* Amazon CloudFront — content delivery and HTTPS front end
* Amazon Route 53 — DNS for ron-jackson.co.uk
* AWS Certificate Manager (ACM) — TLS certificate for the apex and www domains
* Amazon API Gateway (HTTP API) — visitor counter API endpoint
* AWS Lambda (Python) — visitor counter application logic
* Amazon DynamoDB — persistent visitor count storage
* Formspree — contact form handling
* HTML / CSS / JavaScript — frontend

See docs/architecture.md for the technical breakdown.

Technologies

Cloud: AWS · S3 · CloudFront · Route 53 · ACM · API Gateway · Lambda · DynamoDB
Development: Python · HTML · CSS · JavaScript
Other: Formspree · Git · GitHub

What This Repository Is For

This repository is both the source location for the project and an engineering record of how it evolved.

The website shows the polished outcome; this repository explains the decisions behind it.

The documentation focuses on:

1. The problem or requirement.
2. The options considered.
3. The trade-offs behind the chosen solution.
4. How the solution was implemented.
5. How the result was verified.
6. What I learned from the work.

Selected Engineering Challenges

The most useful stories from Website Phase 1 are documented in docs/challenges.md.

Examples include:

* Replacing a browser-only visitor counter with a persistent AWS-backed service.
* Correctly configuring HTTP-to-HTTPS, CloudFront, ACM and Route 53 domain behaviour.
* Separating the contact form into a dedicated page while retaining reliable submission handling.
* Restructuring the Projects area into a portfolio index with dedicated project pages and a Kanban-style delivery board.
* Building a certification page that separates earned credentials from in-progress goals and provides verification links.
* Improving navigation and responsive behaviour as the site expanded.

Project Status

✅ Completed: Cloud Resume & Portfolio Website — Phase 1

Website Phase 1 was managed through tasks WEB-01 to WEB-21 and is complete.

🔄 Ongoing: Cloud Resume Challenge

The broader Cloud Resume Challenge remains in progress.

Items that have not genuinely been completed will not be represented here as complete simply to make the project appear further along.

Repository Structure

.
├── README.md
├── docs/
│   ├── architecture.md
│   ├── challenges.md
│   ├── decision-log.md
│   └── lessons-learned.md
├── website/
│   ├── index.html
│   ├── styles.css
│   ├── project-01.html
│   └── ...
├── backend/
│   └── README.md
└── diagrams/
    └── README.md

The website/ folder contains the reviewed Website Project source.

The backend/ folder is intentionally reserved for the real deployed visitor-counter Lambda source once it has been exported and reviewed; no backend code is fabricated in this repository.

Future Development

The completed Phase 1 website now provides the foundation for Portfolio Website Phase 2 — Cloud Experience.

Planned development includes:

* A full-screen London-at-night welcome experience
* Clear visitor routes into the existing portfolio
* Downloadable CV access
* RonBot integration as an optional AI-powered portfolio interface
* Further Cloud and AI enhancements as the wider portfolio develops

Phase 2 is being treated as a separate project so the completed Phase 1 implementation remains clearly documented.

Key Principle

The most important part of this project is not that every decision was perfect on the first attempt.

The value is in identifying problems, evaluating sensible alternatives, implementing a proportionate solution, testing the result, and documenting what changed.

That is the engineering story this repository is designed to show.
