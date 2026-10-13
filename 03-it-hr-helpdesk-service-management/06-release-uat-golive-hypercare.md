# Release & Launch Readiness, UAT, Go-Live Checklist and Hypercare – HR Helpdesk & Case Management System

> **Simulated project.** Organisation, people and data are fictional and based on a PM Project Lab practice brief. The PM artefacts are my own work, produced to practise real project-management delivery.

## UAT scenarios (sample)
| ID | Scenario | Expected result | Result |
|---|---|---|---|
| UAT-01 | Employee raises a benefits question via portal | Ticket in HR queue; SLA timer started; confirmation email | Pass |
| UAT-02 | Employee raises a confidential concern | Ticket only visible to HR Investigator role | Pass |
| UAT-03 | HR agent (non-investigator) searches for a confidential ticket | No results; attempt logged | Pass |
| UAT-04 | General ticket contains the word "harassment" | Auto re-routed to confidential project; Privacy Officer alerted | Pass |
| UAT-05 | Email to hr@ from an employee | Ticket created under 2 min; employee matched via directory | Pass |
| UAT-06 | Ticket breaches 1-day SLA | Escalation alert to HR Ops Lead | Pass |

## Launch-readiness checklist
- [x] UAT signed off by Product Owner and Privacy Officer
- [x] 18 HR agents trained (100%); user guide published
- [x] 38 knowledge articles live (target 40; 2 scheduled in hypercare)
- [x] CHRO launch email and intranet article approved
- [x] WhatsApp HR groups retirement date announced (2 weeks after launch)
- [x] Support model agreed: IT service desk L1, ITSM team L2, partner L3
- [x] Rollback: email channel remains active if portal unavailable

## Hypercare (Weeks 13–15)
Daily 15-min check-in; monitor ticket volume, SLA %, mis-routed tickets and confidential re-routes. **Exit criteria:** SLA at or above 90% for 2 consecutive weeks, no open high defects, handover to IT support signed.
