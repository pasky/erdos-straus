# z2_split_cover.py (O225, NEAR_SQUARE_EXIST §5): CONJECTURE Y10-S "⊆" at a split prime, numerically.
# n = m^2 - j.  3-parameter Type I polynomial families of shape (deg a, deg c, deg d) = (1, 0, 1), Lambda = 1:
#   c = -alpha n(x) > 0, a = lam (m - x) + alpha, d = (m - x)/(4 c lam) - 1/(4 alpha^2),
#   f = 4acd - n = kappa (m - x), kappa = alpha/lam + lam n(x)/alpha - 2x > 0, b = (n a + c)/f, e = (4 a^2 d + 1)/f.
# For each family with all denominators dividing L, compute its integrality class C mod L and keep it if positive for
# all m >= 1 in C (checked on m in C below a bound, coordinates are eventually increasing).  Then report, among the
# classes m mod L lying in Z_K^+ at all primes of L except ell (and with n a unit at ell), which ell-adic residues are
# covered, versus the Z_K^+ prediction at ell (m - s, m + s both non-zero squares mod ell, s^2 = j).
import sys, itertools, random
from fractions import Fraction as Fr
from math import lcm, gcd

def pmul(p, q):
    r = [Fr(0)] * (len(p) + len(q) - 1)
    for i, x in enumerate(p):
        for k, y in enumerate(q): r[i + k] += x * y
    return r
def padd(p, q):
    n = max(len(p), len(q)); return [(p[i] if i < len(p) else 0) + (q[i] if i < len(q) else 0) for i in range(n)]
def pdiv_lin(p, x):              # exact division of p by (m - x); returns quotient, remainder
    p = list(p); q = [Fr(0)] * (len(p) - 1); rem = Fr(0)
    for i in range(len(p) - 1, 0, -1):
        q[i - 1] = p[i]; p[i - 1] += p[i] * x
    return q, p[0]
def ev(p, m): return sum(c * m ** i for i, c in enumerate(p))

def family(j, x, alpha, lam):
    nx = x * x - j
    c = -alpha * nx
    if c <= 0: return None
    kappa = alpha / lam + lam * nx / alpha - 2 * x
    if kappa <= 0: return None
    a = [alpha - lam * x, lam]
    d = [-x / (4 * c * lam) - Fr(1, 4) / alpha ** 2, 1 / (4 * c * lam)]
    n = [Fr(-j), Fr(0), Fr(1)]
    na_c = padd(pmul(n, a), [c])
    q1, r1 = pdiv_lin(na_c, x)
    e_num = padd(pmul(pmul(a, a), [4 * t for t in d]), [Fr(1)])
    q2, r2 = pdiv_lin(e_num, x)
    if r1 != 0 or r2 != 0: return None          # should not happen (identity)
    b = [t / kappa for t in q1]; e = [t / kappa for t in q2]
    f = [-kappa * x, kappa]
    return dict(a=a, b=b, c=[c], d=d, e=e, f=f)

def den(fam): return lcm(*[t.denominator for p in fam.values() for t in p])

def check_identities(fam, j, m):
    a, b, c, d, e, f = (ev(fam[k], m) for k in 'abcdef'); n = m * m - j
    return 4 * a * b * d == n * e + 1 and c * e == a + b and 4 * a * c * d == n + f and e * f == 4 * a * a * d + 1

def is_sq_unit(x, l): x %= l; return x != 0 and pow(x, (l - 1) // 2, l) == 1

if __name__ == '__main__':
    j, ell, NFAM, seed = int(sys.argv[1]), int(sys.argv[2]), int(sys.argv[3]), int(sys.argv[4])
    random.seed(seed)
    s = next(r for r in range(ell) if (r * r - j) % ell == 0)
    # Z_K^+ classes at the other primes, hard-coded for j = 8 (R225): m = 3 (8), m = 0 (3), m = 3 (7)
    assert j == 8
    BASE = [(8, 3), (3, 0), (7, 3)]
    L = 8 * 3 * 7 * ell
    SM = sorted({2 ** a * 3 ** b * 7 ** c * ell ** d for a in range(5) for b in range(2) for c in range(2) for d in range(2)})
    SM = [v for v in SM if v <= 8 * ell]
    grid = [(Fr(X, qx), Fr(sg * A, qa), Fr(Lm, ql)) for qx in (1, 2, 4) for X in range(-12 * qx, 12 * qx + 1)
            for A in SM for sg in (1, -1) for qa in (1, 2, 4, 8) for Lm in SM for ql in (1, 2, 4, 8, 16)]
    random.shuffle(grid)
    covered = set(); kept = 0; tried = 0
    for x, al, lam in grid:
        if tried >= NFAM: break
        if al * (x * x - j) >= 0: continue
        tried += 1
        fam = family(j, x, al, lam)
        if fam is None: continue
        D = den(fam)
        if L % D and (L * 8) % D: continue
        LL = lcm(L, D)
        C = [m for m in range(LL) if all(ev(p, m).denominator == 1 for p in fam.values())]
        if not C: continue
        # positivity for large m in C: check the first 3 representatives above 100 and the eventual sign
        ok = True
        for m0 in C[:4]:
            for m in (m0 + LL * 2, m0 + LL * 5):
                if any(ev(p, m) <= 0 for p in fam.values()) or not check_identities(fam, j, m): ok = False
        if not ok: continue
        # minimal valid m: all coords positive for all m >= some bound; record classes mod L fully contained in C
        Cs = set(C); kept += 1
        for r in range(L):
            if all((r + L * i) % LL in Cs for i in range(LL // L)): covered.add(r)
    # report at ell
    target = [r for r in range(L) if all(r % M == g for M, g in BASE) and (r * r - j) % ell != 0]
    print(f'j={j} ell={ell} s={s} L={L}: families kept {kept} of {tried} tried; target classes {len(target)}')
    by_res = {}
    for r in target:
        res = r % ell; by_res.setdefault(res, [0, 0]); by_res[res][0] += 1; by_res[res][1] += (r in covered)
    for res in sorted(by_res):
        zk = is_sq_unit(res - s, ell) and is_sq_unit(res + s, ell)
        print(f'  m = {res:2d} mod {ell}: n square? {is_sq_unit(res*res-j, ell)!s:5}  Z_K+? {zk!s:5}  covered {by_res[res][1]}/{by_res[res][0]}')
