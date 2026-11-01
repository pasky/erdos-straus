"""z52d avenue Q10 (Z2990): is R(p)/2 mod m (m = 2, 3, 4) determined by p mod M (M = 24, 120, 840)?
R(n) = #{(u,B,C) : 4uBC - u - B = n} computed for all n <= N by arithmetic-progression slices.
Run: timeout 60 python3 scripts/z52d_avenue_Q10_rparity.py   (N = 3e5, ~3 s)"""
import numpy as np
N = 300000
R = np.zeros(N + 1, dtype=np.int32)
u = 1
while 3 * u - 1 <= N:
    B = 1
    while 4 * u * B - u - B <= N:
        R[4 * u * B - u - B::4 * u * B] += 1
        B += 1
    u += 1
s = np.ones(N + 1, bool); s[:2] = 0
for i in range(2, int(N ** .5) + 1):
    if s[i]: s[i * i::i] = 0
ps = [int(p) for p in np.nonzero(s)[0] if p % 4 == 1 and p >= 5]
print('(*) zeros among primes = 1 (4):', [p for p in ps if R[p] == 0])
print('R(p) always even:', all(R[p] % 2 == 0 for p in ps))
for M in (24, 120, 840):
    for m in (2, 3, 4):
        d = {}
        for p in ps:
            if p > 1000: d.setdefault(p % M, set()).add(int(R[p] // 2) % m)
        print(f'M={M} m={m}: classes={len(d)} classes with constant R/2 mod m: {[a for a in d if len(d[a]) == 1]}')
