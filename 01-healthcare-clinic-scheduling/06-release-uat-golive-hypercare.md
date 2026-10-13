# Release & Launch Readiness, UAT, Go-Live Checklist and Hypercare – Clinic Appointment Scheduling Upgrade

> **Simulated project.** Organisation, people and data are fictional and based on a PM Project Lab practice brief. The PM artefacts are my own work, produced to practise real project-management delivery.

## 1. UAT plan
| Item | Detail |
|---|---|
| Window | Weeks 14–16 (re-planned to Weeks 15–17 after CR-03, see decision log) |
| Testers | 2 clinic managers, 6 booking clerks (1 per clinic), 2 physicians |
| Entry criteria | System test complete; no open critical defects; test data loaded |
| Exit criteria | 100% of Must scenarios passed; no open critical/high defects; Clinical Lead sign-off |
| Defect severity | Critical = patient safety or data loss; High = no workaround; Medium = workaround; Low = cosmetic |

### Sample UAT scenarios
| ID | Scenario | Expected result |
|---|---|---|
| UAT-01 | Book a new patient into a physician template | Slot booked, demographics pulled from patient administration system, reminder scheduled |
| UAT-02 | Attempt to double-book the same clinician | System blocks booking and shows message |
| UAT-03 | Patient replies "C" to reminder | Appointment cancelled, slot freed, booking office alerted |
| UAT-04 | Reschedule a migrated appointment | Original migrated data intact; new reminder generated |
| UAT-05 | Clerk without manager role tries to edit a template | Access denied and attempt logged |
| UAT-06 | Daily utilisation report | Counts match source data within 1% |

## 2. Release and launch-readiness plan
| Readiness area | Check | Owner | Status at go/no-go |
|---|---|---|---|
| Environment | Production configured and smoke-tested | IT Lead | Ready |
| Data | Final migration reconciled 100% (record counts and sample of 200 appointments) | IT Lead | Ready |
| People | Staff trained (target 90%) | Booking Lead | Ready – 94% |
| Support | Hypercare rota, floor-walkers, vendor on-call | IT Lead | Ready |
| Communications | Patients, clinics and switchboard notified | Clinical Lead | Ready |
| Rollback | Legacy system can be reactivated within 4 h | IT Lead | Tested in rehearsal |

## 3. Go-live checklist (cutover weekend)
- [ ] Friday 18:00 – legacy system set to read-only; booking freeze announced
- [ ] Friday 19:00 – final extract; migration load started
- [ ] Saturday 09:00 – reconciliation (counts + 200-record sample) signed by IT Lead and Booking Lead
- [ ] Saturday 12:00 – integration and reminder smoke tests passed
- [ ] Saturday 15:00 – **go / no-go checkpoint 2** (Sponsor, PM, Clinical Lead, IT Lead)
- [ ] Sunday 10:00 – super-users run end-to-end test bookings in each clinic
- [ ] Monday 07:00 – floor-walkers in every clinic; command centre open
- [ ] Monday 17:00 – day-1 report to Sponsor

## 4. Hypercare plan (Weeks 18–21)
| Element | Plan |
|---|---|
| Support model | Command centre (Week 18), then daily stand-up; vendor on-call 07:00–19:00 |
| Issue handling | Logged in service desk; critical = 1 h response, high = 4 h |
| Monitoring | Daily: reminders sent vs booked, failed integrations, open tickets, no-show rate |
| Exit criteria | No critical/high tickets open for 10 working days; ticket volume falling; handover to IT Applications support signed |
