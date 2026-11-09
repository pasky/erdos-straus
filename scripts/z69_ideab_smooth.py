#!/usr/bin/env python3
"""z69 IDEAB Phase 3.5: question (Q-S). S = {2,3,5,7,11}.
Enumerate ALL family classes (seven ET families, superset enumeration) whose modulus is S-smooth and <= M, keep those
compatible with the box B_r = (1+8Z_2)x(1+3Z_3)x(1+5Z_5)x(1+7Z_7)x(r+11Z_11), and decide by complete DFS on the digits
whether they cover B_r.  Output: a surviving S-point (residues mod prime powers) or "COVERED".
usage: smooth.py M r [nodelimit] [seed] [--exact] [--extra q:v ...]
--extra q:v adds the prime q to S with the coordinate at q restricted to the residue class v mod q (box B_r x (v + q Z_q))."""
import sys, math, random, json
from sympy import factorint, divisors, sqrt_mod
sys.setrecursionlimit(100000)
M = int(float(sys.argv[1])); R11 = int(sys.argv[2]); NODELIM = int(float(sys.argv[3])) if len(sys.argv) > 3 else 10**7
random.seed(int(sys.argv[4]) if len(sys.argv) > 4 else 1)
S = [2, 3, 5, 7, 11]; BASE = {2: 3, 3: 1, 5: 1, 7: 1, 11: 1}; BASEVAL = {2: 1, 3: 1, 5: 1, 7: 1, 11: R11}
EXTRA = []
if "--extra" in sys.argv:
    for tok in sys.argv[sys.argv.index("--extra") + 1:]:
        if tok.startswith("--"): break
        q, v = map(int, tok.split(":")); S.append(q); BASE[q] = 1; BASEVAL[q] = v; EXTRA.append((q, v))
TAG = "".join(f"_x{q}-{v}" for q, v in EXTRA)

def smooth_upto(X):
    out = [1]
    for q in S:
        new = []
        for m in out:
            t = m
            while t <= X: new.append(t); t *= q
        out = new
    return sorted(out)
