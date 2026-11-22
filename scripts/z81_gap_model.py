"""Composite-only block surrogate: see data/z81/gap/design.md. Root cwd.
Run with precompiled data/z81/gap/controls.bin. Counts through 1e6 not forecast:
too few controls per fibre. Quadrature for prime intensity (logarithmic integral).
"""
from math import log
from pathlib import Path
from random import Random
from subprocess import check_output
from itertools import accumulate
from collections import defaultdict
P=Path('data/z81/gap'); RS=(1,121,169,289,361,529);rng=Random(81081)
def load(a,b,B):
    s=check_output([str(P/'controls.bin'),str(a),str(b),str(B)],text=True)
    return [list(map(int,r.split())) for r in s.splitlines()]
def rates(rows):
    out=defaultdict(float);marg=defaultdict(float)
    for r in RS:
        prod=1
        for rr,k,N,f,B,s in rows:
            if rr!=r:continue
            assert N
            out[k+4]+=prod*f/N/6;marg[k]+=f/N/6
            if k+4<=123:
                prod*=B/N;out[k+8]+=prod/6;marg[k+4]+=s/N/6
    return out,marg
def experiment(a,b):
    B=int(log(b));w=min(1<<20,(b-a)//4);stats=None
    # Stratified compact windows across the bin, exhaustive below ~4M total width
    for j in range(4):
        l=a+(b-a)*j//4;h=a+(b-a)*(j+1)//4
        L=rng.randint(l,h-w); rows=load(L,L+w,B)
        if stats is None:stats=rows
        else:
            for u,v in zip(stats,rows):
                assert u[:2]==v[:2];u[2:]=[x+y for x,y in zip(u[2:],v[2:])]
    return rates(stats)[0],min(u[2] for u in stats)
if __name__=='__main__':
    raw=[list(map(int,s.split())) for s in (P/'bulk_pairs.txt').read_text().splitlines()];out,marg=rates(raw)
    print('bulk, k, modeled misses, model >=k+4 (18878 actual centres, normalization only)')
    for k in range(3,124,4): print(k,round(marg[k]*18878,2),round(out[k+4]*18878,4))
    counts=defaultdict(float);start=10**6;rec=(8803369,119945383009,1889389369729,3153419441929,5000000000000)
    knots=sorted(set(rec)|{start*2**h for h in range(23) if start*2**h<rec[-1]})
    print('bin_hi, min_controls, expected cumulative since 1e6 at >=59,107,111,119,127, mean-one threshold (capped at 127)')
    for a,b in zip(knots,knots[1:]):
        out,n=experiment(a+1,b+1)
        width=(b-a)/128; mass=sum(width/(32*log(a+width*(j+0.5))) for j in range(128))
        for k,r in out.items():counts[k]+=mass*r
        last=max([3]+[k for k,c in counts.items() if c>=1])
        print(b,n,*(f'{counts[k]:.5g}' for k in (59,107,111,119,127)),last,flush=True)
