"""Arithmetic profile of campaign hard primes: least QNR, h(-4p)/sqrt p and L(1,chi_p) quantiles vs neighbours."""
import cypari2, math, json
from sympy import legendre_symbol, nextprime, prevprime
pari=cypari2.Pari()
def lqnr(p):
    q=2
    while legendre_symbol(q,p)==1: q=int(nextprime(q))
    return q
def L1p(p):
    r=pari.quadclassunit(p); return float(r[0])*float(r[3])/math.sqrt(p)
def hn(p): return int(pari.qfbclassno(-4*p))/math.sqrt(p)
def neigh(p,k=300):
    out=[];q=p
    while len(out)<k:
        q=int(nextprime(q))
        if q%8==p%8: out.append(q)
    q=p
    while len(out)<2*k:
        q=int(prevprime(q))
        if q<10: break
        if q%8==p%8: out.append(q)
    return out
res={}
for lab,lst in [('R-zero',[409,577,5569,9601,23929,83449,102001,329617,712321,1134241,1724209,1726201,5212561,8813281]),('TypeA',[193,2521,66529]),('U-hard',[1201,3361,20521,21841,241,14401,4201,3169])]:
    for p in lst:
        nb=neigh(p,150)
        h=hn(p); hq=sum(hn(q)<h for q in nb)/len(nb)
        L=L1p(p); Lq=sum(L1p(q)<L for q in nb)/len(nb)
        res[p]=dict(kind=lab,p_mod_840=p%840,least_qnr=lqnr(p),h4p_over_sqrtp=round(h,3),h_quantile_vs_same_mod8=round(hq,3),L1chip=round(L,3),L_quantile=round(Lq,3),
                    chi_minus4p=[int(pari.kronecker(-4*p,q)) for q in (3,5,7,11,13,17,19,23)])
        print(p,res[p],flush=True)
json.dump(res,open('data/z52b/hard_profile.json','w'),indent=1)
