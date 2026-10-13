# Executive Status Report – Week 35 (Go / No-Go week)

> **Simulated project.** Organisation, people and data are fictional and based on a PM Project Lab practice brief. The PM artefacts are my own work, produced to practise real project-management delivery.

**Project:** Customer Churn Reduction Project **Sponsor:** Daniel Adebayo **PM:** Sola Debanjo **Overall status: AMBER**

## "Are we still on track?" – evidence, not reassurance
**Partly.** Residential customers (about 85% of the base) can go live on **Week 37 as planned**. SME accounts **cannot**: UAT found a serious defect that gives some SME customers the wrong churn-risk score. I recommend a **phased go-live**, with SME 3 weeks later (Week 40), after the fix is retested. Budget stays within tolerance.

| Area | RAG | Evidence |
|---|---|---|
| Schedule | Amber | Residential on plan (Week 37); SME forecast Week 40 (+3 weeks) |
| Budget | Green | $905K spent of $1.2M (75%) at 81% schedule; forecast $1.16M |
| Scope | Green | CR-02 (SME renewal alerts) approved Week 20; no other changes |
| Quality | Red → Amber | UAT: 212 of 230 scenarios passed; 1 critical defect (I-02) with fix plan; 4 medium |
| Adoption | Green | 8 of 8 save-desk agents trained and assessed |
| Service continuity | Green | No customer-facing incidents caused by the project |

## Decision needed
Approve **phased go-live** (option B in decision log D-05).

## Top risks
| Risk | Score | Action | Owner |
|---|---|---|---|
| Fix for duplicate SME IDs creates new data issues | 12 | Full regression on SME dataset; reconciliation to billing | Emeka Umeh |
| Save desk overloaded at launch | 9 | Start with top 2,000 risk accounts per week; scale up | Ruth Asante |

*All figures are simulated for this practice project.*
