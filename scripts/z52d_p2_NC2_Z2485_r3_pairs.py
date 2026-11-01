# Per-(c,d) analysis for Z2485: class-number parity is a function of D=-16c^2d only,
# so the witness test must be done at the level of (c,d) pairs, not per prime observation.
import json, math
from pathlib import Path
from sympy import primerange, divisors
from scipy.stats import fisher_exact
def classno(D):
 total=0; m=-D
 for a in range(1,math.isqrt(m//3)+2):
  for b in range(-a,a+1):
   if (b*b-D)%(4*a): continue
   c=(b*b-D)//(4*a)
   if a>c or math.gcd(math.gcd(a,abs(b)),c)!=1: continue
   if (abs(b)==a or a==c) and b<0: continue
   total+=1
 return total
P=[p for p in primerange(5,10001) if p%4==1]
C=range(1,21); rows=[]
for c in C:
 for d in C:
  h=classno(-16*c*c*d); w=0
  for p in P:
   N=p*p+4*c*c*d; m=4*c*d
   if any(1<f<N and (f+p)%m==0 for f in divisors(N)): w+=1
  rows.append({'c':c,'d':d,'h':h,'odd':h%2,'witness_rate':w/len(P)})
odd=[r for r in rows if r['odd']]; even=[r for r in rows if not r['odd']]
# 2x2 on pairs: pairs with h odd vs even, split by witness rate >= 0.5
hi_odd=sum(1 for r in odd if r['witness_rate']>=0.5); lo_odd=len(odd)-hi_odd
hi_even=sum(1 for r in even if r['witness_rate']>=0.5); lo_even=len(even)-hi_even
out={'primes':len(P),'pairs':len(rows),'odd_h_pairs':len(odd),'odd_h_pairs_detail':[(r['c'],r['d'],r['h'],round(r['witness_rate'],4)) for r in odd],
 'mean_witness_rate_odd_h':sum(r['witness_rate'] for r in odd)/max(1,len(odd)),
 'mean_witness_rate_even_h':sum(r['witness_rate'] for r in even)/len(even),
 'table_witness_ge_half':[[hi_odd,lo_odd],[hi_even,lo_even]],'fisher_p':float(fisher_exact([[hi_odd,lo_odd],[hi_even,lo_even]])[1])}
d=Path('data/z52b/pass2/NC2/Z2485'); d.mkdir(parents=True,exist_ok=True)
(d/'pairs.json').write_text(json.dumps(out,indent=1,ensure_ascii=False)+'\n'); print(json.dumps({k:v for k,v in out.items() if k!='odd_h_pairs_detail'}))
print('odd-h pairs:', out['odd_h_pairs_detail'][:20])
