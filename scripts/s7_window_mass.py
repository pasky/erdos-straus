"""s7_window_mass: r-adic mass of cap-0 window (Type II) balls on the r-generic line.
On the r-generic line (p ≡ 1 at every prime ≠ r) K_m = (p+m)/4 ≡ 1/4 (mod m) and v_l(K_m) = v_l((1+m)/4) for l ≠ r.
Window m ≡ 3 (4), r ∤ m, fires at cap 0 iff some d = delta * r^c, delta | K0^2 (K0 = r-free part of (1+m)/4),
0 <= c <= 2 v_r(p+m), has d ≡ -1/4 (mod m). Equivalently r^(c - v) ∈ -R_m, v = v_r(1+m), R_m = ratios of divisors
of K0. With c_m the least such c (c = 0 is impossible: it would cover the square point p = 1, T1), window m covers
exactly the ball v_r(p + m) >= b_m := ceil(c_m / 2) (cell -m mod r must be a non-residue). Type I e-slices give the
mirror balls v_r(p + 1/e) >= b_e with the same b. Prints the Type II mass sum_m r^(-b_m), split by b and by c parity.
Usage: python s7_window_mass.py r M CMAX
"""
import sys, math, collections

def spf_sieve(L):
    spf = list(range(L + 1))
    for i in range(2, int(L ** 0.5) + 1):
        if spf[i] == i:
            for j in range(i * i, L + 1, i):
                if spf[j] == j: spf[j] = i
    return spf

r, M, BMAX = map(int, sys.argv[1:4])  # BMAX = CMAX
spf = spf_sieve(M // 4 + 2)
nonres = {c for c in range(1, r) if pow(c, (r - 1) // 2, r) == r - 1}
BALLS = []
par = collections.Counter(); mass = collections.Counter(); cnt = collections.Counter(); ex = collections.defaultdict(list); t1viol = 0
for m in range(3, M + 1, 4):
    if m % r == 0 or ((-m) % r) not in nonres:
        continue
    K0 = (1 + m) // 4
    while K0 % r == 0: K0 //= r
    R = {1}
    k = K0
    while k > 1:
        l = spf[k]; v = 0
        while k % l == 0: k //= l; v += 1
        g = l % m
        if math.gcd(g, m) != 1: continue
        gi = pow(g, -1, m); pw = {1}
        for j in range(1, v + 1): pw.add(pow(g, j, m)); pw.add(pow(gi, j, m))
        R = {x * y % m for x in R for y in pw}
    targets = {(m - 1) * pow(x, -1, m) % m for x in R}   # need r^(c - v) in targets
    vv = 0; t = 1 + m
    while t % r == 0: t //= r; vv += 1
    rr = r % m; base = pow(rr, (-vv) % (10**9) if False else 1, m)
    cm = None; cur = pow(pow(rr, -1, m), vv, m)  # r^(0 - v)
    for c in range(0, BMAX + 1):
        if cur in targets: cm = c; break
        cur = cur * rr % m
    if cm is None: continue
    if cm == 0: t1viol += 1; continue
    bm = (cm + 1) // 2
    par[cm % 2] += 1
    BALLS.append((m, bm))
    mass[bm] += r ** (-bm); cnt[bm] += 1
    if len(ex[bm]) < 4: ex[bm].append(m)
tot = sum(mass.values())
print("r", r, "M", M, "BMAX", BMAX, "T1 violations (must be 0):", t1viol)
print("total window mass %.6f (non-residue cells carry %.3f)" % (tot, (r - 1) / (2 * r)))
print("parity of c_m (odd, even):", par[1], par[0])
for bm in sorted(cnt): print("  b=%d windows %d mass %.6f e.g. %s" % (bm, cnt[bm], mass[bm], ex[bm]))
# --- union of U (centre -m) and U^{-1} (centre -1/m) balls, exact ultrametric union (balls nested or disjoint)
B = max(BALLS, key=lambda t: t[1])[1] if BALLS else 1
allb = set()
for m, b in BALLS:
    mod = r ** b
    allb.add((b, (-m) % mod)); allb.add((b, (-pow(m, -1, mod)) % mod))
allb = sorted(allb)
kept = []; keptset = set()
for b, c in allb:   # shallow first; keep if no ancestor kept
    if any((bb, c % r ** bb) in keptset for bb in range(1, b)):
        continue
    kept.append((b, c)); keptset.add((b, c))
u = sum(r ** (-b) for b, c in kept)
print("U ∪ U^-1 union mass %.6f in %d maximal balls; residual non-residue mass %.6f" % (u, len(kept), (r - 1) / (2 * r) - u))
