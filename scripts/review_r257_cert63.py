# review_r257_cert63.py — R257 FROM-SCRATCH checker for EXP_OPEN Theorem 3.1 (ES for every 63*2^s + 1).
# No imports of z19_/z15_/z14_ code. Pure Python Fractions (sympy only for an optional cross-check of the identity).
# Reads only the DATA of data/z19/cert63_et.json (polynomials in n on residue classes n = r mod M).
# Usage: uv run python scripts/review_r257_cert63.py data/z19/cert63_et.json SMAX
import sys, json
from fractions import Fraction as F
from math import gcd

C0, K, L = 63, 1, 2520

# ---------- tiny polynomial arithmetic on lists of Fractions (low degree first) ----------
def pmul(p, q):
    r = [F(0)] * (len(p) + len(q) - 1)
    for i, a in enumerate(p):
        for j, b in enumerate(q):
            r[i + j] += a * b
    return r
def padd(*ps):
    m = max(len(p) for p in ps); r = [F(0)] * m
    for p in ps:
        for i, a in enumerate(p): r[i] += a
    return r
def pscale(p, c): return [a * c for a in p]
def ptrim(p):
    p = list(p)
    while p and p[-1] == 0: p.pop()
    return p
def peval(p, v): return sum(a * v ** i for i, a in enumerate(p))
def pcompose_lin(p, r, M):          # p(r + M t) as poly in t
    out = [F(0)]; powr = [F(1)]
    for a in p:
        out = padd(out, pscale(powr, a)); powr = pmul(powr, [F(r), F(M)])
    return out
def int_valued(p):                    # integer-valued on Z  <=>  forward differences at 0 integral
    d = len(p) - 1
    vals = [peval(p, t) for t in range(d + 1)]
    for _ in range(d + 1):
        if vals[0].denominator != 1: return False
        vals = [vals[i + 1] - vals[i] for i in range(len(vals) - 1)]
        if not vals: break
    return True

def is_square(N):
    from math import isqrt
    return isqrt(N) ** 2 == N

# ---------- (1) moving-gap class (Theorem 2.3), as polynomials in Y ----------
def check_moving():
    nY = [F(1), F(0), F(0), F(63)]
    a, d = F(5), F(17)
    b = [F(28, 340), F(-9, 340), F(3, 340), F(63, 340)]
    c = [F(64, 340), F(21, 340)]
    # Type II identity c*n + a + b == 4abcd  (equivalent to 4/n = 1/(abd)+1/(acdn)+1/(bcdn))
    lhs = padd(pmul(c, nY), [a], b)
    rhs = pscale(pmul(b, c), 4 * a * d)
    assert ptrim(padd(lhs, pscale(rhs, -1))) == [], 'Type II identity fails'
    # factorisation claims: n + 4a^2 d = 63(Y+3)(Y^2-3Y+9); 4abd - n = 3(Y^2-3Y+9); 4acd - 1 = 21(Y+3)
    assert ptrim(padd(nY, [4 * a * a * d], pscale(pmul([3, 1], [9, -3, 1]), -63))) == []
    assert ptrim(padd(pscale(b, 4 * a * d), pscale(nY, -1), pscale([9, -3, 1], -3))) == []
    assert ptrim(padd(pscale(c, 4 * a * d), [F(-1)], pscale([3, 1], -21))) == []
    # integrality: Y = 2^j, j = s/3, s = 0 mod 24 <=> j = 0 mod 8, j >= 8.
    # numerators NB = 63Y^3+3Y^2-9Y+28, NC = 21Y+64 mod 340 = 4*85: mod 4 need Y = 0 mod 4 (j >= 2): NB = 28, NC = 64 = 0 mod 4.
    # mod 85: ord_85(2) = lcm(4, 8) = 8, so 8 | j  => Y = 1 mod 85 => NB = 85, NC = 85 = 0 mod 85.
    o = next(e for e in range(1, 100) if pow(2, e, 85) == 1); assert o == 8
    for j in range(8, 8 + 8 * 40, 8):     # direct check over many periods (all residues j mod 8*... covered)
        Y = 2 ** j
        assert (63 * Y ** 3 + 3 * Y ** 2 - 9 * Y + 28) % 340 == 0 and (21 * Y + 64) % 340 == 0
    # also: exactly which j make both integral (mod 340 the condition depends on j mod 8 for j >= 2)
    good = [j for j in range(2, 2 + 8) if (63 * 8 ** j + 0) >= 0 and
            (63 * 2 ** (3 * j) + 3 * 2 ** (2 * j) - 9 * 2 ** j + 28) % 340 == 0 and (21 * 2 ** j + 64) % 340 == 0]
    return good

