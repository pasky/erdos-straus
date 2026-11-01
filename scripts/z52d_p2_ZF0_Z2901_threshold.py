"""Explicit conservative BM lower bound; no sieve or large arrays."""
import json, math
A=4/math.pi**2; B=6/math.pi**2; target=3/(32*math.pi**2)
r=10;c=1.5216
const=1+r+r*math.log(c*(1+1/r))
def bound(L):
    g=(r+1)/(4*r)*L+0.5*math.log(L)+const
    ell=L-math.log(8)
    return (3*A/8*ell**2-3*ell-(g+1)*(B/2*ell+3))/4
lo,hi=math.log(1e20),10000.
for _ in range(100):
    mid=(lo+hi)/2
    if bound(mid)>=target*mid**2:hi=mid
    else:lo=mid
out={'r':r,'c2':c,'g_additive_constant':const,'target':target,'numerical_crossing_logp':hi,'numerical_crossing_log10p':hi/math.log(10),'safe_p1':'10^1000','safe_logp':1000*math.log(10),'safe_lower_coefficient':bound(1000*math.log(10))/(1000*math.log(10))**2,'samples':[{'logp':L,'lower_over_logp2':bound(L)/L**2} for L in [500,1000,2000,1000*math.log(10),10000]]}
print(json.dumps(out,indent=2))
