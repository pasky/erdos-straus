"""O169 §8: sign structure of the Jacobi character on length-3 HJ words.
(i) +1 / -1 cells mod 4 (n = 1 mod 4); (ii) action of rotation (v,t,u)->(t,u,v) [n -> n+u-t] on signs, cellwise mod 8;
(iii) for primes p = 1 (8) <= N: |L3(p)|, N_-(p) = #{A in L3(p): (A/p) = -1}; coin heuristic P(N_-=0 | |L3|).
Usage: uv run python scripts/dk_sign.py N
"""
import sys
from math import isqrt
from collections import Counter, defaultdict
def sgn8(t, u, v):
    n = t*u*v - u - v
    val = (n + 1 - (n*(t+u+v-9) + (t*u-1) + (t*v-1))) % 8
    return n, (1 if val == 2 else -1)  # valid for n odd (Cor 4.1)
# (i)
plus4 = set(); minus4 = set()
for t in range(8):
    for u in range(8):
        for v in range(8):
            n, s = sgn8(t, u, v)
            if n % 4 == 1:
                (plus4 if s == 1 else minus4).add((t % 4, u % 4, v % 4))
print("+1 cells mod 4 (t,u,v):", sorted(plus4)); print("mixed mod 4:", sorted(plus4 & minus4))
# (ii) rotation: word (v,t,u) for n has A=tu-1; rotated word (t,u,v) has numerator n'=K(t,u,v)=tuv-t-v, A'=uv-1
T = Counter()
for t in range(8):
    for u in range(8):
        for v in range(8):
            n, s = sgn8(t, u, v)
            if n % 4 != 1: continue
            n2, s2 = sgn8(u, v, t)  # word (t,u,v): middle u, first t, last v -> sgn8(middle, last, first)
            if n2 % 2 == 0: T[(s, 'n2 even')] += 1; continue
            T[(s, n2 % 4, s2)] += 1
print("rotation sign transitions (s, n' mod 4, s'):", dict(T))
# (iii)
N = int(sys.argv[1])
tot = [0]*(N+1); neg = [0]*(N+1)
t = 2
while 4*t - 4 <= N:
    u = 2
    while 2*(t*u-1) - u <= N:
        A = t*u - 1; v = 2
        while (n := v*A - u) <= N:
            if n % 8 == 1:
                tot[n] += 1
                if A % 4 == 0 or (t*v-1) % 4 == 0 or t % 4 == 0 or u % 4 == 0 or v % 4 == 0:
                    neg[n] += 1
            v += 1
        u += 1
    t += 1
sv = bytearray([1])*(N+1); sv[0]=sv[1]=0
for i in range(2, isqrt(N)+1):
    if sv[i]: sv[i*i::i] = bytearray(len(sv[i*i::i]))
ps = [p for p in range(17, N+1, 8) if sv[p]]
q = sum(neg[p] for p in ps) / sum(tot[p] for p in ps)
print(f"N={N}: primes p=1(8): {len(ps)}; global fraction of -1 on L3: {q:.4f}")
byk = defaultdict(lambda: [0, 0])
for p in ps:
    k = tot[p] // 2
    b = min(k // 4 * 4, 40)
    byk[b][0] += 1; byk[b][1] += (neg[p] == 0)
exp = defaultdict(float)
for p in ps: exp[min(tot[p]//2//4*4, 40)] += (1-q)**(tot[p]//2)
print("pairs k bucket: #primes, #(N_-=0), coin-expected #(N_-=0) with P=(1-q)^k")
for b in sorted(byk): print(b, byk[b][0], byk[b][1], round(exp[b], 2))
fr = [neg[p]/tot[p] for p in ps if tot[p] >= 40]
import statistics
print("N_-/|L3| for |L3|>=40: mean %.3f sd %.3f min %.3f" % (statistics.mean(fr), statistics.pstdev(fr), min(fr)))
sq = [m*m for m in range(3, isqrt(N)+1, 2) if m*m % 8 == 1]
print("squares: max N_- =", max(neg[s] for s in sq), " mean |L3| =", statistics.mean(tot[s] for s in sq))
