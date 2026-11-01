"""Exact CLASS_FORCING Prop 3.2 for N=4Cp+1 and K_T's congruence data."""
import json, math
from sympy import divisors,primerange,totient,factorint
Ms=[4,8,24,24,120,120,840,840,2520,2520,27720,27720]
primes=list(primerange(2,1000001));out=[]
for T,M in enumerate(Ms,1):
 ds={C:[int(d) for d in divisors(M) if d%(4*C)==4*C-1] for C in range(1,T+1)}
 classes=[r for r in range(M) if math.gcd(r,M)==1 and any((4*C*r+1)%d==0 for C in ds for d in ds[C])]
 good=set(classes);pp=[p for p in primes if math.gcd(p,M)==1];hard=[p for p in pp if p%4==1]
 # Independent actual-integer witness check, not just residue-table membership.
 for p in pp:
  witness=next(((C,d) for C in ds for d in ds[C] if (4*C*p+1)%d==0),None)
  assert (witness is not None)==(p%M in good)
  if witness:
   C,d=witness; dp=(4*C*p+1)//d
   assert (d+1)%(4*C)==0 and (dp+1)%(4*C)==0
   a,b=(d+1)//(4*C),(dp+1)//(4*C)
   x,y,z=a*b*C,a*C*p,b*C*p
   assert min(x,y,z)>0 and 4*x*y*z==p*(x*y+x*z+y*z)
 row=dict(T=T,M=M,degree=int(totient(M)),forcing_divisors=ds,classes=classes,density=f'{len(classes)}/{totient(M)}',hard_classes=sum(r%4==1 for r in classes),unramified_primes=len(pp),certified_primes=sum(p%M in good for p in pp),hard_primes=len(hard),hard_certified=sum(p%M in good for p in hard))
 out.append(row);print(T,M,len(classes),row['hard_classes'],row['certified_primes'],row['hard_certified'])
json.dump(out,open('data/z52b/pass2/ZF0/Z2860/classes.json','w'),indent=1)
# Z2708: exact cover using the common small-factor modulus 840, and one nonempty class per C.
rows=[];units=[r for r in range(840) if math.gcd(r,840)==1];union=set()
for C in range(1,21):
 m=4*C;ds=[int(d) for d in divisors(840) if d%m==m-1]
 rr=[r for r in units if any((m*r+1)%d==0 for d in ds)]
 union.update(rr)
 d=m-1; L=math.lcm(m,d)
 # p=-1 mod d because m=1 mod d; explicitly list unit classes mod m*d
 example=[r for r in range(L) if math.gcd(r,L)==1 and (m*r+1)%d==0]
 cyclic=[]
 for p,e in factorint(m).items():
  if p==2:
   if e==2:cyclic += [2]
   elif e>=3:cyclic += [2,2**(e-2)]
  else:cyclic += [int((p-1)*p**(e-1))]
 rows.append(dict(C=C,ray_modulus=m,cyclic_factors=cyclic,divisors_of_840=ds,classes_mod840=rr,example_modulus=L,example_classes=example))
squares={r*r%840 for r in units}
json.dump(dict(rows=rows,union_mod840=sorted(union),mordell_hard=sorted(squares),overlap_hard=sorted(union&squares),mordell_easy_not_covered=sorted(set(units)-squares-union)),open('data/z52b/pass2/ZF0/Z2708/classes.json','w'),indent=1)
