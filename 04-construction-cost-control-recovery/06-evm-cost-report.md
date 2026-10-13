# Monthly Earned Value (EVM) Cost Report – Week 26 (Month 6)

> **Simulated project.** Organisation, people and data are fictional and based on a PM Project Lab practice brief. The PM artefacts are my own work, produced to practise real project-management delivery.

Measures the **remaining scope** after the re-baseline (Budget at Completion, BAC = $22.8M cost-to-complete). $15.2M had already been spent before recovery started.

![EVM S-curve](assets/evm-s-curve.png)

| Measure | Value | What it means |
|---|---|---|
| Planned Value (PV) | $11.40M | Work scheduled by Week 26 |
| Earned Value (EV) | $10.90M | Value of work actually completed (site-verified) |
| Actual Cost (AC) | $11.20M | What we actually paid |
| Cost Variance (CV = EV − AC) | −$0.30M | Slightly over cost for work done |
| Schedule Variance (SV = EV − PV) | −$0.50M | Slightly behind (window delay) |
| CPI (EV ÷ AC) | 0.97 | Getting $0.97 of work per $1 spent – target ≥ 0.97 met |
| SPI (EV ÷ PV) | 0.96 | Progressing at 96% of plan |
| EAC for remaining scope (BAC ÷ CPI) | $23.43M | Forecast cost of remaining work |
| Forecast final cost ($15.2M + EAC) | $38.63M | +1.7% vs $38M budget (target ≤ +3%); was +9% at start |

**Commentary:** cost is back within tolerance. Schedule slipped by about 2 weeks because of the window delay (I-02); the temporary enclosure recovered interior work sequencing. Next month's focus: close out the remaining 11 change orders and track the extra heating cost.

The S-curve is generated from [`evm-data.csv`](evm-data.csv) by [`assets/make_chart.py`](assets/make_chart.py).
