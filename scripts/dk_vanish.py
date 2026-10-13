"""O169 §4: vanishing set of the HJ-length-3 X-slice counts over ALL odd n <= N.
a0(n) = #{n/A=[[v,t,u]] : 4 | A}  (Type I a=1 slice),  aT(n) = #{... : 4 | t}  ((A)3 Type II slice).
Prop 3.1: for n = 1 (4) both vanish at odd squares. Question: which NON-square n = 1 (4) have a0 = 0 (resp. a0+aT = 0)?
Usage: PYTHONPATH=scripts uv run python scripts/dk_vanish.py N
"""
import sys
from math import isqrt, gcd
N = int(sys.argv[1])
a0 = bytearray(N + 1); aT = bytearray(N + 1)
t = 2
while 4 * t - 4 <= N:
    u = 2
    while 2 * (t * u - 1) - u <= N:
        A = t * u - 1
        v = 2
        while True:
            n = v * A - u
            if n > N:
                break
            if A % 4 == 0 and a0[n] < 255: a0[n] += 1
            if t % 4 == 0 and aT[n] < 255: aT[n] += 1
            v += 1
        u += 1
    t += 1
z0, z0T = [], []
for n in range(5, N + 1, 4):
    if isqrt(n) ** 2 == n:
        assert a0[n] == 0 and aT[n] == 0, n
        continue
    if a0[n] == 0: z0.append(n)
    if a0[n] == 0 and aT[n] == 0: z0T.append(n)
def fac(n):
    f, q = [], 2
    while q * q <= n:
        while n % q == 0: f.append(q); n //= q
        q += 1
    if n > 1: f.append(n)
    return f
print(f"N={N}: non-square n=1(4) with a0(n)=0: {len(z0)}; with a0=aT=0: {len(z0T)}")
print("a0=aT=0 list (n: factorisation):", [(n, fac(n)) for n in z0T[:60]])
print("largest a0=0:", z0[-10:])
