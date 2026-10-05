#!/usr/bin/env python3
"""POINTWISE_XWIN.md machine checks (O32).

  halfset AMAX           : orbit structure, |S_sigma| = phi(a)/2, #selections = 2^beta(a)
  lemma11 AMAX XMAX      : every x<=XMAX (gcd(x,a)=1) with -1 notin Rat_a(x) has C(x) inside some S_sigma
  rho AMAX KMAX NS SEED  : Monte-Carlo rho_k vs Lemma 2.1 bound 3n 3^-k + 9/4 t (5/9)^k
"""
import sys
import random
from math import gcd
from sympy import factorint, totient, primefactors


def units(a):
    return [g for g in range(1, a) if gcd(g, a) == 1]


def orbits(a):
    seen, orbs = set(), []
    for g in units(a):
        if g in seen:
            continue
        gi = pow(g, -1, a)
        o = sorted({g, gi, (-g) % a, (-gi) % a})
        seen.update(o)
        orbs.append((g, o))
    return orbs


def halves(a):
    """list of (half_plus, half_minus) per orbit; orbit {1,-1} gives ({1},{})"""
    hs = []
    for g, o in orbits(a):
        gi = pow(g, -1, a)
        hp = sorted({g, gi})
        hm = sorted({(-g) % a, (-gi) % a})
        if 1 in o:
            hs.append(([1], None))
        else:
            hs.append((hp, hm))
    return hs


def beta(a):
    phi = int(totient(a))
    w = len(primefactors(a))
    return (phi - 2 ** w) // 4 + 2 ** (w - 1) - 1


def halfset(AMAX):
    bad = 0
    for a in range(3, AMAX + 1, 4):
        phi = int(totient(a))
        hs = halves(a)
        nsel = 1
        size = 0
        for hp, hm in hs:
            if hm is not None:
                assert len(hp) == len(hm), (a, hp, hm)
                assert not set(hp) & set(hm)
                nsel *= 2
            size += len(hp)
        ok = (size * 2 == phi) and (nsel == 2 ** beta(a))
        bad += not ok
    print(f"halfset: a<= {AMAX}, a=3 mod 4: violations {bad}")
    return bad


def rat_set(fac, a):
    S = {1}
    for r, e in fac.items():
        rr = r % a
        ri = pow(rr, -1, a)
        new = set(S)
        for s in S:
            u, v = s, s
            for _ in range(e):
                u = u * rr % a
                v = v * ri % a
                new.add(u)
                new.add(v)
        S = new
    return S


def admissible(C, a):
    """C inside some S_sigma <=> -1 notin C and no g,h in C with gh=-1 or g/h=-1"""
    m1 = a - 1
    if m1 in C:
        return False
    for g in C:
        if (-g) % a in C:
            return False
        if (-pow(g, -1, a)) % a in C:
            return False
    return True


def in_some_halfset(C, a):
    for hp, hm in halves(a):
        inp = any(c in hp for c in C)
        inm = hm is not None and any(c in hm for c in C)
        if hm is None:
            orb = set(hp) | {a - 1}
            if any(c == a - 1 for c in C):
                return False
            continue
        if inp and inm:
            return False
    return True


def lemma11(AMAX, XMAX):
    tot = fails = viol = 0
    for a in range(3, AMAX + 1, 4):
        for x in range(1, XMAX + 1):
            if gcd(x, a) != 1:
                continue
            fac = factorint(x)
            R = rat_set(fac, a)
            tot += 1
            if (a - 1) not in R:
                fails += 1
                C = {r % a for r in fac}
                if not (admissible(C, a) and in_some_halfset(C, a)):
                    viol += 1
    print(f"lemma11: a<={AMAX}, x<={XMAX}: windows {tot}, -1 missing {fails}, violations {viol}")
    return viol


def sigma_pm(cs, a):
    S = {1}
    for c in cs:
        ci = pow(c, -1, a)
        S = S | {s * c % a for s in S} | {s * ci % a for s in S}
    return S


def rho(AMAX, KMAX, NS, seed):
    rnd = random.Random(seed)
    viol = 0
    print("a  n  t   k  rho_hat   bound    (2^-k * #idx2-avoiders lower ref)")
    for a in range(7, AMAX + 1, 4):
        U = units(a)
        n = len(U)
        t = 2 ** len(primefactors(a))
        for k in range(1, KMAX + 1):
            bad = 0
            for _ in range(NS):
                cs = [rnd.choice(U) for _ in range(k)]
                if (a - 1) not in sigma_pm(cs, a):
                    bad += 1
            rh = bad / NS
            bd = 3 * n * 3.0 ** (-k) + 2.25 * t * (5 / 9) ** k
            # allow 4 sigma Monte-Carlo slack
            se = (max(rh, 1 / NS) * (1 - rh) / NS) ** 0.5
            if rh - 4 * se > bd:
                viol += 1
            if k in (2, 4, 6, 8, 10, 12, 14, 16) or k == KMAX:
                print(f"{a:3d} {n:3d} {t:2d} {k:3d} {rh:.5f} {min(bd,9.99):.5f}")
    print(f"rho: violations of Lemma 2.1 bound (4-sigma): {viol}")
    return viol


if __name__ == "__main__":
    mode = sys.argv[1]
    if mode == "halfset":
        v = halfset(int(sys.argv[2]))
    elif mode == "lemma11":
        v = lemma11(int(sys.argv[2]), int(sys.argv[3]))
    elif mode == "rho":
        v = rho(int(sys.argv[2]), int(sys.argv[3]), int(sys.argv[4]), int(sys.argv[5]))
    else:
        sys.exit("unknown mode")
    sys.exit(1 if v else 0)
