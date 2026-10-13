# RAID Log – Customer Churn Reduction Project

> **Simulated project.** Organisation, people and data are fictional and based on a PM Project Lab practice brief. The PM artefacts are my own work, produced to practise real project-management delivery.

Scoring: probability (1–5) × impact (1–5). **15+ = red**, 8–14 = amber, under 8 = green. Reviewed weekly in the project meeting and summarised in the steering update.

| Type | ID | Description | Probability | Impact | Score | Owner | Response / action | Status | Review date |
|---|---|---|---|---|---|---|---|---|---|
| Risk | R-01 | Billing and CRM account IDs don't match, so risk scores attach to the wrong customer | 3 | 5 | 15 | BI/CRM Lead | Data-quality rules + reconciliation in system test | Occurred → I-02 | Week 33 |
| Risk | R-02 | Network maintenance windows delay data-feed testing | 3 | 4 | 12 | PM | Book windows 6 weeks ahead; use extract file as fallback | Open | Week 26 |
| Risk | R-03 | Agents see save desk as extra workload; low adoption | 3 | 4 | 12 | Contact Centre | Agent focus groups, clear targets, recognition scheme | Open | Week 30 |
| Risk | R-04 | Retention offers erode revenue more than churn saves | 2 | 4 | 8 | Finance | Offer matrix with margin floor; Finance monthly review | Open | Week 16 |
| Risk | R-05 | Win-back contact breaches consent rules | 2 | 5 | 10 | Legal | Legal review; consent flag filter on campaign list | Closed | Week 34 |
| Assumption | A-01 | 24 months of history available and usable | — | — | — | BI/CRM Lead | Validated in Week 5 (21 months usable) | Validated with gap | Week 6 |
| Issue | I-01 | Stakeholders asked to add SME 'contract renewal' alerts after seeing first report | 4 | 3 | 12 | PM | Assessed via CR-02; approved with 1-week impact | Resolved | Week 20 |
| Issue | I-02 | UAT found duplicate SME account IDs causing wrong-customer risk scores (2 weeks before go-live) | 5 | 5 | 25 | PM | Phased go-live decision – see decision log D-05 | Resolved | Week 37 |
| Dependency | D-01 | Network ticket data feed (Network Operations) | — | — | — | PM | Data-sharing agreement signed Week 12 | Open | Week 28 |
| Dependency | D-02 | Finance approval of offer budget before Gate 3 | — | — | — | Finance | Approved Week 15 | Closed | Week 16 |
