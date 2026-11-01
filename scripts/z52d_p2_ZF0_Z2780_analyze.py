"""Aggregate shared exhaustive prime census and independently check small cases.
Also finish Z0873 and compare Z2875 coefficient and denominator enumerations.
"""
import csv,json,sys
from pathlib import Path
from fractions import Fraction
from itertools import permutations
from math import gcd,isqrt
from sympy import Poly,Symbol
sys.path.insert(0,str(Path(__file__).resolve().parent))
from pointwise_size_ct_check import solutions,brute
base=Path('data/z52b/pass2/ZF0')
def save(mid,obj):
 (base/mid/'results.json').write_text(json.dumps(obj,indent=2));print(mid,json.dumps(obj)[:6000])
rows=[{k:int(v) for k,v in r.items()} for r in csv.DictReader(open(base/'Z1901/primes.csv'))]
assert len(rows)==9592 and rows[-1]['p']==99991
for r in rows:
 p=r['p']
 if p>200:break
 ss=solutions(p);assert len(ss)==r['triples'];assert set(ss)==brute(p)
 assert sum(any(a*b%(a+b)==0 for a,b in [(x,y),(x,z),(y,z)]) for x,y,z in ss)==r['unit_binary']
 paths=[0]*4;certs=[0]*4
 for s in ss:
  seen=set()
  for u,v,w in set(permutations(s)):
   a=Fraction(1,u);b=a+Fraction(1,v);c=Fraction(4,p)
   middle=abs(a.numerator*b.denominator-b.numerator*a.denominator)==1
   final=abs(b.numerator*c.denominator-c.numerator*b.denominator)==1
   mask=2*middle+final;paths[mask]+=1;seen.add(mask)
  for m in seen:certs[m]+=1
 assert paths==[r['path'+m] for m in ['00','01','10','11']]
 assert certs==[r['cert'+m] for m in ['00','01','10','11']]

def totals(rs):return {k:sum(r[k] for r in rs) for k in rows[0] if k!='p'}
save('Z1901',dict(prime_max=100000,primes=len(rows),totals=totals(rows),by_mod4={str(m):dict(primes=len(rr:=[r for r in rows if r['p']%4==m]),totals=totals(rr)) for m in [1,2,3]},independent_check='all primes <=200: existing brute and divisor enumerators; unit refinements and Farey determinants recomputed with Fraction',max_triples=max(rows,key=lambda r:r['triples']),no_unit_binary_primes=sum(r['unit_binary']==0 for r in rows)))
f=[r for r in rows if r['p']%4==1]
save('Z2780',dict(prime_max=100000,prime_residue='1 mod4',primes=len(f),totals=totals(f),zero_overlap=sum(r['distinct_anchors']==0 for r in f),primes_with_middle_Farey=sum(r['cert10']+r['cert11']>0 for r in f),primes_with_all_Farey=sum(r['cert11']>0 for r in f),primes_with_final_Farey=sum(r['cert01']+r['cert11']>0 for r in f),by_mod24={str(m):dict(primes=len(rr:=[r for r in f if r['p']%24==m]),totals=totals(rr)) for m in [1,5,13,17]},max_overlap=max(f,key=lambda r:r['distinct_anchors'])))
assert all(r['only_z']>0 for r in rows if r['p']>2)
spf=list(range(100001))
for i in range(2,317):
 if spf[i]==i:
  for j in range(i*i,100001,i):
   if spf[j]==j:spf[j]=i
fails=[];lifted=0
for n in range(2,100001):
 m=n
 while m%2==0:m//=2
 if m==1:fails.append(n)
 else:
  p=spf[m];assert p>2 and n%p==0;lifted+=1
save('Z0873',dict(range=[2,100000],failures=fails,successes_by_odd_prime_scaling=lifted,odd_prime_witness_censuses=len(rows)-1,powers_covered_by_proof=[2**k for k in range(1,41)],power_check_method='exact valuation obstruction: v2(4/n),v2(1/x),v2(1/y) >= 1-k but v2(1/z)<=-k; algebraic certificate, not huge denominator enumeration',source_quote='"only z div by n": { "n_fail_primes": 1, "last_fail_prime": 2, ... "n_fail_all3000": 11, "fail_all_head": [2,4,8,16,32,64,128,256,512,1024,2048] }'))
# Cubic grid is an independent enumeration of coefficients, not merely repackaged triples.
grid=[{k:int(v) for k,v in r.items()} for r in csv.DictReader(open(base/'Z2875/grid.csv'))]
allpairs=[];repeated=0;per_n=[]
for n in range(1,101):
 ss=solutions(n);per_n.append(dict(n=n,triples=len(ss)))
 for x,y,z in ss:
  e1=x+y+z;e2=x*y+x*z+y*z;e3=x*y*z;D=((x-y)*(x-z)*(y-z))**2
  assert 4*e3==n*e2
  assert D==e1*e1*e2*e2-4*e2**3-4*e1**3*e3-27*e3*e3+18*e1*e2*e3
  repeated+=D==0;allpairs.append([n,e1,e2,e3,D,x,y,z])
expected={tuple(r[:4]) for r in allpairs if r[1]<=200 and r[2]<=10000}
observed={(r['n'],r['e1'],r['e2'],r['e3']) for r in grid if r['x']}
assert expected==observed
(base/'Z2875/all_split_n100.json').write_text(json.dumps(allpairs))
bad=[r for r in grid if not r['x']]
T=Symbol('T')
for r in grid:
 poly=Poly(T**3-r['e1']*T**2+r['e2']*T-r['e3'],T)
 assert int(poly.discriminant())==r['discriminant']
 assert isqrt(r['discriminant'])**2==r['discriminant']
 if not r['x']:assert poly.is_irreducible
save('Z2875',dict(full_n_range=[1,100],all_split_cubics=len(allpairs),repeated_root_cubics=repeated,distinct_root_cubics=len(allpairs)-repeated,coefficient_grid=dict(n=[1,100],e1=[1,200],e2=[1,10000],integer_e3=True),nonnegative_square_discriminant=len(grid),totally_split_in_grid=len(observed),square_but_irreducible=len(bad),irreducible_examples=bad[:10],per_n=per_n,independent_grid_equals_filtered_denominator_enumeration=True))
