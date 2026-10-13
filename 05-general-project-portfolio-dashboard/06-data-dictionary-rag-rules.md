# Data Dictionary and RAG Rules – Project Portfolio Dashboard

> **Simulated project.** Organisation, people and data are fictional and based on a PM Project Lab practice brief. The PM artefacts are my own work, produced to practise real project-management delivery.

## Data dictionary (core fields)
| Field | Definition | Source | Owner |
|---|---|---|---|
| Budget (CAD) | Approved project budget incl. approved changes | Finance system | Finance |
| Actual to date (CAD) | Costs posted to project to date | Finance export (weekly) | Finance |
| % complete | PM-assessed % of deliverables accepted | Status form | PM |
| Schedule variance (days) | Forecast vs baseline date of next key milestone (negative = late) | Status form | PM |
| Open high risks | Risks scored 15+ (5×5 matrix) | Status form | PM |
| Staffing gap (FTE) | Planned FTE minus assigned FTE | Resourcing export | Delivery Ops |
| Cost index | (% complete × budget) ÷ actual to date | Calculated | BI Lead |

## RAG rules (agreed by all practice leads, Week 6)
| Dimension | Green | Amber | Red |
|---|---|---|---|
| Schedule variance | 0 to −5 days | −6 to −15 days | worse than −15 days |
| Cost index | ≥ 0.95 | 0.85–0.94 | < 0.85 |
| Open high risks | 0–1 | 2 | 3 or more |
| Staffing gap | 0 | 0.5 FTE | 1 FTE or more |

**Overall RAG** = the worst of the four dimensions. A PM may request an override, with a written reason that is logged and reviewed by the Head of PMO.
