"""Verify a saved sterile-component certificate (exact; finite).

PYTHONPATH=scripts uv run --with python-flint python scripts/sterile_certificate_check.py CERT.json.gz [...]

A certificate is {"p":..., "vertices": [[x,y,z],...]} (decimal integers);
with "kind": "seed" it certifies the entire seed component instead (positive
vertices allowed, the seed (-2pt,-2pt,t) must belong to it).
Checks, for the claimed vertex set S:
  (1) every triple is a signed ES solution 4/p = 1/x+1/y+1/z, nonzero,
      sorted, and NOT all-positive;
  (2) S is connected under 'share a denominator';
  (3) S is closed: for every denominator z occurring in S, the complete
      fibre of z is contained in S.  Fibres are recomputed by two methods
      where possible:
        - p-free z in [1,2t]: the incidence equation of SIGNED_REFACTOR §3
          (f | p z^2, f = -z mod 4z-p), enumerated here from scratch with
          FLINT-proved factors, AND the divisor-fibre method of
          pointwise_fibres_big; results must agree;
        - Type I p-divisible z: C interval scan (if available) AND the
          meet-in-the-middle divisor method; results must agree;
        - Type II / p-free outside [1,2t]: the factorization-free constant
          candidate tests of pointwise_fibres (SIGNED_REFACTOR §5).
(1)-(3) imply S is an entire connected component without positive vertex.
"""
import gzip, json, sys
from collections import deque
from math import prod

import flint

from pointwise_fibres_big import BigFibreOracle


def proved_factor(n):
    out = {}
    for ell, e in flint.fmpz(n).factor():
        ell = int(ell)
        assert flint.fmpz(ell).is_prime() == 1
        out[ell] = int(e)
    assert prod(l**e for l, e in out.items()) == n
    return out


def incidence_fibre(p, x):
    """All vertices containing the p-free denominator x (1<=x<=2t) via §3."""
    q = 4 * x - p
    fac = proved_factor(x) if x > 1 else {}
    ds = [1]
    for ell, e in fac.items():
        ds = [d * ell**j for d in ds for j in range(2 * e + 1)]
    out = set()
    for d in ds:
        for f in (d, -d, p * d, -p * d):
            if (x + f) % q:
                continue
            m = (x + f) // q
            if m == 0:
                continue
            assert (p * x * m) % f == 0
            z = p * x * m // f
            out.add(tuple(sorted((x, p * m, z))))
    return out


def check(cert):
    p = int(cert["p"])
    t = (p - 1) // 4
    S = {tuple(sorted(int(v) for v in vv)) for vv in cert["vertices"]}
    assert len(S) == len(cert["vertices"])
    seedcert = cert.get("kind") == "seed"
    for x, y, z in S:
        assert x and y and z and 4 * x * y * z == p * (x * y + x * z + y * z)
        assert seedcert or x < 0, "positive vertex in a claimed sterile component"
    if seedcert:
        assert (-2 * p * t, -2 * p * t, t) in S
    # connectivity
    buckets = {}
    for v in S:
        for z in set(v):
            buckets.setdefault(z, []).append(v)
    start = next(iter(S))
    seen, todo = {start}, deque([start])
    while todo:
        v = todo.popleft()
        for z in set(v):
            for w in buckets[z]:
                if w not in seen:
                    seen.add(w)
                    todo.append(w)
    assert seen == S, "not connected"
    # closure
    A = BigFibreOracle(p)                       # scan where possible
    B = BigFibreOracle(p, scan_budget=1)         # meet-in-the-middle only
    kinds = {"anchor": 0, "typeI": 0, "typeII": 0, "outer": 0}
    for z in buckets:
        if z % p == 0:
            if (4 * (z // p) - 1) % p == 0:
                fa, fb = A.fibre(z), B.fibre(z)
                assert fa == fb, ("Type I methods disagree", z)
                kinds["typeI"] += 1
            else:
                fa = A.fibre(z)
                kinds["typeII"] += 1
        elif 1 <= z <= 2 * t:
            fa = A.fibre(z)
            assert fa == incidence_fibre(p, z), ("anchor methods disagree", z)
            kinds["anchor"] += 1
        else:
            fa = A.fibre(z)
            kinds["outer"] += 1
        assert set(fa) <= S, ("fibre leaves S", z)
        assert set(buckets[z]) <= set(fa)
    return p, len(S), kinds


if __name__ == "__main__":
    for fn in sys.argv[1:]:
        cert = json.load(gzip.open(fn, "rt"))
        p, n, kinds = check(cert)
        what = "SEED component" if cert.get("kind") == "seed" else "sterile component"
        print(f"OK {fn}: p={p} {what} of {n} vertices, entire and closed; denominators {kinds}")
