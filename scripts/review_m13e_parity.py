"""R107 from-scratch check of POINTWISE_MORDELL13E Lemma 2.1 (parity of the ES level in the (2,2) cell).
Random T-generic data (T={11,13}) of the seven families, built so that the T-free condition (class contains
points with residue 1 mod the T-free modulus) holds often; literal classes from the ET Prop 1.9 residues
(own code).  For every datum whose box meets {x_11 = 2 (11), x_13 = 2 (13)} we
 (a) compute the ES level N from the family formula and VERIFY it by the explicit ES identity
     (13B Lemmas 2.1-2.4, re-implemented here) with exact fractions;
 (b) test the parity claim: v_T(N) odd, except I3: v_T(N) = v_T(f)+1 (mod 2);
 (c) also record N <= M_T^2 and M_T <= N.
usage: review_m13e_parity.py [n_per_family] [seed]"""
import random, sys
from math import gcd
from fractions import Fraction as Fr
from sympy import divisors, sqrt_mod

T = (11, 13)
def tp(m):
    t = 1
    for q in T:
        while m % q == 0: m //= q; t *= q
    return t
def v(m):
    s = 0
    for q in T:
        while m and m % q == 0: m //= q; s += 1
    return s
def crt(r1, m1, r2, m2):
    return (r1 + m1 * ((r2 - r1) * pow(m1, -1, m2) % m2)) % (m1 * m2)
TU = [11**i * 13**j for i in range(4) for j in range(4) if 11**i * 13**j < 40000]
def rv():
    return random.choice([1, 1, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 12, 15]) * random.choice([1, 1, 1, 11, 13, 121, 143, 169, 1331, 2197, 1573, 1859])
def tfree_div(m):  # random T-free divisor of m
    ds = [g for g in divisors(m) if gcd(g, 143) == 1]
    return random.choice(ds)

def gen(fam):
    while True:
        if fam in ('I1', 'I3', 'II3', 'II2'):
            a, d = rv(), rv()
            if gcd(a * d, 1) != 1: continue
            if fam == 'I1':
                f = random.choice(divisors(4 * a * a * d + 1))
                if (f + 1) % (4 * (a * d // tp(a * d))): continue
                return (a, d, f)
            g = tfree_div(4 * a * a * d + 1); B = random.choice(TU); f = B * g
            if fam == 'II2':
                if (f + 1) % (4 * a * d): continue
                return (a, d, f)
            if gcd(4 * a * d, f) != 1: continue
            if (f + 1) % (4 * (a * d // tp(a * d))): continue
            return (a, d, f)
        if fam == 'I2':
            a, c = rv(), rv(); g = tfree_div(a + c); f = random.choice(TU) * g
            if gcd(4 * a * c, f) != 1: continue
            if (f + 1) % (4 * (a * c // tp(a * c))): continue
            return (a, c, f)
        if fam in ('I4', 'II1'):
            a, b = rv(), rv(); e = random.choice(divisors(a + b))
            if gcd(e, 4 * a * b) != 1: continue
            if (e + 1) % (4 * (a * b // tp(a * b))): continue
            return (a, b, e)

def cls(fam, P):  # list of residues, modulus
    x, y, z = P
    if fam == 'I1': M = 4 * x * y; return [(-z) % M], M
    if fam == 'II1': M = 4 * x * y; return [(-z) % M], M
    if fam == 'I4': M = 4 * x * y; return [(-pow(z, -1, M)) % M], M
    if fam == 'II2': return [(-4 * x * x * y) % z], z
    if fam == 'II3': M = 4 * x * y * z; return [(-4 * x * x * y - z) % M], M
    if fam == 'I2':
        r2 = (-y * pow(x, -1, z)) % z if z > 1 else 0
        return [crt((-z) % (4 * x * y), 4 * x * y, r2, z)], 4 * x * y * z
    if fam == 'I3':
        if z == 1: roots = [0]
        else: roots = sorted(set(sqrt_mod((-4 * x * x * y) % z, z, all_roots=True) or []))
        return [crt((-z) % (4 * x * y), 4 * x * y, s, z) for s in roots], 4 * x * y * z

def es_level_and_check(fam, P):
    """ES level N and an explicit solution (13B Lemmas 2.1-2.4); asserts 4/N = 1/X+1/Y+1/Z."""
    x, y, z = P
    if fam in ('II1', 'I4'):
        a, b, e = P; F = tp(a * b); c = (a + b) // e; i = Fr((e + 1) * F, 4 * a * b)
        assert i.denominator == 1; i = int(i); sol = (i * a * b, i * a * c, i * b * c); N = F
    elif fam == 'II2':
        a, d, f = P; F = tp(f); fp = f // F; m = (f + 1) // (4 * a * d); assert (a + m) % fp == 0
        j = (a + m) // fp; sol = (a * m * d * F, a * j * d, m * j * d); N = F
    elif fam == 'I2':
        a, c, f = P; A = tp(a * c); B = tp(f); fp = f // B; acp = a * c // A
        t = (f + 1) // (4 * acp); h = (a + c) // fp; sol = (c * t * h, a * t * h, B * a * c * t); N = A * B
    else:  # II3 (a,d,e), I3 (c,d,f), I1 (a,d,f) with B=1
        a, d, e = P; B = 1 if fam == 'I1' else tp(e); g = e // B
        aT, dT = tp(a), tp(d); ap, dp = a // aT, d // dT; lam = aT * aT * dT
        m = (e + 1) // (4 * ap * dp); assert (e + 1) % (4 * ap * dp) == 0
        assert (lam * ap + m) % g == 0; j = (lam * ap + m) // g
        sol = (dp * m * j, lam * ap * dp * j, B * lam * ap * dp * m); N = B * lam
    assert Fr(4, N) == sum(Fr(1, s) for s in sol), (fam, P, N, sol)
    return N

def main():
    n = int(sys.argv[1]) if len(sys.argv) > 1 else 3000
    random.seed(int(sys.argv[2]) if len(sys.argv) > 2 else 1)
    tot = 0; bad = 0; rng = 0; cnt = {}
    for fam in ('I1', 'I2', 'I3', 'I4', 'II1', 'II2', 'II3'):
        cnt[fam] = [0, 0]
        for _ in range(n):
            P = gen(fam); R, M = cls(fam, P); MT = tp(M); Mp = M // MT
            box = {r % MT for r in R if r % Mp == 1 % Mp}
            if not box: continue
            N = es_level_and_check(fam, P); cnt[fam][0] += 1
            if not (MT <= N <= MT * MT): rng += 1; print('RANGE', fam, P, MT, N)
            if not any(all(r % q == 2 for q in T if MT % q == 0) for r in box): continue
            cnt[fam][1] += 1; tot += 1
            want = (v(P[2]) + 1) % 2 if fam == 'I3' else 1
            if v(N) % 2 != want: bad += 1; print('PARITY FAIL', fam, P, MT, N, sorted(box)[:4])
    print('T-generic data / meeting (2,2) cell per family:', cnt)
    print('ES identity verified for all T-generic data; range violations', rng, '; parity failures', bad, 'of', tot)

if __name__ == '__main__':
    main()
