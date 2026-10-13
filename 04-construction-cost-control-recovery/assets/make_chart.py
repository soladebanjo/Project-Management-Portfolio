"""Builds assets/evm-s-curve.png from evm-data.csv (simulated data). Run from the project folder: python assets/make_chart.py"""
import csv, os, sys
sys.path.insert(0, os.path.dirname(__file__))
from style import *
setup()
here = os.path.dirname(os.path.abspath(__file__))
rows = list(csv.DictReader(open(os.path.join(here, "..", "evm-data.csv"), encoding="utf-8")))
w = [int(r["Week"]) for r in rows]
f = lambda k: [float(r[k]) if r[k] else None for r in rows]
pv, ev, ac = f("Planned Value PV ($M)"), f("Earned Value EV ($M)"), f("Actual Cost AC ($M)")
fig, ax = plt.subplots(figsize=(10, 5.6))
ax.plot(w, pv, color=S1, lw=2, label="Planned Value (PV)")
we = [x for x, y in zip(w, ev) if y is not None]
ax.plot(we, [y for y in ev if y is not None], color=S3, lw=2, label="Earned Value (EV)")
ax.plot(we, [y for y in ac if y is not None], color=S2, lw=2, label="Actual Cost (AC)")
last = we[-1]
for series, col, dy in [(pv, S1, 10), (ev, S3, -16), (ac, S2, 4)]:
    y = series[w.index(last)]
    ax.plot([last], [y], "o", color=col, ms=7, markeredgecolor=SURF, markeredgewidth=1.5)
ax.axvline(last, color=INK2, lw=1, ls=(0, (4, 3)))
ax.text(last + 0.6, 1.0, f"Status date: Week {last}\nPV \\${pv[w.index(last)]:.1f}M · EV \\${ev[w.index(last)]:.1f}M · AC \\${ac[w.index(last)]:.1f}M\nCPI 0.97 · SPI 0.96", color=INK2, fontsize=9.5, va="bottom")
ax.text(w[-1], pv[-1] + 0.5, "BAC $22.8M", ha="right", color=INK2, fontsize=9.5)
ax.set_xlabel("Project week"); ax.set_ylabel("Cumulative cost of remaining scope ($M)")
ax.set_xlim(0, 52); ax.set_ylim(0, 25)
ax.legend(loc="upper left", frameon=False)
ax.set_title("Construction Cost Control Recovery – earned value S-curve (simulated data)", loc="left", fontsize=13, fontweight="bold")
fig.tight_layout()
fig.savefig(os.path.join(here, "evm-s-curve.png"), dpi=160)
print("saved evm-s-curve.png")
