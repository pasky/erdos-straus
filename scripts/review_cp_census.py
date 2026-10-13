"""R203 from-scratch recomputation of the COMPOSITION_ES §5 census.

usage: review_cp_census.py lo hi [nonES]
For every prime lo <= p <= hi and every ES point (mu, D) of V_p (Thm 1.3 enumeration), decide for every
divisor d' of D (1 < d' < D) whether the divisor ideal of norm d' of (eps_mu) is principal in O' = Z[sqrt N],
N = 4(mu^2 - p), by one full CF period of sqrt N (Lagrange: |norm| < sqrt N reps are convergents), tracking
convergents mod D only.  Membership of x + y sqrt N in (d', eps_mu): j x + (2 j mu - 1) y = 0 mod d'.
'nonES': also scan mu with D not dividing mu but rad(D) | mu, looking for eps_mu = unit * product of three
V_p points at mu (each norm | mu) -- a B = 1 element obtained by composition that is NOT an ES point.
"""
import sys
from math import isqrt, gcd

def is_prime(m):
    if m < 2: return False
    if m % 2 == 0: return m == 2
    r = 3
    while r * r <= m:
        if m % r == 0: return False
        r += 2
    return True

def divisors(m):
    ds = [1]
    q = 2; mm = m
    while q * q <= mm:
        if mm % q == 0:
            e = 0
            while mm % q == 0:
                mm //= q; e += 1
            ds = [d * q**k for d in ds for k in range(e + 1)]
        q += 1
    if mm > 1:
        ds = [d * k for d in ds for k in (1, mm)]
    return sorted(ds)

def principal_divisors(mu, n, j, D):
    """set of d' | D (1<d'<D) whose divisor ideal of (eps_mu) is principal; also index check."""
    N = 4 * (mu * mu - n)
    a0 = isqrt(N)
    props = [d for d in divisors(D) if 1 < d < D]
    found = set()
    c = (2 * j * mu - 1) % D
    # convergents mod D; Q_k with p_{k-1}^2 - N q_{k-1}^2 = (-1)^k Q_k
    m, Q, a = 0, 1, a0
    pm1, p0 = 1, a0 % D
    qm1, q0 = 0, 1
    k = 0
    eps_index = None
    while True:
        m = Q * a - m
        Q = (N - m * m) // Q
        a = (a0 + m) // Q
        k += 1
        # now (p0,q0) = (p_{k-1}, q_{k-1}) has norm (-1)^k Q
        if D % Q == 0:
            if Q == D and k % 2 == 1 and (j * p0 - c * q0) % D == 0 and eps_index is None:
                eps_index = k
            if 1 < Q < D:
                for sgn in (1, -1):
                    if (j * p0 + sgn * c * q0) % Q == 0:
                        found.add(Q)
        if Q == 1:
            break
        pm1, p0 = p0, (a * p0 + pm1) % D
        qm1, q0 = q0, (a * q0 + qm1) % D
    return found, eps_index, k

def chain(D, prin, normok=lambda d: True):
    """exists d1 | d2 | D, 1<d1<d2<D, both principal, d1 = 3 mod 4, d2 = 1 mod 4 (signs then automatic)."""
    for d1 in prin:
        if d1 % 4 != 3 or not normok(d1): continue
        for d2 in prin:
            if d2 % 4 == 1 and d2 % d1 == 0 and d2 > d1 and normok(d2 // d1) and normok(D // d2):
                return True
    return False

def es_points(n):
    out = []
    for t in range(1, n + 1):
        M = n + 4 * t * t
        for D in divisors(M):
            if D > 1 and (D + 1) % (4 * t) == 0:
                j = (D + 1) // (4 * t)
                out.append((n * j + t, D, j, t))
    return out

def main():
    lo, hi = int(sys.argv[1]), int(sys.argv[2])
    nonES = len(sys.argv) > 3
    nprimes = npts = nDprime = ncomp = ndec = nV = nprimes_dec = 0
    bad_index = 0
    for p in range(max(lo, 5), hi + 1):
        if not is_prime(p): continue
        nprimes += 1
        anydec = False
        for (mu, D, j, t) in es_points(p):
            npts += 1
            assert mu % D == 0
            if is_prime(D):
                nDprime += 1
                continue
            ncomp += 1
            prin, ei, per = principal_divisors(mu, p, j, D)
            want = 3 if mu > 2 * p else 1
            if ei != want:
                bad_index += 1
            if prin:
                ndec += 1; anydec = True
                if chain(D, prin):
                    nV += 1
                    print(f"V-dec p={p} mu={mu} D={D} principal={sorted(prin)}", flush=True)
        nprimes_dec += anydec
        if nonES:
            for mu in range(p + 1, p * p + 2 * p):
                j, t = (mu - 1) // p, (mu - 1) % p + 1
                D = 4 * t * j - 1
                if mu % D == 0: continue
                # radical of D must divide mu
                r = 1
                for q in divisors(D):
                    if q > 1 and is_prime(q): r *= q
                if mu % r: continue
                prin, ei, per = principal_divisors(mu, p, j, D)
                if chain(D, prin, lambda d: mu % d == 0):
                    print(f"NON-ES COMPOSITION: p={p} mu={mu} D={D} (D does not divide mu) principal={sorted(prin)}", flush=True)
    print(f"primes {nprimes}; ES points {npts}; D prime {nDprime}; D composite {ncomp}; decomposable {ndec}; "
          f"V-decomposable {nV}; primes with >=1 decomposable {nprimes_dec}; eps index mismatches {bad_index}")

main()
