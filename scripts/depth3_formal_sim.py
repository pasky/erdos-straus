"""Simulation of the generic (Hypothesis-H) regime of DEPTH3.md Theorem 2 at depth 3.

uv run python scripts/depth3_formal_sim.py [--trials N] [--bits B] [--small L] [--qr-bound Q]

Pick huge q with p=24q+1 prime and p a quadratic residue modulo every prime
5<=ell<=Q. Run the exhaustive depth<=3 test of depth3.py with a PSEUDO
factorizer: primes <= L are split off by trial division, and the remaining
cofactors are refined into a coprime base whose elements are TREATED AS PRIME.
This mimics the situation in which H makes all large factors polynomial primes.
Every divisor used is a genuine divisor, so every vertex/path found is genuine;
only completeness is lost.
Theorem 2's mechanism predicts no escape when every base element b has Jacobi symbol
(b/p)=+1. The script reports escapes and the Jacobi symbols of the base
elements used, so the prediction can be tested directly.
Nothing here is a proof or a certificate.
"""
from __future__ import annotations

import argparse
import json
import random
from math import gcd, prod

from sympy import isprime, jacobi_symbol, primerange

import depth3


class Overlap(RuntimeError):
    pass


class PseudoFactorizer:
    def __init__(self, small_bound, base=()):
        self.small = list(primerange(2, small_bound + 1))
        self.base = set(base)
        self.cache = {}
        self.known = set()

    def add_known(self, *ps):
        for p in ps:
            self.base.add(p)

    def __call__(self, n):
        n = abs(n)
        if n in self.cache:
            return self.cache[n]
        orig, out = n, {}
        for ell in self.small:
            if n % ell == 0:
                e = 0
                while n % ell == 0:
                    n //= ell
                    e += 1
                out[ell] = e
        for b in sorted(self.base):
            if n == 1:
                break
            g = gcd(n, b)
            if g == 1:
                continue
            if g != b:
                raise Overlap((b, g))
            e = 0
            while n % b == 0:
                n //= b
                e += 1
            out[b] = e
        if n > 1:
            # new base element; check it is coprime to the base
            for b in self.base:
                if gcd(n, b) != 1:
                    raise Overlap((b, n))
            self.base.add(n)
            out[n] = out.get(n, 0) + 1
        assert prod(q**e for q, e in out.items()) == orig
        self.cache[orig] = out
        return out


def pick(bits, qr_bound, rng):
    from sympy.ntheory.modular import crt
    smalls = list(primerange(5, qr_bound + 1))
    M = prod(smalls)
    while True:
        res = []
        for l in smalls:
            ok = [r for r in range(1, l) if jacobi_symbol((24 * r + 1) % l, l) == 1]
            res.append(rng.choice(ok))
        q0 = int(crt(smalls, res)[0])
        for _ in range(20000):
            q = q0 + M * rng.getrandbits(max(bits - M.bit_length(), 8))
            p = 24 * q + 1
            if isprime(q) and isprime(p):
                return q, p


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--trials", type=int, default=50)
    ap.add_argument("--bits", type=int, default=120)
    ap.add_argument("--small", type=int, default=2000)
    ap.add_argument("--qr-bound", type=int, default=200)
    ap.add_argument("--seed", type=int, default=1)
    a = ap.parse_args()
    rng = random.Random(a.seed)
    stats = {"trials": 0, "escapes": 0, "overlap": 0}
    for _ in range(a.trials):
        q, p = pick(a.bits, a.qr_bound, rng)
        base = {q, p}
        for _attempt in range(40):
            F = PseudoFactorizer(a.small, base=base)
            try:
                D = depth3.Depth3(p, factor=F, t_factors={2: 1, 3: 1, q: 1})
                r = D.run(all_hits=True)
                break
            except Overlap as e:
                b, g = e.args[0]
                g = gcd(b, g)
                base = (F.base - {b}) | {g, b // g}
        else:
            stats["overlap"] += 1
            continue
        stats["trials"] += 1
        large = sorted(b for b in F.base if b not in (p,))
        neg = [b for b in large if jacobi_symbol(b % p, p) == -1]
        smallneg = [l for l in F.small if l > 3 and jacobi_symbol(l, p) == -1]
        if r["hits"]:
            stats["escapes"] += 1
            # (2a) check: the positive end vertex must involve a base element of symbol -1
            P = r["hits"][0]["path"][-1]
            vals = sorted((z for z in P), key=lambda z: z % p == 0)
            pf = [z for z in P if z % p]
            pair = pf if len(pf) == 2 else [z // p for z in P if z % p == 0]
            AB = abs(pair[0] * pair[1])
            used = [b for b in large if AB % b == 0]
            stats.setdefault("escape_uses_minus", 0)
            stats["escape_uses_minus"] += any(jacobi_symbol(b % p, p) == -1 for b in used)
        print(json.dumps({"qbits": q.bit_length(), "dist": r["dist"], "hits": len(r["hits"]),
                          "base": len(large), "base_jacobi_minus": len(neg),
                          "small_nonresidues_used_bound": len(smallneg),
                          "first": [(h["family"], h.get("h"), h.get("c"), h.get("d"), h.get("a"))
                                    for h in r["hits"][:3]]}), flush=True)
    print("SUMMARY", json.dumps(stats))


if __name__ == "__main__":
    main()
