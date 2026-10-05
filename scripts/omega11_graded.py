#!/usr/bin/env python3
"""POINTWISE_OMEGA11 §2 (EVIDENCE): graded quarantine with log-weighted thresholds (Lemma 2.2).

State: exponents a_l (start a_3=a_5=a_7=1), Q = 8 prod l^{a_l}.  Atom (M,D) survives iff
gcd(M,Q) | 4D+1 and M does not divide Q; its event lives on the coordinates l with
v_l(M) > a_l, probability prod 1/phi(l^v) (a_l=0) resp. l^{-(v-a_l)} (a_l>=1).
Distinct events are (tuple of (l, l^v)), class) pairs.  Rule: raise a_l by one whenever the
fibre mass w_l > c (a_l+1) log l / log T (all violators of a round at once).
Reports: rounds, log Q, number of graded primes, max exponent, final max_E sum_{l in E} w_l
(the local-lemma quantity, must be <= c), S_tot, the Haar bound log phi(Q) - log 8 + 4 S_tot,
and the proven cost bound (L/c) * sum_atoms s(M,D) h(M) (with s = (gcd(M,Q)... ) evaluated as
the exact max-over-Q weight bound gcd(M,4D+1)/M * prod l/(l-1)).

usage: omega11_graded.py T [c]
"""
import sys
from math import log, gcd

from pointwise_omega_S import spf_table, factor, divisors_from


def main():
    T = int(sys.argv[1])
    c = float(sys.argv[2]) if len(sys.argv) > 2 else 1 / 64
    L = log(T)
    spf = spf_table(T + 8)
    atoms = []
    cost_bound = 0.0
    for M in range(3, T + 1, 4):
        f = factor(M, spf)
        A = (M + 1) // 4
        fa = {p: 2 * e for p, e in factor(A, spf).items()}
        fl = tuple(sorted(f.items()))
        h = sum(sum(1 / i for i in range(1, e + 1)) for _, e in fl)
        euler = 1.0
        for p, _ in fl:
            euler *= p / (p - 1)
        for D in divisors_from(fa):
            g = gcd(M, 4 * D + 1)
            if g == M:
                raise RuntimeError("Fact 1.1 violated")
            atoms.append((fl, (-4 * D) % M, (4 * D + 1) % M))
            cost_bound += (L / c) * h * euler * g / M
    a = {3: 1, 5: 1, 7: 1}
    rounds = 0
    while True:
        rounds += 1
        events = {}
        for fl, cls, r41 in atoms:
            # survival: gcd(M,Q) | 4D+1, i.e. for each l: l^{min(v,a_l)} | 4D+1
            ok, coords = True, []
            for p, e in fl:
                al = a.get(p, 0)
                m = p ** min(e, al)
                if m > 1 and r41 % m:
                    ok = False
                    break
                if e > al:
                    coords.append((p, e))
            if not ok or not coords:
                continue
            key = tuple(coords)
            mod = 1
            for p, e in coords:
                mod *= p ** e
            events.setdefault(key, set()).add(cls % mod)
        w = {}
        Stot = 0.0
        evp = []
        for key, cls in events.items():
            pr = 1.0
            for p, e in key:
                al = a.get(p, 0)
                pr *= 1 / ((p - 1) * p ** (e - 1)) if al == 0 else p ** (-(e - al))
            pr *= len(cls)
            Stot += pr
            evp.append(key)
            for p, e in key:
                w[p] = w.get(p, 0.0) + pr
        viol = [p for p, v in w.items() if v > c * (a.get(p, 0) + 1) * log(p) / L]
        if not viol:
            break
        for p in viol:
            a[p] = a.get(p, 0) + 1
    lll = max((sum(w[p] for p, _ in key) for key in evp), default=0.0)
    logQ = log(8) + sum(e * log(p) for p, e in a.items())
    logphiQ = log(4) + sum(log(p - 1) + (e - 1) * log(p) for p, e in a.items() if e > 0)
    graded = sorted(a.items())
    print(f"T={T} c={c:.4f}: rounds={rounds} log Q={logQ:.1f} (proven bound {cost_bound:.0f}) "
          f"#primes in Q={sum(1 for _, e in graded if e > 0)} max prime={max(p for p, e in graded if e > 0)} "
          f"max exp={max(e for _, e in graded)}")
    print(f"  final: max_l w_l={max(w.values()):.4f} max_E sum w={lll:.4f} (need <= c) S_tot={Stot:.2f} "
          f"=> log(1/delta*) <= {logphiQ - log(2) + 4 * Stot:.1f}")
    print("  exponents (l:a_l, first 40):", " ".join(f"{p}:{e}" for p, e in graded[:40]))


if __name__ == "__main__":
    main()
