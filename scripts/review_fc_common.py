"""Independent re-implementation (hostile review of FORMAL_CLOSURE.md).

Does NOT import scripts/formal2*.py or scripts/formal_closure*.py.  Reads only the
JSON data in data/formal_closure/.

Conventions (from FORMAL_CLOSURE.md §1 and the JSON layout):
  * a polynomial key is a tuple of integer coefficients, low degree first;
  * a formal integer is (c, ((key, e), ...)) meaning  c * prod (g / C_g)^e ;
  * certificate.json.gz: q0_mod[ell] = [residue, E_ell];  S entries
    [coeffs, C_g, is_aux, is_entry]; vertices = triples of formal integers.
"""
from __future__ import annotations

import gzip
import json
import sys
from fractions import Fraction
from math import gcd, prod

import flint

sys.set_int_max_str_digits(0)

DATA = "data/formal_closure/"
PKEY = (1, 24)
XKEY = (0, 1)


def load():
    cert = json.load(gzip.open(DATA + "certificate.json.gz"))
    clo = json.load(gzip.open(DATA + "closure_final.json.gz"))
    lamf = json.load(open(DATA + "lam_final.json"))
    return cert, clo, lamf


def crt(pairs):
    """pairs: list of (residue, modulus) with pairwise coprime moduli; product tree."""
    items = [(r % m, m) for r, m in pairs]
    while len(items) > 1:
        nxt = []
        for i in range(0, len(items) - 1, 2):
            (r1, m1), (r2, m2) = items[i], items[i + 1]
            # x = r1 + m1*t,  m1*t = r2-r1 mod m2
            t = ((r2 - r1) * pow(m1, -1, m2)) % m2
            nxt.append((r1 + m1 * t, m1 * m2))
        if len(items) % 2:
            nxt.append(items[-1])
        items = nxt
    return items[0]


def canon_formal(F):
    c, ex = F
    return (int(c), tuple(sorted((tuple(int(a) for a in k), int(e)) for k, e in ex)))


def canon_vertex(v):
    return tuple(sorted(canon_formal(F) for F in v))


def vval(n, ell):
    n = abs(n)
    if n == 0:
        return 10**9
    k = 0
    while n % ell == 0:
        n //= ell
        k += 1
    return k


class Model:
    """q0 (from q0_mod), E, Lambda, S with C_g (recomputed), poly objects."""

    def __init__(self, cert, recompute_C=True):
        self.E = {int(l): int(k) for l, (r, k) in cert["q0_mod"].items()}
        self.res = {int(l): int(r) % int(l) ** int(k) for l, (r, k) in cert["q0_mod"].items()}
        self.lam = sorted(self.E)
        self.lamset = set(self.lam)
        self.lamprod = prod(self.lam)
        self.q0, self.M = crt([(self.res[l], l ** self.E[l]) for l in self.lam])
        self.poly = {}
        self.C = {}
        self.cert_C = {}
        self.flags = {}
        for coeffs, Cg, is_aux, is_entry in cert["S"]:
            key = tuple(int(a) for a in coeffs)
            self.cert_C[key] = int(Cg)
            self.flags[key] = (bool(is_aux), bool(is_entry))
            self.poly[key] = flint.fmpz_poly(list(key))
        self._qmods = None

    def qmod(self, ell):
        if self._qmods is None:
            self._qmods = {l: self.q0 % (l ** self.E[l]) for l in self.lam}
        return self._qmods[ell]

    def lam_part(self, key_or_poly):
        """C_h = prod ell^{v_ell(h(q0))} over Lambda, together with a flag that
        v_ell(h(q0)) < E_ell for every ell (needed for C_h to be q-independent)."""
        h = key_or_poly if isinstance(key_or_poly, flint.fmpz_poly) else flint.fmpz_poly(list(key_or_poly))
        v = int(h(self.q0))
        assert v != 0
        G = gcd(v, self.lamprod)
        C = 1
        ok = True
        if G > 1:
            for ell in self.lam:
                if G % ell == 0:
                    k = vval(v, ell)
                    if k >= self.E[ell]:
                        ok = False
                    C *= ell ** k
        return C, ok

    def Cof(self, key):
        if key not in self.C:
            C, ok = self.lam_part(key)
            if not ok:
                raise ValueError(("precision too low for C_g", key))
            self.C[key] = C
        return self.C[key]

    def formal_poly(self, F):
        """fmpq_poly of a formal integer."""
        c, ex = F
        num = flint.fmpz_poly([int(c)])
        den = 1
        for k, e in ex:
            num *= flint.fmpz_poly(list(k)) ** e
            den *= self.Cof(tuple(k)) ** e
        return flint.fmpq_poly(num) / den
