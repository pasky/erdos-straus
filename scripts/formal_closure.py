"""Formal (Hypothesis-H) closure of the seed component for t=6q, p=24q+1 (DEPTH3.md §6).

uv run python scripts/formal_closure.py [--rounds K] [--B 200] [--seed 1]

A FORMAL PRIME is a primitive irreducible g in Z[X] with positive leading
coefficient.  A generic base point q* is modelled by a concrete huge integer
qt, chosen by CRT so that 24qt+1 is a nonzero square and qt a unit modulo every
prime ell<=B.  C_g = prod_{ell<=B} ell^{v_ell(g(qt))}, and r_g = g(q)/C_g plays
the role of a (large) prime.  Primes ell>B are assumed not to divide any g(q*):
this is the root-avoidance clause of Lemma 1. It is checked a posteriori:
every constant that arises must be B-smooth.

A FORMAL INTEGER is  const * prod r_g^e  (const a nonzero integer).  Fibres
are enumerated exactly as in Lemma 3: reduce (4z-p)/(pz) formally, run over all
formal signed divisors D of s^2, factor D+s over Q, and keep formally integral
results.  Vertices are sorted triples of formal integers (sorted by value at qt).
Output per round: number of formal vertices, formal primes, max degree,
max coefficient height, max |const|.
"""
from __future__ import annotations

import argparse
import json
import random
import sys
from fractions import Fraction
from math import gcd, prod

from sympy import Poly, QQ, ZZ, factorint, primerange, symbols
from sympy.ntheory.modular import crt

X = symbols("X")


