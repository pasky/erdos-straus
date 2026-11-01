# z52d pass2 SK3, item Z2317: empirical level-event probabilities E_C = {R_C(p)>0} for C<=CM, p=1 mod 4 <= 10^6,
# vs the independence model P(no level in S) = prod_{C in S} (1-P(E_C)).  Also pairwise phi-coefficients.
import math
import numpy as np
def primes1mod4(hi):
    s = bytearray([1])*(hi+1); s[0]=s[1]=0
    for i in range(2, int(hi**0.5)+1):
        if s[i]: s[i*i::i] = bytearray(len(s[i*i::i]))
    return [p for p in range(5, hi+1) if s[p] and p % 4 == 1]
def has_level(N, C):
    m = 4*C; d = m-1
    while d*d <= N:
        if N % d == 0: return True
        d += m
    return False
CM = 12
P = primes1mod4(10**6)
E = np.zeros((len(P), CM), dtype=np.int8)
for i, p in enumerate(P):
    for C in range(1, CM+1):
        E[i, C-1] = has_level(4*C*p+1, C)
pE = E.mean(axis=0)
print("n primes =", len(P))
print("P(E_C) C=1..%d:" % CM, np.round(pE, 4).tolist())
none_le = (E.sum(axis=1) == 0)
print("P(no level <= %d) empirical = %.5f" % (CM, none_le.mean()))
print("independence prediction    = %.5f" % np.prod(1-pE))
# phi-coefficients for C,C' <= 6
X = E[:, :6].astype(float); Cm = np.corrcoef(X.T)
print("correlation matrix C=1..6:"); print(np.round(Cm, 3))
# split by p mod 8 (level-1 event depends on p mod 8)
for r in (1, 5):
    sel = np.array([p % 8 == r for p in P])
    print(f"p=={r} mod 8: P(E_1)={E[sel,0].mean():.4f} P(E_2)={E[sel,1].mean():.4f} P(no level<=12)={(E[sel].sum(axis=1)==0).mean():.5f}")
