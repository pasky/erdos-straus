from math import gcd
from sympy import primerange, factorint
import importlib.util,sys
sys.argv=['x','5']
spec=importlib.util.spec_from_file_location('m','scripts/z52d_avenue_Q00_coprime_pair.py'); 
src=open('scripts/z52d_avenue_Q00_coprime_pair.py').read().split('fails=[]')[0]; exec(src)
N=6000
pf=[]
for p in primerange(5,N):
    if p%4!=1: continue
    S=sols(p)
    if not any(gcd(gcd(x,y),z)==1 for x,y,z in S): pf.append(p)
print(len(pf),pf)
for p in pf: print(p,p%24,p%840,factorint(p+4),factorint(p+1))
