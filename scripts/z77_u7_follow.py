"""Seek positive certificates at the six large f-truncation survivors. No nonexistence inference."""
from z77_u7_panel import root,prime
from cypari2 import Pari
pa=Pari()
for line in (root/'u7-panel.txt').read_text().splitlines():
    n,f=map(int,line.split());
    if f or n<10**9:continue
    for x in range(1,3001):
        fs=set()
        for d0 in pa.divisors(n+x):
            d=int(d0);fs.add(d);fs.add((n+x)//d*((d+1)//x)-1) if (d+1)%x==0 else None
        fs.update(map(int,pa.divisors(x*n+1)))
        hits=[(f,c) for f in fs if f>1 and f%8==7 and (r:=-n%f) and (f+1)%r==0 for c in (1,3,5) if f%c==0 and prime(f//c)]
        if hits:
            print(n,x,*min(hits));break
    else:print(n,'unresolved')
