# 🌐 Cloud Resume & Portfolio Website

A production portfolio website hosted on AWS and built as the first completed phase of my wider Cloud Resume Challenge journey.

<p align="center">
  <a href="https://www.ron-jackson.co.uk">🌍 Live Website</a> •
  <a href="https://github.com/Jaron1978/website-project">📁 Repository</a> •
  <a href="docs/architecture.md">🏗️ Architecture</a> •
  <a href="docs/challenges.md">🧠 Engineering Challenges</a>
</p>

---

## 🚀 Project Snapshot

✅ **Website Phase 1 Complete**  
🔄 **Cloud Resume Challenge Ongoing**  
☁️ **AWS Hosted**  
🔐 **HTTPS / Custom Domain**  
⚡ **Serverless Visitor Counter**  
📊 **Project Delivery Board**

## ✨ Key Features

**🌐 Portfolio:** Responsive multi-page website · Dedicated project pages · Certification verification  
**☁️ Cloud:** S3 · CloudFront · Route 53 · ACM  
**⚡ Serverless:** API Gateway · Lambda · DynamoDB visitor counter  
**📨 Integration:** Formspree contact handling  
**📋 Delivery:** Kanban project board · Architecture · Decision & lessons-learned documentation

## Architecture

![Cloud Resume & Portfolio Website Architecture](diagrams/Cloud%20Resume%20and%20Website.png)

### ☁️ Production Architecture

The live website uses a serverless AWS architecture for secure content delivery and the persistent visitor counter.

**Website:** Route 53 → CloudFront → S3  
**Visitor Counter:** API Gateway → Lambda (Python) → DynamoDB  
**Security:** ACM · HTTPS  
**Contact:** Formspree

[View the detailed architecture documentation →](docs/architecture.md)

## 🛠️ Technology Stack

**☁️ AWS:** S3 · CloudFront · Route 53 · ACM · API Gateway · Lambda · DynamoDB  
**💻 Development:** Python · HTML · CSS · JavaScript  
**🔧 Tooling & Integration:** Git · GitHub · Formspree

## 🧠 Engineering Highlights

This project records the engineering decisions and troubleshooting behind the finished portfolio — not just the final result.

- **Persistent visitor counter** — replaced browser-only storage with API Gateway, Lambda and DynamoDB
- **HTTPS & domain configuration** — implemented CloudFront, ACM and Route 53 correctly
- **Portfolio restructuring** — evolved the site into dedicated project pages with a Kanban delivery board
- **Contact handling** — separated the contact experience while maintaining reliable form submission
- **Responsive development** — improved navigation and layout as the portfolio expanded
- **- **Production source-of-truth & cache troubleshooting** — reconciled diverged local and production website content, re-established the local repository as the canonical source, redeployed the site and traced an apparent production mismatch across S3, CloudFront, Route 53 and browser caching

[Read the engineering challenges →](docs/challenges.md) · [Decision log →](docs/decision-log.md) · [Lessons learned →](docs/lessons-learned.md)

The most useful stories from Website Phase 1 are documented in docs/challenges.md.

Examples include:

* Replacing a browser-only visitor counter with a persistent AWS-backed service.
* Correctly configuring HTTP-to-HTTPS, CloudFront, ACM and Route 53 domain behaviour.
* Separating the contact form into a dedicated page while retaining reliable submission handling.
* Restructuring the Projects area into a portfolio index with dedicated project pages and a Kanban-style delivery board.
* Building a certification page that separates earned credentials from in-progress goals and provides verification links.
* Improving navigation and responsive behaviour as the site expanded.
* Reconciling local and production versions of the website, establishing a clear source of truth and diagnosing stale browser responses through the S3 → CloudFront → Route 53 delivery path.

## 🗺️ Status & Roadmap

### ✅ Website Phase 1 — Complete

Website Phase 1 was delivered through tasks `WEB-01` to `WEB-21`, establishing the production portfolio and its AWS-backed functionality.

### 🔄 Cloud Resume Challenge — Ongoing

The wider Cloud Resume Challenge continues beyond the completed website phase. Only genuinely completed work is marked as complete.

### 🌃 Portfolio Phase 2 — Planned

The next evolution of the portfolio will introduce the **London Cloud Experience**, including:

- Full-screen London-at-night welcome experience
- Explore Portfolio, Download CV and Ask RonBot visitor routes
- Professionally presented downloadable CV
- RonBot integration and contextual AI-powered portfolio features
- Continued evolution of the existing Phase 1 portfolio rather than replacement

## 📚 Documentation & Repository

The repository contains the reviewed website source alongside the engineering documentation created during development.

**📁 Website source:** [`website/`](website/)  
**🏗️ Architecture:** [`docs/architecture.md`](docs/architecture.md)  
**🧠 Engineering challenges:** [`docs/challenges.md`](docs/challenges.md)  
**📝 Decision log:** [`docs/decision-log.md`](docs/decision-log.md)  
**💡 Lessons learned:** [`docs/lessons-learned.md`](docs/lessons-learned.md)

> The `backend/` directory is reserved for the real deployed visitor-counter Lambda source once it has been exported and reviewed. No backend implementation is fabricated for the repository.

---

<p align="center">
  <a href="https://www.ron-jackson.co.uk">🌍 Live Website</a> •
  <a href="https://github.com/Jaron1978">👤 GitHub Profile</a> •
  <a href="https://github.com/Jaron1978/RonBot-repo">🤖 RonBot</a>
</p>
