"""O186 §5: exact-T1 test for the V_phi unit-orbit mechanism (T1_TEMPLATE Thm 1.3) over ALL odd n.
Shot k succeeds iff N_k = n^2 + 4n L_{2k+1} - 16 = N(n + 4 phi^{2k+1}) has a prime factor l = +-1 (mod 5) with (n/l) = -1,
or l = 5 with (n/5) = -1. Reports odd n < NMAX with no successful k, |k| <= K, and compares with {m^2, 5m^2}.
usage: uo_phi_all.py NMAX K"""
import sys, numpy as np
from math import isqrt
NMAX, K = int(sys.argv[1]), int(sys.argv[2])
L = {}; a, b = 2, 1  # Lucas L_0, L_1
Ls = [2, 1]
for i in range(2, 2*K + 3): Ls.append(Ls[-1] + Ls[-2])
def Lodd(m):  # m odd, possibly negative
    return Ls[m] if m >= 0 else -Ls[-m]
LIM = NMAX*NMAX + 4*NMAX*Ls[2*K+1] + 1
spf = np.zeros(LIM, dtype=np.int32)
for i in range(2, isqrt(LIM) + 1):
    if spf[i] == 0:
        blk = spf[i*i::i]; blk[blk == 0] = i
def jac(a, n):  # Legendre (a/l) for prime l = n
    a %= n
    return 0 if a == 0 else (1 if pow(a, (n-1)//2, n) == 1 else -1)
fails = []
for n in range(3, NMAX, 2):
    ok = False
    for k in range(-K, K + 1):
        N = abs(n*n + 4*n*Lodd(2*k + 1) - 16)
        while N > 1 and not ok:
            l = N if spf[N] == 0 else int(spf[N])
            while N % l == 0: N //= l
            if l in (2,): continue
            if (l % 5 in (1, 4) or l == 5) and jac(n, l) == -1: ok = True
        if ok: break
    if not ok: fails.append(n)
t1 = {n for n in range(3, NMAX, 2) if isqrt(n)**2 == n or (n % 5 == 0 and isqrt(n//5)**2 == n//5)}
print(f"odd n < {NMAX}, |k| <= {K}: {len(fails)} failures; T1 set size {len(t1)}; failures outside T1: {sorted(set(fails) - t1)[:30]}; T1 members with a hit: {sorted(t1 - set(fails))[:10]}")
