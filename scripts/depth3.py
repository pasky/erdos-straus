"""Exhaustive depth<=3 seed-escape test via the proved classification of DEPTH3.md.

uv run python scripts/depth3.py P [P ...]          # JSON per prime
uv run python scripts/depth3.py --range LO HI      # all primes p=1 mod 4

For p=4t+1 prime, seed distance <= 3 iff one of the families holds:

  (9)  h|t^2, h>0: some D|(ph-t)^2, D>0, D = -h (mod 4h-1)       [distance 2]
  (A)  c|t^2, c>0, d|(pc+t)^2, d>0, d = -c (mod 4c+1),
       a=(d+c)/(4c+1), x=t+a, w=x(pc+t)/d (p-free):
       x or w is PRODUCTIVE                                        [distance 3]
  (B)  delta | t^2 signed, V1=(t, p(delta-t), p(t^2/delta-t)) Type II;
       the other vertex of a Type II fibre of V1 has a productive
       p-free coordinate                                           [distance 3]

A positive p-free z is PRODUCTIVE iff its fibre contains a positive vertex;
for t<z<=2t: some D|z^2 with D = -z or D = -1/4 (mod 4z-p).
FOUND results carry explicit paths that are checked as exact identities.
FAIL (no depth<=3 escape) is only reported when every factorization used is
certified (primes < 2^64 by deterministic test, larger by a Pocklington chain).
"""
from __future__ import annotations

import argparse
import json
import sys
from fractions import Fraction
from math import gcd, isqrt, prod

from sympy import factorint, isprime, primerange

from pointwise_fibres import FibreOracle, checked_vertex


INTERVAL = 200_000


class Uncertified(RuntimeError):
    pass


