# Project Charter – HR Helpdesk & Case Management System (IT Service Management)

> **Simulated project.** Organisation, people and data are fictional and based on a PM Project Lab practice brief. The PM artefacts are my own work, produced to practise real project-management delivery.

| Item | Detail |
|---|---|
| Organisation | Prairie Shield Financial Group (fictional) – regional banking group, ~2,400 employees |
| Industry | IT / Service Management (HR technology) |
| Project Manager | Sola Debanjo, PMP |
| Executive Sponsor | James Okoro, Chief Human Resources Officer |
| Delivery approach | Agile (Scrum – 2-week sprints) |
| Duration | 15 weeks (Week 1 = 05 Jan 2026, simulated) |
| Team size | 8 |
| Budget (assumed) | CAD $180,000 (assumed; includes 10% contingency) |

## 1. Business problem
HR queries are untracked and scattered across personal inboxes and WhatsApp. Response times are unknown, knowledge isn't shared, and confidential matters are handled informally, which creates privacy and compliance risk for a regulated bank.

## 2. Purpose
Implement an HR service portal and case-management system (Jira Service Management) with a shared queue for routine requests, a restricted confidential workflow for sensitive cases, a knowledge base and service reporting.

## 3. Objectives and success measures
| # | Objective | Measure / target |
|---|---|---|
| 1 | Single front door for HR | 100% of routine HR queries logged via portal or email-to-ticket within 8 weeks of launch |
| 2 | Faster, measurable service | First response within 1 business day for 90% of tickets |
| 3 | Protect confidential cases | Grievance / investigation cases visible only to authorised HR investigators; zero unauthorised views |
| 4 | Self-service | Knowledge base with 40+ articles at launch |
| 5 | Visibility | Monthly report on volume, response time and top 10 query themes from Month 1 |
| 6 | Deliver on plan | Launch by Week 13 within budget |

*Baselines and targets are simulated planning assumptions, not real-world results.*

## 4. Scope
**In scope**
- Jira Service Management configuration: HR portal, request types, queues, SLAs
- Confidential case workflow with restricted permissions
- Email-to-ticket channel
- Knowledge base (40+ articles)
- Integration with the employee directory (SSO, employee details)
- Reporting dashboard
- Training for HR staff and launch communications to employees
- Pilot with 2 departments, then bank-wide launch

**Out of scope**
- Payroll system changes
- HRIS replacement
- WhatsApp integration (channel to be retired)
- Chatbot (future phase)

## 5. Key deliverables
- Project charter
- Prioritised product backlog with acceptance criteria
- Configured HR service portal & confidential workflow
- Knowledge base
- Release and launch-readiness plan
- UAT plan, go-live checklist and hypercare plan
- Training & user guides
- Closure report

## 6. Milestones
| Week | Target date | Milestone |
|---|---|---|
| 1 | 05 Jan 2026 | Charter approved |
| 2 | 12 Jan 2026 | Sprint 0 complete – backlog & design ready |
| 6 | 09 Feb 2026 | Confidential workflow & SSO done (Sprint 2) |
| 8 | 23 Feb 2026 | Pilot launch – 2 departments |
| 12 | 23 Mar 2026 | UAT & readiness sign-off |
| 13 | 30 Mar 2026 | Bank-wide launch |
| 15 | 13 Apr 2026 | Hypercare exit & closure |

## 7. Assumptions
- Bank already licenses Jira Service Management through IT
- HR provides content owners for knowledge articles
- Pilot departments (Retail Operations, Finance) agree to route all queries through the portal
- Employee directory supports SSO

## 8. Constraints
- Several stakeholders influence the work but don't report to the PM
- Some HR staff hesitant to use a shared queue
- Confidential cases must be segregated (privacy and banking compliance)
- Limited contingency; scope increases through change control

## 9. High-level risks
- HR Business Partners keep answering by email/WhatsApp, bypassing the queue (owner: HR Ops Lead)
- Sensitive case logged in the general queue (owner: Privacy Officer)
- SSO integration delayed by Identity team (owner: ITSM Lead)
- Knowledge articles not ready for launch (owner: Product Owner)

## 10. Budget summary (assumed)
| Cost category | Amount (CAD) | Notes |
|---|---|---|
| Configuration partner (Jira Service Management) | $62,000 | Fixed price |
| Additional agent licences (Year 1) | $24,000 | HR agents |
| Internal IT (SSO, directory integration) | $28,000 |  |
| Knowledge-base content & training | $22,000 | Writer + HR SMEs |
| Project management / Scrum facilitation | $27,600 |  |
| Contingency (10%) | $16,400 |  |
| **Total** | **$180,000** |  |

## 11. Governance
Agile delivery with a light governance wrapper: **sprint review** every 2 weeks (product owner, stakeholders); **monthly sponsor checkpoint** (CHRO, Head of IT Service Management, Privacy & Compliance Officer, PM). The product owner prioritises the backlog; anything that changes budget, launch date or the privacy model needs sponsor approval.

## 12. Approval
| Role | Name | Decision | Date |
|---|---|---|---|
| Executive Sponsor | James Okoro | Approved | 09 Jan 2026 |
| Project Manager | Sola Debanjo | Prepared | 07 Jan 2026 |
