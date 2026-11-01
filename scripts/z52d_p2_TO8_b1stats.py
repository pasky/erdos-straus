# z52d P2 TO8: b=1 counts B1(p) (divisor form) vs p; low end; joint with (★) failures (Z3138, Z3142, Z2981)
import math
from collections import defaultdict
D = 'data/z52b/pass2/TO8/'
R = {int(l.split()[0]): int(l.split()[1]) for l in open(D + 'R_all_1e6.txt')}
B = {int(l.split()[0]): int(l.split()[1]) for l in open(D + 'b1_1e6.txt')}
ps = sorted(p for p in B if p > 50)
mb = [B[p] for p in ps]
print("primes≡1(4) 50<p≤1e6:", len(ps), " B1 quantiles:", [sorted(mb)[int(q * len(mb))] for q in (0.01, 0.05, 0.1, 0.5)])
low = sorted(ps, key=lambda p: B[p])[:12]
print("12 smallest B1(p):", [(p, B[p]) for p in low])
print("joint (★)&b1 failures:", [p for p in ps if R[p] == 0 and B[p] == 0], " b1-fails:", [p for p in ps if B[p] == 0], " (★)-fails with B1>0:", [(p, B[p]) for p in ps if R[p] == 0])
# rank of the 3 b1-fails among B1 values and the ratio to log^2 p
for p in [193, 2521, 66529]:
    print("b1-fail", p, "B1=0; quantile of log^2-normalised mean", round(B.get(p, -1) / math.log(p) ** 2, 3))
# Z2981: mean B1/log^2p by l(p)? (ℓ via Legendre, same as before, class p≡1 mod 24, p>1000)
def is_qr(a, p): return pow(a % p, (p - 1) // 2, p) == 1
def lnr(p):
    l = 2
    while True:
        if l % p and not is_qr(l, p): return l
        l += 1
bins = defaultdict(list)
for p in ps:
    if p > 1000 and p % 24 == 1: bins[lnr(p)].append(B[p] / math.log(p) ** 2)
print("Z2981: b1 mean B1/log^2 p by ℓ (p≡1 mod 24, p>1000):", [(l, len(v), round(sum(v) / len(v), 3)) for l, v in sorted(bins.items())[:8]])
