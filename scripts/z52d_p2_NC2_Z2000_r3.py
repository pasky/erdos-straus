import json, math, random
from pathlib import Path
from sympy import primerange, factorint
from scipy.stats import ttest_ind
LIMIT=10_000_000
pr=[p for p in primerange(5,LIMIT+1) if p%4==1]
def R(p):
 n=4*p+1; f=factorint(n); ds=[1]
 for q,e in f.items(): ds=[x*q**j for x in ds for j in range(e+1)]
 return sum((1 if x*x==n else 2) for x in ds if x*x<=n and x%4==3 and (n//x)%4==3)
random.seed(2000); allvals={p:R(p)/(math.log(p)**2) for p in pr}
out={'limit':LIMIT,'statistic':'R(p)/(log p)^2','R_definition':'ordered divisor pairs x,y=3 mod4, xy=4p+1','classes':{}}
for mod in [840,9240,120120]:
 target=[p for p in pr if p%mod==1]; ctlpool=[p for p in pr if p%840==1 and p%mod!=1] if mod!=840 else [p for p in pr if p%840!=1]
 ctl=random.sample(ctlpool,min(len(target),len(ctlpool)))
 a=[allvals[p] for p in target]; b=[allvals[p] for p in ctl]
 se=math.sqrt((sum((x-sum(a)/len(a))**2 for x in a)/(len(a)-1))/len(a)+(sum((x-sum(b)/len(b))**2 for x in b)/(len(b)-1))/len(b)) if len(a)>1 and len(b)>1 else float('nan')
 out['classes'][str(mod)]={'count':len(target),'mean':sum(a)/len(a),'control_count':len(ctl),'control_mean':sum(b)/len(b),'difference':sum(a)/len(a)-sum(b)/len(b),'welch_se':se,'standard_errors':(sum(a)/len(a)-sum(b)/len(b))/se if se else None,'welch_p':float(ttest_ind(a,b,equal_var=False).pvalue) if len(a)>1 and len(b)>1 else None,'control_definition':'for 840: p mod840 !=1 (no same-class control possible); deeper: complementary to target inside p=1 mod840'}
d=Path('data/z52b/pass2/NC2/Z2000'); d.mkdir(parents=True,exist_ok=True); (d/'metrics.json').write_text(json.dumps(out,indent=2)+'\n'); print(json.dumps(out))
