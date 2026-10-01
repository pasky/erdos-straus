#!/usr/bin/env python3
"""Hostile review of POINTWISE_SIZE.md Theorem M / Lemma D / (F3') / Prop. A / Theorem C.

From-scratch formal-vs-actual simulator, sharing no code with
scripts/pointwise_size_*.py.  One program text, two machines:

  * ActualMachine  -- integers, sympy.factorint, exact comparisons;
  * FormalMachine  -- elements of Q[X] at a lazily specified profinite point q*,
                      implementing Lemma D, (F3'), (F4), (F5) and Prop. A literally
                      as written in POINTWISE_SIZE §1.2/§4.1.

Every primitive call is logged.  The formal log, evaluated at q, must equal the
actual log *entry by entry* (not just the output).  Every eventual-sign decision
records its polynomial, and a rigorous Cauchy root bound gives an explicit
threshold q_0 for the whole run, so we can check Theorem M(a) in the stated form
"for every admissible q >= q_0", with no unexplained mismatches.

The profinite point: q*_l = qt (mod l^E_l) for l <= B (the set Lam0), and for
l > B we *declare* q*_l off the roots of every polynomial met (consistent as long
as sum of degrees < B; asserted).  Then C_h = prod_{l<=B} l^{v_l(h(qt))}, with
v_l < E_l asserted (else: precision error, the point must be refined).

Tests:
  T1  random programs (ring ops, divmod, DIVIDES, signs, comparisons with p^(1/k)),
      no FACTOR: compared at random q = qt (mod M), q >= q_0  (Lemma D, (F3'), Prop A).
  T2  an adaptive ES program (Euclid while-loop, FACTOR, DIVISORS, list loops,
      formal-prime-dependent Type I step creating a quadratic h, size filter d<=sqrt p,
      final ES identity check) at a square-mimicking and a non-square point; compared
      on actual admissible q (all r_h prime, found by sieve).  Also checks Theorem C's
      character formula (r_h/p) = (H_h/p)(u/p)^{deg h}(C_h/p) at every admissible q.

Usage: PYTHONPATH=scripts uv run python scripts/review_pointwise_size_engine.py [T1progs] [T2kmax]
"""
import sys
import random
from fractions import Fraction
from functools import cmp_to_key
from math import gcd, prod

import numpy as np
import sympy as sp
from sympy import factorint, isprime, primerange, jacobi_symbol

Xs = sp.Symbol('X')
QQ = sp.QQ
ZZ = sp.ZZ


class Halt(Exception):
    pass


class PrecisionError(Exception):
    pass


def lcm(a, b):
    return a * b // gcd(a, b)


def vl(n, l):
    n = abs(n)
    if n == 0:
        return 10 ** 9
    v = 0
    while n % l == 0:
        n //= l
        v += 1
    return v


# ----------------------------------------------------------------------------- actual
def factor_with_hints(n, hints):
    """true factorisation of n>0.  hints: known primes (verified) tried first, so that
    products of several ~30-digit primes are feasible; the result is the unique
    factorisation regardless of the hints (all factors are primality-checked)."""
    f = {}
    for h in hints:
        if h > 1 and n % h == 0:
            assert isprime(h)
            while n % h == 0:
                n //= h
                f[h] = f.get(h, 0) + 1
    for l, e in factorint(n).items():
        f[l] = f.get(l, 0) + e
    assert all(isprime(l) for l in f)
    return f


