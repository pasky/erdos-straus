"""Validate the formal fibre computation of formal_closure.py against the exact lazy fibres (DEPTH3 §6).

uv run python scripts/formal_validate.py [--B 13] [--trials 3] [--rounds 2]

Pick actual primes q with p=24q+1 prime, p a quadratic residue and q a unit modulo
every prime 5<=ell<=B. Use q itself as the base point qt of the formal model.
For every denominator z expanded within the given radius, compare the formal
fibre F(z), evaluated at q, with the actual fibre A(z) from pointwise_fibres.
Two checks are made:
  (i) F(z) is contained in A(z) (every formal vertex is a genuine vertex);
 (ii) F(z) = A(z) whenever the formal factorization of s is the true one,
      i.e. every formal prime value r_g dividing s is an actual prime > B.
"""
from __future__ import annotations

import argparse
import json
import random

from sympy import isprime, jacobi_symbol, primerange

from formal_closure import Formal
from pointwise_fibres import FibreOracle


def pick(B, rng, lo=10**9, hi=10**11):
    smalls = list(primerange(5, B + 1))
    while True:
        q = rng.randrange(lo, hi)
        if not isprime(q) or not isprime(24 * q + 1):
            continue
        p = 24 * q + 1
        if all(q % l and jacobi_symbol(p % l, l) == 1 for l in smalls):
            return q


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--B", type=int, default=13)
    ap.add_argument("--trials", type=int, default=3)
    ap.add_argument("--rounds", type=int, default=2)
    ap.add_argument("--seed", type=int, default=5)
    ap.add_argument("--model-B", type=int, default=None,
                    help="strip primes up to this bound into C_g (accident-aware model); default B")
    a = ap.parse_args()
    rng = random.Random(a.seed)
    tot = {"fibres": 0, "contained": 0, "exact_expected": 0, "exact_ok": 0,
           "dead": 0, "dead_singleton": 0}
    for _ in range(a.trials):
        q = pick(a.B, rng)
        p = 24 * q + 1
        F = Formal(a.model_B or a.B, qt=q)
        O = FibreOracle(p, max_divisors=10**7, max_fibre=10**7)
        frontier, done, V = [F.seed()], set(), {F.seed()}
        for _r in range(a.rounds):
            new = []
            for v in frontier:
                for z in v:
                    if z in done:
                        continue
                    done.add(z)
                    Ff = F.fibre(z)
                    Fv = {tuple(sorted(F.value(x) for x in w)) for w in Ff}
                    Av = set(O.fibre(F.value(z)))
                    tot["fibres"] += 1
                    if F.kind(z) == "dead":
                        tot["dead"] += 1
                        tot["dead_singleton"] += len(Av) <= 1
                    tot["contained"] += Fv <= Av
                    # exactness expected if the formal factorisation of s is true
                    N = F.from_poly(4 * F.poly(z) - __import__("sympy").Poly(24 * __import__("sympy").Symbol("X") + 1, __import__("sympy").Symbol("X"), domain=__import__("sympy").QQ))
                    keys = {k for k, e in N[1]} | {k for k, e in z[1]}
                    if all(isprime(F.primes[k][2]) and F.primes[k][2] > F.B for k in keys):
                        tot["exact_expected"] += 1
                        tot["exact_ok"] += Fv == Av
                    for w in Ff:
                        if w not in V:
                            V.add(w)
                            new.append(w)
            frontier = new
        print(json.dumps({"q": q, "formal_vertices": len(V), **tot}), flush=True)
    print("SUMMARY", json.dumps(tot))


if __name__ == "__main__":
    main()
