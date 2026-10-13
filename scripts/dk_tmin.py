"""O169 §10: t_min(p) = least middle entry t of a Jacobi -1 length-3 word for p (primes p = 1 (8) <= N).
Usage: uv run python scripts/dk_tmin.py N
"""
import sys
from math import isqrt, log
N = int(sys.argv[1])
tmin = [0] * (N + 1)
t = 2
while 4 * t - 4 <= N:
    u = 2
    while 2 * (t * u - 1) - u <= N:
        A = t * u - 1; v = 2
        while (n := v * A - u) <= N:
            if not tmin[n] and (A % 4 == 0 or (t*v-1) % 4 == 0 or t % 4 == 0 or u % 4 == 0 or v % 4 == 0):
                tmin[n] = t
            v += 1
        u += 1
    t += 1
sv = bytearray([1]) * (N + 1); sv[0] = sv[1] = 0
for i in range(2, isqrt(N) + 1):
    if sv[i]: sv[i*i::i] = bytearray(len(sv[i*i::i]))
rec = 0
for p in range(17, N + 1, 8):
    if sv[p] and tmin[p] > rec:
        rec = tmin[p]; print("record", p, rec, "t/log^2 p = %.2f" % (rec / log(p) ** 2))
