"""R128: from-scratch checks of O128 Prop 2.1/Lemma 2.2 (separation), Prop 2.4/2.5 (incidence),
and non-primitive shell points.  Usage: uv run --with sympy python scripts/review_t2s_geom.py P"""
import sys, math
from collections import defaultdict
from sympy import primerange

def quads(p):  # (a,b,c,d) with 4abcd = a+b+pc, gcd(a,c)=1 ; plus non-primitive ones flagged
    out = []
    for a in range(1, p + 1):
        if 3 * a - 1 > p: break
        for b in range(1, p + 1):
            if 4 * a * b - a - b > p: break
            s = a + b
            for c in range(1, s + 1):
                if s % c: continue
                num = s + p * c
                if num % (4 * a * b * c): continue
                out.append((a, b, c, num // (4 * a * b * c)))
    return out

def cosh_dist(z, w):
    return 1 + abs(z - w) ** 2 / (2 * z.imag * w.imag)

P = int(sys.argv[1]) if len(sys.argv) > 1 else 400
worst_sep, worst_detp, worst_inc, nonprim, npts = 9e9, 9e9, 0.0, 0, 0
ratio_detp = 9e9
for p in primerange(5, P):
    Q = quads(p)
    byd = defaultdict(list); byd_detp = defaultdict(list)
    for (a, b, c, d) in Q:
        g = math.gcd(a, c)
        f, fp = 4 * a * c * d - 1, 4 * b * c * d - 1
        assert f * fp - 4 * c * c * d * p == 1
        D = d * p
        # level-dp form [f, 4cdp, dp f'] : disc and root
        A, B, C = f, 4 * c * D, D * fp
        assert B * B - 4 * A * C == -4 * D
        z = complex(-B, math.sqrt(4 * D)) / (2 * A)
        # det-p form [f, 4ad, d e]
        e = (a + b) // c
        A1, B1, C1 = f, 4 * a * d, d * e
        assert B1 * B1 - 4 * A1 * C1 == -4 * D and A1 % B1 == B1 - 1
        z1 = complex(-B1, math.sqrt(4 * D)) / (2 * A1)
        # Prop 2.5: <u,v>_Q = A - cB = -1 ; sinh dist(z1, Re=-1/2c) = 1/(c sqrt|D|), left side
        sh = (z1.real + 1 / (2 * c)) / z1.imag
        worst_inc = max(worst_inc, abs(sh + 1 / (c * math.sqrt(4 * D))) * c * math.sqrt(4 * D))
        # Prop 2.4: w = z/D on ray X = -(1+Y sqrt(dp))/(2ad)
        w = z / D
        worst_inc = max(worst_inc, abs(w.real + (1 + w.imag * math.sqrt(D)) / (2 * a * d)) * f)
        if g == 1:
            npts += 1
            byd[d].append(z); byd_detp[d].append(z1)
    # non-primitive shell points: forms satisfying all shell conditions with gcd(a,c)>1
    for a in range(1, p + 1):
        for c in range(1, p + 1):
            if math.gcd(a, c) == 1: continue
            for d in range(1, p + 1):
                f = 4 * a * c * d - 1
                if f > p + 4 * a * a * d: break
                if (p + 4 * a * a * d) % f == 0: nonprim += 1
            if 4 * a * c - 1 > p + 4 * a * a: break
    for d, L in byd.items():
        for i in range(len(L)):
            for j in range(i):
                worst_sep = min(worst_sep, cosh_dist(L[i], L[j]))
    for d, L in byd_detp.items():
        for i in range(len(L)):
            for j in range(i):
                ratio_detp = min(ratio_detp, (cosh_dist(L[i], L[j]) - 1) * 2 * p)
print(f"primes<{P}: primitive Type II points {npts}; min cosh (level dp, same d) = {worst_sep:.6f} (claim >=1.5)")
print(f"min (cosh-1)*2p in det-p coords = {ratio_detp:.6f} (claim >=1)")
print(f"max relative incidence error = {worst_inc:.2e}; non-primitive shell points (gcd(a,c)>1) = {nonprim}")
