"""Builds assets/portfolio-dashboard.png from portfolio-data.csv (simulated data).
RAG is calculated from the agreed rules (worst of 4 dimensions). Run: python assets/make_chart.py"""
import csv, os, sys
sys.path.insert(0, os.path.dirname(__file__))
from style import *
setup()
here = os.path.dirname(os.path.abspath(__file__))
rows = list(csv.DictReader(open(os.path.join(here, "..", "portfolio-data.csv"), encoding="utf-8")))

def rag(r):
    sv, hr, gap = float(r["Schedule variance (days)"]), int(r["Open high risks"]), float(r["Staffing gap (FTE)"])
    ci = float(r["% complete"]) / 100 * float(r["Budget (CAD)"]) / float(r["Actual to date (CAD)"])
    dims = ["G" if sv >= -5 else "A" if sv >= -15 else "R", "G" if ci >= 0.95 else "A" if ci >= 0.85 else "R",
            "G" if hr <= 1 else "A" if hr == 2 else "R", "G" if gap == 0 else "A" if gap < 1 else "R"]
    return ("Red" if "R" in dims else "Amber" if "A" in dims else "Green"), ci

for r in rows:
    r["calc"], r["ci"] = rag(r)
    assert r["calc"] == r["RAG"], f"RAG mismatch for {r['Project ID']}"
col = {"Green": GOOD, "Amber": WARN, "Red": CRIT}
fig = plt.figure(figsize=(12, 6.8))
gs = fig.add_gridspec(2, 2, height_ratios=[1, 4.2], hspace=0.35, wspace=0.35)
# stat tiles
tiles = [("Active projects", str(len(rows))), ("Red", str(sum(r["calc"] == "Red" for r in rows))),
         ("Amber", str(sum(r["calc"] == "Amber" for r in rows))), ("Green", str(sum(r["calc"] == "Green" for r in rows)))]
tax = fig.add_subplot(gs[0, :]); tax.axis("off")
for i, (lab, val) in enumerate(tiles):
    x = i * 0.25
    tax.text(x, 0.75, lab, fontsize=10.5, color=INK2, transform=tax.transAxes)
    tax.text(x, 0.05, val, fontsize=26, fontweight="bold", color=INK, transform=tax.transAxes)
    if lab in col:
        tax.plot([x + 0.075], [0.25], "o", ms=11, color=col[lab], transform=tax.transAxes)
order = sorted(rows, key=lambda r: float(r["Schedule variance (days)"]))
ax = fig.add_subplot(gs[1, 0])
ys = range(len(order))
ax.barh(ys, [float(r["Schedule variance (days)"]) for r in order], color=[col[r["calc"]] for r in order], height=0.62)
for y, r in zip(ys, order):
    v = float(r["Schedule variance (days)"])
    ax.text(v - 0.6 if v < 0 else v + 0.6, y, f"{v:g}  {r['calc']}", va="center", ha="right" if v < 0 else "left", fontsize=8.5, color=INK2)
ax.set_yticks(list(ys)); ax.set_yticklabels([f"{r['Project ID']} · {r['Practice']}" for r in order], fontsize=8.5)
ax.axvline(0, color=INK2, lw=1); ax.set_xlim(-26, 8); ax.grid(axis="y", visible=False)
ax.set_title("Schedule variance (days) · bar colour = overall RAG", loc="left", fontsize=11)
ax2 = fig.add_subplot(gs[1, 1])
order2 = sorted(rows, key=lambda r: r["ci"])
ax2.barh(range(len(order2)), [r["ci"] for r in order2], color=S1, height=0.62)
for y, r in enumerate(order2):
    ax2.text(r["ci"] + 0.01, y, f"{r['ci']:.2f}", va="center", fontsize=8.5, color=INK2)
ax2.axvline(0.95, color=INK2, lw=1.2, ls=(0, (4, 3))); ax2.text(0.952, len(order2) - 0.4, "Green ≥ 0.95", fontsize=8.5, color=INK2)
ax2.axvline(0.85, color=INK2, lw=1.2, ls=(0, (1, 2))); ax2.text(0.852, -0.9, "Red < 0.85", fontsize=8.5, color=INK2)
ax2.set_yticks(range(len(order2))); ax2.set_yticklabels([r["Project ID"] for r in order2], fontsize=8.5)
ax2.set_xlim(0.6, 1.15); ax2.set_ylim(-1.3, len(order2) - 0.1); ax2.grid(axis="y", visible=False)
ax2.set_title("Cost index (value earned per $1 spent)", loc="left", fontsize=11)
fig.suptitle("Meridian Advisory – Portfolio overview (simulated data)", x=0.01, ha="left", fontsize=14, fontweight="bold")
fig.savefig(os.path.join(here, "portfolio-dashboard.png"), dpi=160, bbox_inches="tight", facecolor=SURF)
print("saved portfolio-dashboard.png")
