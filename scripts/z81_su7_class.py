"""Class-group and witness diagnostics. Requires cypari2 (e.g. 2.2.4)."""
from cypari2 import Pari
from z80_square_span import primes_to,jac
from pathlib import Path
from collections import Counter,defaultdict
from math import prod
import sys, csv, subprocess
CHECK='data/z81/s_u7/classcheck'
pari=Pari()
DABS=[4,8,20]

def chi(form,l):
    a,b,c=map(int,form)
    return next(jac(n,l) for n in [a,c,a+b+c] if n%l)

def internal(p,l,d,primes):
    # For these odd p, -d*p and -d*l*p have the same parity of fundamental discriminant.
    c=1 if -d*p%4==1 else 4
    for D in [-c*d*l*p,-c*d*p*l**2]:
        cy=pari.quadclassunit(D); orders=list(map(int,cy[1]));gens=list(cy[2]); sgn=[chi(g,l) for g in gens]
        print('D',D,'invariants',orders,'gens',gens,'chi',l,sgn)
        assert all(o%4==0 for o,s in zip(orders,sgn) if s<0)
        h_exact=int(subprocess.check_output([CHECK,str(-D)],text=True).split()[1]);assert h_exact==int(cy[0])
        one=pari.qfbpow(gens[0],0);assert all(pari.qfbpow(g,o)==one for g,o in zip(gens,orders))
        A={tuple(map(int,one)):0}
        for o,g,s in zip(orders,gens,sgn):
            old=A;A={}
            for k in range(o):
                h=pari.qfbpow(g,k)
                for f,z in old.items():
                    val=tuple(map(int,pari.qfbcomp(pari.Qfb(*f),h)))
                    assert val not in A;A[val]=(z+k*(s<0))%4
        assert len(A)==int(cy[0]);
        for q in primes:
            f=pari.qfbred(pari.qfbprimeform(D,q));print('prime',q,'form',f,'quartic_log',A[tuple(map(int,f))]);


def groups():
    zeros={int(x) for x in Path('data/z58/screens/star_prime_zeros.txt').read_text().splitlines() if x and x[0].isdigit()}
    main={p for p in primes_to(10**7) if p%840==1}
    inputs=main|zeros|{2521,3361,21841,76441}
    W={}
    for row in csv.reader(open('data/z80/jugular/r2/words.csv')):
        p=int(row[0]); W[p]=tuple(int(row[i]) for i in [7,43,67]) # R,U7,HJ3good up to reversal
    exact={row[0]:row[1:] for line in subprocess.check_output([CHECK],input=''.join(f'{p}\n' for p in sorted(inputs)),text=True).splitlines() if (row:=list(map(int,line.split())))}
    bins=defaultdict(list)
    for p in sorted(inputs):
        ranks=[]
        for d in DABS:
            cyc=list(map(int,pari.quadclassunit(-d*p)[1]));assert prod(cyc)==exact[p][len(ranks)]
            ranks.append(tuple(sum(o%(2**k)==0 for o in cyc) for k in [1,2,3]))
        key=tuple(r[2] for r in ranks);R,U,S=W[p]
        if p in main:
            assert tuple(r[:2] for r in ranks)==((1,1),(1,1),(2,1)); bins[key].append((p,R,U,S))
        if p in zeros or p in [2521,3361,21841,76441]:print('control',p,ranks,'counts',R,U,S)
    print('rank8 triple, p count, R zeros, means of R U7 HJ3good (unordered; descriptive only), min R U7 S')
    for key,rows in sorted(bins.items()):
        vals=list(zip(*rows))[1:];print(key,len(rows),sum(x==0 for x in vals[0]),tuple(round(sum(x)/len(x),2) for x in vals),tuple(min(x) for x in vals))
    print('main',len(main))
if __name__=='__main__':
    internal(26881,17,1,[83,2447]);internal(341041,5,11,[151,239]);groups()
