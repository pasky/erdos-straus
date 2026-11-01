"""Summarise data/z53/genuslval/slice_checks.txt (Prop C closed form vs exact slice) by X_u range."""
import re, os
ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
rows = []
for l in open(os.path.join(ROOT, 'data/z53/genuslval/slice_checks.txt')):
    m = re.match(r"p=(\d+) u=(\d+) X=(\d+) S_u direct=([\d.]+) .*closed-form=([\d.]+) err=([-+\d.e]+)", l)
    if m:
        p, u, X = map(int, m.group(1, 2, 3)); d, c, e = map(float, m.group(4, 5, 6))
        rows.append((p, u, X, d, c, e))
out = []
for lo, hi in [(1, 10**2), (10**2, 10**3), (10**3, 10**4), (10**4, 10**5), (10**5, 10**8)]:
    sel = [r for r in rows if lo <= r[2] < hi]
    if not sel: continue
    mx = max(sel, key=lambda r: abs(r[5]))
    rel = max(abs(r[5]) / max(r[3], 1e-9) for r in sel if r[3] > 0)
    out.append(f"X_u in [{lo:.0e},{hi:.0e}): n={len(sel)}  max|err|={abs(mx[5]):.2e} (p={mx[0]},u={mx[1]})  max rel={rel:.3f}")
txt = "\n".join(out); print(txt)
open(os.path.join(ROOT, 'data/z53/genuslval/slice_summary.txt'), 'w').write(txt + "\n")
