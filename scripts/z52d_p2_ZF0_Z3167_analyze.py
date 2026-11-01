"""Census analysis plus independent divisor checks; run via uv with numpy,sympy."""
import csv,json,math
from pathlib import Path
import numpy as np
import sympy as s
D=Path('data/z52b/pass2/ZF0/Z3167')
rows=list(csv.DictReader(open(D/'decades.csv')))
fits={}
for low in [100,1000,10000]:
 r=[x for x in rows if int(x['bound'])>=low]
 x=np.log(np.log([int(z['bound']) for z in r]));y=np.log([int(z['maxC']) for z in r])
 a,b=np.polyfit(x,y,1);fits[str(low)]={'points':len(r),'A':float(a),'intercept':float(b),'R2':float(1-np.sum((y-a*x-b)**2)/np.sum((y-y.mean())**2))}
def full(p):
 best=None;witness=None
 for a in range(1,(1+math.isqrt(1+4*p))//4+2):
  if 4*a*a-2*a>p:break
  for d in s.divisors(p+a):
   if (d+1)%(4*a)==0 and (p+a)//d>=a:
    c=(d+1)//(4*a)
    if best is None or c<best:best=c;witness=[a,(p+a)//d,c]
 return best,witness
hard=sorted(set(map(int,open('data/lsa/hard.txt'))))
expected={int(r['p']):int(r['minC']) or None for r in csv.DictReader(open(D/'tail.csv'))}
expected.update({int(r['p']):int(r['minC']) for r in csv.DictReader(open(D/'records.csv'))})
checks={}
for p in sorted(set(expected)|set(hard)):
 k,w=full(p)
 if p in expected:assert k==expected[p],(p,k,expected[p])
 checks[str(p)]={'minC':k,'witness':w,'hard_list':p in hard}
# Small direct level tests independently verify the AP sieve's first-decade maxima.
small=[]
for p in s.primerange(5,10001):
 if p%4!=1:continue
 k,w=full(p);small.append((p,k))
for r in rows:
 B=int(r['bound'])
 if B>10000:continue
 z=[k for p,k in small if p<=B]
 assert sum(k is None for k in z)==int(r['zeros'])
 assert max(k for k in z if k is not None)==int(r['maxC'])
out={'fits':fits,'independent_checks':checks,'small_full_prime_checks':len(small),'note':'Zeros mean K=infinity, not missing/censored data. Fits exclude all infinity values.'}
(D/'analysis.json').write_text(json.dumps(out,indent=2)+'\n')
print(json.dumps({'fits':fits,'checked':len(checks),'small':len(small)},indent=2))
