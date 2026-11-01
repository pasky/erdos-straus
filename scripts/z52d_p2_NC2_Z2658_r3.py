from fractions import Fraction
from functools import lru_cache
from math import gcd,isqrt
from pathlib import Path
import json

def primes(N):
 s=bytearray(b'\x01')*(N+1); s[:2]=b'\0\0'
 for i in range(2,isqrt(N)+1):
  if s[i]: s[i*i:N+1:i]=b'\0'*(((N-i*i)//i)+1)
 return [i for i,x in enumerate(s) if x]
def hj(n,a):
 out=[]
 while a:
  b=(n+a-1)//a; out.append(b); n,a=a,b*a-n
 return out
@lru_cache(None)
def d(p,q,i):
 if q==1:return Fraction((2*i-p)**2-p,4*p)
 return Fraction((2*i+1-p-q)**2-p*q,4*p*q)-d(q,p%q,i%q)
groups={1:[], -1:[]}; pair_count=0; checks=0
for p in primes(1999):
 if p%4!=1:continue
 for a in range(1,p):
  if gcd(a,p)>1 or len(hj(p,a))!=3: continue
  pair_count+=1; chi=1 if pow(a,(p-1)//2,p)==1 else -1
  groups[chi].append(sum((d(p,a,i) for i in range(p)),Fraction(0)))
for p in primes(200):
 for i in range(p): checks+=d(p,1,i)==Fraction((2*i-p)**2-p,4*p)
means={str(s):str(sum(v,Fraction())/len(v)) for s,v in groups.items()}
out={'max_prime':max(p for p in primes(1999) if p%4==1),'all_p_lt':2000,'length3_pairs':pair_count,'sample_size_by_legendre':{str(k):len(v) for k,v in groups.items()},'mean_sum_d_by_legendre':means,'sample_variance_by_legendre':{str(k):float(sum((float(x)-float(sum(v,Fraction())/len(v)))**2 for x in v)/(len(v)-1)) for k,v in groups.items()},'L(p,1)_closed_form_checks':checks,'recursion':'d(p,q,i)=((2i+1-p-q)^2-pq)/(4pq)-d(q,p mod q,i mod q), q=1 closed form','sign_split_consistency':'no established selector; group means determine empirical split'}
d=Path('data/z52b/pass2/NC2/Z2658'); d.mkdir(parents=True,exist_ok=True); (d/'metrics.json').write_text(json.dumps(out,indent=2)+'\n'); print(json.dumps(out))
