import csv,json
from pathlib import Path
import numpy as np
import sympy as s
D=Path('data/z52b/pass2/ZF0/Z2819');rows=list(csv.DictReader(open(D/'graphs.csv')))
R={int(r['p']):{k:float(v) for k,v in r.items() if k!='p'} for r in rows};zeros=[409,577,5569,9601,23929,83449]
metrics=['edges','components','giant','isolates'];matched=[]
for p in zeros:
 controls=sorted([q for q in R if q%840==p%840 and q not in zeros],key=lambda q:abs(q-p))[:10]
 matched.append({'p':p,'hard':R[p],'controls':controls,'control_mean':{m:float(np.mean([R[q][m] for q in controls])) for m in metrics},'control_range':{m:[min(R[q][m] for q in controls),max(R[q][m] for q in controls)] for m in metrics}})
obs=sum(r['HH'] for r in R.values());exp=sum(r['expected_HH'] for r in R.values())
out={'n':len(R),'Cmax':1024,'shared_HH':obs,'within_p_16level_bin_permutation_expected_HH':exp,'ratio':obs/exp,'matched':matched,'ranges':{m:[min(r[m] for r in R.values()),max(r[m] for r in R.values())] for m in metrics}}
mr=list(csv.DictReader(open(D/'matched.csv')))
out['fixed_level_matched']={'n':len(mr),'HH':sum(int(r['observed_HH']) for r in mr),'expected':sum(float(r['level_matched_expected_HH']) for r in mr),'stratum_size_range':[min(int(r['stratum_n']) for r in mr),max(int(r['stratum_n']) for r in mr)]}
out['fixed_level_matched']['ratio']=out['fixed_level_matched']['HH']/out['fixed_level_matched']['expected']
# Save actual hyperedges, not only graph summaries, for hard/control fixtures.
fixtures={}
for p in zeros+[x['controls'][0] for x in matched]:
 edges={}
 for q in s.primerange(3,1025):
  if p==q:continue
  r=(-pow(4*p,-1,q))%q;vertices=list(range(r,1025,q))
  if len(vertices)>1:edges[str(q)]=vertices
 fixtures[str(p)]=edges
(D/'hyperedges.json').write_text(json.dumps(fixtures,separators=(',',':'))+'\n')
(D/'analysis.json').write_text(json.dumps(out,indent=2)+'\n');print(json.dumps(out,indent=2))
