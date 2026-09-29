"""Formal (Hypothesis-H) closure of the seed component, exact version (FORMAL_CLOSURE.md).

uv run --with python-flint python scripts/formal2.py --B 1500 --seed 1 --jobs 14 --dump OUT.json.gz

Model.  LAM = primes <= B ("model primes").  A model point qt (the same one as
scripts/formal_closure.py for the given (B, seed)) fixes q mod ell^E for ell in LAM,
with E as large as needed (reported).  For a primitive irreducible g in Z[X] with
lc>0, C_g = LAM-part of g(qt); R_g = g(qt)/C_g is the model value of the formal
prime r_g.  A FORMAL INTEGER is (c, ((key,e),...)) meaning c*prod (g/C_g)^e, c a
nonzero integer.  At an admissible q (q = qt mod prod ell^E_ell, every r_g prime
and outside LAM, q large) its prime factorisation is c * prod r_g^e, and for every
prime ell NOT in LAM, v_ell(g(q)) = 0 for g in S.

Fibre of Z (as in DEPTH3 Lemma 3): r/s = (4Z-P)/(PZ) reduced, D runs over formal
signed divisors of s^2, y=(D+s)/r, w=(s^2/D+s)/r.  Decision per candidate D:
  * numeric test at qt modulo L' = lcm_g(R_g^beta_g) * (LAM-part of c_r) : failing it
    is a ROBUST rejection (fails at every admissible q);
  * (A) g^beta | D+s in Q[X] for every g in r (checked by factorisation): robust;
  * for each prime ell of c_r outside LAM ("r-prime"): GENERIC test
    ell^v | content(D+s numerator).  At admissible q with q mod ell avoiding the roots
    of the primitive part of D+s the generic answer is the true one.
A candidate passing everything is ACCEPTED (vertex).  A candidate failing only generic
tests is FRAGILE: the closure is correct provided the residue rho_ell of q mod ell
(ell then joins Lambda with E_ell=1) avoids the roots of the witness polynomial.
For "large" r-primes we only record a root budget (counting argument); for primes in
--explicit we record the witness polynomial mod ell.

Dead denominators (p-free, negative or > 2t eventually) have singleton fibres
(SIGNED_REFACTOR 5, WINDMILL Thm 7) and are not expanded.
"""
from __future__ import annotations

import argparse
import gzip
import json
import sys
import time
from fractions import Fraction
from math import gcd, prod
from multiprocessing import Pool

import flint
sys.set_int_max_str_digits(0)
from sympy import factorint, primerange

PX = flint.fmpz_poly([1, 24])  # 24X+1
XX = flint.fmpz_poly([0, 1])


def lcm(a, b):
    return a // gcd(a, b) * b


def vval(n, ell):
    n = abs(n)
    if n == 0:
        return 10**9
    k = 0
    while n % ell == 0:
        n //= ell
        k += 1
    return k


def model_point(B, seed):
    sys.path.insert(0, __file__.rsplit("/", 1)[0])
    import formal_closure as fc
    F = fc.Formal(B, seed)
    return F.qt


def build_qt(residues, seed, bits=400):
    """qt = res_ell mod ell^k for all ell, plus a random multiple of the modulus"""
    import random
    from sympy.ntheory.modular import crt
    mods = [l**k for l, (r, k) in sorted(residues.items())]
    res = [r % (l**k) for l, (r, k) in sorted(residues.items())]
    q0 = int(crt(mods, res)[0])
    return q0 + prod(mods) * random.Random(seed).getrandbits(bits)


