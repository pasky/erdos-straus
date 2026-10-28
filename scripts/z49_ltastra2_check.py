"""Exact checks of the new z49 identities; existing engines handle old controls.

No dense CRT arrays: enumerate only one small fibre at a time. Run with
ulimit -v 8000000; timeout 180 uv run python scripts/z49_ltastra2_check.py.
"""
from fractions import Fraction as F
from itertools import product
from math import gcd, log
from pathlib import Path
import json

from sympy import divisors, isprime, jacobi_symbol
from mordell_lib import cls_modulus_residues, solve
from s8_check_b1 import line_counts_k

OUT = Path(__file__).resolve().parents[1] / "data/z49_ltastra2"


def menu(Q):
    cells = []
    for m0 in divisors(Q // 4):
        m = int(m0)
        for u0 in divisors(m):
            u = int(u0)
            v = m // u
            if gcd(u, v) == 1 and (u + v) % 2:
                cells.append((4*m, (-u-v) % (4*m)))
            if v >= 3 and v % 4 == 3 and gcd(u, v) == 1:
                cells.append((4*m, (-4*u-v) % (4*m)))
    return cells


def check_maps():
    cases = 0
    for u in range(1, 25):
        for v in range(1, 25):
            if gcd(u, v) != 1:
                continue
            if (u+v) % 2:
                q, residues = cls_modulus_residues("II1", (u, v, u+v))
                assert q == 4*u*v and residues == [(-u-v) % q]
                for C in (1, 2, 5):
                    n = q*C-u-v
                    xyz = solve("II1", (u, v, u+v), n)
                    assert sum((F(1, x) for x in xyz), F()) == F(4, n)
                    assert sorted(xyz) == sorted((u*v*C, n*v*C, n*u*C))
                    cases += 1
            if v >= 3 and v % 4 == 3:
                q, residues = cls_modulus_residues("II3", (1, u, v))
                assert q == 4*u*v and residues == [(-4*u-v) % q]
                for C in (1, 2, 5):
                    n = q*C-4*u-v
                    xyz = solve("II3", (1, u, v), n)
                    assert sum((F(1, x) for x in xyz), F()) == F(4, n)
                    assert sorted(xyz) == sorted((u*(C*v-1), n*C*u,
                                                 n*C*u*(C*v-1)))
                    cases += 1
    return cases


def check_fibres():
    rows = []
    for r in (7, 11, 19, 23, 31, 43):
        for e in (1, 2):
            Q = 24*r**e
            cells = menu(Q)
            fibre = [a for a in range(1, Q, 24)
                     if gcd(a, Q) == 1 and jacobi_symbol(a, r) == -1]
            counts = [sum(a % q == b for q, b in cells) for a in fibre]
            mu = F(sum(counts), len(fibre))
            # Independent, one-cell-at-a-time square image projection.
            mean_by_images = F()
            for q, a in cells:
                image = {x*x % q for x in range(1, q) if gcd(x, q) == 1}
                g = fibre[0]*pow(a, -1, q) % q
                if g in image:
                    mean_by_images += F(1, len(image))
            assert mu == mean_by_images, (r, e, mu, mean_by_images)
            assert mu >= F(4, r-1)
            # A conditional average is not asserted to be a minorant.
            if min(counts) == 0:
                assert min(F(x)-mu for x in counts) == -mu
                assert max(F(x)-mu for x in counts) > 0
            rows.append({"r": r, "e": e, "Q": Q, "size": len(fibre),
                         "mean": str(mu), "minimum": min(counts),
                         "argmin": fibre[counts.index(min(counts))]})
    # Long prime-power cells: algebraic genus permission, independent Euler tests.
    power_checks = 0
    for r in (7, 11, 19, 31):
        for k in (1, 3, 5):
            q, a = 8*r**k, -1-2*r**k
            assert a % 8 == 1 and jacobi_symbol(a, r) == -1
            # Every possible negative sign modulo r is in the same square coset.
            for z in range(1, r):
                if jacobi_symbol(z, r) == -1:
                    ratio = z * pow(a, -1, r) % r
                    assert pow(ratio, (r-1)//2, r) == 1
                    power_checks += 1
    return rows, power_checks


def check_moments():
    cases = 0
    for N in range(1, 4):
        for m in (F(2), F(7, 2), F(5)):
            top = -(-m.numerator // m.denominator)
            for k in (1, 2, 3):
                for C in (F(1, 4), F(1), F(2)):
                    budget = N*(C*k*m)**k
                    for eta in (F(0), F(1, 3), F(1, 2)):
                        cutoff = eta*m
                        floor_cutoff = cutoff.numerator // cutoff.denominator
                        d = m-floor_cutoff
                        E = budget/d**(2*k)
                        largest_bad = 0
                        for vector in product(range(top+1), repeat=N):
                            moment = sum(max(m-x, 0)**(2*k) for x in vector)
                            if moment <= budget:
                                bad = sum(x <= cutoff for x in vector)
                                assert bad <= E
                                largest_bad = max(largest_bad, bad)
                        assert largest_bad == min(N, E.numerator//E.denominator)
                        cases += 1
    # Numerical evaluation of the subleading boundary, not asymptotic proof.
    boundary = []
    for L in (100., 1000., 10000., 1000000.):
        c, C, eta, delta = .1, 1., .25, 1.
        t = L-log(L)
        A = (1-eta)**2*c*L*L/C
        h = log(L)+log(log(L))+log((1-eta)**2*c/C)
        below = L/(h+delta)
        above = L/(h-delta)
        logE_below = t + below*log(below/A)
        logE_above = t + above*log(above/A)
        assert logE_below > 0 and logE_above < 0
        boundary.append({"L": L, "logE_weaker": logE_below,
                         "logE_stronger": logE_above})
    return cases, boundary


def check_perturbations():
    # Arbitrary rational weights test the norm bounds more strongly than log n.
    N = 300
    base = {n for n in range(2, N+1) if isprime(n)}
    extra = {49, 121, 169, 289}
    D = sum(F(n, N) for n in extra)
    l1 = F()
    l2 = F()
    for q in range(1, 61):
        delta = {}
        for n in extra:
            a = n % q
            if gcd(a, q) == 1:
                delta[a] = delta.get(a, F())+F(n, N)
        l1 += max(delta.values(), default=F())
        l2 += sum(x*x for x in delta.values())
        assert l1 <= q*D and l2 <= q*D*D
    # Union-bound audit for nonconstant affine forms of varying slopes.
    tuple_cases = 0
    for forms in (((1, 0), (1, 2)), ((2, 1), (3, 2), (1, 0)),
                  ((1, 0), (1, 72))):
        def count(S):
            return sum(all(a*t+b in S for a, b in forms)
                       for t in range(1, N+1)
                       if all(1 <= a*t+b <= N for a, b in forms))
        assert abs(count(base | extra)-count(base)) <= len(forms)*len(extra)
        tuple_cases += 1
    return {"weighted_l1": str(l1), "weighted_l2_squared": str(l2),
            "D": str(D), "tuple_cases": tuple_cases}


def controls():
    # Existing general-numerator engine, not a duplicated ES enumerator.
    out = {"squares": {}, "numerator8": {}}
    for m in (3, 5, 7, 11, 17, 31, 51):
        counts = line_counts_k(m*m, 4)
        assert counts == (0, 0)
        out["squares"][m*m] = counts
    for n in (17, 241):
        counts = line_counts_k(n, 8)
        assert counts == (0, 0)
        out["numerator8"][n] = counts
    return out


def main():
    OUT.mkdir(parents=True, exist_ok=True)
    report = {"ET_identity_checks": check_maps()}
    report["finite_fibres"], report["prime_power_checks"] = check_fibres()
    report["moment_exhaustions"], report["moment_boundary"] = check_moments()
    report["perturbations"] = check_perturbations()
    report["controls"] = controls()
    (OUT / "checks.json").write_text(json.dumps(report, indent=2)+"\n")
    print(json.dumps(report, indent=2))


if __name__ == "__main__":
    main()
