# Project Charter – Clinic Appointment Scheduling Upgrade

> **Simulated project.** Organisation, people and data are fictional and based on a PM Project Lab practice brief. The PM artefacts are my own work, produced to practise real project-management delivery.

| Item | Detail |
|---|---|
| Organisation | Riverbend Community Hospital (fictional) – 200-bed provider with 6 outpatient clinics |
| Industry | Healthcare |
| Project Manager | Sola Debanjo, PMP |
| Executive Sponsor | David Mensah, Chief Operating Officer |
| Delivery approach | Hybrid (Waterfall governance + Agile configuration sprints) |
| Duration | 21 weeks (Week 1 = 05 Jan 2026, simulated) |
| Team size | 13 |
| Budget (assumed) | CAD $850,000 (assumed; includes 10% contingency) |

## 1. Business problem
The legacy scheduling tool is unsupported, cannot send automated reminders, allows double bookings and produces no usable reporting. Booking staff spend significant time on manual reminder calls, and a high no-show rate wastes clinic capacity and lengthens wait lists.

## 2. Purpose
Replace the legacy scheduling system across all six outpatient clinics with a supported, integrated scheduling module with automated reminders and operational reporting, delivered safely without disrupting patient care.

## 3. Objectives and success measures
| # | Objective | Measure / target |
|---|---|---|
| 1 | Go live on the new scheduling module in all 6 clinics | Go-live by Week 18; within approved budget (±5%) |
| 2 | Automate appointment reminders | 100% of booked appointments receive an SMS/email reminder 48 h before |
| 3 | Reduce missed appointments | No-show rate from 18% (simulated baseline) to 12% or lower within 3 months of go-live |
| 4 | Protect patient safety and data | Zero critical defects open at go-live; privacy impact assessment approved |
| 5 | Prepare staff | 90% or more of booking and clinic staff trained before go-live |
| 6 | Give managers visibility | Daily utilisation and no-show report available to clinic managers from Week 19 |

*Baselines and targets are simulated planning assumptions, not real-world results.*

## 4. Scope
**In scope**
- Configuration of the vendor's scheduling module for 6 clinics (templates, resources, booking rules)
- Integration with the patient administration system (demographics) via the interface engine
- Automated SMS/email reminder service
- Migration of future-dated appointments from the legacy system
- Role-based access, audit logging and privacy impact assessment
- Training, UAT, go-live cutover and 4 weeks of hypercare
- Clinic utilisation and no-show reporting

**Out of scope**
- Patient self-booking portal (Phase 2)
- Billing or clinical documentation changes
- Inpatient bed management
- Hardware refresh of front-desk PCs

## 5. Key deliverables
- Configured, tested scheduling module live in 6 clinics
- Integration with patient administration system
- Migrated future-dated appointments with reconciliation sign-off
- Prioritised scope backlog with acceptance criteria
- Release & launch-readiness plan
- UAT plan, go-live checklist and hypercare plan
- Training materials and quick-reference guides
- Closure report and benefits tracking handover

## 6. Milestones
| Week | Target date | Milestone |
|---|---|---|
| 1 | 05 Jan 2026 | Charter approved |
| 3 | 19 Jan 2026 | Requirements signed off |
| 6 | 09 Feb 2026 | Configuration design approved |
| 10 | 09 Mar 2026 | Integration build complete |
| 12 | 23 Mar 2026 | Data migration trial reconciled |
| 16 | 20 Apr 2026 | UAT sign-off |
| 17 | 27 Apr 2026 | Go / no-go decision |
| 18 | 04 May 2026 | Go-live (all clinics) |
| 21 | 25 May 2026 | Hypercare exit & closure |

## 7. Assumptions
- Vendor provides a dedicated implementation lead for the full project
- Interface engine team can give 2 days/week to the integration from Week 7
- Clinic managers release booking staff for 2 × 3-hour training sessions each
- Legacy system stays available read-only for 6 months after go-live

## 8. Constraints
- Patient bookings must continue throughout; cutover over a weekend only
- Patient safety and privacy approvals (privacy impact assessment) are on the critical path
- Limited contingency: any scope increase goes through formal change control
- Fixed vendor contract; extra vendor days require a change request

## 9. High-level risks
- Vendor misses integration milestone, delaying system testing (owner: IT Lead)
- Booking staff resist new workflows, slowing adoption (owner: Booking Lead)
- Migrated appointments lost or duplicated (owner: IT Lead)
- Reminder messages expose patient information (owner: Privacy Officer)
- Clinicians unavailable for UAT (owner: Clinical Lead)

## 10. Budget summary (assumed)
| Cost category | Amount (CAD) | Notes |
|---|---|---|
| Vendor licences & implementation services | $410,000 | Fixed-price contract |
| Internal IT & interface engine effort | $150,000 | Backfill for analysts |
| SMS/email reminder service (Year 1) | $45,000 | Per-message pricing |
| Training & backfill for booking staff | $90,000 | 2 sessions per person |
| Project management & change management | $77,000 |  |
| Contingency (10%) | $78,000 | Released by sponsor only |
| **Total** | **$850,000** |  |

## 11. Governance
Monthly **Steering Committee** (COO – chair, Director of Ambulatory Care, IT Director, Privacy Officer, PM). Weekly **project working group** (PM, clinical lead, IT lead, booking office lead, vendor lead). Change requests above $10,000 or 1 week of schedule impact go to the Steering Committee; smaller changes are approved by the sponsor.

## 12. Approval
| Role | Name | Decision | Date |
|---|---|---|---|
| Executive Sponsor | David Mensah | Approved | 09 Jan 2026 |
| Project Manager | Sola Debanjo | Prepared | 07 Jan 2026 |
