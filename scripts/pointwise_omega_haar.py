#!/usr/bin/env python3
"""POINTWISE_OMEGA.md section 9 (Haar side, EVIDENCE): class-of-one quarantine at all primes <= z,
then the surviving atoms (M<=T, M=3 mod 4, rough part r>1, D | A_M^2 with m | 4D+1, m = z-smooth
part of M) as distinct events (r, a = -4D mod r) of Haar probability 1/phi(r).

Prints: S_tot = sum_E 1/phi(r_E); per-prime w_l = sum_{E: l | r_E} 1/phi(r_E) for primes l > z, the LLL
quantity  max_l w_l * 8 log T / log z  (Hypothesis H_PP(z) asks <= 1), max_l l*w_l, and the
structural-lemma check m <= r^2+1 for every surviving atom (Lemma 9.1).
Usage: PYTHONPATH=scripts uv run python scripts/pointwise_omega_haar.py T z1 [z2 ...]"""
import sys
from math import log
from pointwise_omega_S import spf_table, factor, divisors_from


def phi_from(f):
    r = 1
    for p, e in f.items():
        r *= (p - 1) * p ** (e - 1)
    return r


def run(T, z, spf):
    events = {}  # r -> set of classes
    rfac = {}
    viol = 0
    natoms = 0
    for M in range(3, T + 1, 4):
        f = factor(M, spf)
        m, r, fr = 1, 1, {}
        for p, e in f.items():
            if p <= z:
                m *= p ** e
            else:
                r *= p ** e
                fr[p] = e
        if r == 1:
            continue
        A = (M + 1) // 4
        fa = {p: 2 * e for p, e in factor(A, spf).items()}
        for D in divisors_from(fa):
            if (4 * D + 1) % m == 0:
                natoms += 1
                if m > r * r + 1:
                    viol += 1
                events.setdefault(r, set()).add((-4 * D) % r)
        rfac[r] = fr
    S = 0.0
    w = {}
    wm = {}
    for r, cls in events.items():
        pr = len(cls) / phi_from(rfac[r])
        S += pr
        for p in rfac[r]:
            w[p] = w.get(p, 0.0) + pr
            if len(rfac[r]) >= 2:
                wm[p] = wm.get(p, 0.0) + pr
    Lf = 8 * log(T) / log(z)
    if wm:
        mm = max(wm.items(), key=lambda kv: kv[1])
        lm = max((v * p, p) for p, v in wm.items())
        print(f"   multi-prime part: max w^multi_l={mm[1]:.4f} (l={mm[0]}), ratio*{Lf:.1f}={mm[1]*Lf:.3f}, "
              f"max l*w^multi_l={lm[0]:.2f} (l={lm[1]})")
    lll = max(v for v in w.values()) * 8 * log(T) / log(z)
    lmax, worst = max((v * p, p) for p, v in w.items())
    lw = max(w.items(), key=lambda kv: kv[1])
    print(f"T={T} z={z}: atoms={natoms} events={sum(len(c) for c in events.values())} S_tot={S:.3f} "
          f"max w_l={lw[1]:.4f} (l={lw[0]}) LLL ratio max w*8logT/logz={lll:.3f} "
          f"max l*w_l={lmax:.2f} (l={worst}) structural violations m>r^2+1: {viol}")
    return viol


if __name__ == "__main__":
    T = int(sys.argv[1])
    spf = spf_table(T + 8)
    bad = 0
    for z in map(int, sys.argv[2:]):
        bad += run(T, z, spf)
    if bad:
        sys.exit(1)


def F_full(l):
    """Lemma 9.1 parametrisation: all single-prime atom classes at the prime l (any m coprime to l):
    D = s r'^2 <= A (s squarefree), n = s r' <= l/2, v | 4 n r' + 1, 4n | l + v, m = (4nr'+1)/v,
    k = m (l+v)/(4n) - r' >= r'.  Classes -4D and its partner -(4D)^{-1} (mod l)."""
    from sympy import divisors
    out = set()
    for n in range(1, l // 2 + 1):
        for r in divisors(n):
            if True:
                s = n // r
                if all(s % (p * p) for p in range(2, int(s ** 0.5) + 1)):
                    N0 = 4 * n * r + 1
                    for v in divisors(N0):
                        if (l + v) % (4 * n):
                            continue
                        m = N0 // v
                        k = m * (l + v) // (4 * n) - r
                        if k < r or (m * l) % 4 != 3:
                            continue
                        D = s * r * r
                        out.add((-4 * D) % l)
                        out.add((-pow(4 * D, -1, l)) % l)
    return out