class Engine:
    def __init__(self, qt, lam, explicit=()):
        self.qt = qt
        self.lam = list(lam)
        self.lamset = set(lam)
        self.lamprod = prod(self.lam)
        self.explicit = set(explicit)
        self.polys = {}
        self.P = self.reg(PX)
        self.X = self.reg(XX)

    # ----- formal primes
    @staticmethod
    def normalize(g):
        c = g.content()
        if c != 1:
            g = g // c
        if g.coeffs()[-1] < 0:
            g = -g
        return g

    def reg(self, g):
        """register a (primitive, lc>0) poly or key; return key"""
        if isinstance(g, tuple):
            key = g
            if key in self.polys:
                return key
            g = flint.fmpz_poly(list(key))
        else:
            g = self.normalize(g)
            key = tuple(int(a) for a in g.coeffs())
            if key in self.polys:
                return key
        v = int(g(self.qt))
        assert v > 0, key
        C = 1
        vals = {}
        # quick filter: only primes dividing gcd(v, lamprod)
        gg = gcd(v, self.lamprod)
        if gg > 1:
            for ell in self.lam:
                if gg % ell == 0:
                    k = 0
                    while v % ell == 0:
                        v //= ell
                        k += 1
                    C *= ell**k
                    vals[ell] = k
        self.polys[key] = (g, C, v, g.degree(), vals)
        return key

    # ----- formal integers
    def value(self, F):
        c, ex = F
        return c * prod(self.polys[k][2] ** e for k, e in ex)

    def polyq(self, F):
        """(numerator fmpz_poly, positive denominator int)"""
        c, ex = F
        num = flint.fmpz_poly([c])
        den = 1
        for k, e in ex:
            g, C, _, _, _ = self.polys[k]
            num = num * g**e
            den *= C**e
        return num, den

    def degree(self, F):
        return sum(self.polys[k][3] * e for k, e in F[1])

    @staticmethod
    def mul(F, G):
        ex = dict(F[1])
        for k, e in G[1]:
            ex[k] = ex.get(k, 0) + e
        return (F[0] * G[0], tuple(sorted((k, e) for k, e in ex.items() if e)))

    @staticmethod
    def div(F, G):
        """exact formal division or None"""
        if F[0] % G[0]:
            return None
        ex = dict(F[1])
        for k, e in G[1]:
            ex[k] = ex.get(k, 0) - e
            if ex[k] < 0:
                return None
        return (F[0] // G[0], tuple(sorted((k, e) for k, e in ex.items() if e)))

    @staticmethod
    def gcdF(F, G):
        b = dict(G[1])
        ex = tuple(sorted((k, min(e, b[k])) for k, e in F[1] if k in b))
        return (gcd(F[0], G[0]), tuple((k, e) for k, e in ex if e))

    def from_poly(self, num, den, register=True):
        """formal form of the polynomial num/den (num in Z[X]) assumed integer-valued at
        admissible q.  Returns (formal, keys) with constant = cont*prod C_h^e/den (must be int)."""
        cont, facs = num.factor()
        cont = int(cont)
        ex = {}
        Cp = 1
        for h, e in facs:
            if h.degree() == 0:
                cont *= int(h.coeffs()[0]) ** e
                continue
            if h.coeffs()[-1] < 0:
                h = -h
                if e % 2:
                    cont = -cont
            k = self.reg(h)
            ex[k] = ex.get(k, 0) + e
            Cp *= self.polys[k][1] ** e
        c = Fraction(cont * Cp, den)
        assert c.denominator == 1, ("non-integral constant", num, den)
        return (int(c), tuple(sorted(ex.items())))

    def kind(self, Z):
        """'pdiv' | 'anchor' (p-free, 0<Z<=2t=12X eventually) | 'dead'"""
        if any(k == self.P for k, e in Z[1]):
            return "pdiv"
        if Z[0] < 0:
            return "dead"
        d = self.degree(Z)
        if d == 0:
            return "anchor"
        if d >= 2:
            return "dead"
        num, den = self.polyq(Z)
        a1, a0 = Fraction(int(num.coeffs()[1]), den), Fraction(int(num.coeffs()[0]), den)
        if a1 > 12 or (a1 == 12 and a0 > 0):
            return "dead"
        return "anchor"

    def seed(self):
        t = (6, ((self.X, 1),))
        m = (-12, tuple(sorted([(self.X, 1), (self.P, 1)])))
        return self.canon((t, m, m))

    def canon(self, v):
        return tuple(sorted(v, key=lambda z: (self.value(z), z)))

    # ----- the fibre
    def fibre(self, Z):
        info = {"aux": [], "needE": {}, "budget": {}, "fragile": {}, "rprimes": [],
                "ncand": 0, "nsurv": 0, "nfact": 0}
        Zn, Zd = self.polyq(Z)
        Nn = 4 * Zn - PX * Zd
        assert Nn != 0
        N = self.from_poly(Nn, Zd)
        info["aux"] = [k for k, e in N[1]]
        PZ = self.mul(Z, (1, ((self.P, 1),)))
        g = self.gcdF(N, PZ)
        r, s = self.div(N, g), self.div(PZ, g)
        if s[0] < 0:
            r, s = (-r[0], r[1]), (-s[0], s[1])
        cr, cs = r[0], s[0]
        acr = abs(cr)
        # LAM part of c_r and the r-primes
        Lr, rest = 1, acr
        for ell in self.lam:
            if rest % ell == 0:
                k = 0
                while rest % ell == 0:
                    rest //= ell
                    k += 1
                Lr *= ell**k
        nonlam = {int(l): int(e) for l, e in factorint(rest).items()} if rest > 1 else {}
        info["rprimes"] = sorted(nonlam)
        # precision needed at LAM primes for the numeric decisions
        sden = prod(self.polys[k][1] ** (2 * e) for k, e in s[1])
        for ell in self.lam:
            v = vval(Lr, ell)
            if v:
                info["needE"][ell] = v + vval(sden, ell)
        Lp = Lr
        for k, beta in r[1]:
            Lp = lcm(Lp, self.polys[k][2] ** beta)
        large = {l: e for l, e in nonlam.items() if l not in self.explicit}
        small = {l: e for l, e in nonlam.items() if l in self.explicit}
        M1 = Lp
        for l, e in large.items():
            if gcd(M1, l) == 1:
                M1 *= l**e
        cs2 = cs * cs
        cf = factorint(cs)
        sv = self.value(s)
        s2 = self.mul(s, s)
        sn, sd = self.polyq(s)
        degs = self.degree(s)
        edivs = [()]
        for k, e in s[1]:
            edivs = [ed + ((k, j),) for ed in edivs for j in range(2 * e + 1)]
        nE = len(edivs)
        tau = prod(2 * e + 1 for e in cf.values())
        # crude root budget for large r-primes: every candidate passing the L' test
        # could be a fragile one with that witness; each contributes <= 2*deg(s) roots
        ncount = 2 * nE if Lp > 2 * cs2 else 2 * tau * nE
        info["ncand"] = 2 * tau * nE
        for l in large:
            info["budget"][l] = ncount * max(1, 2 * degs)
        cdivs = None
        out = set()
        rkeys = dict(r[1])
        seen = set()
        for ed in edivs:
            E = (1, tuple(sorted((k, j) for k, j in ed if j)))
            Ev = self.value(E)
            cands = []
            if M1 > 2 * cs2 and gcd(Ev, M1) == 1:
                u = (-sv * pow(Ev, -1, M1)) % M1
                if u and u <= cs2 and cs2 % u == 0:
                    cands.append(u)
                if M1 - u <= cs2 and cs2 % (M1 - u) == 0:
                    cands.append(-(M1 - u))
            else:
                if cdivs is None:
                    cdivs = [1]
                    for ell, e in cf.items():
                        cdivs = [d * ell**j for d in cdivs for j in range(2 * e + 1)]
                Evm, svm = Ev % M1, sv % M1
                cands = [sg * c for c in cdivs for sg in (1, -1) if (sg * c * Evm + svm) % M1 == 0]
            for sc in cands:
                D = (sc, E[1])
                Dc = self.div(s2, D)
                if (self.value(Dc) + sv) % M1:
                    continue
                pair = tuple(sorted([D, Dc]))
                if pair in seen:
                    continue
                seen.add(pair)
                info["nsurv"] += 1
                res = self.decide(D, Dc, s, sn, sd, r, rkeys, nonlam, large, small, info)
                if res is not None:
                    out.add(self.canon((Z, res[0], res[1])))
        return out, info

    def decide(self, D, Dc, s, sn, sd, r, rkeys, nonlam, large, small, info):
        Fs = []
        for DD in (D, Dc):
            dn, dd = self.polyq(DD)
            L = lcm(dd, sd)
            Fn = dn * (L // dd) + sn * (L // sd)
            if Fn == 0:
                return None  # zero denominator
            Fs.append((Fn, L))
        # generic tests at r-primes (content valuations)
        fails = []  # (ell, index)
        for idx, (Fn, L) in enumerate(Fs):
            ct = int(Fn.content())
            for ell, v in nonlam.items():
                if vval(ct, ell) < v:
                    fails.append((ell, idx))
        # (A): exponents of the polys of r in D+s; factor (needed anyway if accepted)
        forms = []
        for Fn, L in Fs:
            if rkeys or not fails:
                info["nfact"] += 1
                FF = self.from_poly(Fn, L)
                fx = dict(FF[1])
                if any(fx.get(k, 0) < b for k, b in rkeys.items()):
                    return None  # robust rejection (A)
                forms.append(FF)
            else:
                forms.append(None)
        if not fails:
            ys = []
            for FF in forms:
                y = self.div(FF, r)
                assert y is not None, "generic pass but formal division failed"
                ys.append(y)
            return ys
        # fragile: robust tests all pass, only generic failures remain
        lg = [f for f in fails if f[0] in large]
        if lg:
            return None  # witness is a large r-prime: covered by the crude budget
        ell, idx = max(fails)
        Fn, L = Fs[idx]
        prim = Fn // Fn.content()
        c = [int(a) % ell for a in prim.coeffs()]
        while c and c[-1] == 0:
            c.pop()
        if len(c) >= 2:
            if len(c) == 2:
                rts = [(-c[0] * pow(c[1], -1, ell)) % ell]
            else:
                rts = [int(x) for x, _ in flint.nmod_poly(c, ell).roots()]
            d = info["fragile"].setdefault(ell, {})
            for x in rts:
                d[x] = d.get(x, 0) + 1
        info["nfragile"] = info.get("nfragile", 0) + 1
        return None


# ---------------------------------------------------------------- driver
G = {}


def init(qt, lam, explicit):
    G["E"] = Engine(qt, lam, explicit)


def work(Z):
    E = G["E"]
    for k, e in Z[1]:
        E.reg(k)
    out, info = E.fibre(Z)
    return Z, sorted(out), info


def jsonable_formal(F):
    return [F[0], [[list(k), e] for k, e in F[1]]]


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--B", type=int, default=1500)
    ap.add_argument("--seed", type=int, default=1)
    ap.add_argument("--jobs", type=int, default=14)
    ap.add_argument("--rounds", type=int, default=40)
    ap.add_argument("--dump", default=None)
    ap.add_argument("--explicit", default=None, help="file with r-primes to treat explicitly")
    ap.add_argument("--noprune", action="store_true")
    ap.add_argument("--lam-file", default=None, help="JSON {residues: {ell: [res, k]}, seed}: LAM and qt = res mod ell^k")
    ap.add_argument("--qt-from", default=None, help="take the model point qt from a previous dump")
    a = ap.parse_args()
    if a.lam_file:
        LF = json.load(open(a.lam_file))
        lam = sorted(int(l) for l in LF["residues"])
        qt = build_qt({int(l): tuple(v) for l, v in LF["residues"].items()}, LF.get("seed", 1))
    else:
        lam = [int(l) for l in primerange(2, a.B + 1)]
        qt = model_point(a.B, a.seed) if not a.qt_from else int(json.load(gzip.open(a.qt_from, "rt"))["qt"])
    explicit = []
    if a.explicit:
        explicit = [int(x) for x in open(a.explicit).read().split()]
    E = Engine(qt, lam, explicit)
    s0 = E.seed()
    V, done, frontier = {s0}, set(), [s0]
    AUX, NEEDE, BUDGET, FRAG, RP = set(), {}, {}, {}, set()
    NFRAG = 0
    FIB = {}
    t0 = time.time()
    stable = False
    with Pool(a.jobs, initializer=init, initargs=(qt, lam, explicit)) as pool:
        for rnd in range(1, a.rounds + 1):
            todo = []
            for v in frontier:
                for z in v:
                    if z in done:
                        continue
                    done.add(z)
                    for k, e in z[1]:
                        E.reg(k)
                    if not a.noprune and E.kind(z) == "dead":
                        continue
                    todo.append(z)
            new = []
            for Z, ws, info in pool.imap_unordered(work, todo, chunksize=2):
                for k in info["aux"]:
                    E.reg(k)
                    AUX.add(k)
                for l, v in info["needE"].items():
                    NEEDE[l] = max(NEEDE.get(l, 0), v)
                for l, b in info["budget"].items():
                    BUDGET[l] = BUDGET.get(l, 0) + b
                for l, d in info["fragile"].items():
                    D = FRAG.setdefault(l, {})
                    for x, c in d.items():
                        D[x] = D.get(x, 0) + c
                NFRAG += info.get("nfragile", 0)
                RP.update(info["rprimes"])
                FIB[Z] = (len(ws), info["ncand"], info["nsurv"], info["nfact"])
                for w in ws:
                    for z in w:
                        for k, e in z[1]:
                            E.reg(k)
                    w = E.canon(w)
                    if w not in V:
                        V.add(w)
                        new.append(w)
            npos = sum(1 for w in new if all(z[0] > 0 for z in w))
            st = {"round": rnd, "expanded": len(todo), "new": len(new), "vertices": len(V),
                  "positive_new": npos, "polys": len(E.polys), "rprimes": len(RP),
                  "fragile": NFRAG, "time": round(time.time() - t0)}
            print(json.dumps(st), flush=True)
            if not new:
                stable = True
                print("STABILIZED", flush=True)
                break
            frontier = new
    entry = {k for v in V for z in v for k, e in z[1]}
    S = entry | AUX
    maxval = {}
    for k in S:
        for l, v in E.polys[k][4].items():
            maxval[l] = max(maxval.get(l, 0), v)
    sdeg = sum(E.polys[k][3] for k in S)
    print(json.dumps({"S": len(S), "entry": len(entry), "aux_only": len(AUX - entry), "sum_deg": sdeg,
                      "max_deg": max(E.polys[k][3] for k in S),
                      "positive_vertices": sum(1 for w in V if all(z[0] > 0 for z in w))}), flush=True)
    if a.dump:
        state = {"B": a.B, "lam": lam, "seed": a.seed, "qt": str(qt), "stabilized": stable, "pruned": not a.noprune,
                 "explicit": explicit,
                 "S": [[list(k), E.polys[k][1], k in AUX, k in entry] for k in sorted(S)],
                 "needE": {str(l): v for l, v in NEEDE.items()},
                 "maxval": {str(l): v for l, v in maxval.items()},
                 "budget": {str(l): b for l, b in BUDGET.items()},
                 "rprimes": sorted(RP), "nfragile": NFRAG,
                 "fragile": {str(l): {str(x): c for x, c in d.items()} for l, d in FRAG.items()},
                 "fibres": [[jsonable_formal(Z), list(x)] for Z, x in FIB.items()],
                 "vertices": [[jsonable_formal(z) for z in v] for v in V]}
        with gzip.open(a.dump, "wt") as fh:
            json.dump(state, fh)


if __name__ == "__main__":
    main()
