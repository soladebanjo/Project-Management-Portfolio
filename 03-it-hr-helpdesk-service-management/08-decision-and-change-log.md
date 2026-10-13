# Decision Log and Change Request – HR Helpdesk & Case Management System

> **Simulated project.** Organisation, people and data are fictional and based on a PM Project Lab practice brief. The PM artefacts are my own work, produced to practise real project-management delivery.

## Decision log
| ID | Date | Decision | Made by | Rationale |
|---|---|---|---|---|
| D-01 | 12 Jan 2026 | Pilot with 2 departments before bank-wide launch | Sponsor | Test adoption and privacy model at low risk |
| D-02 | 12 Jan 2026 | Confidential cases in a separate restricted project, not just a hidden field | Privacy Officer | Stronger segregation, easier to audit |
| D-03 | 26 Jan 2026 | Add 'preferred adviser' routing (HR-07) | Product Owner | Answers HRBP concern about losing relationships (R-01) |
| D-04 | 23 Feb 2026 | Add keyword re-routing (HR-08) and negative permission tests to Definition of Done | Sponsor & Privacy Officer | Response to incident I-01 |
| D-05 | 23 Mar 2026 | GO for bank-wide launch | Sponsor | UAT passed; readiness checklist complete |

## Event: a sensitive case is logged in the general queue
**What happened (pilot week 1):** An employee raised a grievance about their manager using the "General question" request type. The ticket was visible to 6 HR agents for about 3 hours before an agent flagged it.

**My response**
| Step | Action | When |
|---|---|---|
| 1. Contain | Moved ticket to the restricted confidential project; checked the audit log for who viewed it (2 agents opened it) | Within 30 min of flag |
| 2. Notify | Informed Privacy Officer and Sponsor; Privacy Officer led the internal privacy assessment | Same day |
| 3. Support the employee | HR Investigator contacted the employee, explained what happened and how the case is now protected | Next morning |
| 4. Root cause | Confidential option was the 9th of 12 request types and labelled 'Employee relations' – unclear to employees | Day 2 |
| 5. Fix | Renamed to 'Raise a confidential concern', moved to the top; added keyword auto re-route (HR-08); reminder to agents on handling | Sprint 4 |
| 6. Prevent | Added negative permission tests to the Definition of Done; weekly audit of confidential re-routes during hypercare | Ongoing |

## Change request CR-01 (scope within sprint capacity)
| Field | Detail |
|---|---|
| Description | Add HR-08 keyword re-routing and permission testing |
| Schedule impact | None – HR-10 moved from Sprint 4 to Sprint 5 |
| Cost impact | $0 – within sprint capacity |
| Decision | Approved by Sponsor and Privacy Officer, 23 Feb 2026 |
