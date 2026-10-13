# Decision Log and Change Request – Clinic Appointment Scheduling Upgrade

> **Simulated project.** Organisation, people and data are fictional and based on a PM Project Lab practice brief. The PM artefacts are my own work, produced to practise real project-management delivery.

## Decision log
| ID | Date | Decision | Made by | Rationale |
|---|---|---|---|---|
| D-01 | 19 Jan 2026 | Online self-booking moved to Phase 2 | Steering Committee | Protects Week 18 go-live; needs separate patient portal business case |
| D-02 | 09 Feb 2026 | Reminders contain date, time, clinic only – no clinical details | Privacy Officer & Sponsor | Minimum necessary information; closes R-04 |
| D-03 | 23 Mar 2026 | Reject vendor recovery date; re-plan go-live to Week 19 (CR-03) | Sponsor | Vendor date not supported by evidence; see below |
| D-04 | 27 Apr 2026 | GO for go-live Week 19 | Sponsor (go/no-go) | All readiness criteria met; 0 critical, 0 high defects |

## Event: vendor misses a milestone and offers an optimistic recovery date
**What happened (Week 10):** The vendor reported "integration 90% complete – will finish next week." The integration-complete milestone was missed.

**How I challenged it, using evidence:**
1. Asked for the integration **test results**, not a percentage: 11 of 24 interface messages were passing (46%), not 90%.
2. Checked the **dependency**: the interface engine team had only 1 day/week available for the next 2 weeks (holiday cover), not the 2 days agreed (D-01).
3. Compared against **acceptance criteria**: integration is only "complete" when all 24 message types pass, including error handling.
4. Asked the vendor and the interface team for a joint, task-level plan. This gave a realistic finish date of **Week 12**.

**Options assessed**
| Option | Schedule | Cost | Risk | Recommendation |
|---|---|---|---|---|
| A. Accept vendor date (Week 11) | Go-live Week 18 on paper | $0 | High – likely second slip, UAT squeezed, patient-safety testing cut | No |
| B. Re-plan to evidence-based date; use contingency; overlap training with system testing | Go-live Week 19 (+1 week) | $0 (vendor absorbs extra days under contract) | Low–medium | **Yes** |
| C. Go live without integration (manual demographics entry) | Week 18 | +$20K staff overtime | High – re-keying errors in patient identity | No |

## Change request CR-03
| Field | Detail |
|---|---|
| Requested by | Sola Debanjo (PM) |
| Description | Move go-live from Week 18 to Week 19; UAT moves to Weeks 15–17; training starts during system testing |
| Reason | Vendor integration milestone missed; realistic finish Week 12 |
| Schedule impact | +1 week (uses the 1 week of contingency) |
| Cost impact | $0 – vendor contract clause covers extra vendor days for vendor-caused delay |
| Scope / quality impact | None; full UAT kept |
| Decision | Approved by David Mensah, 23 Mar 2026 |