class ActualMachine:
    def __init__(self, p, hints=()):
        self.p = p
        self.log = []
        self.hints = list(hints)

    def inp(self):
        return self.p

    def const(self, c):
        return c

    def add(self, a, b):
        return a + b

    def sub(self, a, b):
        return a - b

    def mul(self, a, b):
        return a * b

    def divmod(self, a, b):
        if b == 0:
            self.log.append(('divmod', 'ERR'))
            raise Halt
        q, r = divmod(a, b)       # Python floor division == mathematical floor
        self.log.append(('divmod', q, r))
        return q, r

    def divides(self, a, b):      # truth of b | a
        res = (a == 0) if b == 0 else (a % b == 0)
        self.log.append(('divides', res))
        return res

    def sign(self, a):
        s = (a > 0) - (a < 0)
        self.log.append(('sign', s))
        return s

    def cmp_root(self, a, k):     # sign(a - p^(1/k)), exact
        if a <= 0:
            s = -1
        else:
            t = a ** k - self.p
            s = (t > 0) - (t < 0)
        self.log.append(('cmproot', k, s))
        return s

    def factor(self, a):
        if a == 0:
            self.log.append(('factor', 'ERR'))
            raise Halt
        f = sorted(factor_with_hints(abs(a), self.hints).items())
        self.log.append(('factor', tuple(f)))
        return f

    def divisors(self, a):
        if a == 0:
            self.log.append(('divisors', 'ERR'))
            raise Halt
        ds = [1]
        for l, e in factor_with_hints(abs(a), self.hints).items():
            ds = [d * l ** i for d in ds for i in range(e + 1)]
        ds.sort()
        self.log.append(('divisors', tuple(ds)))
        return ds


# ----------------------------------------------------------------------------- formal
def P_(expr):
    return sp.Poly(expr, Xs, domain=QQ)


def cauchy_bound(f):
    """every real root of the nonzero poly f is < this bound."""
    cs = [Fraction(int(c.p), int(c.q)) for c in f.all_coeffs()]
    lc = cs[0]
    if len(cs) == 1:
        return 0
    return int(1 + max(abs(c / lc) for c in cs[1:])) + 1