class Formal:
    def __init__(self, B=200, seed=1, bits=400, qt=None, extra_small=()):
        self.B = B
        self.small = sorted(set(primerange(2, B + 1)) | set(int(l) for l in extra_small))
        rng = random.Random(seed)
        mods, res = [], []
        self.E = {}
        self.smallset = set(self.small)
        self.maxval = {}
        self.aux_keys = set()
        self.r_primes = set()
        self.r_root_budget = {}
        self.flags = []
        for ell in self.small:
            # only the residue class matters for choosing qt (the final class modulus
            # uses E_ell > max observed valuation), so a small precision suffices
            E = 12 if ell <= 7 else (6 if ell <= 50 else 1)
            if ell in (2, 3):
                r = rng.randrange(1, ell**E)
                while r % ell == 0:
                    r = rng.randrange(1, ell**E)
            else:
                while True:
                    r = rng.randrange(1, ell**E)
                    if r % ell and pow((24 * r + 1) % ell, (ell - 1) // 2, ell) == 1:
                        break
            self.E[ell] = E
            mods.append(ell**E)
            res.append(r)
        q0 = int(crt(mods, res)[0])
        M = prod(mods)
        self.qt = q0 + M * rng.getrandbits(bits) if qt is None else qt
        self.primes = {}  # key -> (Poly, C, rval)
        self.P = self.key(Poly(24 * X + 1, X, domain=ZZ))
        self.Xk = self.key(Poly(X, X, domain=ZZ))
        self.nonsmooth = 0

    # ---------- formal primes
    def key(self, g: Poly):
        g = Poly(g, X, domain=ZZ)
        c, g = g.primitive()
        if g.LC() < 0:
            g = -g
        k = tuple(int(a) for a in g.all_coeffs())
        if k not in self.primes:
            v = int(g.eval(self.qt))
            assert v > 0
            C = 1
            for ell in self.small:
                n = 0
                while v % ell == 0:
                    v //= ell
                    C *= ell
                    n += 1
                # q* := qt at every ell <= B; the final class modulus uses E_ell > max valuation
                self.maxval[ell] = max(self.maxval.get(ell, 0), n)
            self.primes[k] = (g, C, v)
        return k

    # ---------- formal integers: (const, tuple(sorted((key,e))))
    def value(self, F):
        c, ex = F
        return c * prod(self.primes[k][2] ** e for k, e in ex)

    def poly(self, F):
        c, ex = F
        out = Poly(c, X, domain=QQ)
        for k, e in ex:
            g, C, _ = self.primes[k]
            out = out * (Poly(g, X, domain=QQ) * QQ(1, C)) ** e
        return out

    def from_poly(self, f: Poly):
        """Formal factorization of a nonzero polynomial taking integer values at admissible q."""
        f = Poly(f, X, domain=QQ)
        num = f.eval(self.qt)
        cont, facs = Poly(f, X, domain=QQ).factor_list()
        ex = {}
        for g, e in facs:
            g = Poly(g, X, domain=QQ)
            # clear denominators and make primitive in Z[X]
            coeffs = [Fraction(int(a.numerator), int(a.denominator)) for a in g.all_coeffs()]
            L = 1
            for a in coeffs:
                L = L * a.denominator // gcd(L, a.denominator)
            gz = Poly([int(a * L) for a in coeffs], X, domain=ZZ)
            if gz.degree() == 0:
                continue
            k = self.key(gz)
            ex[k] = ex.get(k, 0) + e
        # constant = f(qt) / prod r^e  (must be a nonzero integer)
        r = prod(self.primes[k][2] ** e for k, e in ex.items())
        val = Fraction(int(num.numerator), int(num.denominator))
        c = val / r
        if c.denominator != 1:
            return None  # not integral at admissible q
        c = int(c)
        # B-smoothness check of the constant (root-avoidance consistency)
        cc = abs(c)
        for ell in self.small:
            while cc % ell == 0:
                cc //= ell
        if cc != 1:
            self.nonsmooth += 1
        return (c, tuple(sorted(ex.items())))

    def accidental(self, f, Lr):
        """numeric integrality passed but formal failed: is a prime of const(r) hidden in an rval?"""
        _, facs = Poly(f, X, domain=QQ).factor_list()
        for g, e in facs:
            coeffs = [Fraction(int(a.numerator), int(a.denominator)) for a in Poly(g, X, domain=QQ).all_coeffs()]
            L = 1
            for a in coeffs:
                L = L * a.denominator // gcd(L, a.denominator)
            gz = Poly([int(a * L) for a in coeffs], X, domain=ZZ)
            if gz.degree() == 0:
                continue
            k = self.key(gz)
            if any(self.primes[k][2] % ell == 0 for ell in Lr):
                return True
        return False

    @staticmethod
    def mul(F, G):
        ex = dict(F[1])
        for k, e in G[1]:
            ex[k] = ex.get(k, 0) + e
        return (F[0] * G[0], tuple(sorted((k, e) for k, e in ex.items() if e)))

    @staticmethod
    def div(F, G):
        if F[0] % G[0]:
            return None
        ex = dict(F[1])
        for k, e in G[1]:
            ex[k] = ex.get(k, 0) - e
            if ex[k] < 0:
                return None
        return (F[0] // G[0], tuple(sorted((k, e) for k, e in ex.items() if e)))

    def gcdF(self, F, G):
        a, b = dict(F[1]), dict(G[1])
        ex = tuple(sorted((k, min(e, b[k])) for k, e in a.items() if k in b and min(e, b[k]) > 0))
        return (gcd(F[0], G[0]), ex)

    # ---------- fibre
    def fibre(self, Z):
        p = (1, ((self.P, 1),))
        N = self.from_poly(4 * self.poly(Z) - Poly(24 * X + 1, X, domain=QQ))
        assert N is not None
        # the formal primes of 4z-p must also be prime at admissible q (they decide integrality)
        self.aux_keys.update(k for k, e in N[1])
        den = self.mul(p, Z)
        g = self.gcdF(N, den)
        r, s = self.div(N, g), self.div(den, g)
        if s[0] < 0:
            r, s = (-r[0], r[1]), (-s[0], s[1])
        # primes > B of const(r): integrality at such ell depends on q mod ell;
        # the model is valid only if q* = qt there and no relevant rval is divisible by ell
        Lr = [ell for ell in factorint(abs(r[0])) if ell not in self.smallset]
        self.r_primes.update(Lr)
        if Lr:
            # generic-residue bound: every candidate D gives a polynomial D+s of degree
            # <= 2*deg(s); record (#candidates * degree) per prime of const(r)
            ncand = 2 * prod(2 * e + 1 for e in factorint(s[0]).values()) * prod(2 * e + 1 for k, e in s[1])
            dg = 2 * max(1, self.poly(s).degree())
            for ell in Lr:
                self.r_root_budget[ell] = self.r_root_budget.get(ell, 0) + ncand * dg
        # divisors of s^2: D = sign * c * E, c | const(s)^2, E a formal monomial
        cs2 = s[0] * s[0]
        cf = factorint(s[0])
        edivs = [()]
        for k, e in s[1]:
            edivs = [ed + ((k, j),) for ed in edivs for j in range(2 * e + 1)]
        s2 = self.mul(s, s)
        sp = self.poly(s)
        sv, rv = self.value(s), self.value(r)
        R = abs(rv)
        out = set()
        cdivs = None
        for ed in edivs:
            E = (1, tuple(sorted((k, j) for k, j in ed if j)))
            Ev = self.value(E)
            cands = []
            if R > 2 * cs2 and gcd(Ev, R) == 1:
                # D = -s (mod r) pins sign*c to one residue: O(1) instead of enumerating c
                u = (-sv * pow(Ev, -1, R)) % R
                if u and u <= cs2 and cs2 % u == 0:
                    cands.append(u)
                if R - u <= cs2 and cs2 % (R - u) == 0:
                    cands.append(-(R - u))
            else:
                if cdivs is None:
                    cdivs = [1]
                    for ell, e in cf.items():
                        cdivs = [d * ell**j for d in cdivs for j in range(2 * e + 1)]
                cands = [sg * c for c in cdivs for sg in (1, -1)]
            for sc in cands:
                D = (sc, E[1])
                Dv = sc * Ev
                if Dv == -sv or (Dv + sv) % rv or (sv * sv // Dv + sv) % rv:
                    continue
                Dc = self.div(s2, D)
                ys = []
                for DD in (D, Dc):
                    f = self.poly(DD) + sp
                    if f.is_zero:
                        break
                    FF = self.from_poly(f)
                    y = None if FF is None else self.div(FF, r)
                    if y is None:
                        if Lr and self.accidental(f, Lr):
                            self.flags.append((str(self.poly(Z)), [int(l) for l in Lr]))
                        break
                    ys.append(y)
                if len(ys) == 2:
                    out.add(tuple(sorted([Z, ys[0], ys[1]], key=self.value)))
        return out

    def seed(self):
        t = (6, ((self.Xk, 1),))
        m = (-12, ((self.Xk, 1), (self.P, 1)))
        return tuple(sorted([t, m, m], key=self.value))

    def anchors(self, V):
        """distinct formal denominators of degree 1 with 0 < leading coeff <= 12 (the p-free anchors)"""
        out = {}
        for v in V:
            for z in v:
                if self.kind(z) == "anchor":
                    f = self.poly(z)
                    lc = f.LC() if f.degree() == 1 else 0
                    out[z] = (Fraction(str(lc)), Fraction(str(f.TC())))
        return out

    def kind(self, z):
        """'pdiv' | 'anchor' (positive p-free, <=2t for large q) | 'dead' (negative p-free
        or p-free >2t: fibre is {itself}, SIGNED_REFACTOR 5 / WINDMILL Thm 7)"""
        if any(k == self.P for k, e in z[1]):
            return "pdiv"
        f = self.poly(z)
        lc = f.LC()
        if lc < 0:
            return "dead"
        if f.degree() >= 2 or (f.degree() == 1 and (lc > 12 or (lc == 12 and f.TC() > 0))):
            return "dead"
        return "anchor"

    def stats(self, V):
        deg = int(max((self.primes[k][0].degree() for k in self.primes), default=0))
        h = int(max(max(abs(int(a)) for a in self.primes[k][0].all_coeffs()) for k in self.primes))
        cmax = max(abs(z[0]) for v in V for z in v)
        A = self.anchors(V)
        betas = sorted(abs(b) for a, b in A.values())
        alphas = sorted(set(str(a) for a, b in A.values()), key=lambda u: Fraction(u))
        return {"anchors": len(A), "anchor_max_|beta|": str(betas[-1]) if betas else None,
                "anchor_median_|beta|": str(betas[len(betas)//2]) if betas else None,
                "anchor_alphas": alphas[:40],
                "vertices": len(V), "formal_primes": len(self.primes), "max_deg": deg,
                "max_coeff_height": h, "max_const": cmax, "nonsmooth_consts": self.nonsmooth}


def check_vertex(F, v):
    """exact identity at q=qt (the formal identity holds for all q iff for infinitely many)"""
    p = 24 * F.qt + 1
    vals = [F.value(z) for z in v]
    assert all(vals) and sum(Fraction(1, x) for x in vals) == Fraction(4, p), v
    return vals


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--rounds", type=int, default=6)
    ap.add_argument("--B", type=int, default=200)
    ap.add_argument("--seed", type=int, default=1)
    ap.add_argument("--max-vertices", type=int, default=200000)
    ap.add_argument("--prune", action="store_true",
                    help="skip fibres of negative p-free and p-free >2t denominators (at most one vertex)")
    a = ap.parse_args()
    F = Formal(a.B, a.seed)
    V = {F.seed()}
    done = set()
    frontier = [F.seed()]
    for rnd in range(1, a.rounds + 1):
        new = []
        for v in frontier:
            for z in v:
                if z in done:
                    continue
                done.add(z)
                if a.prune and F.kind(z) == "dead":
                    continue
                for w in F.fibre(z):
                    if w not in V:
                        V.add(w)
                        new.append(w)
        for w in new:
            assert any(F.kind(z) == "anchor" for z in w), ("no anchor", w)
            vals = check_vertex(F, w)
            assert not all(x > 0 for x in vals), ("POSITIVE formal vertex", w)
        frontier = new
        st = F.stats(V)
        st.update(round=rnd, new=len(new), expanded_denominators=len(done))
        print(json.dumps(st), flush=True)
        if not new:
            print("STABILIZED", flush=True)
            break
        if len(V) > a.max_vertices:
            print("BUDGET", flush=True)
            break


if __name__ == "__main__":
    main()
