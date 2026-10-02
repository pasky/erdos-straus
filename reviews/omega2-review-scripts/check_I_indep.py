"""Reviewer's independent check of implication (I) of POINTWISE_OMEGA2 Lemma 4.3.
Formulation differs from the author's: R(M) is built from the paper's definition
   n = -u v^{-1} (mod M) with u v w = A_M      (es-omega-note.tex, eq. for W),
and survival is "class c in R(M) with c = 1 mod m_Pi(M)"; events are c mod r_Pi(M).
Bad primes: threshold on Haar mass of singles at Pi_0 (as Construction 4.2.1).
Samples n = 1 (mod Q) via CRT, residues at free primes drawn uniformly from units
avoiding singles, rejection on edges; checks W(n) > T directly.
Also asserts every surviving event has r in {l, l^2, l l'} when y > T^{1/3}.
usage: check_I_indep.py T y_exponent gbad samples seed
"""
import sys, random
from math import gcd

def sieve(n):
    s = list(range(n + 1))
    for i in range(2, int(n ** .5) + 1):
        if s[i] == i:
            for j in range(i * i, n + 1, i):
                if s[j] == j:
                    s[j] = i
    return s

def fac(n, s):
    f = {}
    while n > 1:
        p = s[n]; f[p] = f.get(p, 0) + 1; n //= p
    return f

def divs(n, s):
    ds = [1]
    for p, e in fac(n, s).items():
        ds = [d * p ** k for d in ds for k in range(e + 1)]
    return ds

def main():
    T, th, gbad, samples, seed = int(sys.argv[1]), float(sys.argv[2]), float(sys.argv[3]), int(sys.argv[4]), int(sys.argv[5])
    s = sieve(T + 5)
    primes = [p for p in range(2, T + 1) if s[p] == p]
    y = T ** th
    e = {}
    for p in primes:
        k = 1
        while p ** (k + 1) <= T: k += 1
        e[p] = k
    R = {}
    for M in range(3, T + 1, 4):
        A = (M + 1) // 4
        cl = set()
        for u in divs(A, s):
            for v in divs(A // u, s):
                if gcd(v, M) == 1:
                    cl.add((-u * pow(v, -1, M)) % M)
        R[M] = cl
    def events(inPi):
        out = []
        for M, cl in R.items():
            m = 1
            for p, k in fac(M, s).items():
                if inPi(p): m *= p ** k
            r = M // m
            if r == 1:
                assert all(c % m != 1 % m for c in cl)  # class of one
                continue
            for c in cl:
                if c % m == 1 % m:
                    out.append((r, c % r, tuple(sorted(fac(r, s)))))
        return out
    ev0 = events(lambda p: p <= y)
    g0 = {}
    for r, c, ps in ev0:
        if len(ps) == 1:
            g0.setdefault(ps[0], set()).add((r, c))
    def mass(l, S):
        mod = l ** e[l]
        return sum(1 for a in range(mod) if a % l and any(a % r == c for r, c in S)) / (mod - mod // l)
    bad = {l for l, S in g0.items() if mass(l, S) > gbad}
    inPi = lambda p: p <= y or p in bad
    ev = events(inPi)
    free = [p for p in primes if not inPi(p)]
    if y > T ** (1 / 3):
        for r, c, ps in ev:
            f = fac(r, s)
            assert len(ps) <= 2 and sum(f.values()) <= 2, (r, f)
    sing = {}; edg = []
    for r, c, ps in ev:
        if len(ps) == 1: sing.setdefault(ps[0], set()).add((r, c))
        else: edg.append((r, c))
    Q = 24
    for p in primes:
        if inPi(p): Q = Q * p ** e[p] // gcd(Q, p ** e[p])
    rng = random.Random(seed)
    got = ok = tries = 0
    while got < samples and tries < 1000 * samples:
        tries += 1
        n, mod = 1, Q
        for l in free:
            m2 = l ** e[l]
            while True:
                a = rng.randrange(1, m2)
                if a % l and not any(a % r == c for r, c in sing.get(l, ())): break
            t = ((a - n) * pow(mod, -1, m2)) % m2
            n, mod = n + mod * t, mod * m2
        if any(n % r == c for r, c in edg):
            continue
        got += 1
        ok += all(n % M not in R[M] for M in R)
    print(f"T={T} y={y:.1f} bad={sorted(bad)} free={len(free)} singles-primes={len(sing)} edges={len(edg)} "
          f"forced survivors={got} with W>T: {ok} (mismatches {got-ok}) tries={tries}")

main()