class FormalMachine:
    def __init__(self, Ppoly, qt, E):
        self.P = P_(Ppoly)
        self.qt = qt
        self.E = dict(E)                  # l -> E_l for l in Lam0
        self.B = max(E)
        self.log = []
        self.thr = []                     # polys whose eventual sign was used
        self.S = {}                       # primitive h (tuple of int coeffs) -> C_h
        self.Lam = set()                  # primes forced into Lambda (C_h, D, D')
        self.Kprimes = set()
        self.cnt = dict(floor_rho0_sigma_neg=0, floor_rho_nonzero=0, divides_R0=0, divides_Rnz=0,
                        divides_B0=0)

    # -- helpers
    def note(self, f):
        if not f.is_zero:
            self.thr.append(f)

    def esign(self, f):
        if f.is_zero:
            return 0
        self.note(f)
        return 1 if f.LC() > 0 else -1

    def residue(self, F, D):
        """F(q*) mod D, F in Z[X] (as QQ poly with integer coeffs)."""
        for l in sp.primefactors(D):
            if l > self.B or vl(D, l) > self.E[l]:
                raise PrecisionError(('residue', l, vl(D, l)))
            self.Lam.add(l)
        val = F.eval(self.qt)
        assert val.q == 1
        return int(val.p) % D

    @staticmethod
    def den(f):
        d = 1
        for c in f.all_coeffs():
            d = lcm(d, int(sp.Rational(c).q))
        return d

    def C_of(self, h):
        """h: primitive Poly over ZZ, lc>0.  C_h at q*."""
        key = tuple(int(c) for c in h.all_coeffs())
        if key in self.S:
            return self.S[key]
        val = int(h.eval(self.qt))
        if val == 0:
            raise PrecisionError(('degenerate', key))
        C = 1
        for l in self.E:
            v = vl(val, l)
            if v >= self.E[l]:
                raise PrecisionError(('C_h precision', key, l))
            C *= l ** v
            if v:
                self.Lam.add(l)
        self.S[key] = C
        assert sum(len(k) - 1 for k in self.S) < self.B, "sum deg >= B: point not consistent"
        return C

    # -- instructions
    def inp(self):
        return self.P

    def const(self, c):
        return P_(c)

    def add(self, a, b):
        return a + b

    def sub(self, a, b):
        return a - b

    def mul(self, a, b):
        return a * b

    def divmod(self, A, Bp):
        if Bp.is_zero:
            self.log.append(('divmod', 'ERR'))
            raise Halt
        self.note(Bp)                                   # B(q) != 0
        Q, R = A.div(Bp)
        D = self.den(Q)
        F = Q * D
        rho = self.residue(F, D)
        sigma = self.esign(R * Bp) if not R.is_zero else 0
        if not R.is_zero:
            self.note(Bp * Bp - (R * R) * (D * D))       # |R/B| < 1/D
            assert (Bp * Bp - (R * R) * (D * D)).LC() > 0
        fl = P_(sp.Rational(1, D) * (F.as_expr() - rho))
        if rho == 0 and sigma < 0:
            fl = fl - 1
            self.cnt['floor_rho0_sigma_neg'] += 1
        if rho:
            self.cnt['floor_rho_nonzero'] += 1
        rem = A - Bp * fl
        self.log.append(('divmod', fl, rem))
        return fl, rem

    def divides(self, A, Bp):
        if Bp.is_zero:
            res = A.is_zero
            self.cnt['divides_B0'] += 1
        else:
            self.note(Bp)
            Q, R = A.div(Bp)
            D = self.den(Q)
            if not R.is_zero:
                self.note(R)
                self.note(Bp * Bp - (R * R) * (D * D))
                res = False
                self.cnt['divides_Rnz'] += 1
            else:
                res = self.residue(Q * D, D) == 0
                self.cnt['divides_R0'] += 1
        self.log.append(('divides', res))
        return res

    def sign(self, A):
        s = self.esign(A)
        self.log.append(('sign', s))
        return s

    def cmp_root(self, A, k):
        """Prop. A with c=1, theta=1/k, deg P = 1."""
        if self.esign(A) <= 0:
            s = -1
        else:
            s = self.esign(A ** k - self.P)
        self.log.append(('cmproot', k, s))
        return s

    def _fact(self, A):
        if A.is_zero:
            raise Halt
        self.note(A)
        c, facs = sp.factor_list(A.as_expr(), Xs)
        kappa = sp.Rational(c)
        out = []
        for f, e in facs:
            fp = sp.Poly(f, Xs, domain=QQ)
            # make primitive integer with positive lc
            fz = fp * self.den(fp)
            cont = sp.Poly(fz.as_expr(), Xs, domain=ZZ).content()
            h = sp.Poly((fz.as_expr() / cont), Xs, domain=ZZ)
            scale = sp.Rational(fp.LC()) / sp.Rational(h.LC())  # fp = scale*h
            if h.LC() < 0:
                h = -h
                scale = -scale
            kappa *= scale ** e
            if h.degree() == 0:
                kappa *= sp.Rational(h.LC()) ** e
                continue
            out.append((h, e))
        K = kappa
        for h, e in out:
            K *= self.C_of(h) ** e
        assert K.q == 1, ("K_A not an integer: Lemma I violated?", K)
        K = int(K)
        r = [(P_(h.as_expr() / self.C_of(h)), e) for h, e in out]
        return K, r

    def _order(self, items, key):
        def cmp(a, b):
            return self.esign(key(a) - key(b))
        return sorted(items, key=cmp_to_key(cmp))

    def factor(self, A):
        try:
            K, r = self._fact(A)
        except Halt:
            self.log.append(('factor', 'ERR'))
            raise
        cp = sorted(factorint(abs(K)).items())
        self.Kprimes |= {l for l, _ in cp}
        big = max([l for l, _ in cp] + [1])
        for rh, _ in r:
            self.note(rh - big)                    # r_h exceeds every prime of K
        r = self._order(r, lambda t: t[0])
        out = [(P_(l), v) for l, v in cp] + r
        self.log.append(('factor', tuple(out)))
        return out

    def divisors(self, A):
        try:
            K, r = self._fact(A)
        except Halt:
            self.log.append(('divisors', 'ERR'))
            raise
        big = max(list(factorint(abs(K))) + [1])
        for rh, _ in r:
            self.note(rh - big)
        ds = [P_(d) for d in sp.divisors(abs(K))]
        for rh, e in r:
            ds = [d * rh ** j for d in ds for j in range(e + 1)]
        ds = self._order(ds, lambda t: t)
        for a, b in zip(ds, ds[1:]):
            assert not (a - b).is_zero, "tie between formal divisors"
        self.log.append(('divisors', tuple(ds)))
        return ds

    def threshold(self):
        return max([cauchy_bound(f) for f in self.thr] + [0])


