# Project Charter – Customer Churn Reduction Project

> **Simulated project.** Organisation, people and data are fictional and based on a PM Project Lab practice brief. The PM artefacts are my own work, produced to practise real project-management delivery.

| Item | Detail |
|---|---|
| Organisation | ClearWave Telecom (fictional) – regional home-internet and SME broadband provider, ~180,000 subscribers |
| Industry | Telecommunications |
| Project Manager | Sola Debanjo, PMP |
| Executive Sponsor | Daniel Adebayo, Chief Commercial Officer |
| Delivery approach | Waterfall (stage-gated) |
| Duration | 43 weeks (Week 1 = 05 Jan 2026, simulated) |
| Team size | 17 |
| Budget (assumed) | CAD $1.2M (assumed; includes 10% contingency) |

## 1. Business problem
Monthly churn has risen to a simulated 2.4%. There is no early-warning signal for at-risk customers. Retention offers are inconsistent and slow (up to 5 days for approval), and repeat complaints about outages and billing are a leading reason customers leave.

## 2. Purpose
Build a repeatable churn-prevention capability: an early-warning churn-risk report, a dedicated retention ('save') desk with governed offers, and a redesigned complaint-to-resolution process, measured through a benefits dashboard.

## 3. Objectives and success measures
| # | Objective | Measure / target |
|---|---|---|
| 1 | Reduce churn | Monthly churn from 2.4% (simulated baseline) to 1.9% or lower within 6 months of go-live |
| 2 | Detect risk early | Weekly churn-risk list covering 100% of active accounts, ranked by risk score |
| 3 | Speed up retention offers | Offer approval in under 24 h for 95% of cases (baseline up to 5 days) |
| 4 | Fix the complaint loop | Repeat complaints within 30 days down from 22% to 15% (simulated) |
| 5 | No disruption | Zero unplanned customer-facing outages caused by the project |
| 6 | Deliver on plan | Go-live by Week 37 within budget ±5% |

*Baselines and targets are simulated planning assumptions, not real-world results.*

## 4. Scope
**In scope**
- Data integration of billing, CRM and network-ticket data into a churn-risk data mart
- Churn-risk scoring rules and weekly at-risk report (BI)
- Retention ('save') desk set-up: roles, scripts, offer matrix
- Offer approval workflow in CRM
- Complaint-handling process redesign (current → future state)
- Win-back campaign for recently lost customers (consent-compliant)
- Training for contact centre and field sales; benefits/KPI dashboard

**Out of scope**
- Network infrastructure upgrades
- Price-plan restructure
- New product development
- Replacing the CRM platform

## 5. Key deliverables
- Project charter and stage-gate approvals
- Current-state / future-state process map
- Churn-risk data mart and weekly risk report
- Save-desk operating model and offer matrix
- CRM offer-approval workflow
- Implementation plan with owners and acceptance criteria
- Benefits / KPI dashboard
- Closure pack with benefits-tracking handover

## 6. Milestones
| Week | Target date | Milestone |
|---|---|---|
| 3 | 19 Jan 2026 | Gate 1 – Charter approved |
| 10 | 09 Mar 2026 | Gate 2 – Requirements signed off |
| 16 | 20 Apr 2026 | Gate 3 – Design approved |
| 28 | 13 Jul 2026 | Build complete |
| 34 | 24 Aug 2026 | Gate 4 – UAT sign-off |
| 35 | 31 Aug 2026 | Go / no-go decision |
| 37 | 14 Sep 2026 | Go-live |
| 43 | 26 Oct 2026 | Benefits review & closure |

## 7. Assumptions
- Billing and CRM share a reliable customer account ID
- Contact centre can release 8 agents to form the save desk
- Finance approves an annual retention-offer budget before Gate 3
- Historical data (24 months) is available for scoring rules

## 8. Constraints
- The business must keep operating; no CRM downtime in business hours
- Network availability (maintenance windows) may affect data-integration testing
- Requirements likely to change once stakeholders see the first risk report
- Outbound win-back contact must follow anti-spam consent rules
- Limited contingency; scope increases through formal change control

## 9. High-level risks
- Billing and CRM account IDs don't match, so risk scores attach to the wrong customer (owner: BI/CRM Lead)
- Network maintenance windows delay data-feed testing (owner: PM)
- Agents see save desk as extra workload; low adoption (owner: Contact Centre)
- Retention offers erode revenue more than churn saves (owner: Finance)
- Win-back contact breaches consent rules (owner: Legal)

## 10. Budget summary (assumed)
| Cost category | Amount (CAD) | Notes |
|---|---|---|
| Data integration & BI development | $420,000 | Data engineers, BI developer |
| CRM workflow configuration | $180,000 | CRM partner |
| Save-desk set-up & training | $170,000 | Scripts, coaching, backfill |
| Process redesign & change management | $120,000 |  |
| Project management & QA | $200,000 |  |
| Contingency (10%) | $110,000 |  |
| **Total** | **$1,200,000** | Retention-offer budget held separately by Finance |

## 11. Governance
Stage-gated Waterfall. **Steering Committee** (CCO – chair, CFO delegate, CTO delegate, Head of Retention, PM) meets monthly and approves each gate. Weekly **delivery meeting** of workstream leads. Change requests over $15,000 or 2 weeks go to steering.

## 12. Approval
| Role | Name | Decision | Date |
|---|---|---|---|
| Executive Sponsor | Daniel Adebayo | Approved | 09 Jan 2026 |
| Project Manager | Sola Debanjo | Prepared | 07 Jan 2026 |