SM = smooth_upto(M); SMSET = set(SM)
def sdivs(m): return [d for d in divisors(m)]            # m smooth => all divisors smooth
cls = {}
def add(m, rho): cls.setdefault(m, set()).add(rho % m)
for m in SM:
    if m % 4 == 0:
        q4 = m // 4
        for a in sdivs(q4):
            b = q4 // a
            if a <= b:                                                   # II-1, I-4
                for e in divisors(a + b):
                    if math.gcd(e, m) == 1: add(m, -e); add(m, -pow(e, -1, m))
            d = b                                                        # I-1 with (a, d) = (a, q4/a)
            for f in divisors(4 * a * a * d + 1): add(m, -f)
        odd = q4
        while odd % 2 == 0: odd //= 2
        fo = factorint(odd)
        ps = list(fo)
        for mask in range(1, 1 << len(ps)):                              # f = full prime-power components
            f = 1
            for i, q in enumerate(ps):
                if mask >> i & 1: f *= q ** fo[q]
            if f % 4 != 3: continue
            uv = q4 // f; m4 = 4 * uv; inv = pow(m4, -1, f); r4 = (-f) % m4
            crt = lambda rf: (r4 + m4 * ((rf - r4) * inv % f)) % m
            for u in sdivs(uv):
                v = uv // u
                add(m, crt((-v * pow(u, -1, f)) % f))                    # I-2 (a,c) = (u,v)
                add(m, crt((-4 * u * u * v) % f))                        # II-3 (a,d) = (u,v), e = f
                rts = sqrt_mod((-4 * u * u * v) % f, f, all_roots=True) or []
                for x in rts: add(m, crt(x))                             # I-3 (c,d) = (u,v)
    if m % 4 == 3:                                                       # II-2
        k = (m + 1) // 4
        for a in divisors(k):
            for d in divisors(k // a): add(m, -4 * a * a * d)
ntot = sum(len(v) for v in cls.values())

def expo(m):
    e = {}
    for q in S:
        c = 0
        while m % q == 0: m //= q; c += 1
        e[q] = c
    return e
comp = []; weight = 0.0; bad_T1 = 0; full = []
for m, Rs in cls.items():
    e = expo(m)
    for rho in Rs:
        if any(rho % (q ** min(e[q], BASE[q])) != BASEVAL[q] % (q ** min(e[q], BASE[q])) for q in S): continue
        if e[11] == 0:
            bad_T1 += 1
            if not EXTRA: continue
        c = tuple((e[q], rho % (q ** e[q])) for q in S)
        w = 1.0
        for q in S: w /= q ** max(0, e[q] - BASE[q])
        weight += w; comp.append(c)
        if w == 1.0: full.append((m, rho))
comp = list(set(comp))
assert bad_T1 == 0 or EXTRA, 'a compatible class with 11 not dividing its modulus exists: T1 sanity failed'
print(f"M={M:.3g} r={R11} extra={EXTRA}: {len(SM)} smooth moduli, {ntot} classes, {len(comp)} compatible with B_r, total relative weight {weight:.3f}; "
      f"compatible classes with 11 not dividing modulus (must be 0 by T1 when no non-residue --extra coordinate is used): {bad_T1}; classes covering all of B_r: {full}", flush=True)

# Monte Carlo estimate of the uncovered relative measure of B_r at this level
maxe = {q: max([c[i][0] for c in comp] + [BASE[q]]) for i, q in enumerate(S)}
NMC = 200000; unc = 0
import collections
by11 = collections.defaultdict(list)
for c in comp: by11[c[4]].append(c)
OTH = [i for i in range(len(S)) if i != 4]
for _ in range(NMC):
    x = {q: BASEVAL[q] % (q ** BASE[q]) + (q ** BASE[q]) * random.randrange(q ** (maxe[q] - BASE[q])) for q in S}
    hitp = False
    for (e11, r11), L in by11.items():
        if x[11] % (11 ** e11) != r11: continue
        for c in L:
            if all(x[S[i]] % (S[i] ** c[i][0]) == c[i][1] for i in OTH): hitp = True; break
        if hitp: break
    unc += not hitp
print(f"   Monte Carlo ({NMC} random points of B_r): uncovered fraction = {unc / NMC:.4f}", flush=True)
nodes = 0; found = None
def dfs(D, X, active):
    """D[q] depth, X[q] residue mod q^D[q]; active = classes consistent so far and not yet dodged."""
    global nodes, found
    nodes += 1
    if nodes > NODELIM: raise TimeoutError
    best = None; bestrem = 10**9
    for c in active:
        rem = 0; first = None
        for i, q in enumerate(S):
            if c[i][0] > D[q]:
                rem += c[i][0] - D[q]
                if first is None: first = q
        if rem == 0: return False                      # this cylinder lies inside a class: covered
        if rem < bestrem: bestrem = rem; best = first
    if best is None:
        found = (dict(D), dict(X)); return True         # no active class: every extension is uncovered
    q = best; i = S.index(q); pw = q ** D[q]
    digs = list(range(q)); random.shuffle(digs)
    for dg in digs:
        nx = X[q] + dg * pw
        na = [c for c in active if c[i][0] <= D[q] or (c[i][1] // pw) % q == dg]
        D[q] += 1; old = X[q]; X[q] = nx
        r = dfs(D, X, na)
        D[q] -= 1; X[q] = old
        if r: return True
    return False

from fractions import Fraction
vnodes = 0
def volume(D, active, vol):
    """exact relative measure of the part of the current cylinder (relative volume vol) not covered by `active`."""
    global vnodes
    vnodes += 1
    if vnodes > NODELIM: raise TimeoutError
    best = None; bestrem = 10**9
    for c in active:
        rem = 0; first = None
        for i, q in enumerate(S):
            if c[i][0] > D[q]:
                rem += c[i][0] - D[q]
                if first is None: first = q
        if rem == 0: return Fraction(0)
        if rem < bestrem: bestrem = rem; best = first
    if best is None: return vol
    q = best; i = S.index(q); pw = q ** D[q]
    groups = {}
    rest = []
    for c in active:
        if c[i][0] <= D[q]: rest.append(c)
        else: groups.setdefault((c[i][1] // pw) % q, []).append(c)
    tot = Fraction(0)
    D[q] += 1
    free_digits = q - len(groups)
    if free_digits: tot += free_digits * volume(D, rest, vol / q)     # digits no class asks for: identical subtrees
    for dg, L in groups.items(): tot += volume(D, rest + L, vol / q)
    D[q] -= 1
    return tot
if "--exact" in sys.argv:
    try:
        u = volume(dict(BASE), comp, Fraction(1))
        print(f"   EXACT uncovered relative measure of B_r at level {M:.0e}: {u} = {float(u):.6f}  ({vnodes} nodes)", flush=True)
    except TimeoutError:
        print(f"   exact measure: node limit reached ({NODELIM})", flush=True)
D0 = dict(BASE); X0 = {q: BASEVAL[q] % (q ** BASE[q]) for q in S}
try:
    res = dfs(D0, X0, comp)
    if res:
        Dq, Xq = found
        print(f"SURVIVOR after {nodes} nodes: depths {Dq}  residues {Xq}", flush=True)
        # independent re-check of the survivor against every compatible class and against the raw table
        # re-check against the RAW class table (every smooth-modulus class, not the filtered list): a class (m, rho) meets
        # the survivor cylinder iff rho = X_q mod q^min(e_q, D_q) for all q in S
        hit = 0
        for m, Rs in cls.items():
            e = expo(m)
            for rho in Rs:
                if all(Xq[q] % (q ** min(e[q], Dq[q])) == rho % (q ** min(e[q], Dq[q])) for q in S): hit += 1
        print(f"   raw-table re-check: classes (of all {ntot}) meeting the survivor cylinder: {hit}", flush=True)
        assert hit == 0
        json.dump({"M": M, "r": R11, "depths": Dq, "residues": {str(q): Xq[q] for q in S}, "nodes": nodes, "ncompatible": len(comp), "weight": weight},
                  open(f"data/z69/ideab/smooth_M{M:.0e}_r{R11}{TAG}.json", "w"))
    else:
        print(f"COVERED: exhaustive DFS ({nodes} nodes) found no S-point of B_r outside the S-smooth classes of modulus <= {M}", flush=True)
        json.dump({"M": M, "r": R11, "covered": True, "nodes": nodes, "ncompatible": len(comp), "weight": weight}, open(f"data/z69/ideab/smooth_M{M:.0e}_r{R11}{TAG}.json", "w"))
except TimeoutError:
    print(f"UNDECIDED: node limit {NODELIM} reached", flush=True)
