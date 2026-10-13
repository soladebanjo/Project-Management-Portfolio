# Stakeholder Register and RACI – Clinic Appointment Scheduling Upgrade

> **Simulated project.** Organisation, people and data are fictional and based on a PM Project Lab practice brief. The PM artefacts are my own work, produced to practise real project-management delivery.

## Stakeholder register
| Stakeholder | Role | Primary concern | Influence | Interest | Engagement approach |
|---|---|---|---|---|---|
| David Mensah | Executive Sponsor (COO) | Outcome, patient safety and budget | High | High | Monthly steering; weekly 1-page update; decision requests with options |
| Mariam Bello | Clinical / Service Lead (Outpatient Services Manager) | Operational impact and adoption | High | High | Weekly working group; co-designs clinic templates; signs off UAT |
| Fatima Sule | Technology Lead (IT Applications Manager) | Integration, security and delivery capacity | High | High | Weekly working group; owns technical design and integration |
| Michael Adekunle | Operations / Frontline Lead (Booking Office Supervisor) | Workflow disruption and usability | Medium | High | Super-user network lead; early demos; training schedule |
| Vendor Implementation Lead | Supplier | Contract scope and payment milestones | Medium | High | Weekly vendor checkpoint; milestone evidence reviews |
| Privacy Officer | Compliance | Patient data protection, access control | High | Medium | Privacy impact assessment; review of reminder content |
| Clinic physicians | End users (clinical) | Clinic templates, session lengths | Medium | Medium | Clinic huddles; template review sessions |
| Booking & reception staff | End users | Ease of use, workload during cutover | Low | High | Super-users, hands-on training, floor-walkers at go-live |
| Patients / Patient Advisory Council | Service users | Clear reminders, no lost appointments | Low | Medium | Reminder wording tested with council; patient notices |

## Power / interest summary
- **Manage closely (high influence, high interest):** David Mensah, Mariam Bello, Fatima Sule
- **Keep satisfied (high influence, lower interest):** Privacy Officer
- **Keep informed (lower influence, high interest):** Michael Adekunle, Vendor Implementation Lead, Booking & reception staff
- **Monitor:** Clinic physicians, Patients / Patient Advisory Council

## RACI matrix
R = Responsible · A = Accountable · C = Consulted · I = Informed

| Activity / deliverable | Sponsor | PM (Sola) | Clinical Lead | IT Lead | Booking Lead | Vendor | Privacy Officer |
|---|---|---|---|---|---|---|---|
| Project charter | A | R | C | C | I | I | I |
| Requirements & clinic templates | I | A | R | C | R | C | I |
| Integration build & testing | I | A | C | R | I | R | I |
| Privacy impact assessment | I | A | C | C | I | C | R |
| Data migration & reconciliation | I | A | C | R | R | R | I |
| Training | I | A | C | I | R | R | I |
| UAT sign-off | I | R | A | C | R | C | I |
| Go / no-go decision | A | R | C | C | C | C | C |
| Hypercare & issue resolution | I | A | C | R | R | R | I |

**Rule applied:** exactly one **A** per row, so every deliverable has a single accountable owner.
