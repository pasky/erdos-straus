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
    out = []; dead = None; big = []
    for l in sorted(emax):
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
        x = rng.choice(ok)
        # CRT r mod Q, x mod L
        r = (r + Q * ((x - r) * pow(Q, -1, L) % L)) % (Q * L); Q *= L
        if f > 0.5: big.append((l, round(f, 3)))
    nb = sum(1 for l, f in out if f > 0)
    print(f"m={m} T={T} mode={mode} seed={seed}: primes processed={len(out)} dead_at={dead} "
          f"f>0 at {nb} primes; f>1/2 at {big[:30]}")
    print("   first f_l:", [(l, round(f, 3)) for l, f in out[:25]])
    tail = [(l, round(f, 4)) for l, f in out if f > 0 and l > 50][:25]
    print("   f_l>0 with l>50:", tail)


if __name__ == "__main__":
    main()
