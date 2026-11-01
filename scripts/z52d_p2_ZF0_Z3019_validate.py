"""Independent exact checks of new tables, using SymPy factors/divisors.
No array products: at most one integer's divisors / one 1024-vertex graph."""
import csv,gzip,json,math
from pathlib import Path
import sympy as s
D=Path('data/z52b/pass2/ZF0');out={}
# Uniform-index sample plus minimal-u record and all zero cases.
with gzip.open(D/'Z1721/minu.csv.gz','rt') as f:rows=list(csv.DictReader(f))
chosen=[r for i,r in enumerate(rows) if i%3321==0 or int(r['u'])==410 or int(r['u'])==0]
for r in chosen:
 p=int(r['p']);got=None
 for u in range(1,math.isqrt(p)//2+2):
  if 4*u*u-2*u>p:break
  sols=[((p+u)//d,(d+1)//(4*u)) for d in s.divisors(p+u) if (d+1)%(4*u)==0 and (p+u)//d>=u]
  if sols:
   k,c=min(sols);got=(u,k,c,len(sols));break
 assert got==(tuple(int(r[x]) for x in ['u','k','C','kchoices']) if int(r['u']) else None),(p,got,r)
out['minu_checks']=len(chosen)
# Enumerate divisor pairs directly (no exponent-ratio search used in C).
slicechecks=0
with gzip.open(D/'Z3019/slices.csv.gz','rt') as f:
 for i,r in enumerate(csv.DictReader(f)):
  if i%6643 and int(r['p']) not in [5,13,17,409,577,8803369]:continue
  p=int(r['p']);mask=int(r['hitmask'],16);actual=0
  for e in range(3,min(256,3*p),4):
   if e%p==0:continue
   n=(p+e)//4;ds=s.divisors(n)
   h=any((a+b)%e==0 for a in ds for b in s.divisors(n//a))
   if h:actual|=1<<((e-3)//4)
   slicechecks+=1
  assert mask==actual,(p,mask,actual)
out['slice_checks']=slicechecks
# Rich failure examples and some full level factorisations.
richchecks=[]
for r in csv.DictReader(open(D/'Z1597/perprime.csv')):
 p=int(r['p']);c=int(r['rich_fail_example_C'])
 if not c or 8*c-3>p:continue
 if len(richchecks)>=30:break
 n=4*c*p+1;fac=s.factorint(n);assert len(fac)>=6
 assert not any(d%(4*c)==4*c-1 for d in s.divisors(n))
 richchecks.append({'p':p,'C':c,'factorization':{str(k):int(v) for k,v in fac.items()}})
out['rich_failure_checks']=richchecks
# Rebuild named graphs directly from gcd; check saved hyperedges and summary.
G={int(r['p']):r for r in csv.DictReader(open(D/'Z2819/graphs.csv'))};H=json.load(open(D/'Z2819/hyperedges.json'));gchecks=[]
for p in [409,577,1249,7297]:
 edges=set()
 for q,vs in H[str(p)].items():
  for v in vs:assert (4*v*p+1)%int(q)==0
  for i,c in enumerate(vs):
   for d in vs[i+1:]:edges.add((c,d))
 direct={(c,d) for c in range(1,1025) for d in range(c+1,1025) if math.gcd(4*c*p+1,4*d*p+1)>1}
 assert direct==edges and len(edges)==int(G[p]['edges'])
 gchecks.append(p)
out['graph_checks']=gchecks
(D/'Z3019/validation.json').write_text(json.dumps(out,indent=2)+'\n')
print(json.dumps({k:len(v) if isinstance(v,list) else v for k,v in out.items()},indent=2))