# ---------- (2) ET/divisor classes ----------
def check_classes(cert):
    assert cert['c0'] == 63 and cert['k'] == 1 and cert['b'] == 2
    out = []
    n = [F(0), F(1)]
    N10 = C0 * 2 ** 10 + K
    for cl in cert['classes']:
        M, r = cl['M'], cl['r']
        x, y, z = [[F(c) for c in p] for p in cl['xyz']]
        # identity 4xyz = n(xy + yz + zx)
        lhs = pscale(pmul(pmul(x, y), z), 4)
        rhs = pmul(n, padd(pmul(x, y), pmul(y, z), pmul(z, x)))
        assert ptrim(padd(lhs, pscale(rhs, -1))) == [], ('identity', M, r)
        for p in (x, y, z):
            assert int_valued(pcompose_lin(p, r, M)), ('integrality', M, r, p)
            # positivity for n >= N10: Taylor shift p(N10 + u) has all coeffs >= 0, constant > 0
            sh = pcompose_lin(p, N10, 1)
            assert all(c >= 0 for c in sh) and sh[0] > 0, ('positivity', M, r)
        e, Mo = 0, M
        while Mo % 2 == 0: Mo //= 2; e += 1
        assert e <= 10
        per = next(t for t in range(1, L + 1) if pow(2, t, Mo) == 1) if Mo > 1 else 1
        assert L % per == 0, ('period', M)
        assert r % (2 ** e) == 1 % (2 ** e), ('2-part residue', M, r)   # n = 1 mod 2^e for s >= e
        out.append((M, r, (x, y, z), per, cl['fam']))
    return out

def sol_from_class(classes, s):
    N = C0 * 2 ** s + K
    for M, r, (x, y, z), per, fam in classes:
        if N % M == r:
            v = [peval(p, N) for p in (x, y, z)]
            assert all(t.denominator == 1 and t > 0 for t in v), (s, M)
            return [int(t) for t in v], (M, r, fam)
    return None, None

def brute(N):   # 4/N = 1/x + 1/y + 1/z, x <= y <= z
    for x in range(N // 4 + 1, 3 * N // 4 + 1):
        R = F(4, N) - F(1, x)
        if R <= 0: continue
        ylo = max(x, R.denominator // R.numerator)
        for y in range(ylo, int(2 / R) + 1):
            R2 = R - F(1, y)
            if R2 > 0 and R2.numerator == 1: return [x, y, R2.denominator]
    return None

def main():
    cert = json.load(open(sys.argv[1])); SMAX = int(sys.argv[2]) if len(sys.argv) > 2 else 1500
    good = check_moving(); print('moving class: identity/factorisations OK; integral j in [2,10):', good)
    classes = check_classes(cert)
    print('classes OK:', len(classes), 'periods', sorted(set(c[3] for c in classes)),
          'moduli', sorted(set(c[0] for c in classes)))
    # coverage: for s >= 10, n_s mod M depends only on s mod 2520 (checked above). Test one full period.
    unc, used = [], {}
    for s in range(2520, 2520 + L):
        if s % 24 == 0: continue
        sol, tag = sol_from_class(classes, s)
        if sol is None: unc.append(s % L)
        else: used[tag] = used.get(tag, 0) + 1
    print('uncovered residues (s != 0 mod 24):', unc)
    print('class usage over one period:', used)
    # residues s = 0 mod 24 covered also by some ET class? (should be none if mu=0 obstruction is real)
    alsoET = [s % L for s in range(2520, 2520 + L, 24) if sol_from_class(classes, s)[0] is not None]
    print('s = 0 mod 24 residues that ET classes ALSO cover:', len(alsoET), 'of', L // 24)
    # T1: odd squares in family
    sq = [s for s in range(0, 4000) if is_square(C0 * 2 ** s + K)]
    print('squares 63*2^s+1 for s < 4000:', sq)
    # exact solutions for all s <= SMAX
    cnt = {'moving': 0, 'ET': 0, 'brute': 0}
    for s in range(0, SMAX + 1):
        N = C0 * 2 ** s + K; sol = None
        if s % 24 == 0 and s >= 24:
            Y = 2 ** (s // 3); a, d = 5, 17
            nb, nc = 63 * Y ** 3 + 3 * Y ** 2 - 9 * Y + 28, 21 * Y + 64
            assert nb % 340 == 0 and nc % 340 == 0
            b, c = nb // 340, nc // 340
            sol = [a * b * d, a * c * d * N, b * c * d * N]; cnt['moving'] += 1
        elif s >= 10:
            sol, _ = sol_from_class(classes, s); assert sol, s; cnt['ET'] += 1
        else:
            sol = brute(N); assert sol, s; cnt['brute'] += 1
        x, y, z = sol
        assert min(sol) > 0 and 4 * x * y * z == N * (x * y + y * z + z * x), s
    print('exact solutions verified for all 0 <= s <=', SMAX, cnt)

if __name__ == '__main__':
    main()
