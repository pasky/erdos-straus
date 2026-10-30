"""Correlate ES counts at primes with classical arithmetic functions (Spearman on residuals)."""
import numpy as np, json, math, sys
from sympy import isprime, divisor_count, primefactors, legendre_symbol, factorint
import cypari2
pari = cypari2.Pari(); pari.allocatemem(2*10**9)
R = 'data/z52b/raw/'
F = np.loadtxt(R+'f4_all_30000.txt', dtype=np.int64)
FP = np.vstack([F[[isprime(int(x)) for x in F[:,0]]], np.loadtxt(R+'pr_20001_200000.txt', dtype=np.int64)])
FP = FP[np.argsort(FP[:,0])]; FP = FP[np.concatenate([[True], np.diff(FP[:,0])>0])]
W = np.load(R+'words_3e6.npy')
FP = FP[(FP[:,0] % 4 == 1) & (FP[:,0] > 100)]
P = FP[:,0]
def cfper(n):
    a0 = math.isqrt(n); m, d, a, k = 0, 1, a0, 0
    while True:
        m = d*a - m; d = (n - m*m)//d; a = (a0 + m)//d; k += 1
        if a == 2*a0: return k
def lqnr(p):
    q = 2
    while legendre_symbol(q, p) == 1: q += 1
    return q
