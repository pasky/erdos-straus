"""Stored controls, not a rerun of all z78 underlying centre enumerations."""
from pathlib import Path
from math import gcd
D=Path('data/z78/exact')
def cells(r,tag):return set(map(int,(D/f'r{r}_{tag}.txt').read_text().split()))
nonsq=set(range(1,13))-{i*i%13 for i in range(13)}
assert nonsq <= cells(13,'p1')|cells(13,'q1')
a,d,e=8,33,11999; m=4*a*d*e; n=(-4*a*a*d-e)%m
assert gcd(4*a*d,e)==1 and (m,n)==(12670944,12650497)
assert (n-2)%11==0 and (n-2)%169==0 and (n-1)%(m//(11*169))==0
for r in (17,19,23,29,31,37,41,43,47,53):
 a,b,c,w=[cells(r,t) for t in ('p1','p3','q3','p5')]; a|=cells(r,'q1'); sq={x*x%r for x in range(r)}
 alive=lambda x:x%r not in sq|a
 b={x for x in b if alive(x)};c={x for x in c if alive(x) and x%(r*r) not in b};w={x for x in w if alive(x) and x%(r*r) not in b}-c
 expected=[list(map(int,s.split())) for s in (D/'union.tsv').read_text().splitlines()[1:] if int(s.split()[0])==r][0]
 assert expected==[r,len(a-sq)*r*r,len(b)*r,len(c),len(w)]
tab=Path('data/z80/crush/ledger.txt').read_text().splitlines();passed={int(l.split()[0]) for l in tab if int(l.split()[-1])>0};old={int(l.split()[0]) for l in Path('data/z79/r2/ledger.txt').read_text().splitlines() if int(l.split()[8])>0};assert len(old)==28 and old<=passed and all(int(l.split()[0]) in passed for l in tab if int(l.split()[0])>=89)
print('13 covered; two-prime II3 control; z78 exact parent counts 17..53; all old passes and new terminal run retained')
