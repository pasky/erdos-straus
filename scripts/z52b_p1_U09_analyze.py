# z52b pass1 U09: analysis of the (★) family R(p) = #{(u,B,C): 4uBC-u-B=p} (C-enumeration from z52b_p1_U09_core.c)
# Usage: python3 scripts/z52b_p1_U09_analyze.py data/z52b/pass1/U09/R_primes1mod4_le2e5.txt
import sys, math, collections
import numpy as np
from scipy.stats import spearmanr
fn = sys.argv[1]
rows = np.array([list(map(int, l.split())) for l in open(fn)], dtype=object)
P = np.array([int(r[0]) for r in rows]); R = np.array([int(r[1]) for r in rows])
minC = np.array([int(r[2]) for r in rows]); minMax = np.array([int(r[3]) for r in rows]); mask = np.array([int(r[4]) for r in rows], dtype=object)
print("primes", len(P), "max p", P.max())
# ---- Z1442: C=1 criterion vs 'prime factor 3 mod 4 of 4p+1'
def has3mod4_factor(n):
    m = n; f = 2
    while f*f <= m:
        while m % f == 0:
            if f % 4 == 3: return True
            m //= f
        f += 1
    return m > 1 and m % 4 == 3
bit0 = np.array([int(m) & 1 for m in mask])
hit = np.array([has3mod4_factor(4*int(p)+1) for p in P])
print("Z1442: C=1 bit == (4p+1 has prime factor 3 mod 4) on all primes:", bool(np.all((bit0 == 1) == hit)), " mismatches:", int(np.sum((bit0==1)!=hit)))
print("Z1442: fraction of p with C=1 failing:", round(float(np.mean(bit0==0)),4), " count:", int(np.sum(bit0==0)))
for X in [10**4, 10**5, 2*10**5]:
    s = P<=X
    print(f"   p<= {X}: C=1 fails for {int(np.sum((bit0==0)&s))} of {int(s.sum())}")
# ---- Z1406 / Z1398: witness index and max-coordinate scale
ok = minC>0
lp = np.log(P[ok].astype(float))
print("Z1406: minC quantiles 50/90/99/max:", np.percentile(minC[ok],[50,90,99]).round(1), minC[ok].max())
for X in [10**3, 10**4, 10**5, 2*10**5]:
    s = (P<=X)&ok
    print(f"   p<={X}: median minC {np.median(minC[s])}, frac minC>log^2 p: {np.mean(minC[s] > np.log(P[s].astype(float))**2):.3f}, frac minC>sqrt p: {np.mean(minC[s] > np.sqrt(P[s].astype(float))):.3f}")
s2 = ok & (minMax>0)
slope = np.polyfit(np.log(P[s2].astype(float)), np.log(minMax[s2].astype(float)), 1)
print("Z1398 (★)-family only: fit log minMax ~ a log p + b: a=%.4f b=%.3f" % (slope[0], slope[1]))
print("   median log(minMax)/log p:", np.median(np.log(minMax[s2].astype(float))/np.log(P[s2].astype(float))).round(4), " max:", (np.log(minMax[s2].astype(float))/np.log(P[s2].astype(float))).max().round(3))
# ---- Z1496: isolated primes (R=0) as function of X
zeros = P[R==0]
print("Z1496: R=0 primes (isolated in (★) graph):", zeros.tolist())
for X in [10**3, 10**4, 10**5, 2*10**5]:
    print(f"   #R=0 primes <= {X}: {int(np.sum(zeros<=X))}")
# ---- Z1457: rate of good(C) by C and by C mod q (C<=64)
Cs = np.arange(1,65)
good = np.array([[(int(m) >> (int(c)-1)) & 1 for c in Cs] for m in mask])  # primes x 64
rate = good.mean(axis=0)
print("Z1457: good(C) rate C=1..12:", rate[:12].round(3).tolist())
for q in [3,4,5,8]:
    rr = [round(float(good[:, (Cs % q)==r].mean()),4) for r in range(q)]
    print(f"   by C mod {q}:", rr)
# ---- Z1609 / Z1980: class means of R(p)/log^2 p modulo 840 (p ≡ 1 mod 4, coprime to 840)
L = np.log(P.astype(float))**2
cls = P % 840
cm = collections.defaultdict(list)
for c, v in zip(cls, R / L):
    cm[int(c)].append(float(v))
means = {c: np.mean(v) for c, v in cm.items() if len(v) >= 20}
allm = np.array(list(means.values()))
print("Z1980: classes mod 840 with n>=20:", len(means), " mean R/log^2 p spread (min,max,sd):", allm.min().round(3), allm.max().round(3), allm.std().round(3))
ses = {c: np.std(cm[c])/math.sqrt(len(cm[c])) for c in means}
z = np.array([(means[c]-np.mean(R/L))/ses[c] for c in means])
print("   max |z| over classes:", np.abs(z).max().round(2), " #classes |z|>3:", int(np.sum(np.abs(z)>3)), "of", len(z))
# ---- Hardy–Littlewood singular series (Z1534 / Z1460): N_q(p) = #{(u,B,C) mod q : 4uBC-u-B ≡ p}/q^2 over odd primes q<=Q
def primes_upto(n):
    s = [True]*(n+1); s[0]=s[1]=False
    for i in range(2,int(n**0.5)+1):
        if s[i]:
            for j in range(i*i,n+1,i): s[j]=False
    return [i for i,v in enumerate(s) if v]
Q = 60
logS = np.zeros(len(P))
for q in primes_upto(Q):
    if q == 2: continue
    r = np.arange(q)
    u, B, C = np.meshgrid(r, r, r, indexing='ij')
    val = (4*u*B*C - u - B) % q
    cnt = np.bincount(val.ravel(), minlength=q) / q**2
    logS += np.log(cnt[P % q])
S = np.exp(logS)
rho = spearmanr(S, R).correlation
print("Z1534/Z1460: Spearman corr(S(p), R(p)) over p<=2e5 (q odd <=60):", round(float(rho),4))
print("   corr(log S, R/log^2 p):", round(float(np.corrcoef(logS, R/L)[0,1]),4))