E11 = pari.ellinit([0,-1,1,-10,-20]); E37 = pari.ellinit([0,0,1,-1,0]); E32 = pari.ellinit([0,0,0,-1,0]); E27=pari.ellinit([0,0,1,0,-7])
feat = {}
def F_(name, f): feat[name] = np.array([f(int(p)) for p in P], dtype=float)
F_('tau(p-1)', lambda p: divisor_count(p-1))
F_('omega(p-1)', lambda p: len(primefactors(p-1)))
F_('v2(p-1)', lambda p: (p-1 & -(p-1)).bit_length()-1)
F_('v3(p-1)', lambda p: factorint(p-1).get(3,0))
F_('p≡1 mod 840', lambda p: p % 840 == 1)
F_('p≡1 mod 24', lambda p: p % 24 == 1)
F_('p mod 840 is a square', lambda p: (p % 840) in {1,121,169,289,361,529})
F_('tau(p+3)', lambda p: divisor_count(p+3))
F_('tau((p+3)/4)', lambda p: divisor_count((p+3)//4))
F_('tau(p+1)', lambda p: divisor_count(p+1))
F_('tau(p+4)', lambda p: divisor_count(p+4))
F_('tau(4p+1)', lambda p: divisor_count(4*p+1))
F_('tau(p+12)', lambda p: divisor_count(p+12))
F_('sum_{d<=8} tau(p+4d)', lambda p: sum(divisor_count(p+4*d) for d in range(1,9)))
F_('h(-4p)', lambda p: int(pari.qfbclassno(-4*p)))
F_('h(-p) [disc -p, only p≡3(4) fund] → h(-3p)', lambda p: int(pari.qfbclassno(-3*p)) if (-3*p) % 4 in (0,1) else 0)
def qcu(p):
    r = pari.quadclassunit(p); return float(r[0]), float(r[3])
hr = [qcu(int(p)) for p in P]
feat['h(p) real'] = np.array([a for a,b in hr]); feat['regulator log eps_p'] = np.array([b for a,b in hr])
feat['regulator/sqrt p'] = feat['regulator log eps_p']/np.sqrt(P)
F_('CF period of sqrt p', cfper)
F_('least QNR', lqnr)
F_('#QNR among primes <=29', lambda p: sum(legendre_symbol(q,p)==-1 for q in [2,3,5,7,11,13,17,19,23,29]))
F_('(2/p)', lambda p: legendre_symbol(2,p)); F_('(3/p)', lambda p: legendre_symbol(3,p)); F_('(5/p)', lambda p: legendre_symbol(5,p)); F_('(7/p)', lambda p: legendre_symbol(7,p))
F_('ord_p(2)/(p-1)', lambda p: int(pari.znorder(pari.Mod(2,p)))/(p-1))
F_('least primitive root', lambda p: int(pari.znprimroot(p).lift()))
F_('a_p(11a1)/2sqrt p', lambda p: int(pari.ellap(E11,p))/(2*math.sqrt(p)))
F_('a_p(37a1)/2sqrt p', lambda p: int(pari.ellap(E37,p))/(2*math.sqrt(p)))
F_('|a_p(32a: y^2=x^3-x)|/2sqrt p', lambda p: abs(int(pari.ellap(E32,p)))/(2*math.sqrt(p)))
F_('a_p(32a) mod 8', lambda p: int(pari.ellap(E32,p)) % 8)
F_('ramanujan tau(p)/p^5.5', lambda p: int(pari.ramanujantau(p))/p**5.5)
F_('p=a^2+b^2: min(a,b)/sqrt p', lambda p: min(abs(int(x)) for x in pari.qfbsolve(pari.Qfb(1,0,1),p))/math.sqrt(p))
F_('p mod 5', lambda p: p % 5); F_('p mod 7', lambda p: p % 7); F_('p mod 3', lambda p: p % 3)
F_('spf(p+4)', lambda p: min(primefactors(p+4)))
F_('P+(p-1)/p (smoothness)', lambda p: math.log(max(primefactors(p-1)))/math.log(p))
F_('R(p) (★ count)', lambda p: int(W[p-1,3])); F_('Uv(p)', lambda p: int(W[p-1,4])); F_('I3(p)', lambda p: int(W[p-1,2])); F_('W(p)', lambda p: int(W[p-1,1]))
F_('sigma(p-1)/(p-1)', lambda p: float(pari.sigma(p-1))/(p-1))
F_('phi(p-1)/(p-1)', lambda p: float(pari.eulerphi(p-1))/(p-1))
F_('h(-8p)', lambda p: int(pari.qfbclassno(-8*p)))
F_('h(-4p)/sqrt p', lambda p: int(pari.qfbclassno(-4*p))/math.sqrt(p))
F_('L(1,chi_-4p) ~ pi h/(2 sqrt p)', lambda p: math.pi*int(pari.qfbclassno(-4*p))/(2*math.sqrt(p)))
F_('L(1,chi_p)·sqrt p ~ h R', lambda p: 0)
feat['L(1,chi_p) ~ hR/sqrt p'] = feat['h(p) real']*feat['regulator log eps_p']/np.sqrt(P); del feat['L(1,chi_p)·sqrt p ~ h R']
from scipy.stats import spearmanr
lp = np.log(P.astype(float))
targets = {'U(p)': FP[:,1], 'minz(p)/p': FP[:,4]/P, 'maxx(p)-p/4': FP[:,7]-P/4, 'k1(p)': FP[:,10], 'k2(p)': FP[:,11], 'nx(p)': FP[:,9], 'minlcm(p)/p': FP[:,13]/P}
res = {}
for tn, t in targets.items():
    t = t.astype(float)
    # residual after regressing log(t+1) on log p, log log p
    y = np.log(t + 1); X = np.vstack([np.ones_like(lp), lp, np.log(lp)]).T
    beta = np.linalg.lstsq(X, y, rcond=None)[0]; r = y - X @ beta
    for fn, f in feat.items():
        if np.std(f) == 0: continue
        rho, pv = spearmanr(r, f)
        res[f'{tn} ~ {fn}'] = (round(float(rho),4), float(pv))
json.dump(res, open('data/z52b/classical_corr.json','w'), indent=1)
np.save(R+'classical_feat.npy', np.vstack([P]+[feat[k] for k in feat])); json.dump(list(feat), open(R+'classical_feat_names.json','w'))
for k, v in sorted(res.items(), key=lambda kv: -abs(kv[1][0])):
    print(f'{v[0]:+.4f}  p={v[1]:.1e}  {k}')
