"""O148 brainstorm (BRAINSTORM/gon_lll_relation_lattice.md).

For e-slices (LONGSHOT_PIGEONHOLE Lemma 1.1): N = (p+e)/4 (Type II) or (pe+1)/4 (Type I), e = -p (mod 4).
ES slice holds iff -1 in Sigma_e(N) = {prod l^t mod e : |t_l| <= v_l(N)}  (box in the relation lattice).
Relaxation (linear algebra / group membership, no box): -1 in H_e = <l mod e : l | N>.
We count, for hard primes p (p = 1 mod 24, p mod 840 a square class) and odd-square controls n = m^2:
  slices, slices with -1 in H_e, slices with -1 in Sigma_e(N); and for prime e the genus prediction.
Usage: bs_gon_relation.py [EMAX] [NPRIMES]
"""
import sys
from math import gcd
from sympy import factorint, isprime, nextprime

EMAX = int(sys.argv[1]) if len(sys.argv) > 1 else 800
NP = int(sys.argv[2]) if len(sys.argv) > 2 else 12
SQ840 = {(x * x) % 840 for x in range(840) if gcd(x, 840) == 1}


def subgroup_has(gens, e, target):
    H = {1}
    frontier = [1]
    while frontier:
        new = []
        for h in frontier:
            for g in gens:
                y = h * g % e
                if y not in H:
                    H.add(y); new.append(y)
        frontier = new
        if target in H:
            return True
    return target in H


def sigma_has(fac, e, target):
    S = {1}
    for l, v in fac.items():
        li = pow(l, -1, e)
        powers = [1]
        for _ in range(v):
            powers.append(powers[-1] * l % e)
        ipow = [1]
        for _ in range(v):
            ipow.append(ipow[-1] * li % e)
        mult = set(powers) | set(ipow)
        S = {s * m % e for s in S for m in mult}
    return target in S


BINS = [30, 100, 300, 1000, 3000, 10**9]
ISP = False


def scan(n):
    """n = p prime or odd square; returns per-type counters."""
    global ISP
    ISP = isprime(n)
    res = {}
    for T in ('I', 'II'):
        cnt = dict(slices=0, H=0, Sig=0, Hprime=0, Sigprime=0, slices_prime=0)
        for e in range(3, EMAX + 1):
            if (n + e) % 4 or gcd(e, n) != 1:
                continue
            M = n + e if T == 'II' else n * e + 1
            if M % 4:
                continue
            N = M // 4
            fac = factorint(N)
            cnt['slices'] += 1
            pe = isprime(e)
            cnt['slices_prime'] += pe
            h = subgroup_has([l % e for l in fac], e, e - 1)
            s = h and sigma_has(fac, e, e - 1)
            cnt['H'] += h; cnt['Sig'] += s
            cnt['Hprime'] += h and pe; cnt['Sigprime'] += s and pe
            if pe and ISP:  # genus prediction for prime e: -1 in H iff some l | N has (l/p) = -1
                g = any(pow(l, (n - 1) // 2, n) == n - 1 for l in fac)
                assert g == h, (n, e, T)
            b = min(len(BINS) - 1, next(i for i, B in enumerate(BINS) if e <= B))
            cnt.setdefault('bins', [[0, 0, 0] for _ in BINS])
            cnt['bins'][b][0] += 1; cnt['bins'][b][1] += h; cnt['bins'][b][2] += s
        res[T] = cnt
    return res


if __name__ == "__main__":
    P0 = int(sys.argv[3]) if len(sys.argv) > 3 else 10**6
    p, primes = P0, []
    while len(primes) < NP:
        p = nextprime(p)
        if p % 24 == 1 and p % 840 in SQ840:
            primes.append(p)
    print(f"EMAX={EMAX}")
    agg = {T: [[0, 0, 0] for _ in BINS] for T in ('I', 'II')}
    for p in primes:
        r = scan(p)
        for T in r:
            for i, x in enumerate(r[T]['bins']):
                for j in range(3):
                    agg[T][i][j] += x[j]
        print(p, {T: (r[T]['slices'], r[T]['H'], r[T]['Sig'], r[T]['slices_prime'], r[T]['Hprime'], r[T]['Sigprime']) for T in r})
    print("e-bins (upper edge): [slices, -1 in H, -1 in Sigma]")
    for T in agg:
        print(T, list(zip(BINS, agg[T])))
    print("odd-square controls (m^2, m = 1 mod 840 neighbourhood):")
    for m in [1001, 1003, 1007, 1009, 1013, 1019]:
        r = scan(m * m)
        print(m * m, {T: (r[T]['slices'], r[T]['H'], r[T]['Sig']) for T in r})
