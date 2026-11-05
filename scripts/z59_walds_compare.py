#!/usr/bin/env python3
"""z59 WALDS: Theorem W1 prediction vs the exact half-integral sweep.
For each sweep run (L = 4N, psi = (D/.), all odd squares as T1 rows, l0 = 0) compare the observed rank of the T1-kernel
on C1(2N) (coefficients n <= B) with the number of RATIONAL Gauss-exceptional eigensystems: elliptic-curve isogeny
classes E with conductor | 2N such that G = E (x) chi_{D'} (D' = disc Q(sqrt(-D))) has root number +1 and rank >= 2
(pari ellrank lower bound, rigorous, so L(G,1) = 0 by Gross-Zagier-Kolyvagin). W1 + Cor. 2 (rank <= 1 per eigensystem on
C1, memo Lemma W1') predict observed <= #rational exceptional + #irrational exceptional; equality expected.
'sat' = the T1 rows did not reach full rank (rank(cond) < #rows), i.e. the kernel is plausibly saturated.
Usage: python3 scripts/z59_walds_compare.py identify_file sweep_file1 [sweep_file2 ...]
"""
import re, sys


def sqfree_part(d):
    s, n, p = 1, abs(d), 2
    sign = -1 if d < 0 else 1
    while p * p <= n:
        while n % (p * p) == 0:
            n //= p * p
        if n % p == 0:
            s *= p
            n //= p
        p += 1
    return sign * s * n


def disc_of(d):  # fundamental discriminant of Q(sqrt d), d squarefree
    return d if d % 4 == 1 else 4 * d


ident = []
for line in open(sys.argv[1]):
    m = re.match(r"N=(\d+) a=(\[[^]]*\]) .*\| (.*)$", line)
    if not m:
        continue
    tw = {}
    for item in m[3].split():
        mm = re.match(r"(-?\d+):([+-]\d)/r(\d+)/\[(\d+),(\d+)\]", item)
        tw[int(mm[1])] = (int(mm[2]), int(mm[3]), int(mm[4]))
    ident.append((int(m[1]), m[2], tw))

print("L | D (psi) | D' (twist) | sat | observed rank on C1 | rational Gauss-exceptional phi (conductor | 2N) | match")
nm = nmis = 0
for fn in sys.argv[2:]:
    for line in open(fn):
        m = re.match(r"L=(\d+) N=(\d+) D=(-?\d+) (?:space=(\d+) )?dim=(\d+) B=(\d+) l0=(\d+) #T1-conditions=(\d+) rank\(cond\)=(\d+)", line)
        if m:
            cur = dict(L=int(m[1]), N=int(m[2]), D=int(m[3]), l0=int(m[7]), rows=int(m[8]), rc=int(m[9]))
            continue
        m = re.match(r"\s+rank of K on C1 \(n<=B, (\d+) indices\) = (\d+)", line)
        if m and cur["l0"] == 0:
            obs = int(m[2])
            Dp = disc_of(sqfree_part(-cur["D"]))
            pred = [f"{NE}{ai}" for NE, ai, tw in ident if (2 * cur["N"]) % NE == 0 and Dp in tw
                    and tw[Dp][0] == 1 and tw[Dp][2] >= 2]
            sat = cur["rc"] < cur["rows"]
            ok = (obs == len(pred))
            nm += ok
            nmis += (not ok)
            if obs or pred or not ok:
                print(f"{cur['L']} | {cur['D']} | {Dp} | {'sat' if sat else 'UNSAT'} | {obs} | {', '.join(pred) or '-'} | {'yes' if ok else 'NO'}")
print(f"# runs (l0=0) matching prediction: {nm}; not matching: {nmis} (all other matching runs have observed 0 = predicted 0)")
