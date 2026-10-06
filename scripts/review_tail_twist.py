"""R76: from-scratch numeric sanity check of POINTWISE_TAIL Lemma 3.2's Euler-product claim:
Sum_{M<=T, M=3(4)} w(M) t^{omega_Y(M)}/M  /  Sum w(M)/M  stays O(1) (author: <= exp(2b(t-1)(loglogY+O(1))) ),
w(M)=tau(A^2) * b^{omega(M)} 2^{omega_Y(M)} * M/phi(M),  A=(M+1)/4,  t=1+1/loglogY, b=1+1/log log T.
Also reports the weighted mean of omega_Y and of log rad(M_Y) (the latter for suggestion S1)."""
import sys, math, numpy as np
T = int(float(sys.argv[1])); Ys = [int(y) for y in sys.argv[2:]] or [30, 300, 3000]
L = math.log(T); b = 1 + 1 / math.log(L)
lim = T + 2
spf = np.zeros(lim, dtype=np.int64)
for p in range(2, int(lim**0.5) + 1):
    if spf[p] == 0:
        blk = spf[p*p::p]; blk[blk == 0] = p; spf[p*p::p] = blk
idx = np.nonzero(spf == 0)[0]; spf[idx] = idx
def fac(n):
    f = {}
    while n > 1:
        p = int(spf[n]); f[p] = f.get(p, 0) + 1; n //= p
    return f
rows = []
for M in range(3, T + 1, 4):
    A = (M + 1) // 4
    tauA2 = 1
    for p, e in fac(A).items(): tauA2 *= 2 * e + 1
    fm = fac(M); rows.append((M, tauA2, list(fm)))
for Y in Ys:
    t = 1 + 1 / math.log(math.log(Y))
    S0 = S1 = Sw = Sr = 0.0
    for M, tauA2, ps in rows:
        wY = sum(1 for p in ps if p <= Y)
        w = tauA2 * b ** len(ps) * 2 ** wY * math.prod(p / (p - 1) for p in ps) / M
        S0 += w; S1 += w * t ** wY; Sw += w * wY; Sr += w * sum(math.log(p) for p in ps if p <= Y)
    print(f"T={T:.0e} Y={Y} t={t:.3f} ratio(t-twist)={S1/S0:.3f} bound e^(2b(t-1)loglogY)={math.exp(2*b*(t-1)*math.log(math.log(Y))):.3f}"
          f"  mean omega_Y={Sw/S0:.3f} (loglogY={math.log(math.log(Y)):.3f})  mean log rad M_Y={Sr/S0:.3f} (logY={math.log(Y):.2f})")
