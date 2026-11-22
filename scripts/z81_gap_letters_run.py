"""Reproducible finite-size integration of the separate analytic letter model.
Numbers are simulation, not certified frequencies. Errors = sample SE across
independent replicate integrals; not discretization error or model error.
"""
from pathlib import Path
from math import log,sqrt
from statistics import mean,stdev
from subprocess import check_output
P=Path('data/z81/gap'); B=str(P/'letters.bin'); reps=12

def sample(H,seed):
    s=check_output([B,str(H),'8192',str(reps),str(seed)],text=True)
    return [list(map(float,L.split())) for L in s.splitlines()]
def pr(v):return f'{mean(v):.4g}({stdev(v)/sqrt(len(v)):.2g})'
if __name__=='__main__':
    bulk=sample(15*10**6,81001)
    print('bulk mid-point g>=, model count conditional on 18878 inputs, replicate s.e.')
    for j in range(15):print(7+4*j,pr([18878*r[j] for r in bulk]))
    # Include early intervals; coarse prime intensity unreliable at tiny bins with one input.
    rec=(1009,1129,1201,21169,118801,8803369,119945383009,1889389369729,3153419441929,5000000000000)
    knots=sorted(set(rec)|{1009*2**h for h in range(33) if 1009*2**h<rec[-1]})
    C=[[0.]*31 for _ in range(reps)];print('endpoint: cumulative mean (se), thresholds 11 23 31 59 107 111 119 127')
    for i,(a,b) in enumerate(zip(knots,knots[1:])):
        mass=sum((b-a)/(128*32*log(a+(b-a)*(j+.5)/128)) for j in range(128));R=sample((a+b)/2,81002+i)
        for v,r in zip(C,R):
            for j in range(31):v[j]+=mass*r[j]
        if b in rec:print(b,*(pr([v[(g-7)//4] for v in C]) for g in (11,23,31,59,107,111,119,127)),flush=True)
