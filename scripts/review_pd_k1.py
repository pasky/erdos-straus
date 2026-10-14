#!/usr/bin/env python3
"""R209 from-scratch check of PHASE_DIAGRAM §3 EVIDENCE (k = 1 slice).

k = 1 slice (derived independently): g = 3 (mod 4) | 4n + Q1^2, Q0 = (g+1)/4, Q = Q0*Q1; then g | n + 4Q^2
(4Q0 = 1 mod g).  Overflow = Q1 when gcd(Q1, 1) = 1 (always).  Mute condition rad(Q1) | Q0, cap e = max v_l(Q1).
Mode 'cap'  n...: for odd Q1 <= L prime to n, list k=1 shots and their cap e; report counts / max Q1 / bit-lengths.
Mode 'three' P A: for each prime 5 <= p < P, least a <= A with a k=1 shot with Q1 = 3^a (histogram); + square control.
Factorisations by GNU coreutils `factor` in batch (C, independent of the author's code); every shot is
re-verified with exact rationals.
"""
import sys, subprocess
from fractions import Fraction as F
from math import gcd
from collections import Counter
from sympy import primerange


def factor_batch(nums):
    out = subprocess.run(["factor"], input="\n".join(map(str, nums)) + "\n", capture_output=True,
                         text=True, check=True).stdout.splitlines()
    assert len(out) == len(nums)
    res = []
    for line, N in zip(out, nums):
        lhs, rhs = line.split(":")
        assert int(lhs) == N
        fs = Counter(int(t) for t in rhs.split())
        P = 1
        for p, e in fs.items():
            P *= p ** e
        assert P == N
        res.append(fs)
    return res


def divisors_from(fs):
    ds = [1]
    for p, e in fs.items():
        ds = [d * p ** i for d in ds for i in range(e + 1)]
    return ds


def verify(n, Q, g, Q1):
    num = n * (g + 1) + 4 * Q * Q
    assert num % (4 * g) == 0
    x = num // (4 * g); y = n * (g + 1) // 4
    z = 1 / (F(4, n) - F(1, x) - F(1, y))
    assert z > 0 and z.denominator == Q1 * Q1 and y % rad_and_cap(Q1)[0] == 0
    assert F(4, n) == F(1, x) + F(1, y) + 1 / z


def rad_and_cap(m):
    r, e, p = 1, 0, 3
    while p * p <= m:
        if m % p == 0:
            c = 0
            while m % p == 0:
                m //= p; c += 1
            r *= p; e = max(e, c)
        p += 2
    if m > 1:
        r *= m; e = max(e, 1)
    return r, e


def mode_cap(ns, L):
    for n in ns:
        Q1s = [q for q in range(1, L + 1, 2) if gcd(q, n) == 1]
        hits = {}
        CH = 20000
        for i in range(0, len(Q1s), CH):
            chunk = Q1s[i:i + CH]
            for Q1, fs in zip(chunk, factor_batch([4 * n + q * q for q in chunk])):
                r, e = rad_and_cap(Q1)
                mod = 4 * r
                for g in divisors_from(fs):
                    if g % mod != mod - 1:
                        continue
                    Q0 = (g + 1) // 4
                    if gcd(Q0, n) != 1:
                        continue
                    verify(n, Q0 * Q1, g, Q1)
                    hits.setdefault(e, []).append(Q1)
        for e in sorted(hits):
            qs = sorted(set(hits[e]))
            bl = sorted(set(q.bit_length() for q in qs))
            print(f"n={n} cap={e}: {len(hits[e])} shots, {len(qs)} distinct Q1, max Q1={qs[-1]}"
                  + (f", bit-lengths {bl}" if e >= 2 else ""))
        if not hits:
            print(f"n={n}: no k=1 ES^(y) shot with Q1 <= {L}")


def mode_three(P, A):
    def least_a(p):
        for a in range(A + 1):
            fs = factor_batch([4 * p + 9 ** a])[0]
            mod = 4 if a == 0 else 12
            for g in divisors_from(fs):
                if g % mod == mod - 1 and gcd((g + 1) // 4, p) == 1:
                    verify(p, (g + 1) // 4 * 3 ** a, g, 3 ** a)
                    return a
        return None
    # batch over a for speed: process level by level
    todo = [p for p in primerange(5, P)]
    hist = Counter()
    for a in range(A + 1):
        if not todo:
            break
        mod = 4 if a == 0 else 12
        nxt = []
        for i in range(0, len(todo), 20000):
            chunk = todo[i:i + 20000]
            for p, fs in zip(chunk, factor_batch([4 * p + 9 ** a for p in chunk])):
                ok = False
                for g in divisors_from(fs):
                    if g % mod == mod - 1 and gcd((g + 1) // 4, p) == 1:
                        verify(p, (g + 1) // 4 * 3 ** a, g, 3 ** a); ok = True; break
                if ok:
                    hist[a] += 1
                else:
                    nxt.append(p)
        todo = nxt
    print("least-a histogram:", dict(sorted(hist.items())), "unresolved:", todo[:10], len(todo))
    # square control
    sq = [m * m for m in range(3, int(P ** 0.5) + 1, 2) if m % 3]
    bad = 0
    for a in range(A + 1):
        mod = 4 if a == 0 else 12
        for N2, fs in zip(sq, factor_batch([4 * s + 9 ** a for s in sq])):
            if any(g % mod == mod - 1 for g in divisors_from(fs)):
                bad += 1
    print(f"square control: {len(sq)} odd squares m^2 < {P} (3 !| m), a <= {A}: hits {bad}")


if __name__ == "__main__":
    if sys.argv[1] == "cap":
        mode_cap([int(t) for t in sys.argv[3:]], int(sys.argv[2]))
    else:
        mode_three(int(sys.argv[2]), int(sys.argv[3]))
