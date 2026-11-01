#!/usr/bin/env python3
"""Z53_NONCRTLOGIC -- second half: does an escaping QNR primitive (n_p) carry information about (*) certificates
beyond its quadratic character?

For primes p = 1 (mod 24) in [A, B): enumerate ALL (*) solutions 4uBC - u - B = p (unordered {u, B}; trial form
B = (p+u)/(4uC-1), u <= B), using a smallest-prime-factor sieve.  The p-free Type II denominator is x = uBC; by Lemma CT it
has a prime factor l with (l/p) = -1.

For each small prime 5 <= l <= LMAX we record, per p:
   status(l) in {LEAST (l = n_p), QNR (l non-residue, l != n_p), QR (residue)}
   used(l)  = [some solution has l | uBC]
   frac(l)  = #{solutions with l | uBC} / #solutions
and aggregate by (l, status).  "Parity-only" prediction (Assessment): QNR rates > QR rates (Lemma CT forces a non-residue),
and LEAST = QNR for the same l (being the *least* non-residue carries no extra information).
Second generator: s_p = least prime l = +-3 (mod 8) dividing a norm Q_k of the continued fraction of sqrt(2p)
(such l are automatically non-residues: (2p/l) = 1 => (p/l) = (2/l) = -1).  Recorded: s_p, [s_p = n_p], used(s_p).
Controls / special primes: the (*)-zero primes in range (R = 0), reported separately.

Usage: uv run --with numpy --with gmpy2 python scripts/z53_noncrtlogic_qnrseed.py A B LMAX OUT.json
"""
import sys
import json
import numpy as np
import gmpy2


def spf_sieve(n):
    spf = np.zeros(n + 1, dtype=np.int32)
    spf[1] = 1
    for i in range(2, int(n ** 0.5) + 1):
        if spf[i] == 0:
            spf[i] = i
            blk = spf[i * i::i]
            mask = blk == 0
            blk[mask] = i
            spf[i * i::i] = blk
    rest = np.nonzero(spf == 0)[0]
    spf[rest] = rest
    return spf


def factor(n, spf):
    f = {}
    while n > 1:
        l = int(spf[n])
        f[l] = f.get(l, 0) + 1
        n //= l
    return f


def divisors_from(f):
    ds = [1]
    for l, e in f.items():
        ds = [d * l ** k for d in ds for k in range(e + 1)]
    return ds


def star_solutions(p, spf):
    sols = []
    u = 1
    while True:
        # need B >= u with C >= 1: m = 4uC-1 <= (p+u)/u
        if (4 * u - 1) * u > p + u:
            break
        N = p + u
        for m in divisors_from(factor(N, spf)):
            if (m + 1) % (4 * u) == 0:
                B = N // m
                if B >= u:
                    C = (m + 1) // (4 * u)
                    sols.append((u, B, C))
        u += 1
    return sols


def least_qnr(p):
    l = 2
    while True:
        if gmpy2.is_prime(l) and gmpy2.legendre(l, p) == -1:
            return l
        l += 1


def sqrt2p_seed(p, maxsteps=10 ** 6):
    """least prime l = +-3 mod 8 dividing some CF norm Q_k of sqrt(2p) (one period); None if none."""
    D = 2 * p
    a0 = gmpy2.isqrt(D)
    P, Q = 0, 1
    best = None
    steps = 0
    while True:
        a = (a0 + P) // Q
        P = a * Q - P
        Q = (D - P * P) // Q
        steps += 1
        if Q > 1:
            n = int(Q)
            while n % 2 == 0:      # strip the 2-part first (review finding 15)
                n //= 2
            l = 3
            while l * l <= n:
                if n % l == 0:
                    if l % 8 in (3, 5) and (best is None or l < best):
                        best = l
                    while n % l == 0:
                        n //= l
                l += 2
            if n > 1 and n % 8 in (3, 5) and (best is None or n < best):
                best = n
        if Q == 1:
            break
        if steps > maxsteps:
            raise RuntimeError(f"CF period of sqrt(2p) not finished within {maxsteps} steps at p={p}")
    return best


def main():
    A, B, LMAX, out = int(sys.argv[1]), int(sys.argv[2]), int(sys.argv[3]), sys.argv[4]
    spf = spf_sieve(B + int(B ** 0.5) + 10)
    small = [l for l in range(5, LMAX + 1) if gmpy2.is_prime(l)]
    agg = {l: {s: [0, 0, 0.0] for s in ('LEAST', 'QNR', 'QR')} for l in small}  # [n_p, used, sum frac]
    seed = {'n': 0, 's_eq_n': 0, 's_none': 0, 'used_n': 0, 'used_s': 0}
    zero = []
    nprimes = 0
    for p in range(A + (1 - A) % 24, B, 24):
        if not gmpy2.is_prime(p):
            continue
        nprimes += 1
        sols = star_solutions(p, spf)
        npl = least_qnr(p)
        seed['all'] = seed.get('all', 0) + 1
        if not sols:
            zero.append({'p': p, 'n_p': npl})
            continue
        xs = [u * Bv * C for (u, Bv, C) in sols]
        for l in small:
            st = 'LEAST' if l == npl else ('QNR' if gmpy2.legendre(l, p) == -1 else 'QR')
            k = sum(1 for x in xs if x % l == 0)
            a = agg[l][st]
            a[0] += 1
            a[1] += (k > 0)
            a[2] += k / len(xs)
        s = sqrt2p_seed(p)
        seed['n'] += 1
        if s is None:
            seed['s_none'] += 1
        else:
            seed['s_eq_n'] += (s == npl)
            seed['used_s'] += any(x % s == 0 for x in xs)
        seed['used_n'] += any(x % npl == 0 for x in xs)
    res = {'A': A, 'B': B, 'primes': nprimes, 'agg': {str(l): agg[l] for l in small}, 'seed': seed, 'zero': zero}
    with open(out, 'w') as fh:
        json.dump(res, fh)
    print(f"primes p=1(24) in [{A},{B}): {nprimes}; (*)-zero: {[z['p'] for z in zero]}")
    print(" l  | status | #p    | P(used)  | mean frac of solutions with l | uBC")
    for l in small:
        for st in ('LEAST', 'QNR', 'QR'):
            n, u, f = agg[l][st]
            if n:
                print(f"{l:3d} | {st:5s}  | {n:6d} | {u / n:.4f}  | {f / n:.4f}")
    sd = seed
    print(f"seed: primes with R(p)>0: {sd['n']} of {sd['all']}; P(some solution uses n_p | R>0) = {sd['used_n'] / sd['n']:.4f}, "
          f"unconditional {sd['used_n'] / sd['all']:.4f}; "
          f"sqrt(2p)-seed s_p: none {sd['s_none']}, s_p = n_p {sd['s_eq_n']}, "
          f"P(some solution uses s_p | R>0, s_p exists) = {sd['used_s'] / max(1, sd['n'] - sd['s_none']):.4f} "
          f"(denominator {sd['n'] - sd['s_none']})")


if __name__ == '__main__':
    main()
