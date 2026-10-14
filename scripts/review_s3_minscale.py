"""R207: least Type II modulus h_min(p) (h = 3 mod 4, -p = 4c^2 d mod h with cd | (h+1)/4) and least prime
g = 3 (4) with (p/g) = -1, for primes p = 1 (4), 5 <= p < N. Usage: N"""
import sys
from math import log, isqrt
N = int(sys.argv[1])
sv = bytearray([1]) * N; sv[0:2] = b"\0\0"
for i in range(2, isqrt(N) + 1):
    if sv[i]: sv[i*i::i] = bytearray(len(sv[i*i::i]))
def divs(k):
    out = []
    for a in range(1, isqrt(k) + 1):
        if k % a == 0:
            out.append(a)
            if a * a != k: out.append(k // a)
    return out
best = (0, 0); worst = (0, 0); hm = []; gmax = (0, 0)
for p in range(5, N, 4):
    if not sv[p]: continue
    h = 3
    while True:
        k = (h + 1) // 4; t = (-p) % h
        if any((4 * c * c * (m // c)) % h == t for m in divs(k) for c in divs(m)):
            break
        h += 4
    hm.append(h)
    r = h / log(p) ** 3
    if r > best[0]: best = (r, p, h)
    if h > worst[0]: worst = (h, p)
    g = 3
    while not (sv[g] and pow(p, (g - 1) // 2, g) == g - 1): g += 4
    if g / log(p) ** 2 > gmax[0]: gmax = (g / log(p) ** 2, p, g)
hm.sort()
print(f"N={N} primes={len(hm)} max h_min={worst} max h_min/log^3 p={best} median={hm[len(hm)//2]} "
      f"mean={sum(hm)/len(hm):.2f} p99={hm[int(.99*len(hm))]} max g_box/log^2 p={gmax}")
