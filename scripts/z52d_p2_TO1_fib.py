# z52d pass2 TO1 (Z0366): p + F_k representations of odd n <= L, all Fibonacci values F_k >= 1 (F_1 = F_2 = 1 included once).
import numpy as np, sys
L = int(sys.argv[1]) if len(sys.argv) > 1 else 100000
s = np.ones(L+1, bool); s[:2] = False
for i in range(2, int(L**0.5)+1):
    if s[i]: s[i*i::i] = False
F = [1, 2]
while F[-1] < L: F.append(F[-1]+F[-2])
F = sorted(set(f for f in F if f < L))
ns = np.arange(3, L+1, 2)
c = np.zeros(len(ns), np.int64)
for f in F:
    q = ns - f; ok = q >= 2
    c[ok] += s[q[ok]]
print(f"odd n in [3,{L}]: {len(ns)}; Fibonacci values used: {F}")
print(f"zero representations: {int((c==0).sum())} ({(c==0).mean():.4f}); min count {int(c.min())}; mean {c.mean():.3f}")
print("zero-representation n (first 15):", ns[c==0][:15].tolist())
print("zero-representation fraction by decade:", [round(float((c[(ns>=lo)&(ns<hi)]==0).mean()),4) for lo,hi in [(3,1000),(1000,10000),(10000,100001)]])
