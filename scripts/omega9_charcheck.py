"""OMEGA9 Thm 1.1 sanity check (toy; illustrates, proves nothing).

Free coordinates: units mod l for l in PR; Q = 3.  F = indicator that no
random single-value event (on <=2 coordinates) occurs.  B = inclusion-
exclusion expansion of F over all event subsets (an exact signed cell
combination with large M_1).  We check:
 (1) c(chi_Q chi_D) = E_D[B conj(chi_D)]/phi(Q) for every character, by brute
     force over (Z/QD)^*, and max|c| <= E|B|/phi(Q);
 (2) the prime sum S(x) = sum_{p<=x, p=1 (Q), p!|D} B(p) log p against
     mu*x/phi(Q): its relative error versus the PO-Thm-4.1-style bookkeeping
     bound M_1 * max_i |eps_i| (per-progression errors).
Usage: omega9_charcheck.py [seed] [xmax]
"""
import sys, itertools, math, random
import numpy as np
from sympy import primerange, primitive_root

seed = int(sys.argv[1]) if len(sys.argv) > 1 else 1
XMAX = int(float(sys.argv[2])) if len(sys.argv) > 2 else 3 * 10**6
rng = random.Random(seed)
PR = [7, 11, 13, 17]
Q = 3
D = math.prod(PR)
out = []

# events: (coords tuple, values tuple) residues mod l, nonzero
events = []
for _ in range(9):
    r = rng.choice([1, 2])
    cs = tuple(sorted(rng.sample(range(len(PR)), r)))
    vs = tuple(rng.randrange(1, PR[c]) for c in cs)
    events.append((cs, vs))

# cells of inclusion-exclusion: for each subset of events, consistent
# assignment -> cell (dict coord->value), coefficient (-1)^|J|
cells = {}
for r in range(len(events) + 1):
    for J in itertools.combinations(range(len(events)), r):
        asg = {}
        ok = True
        for j in J:
            for c, v in zip(*events[j]):
                if asg.get(c, v) != v:
                    ok = False
                asg[c] = v
        if ok:
            key = tuple(sorted(asg.items()))
            cells[key] = cells.get(key, 0) + (-1) ** r
cells = {k: v for k, v in cells.items() if v != 0}
phi = lambda key: math.prod(PR[c] - 1 for c, _ in key)
mu = sum(v / phi(k) for k, v in cells.items())
M1 = sum(abs(v) / phi(k) for k, v in cells.items())


def Bval(n):
    return sum(v for k, v in cells.items() if all(n % PR[c] == a for c, a in k))


# all units mod D as residue vectors
units = [n for n in range(1, D) if math.gcd(n, D) == 1]
Bv = np.array([Bval(n) for n in units], dtype=float)
EabsB = np.abs(Bv).mean()
out.append(f"seed={seed} events={len(events)} cells={len(cells)} mu={mu:.6f} "
           f"E|B|/mu={EabsB/mu:.4f} M1/mu={M1/mu:.3f}")
assert abs(Bv.mean() - mu) < 1e-9

# characters mod D: product of characters mod each prime via discrete logs
logs = []
for l in PR:
    g = primitive_root(l)
    dl = {pow(g, e, l): e for e in range(l - 1)}
    logs.append(np.array([dl[n % l] for n in units]))
# characters mod Q=3: trivial and the real one; c(chi) via brute force over (Z/QD)^*
maxdev, maxc = 0.0, 0.0
idx = {n: i for i, n in enumerate(units)}
QDunits = [n for n in range(1, Q * D) if math.gcd(n, Q * D) == 1]
f = np.array([Bv[idx[n % D]] if n % Q == 1 else 0.0 for n in QDunits])
logsQD = [np.array([lg[idx[n % D]] for n in QDunits]) for lg in logs]
chiQ = [np.ones(len(QDunits)), np.array([1.0 if n % 3 == 1 else -1.0 for n in QDunits])]
count = 0
for exps in itertools.product(*[range(l - 1) for l in PR]):
    ph = sum(2j * math.pi * e * lg / (l - 1) for e, lg, l in zip(exps, logsQD, PR))
    chiD_QD = np.exp(ph)
    phD = sum(2j * math.pi * e * lg / (l - 1) for e, lg, l in zip(exps, logs, PR))
    pred = (Bv * np.exp(-phD)).mean() / 2  # E_D[B conj chi_D]/phi(Q)
    for cq in chiQ:
        c = (f * np.conj(cq * chiD_QD)).sum() / len(QDunits)
        maxdev = max(maxdev, abs(c - pred))
        maxc = max(maxc, abs(c))
        count += 1
out.append(f"(1) characters={count} max|c - E_D[B conj chi_D]/phi(Q)|={maxdev:.2e} "
           f"max|c|*phi(Q)/E|B|={maxc*2/EabsB:.4f} (<=1 required)")
assert maxdev < 1e-9 and maxc * 2 <= EabsB + 1e-12

# (2) prime sums
ps = np.array(list(primerange(D + 1, XMAX)), dtype=np.int64)
ps = ps[ps % Q == 1]
lp = np.log(ps.astype(float))
for x in [XMAX // 30, XMAX // 3, XMAX]:
    sel = ps <= x
    pp, ll = ps[sel], lp[sel]
    res = np.array([idx[int(p % D)] for p in pp])
    S = float((Bv[res] * ll).sum())
    main = mu * x / 2
    # per-progression relative errors eps_i
    maxeps = 0.0
    for k, v in cells.items():
        mask = np.ones(len(pp), bool)
        for c, a in k:
            mask &= (pp % PR[c]) == a
        th = float(ll[mask].sum())
        expct = x / 2 / phi(k)
        maxeps = max(maxeps, abs(th / expct - 1))
    out.append(f"(2) x={x:.2e} S/main-1={S/main-1:+.4f}  PO-style bound M1/mu*max eps="
               f"{M1/mu*maxeps:.3f}  (E|B|/mu)*max eps={EabsB/mu*maxeps:.4f}")
print("\n".join(out))