def ev(obj, q):
    """evaluate a formal log entry / output at X=q."""
    if isinstance(obj, sp.Poly):
        v = obj.eval(q)
        if v.q != 1:
            raise AssertionError("formal value not integral at q")
        return int(v.p)
    if isinstance(obj, (tuple, list)):
        return tuple(ev(o, q) for o in obj)
    return obj


def run(prog, mach):
    try:
        out = prog(mach)
    except Halt:
        out = ('FAIL', 'error')
    return out


def norm(obj):
    if isinstance(obj, (tuple, list)):
        return tuple(norm(o) for o in obj)
    return obj


# ----------------------------------------------------------------------------- T1
def random_program(rng):
    """instruction list over registers; registers 0 = p, 1..3 = small constants."""
    prog = []
    nreg = 4
    for _ in range(rng.randint(6, 14)):
        op = rng.choice(['add', 'sub', 'mul', 'divc', 'divr', 'divides', 'if', 'cmp'])
        i, j = rng.randrange(nreg), rng.randrange(nreg)
        if op == 'divc':
            prog.append(('divc', i, rng.choice([2, 3, 4, 5, 6, 8, 9, 12, 16, 24, -3, -4])))
            nreg += 2
        elif op == 'divr':
            prog.append(('divr', i, j))
            nreg += 2
        elif op == 'divides':
            prog.append(('divides', i, j, rng.choice([2, 3, 4, 8, 9, 5])))
            nreg += 1
        elif op == 'if':
            prog.append(('if', i, j, rng.randrange(nreg)))
            nreg += 1
        elif op == 'cmp':
            prog.append(('cmp', i, rng.choice([2, 3])))
            nreg += 1
        else:
            prog.append((op, i, j))
            nreg += 1
    return prog


def interp(prog, consts):
    def f(m):
        R = [m.inp()] + [m.const(c) for c in consts]
        for ins in prog:
            op = ins[0]
            if op in ('add', 'sub', 'mul'):
                R.append(getattr(m, op)(R[ins[1]], R[ins[2]]))
            elif op == 'divc':
                q, r = m.divmod(R[ins[1]], m.const(ins[2]))
                R += [q, r]
            elif op == 'divr':
                q, r = m.divmod(R[ins[1]], R[ins[2]])
                R += [q, r]
            elif op == 'divides':
                # test  c*R[j]+1 | R[i]  and  R[i] | ...  -- exercise R=0 and R!=0 cases
                b = m.add(m.mul(m.const(ins[3]), R[ins[2]]), m.const(0))
                t = m.divides(R[ins[1]], b)
                R.append(m.const(1) if t else m.const(0))
            elif op == 'if':
                s = m.sign(m.sub(R[ins[1]], R[ins[2]]))
                R.append(R[ins[3]] if s > 0 else m.add(R[ins[3]], m.const(7)))
            elif op == 'cmp':
                s = m.cmp_root(R[ins[1]], ins[2])
                R.append(m.const(s))
        return ('OUT', tuple(R[-4:]))
    return f


def degree_ok(prog, consts, Ppoly):
    """reject programs whose formal values get large degree (keeps Cauchy bounds sane)."""
    fm = FormalMachine(Ppoly, 0, {2: 30, 3: 20, 5: 12})
    try:
        out = run(interp(prog, consts), fm)
    except PrecisionError:
        return True
    for e in fm.log:
        for o in e:
            if isinstance(o, sp.Poly) and o.degree() > 4:
                return False
    return True


