"""Shared exact ES interior-word conventions; runnable Borel/Weil-coefficient test."""
import json,math
from pathlib import Path
from sympy import primerange

def words(p):
 for t in range(2,(p+4)//4+1):
  for u in range(2,(p+2)//(2*t-1)+1):
   q,r=divmod(p+u,t*u-1)
   if not r and q>=2: yield t,u,q

def chi(a,p):
 x=pow(a%p,(p-1)//2,p)
 return -1 if x==p-1 else x

def save(mid,obj):
 path=Path('data/z52b/pass2/ZF0')/mid
 path.mkdir(parents=True,exist_ok=True)
 (path/'results.json').write_text(json.dumps(obj,indent=2)+'\n')

def mul(g,h,m):
 a,b,c,d=g;e,f,j,k=h
 return ((a*e+b*j)%m,(a*f+b*k)%m,(c*e+d*j)%m,(c*f+d*k)%m)

if __name__=='__main__':
 rows=[];maxerr=0
 # Gauss-sum ratio realizes the quadratic character exactly; floating sums
 # independently check the coefficient only for p<100, not a proof of identity.
 import cmath
 for p in primerange(5,500):
  if p%4!=1: continue
  ww=list(words(p));S={(t*u-1,p,t,t*v-1) for t,u,v in ww}
  S4={tuple(x%(4*p) for x in g) for g in S}
  Sp={tuple(x%p for x in g) for g in S}
  # Lower Borel B^-: projection lies in B^-, hence its B^- double-coset
  # saturation is exactly B^- (when nonempty), of size p(p-1).
  overlap=sum(mul(g,(1,0,1,1),4*p) in S4 for g in S4)
  signs=sum(chi(t*u-1,p) for t,u,v in ww)
  if p<100:
   G=[sum(cmath.exp(2j*math.pi*((a*x*x)%p)/p) for x in range(p)) for a in range(p)]
   maxerr=max(maxerr,max((abs(G[g[0]%p]/G[1]-chi(g[0],p)) for g in S),default=0))
  rows.append({'p':p,'words':len(ww),'distinct_mod4p':len(S4),'distinct_modp':len(Sp),'borel_size':p*(p-1),'right_L_overlap':overlap,'sign_sum':signs})
 out={'convention':'gamma=[[tu-1,p],[t,tv-1]], t,u,v>=2','prime_count':len(rows),'word_count':sum(r['words'] for r in rows),'nonempty_fibres':sum(r['words']>0 for r in rows),'right_L_overlap_total':sum(r['right_L_overlap'] for r in rows),'max_borel_density':max(r['distinct_modp']/r['borel_size'] for r in rows),'gauss_ratio_max_error_p_lt100':maxerr,'rows':rows}
 save('Z2806',out);print(json.dumps({k:v for k,v in out.items() if k!='rows'},indent=2))
