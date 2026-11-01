import json, random
from pathlib import Path
from sympy import isprime, primerange, factorint
N=10000
def R(p):
 n=4*p+1; f=factorint(n); div=[1]
 for q,e in f.items(): div=[x*q**j for x in div for j in range(e+1)]
 return sum((1 if x*x==n else 2) for x in div if x*x<=n and x%4==3 and n//x%4==3)
eul=sorted({n*n+n+41 for n in range(N) if (n*n+n+41)%4==1 and isprime(n*n+n+41)})
maxp=max(eul); allp=[p for p in primerange(5,maxp+1) if p%4==1 and p not in set(eul)]
random.seed(1999); ec={}; cc={}
for p in eul: ec.setdefault(p%840,[]).append(p)
controls=[]
for c,arr in ec.items():
 pool=[p for p in allp if p%840==c]; controls += random.sample(pool,min(len(pool),len(arr)))
ra=[R(p) for p in eul]; rb=[R(p) for p in controls]
from scipy.stats import mannwhitneyu
out={'N':N,'family_n':len(eul),'range_max':maxp,'controls':len(controls),'definition':'exact ordered-pair R from divisors of 4p+1; non-family primes p=1 mod4 stratified to same p mod840 counts','family_mean':sum(ra)/len(ra),'family_median':sorted(ra)[len(ra)//2],'family_min_fraction':sum(x==min(ra+rb) for x in ra)/len(ra),'control_mean':sum(rb)/len(rb),'control_median':sorted(rb)[len(rb)//2],'control_min_fraction':sum(x==min(ra+rb) for x in rb)/len(rb),'mann_whitney_u_p':float(mannwhitneyu(ra,rb,alternative='two-sided').pvalue),'family_min_R_in_combined':'see family_min_fraction'}
d=Path('data/z52b/pass2/NC2/Z1999'); d.mkdir(parents=True,exist_ok=True); (d/'metrics.json').write_text(json.dumps(out,indent=2)+'\n'); print(json.dumps(out))
