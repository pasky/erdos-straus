"""R232 round 2: cross-check of the author's value-selected P tail at N0 = 2^800 (STERILE_LOWER Lemma 1.2) using R223's
INDEPENDENT exact-exponent tail implementation (scripts/review_se2_tail.py, written for STERILE_EXPLICIT by R223, not by the
author), with two changes made here by source transformation (the R223 file itself is not modified):
  L0bits = 600 -> 800, and the per-box route rule "least (max exponent, value)" -> "least value at N0 among routes whose every
  term has e < 1/2 - 1e-6 and p <= (1/2 - e) ln N0" (fallback: R223's rule; the final admissibility check below fails closed).
Writes the aggregated term list to data/review_r232/r2/tail800_r223.pkl and prints G = bound(N0)/sqrt(N0)."""
import sys, os, math, pickle
from fractions import Fraction as Fr
HERE = os.path.dirname(os.path.abspath(__file__)); sys.path.insert(0, HERE)
src = open(os.path.join(HERE, 'review_se2_tail.py')).read()
assert src.count("L0bits = 600") == 1 and src.count("                k = min(R, key=lambda t: key(R[t]))") == 1
src = src.replace("L0bits = 600", "L0bits = 800")
src = src.replace("                k = min(R, key=lambda t: key(R[t]))",
"""                okr = [t for t in R if all(e < Fr(1, 2) - Fr(1, 10 ** 6) and p <= (Fr(1, 2) - e) * L0lo for (c, e, p) in R[t])]
                k = min(okr, key=lambda t: val(R[t], float(L0lo))) if okr else min(R, key=lambda t: key(R[t]))""")
src = src.split("if __name__ == '__main__':")[0]
g = {'__name__': 'r223_tail800'}
exec(compile(src, 'review_se2_tail.py[R232-transformed]', 'exec'), g)
M = int(sys.argv[1]) if len(sys.argv) > 1 else 32
terms, worst, nbox, used = g['tailP'](M)
L0lo, L0hi = g['L0lo'], g['L0hi']
ok = all(e >= 0 and p >= 0 and e < Fr(1, 2) and p <= (Fr(1, 2) - e) * L0lo for (c, e, p) in terms)
G = sum(float(c) * math.exp(float(e - Fr(1, 2)) * float(L0hi)) * float(L0hi) ** p for (c, e, p) in terms)
print(f"M={M} boxes {nbox} terms {len(terms)} max exponent {float(worst):.5f} admissible {ok} G(2^800) = {G:.6e} routes {used}")
if not ok: sys.exit(1)
pickle.dump([(c, e, p) for (c, e, p) in terms], open(os.path.join(os.path.dirname(HERE), 'data/review_r232/r2/tail800_r223.pkl'), 'wb'))
