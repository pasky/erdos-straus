"""Exhaust all feasible positive first terms until a (+,−,−) witness is found."""
import json, time
from math import gcd
from pathlib import Path
from sympy import factorint, divisors
start=time.monotonic(); failures=[]; nearest_fail=[]; witnesses=[]; scanned=0; equal=0; max_back=(0,0)
for n in range(1,10001):
 top=(n-1)//4;found=None
 for x in range(top,0,-1):
  scanned+=1;a=n-4*x;b=n*x;g=gcd(a,b);a//=g;b//=g
  if 2*b%a==0:
   y=z=2*b//a
  else:
   y=z=None
   for d in divisors(b*b):
    if d>b:break
    if (d+b)%a==0:
     y=(d+b)//a;z=(b*b//d+b)//a;break
  if y is not None:
   assert n*y*z- n*x*z-n*x*y==4*x*y*z
   found=(x,y,z);equal+=y==z;max_back=max(max_back,(top-x,n));break
  if x==top:nearest_fail.append(n)
 if found is None:failures.append(n)
 else:witnesses.append([n,*found])
p=Path('data/z52b/pass2/ZF0/Z0307');p.mkdir(parents=True,exist_ok=True)
(p/'witnesses.json').write_text(json.dumps(witnesses))
r=dict(range=[1,10000],bound='1 <= x <= floor((n-1)/4)',failures=failures,nearest_failures=nearest_fail,nearest_failure_count=len(nearest_fail),equal_negative_witnesses=equal,first_terms_examined=scanned,max_backtrack=max_back,seconds=time.monotonic()-start)
(p/'results.json').write_text(json.dumps(r,indent=2));print(json.dumps(r,indent=2))