# ---------------------------------------------------------------- primality
def pocklington(n: int, depth: int = 0) -> bool:
    """Prove n prime (n > 2^64) by the Pocklington criterion, recursively."""
    if n < 2**64:
        return isprime(n)
    if depth > 30:
        raise Uncertified("certificate recursion too deep")
    m = n - 1
    fac = factorint(m, limit=10**7)
    # use fully certified part F of n-1 with F > sqrt(n)
    F, used = 1, []
    for q, e in sorted(fac.items()):
        if q < 2**64 and isprime(q) or (q >= 2**64 and isprime(q) and q < m and pocklington(q, depth + 1)):
            F *= q**e
            used.append(q)
    if F * F <= n:
        fac = factorint(m)  # try harder
        F, used = 1, []
        for q, e in sorted(fac.items()):
            if (q < 2**64 and isprime(q)) or (isprime(q) and pocklington(q, depth + 1)):
                F *= q**e
                used.append(q)
        if F * F <= n:
            raise Uncertified(f"could not certify {n}")
    for q in used:
        for a in range(2, 200):
            if pow(a, m, n) != 1:
                return False
            if gcd(pow(a, m // q, n) - 1, n) == 1:
                break
        else:
            raise Uncertified(f"no Pocklington witness for {n}")
    return True


class Factorizer:
    def __init__(self, known=(2, 3)):
        self.known = set(known)
        self.cache: dict[int, dict[int, int]] = {}

    def add_known(self, *ps):
        for q in ps:
            self.known.add(q)

    def __call__(self, n: int) -> dict[int, int]:
        n = abs(n)
        if n == 0:
            raise ValueError("factor(0)")
        if n in self.cache:
            return self.cache[n]
        orig, out = n, {}
        for q in sorted(self.known):
            if n % q == 0:
                e = 0
                while n % q == 0:
                    n //= q
                    e += 1
                out[q] = e
        if n > 1:
            for q, e in factorint(n).items():
                if not (isprime(q) and (q < 2**64 or pocklington(q))):
                    raise Uncertified(f"factor {q} not certified")
                out[q] = out.get(q, 0) + e
                self.known.add(q)
        assert prod(q**e for q, e in out.items()) == orig
        self.cache[orig] = out
        return out


def sq_divisors(fac: dict[int, int]) -> list[int]:
    ds = [1]
    for q, e in fac.items():
        ds = [d * q**k for d in ds for k in range(2 * e + 1)]
    return ds


def divisors_of(fac: dict[int, int]) -> list[int]:
    ds = [1]
    for q, e in fac.items():
        ds = [d * q**k for d in ds for k in range(e + 1)]
    return ds


def vertex_ok(p, v):
    return checked_vertex(p, v)


# ---------------------------------------------------------------- the test
class Depth3:
    def __init__(self, p: int, factor: Factorizer | None = None, t_factors=None):
        self.p, self.t = p, (p - 1) // 4
        self.F = factor or Factorizer()
        self.F.add_known(p)
        t = self.t
        self.tf = t_factors or self.F(t)
        self.F.add_known(*self.tf.keys())
        self.T2 = sorted(sq_divisors(self.tf))  # positive divisors of t^2

    # positive vertices containing the positive p-free denominator z
    def productive(self, z: int):
        p, t = self.p, self.t
        if z <= t or z % p == 0:
            return None
        q = 4 * z - p
        if z > 2 * t:
            # interval (10): at most two candidates x in [1,2t]
            R = Fraction(4, p) - Fraction(1, z)
            low = 1 / (R + Fraction(1, p * t))
            lo = -((-low.numerator) // low.denominator)
            up = 1 / (R - Fraction(1, p * (3 * t + 1)))
            hi = up.numerator // up.denominator
            for x in range(max(lo, 1), hi + 1):
                den = 4 * z * x - p * (z + x)
                if den and (p * z * x) % den == 0:
                    w = p * z * x // den
                    if w > 0:
                        return vertex_ok(p, (z, x, w))
            return None
        zf = self.F(z)
        inv4 = pow(4, -1, q) if q > 1 else 0
        for D in sq_divisors(zf):
            if q == 1 or (D + z) % q == 0:
                # (z, p(z+D)/q, p(z+z^2/D)/q)  Type II positive
                return vertex_ok(p, (z, p * (z + D) // q, p * (z + z * z // D) // q))
            if (D - (-inv4)) % q == 0:
                # D = -1/4: (z, (pz + p^2 z^2/(pD)... ) use general formula
                y = (p * p * D + p * z) // q
                w = (z * z // D + p * z) // q
                return vertex_ok(p, (z, y, w))
        return None

    def crit9(self, all_hits=False):
        p, t = self.p, self.t
        hits = []
        for h in self.T2:
            M = p * h - t
            K = 4 * h - 1
            bound = (4 * t * t + h) // K
            if bound <= INTERVAL:
                # positive bucket vertices are exactly (a,h), 1<=a<=t, e=(4a-1)h-a | (t+a)^2
                for a in range(1, min(t, bound) + 1):
                    e = (4 * a - 1) * h - a
                    if ((t + a) ** 2) % e == 0:
                        x = t + a
                        P = vertex_ok(p, (x, p * M, x * M // e))
                        V1 = vertex_ok(p, (t, p * M, -t * M // h))
                        hits.append({"family": "9", "h": h, "a": a, "path": [V1, P]})
                        break
                if hits and not all_hits:
                    return hits
                continue
            Mf = self.F(M)
            for D in sq_divisors(Mf):
                if (D + h) % K == 0:
                    y, z = (M + D) // K, (M + M * M // D) // K
                    P = vertex_ok(p, (p * M, y, z))
                    V1 = vertex_ok(p, (t, p * M, -t * M // h))
                    hits.append({"family": "9", "h": h, "path": [V1, P]})
                    break
            if hits and not all_hits:
                return hits
        return hits

    def famA(self, all_hits=False):
        p, t = self.p, self.t
        hits = []
        for c in self.T2:
            M = p * c + t
            K = 4 * c + 1
            V1 = vertex_ok(p, (t, -p * M, -t * M // c))
            bound = (4 * t * t + c) // K
            if bound <= INTERVAL:
                # all bucket vertices with a>=1 have a representative 1<=a<=t with
                # E=(4c+1)a-c | (t+a)^2 and E <= (t+a)^2 <= 4t^2
                cands = [((4 * c + 1) * a - c, a) for a in range(1, min(t, bound) + 1)
                         if ((t + a) ** 2) % ((4 * c + 1) * a - c) == 0]
            else:
                cands = [(d, (d + c) // K) for d in sorted(sq_divisors(self.F(M))) if (d + c) % K == 0]
            for d, a in cands:
                x = t + a
                if x % p == 0:
                    continue
                w = x * M // d
                V2 = vertex_ok(p, (x, -p * M, w))
                for z in (x, w):
                    P = self.productive(z)
                    if P:
                        hits.append({"family": "A", "c": c, "d": d, "a": a, "via": "x" if z == x else "w",
                                     "path": [V1, V2, P]})
                        if not all_hits:
                            return hits
        return hits

    def type2_fibre(self, m: int):
        """All vertices (x, pm, pn) -- two-candidate construction of SIGNED_REFACTOR 5."""
        p, t = self.p, self.t
        k = 4 * m - 1
        out = set()
        n = (m * pow(k, -1, p)) % p
        if n > 2 * t:
            n -= p
        den = 4 * m * n - m - n
        if n and den and (p * m * n) % den == 0:
            out.add(vertex_ok(p, (p * m * n // den, p * m, p * n)))
        center = Fraction(p * m, k)
        x = (2 * center.numerator + center.denominator) // (2 * center.denominator)
        D = k * x - p * m
        if D and (m * m) % D == 0 and x:
            out.add(vertex_ok(p, (x, p * m, p * (m * x // D))))
        return out

    def famB(self, all_hits=False, validate=False):
        p, t = self.p, self.t
        hits = []
        seen = set()
        for dd in self.T2:
            for delta in (dd, -dd):
                if delta in (t, -t):
                    continue
                m, n = delta - t, t * t // delta - t
                V1 = vertex_ok(p, (t, p * m, p * n))
                if V1 in seen:
                    continue
                seen.add(V1)
                for mm in (m, n):
                    for V2 in self.type2_fibre(mm):
                        if V2 == V1:
                            continue
                        assert V2[0] <= 0
                        pfree = [z for z in V2 if z % p]
                        assert len(pfree) == 1
                        P = self.productive(pfree[0]) if pfree[0] > 0 else None
                        if P:
                            hits.append({"family": "B", "delta": delta, "path": [V1, V2, P]})
                            if not all_hits:
                                return hits
        return hits

    def run(self, all_hits=False):
        r9 = self.crit9(all_hits)
        if r9 and not all_hits:
            return {"p": self.p, "dist": 2, "hits": r9}
        rA = self.famA(all_hits)
        rB = self.famB(all_hits) if (all_hits or not rA) else []
        hits = r9 + rA + rB
        dist = 2 if r9 else (3 if (rA or rB) else ">=4")
        return {"p": self.p, "dist": dist, "hits": hits}


def check_path(p, path):
    t = (p - 1) // 4
    seed = tuple(sorted((t, -2 * p * t, -2 * p * t)))
    full = [seed] + [tuple(v) for v in path]
    for v in full:
        assert sum(Fraction(1, z) for z in v) == Fraction(4, p)
    for u, v in zip(full, full[1:]):
        assert set(u) & set(v), (u, v)
    assert min(full[-1]) > 0 and all(min(v) < 0 for v in full[:-1])
    return len(full) - 1


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("ps", nargs="*", type=int)
    ap.add_argument("--range", nargs=2, type=int)
    ap.add_argument("--all", action="store_true")
    args = ap.parse_args()
    ps = list(args.ps)
    if args.range:
        ps += [q for q in primerange(*args.range) if q % 4 == 1]
    for p in ps:
        try:
            r = Depth3(p).run(args.all)
        except Uncertified as e:
            print(json.dumps({"p": p, "status": "UNKNOWN", "reason": str(e)}))
            continue
        for h in r["hits"]:
            check_path(p, h["path"])
        print(json.dumps(r, default=str), flush=True)


if __name__ == "__main__":
    main()
