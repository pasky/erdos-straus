# z55 CROSSU: pair statistics of the firing set against a MATCHED null.
# For each n: hits H = {(u,d): j = 1}; genus points Gp = {(u,d): j in squares}. Null: sample |H| points from Gp with
# probability proportional to the genus weight 1/|square class| = 2^{omega(u)}/phi(u) (exactly the G-prediction of a
# hit), repeated REP times. Statistics over unordered pairs with u1 != u2: gcd(u1,u2) > 1, gcd(d1,d2) > 1,
# |u1-u2| <= U1/20, u1 | u2 or u2 | u1. Usage: python scripts/z55_crossu_pairs.py DUMPDIR [REP]
import sys, os, math, itertools, random
D = sys.argv[1]; REP = int(sys.argv[2]) if len(sys.argv) > 2 else 20
random.seed(1)
def omega_phi(u):
    k = 0; ph = 1; t = u; q = 3
    while q * q <= t:
        if t % q == 0: k += 1; ph *= q - 1; t //= q
        q += 2
    if t > 1: k += 1; ph *= t - 1
    return k, ph
stats = {k: {'n': 0, 'gu': 0, 'gd': 0, 'near': 0, 'div': 0} for k in ['HH', 'NN']}
def add(k, pairs, U1, scale=1.0):
    st = stats[k]
    for (u1, d1), (u2, d2) in pairs:
        if u1 == u2: continue
        st['n'] += scale
        st['gu'] += scale * (math.gcd(u1, u2) > 1); st['gd'] += scale * (math.gcd(d1, d2) > 1)
        st['near'] += scale * (abs(u1 - u2) <= U1 / 20); st['div'] += scale * (u1 % u2 == 0 or u2 % u1 == 0)
nn = 0; nh = 0; sumu_H = 0; sumu_N = 0
for fn in sorted(os.listdir(D)):
    pts = [tuple(map(int, l.split())) for l in open(os.path.join(D, fn))]
    if not pts: continue
    nn += 1
    U1 = max(u for u, w, d, j, s in pts)
    H = [(u, d) for u, w, d, j, s in pts if j == 1]
    Gp = [(u, d) for u, w, d, j, s in pts if s == 1]
    nh += len(H); sumu_H += sum(u for u, d in H)
    wts = []
    for u, d in Gp:
        k, ph = omega_phi(u); wts.append((1 << k) / ph)
    add('HH', itertools.combinations(H, 2), U1)
    if len(H) >= 2 and Gp:
        for r in range(REP):
            N = random.choices(Gp, weights=wts, k=len(H))
            sumu_N += sum(u for u, d in N) / REP
            add('NN', itertools.combinations(N, 2), U1, 1.0 / REP)
print(f"files={nn} hits={nh} mean_u(hits)={sumu_H/max(nh,1):.1f} mean_u(null)={sumu_N/max(nh,1):.1f}")
for k, st in stats.items():
    n = st['n'] or 1
    print(f"{k}: pairs={st['n']:.0f} gcd(u)>1: {st['gu']/n:.4f}  gcd(d)>1: {st['gd']/n:.4f}  |u1-u2|<=U1/20: {st['near']/n:.4f}  u|u': {st['div']/n:.5f}")