def T1(nprog, seed=12345):
    rng = random.Random(seed)
    Ppoly = 24 * Xs + 1
    E = {2: 12, 3: 8, 5: 6, 7: 4, 11: 3, 13: 3}
    M = prod(l ** e for l, e in E.items())
    stats = dict(progs=0, skipped_precision=0, skipped_degree=0, runs=0, mism=0, cmp=0, signs=0)
    for _ in range(nprog):
        prog = random_program(rng)
        consts = [rng.randint(-9, 9) for _ in range(3)]
        if not degree_ok(prog, consts, Ppoly):
            stats['skipped_degree'] += 1
            continue
        qt = rng.randrange(M)
        fm = FormalMachine(Ppoly, qt, E)
        try:
            fout = run(interp(prog, consts), fm)
        except PrecisionError:
            stats['skipped_precision'] += 1
            continue
        stats['progs'] += 1
        for kk, vv in fm.cnt.items():
            stats[kk] = stats.get(kk, 0) + vv
        q0 = fm.threshold()
        for e in fm.log:
            if e[0] == 'divides':
                pass
        for _ in range(6):
            k = rng.randrange(1, 10 ** 6)
            q = qt + M * (k + q0 // M + 1)
            assert q >= q0
            am = ActualMachine(24 * q + 1)
            aout = run(interp(prog, consts), am)
            stats['runs'] += 1
            if norm(ev(fm.log, q)) != norm(tuple(am.log)) or norm(ev(fout, q)) != norm(aout):
                stats['mism'] += 1
                if stats['mism'] <= 3:
                    print('MISMATCH', prog, consts, qt, q)
                    for a, b in zip(ev(fm.log, q), am.log):
                        if a != b:
                            print('   formal', a, ' actual', b)
                            break
        # feature coverage counters (from the formal log)
        for e in fm.log:
            if e[0] == 'cmproot':
                stats['cmp'] += 1
            if e[0] == 'sign':
                stats['signs'] += 1
    return stats


def T1_lemmaD_direct(n, seed=7):
    """Direct check of Lemma D on random (A,B) incl. the rho=0, sigma<0 branch."""
    rng = random.Random(seed)
    E = {2: 10, 3: 6, 5: 4, 7: 3}
    M = prod(l ** e for l, e in E.items())
    cnt = dict(cases=0, rho0_neg=0, rho0_pos=0, rho_pos=0, mism=0)
    for _ in range(n):
        A = P_(sum(rng.randint(-30, 30) * Xs ** i for i in range(rng.randint(0, 4))) + rng.randint(-30, 30))
        B = P_(sum(rng.randint(-6, 6) * Xs ** i for i in range(rng.randint(0, 2))) + rng.choice([-1, 1]) * rng.randint(1, 6))
        if B.is_zero:
            continue
        qt = rng.randrange(M)
        fm = FormalMachine(24 * Xs + 1, qt, E)
        try:
            fl, rem = fm.divmod(A, B)
        except PrecisionError:
            continue
        Q, R = A.div(B)
        D = fm.den(Q)
        rho = int((Q * D).eval(qt)) % D
        sig = 0 if R.is_zero else (1 if (R * B).LC() > 0 else -1)
        cnt['cases'] += 1
        if rho == 0 and sig < 0:
            cnt['rho0_neg'] += 1
        elif rho == 0:
            cnt['rho0_pos'] += 1
        else:
            cnt['rho_pos'] += 1
        q0 = fm.threshold()
        for _ in range(5):
            q = qt + M * (rng.randrange(10 ** 6) + q0 // M + 1)
            a, b = int(A.eval(q)), int(B.eval(q))
            if (a // b, a - b * (a // b)) != (ev(fl, q), ev(rem, q)):
                cnt['mism'] += 1
        # remainder-zero claim of Lemma D
        assert rem.is_zero == (R.is_zero and rho == 0)
    return cnt


# ----------------------------------------------------------------------------- T2
def es_program(m):
    """adaptive bounded ES program (different from the author's toy)."""
    p = m.inp()
    one, four = m.const(1), m.const(4)
    # Euclid while-loop on (p+7)/4, (p+3)/4  (formal floors with D>1, rho/sigma cases)
    a, _ = m.divmod(m.add(p, m.const(7)), four)
    b, _ = m.divmod(m.add(p, m.const(3)), four)
    while m.sign(b) != 0:
        _, r = m.divmod(a, b)
        a, b = b, r
    g = a
    xs = []
    for aa in (3, 7):
        A = m.const(aa)
        num = m.add(p, A)
        if not m.divides(num, four):
            continue
        x, _ = m.divmod(num, four)
        xs.append(x)
        xx = m.mul(x, x)
        for d in m.divisors(xx):
            if m.sign(m.sub(d, x)) > 0:          # only d <= x
                continue
            if m.cmp_root(d, 2) > 0:             # size filter d <= sqrt(p)  (Prop. A)
                continue
            if m.divides(m.add(d, x), A):
                y, _ = m.divmod(m.mul(p, m.add(x, d)), A)
                w, _ = m.divmod(m.mul(p, m.add(x, m.divmod(xx, d)[0])), A)
                return finish(m, p, x, y, w, ('II', aa))
    # tie stress: divisors of x3*x7 contain 6X+1 and 2(3X+1) (adjacent when C=1)
    if len(xs) == 2:
        m.divisors(m.mul(xs[0], xs[1]))
    # adaptive Type I step with modulus = each prime factor l = 3 (4) of the windows
    for x in xs:
        for (ell, e) in m.factor(x):
            if not m.divides(m.add(ell, one), four):
                continue
            z, _ = m.divmod(m.add(m.mul(p, ell), one), four)
            z2 = m.mul(z, z)
            for d in m.divisors(z2):
                if m.sign(m.sub(d, z)) > 0:
                    continue
                if m.divides(m.add(d, z), ell):
                    y1, _ = m.divmod(m.add(z, d), ell)
                    y2, _ = m.divmod(m.add(z, m.divmod(z2, d)[0]), ell)
                    return finish(m, p, y1, y2, m.mul(p, z), ('I',))
    return ('FAIL', g)


def finish(m, p, x, y, z, tag):
    lhs = m.mul(m.mul(m.mul(m.const(4), x), y), z)
    rhs = m.mul(p, m.add(m.add(m.mul(x, y), m.mul(y, z)), m.mul(x, z)))
    if m.sign(m.sub(lhs, rhs)) != 0 or m.sign(x) <= 0 or m.sign(y) <= 0 or m.sign(z) <= 0:
        return ('FAIL', 'bogus')
    return ('SUCCESS', x, y, z)


def make_point(rng, E, square=True, nonsq_at=7):
    """qt with q*_l a unit and 24q*+1 a nonzero square unit mod l (all l in E),
    except at nonsq_at when square=False."""
    res, mods = [], []
    for l, e in E.items():
        while True:
            r = rng.randrange(l ** e)
            if r % l == 0:
                continue
            u = (24 * r + 1) % l
            if l in (2, 3):
                ok = True                       # 24r+1 = 1 mod 8 / mod 3
            else:
                if u == 0:
                    continue
                isq = pow(u, (l - 1) // 2, l) == 1
                ok = isq if (square or l != nonsq_at) else not isq
            if ok:
                break
        res.append(r)
        mods.append(l ** e)
    from sympy.ntheory.modular import crt
    return int(crt(mods, res)[0])


def sieve_admissible(qt, M, forms, kmax, small_hi=3000, chunk=1 << 20):
    """forms: list of (Poly h over ZZ, C_h).  q = qt + M k admissible iff all h(q)/C_h prime."""
    small = [l for l in primerange(2, small_hi) if M % l]
    hits = []
    hz = [(sp.Poly(h, Xs), C) for h, C in forms]
    roots = []
    for h, C in hz:
        coeffs = [int(c) for c in h.all_coeffs()]
        rl = []
        for l in small:
            bad = [k for k in range(l) if sum(c * pow((qt + M * k) % l, len(coeffs) - 1 - i, l)
                                              for i, c in enumerate(coeffs)) % l == 0]
            rl.append((l, bad))
        roots.append(rl)
    for k0 in range(0, kmax, chunk):
        ks = np.arange(k0, min(kmax, k0 + chunk), dtype=np.int64)
        alive = np.ones(len(ks), dtype=bool)
        for rl in roots:
            for l, bad in rl:
                if bad:
                    km = ks % l
                    for b in bad:
                        alive &= km != b
        for k in ks[alive]:
            q = qt + M * int(k)
            if all(isprime(int(h.eval(q)) // C) for h, C in hz):
                hits.append(q)
    return hits


def T2(kmax, seed=2026):
    rng = random.Random(seed)
    E = {2: 8, 3: 4, 5: 3, 7: 3, 11: 2, 13: 2, 17: 2, 19: 2, 23: 2, 29: 2, 31: 2, 37: 2}
    M = prod(l ** e for l, e in E.items())
    report = []
    for label, square in (('square-mimicking', True), ('non-square at 7', False)):
        tries = 0
        while True:
            tries += 1
            qt = make_point(rng, E, square=square)
            fm = FormalMachine(24 * Xs + 1, qt, E)
            try:
                fout = run(es_program, fm)
            except PrecisionError:
                continue
            # want a non-trivial run: on the non-square point prefer a SUCCESS, and
            # want the adaptive Type I step to create a quadratic h
            quad = any(len(k) == 3 for k in fm.S)
            if square and (not quad or fout[0] != 'FAIL'):
                if tries < 400:
                    continue
            if not square and fout[0] != 'SUCCESS' and tries < 400:
                continue
            break
        q0 = fm.threshold()
        forms = [(sp.Poly(list(k), Xs, domain=ZZ).as_expr(), C) for k, C in fm.S.items()]
        forms = [(24 * Xs + 1, 1)] + [f for f in forms if sp.expand(f[0] - (24 * Xs + 1)) != 0]
        hits = sieve_admissible(qt, M, forms, kmax)
        hits = [q for q in hits if q >= q0]
        mism = 0
        charviol = 0
        allplus = True
        bo = BrokenOrder(24 * Xs + 1, qt, E)
        bout = run(es_program, bo)
        broken_detected = 0
        for q in hits:
            p = 24 * q + 1
            hints = [int(sp.Poly(list(k), Xs).eval(q)) // C for k, C in fm.S.items()]
            am = ActualMachine(p, hints)
            aout = run(es_program, am)
            if norm(ev(fm.log, q)) != norm(tuple(am.log)) or norm(ev(fout, q)) != norm(aout):
                mism += 1
            if norm(ev(bo.log, q)) != norm(tuple(am.log)):
                broken_detected += 1
            # Theorem C character formula for every h != P
            for k, C in fm.S.items():
                h = sp.Poly(list(k), Xs, domain=ZZ)
                if sp.expand(h.as_expr() - (24 * Xs + 1)) == 0:
                    continue
                rh = int(h.eval(q)) // C
                Hh = int(sp.Rational(24) ** h.degree() * h.as_expr().subs(Xs, sp.Rational(-1, 24)))
                if Hh % p == 0:
                    charviol += 1
                    continue
                lhs = jacobi_symbol(rh % p, p)
                rhs = jacobi_symbol(Hh % p, p) * jacobi_symbol(24, p) ** h.degree() * jacobi_symbol(C, p)
                if lhs != rhs:
                    charviol += 1
                if lhs != 1:
                    allplus = False
        Hprimes = set()
        for k in fm.S:
            h = sp.Poly(list(k), Xs, domain=ZZ)
            Hh = int(sp.Rational(24) ** h.degree() * h.as_expr().subs(Xs, sp.Rational(-1, 24)))
            if Hh != 24 * 0 + 0 and sp.expand(h.as_expr() - (24 * Xs + 1)) != 0:
                Hprimes |= set(sp.primefactors(Hh))
        report.append(dict(point=label, qt=qt, M=M, formal_out=str(ev_out_str(fout)), q0=q0,
                           S={str(sp.Poly(list(k), Xs).as_expr()): C for k, C in fm.S.items()},
                           Kprimes=sorted(fm.Kprimes), Hprimes=sorted(Hprimes),
                           admissible=len(hits), mismatches=mism,
                           broken_order_mutation_detected=broken_detected, char_formula_violations=charviol,
                           all_formal_primes_residues=allplus,
                           example=(hits[0], 24 * hits[0] + 1) if hits else None,
                           loglen=len(fm.log)))
    return report


def T3(npts, seed=99):
    """Theorem C scan: random points square-mimicking at Lam0 = primes <= 37.  If the
    explicit Lam' of the proof of Theorem C (2, primes <= sum deg, primes of u=24, of every
    K_A, of every C_h, of every H_h) lies inside Lam0, Theorem C says the formal output
    must be FAIL (else no admissible q could exist).  Count violations."""
    rng = random.Random(seed)
    E = {2: 8, 3: 4, 5: 3, 7: 3, 11: 2, 13: 2, 17: 2, 19: 2, 23: 2, 29: 2, 31: 2, 37: 2}
    out = dict(points=0, precision=0, fail=0, success=0, lam_inside=0, lam_inside_success=0,
               nonsq_points=0, nonsq_success=0)
    for sq in (True, False):
        for _ in range(npts):
            qt = make_point(rng, E, square=sq)
            fm = FormalMachine(24 * Xs + 1, qt, E)
            try:
                fo = run(es_program, fm)
            except PrecisionError:
                out['precision'] += 1
                continue
            if not sq:
                out['nonsq_points'] += 1
                out['nonsq_success'] += fo[0] == 'SUCCESS'
                continue
            out['points'] += 1
            out['fail' if fo[0] == 'FAIL' else 'success'] += 1
            lam = {2, 3} | set(sp.primerange(2, sum(len(k) - 1 for k in fm.S) + 2))
            lam |= fm.Kprimes
            for k, C in fm.S.items():
                lam |= set(sp.primefactors(C))
                h = sp.Poly(list(k), Xs, domain=ZZ)
                if sp.expand(h.as_expr() - (24 * Xs + 1)) != 0:
                    Hh = int(sp.Rational(24) ** h.degree() * h.as_expr().subs(Xs, sp.Rational(-1, 24)))
                    lam |= set(sp.primefactors(Hh))
            if max(lam) <= max(E):
                out['lam_inside'] += 1
                out['lam_inside_success'] += fo[0] == 'SUCCESS'
    return out


class BrokenFloor(FormalMachine):
    """mutation: Lemma D without the [rho=0 and sigma<0] correction."""
    def divmod(self, A, Bp):
        fl, rem = super().divmod(A, Bp)
        Q, R = A.div(Bp)
        D = self.den(Q)
        rho = int((Q * D).eval(self.qt)) % D
        if rho == 0 and not R.is_zero and (R * Bp).LC() < 0:
            fl = fl + 1
            rem = A - Bp * fl
            self.log[-1] = ('divmod', fl, rem)
        return fl, rem


class BrokenOrder(FormalMachine):
    """mutation: formal divisors ordered by (degree, constant term) instead of eventually."""
    def _order(self, items, key):
        return sorted(items, key=lambda t: (key(t).degree(), key(t).eval(0)))


def mutation_check(seed=5):
    rng = random.Random(seed)
    E = {2: 10, 3: 6, 5: 4, 7: 3}
    M = prod(l ** e for l, e in E.items())
    det = 0
    for _ in range(300):
        A = P_(rng.randint(1, 5) * Xs + rng.randint(-20, 20))
        B = P_(rng.randint(1, 3) * Xs + rng.randint(-5, 5))
        qt = rng.randrange(M)
        fm = BrokenFloor(24 * Xs + 1, qt, E)
        prog = lambda m: m.divmod(A if isinstance(m, FormalMachine) else None, B)
        try:
            fl, rem = fm.divmod(A, B)
        except PrecisionError:
            continue
        q = qt + M * 10 ** 6
        a, b = int(A.eval(q)), int(B.eval(q))
        det += (a // b) != ev(fl, q)
    # order mutation on the ES program at a non-square point with admissible q
    rng2 = random.Random(2026)
    return dict(broken_floor_detected=det)


def ev_out_str(o):
    if isinstance(o, sp.Poly):
        return o.as_expr()
    if isinstance(o, tuple):
        return tuple(ev_out_str(x) for x in o)
    return o


def main():
    n1 = int(sys.argv[1]) if len(sys.argv) > 1 else 300
    k2 = int(sys.argv[2]) if len(sys.argv) > 2 else 2_000_000
    d = T1_lemmaD_direct(3000)
    print('Lemma D direct:', d)
    s = T1(n1)
    print('T1 random programs:', s)
    ok = d['mism'] == 0 and s['mism'] == 0
    for r in T2(k2):
        print('T2:', r)
        ok &= r['mismatches'] == 0 and r['char_formula_violations'] == 0
    t3 = T3(n1)
    print('T3 Theorem C scan:', t3)
    ok &= t3['lam_inside_success'] == 0
    print('mutation (harness has teeth):', mutation_check())
    print('OK' if ok else 'FAILED (see above)')


if __name__ == '__main__':
    main()
