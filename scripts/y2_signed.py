r"""y2_signed: signed words (letters in [-L,L]\{0}) at odd squares N: zero-mod-4 quiddities exist? and does the
even-edge law (h'/N) = (-1/N)(-1)^[8|ee'] survive with |.| conventions?  usage: y2_signed.py L"""
import sys
from y2_even_edge import jacobi
from math import isqrt
L = int(sys.argv[1]); R = range(-L, L + 1)
zero_sq = set(); bad = 0; tot = 0
for c in R:
    for m in R:
        for s in R:
            if 0 in (c, m, s): continue
            N = m * c * s - c - s
            if N <= 1 or N % 2 == 0: continue
            q = (m * s - 1, c, m, s, c * m - 1)
            if any(x == 0 for x in q): continue
            tot += 1
            if isqrt(N) ** 2 == N and any(x % 4 == 0 for x in q):
                zero_sq.add(N)
            ev = [x for x in q if x % 2 == 0]
            law = (jacobi((m*s-1) % N, N) == jacobi(-1, N) * (-1 if (ev[0]*ev[1]) % 8 == 0 else 1))
            bad += (not law) and min(q) > 0
            if not law and min(q) < 0: pass
print("signed words:", tot, "| odd squares with a zero-mod-4 signed word:", sorted(zero_sq)[:12], "| positive-word law failures:", bad)
