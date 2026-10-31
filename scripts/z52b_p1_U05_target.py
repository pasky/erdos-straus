"""z52b pass1 U05 Z0884: targeted search. Model (fit on primes ≡1(4), 5<p≤1e5, U from U_primes_1e5.txt):
log(U/log²p) ~ 1 + sum_{q≤100} (q/p). Apply to all primes p≡1 (mod 840) in (1e5, 1e6]; compute exact U (ucount) for
all of them; compare U/log²p of the model's top-10 predicted-hardest vs bottom-10 (predicted-easiest)."""
import math, subprocess, numpy as np
from collections import Counter
D = "data/z52b/pass1/U05/2nd/"
UP = {}
for l in open(D+"U_primes_1e5.txt"):
    p, u, nx = map(int, l.split()); UP[p] = u
N = 1000000
s = bytearray([1])*(N+1); s[0] = s[1] = 0
for i in range(2, int(N**.5)+1):
    if s[i]: s[i*i::i] = bytearray(len(s[i*i::i]))
isp = lambda n: s[n] == 1
def leg(a, p):
    a %= p; return 1 if pow(a, (p-1)//2, p) == 1 else -1
Q = [q for q in range(3, 101) if isp(q)]
P1 = [p for p in UP if p % 4 == 1 and p > 4]
X = np.array([[1.0] + [leg(q, p) for q in Q] for p in P1], float)
y = np.array([math.log(UP[p]/math.log(p)**2) for p in P1])
beta = np.linalg.lstsq(X, y, rcond=None)[0]
cand = [p for p in range(840*120+1, 1000001, 840) if isp(p)]
cand = [p for p in cand if p % 840 == 1]
Xc = np.array([[1.0] + [leg(q, p) for q in Q] for p in cand], float)
pred = Xc @ beta
out = subprocess.run(["/tmp/ucount"], input="\n".join(map(str, cand)), capture_output=True, text=True).stdout.split("\n")
U = {int(l.split()[0]): int(l.split()[1]) for l in out if l}
act = np.array([math.log(U[p]/math.log(p)**2) for p in cand])
order = np.argsort(pred)
top = order[-10:]; bot = order[:10]
print(f"candidates p≡1 (840), 1e5<p≤1e6: {len(cand)}; model R2 on training primes: {1-((y-X@beta)**2).sum()/((y-y.mean())**2).sum():.3f}")
print("correlation(model prediction, actual log(U/log²p)) over candidates: %.3f" % np.corrcoef(pred, act)[0, 1])
print("mean actual log(U/log²p): model top-10 (predicted most solutions) = %.3f ; bottom-10 (predicted fewest) = %.3f" % (act[top].mean(), act[bot].mean()))
print("min U over candidates:", min(U.values()), "at", min(U, key=U.get), "; predicted fewest-solutions:", [cand[i] for i in bot[:5]])
