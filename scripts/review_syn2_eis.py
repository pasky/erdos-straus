"""R193 from-scratch checks for SYNTHESIS_SPARKS2 §3 (order-3 TES over O = Z[ω]).

Own Z[ω] arithmetic (a + bω, ω² = −1 − ω), own cubic residue / tame Hilbert symbols; sympy only for factorint/isprime.
(1) Cor 3.4: (18/r)_3 for all prime elements r ≡ 10+ω (mod 18), N(r) ≤ NR; and whether (18/·)_3 factors through
    (O/18)^*/μ6 (ray class mod 18) on all degree-1 primes N ≤ NR.
(2) Thm 3.5 recipe at every 2-primary split prime π, N(π) ≤ NMAX (all 2-primary associates of all prime ideals):
    exact equation in K, 2-primarity, Type II shape at π, (N_q) at every q | Q, tame symbols at EVERY non-λ place
    (incl. the anchor 2) -> mute places 0, other tame places 0, inv_π, and Σ_tame = 0 (⇔ inv_λ = 0 by reciprocity).
(3) T1_3 control at cubes: n = π³, D = Q³ for 2-primary Q ∈ O, N(Q) ≤ QN: no divisor of n + 18D in the class g0.
(4) Plain single shot π + 18 (D = 1): how many 2-primary split primes have a divisor ≡ g0 (mod 18).
Usage: PYTHONPATH=scripts uv run --with sympy python scripts/review_syn2_eis.py [NMAX] [NR] [CUBE_NMAX] [QN]
"""
import sys
from fractions import Fraction as F
from itertools import product
from sympy import factorint, isprime

# ---------- O = Z[ω] ----------
def mul(x, y):
    a, b = x; c, d = y
    return (a * c - b * d, a * d + b * c - b * d)
def add(x, y): return (x[0] + y[0], x[1] + y[1])
def sub(x, y): return (x[0] - y[0], x[1] - y[1])
def neg(x): return (-x[0], -x[1])
def conj(x): a, b = x; return (a - b, -b)
def norm(x): a, b = x; return a * a - a * b + b * b
def smul(k, x): return (k * x[0], k * x[1])
OMEGA, OMEGA2, ONE = (0, 1), (-1, -1), (1, 0)
UNITS = [(1, 0), (0, 1), (-1, -1), (-1, 0), (0, -1), (1, 1)]
assert mul(OMEGA, OMEGA) == OMEGA2 and mul(OMEGA, OMEGA2) == ONE

