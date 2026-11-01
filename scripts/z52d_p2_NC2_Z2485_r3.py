import json, math
from pathlib import Path
from sympy import primerange, isprime
from scipy.stats import chi2_contingency

def classno(D):
 # Proper primitive positive binary quadratic forms of negative order discriminant D.
 total=0; m=-D
 for a in range(1,math.isqrt(m//3)+2):
  for b in range(-a,a+1):
   if (b*b-D)%(4*a): continue
   c=(b*b-D)//(4*a)
   if a>c or math.gcd(math.gcd(a,abs(b)),c)!=1: continue
   if (abs(b)==a or a==c) and b<0: continue
   total+=1
 return total
C=range(1,21); ds={}; yes_odd=yes_even=no_odd=no_even=0; witnesses=0; total=0
for c in C:
 for d in C:
  D=-16*c*c*d; ds[c,d]=classno(D)
for p in primerange(5,10001):
 if p%4!=1: continue
 for c in C:
  for d in C:
   # Operational divisor-type witness: the Type-I form has a proper nontrivial divisor.
   # The item does not specify a residue constraint; do not import one from a different certificate family.
   val=p*p+4*c*c*d
   witness=not isprime(val)
   parity=ds[c,d]%2; total+=1
   if witness:
    witnesses+=1
    if parity:yes_odd+=1
    else:yes_even+=1
   elif parity:no_odd+=1
   else:no_even+=1
table=[[yes_odd,yes_even],[no_odd,no_even]]
try:
 chi,pval,_,_=chi2_contingency(table,correction=False)
 chi,pval=float(chi),float(pval)
except ValueError:
 chi,pval=None,None
out={'prime_limit':10000,'primes_1mod4':sum(1 for p in primerange(5,10001) if p%4==1),'cd_pairs':400,'observations':total,'witness_definition':'exists proper nontrivial divisor 1<f≤sqrt(p²+4c²d); operational refinement because the item does not specify a residue condition','discriminant':'order discriminant D=−16c²d, primitive positive reduced binary quadratic forms; not fundamental discriminant','class_number_range':[min(ds.values()),max(ds.values())],'witness_observations':witnesses,'witness_h_parity_counts':{'odd':yes_odd,'even':yes_even},'no_witness_h_parity_counts':{'odd':no_odd,'even':no_even},'fraction_odd_witness':yes_odd/witnesses if witnesses else None,'fraction_odd_no_witness':no_odd/(total-witnesses),'chi_square':chi,'chi_square_p':pval}
outdir=Path('data/z52b/pass2/NC2/Z2485'); outdir.mkdir(parents=True,exist_ok=True); (outdir/'metrics.json').write_text(json.dumps(out,indent=2)+'\n'); print(json.dumps(out))
