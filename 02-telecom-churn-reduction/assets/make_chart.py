"""Builds assets/kpi-dashboard.png from kpi-dashboard.csv (simulated data). Run from the project folder: python assets/make_chart.py"""
import csv, os, sys
sys.path.insert(0, os.path.dirname(__file__))
from style import *
setup()
here = os.path.dirname(os.path.abspath(__file__))
rows = list(csv.DictReader(open(os.path.join(here, "..", "kpi-dashboard.csv"), encoding="utf-8")))
num = lambda s: float(s.replace("%", "").replace("$", "").replace("≤", "").replace("~", "").strip())
pick = ["Monthly churn rate", "Save rate (save desk)", "Offer approval within 24 h", "Repeat complaints within 30 days"]
better = {"Monthly churn rate": "lower", "Save rate (save desk)": "higher", "Offer approval within 24 h": "higher", "Repeat complaints within 30 days": "lower"}
fig, axes = plt.subplots(2, 2, figsize=(10, 6.2))
for ax, name in zip(axes.flat, pick):
    r = next(x for x in rows if x["KPI"] == name)
    xs, ys, labels = [], [], []
    if r["Baseline (simulated)"] not in ("n/a",):
        xs.append(0); ys.append(num(r["Baseline (simulated)"])); labels.append("Baseline")
    for i, m in enumerate(["Month 1", "Month 2", "Month 3"], 1):
        xs.append(i); ys.append(num(r[m])); labels.append(m)
    tgt = num(r["Target"])
    ax.axhline(tgt, color=INK2, lw=1.2, ls=(0, (4, 3)))
    ax.text(-0.25, tgt, f"Target {r['Target']}", va="bottom", ha="left", color=INK2, fontsize=9)
    ax.plot(xs, ys, color=S1, lw=2, marker="o", ms=6, markeredgecolor=SURF, markeredgewidth=1.5)
    ax.annotate(f"{ys[-1]:g}%", (xs[-1], ys[-1]), textcoords="offset points", xytext=(0, 9), ha="center", fontsize=9, color=INK)
    ax.set_xticks(range(4)); ax.set_xticklabels(["Baseline", "Month 1", "Month 2", "Month 3"], fontsize=9)
    ax.set_xlim(-0.3, 3.4)
    lo, hi = min(ys + [tgt]), max(ys + [tgt]); pad = (hi - lo) * 0.25 + 0.1
    ax.set_ylim(lo - pad, hi + pad)
    ax.set_title(f"{name.replace(' (save desk)', '')} (%) – {better[name]} is better", fontsize=10.5, loc="left", color=INK)
fig.suptitle("Churn Reduction – benefits KPIs after go-live (simulated data)", x=0.01, ha="left", fontsize=13, fontweight="bold")
fig.tight_layout(rect=(0, 0, 1, 0.95))
os.makedirs(here, exist_ok=True)
fig.savefig(os.path.join(here, "kpi-dashboard.png"), dpi=160)
print("saved kpi-dashboard.png")