def divexact(x, y):
    """x / y in O, or None."""
    n = norm(y); t = mul(x, conj(y))
    if t[0] % n or t[1] % n: return None
    return (t[0] // n, t[1] // n)

def divmod_(x, y):
    n = norm(y); t = mul(x, conj(y))
    q = ((2 * t[0] + n) // (2 * n), (2 * t[1] + n) // (2 * n))
    return q, sub(x, mul(q, y))

def gcd(x, y):
    while y != (0, 0):
        _, r = divmod_(x, y); x, y = y, r
    return x

def cong(x, y, m): return (x[0] - y[0]) % m == 0 and (x[1] - y[1]) % m == 0
def two_primary(x): return x[0] % 2 == 1 and x[1] % 2 == 0

# ---------- K = Q(ω) as pairs of Fractions ----------
def kf(x): return (F(x[0]), F(x[1]))
def kmul(x, y):
    a, b = x; c, d = y
    return (a * c - b * d, a * d + b * c - b * d)
def kinv(x):
    n = x[0] * x[0] - x[0] * x[1] + x[1] * x[1]
    c = (x[0] - x[1], -x[1]); return (c[0] / n, c[1] / n)
def kadd(x, y): return (x[0] + y[0], x[1] + y[1])
def kdiv(x, y): return kmul(x, kinv(y))
def k_to_O_den(x):
    """x = num/d with num ∈ O, d ∈ Z>0."""
    from math import lcm
    d = lcm(x[0].denominator, x[1].denominator)
    return (int(x[0] * d), int(x[1] * d)), d

# ---------- primes ----------
_cache = {}
def primes_above(p):
    """list of (prime element, residue info). info = ('deg1', s) with ω ≡ s mod π, or ('inert',) or ('lam',)."""
    if p in _cache: return _cache[p]
    if p == 3: res = [((1, -1), ('lam',))]
    elif p % 3 == 2: res = [((p, 0), ('inert',))]
    else:
        g = 2
        while True:
            s = pow(g, (p - 1) // 3, p)
            if s != 1: break
            g += 1
        pi = gcd((p, 0), (-s, 1))  # gcd(p, ω − s)
        assert norm(pi) == p
        out = []
        for P in (pi, conj(pi)):
            a, b = P
            sP = (-a * pow(b, -1, p)) % p
            assert (sP * sP + sP + 1) % p == 0
            out.append((P, ('deg1', sP)))
        res = out
    _cache[p] = res; return res

def val(P, x):
    if x == (0, 0): return 10 ** 9
    k = 0
    while True:
        q = divexact(x, P)
        if q is None: return k
        x = q; k += 1

def kval(P, x):
    num, d = k_to_O_den(x)
    return val(P, num) - val(P, (d, 0))

def all_primes_of(*elts):
    ps = set()
    for x in elts:
        num, d = k_to_O_den(x) if isinstance(x[0], F) else (x, 1)
        for p in set(factorint(norm(num))) | set(factorint(d)):
            for P, info in primes_above(p): ps.add((P, info))
    return ps

def red_power(x, P, info, e):
    """x ∈ O, P ∤ x: x^e mod P, returned as exponent k with x^e ≡ ω^k (must be a cube root of unity)."""
    if info[0] == 'deg1':
        p = norm(P); s = info[1]
        r = pow((x[0] + x[1] * s) % p, e, p)
        for k in range(3):
            if r == pow(s, k, p): return k
        raise ValueError("not a cube root of unity")
    q = P[0]  # inert rational prime
    acc, base, ee = ONE, (x[0] % q, x[1] % q), e
    while ee:
        if ee & 1: acc = mul(acc, base); acc = (acc[0] % q, acc[1] % q)
        base = mul(base, base); base = (base[0] % q, base[1] % q); ee >>= 1
    for k, w in enumerate((ONE, OMEGA, OMEGA2)):
        if cong(acc, w, q): return k
    raise ValueError("not a cube root of unity")

def unitpart(x, P):
    """x ∈ K^*, returns (u_num ∈ O, u_den ∈ O) P-units with x = P^v u_num/u_den."""
    num, d = k_to_O_den(x); dd = (d, 0)
    while (q := divexact(num, P)) is not None: num = q
    while (q := divexact(dd, P)) is not None: dd = q
    return num, dd

def tame(A, B, P, info):
    """cubic tame symbol (A,B)_P as exponent of ω; P ∤ 3."""
    N = norm(P); e = (N - 1) // 3
    va, vb = kval(P, A), kval(P, B)
    an, ad = unitpart(A, P); bn, bd = unitpart(B, P)
    # (-1)^{va vb} A^{vb} / B^{va}, as product of unit residues; -1 is a cube -> drop sign.
    k = vb * (red_power(an, P, info, e) - red_power(ad, P, info, e)) - va * (red_power(bn, P, info, e) - red_power(bd, P, info, e))
    return k % 3

def cubic_symbol(a, P, info):
    return red_power(a, P, info, (norm(P) - 1) // 3)

G0 = (10, 1)

def prime_elements(NR):
    """all prime elements (all 6 associates, both conjugates) of degree-1 primes with N ≤ NR."""
    for p in range(7, NR + 1, 6):
        if isprime(p):
            for P, info in primes_above(p):
                for u in UNITS:
                    yield mul(u, P), info, p

# ---------- (1) Cor 3.4 ----------
def part1(NR):
    vals = {}; table = {}; conflicts = 0; n_r = 0
    for r, info, p in prime_elements(NR):
        P = r
        c = cubic_symbol((18, 0), P, ('deg1', info[1]))
        key = (r[0] % 18, r[1] % 18)
        if key in table and table[key] != c: conflicts += 1
        table[key] = c
        if key == G0:
            n_r += 1; vals[c] = vals.get(c, 0) + 1
    print(f"(1) prime elements r ≡ 10+ω (18), N(r) ≤ {NR}: {n_r}; values of (18/r)_3 as ω^k: {vals}")
    print(f"    (18/·)_3 well defined on residues mod 18 over all degree-1 primes N ≤ {NR}: conflicts = {conflicts}"
          f" ({len(table)} residue classes seen)")
    # consistency over μ6-orbits: symbol depends only on the ideal, so classes c and u*c must agree
    orbit_conf = 0
    for key, c in table.items():
        for u in UNITS:
            k2 = mul(u, key); k2 = (k2[0] % 18, k2[1] % 18)
            if k2 in table and table[k2] != c: orbit_conf += 1
    print(f"    μ6-orbit consistency conflicts: {orbit_conf}")

# ---------- (2) Thm 3.5 recipe ----------
def solve(n, r, rinfo, D):
    E = divexact(add(n, smul(18, D)), r); assert E is not None
    a = divexact(add(r, OMEGA2), (9, 0)); assert a is not None
    x = divexact(add(mul(OMEGA, n), E), (9, 0)); assert x is not None
    y = mul(n, a)
    Z = mul(mul(n, x), a)
    return x, y, Z, a, E

def part2(NMAX):
    rlist = sorted(((p, r, info) for r, info, p in prime_elements(20000) if cong(r, G0, 18)), key=lambda t: t[0])
    tot = 0; maxNr = 0; maxQ = 0; invpi = {}; inv2 = {}; mute_places = 0; strong_fail = 0; bad = 0; other_tame_nonzero = 0
    for p in range(7, NMAX + 1, 6):
        if not isprime(p): continue
        for P, info in primes_above(p):
            for n in (P, neg(P), mul(OMEGA, P), mul(OMEGA2, P), neg(mul(OMEGA, P)), neg(mul(OMEGA2, P))):
                if not two_primary(n): continue
                tot += 1
                for (Nr, r, rinfo) in rlist:
                    if divexact(n, r) is not None: continue
                    if cubic_symbol(n, r, rinfo) == cubic_symbol((18, 0), r, rinfo): break
                else:
                    raise RuntimeError("no r found")
                maxNr = max(maxNr, Nr)
                s = rinfo[1]
                t_target = (-(n[0] + n[1] * s) * pow(18, -1, Nr)) % Nr
                t = next(t for t in range(1, Nr) if pow(t, 3, Nr) == t_target)
                Q = t
                while Q % 2 == 0 or Q % 3 == 0 or Q % p == 0: Q += Nr
                maxQ = max(maxQ, Q)
                D = (Q ** 3, 0)
                x, y, Z, a, E = solve(n, r, rinfo, D)
                # exact equation in K
                lhs = kdiv(kf((9, 0)), kf(n))
                rhs = kadd(kadd(kdiv(kf(OMEGA), kf(x)), kdiv(kf(OMEGA2), kf(y))), kdiv(kmul(kf((2, 0)), kf(D)), kf(Z)))
                ok = lhs == rhs and two_primary(x) and two_primary(y) and two_primary(Z) and two_primary(D)
                ok &= val(P, x) == 0 and val(P, y) >= 1 and val(P, Z) >= 1
                z = kdiv(kf(Z), kf(D))
                u1, u2, u3 = kdiv(kf(x), kf(OMEGA)), kdiv(kf(y), kf(OMEGA2)), kdiv(z, kf((2, 0)))
                A = kmul(kf((-1, 0)), kdiv(u1, u3)); B = kmul(kf((-1, 0)), kdiv(u2, u3))
                places = all_primes_of(A, B) | set(primes_above(2)) | {(P, info)}
                tsum = 0
                for (Pl, inf) in places:
                    if inf[0] == 'lam': continue
                    t3 = tame(A, B, Pl, inf); tsum += t3
                    if Pl == P: invpi[t3] = invpi.get(t3, 0) + 1
                    elif Pl == (2, 0): inv2[t3] = inv2.get(t3, 0) + 1
                    elif val(Pl, (Q, 0)) > 0:
                        mute_places += 1
                        vz = kval(Pl, z)
                        if vz < 0 and val(Pl, x) == 0 and vz % 3: ok = False
                        if vz < 0 and vz % 3: strong_fail += 1
                        if t3: ok = False
                    elif t3: other_tame_nonzero += 1
                if tsum % 3: ok = False
                if not ok: bad += 1
    print(f"(2) 2-primary split primes N ≤ {NMAX}: {tot} solved; failures {bad}; max N(r) = {maxNr}; max Q = {maxQ}")
    print(f"    inv_π (exp. of ω) distribution {invpi}; inv_2 {inv2}; mute places checked {mute_places}; "
          f"of which violate the STRONG normalisation (3 | v_q(z) whenever < 0): {strong_fail}; "
          f"nonzero symbols at other tame places {other_tame_nonzero}; Σ_tame ≡ 0 required (⇔ inv_λ = 0)")

# ---------- divisors in class g0 ----------
def factor_elt(x):
    fac = []
    for p in factorint(norm(x)):
        for P, info in primes_above(p):
            k = val(P, x)
            if k: fac.append((P, k))
    return fac

def has_div_g0(x):
    fac = factor_elt(x)
    for exps in product(*[range(k + 1) for _, k in fac]):
        d = ONE
        for (P, _), e in zip(fac, exps):
            for _ in range(e): d = mul(d, P)
        for u in UNITS:
            if cong(mul(u, d), G0, 18): return True
    return False

def part3(CN, QN, cube=True):
    shots = hits = 0
    Qs = [(a, b) for a in range(-12, 13) for b in range(-12, 13) if two_primary((a, b)) and 0 < norm((a, b)) <= QN]
    for p in range(7, CN + 1, 6):
        if not isprime(p): continue
        for P, info in primes_above(p):
            for n0 in (P, neg(P)):
                if not two_primary(n0): continue
                n = mul(mul(n0, n0), n0)
                for Qe in Qs:
                    if norm(Qe) % 3 == 0 or norm(Qe) % p == 0: continue
                    D = mul(mul(Qe, Qe), Qe) if cube else Qe
                    shots += 1
                    if has_div_g0(add(n, smul(18, D))): hits += 1
    print(f"(3{'' if cube else '-control: D = Q NOT a cube'}) cubes n = π³ (all 2-primary π, N(π) ≤ {CN}), D = Q³, Q 2-primary in O, N(Q) ≤ {QN}, prime to 6n:"
          f" {shots} shots, {hits} with a divisor ≡ g0 (mod 18)")

def part4(NMAX):
    tot = fire = 0; ideals_fire = set()
    for p in range(7, NMAX + 1, 6):
        if not isprime(p): continue
        for P, info in primes_above(p):
            for n in (P, neg(P), mul(OMEGA, P), mul(OMEGA2, P), neg(mul(OMEGA, P)), neg(mul(OMEGA2, P))):
                if not two_primary(n): continue
                tot += 1
                if has_div_g0(add(n, (18, 0))): fire += 1; ideals_fire.add(P)
    print(f"(4) single shot n + 18: fires for {fire} of {tot} 2-primary split primes ({len(ideals_fire)} prime ideals)")

if __name__ == "__main__":
    NMAX = int(sys.argv[1]) if len(sys.argv) > 1 else 6000
    NR = int(sys.argv[2]) if len(sys.argv) > 2 else 20000
    CN = int(sys.argv[3]) if len(sys.argv) > 3 else 200
    QN = int(sys.argv[4]) if len(sys.argv) > 4 else 100
    part1(NR); part2(NMAX); part3(CN, QN); part3(CN, QN, cube=False); part4(NMAX)
