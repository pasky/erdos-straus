"""Exact seven ET-period first hits, using 192 previously certified primes.
Primary scanner splits m, checks p at the reconstructed omitted coordinates;
reference scanner uses (residue,period) atoms and exact divisor/root equations.
"""
from functools import lru_cache
from math import gcd,isqrt
from pathlib import Path
from statistics import median
import csv,sys
@lru_cache(None)
def div(n):
    return sorted({j for i in range(1,isqrt(n)+1) if n%i==0 for j in (i,n//i)})

def hit(p,m):
    # test by reconstruction + identities, not lists of f/E polynomial roots
    if m%4==3:
        h=(m+1)//4
        for a in div(h):
            for c in div(h//a):
                d=h//(a*c); q,r=divmod(p+4*a*a*d,m)
                if r==0: return 'II2',a,c*q-a,c,d,q
    if m%4: return None
    h=m//4
    for a in div(h):
        d=h//a; r=(-p)%m
        # f need not be <m
        for f in range(r,4*a*h+2,m):
            if f and (4*a*h+1)%f==0:
                c=(p+f)//m;e=(4*a*h+1)//f
                return 'I1',a,c*e-a,c,d,e
        b=d
        for tag,e in (('I4',(-pow(p,-1,m))%m),('II1',r)):
            if e and (a+b)%e==0:
                d=((p*e+1) if tag=='I4' else p+e)//m
                return tag,a,b,(a+b)//e,d,e
        for j in div(h//a):
            k=h//(a*j)
            if (p+k)%(4*a*j)==0:
                big=(p+k)//(4*a*j)
                for tag,A,C,D in (('I2',a,j,big),('I3',big,a,j)):
                    e,rem=divmod(4*A*A*D+1,k)
                    if not rem: return tag,A,C*e-A,C,D,e
            e=k;d=j;c,rem=divmod(p+4*a*a*d+e,m)
            if not rem:return 'II3',a,c*e-a,c,d,e
    return None

def ref_atoms(m):
    # all viable residues at m, independent implementation (CRT-free tests).
    if m%4==3:
        h=(m+1)//4
        return {(-4*a*a*d)%m for a in div(h) for d in div(h//a)}
    if m%4:return set()
    h=m//4;s=set()
    for a in div(h):
        j=h//a
        s.update((-f)%m for f in div(4*a*h+1))
        for e in div(a+j):
            if gcd(e,m)==1:s.update(((-e)%m,(-pow(e,-1,m))%m))
        for f in div(j):
            b=j//f;u=4*a*b;r=(-f)%u
            if gcd(u,f)>1:continue
            s.add((-4*a*a*b-f)%m)
            for v in range(r,m,u):
                if (a*v+b)%f==0 or (v*v+4*a*a*b)%f==0:s.add(v)
    return {v for v in s if gcd(v,m)==1}

def verify(p,m,row):
    tag,a,b,c,d,e=row
    assert min(a,b,c,d,e)>0 and c*e==a+b
    if tag.startswith('II'):
        assert 4*a*b*d==p+e
        x,y,z=a*b*d,p*a*c*d,p*b*c*d
        h={'II1':4*a*b,'II2':4*a*c*d-1,'II3':4*a*d*e}[tag]
    else:
        assert 4*a*b*d==p*e+1
        x,y,z=a*c*d,b*c*d,p*a*b*d;f=4*a*c*d-p
        h={'I1':4*a*d,'I2':4*a*c*f,'I3':4*c*d*f,'I4':4*a*b}[tag]
    assert m==h and 4*x*y*z==p*(x*y+x*z+y*z)

if __name__=='__main__':
    prev=list(csv.DictReader(Path('data/z78/wild_depth.csv').open()));rows=[]
    # group by shared B: all m with only small prime factors are dead.
    for B in sorted({int(v['B']) for v in prev}):
        pp=[v for v in prev if int(v['B'])==B];block=[]
        for v in pp:
            p=int(v['p']); top=int(v['f']);small={q for q in range(2,B+1) if len(div(q))==2}
            for m in range(B+1,top+1):
                if m%4 not in (0,3):continue
                if all(q in small for q in div(m) if q>1 and len(div(q))==2):continue
                row=hit(p,m)
                if row:break
            else: raise ValueError('missing round-1 (star) hit')
            verify(p,m,row);block.append((B,int(v['t']),p,m,*row));rows.extend([block[-1]])
        print(B, min(v[3] for v in block),median(v[3] for v in block),max(v[3] for v in block),flush=True)
    # Every period, including square-safe smooth ones (no smoothness shortcut).
    # Evaluate the residue set once for the active primes, discard as soon as tested.
    for m in range(3,max(v[3] for v in rows)+1):
        if m%4 not in (0,3):continue
        A=ref_atoms(m)
        for _,_,p,h,*_ in rows:
            if m<=h:assert (p%m in A)==(m==h),(p,m,h)
    pth=Path('data/z78/wild_full.csv');txt='B,t,p,m,row,a,b,c,d,e\n'+''.join(','.join(map(str,v))+'\n' for v in rows)
    if '--write' in sys.argv:pth.write_text(txt)
    else:assert pth.read_text()==txt
