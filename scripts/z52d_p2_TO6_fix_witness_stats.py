"""z52d pass2 TO6 fix: statistics from the witness bitmask (primes p≡1 mod 4 ≤ 2e5; line t=3+4j, j<64).
Items: Z2021 (independence/Poisson model of witness absence), Z2357 (union-of-lines failure phase),
Z2374 (small prime q | tp+1 with q ≡ -1 mod t), Z2376/Z2377 (at-least-m events over lines), Z2409 (pretentious
correlation of witness indicators with real characters), Z2276 (equidistribution mod squarefree moduli)."""
import json, math
import numpy as np
from sympy import legendre_symbol, factorint, primerange
D='data/z52b/pass2/TO6/'
rows=[l.split() for l in open(D+'witmask_p1mod4_2e5.txt')]
P=np.array([int(a) for a,b in rows]); M=[int(b,16) for a,b in rows]
W=np.array([[ (m>>j)&1 for j in range(64)] for m in M],dtype=np.int8)   # W[p,j]
T=np.array([3+4*j for j in range(64)])
n=len(P); out={}
# ---- Z2021: independence model of absence. pi_j = empirical density of line j; predicted P(no witness in lines J)=prod(1-pi_j)
pi=W.mean(0)
def absent(J): return (W[:,J].sum(1)==0).mean()
res=[]
for K in [1,2,4,8,16,32,64]:
    J=list(range(K))
    emp=absent(J); pred=float(np.prod(1-pi[J]))
    res.append(dict(K=K, t_max=int(T[K-1]), emp=emp, indep_pred=round(pred,6), ratio=round(emp/pred,3) if pred>0 else None))
out['Z2021_independence_absence']=res
# Poisson lower tail for R(p) is in analysis; here: witness counts vs binomial with pi_j
cnt=W.sum(1); mu=pi.sum()
# Poisson-binomial prediction of P(count=0 among 64 lines) vs empirical
out['Z2021_count_stats']=dict(mean_count_emp=round(float(cnt.mean()),3), mean_count_pred=round(float(mu),3),
    var_emp=round(float(cnt.var()),3), var_indep_pred=round(float((pi*(1-pi)).sum()),3), P0_emp=float((cnt==0).mean()))
# ---- Z2357: union of first k lines: failures F_k and fit log F_k ~ -c k
F=[]
for k in range(1,65):
    F.append(int((W[:,:k].sum(1)==0).sum()))
out['Z2357_phase']=dict(F_k_first_k_lines=F, primes=n)
ks=np.arange(1,65); mask=np.array(F)>=20
slope=np.polyfit(ks[mask], np.log(np.array(F)[mask]),1)[0]
out['Z2357_phase']['fit_logF_slope_per_line']=round(float(slope),4)
out['Z2357_phase']['line_density_pi_first8']=[round(float(x),3) for x in pi[:8]]
# ---- Z2376/Z2377: at-least-m witnessed lines among first K lines (k=16,32)
for K in [16,32]:
    c=W[:,:K].sum(1)
    out[f'Z2376_atleast_K{K}']={m: round(float((c>=m).mean()),4) for m in [1,2,3,5,8]}
    out[f'Z2376_indep_K{K}_binomial_model']={m: round(float(sum(math.comb(K,i)*(0.5)**0 for i in [])),4) for m in []}
# independence prediction for at-least-m with pi_j (Poisson-binomial via DP)
def pb_tail(ps):
    dist=np.zeros(len(ps)+1); dist[0]=1
    for p_ in ps:
        dist[1:]=dist[1:]*(1-p_)+dist[:-1]*p_; dist[0]*= (1-p_)
    return dist
for K in [16,32]:
    d=pb_tail(pi[:K]); out[f'Z2376_indep_K{K}']={m: round(float(d[m:].sum()),4) for m in [1,2,3,5,8]}
# ---- Z2374: small prime q ≤ (log p)^2 with q | tp+1 and q ≡ -1 (mod t), over all witnessed-line t ≤ 255
Pl=[int(x) for x in P[:2000]]  # sample for speed
hit=0; tot=0; ex=[]
for p in Pl:
    y=(math.log(p))**2
    found=False
    for t in T[:16]:
        N=int(t)*p+1
        for q in factorint(N):
            if q<=y and q%int(t)==int(t)-1: found=True; break
        if found: break
    hit+=found; tot+=1
out['Z2374_small_prime_q']=dict(sample=tot, frac_with_small_q_in_class_t_le_63=round(hit/tot,4))
# ---- Z2409: pretentious test: correlation of witness indicator I_j with real characters (d/p)
def kron(d,p):
    return legendre_symbol(d%p,p) if p>2 else 0
ds=[-3,2,-7,5,3,-11,7,-15,-19,11,13,-23]
pr=[int(x) for x in P[:3000]]
corr_rows=[]
for j in [0,1,2,3,4,5,6,7]:
    best=(0,None)
    for d in ds:
        vals=np.array([legendre_symbol(d%p,p) if d%p else 0 for p in pr],dtype=float)
        I=W[:3000,j].astype(float)
        c=np.corrcoef(I,vals)[0,1] if vals.std()>0 else 0
        if abs(c)>abs(best[0]): best=(round(float(c),4),d)
    corr_rows.append(dict(t=int(T[j]),max_abs_corr=best[0],char_d=best[1]))
out['Z2409_pretentious_max_corr']=corr_rows
# ---- Z2276: equidistribution of line-density across residue classes mod squarefree moduli (105 = 3*5*7, 1155=3*5*7*11)
def class_chi(mod, j):
    cls=P%mod
    tab={}
    for c in np.unique(cls):
        sel=cls==c; tab[int(c)]=(int(sel.sum()), float(W[sel,j].mean()))
    overall=W[:,j].mean()
    chi=sum(((W[cls==c,j].sum()-overall*(cls==c).sum())**2)/(overall*(1-overall)*(cls==c).sum()) for c in np.unique(cls) if (cls==c).sum()>0)
    rng=[v[1] for v in tab.values() if v[0]>=3] or [float("nan")]
    return dict(mod=mod,t=int(T[j]),classes=len(tab),chi2=round(float(chi),1),dof=len(tab)-1,min_density=round(min(rng),3),max_density=round(max(rng),3))
out['Z2276_equidistribution']=[class_chi(m,j) for m in [105,1155] for j in [0,1,2]]
json.dump(out, open(D+'witness_stats_TO6.json','w'), indent=1, default=float)
print(json.dumps(out, default=float)[:6000])
