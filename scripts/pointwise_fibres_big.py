"""Exact lazy signed-ES component search for large p (not a universal proof).

PYTHONPATH=scripts uv run --with python-flint python scripts/pointwise_fibres_big.py P X

Extends pointwise_fibres.FibreOracle beyond the 2^64 factorization range:

* fresh factorizations use FLINT (fmpz.factor); EVERY returned prime is
  re-proved with fmpz.is_prime() == 1 (FLINT's proving test; a return of -1
  or 0 raises IncompleteSearch), and the product is checked;
* a Type I p-divisible bucket (label 0, m = p*h - t) is enumerated by the
  exact interval scan a in [lo,hi], |(4h-1)a-h| <= (t+a)^2, in C
  (typei_scan.c) whenever that interval has at most `scan_budget` points,
  and otherwise by the divisor method of the parent class.

All other fibres are the parent's (constant-candidate Type II / outer p-free,
exact divisor fibres).  Budget failures raise IncompleteSearch, never a
sterile verdict.  The CLI explores the component of a vertex in the fibre
of denominator X and prints FOUND/STERILE/UNKNOWN as JSON.
"""
from __future__ import annotations

import argparse, ctypes, json, os, subprocess, sys
from math import prod

import flint

from pointwise_fibres import FibreOracle, IncompleteSearch, explore, require_integer

_LIB = None


def _lib():
    global _LIB
    if _LIB is None:
        here = os.path.dirname(os.path.abspath(__file__))
        so = f"/tmp/typei_scan_{os.getuid()}.so"
        src = os.path.join(here, "typei_scan.c")
        if not os.path.exists(so) or os.path.getmtime(so) < os.path.getmtime(src):
            subprocess.run(["gcc", "-O3", "-shared", "-fPIC", src, "-o", so + ".tmp"], check=True)
            os.replace(so + ".tmp", so)
        lib = ctypes.CDLL(so)
        lib.typei_scan.restype = ctypes.c_long
        lib.typei_scan.argtypes = [ctypes.c_int64, ctypes.c_uint64, ctypes.c_int64, ctypes.c_uint64,
                                   ctypes.c_int64, ctypes.c_int64, ctypes.POINTER(ctypes.c_int64), ctypes.c_long]
        _LIB = lib
    return _LIB


def _split(v: int):
    return v >> 64, v & ((1 << 64) - 1)


class BigFibreOracle(FibreOracle):
    def __init__(self, p: int, *, max_divisors=5_000_000, max_fibre=1_000_000,
                 scan_budget=300_000_000):
        p = require_integer(p, "p")
        if not (5 <= p < 2**61 and p % 4 == 1 and flint.fmpz(p).is_prime() == 1):
            raise ValueError("expected a proven prime p=1 mod 4 below 2^61")
        # parent validation uses sympy isprime only below 2^64; fine here.
        super().__init__(p, max_divisors=max_divisors, max_fibre=max_fibre,
                         interval_budget=1, factor_limit=1)
        self.scan_budget = scan_budget

    def factor(self, n: int) -> dict[int, int]:
        n = require_integer(n, "factorization input")
        if n < 1:
            raise ValueError("expected a positive integer to factor")
        original, factors = n, {}
        for ell in sorted(self._known_primes):
            e = 0
            while n % ell == 0:
                n //= ell
                e += 1
            if e:
                factors[ell] = e
        if n > 1:
            for ell, e in flint.fmpz(n).factor():
                ell = int(ell)
                if flint.fmpz(ell).is_prime() != 1:
                    raise IncompleteSearch("factor not proved prime")
                factors[ell] = factors.get(ell, 0) + int(e)
                self._known_primes.add(ell)
        if prod(ell**e for ell, e in factors.items()) != original:
            raise IncompleteSearch("factorization product mismatch")
        return factors

    def fibre(self, z: int):
        z = require_integer(z, "denominator")
        if z in self._cache:
            return self._cache[z]
        p, t = self.p, self.t
        if z % p == 0 and z % (p * p) and (4 * (z // p) - 1) % p == 0:
            m = z // p
            h = (m + t) // p
            bound = (4 * t * t + abs(h)) // abs(4 * h - 1)
            lo, hi = max(1 - t, -bound), min(t, bound)
            if hi - lo + 1 <= self.scan_budget and abs(h) < 2**100:
                cap = 1 << 16
                buf = (ctypes.c_int64 * cap)()
                n = _lib().typei_scan(*_split(t), *_split(h), lo, hi, buf, cap)
                if n < 0:
                    raise IncompleteSearch("scan output capacity exceeded")
                out = set()
                for i in range(n):
                    a = buf[i]
                    x, e = t + a, (4 * a - 1) * h - a
                    assert e and (x * x) % e == 0 and (x * m) % e == 0
                    self._add(out, (x, z, x * m // e))
                self._cache[z] = frozenset(out)
                return self._cache[z]
            out = frozenset(self._typei_divisors(m, h, lo, hi))
            self._cache[z] = out
            return out
        return super().fibre(z)

    def _typei_divisors(self, m, h, lo, hi):
        # Symmetric chart (SIGNED_REFACTOR.md §8): with H=4h-1, x=t+a,
        # e=aH-h, one has H*x = m+e and gcd(H,e)=1, so e | x^2 <=> e | m^2.
        # Enumerate positive divisors d <= E of m^2 (size-pruned DFS), both
        # signs e=+-d, and keep a=(e+h)/H in [lo,hi] with e | (t+a)^2.
        p, t = self.p, self.t
        H = 4 * h - 1
        E = 4 * t * t + 2 * abs(h) + abs(H)  # |e| <= (t+a)^2 <= 4t^2 on [lo,hi]
        factors = sorted(self.factor(abs(m)).items())
        out, count = set(), 0
        stack = [(0, 1)]
        while stack:
            i, d = stack.pop()
            if i == len(factors):
                count += 1
                if count > self.max_divisors:
                    raise IncompleteSearch("Type I pruned-divisor budget exceeded")
                for e in (d, -d):
                    if (e + h) % H:
                        continue
                    a = (e + h) // H
                    if not lo <= a <= hi:
                        continue
                    x = t + a
                    assert (4 * a - 1) * h - a == e
                    if (x * x) % e == 0:
                        self._add(out, (x, p * m, x * m // e))
                continue
            ell, k = factors[i]
            v = d
            for _ in range(2 * k + 1):
                if v > E:
                    break
                stack.append((i + 1, v))
                v *= ell
        return out


def hub_component(p: int, x: int, max_vertices=10**6, **kw):
    oracle = BigFibreOracle(p, **kw)
    F = oracle.fibre(x)
    if not F:
        return {"status": "EMPTY_FIBRE"}
    r = explore(oracle, sorted(F)[0], max_vertices=max_vertices)
    return {"status": r.status, "visited": r.visited, "expanded": r.expanded,
            "hubfibre": len(F), "path": r.path}


if __name__ == "__main__":
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument("p", type=int)
    ap.add_argument("x", type=int)
    ap.add_argument("--max-vertices", type=int, default=10**6)
    a = ap.parse_args()
    try:
        res = hub_component(a.p, a.x, a.max_vertices)
    except IncompleteSearch as error:
        print(json.dumps({"p": a.p, "x": a.x, "status": "UNKNOWN", "reason": str(error)}))
        raise SystemExit(2)
    res.update(p=a.p, x=a.x)
    print(json.dumps(res, default=str))
