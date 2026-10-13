# Current-State / Future-State Reporting Process – Project Portfolio Dashboard

> **Simulated project.** Organisation, people and data are fictional and based on a PM Project Lab practice brief. The PM artefacts are my own work, produced to practise real project-management delivery.

## Current state
```mermaid
flowchart LR
    A[PM builds own Excel report] --> B[Emails to practice lead]
    B --> C[Practice lead edits RAG]
    C --> D[PMO copies into master deck]
    D --> E[Leaders debate whose numbers are right]
```
**Pain points:** 6 different templates; RAG based on opinion; finance figures re-keyed by hand; about 3 hours per PM per week; reports are already a week old by the meeting.

## Future state
```mermaid
flowchart LR
    A[PM completes standard form - 15 min] --> D[(SharePoint list)]
    B[Finance export - automatic] --> E[Power BI data model]
    C[Resourcing export - automatic] --> E
    D --> E
    E --> F[RAG calculated by rules]
    F --> G[Portfolio dashboard refreshed Monday 08:00]
    G --> H[Weekly portfolio meeting uses dashboard as agenda]
```
## Controls and handoffs
| Control | Owner |
|---|---|
| Submission deadline Friday 15:00; missing reports shown on dashboard | Delivery Ops |
| Finance reconciliation check before refresh | BI Lead |
| RAG override only with written reason (logged) | Head of PMO |
| Row-level security by practice | BI Lead |
