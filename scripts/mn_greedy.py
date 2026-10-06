#!/usr/bin/env python3
"""POINTWISE_MN §3 experiment: greedy random hard class, primes in increasing order.
All atoms (M <= T, M = -1 mod m, D | A^2) are grouped by P = largest prime of M.
Processing primes l = 2,3,5,... we fix r mod l^e (e = max v_l(M), M <= T, M = -1 mod m)
uniformly among the units mod l^e (mode 'unit') or among the 2-adic/odd squares (mode 'sq')
that do not complete a consistent atom, i.e. avoid x = c mod l^v for every atom with
P(M) = l, M = l^v M', c = r mod M'.  Records the forbidden fraction f_l (within the mode's
candidate set) and whether the process dies (f_l = 1).
usage: mn_greedy.py m T mode seed [maxprint]"""
import sys, random
from math import gcd
from pointwise_omega_S import spf_table, factor, divisors_from


def main():
    m, T, mode, seed = int(sys.argv[1]), int(sys.argv[2]), sys.argv[3], int(sys.argv[4])
    rng = random.Random(seed)
    L0 = 0
    if mode.startswith('unit1:'):
        L0 = int(mode.split(':')[1]); mode = 'unit'
    spf = spf_table(T + 8)
    byP = {}
    emax = {}
    for M in range(m - 1, T + 1, m):
        if M < 3: continue
        fM = factor(M, spf); P = max(fM)
        for l, v in fM.items(): emax[l] = max(emax.get(l, 0), v)
        A = (M + 1) // m
        fa = {p: 2 * e for p, e in factor(A, spf).items()} if A > 1 else {}
        v = fM[P]; q = P ** v; Mp = M // q
        cl = byP.setdefault(P, [])
        for D in divisors_from(fa):
            cl.append((Mp, q, (-m * D) % M))
    r, Q = 0, 1  # r mod Q
    if mode.startswith('pref:'):
        # r_0 uniform on the hard set of the L0-smooth subsystem (rejection sampling)
        L0 = int(mode.split(':')[1]); mode = 'unit'
        small = [l for l in sorted(emax) if l <= L0]
        Q0 = 1
        for l in small: Q0 *= l ** emax[l]
        sm = [(Mp * q, c) for l in small for Mp, q, c in byP.get(l, [])]
        tries = 0
        while True:
            tries += 1
            x = rng.randrange(1, Q0)
            if any(x % l == 0 for l in small): continue
            if all(x % MM != c for MM, c in sm): break
        r, Q = x, Q0
        print(f"   prefix L0={L0}: Q0={Q0} accepted after {tries} unit draws")
        L0 = -1
    out = []; dead = None; big = []
    for l in sorted(emax):
        if Q % l == 0: continue
        e = emax[l]; L = l ** e
        if mode == 'sq':
            if l == 2: cand = [x for x in range(1, L, 2) if (e == 1 or (e == 2 and x % 4 == 1) or x % 8 == 1)]
            else:
                sq = {(y * y) % l for y in range(1, l)}
                cand = [x for x in range(1, L) if x % l in sq]
        else:
            cand = [x for x in range(1, L) if x % l]
        forb = {}
        for Mp, q, c in byP.get(l, []):
            if c % Mp == r % Mp: forb.setdefault(q, set()).add(c % q)
        ok = [x for x in cand if not any(x % q in s for q, s in forb.items())]
        f = 1 - len(ok) / len(cand)
        out.append((l, f))
        if not ok: dead = l; break
        if l <= L0:
            assert 1 in ok; x = 1
        else:
            x = rng.choice(ok)
        # CRT r mod Q, x mod L
        r = (r + Q * ((x - r) * pow(Q, -1, L) % L)) % (Q * L); Q *= L
        if f > 0.5: big.append((l, round(f, 3)))
    import math
    lam = [(l, 1 / (1 - f)) for l, f in out if f < 1]
    mx = max(lam, key=lambda t: t[1]) if lam else None
    s50 = sum(math.log(x) for l, x in lam if l > 50)
    s_all = sum(math.log(x) for l, x in lam)
    print(f"   Lambda: max={mx[0]},{mx[1]:.2f}  sum log Lambda: all={s_all:.2f}  l>50: {s50:.2f}  "
          f"l>1000: {sum(math.log(x) for l, x in lam if l > 1000):.3f}  max_(l>50) l*f/log(l)^3="
          f"{max((l*f/math.log(l)**3 for l, f in out if l > 50), default=0):.3f}")
    nb = sum(1 for l, f in out if f > 0)
    print(f"m={m} T={T} mode={mode} seed={seed}: primes processed={len(out)} dead_at={dead} "
          f"f>0 at {nb} primes; f>1/2 at {big[:30]}")
    print("   first f_l:", [(l, round(f, 3)) for l, f in out[:25]])
    tail = [(l, round(f, 4)) for l, f in out if f > 0 and l > 50][:25]
    print("   f_l>0 with l>50:", tail)


if __name__ == "__main__":
    main()
