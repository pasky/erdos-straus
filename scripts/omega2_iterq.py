#!/usr/bin/env python3
"""POINTWISE_OMEGA2 §11 (EVIDENCE): iterated class-of-one quarantine (Lemma 11.2).

Start from Pi_0 = {primes <= z}; repeatedly add every free prime l with per-prime event
mass w_l(Pi) > c0 (c0 = 1/(8k), k = floor(log T/log z) unless given).  Report the rounds,
|B|, the bound k*S*/c0 (S* evaluated exactly), final max w_l, S_tot(Pi), the local-lemma
check max_E sum_{E'~E} x_E' (x = 2P), and the resulting Haar lower bound
log(1/delta*) <= log phi(Q_Pi) - log 8 + 4 S_tot.

usage: omega2_iterq.py T z [c0]
"""
import sys
from math import log, gcd

from pointwise_omega_S import spf_table, factor, divisors_from


def phi_pp(p, e):
    return (p - 1) * p ** (e - 1)


def main():
    T, z = int(sys.argv[1]), int(sys.argv[2])
    k = max(1, int(log(T) / log(z)))
    c0 = float(sys.argv[3]) if len(sys.argv) > 3 else 1 / (8 * k)
    spf = spf_table(T + 8)
    atoms = []  # (fac(M) dict, D mod M, g=gcd(M,4D+1))
    Sstar = 0.0
    for M in range(3, T + 1, 4):
        f = factor(M, spf)
        A = (M + 1) // 4
        fa = {p: 2 * e for p, e in factor(A, spf).items()}
        for D in divisors_from(fa):
            g = gcd(M, 4 * D + 1)
            atoms.append((M, f, D))
            # S*: max over Pi of 1/phi(r_Pi) with m_Pi | g: take m = largest unitary divisor of M dividing g
            m = 1
            for p, e in f.items():
                if g % (p ** e) == 0:
                    m *= p ** e
            if m < M:
                r = M // m
                ph = 1
                for p, e in f.items():
                    if r % p == 0:
                        ph *= phi_pp(p, e)
                Sstar += 1 / ph
    primes = [p for p in range(2, T + 1) if spf[p] == p]
    Pi = {p for p in primes if p <= z}
    rounds = 0
    while True:
        events = {}
        for M, f, D in atoms:
            m, r, fr = 1, 1, {}
            for p, e in f.items():
                if p in Pi:
                    m *= p ** e
                else:
                    r *= p ** e
                    fr[p] = e
            if r == 1 or (4 * D + 1) % m:
                continue
            key = r
            if key not in events:
                events[key] = (fr, set())
            events[key][1].add((-4 * D) % r)
        w = {}
        Stot = 0.0
        for r, (fr, cls) in events.items():
            ph = 1
            for p, e in fr.items():
                ph *= phi_pp(p, e)
            pr = len(cls) / ph
            Stot += pr
            for p in fr:
                w[p] = w.get(p, 0.0) + pr
        bad = {p for p, v in w.items() if v > c0}
        rounds += 1
        if not bad:
            break
        Pi |= bad
    B = sorted(p for p in Pi if p > z)
    # LLL check: max over events of 2*sum over its primes of w_l
    lll = 0.0
    for r, (fr, cls) in events.items():
        lll = max(lll, 2 * sum(w[p] for p in fr))
    logQ = sum(log(p) * max(e for e in range(1, 64) if p ** e <= T) for p in Pi)
    print(f"T={T} z={z} k={k} c0={c0:.4f}: rounds={rounds} |B|={len(B)} (bound k*S*/c0={k*Sstar/c0:.1f}, S*={Sstar:.2f}) "
          f"B[:12]={B[:12]}")
    print(f"  final: max w_l={max(w.values()):.4f} S_tot(Pi)={Stot:.2f} LLL max sum x={lll:.3f} (need <=~1/2) "
          f"log Q_Pi={logQ:.1f}  => log(1/delta*) <= {logQ - log(8) + 4*Stot:.1f}")


if __name__ == "__main__":
    main()
