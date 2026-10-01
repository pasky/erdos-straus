#!/usr/bin/env python3
"""POINTWISE_SIZE.md section 7: the independence-model exponent
   I(T) = sum_{M<=T, M=3(4)} -log(1-h_M),  h_M = |R(M) cap hard units| / #hard units mod M,
where R(M) = {-4D mod M : D | ((M+1)/4)^2} and 'hard' means n = 1 (mod 3) when 3 | M.
Usage: uv run python scripts/pointwise_size_indep.py TMAX"""
import sys, json
from math import log
from sympy import factorint, totient

TMAX = int(sys.argv[1])
out, I, t = {}, 0.0, 7
for M in range(3, TMAX + 1, 4):
    while t < M:
        out[t] = round(I, 4); t = 2 * t + 1
    A = (M + 1) // 4
    divs = [1]
    for l, e in factorint(A).items():
        divs = [d * l ** i for d in divs for i in range(2 * e + 1)]
    cls = {(-4 * D) % M for D in divs}
    units = int(totient(M))
    if M % 3 == 0:
        cls = {c for c in cls if c % 3 == 1}
        units //= 2
    h = len(cls) / units
    I += -log(1 - h)
while t <= TMAX:
    out[t] = round(I, 4); t = 2 * t + 1
print(json.dumps(out))
