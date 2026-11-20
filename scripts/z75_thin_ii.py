"""Fixed Type II divisor A=f: n≡-a/b mod f, 4ab|f+1. Complete the certificate if possible."""
from z75_conjs_period_helper import order
from cypari2 import Pari
from pathlib import Path
import json,sys
k,H,B=map(int,sys.argv[1:4]);p=Pari();dir=Path('data/z75/thin_cyclo');base=json.loads((dir/f'{k}-{H}-smooth.json').read_text());left=set(base['left']);rules=[]
ps=sorted(int(q) for q in p.primes([3,B]) if pow(4,H,int(q))==1);mods=[1]
for q in ps:
  z=q;ext=[]
  while z<=B and pow(4,H,z)==1:
    ext.extend(v*z for v in mods if v*z<=B);z*=q
  mods.extend(ext)
for f in sorted(v for v in mods if v%4==3):
  if not left:break
  m=(f+1)//4
  for b in map(int,p.divisors(m)):
    for j in tuple(left):
      a=-(pow(4,j,f)+k)*b%f
      if a and m%(a*b)==0:rules.append([j,f,a,b]);left.remove(j)
(dir/f'{k}-{H}-ii.json').write_text(json.dumps({'rules':rules,'left':sorted(left)})+'\n');print(H,len(base['left']),sorted(left))
