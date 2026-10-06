"""R74 from-scratch check of POINTWISE_MN2 §4 table: density of Type-II-hard units mod Q(q0).

Q(q0) = lcm{ l^k <= q0 : l prime, l not dividing m }.
H_m(Q) = { r in (Z/Q)^x : for all M | Q, M = -1 (mod m), M >= 3, and all D | A^2 (A=(M+1)/m):
           r != -m D (mod M) }.
Independent implementation: tensor over CRT coordinates (units mod each l^e || Q), each
modulus M | Q contributes an outer-product-free broadcast of its forbidden mask.
Usage: review_mn2_delta.py m q0 [q0 ...]
"""
import sys
from math import gcd
from fractions import Fraction
import numpy as np


def primes_upto(n):
    return [p for p in range(2, n + 1) if all(p % d for d in range(2, int(p ** 0.5) + 1))]


def divisors(n):
    ds = [1]
    x = n
    p = 2
    fac = {}
    while p * p <= x:
        while x % p == 0:
            fac[p] = fac.get(p, 0) + 1
            x //= p
        p += 1
    if x > 1:
        fac[x] = fac.get(x, 0) + 1
    for p, e in fac.items():
        ds = [d * p ** k for d in ds for k in range(e + 1)]
    return ds


def run(m, q0):
    pp = []  # (l, e) with l^e || Q
    for l in primes_upto(q0):
        if m % l == 0:
            continue
        e = 0
        while l ** (e + 1) <= q0:
            e += 1
        pp.append((l, e))
    Q = 1
    for l, e in pp:
        Q *= l ** e
    axes = [[u for u in range(l ** e) if u % l] for l, e in pp]
    shape = tuple(len(a) for a in axes)
    killed = np.zeros(shape, dtype=bool)
    # enumerate M | Q via exponent vectors
    def rec(i, M, expo):
        if i == len(pp):
            yield M, list(expo)
            return
        l, e = pp[i]
        for b in range(e + 1):
            expo.append(b)
            yield from rec(i + 1, M * l ** b, expo)
            expo.pop()
    nM = 0
    for M, expo in rec(0, 1, []):
        if M < 3 or (M + 1) % m:
            continue
        A = (M + 1) // m
        classes = {(-m * D) % M for D in divisors(A * A)}
        assert all(gcd(c, M) == 1 for c in classes)
        nM += 1
        # forbidden mask on sub-axes: for axis i with b_i>0, index by u mod l^b_i
        sub = [i for i, b in enumerate(expo) if b > 0]
        subshape = [len(axes[i]) for i in sub]
        mask = np.zeros(subshape, dtype=bool)
        # residues of each axis value mod l^b
        red = [np.array([u % pp[i][0] ** expo[i] for u in axes[i]]) for i in sub]
        for c in classes:
            sel = [red[k] == c % pp[i][0] ** expo[i] for k, i in enumerate(sub)]
            outer = sel[0]
            for s in sel[1:]:
                outer = np.logical_and.outer(outer, s)
            mask |= outer
        # broadcast into full shape
        full_shape = [shape[i] if i in sub else 1 for i in range(len(pp))]
        killed |= mask.reshape(full_shape)
    hard = int((~killed).sum())
    tot = int(np.prod(shape))
    return Q, tot, hard, nM


if __name__ == "__main__":
    m = int(sys.argv[1])
    for q0 in map(int, sys.argv[2:]):
        Q, tot, hard, nM = run(m, q0)
        d = Fraction(hard, tot)
        print(f"m={m} q0={q0} Q={Q} phi={tot} hard={hard} delta={d} 1/delta={float(1/d):.4g} "
              f"q0^-1/2/delta={float(q0**-0.5/d):.4g} (#M={nM})", flush=True)
