#!/usr/bin/env python3
"""O254 / JOINT_BUDGET: machine checks of Theorem A, Prop 3.2, Prop 4.2, Remark 4.4.
(a) Theorem A: sympy factor_list of every RT2 side N_theta(X) for random polynomial slice choices theta(u1,u2)
    (positive leading coefficients): the X-dependent part is irreducible, the content is X-free.
(b) Prop 3.2 (Kneser threshold): random (m, K) with m prime, K composed of small primes: whenever (3.1) holds,
    the box Sigma_m(K) equals H0 (brute force).
(c) Prop 4.2: for primes p ≡ 1 (4) <= P, every CF norm m = |P_k^2 - p Q_k^2| (odd, gcd(Q_k, m) = 1, m > 1) and every
    near-square window m = w^2 - p (odd, > 0, w < sqrt(p)+30) has Jacobi (p/m) = +1.
(d) Remark 4.4 (p is a non-square mod 4ab) is checked inside z26_cyclo_depth (all k* even) and here for p <= 3000, all
    Type II points.
"""
import random, sys, math
import sympy as sp
from sympy import factor_list, symbols, jacobi_symbol, isprime, primerange

random.seed(254)
u1, u2, X = symbols('u1 u2 X')


def rpoly():
    # random polynomial with non-negative coefficients, degree <= 2 in (u1, u2), not identically zero
    mons = [1, u1, u2, u1*u2, u1**2, u2**2]
    f = sum(random.randint(0, 3) * m for m in mons)
    return f if f != 0 else 1 + u1


def check_A(trials=60):
    bad = 0
    for _ in range(trials):
        a, b, c, d, e = (rpoly() for _ in range(5))
        sides = [X**2 + 4*c**2*d, a*X + c, e*X + 1, 4*c**2*d*X + 1, c*X + a, X + 4*a**2*d, X + e]
        for N in sides:
            const, facs = factor_list(sp.expand(N))
            xdep = [(f, k) for f, k in facs if f.has(X)]
            if len(xdep) != 1 or xdep[0][1] != 1 or sp.degree(xdep[0][0], X) != sp.degree(N, X):
                bad += 1
                print('A-violation', N, facs)
    return bad


def box(m, K):
    fac = sp.factorint(K)
    S = {1}
    for s, v in fac.items():
        inv = pow(s, -1, m)
        new = set()
        for x in S:
            y = x
            for _ in range(v + 1):
                new.add(y); y = y * s % m
            y = x
            for _ in range(v):
                y = y * inv % m; new.add(y)
        S = new
    return S, fac


def subgroup_gen(m, gens):
    H = {1}
    frontier = [1]
    while frontier:
        x = frontier.pop()
        for g in gens:
            y = x * g % m
            if y not in H:
                H.add(y); frontier.append(y)
    return H


def all_subgroups(m, H0):
    # subgroups of the cyclic group H0 <= (Z/m)^*: one per divisor of |H0|
    n = len(H0)
    gen = next(g for g in H0 if len(subgroup_gen(m, [g])) == n)
    return [subgroup_gen(m, [pow(gen, n // t, m)]) for t in sp.divisors(n)]


def check_kneser(trials=3000):
    tested = held = viol = 0
    primes = list(primerange(3, 60))
    for _ in range(trials):
        m = random.choice([q for q in primerange(5, 80)])
        sm = [q for q in primes if q % m]
        K = 1
        for _ in range(random.randint(1, 7)):
            K *= random.choice(sm)
        S, fac = box(m, K)
        H0 = subgroup_gen(m, [s % m for s in fac])
        cond = True
        for H in all_subgroups(m, H0):
            if len(H) == len(H0):
                continue
            lhs = sum(2 * v for s, v in fac.items() if s % m not in H)
            if lhs < len(H0) // len(H) - 1:
                cond = False; break
        tested += 1
        if cond:
            held += 1
            if S != H0:
                viol += 1
                print('Kneser violation', m, K)
    return tested, held, viol


def cf_norms(p, terms=40):
    a0 = math.isqrt(p); mm, dd, aa = 0, 1, a0
    P0, P1, Q0, Q1 = 1, a0, 0, 1
    out = []
    for _ in range(terms):
        out.append((P1, Q1))
        mm = dd * aa - mm; dd = (p - mm * mm) // dd; aa = (a0 + mm) // dd
        P0, P1 = P1, aa * P1 + P0; Q0, Q1 = Q1, aa * Q1 + Q0
    return out


def check_42(P=200000):
    n = bad = 0
    for p in primerange(5, P):
        if p % 4 != 1:
            continue
        for (A, B) in cf_norms(p):
            m = abs(A * A - p * B * B)
            if m > 1 and m % 2 and math.gcd(B, m) == 1 and m % p:
                n += 1
                if jacobi_symbol(p, m) != 1:
                    bad += 1
        w0 = math.isqrt(p) + 1
        for w in range(w0, w0 + 30):
            m = w * w - p
            if m % 2 and m > 1 and m % p:
                n += 1
                if jacobi_symbol(p, m) != 1:
                    bad += 1
    return n, bad


def check_44(P=3000):
    n = bad = 0
    for p in primerange(5, P):
        if p % 4 != 1:
            continue
        for e in range(3, (p + 4) // 3 + 1, 4):
            K = (p + e) // 4
            for a in sp.divisors(K):
                for b in sp.divisors(K // a):
                    if b >= a and (a + b) % e == 0:
                        n += 1
                        M = 4 * a * b
                        if sp.ntheory.residue_ntheory.is_quad_residue(p % M, M):
                            bad += 1
    return n, bad


if __name__ == '__main__':
    print('(a) Theorem A violations:', check_A())
    print('(b) Kneser: tested/(3.1) held/violations:', check_kneser())
    print('(c) Prop 4.2: windows checked/violations:', check_42())
    print('(d) Remark 4.4: Type II points p<3000 / p square mod 4ab:', check_44())
