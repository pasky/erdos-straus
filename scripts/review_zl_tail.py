"""review_zl_tail.py -- R231: independent check of STERILE_LOWER Lemma 1.2 (value-selected tail routes).
Uses SE's REVIEWED route term lists (scripts/se_tail.py, unchanged from main; reviewed by R222/R223), NOT zl_tail.py.
Intercepts se_tail's per-box route choice (min over the dict R of routes), re-selects by
  admissible (every term e < h, p <= (h-e) ln N0)  and least value at N0  (own code),
and recomputes G = sum c N0^{e-h} (ln N0)^p in 50-digit mpmath. Reports route usage old vs new selection.
Usage: review_zl_tail.py P|Q M L0bits"""
import os, sys, builtins
os.environ.setdefault("SE_W", "40")
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import se_tail
from mpmath import mp, mpf, exp, log
mp.dps = 50
from collections import Counter
mode, M, L0bits = sys.argv[1], int(sys.argv[2]), float(sys.argv[3])
h = mpf(1) / 2 if mode == "P" else mpf(1)
L0 = mpf(L0bits) * log(2)
def value(T): return sum(mpf(c) * exp(mpf(e) * L0) * L0 ** p for (c, e, p) in T)
def adm(T): return all(mpf(e) < h - mpf(10) ** -6 and p <= (h - mpf(e)) * L0 for (c, e, p) in T)
old, new, boxes, olds = Counter(), Counter(), [], []
_min = builtins.min
def mymin(*args, key=None):
    if len(args) == 1 and isinstance(args[0], dict):
        R = args[0]
        try: k_old = _min(R, key=lambda k: (max(e for (c, e, p) in R[k]), value(R[k])))
        except OverflowError: k_old = None
        old[k_old] += 1; olds.append(R[k_old] if k_old else None)
        ok = [k for k in R if adm(R[k])]
        k = _min(ok, key=lambda k: value(R[k])) if ok else k_old
        new[k] += 1; boxes.append((k, R[k], ok != []))
        return k
    return _min(*args, key=key) if key else _min(*args)
se_tail.min = mymin
terms, worst_old, nbox, _ = (se_tail.tailP if mode == "P" else se_tail.tailQ)(M, L0bits)
noadm = sum(1 for b in boxes if not b[2])
allterms = [t for b in boxes for t in b[1]]
G = sum(mpf(c) * exp((mpf(e) - h) * L0) * L0 ** p for (c, e, p) in allterms)
Gold = sum(mpf(c) * exp((mpf(e) - h) * L0) * L0 ** p for T in olds for (c, e, p) in T) if all(olds) else None
print(f"mode {mode} M {M} L0 {L0bits}: boxes {nbox}, boxes w/o admissible route {noadm}")
print(f"  new selection: G = {mp.nstr(G, 8)}, max exponent {max(e for (c, e, p) in allterms):.6f}, all admissible {all(adm(b[1]) for b in boxes)}")
print(f"  SE selection : G = {mp.nstr(Gold, 8) if Gold is not None else 'n/a'}, max exp {max(e for T in olds if T for (c,e,p) in T):.6f}")
print("  routes SE  :", dict(old)); print("  routes new :", dict(new))
if os.environ.get("DUMP"):
    import json
    sel = os.environ.get("SEL", "new")
    out = [t for b in boxes for t in b[1]] if sel == "new" else [t for T in olds for t in T]
    if sel != "new": assert all(adm(T) for T in olds), "SE selection not admissible"
    json.dump(out, open(os.environ["DUMP"], "w"))
    print("dumped", len(out), "terms (", sel, ") to", os.environ["DUMP"])
