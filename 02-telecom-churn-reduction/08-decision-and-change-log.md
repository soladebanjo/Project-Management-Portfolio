# Decision Log and Change Requests – Customer Churn Reduction Project

> **Simulated project.** Organisation, people and data are fictional and based on a PM Project Lab practice brief. The PM artefacts are my own work, produced to practise real project-management delivery.

## Decision log
| ID | Date | Decision | Made by | Rationale |
|---|---|---|---|---|
| D-01 | 19 Jan 2026 | Gate 1 approved – Waterfall with 4 stage gates | Steering Committee | Data and process dependencies need sequenced sign-offs |
| D-02 | 09 Mar 2026 | Use rules-based risk score for Release 1; predictive model later | Business Owner | Explainable to agents; data history limited to 21 months |
| D-03 | 13 Apr 2026 | Offer matrix approved with margin floor | Finance & Sponsor | Controls offer cost (R-04) |
| D-04 | 18 May 2026 | CR-02 approved: add SME renewal alerts (+1 week, +$12K) | Sponsor | High value for SME retention; within tolerance |
| D-05 | 31 Aug 2026 | Phased go-live: residential Week 37, SME Week 40 | Steering Committee | See event below |

## Event: UAT finds a serious defect two weeks before go-live
**What happened:** In UAT (Week 34), testers found that about 3% of SME accounts had **duplicate account IDs** between billing and CRM. Their churn-risk scores attached to the wrong customer, so the save desk could call the wrong business with an offer.

**Decision path I followed**
1. **Classify:** severity *Critical* – wrong-customer contact is a privacy and reputation risk, not a cosmetic issue.
2. **Contain:** SME records excluded from the risk report immediately; residential data re-checked (clean – IDs reconciled 100%).
3. **Assess impact:** fix and regression test estimated at 3 weeks by the BI team (evidence: defect analysis, 1,140 affected records).
4. **Options to sponsor** (below), with my recommendation.
5. **Communicate:** same-day note to sponsor; steering decision within 48 h; contact centre and sales briefed on the phased plan.

| Option | Schedule | Cost | Risk | Recommendation |
|---|---|---|---|---|
| A. Go live fully on Week 37 and fix later | On time | $0 | High – wrong-customer contact; privacy breach risk | No |
| B. Phased: residential Week 37, SME Week 40 after fix | +3 weeks for SME only | +$18K (BI effort, from contingency) | Low | **Yes** |
| C. Delay all go-live to Week 40 | +3 weeks for everyone | +$40K (team extension) | Low, but delays benefits for 85% of customers | No |

## Change request CR-05
| Field | Detail |
|---|---|
| Description | Phased go-live: residential Week 37; SME Week 40 |
| Reason | Critical defect I-02 (duplicate SME account IDs) |
| Schedule impact | SME +3 weeks; closure still Week 43 |
| Cost impact | +$18K from contingency (contingency remaining $80K) |
| Decision | Approved by Steering Committee, 31 Aug 2026 |
