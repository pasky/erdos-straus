#!/usr/bin/env python3
"""POINTWISE_MN2 §4: density delta_m(Q(q0)) of Type-II-hard unit classes modulo
Q(q0) = lcm{ prime powers q <= q0 with prime not dividing m }.
Stand-alone (numpy + sympy only).  usage: mn2_delta.py m q0 [q0 ...]
Hard: r unit mod Q and r mod M != -mD mod M for every M | Q, M >= 3, M = -1 (m), D | A^2, A=(M+1)/m.
Also prints 1/delta and q0^(-1/2)/delta (Theorem 3.1 needs C_nu * q0^(-1/2+eps) small)."""
import sys
import numpy as np
from sympy import factorint, divisors, primerange


def Qof(m, q0):
    Q = 1
    for p in primerange(2, q0 + 1):
        if m % p == 0:
            continue
        pe = p
        while pe * p <= q0:
            pe *= p
        Q *= pe
    return Q


def delta(m, q0):
    Q = Qof(m, q0)
    arr = np.ones(Q, dtype=bool)
    for p in factorint(Q):
        arr[0::p] = False
    phi = int(arr.sum())
    nat = 0
    for M in divisors(Q):
        if M < 3 or M % m != m - 1:
            continue
        nat += 1
        A = (M + 1) // m
        for D in divisors(A * A):
            arr[(-m * D) % M::M] = False
    h = int(arr.sum())
    return Q, phi, h, nat


def main():
    m = int(sys.argv[1])
    for q0 in map(int, sys.argv[2:]):
        Q, phi, h, nat = delta(m, q0)
        d = h / phi
        print(f"m={m} q0={q0} Q={Q} phi={phi} moduli={nat} |H|={h} delta={d:.6g} "
              f"1/delta={1/d:.4g} q0^-0.5/delta={q0**-0.5/d:.4g}", flush=True)


if __name__ == "__main__":
    main()
