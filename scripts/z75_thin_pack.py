"""Pack discovered rules; the portable verifier does not import this or any other search code."""
from pathlib import Path
import json,math
from cypari2 import Pari
p=Pari();root=Path('data/z75/thin_cyclo')
def read(s):return json.loads((root/s).read_text())
def small(n):
    if not n%2:return [n//2,n,n]
    for f in range((-n)%4 or 4,20000,4):
        K=(n+f)//4;N=n*K
        for a in p.divisors(N*N):
            a=int(a);b=N*N//a
            if (a+N)%f==(b+N)%f==0:return [K,(N+a)//f,(N+b)//f]
    raise ValueError(n)
for k,H in [(33,720720),(273,55440),(297,5040)]:
    rows=[];L=set(range(H));qset={4**s+k for s in range(32)}
    def add(P,j,kind,args):
        if not any(x in L for x in range(j,H,P)):return
        rows.append([P,j,kind,args]);L.difference_update(range(j,H,P))
        if kind=='D':qset.add(args[0])
    for P,j,kind,args,match in read(f'{k}-5040.json')['rules']:add(P,j,kind,args+([match] if match else []))
    for h in [h for h in (5040,55440,720720) if H%h==0]:
        for j,kind,*args in read(f'{k}-{h}-smooth.json')['rules']:add(h,j,kind,args)
    if L:
        for j,f,a,b in read(f'{k}-{H}-ii.json')['rules']:add(H,j,'II',[f,a,b])
        for j,kind,i,A in read(f'{k}-{H}-final.json')['rules']:
            assert kind in ['T','U','UV']
            if kind=='UV':add(H,j,'UV',[i,A]);continue
            add(H,j,'A',[A,i if kind=='U' else (A+1)//i])
    assert not L,L
    data={'k':k,'H':H,'S':32,'rows':rows,'triples':{n:small(n) for n in sorted(qset)}}
    (root/f'cert_{k}.json').write_text(json.dumps(data,separators=(',',':'))+'\n')
