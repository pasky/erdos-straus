#!/usr/bin/env python3
"""Exploratory (slow) ell-local envelope experiment; not the fast verifier."""
from sympy import factorint
from sympy.ntheory.modular import crt
from random import Random
import json, time
import numpy as np

ELLS = [103, 199, 431, 863, 1699, 3467, 6899, 13799]
KS = [1, 5, 9, 13, 17]
NSAMPLES = 40
MAX_N = 100_000_000
MIN_N = 1_000_000
MAX_RES = 20000
SEED = 20260819


def has_exact_witness(x, q):
    """Find d|x^2 making both reconstructed denominators integral."""
    divisors = [1]
    for p, e in factorint(x).items():
        powers = [p**j for j in range(2 * e + 1)]
        divisors = [a * b for a in divisors for b in powers]
        if any((d + x) % q == 0 and (x + x * x // d) % q == 0
               for d in divisors):
            return True
    return (1 + x) % q == 0 and (x + x * x) % q == 0


def witness(n, ell, k, half):
    w=k*ell
    if half=='B':
        if (n+w)%4: return False
        x=(n+w)//4
    else:
        if (n*w+1)%4: return False
        x=(n*w+1)//4
    return has_exact_witness(x,w)


def f_pw(ell):
    a=(ell+1)//4
    fac=factorint(a)
    tau_a2=1
    for e in fac.values(): tau_a2*=2*e+1
    return tau_a2//2


def run_ell(ell):
    rng=Random(SEED+ell)
    residues=list(range(1,ell))
    if len(residues)>MAX_RES: residues=rng.sample(residues,MAX_RES)
    # Every target is selected n == r (ell), n == 1 (4), the only hard mod-4 class.
    bases={r:int(crt([ell,4],[r,1])[0]) for r in residues}
    states={r:{(h,k):True for h in 'BA' for k in KS} for r in residues}
    union={r:True for r in residues}
    examples={}
    lo=lambda b: max(0,(MIN_N-b+4*ell-1)//(4*ell))
    hi=lambda b: (MAX_N-b)//(4*ell)
    for j in range(NSAMPLES):
        alive=[r for r in residues if union[r] or any(states[r].values())]
        for r in alive:
            b=bases[r]; L,H=lo(b),hi(b)
            idx=rng.randint(L,H)
            n=b+4*ell*idx
            any_now=False
            for h in 'BA':
                for k in KS:
                    key=(h,k)
                    if states[r][key] or union[r]:
                        ok=witness(n,ell,k,h)
                        if states[r][key] and not ok: states[r][key]=False
                        if ok:
                            any_now=True
                            examples.setdefault((r,h,k),(n,))
            if union[r] and not any_now: union[r]=False
        print(ell,j+1,len(alive),sum(union.values()),flush=True)
    scale=(ell-1)/len(residues)
    counts={f'{h}{k}':sum(states[r][(h,k)] for r in residues)*scale for h in 'BA' for k in KS}
    out={'ell':ell,'tested':len(residues),'samples':NSAMPLES,'scale':scale,'f':f_pw(ell),
         'B1':counts['B1'],'A1':counts['A1'],'union':sum(union.values())*scale,
         'counts':counts,'passing_residues':[r for r in residues if union[r]][:100]}
    print('RESULT',json.dumps(out),flush=True)
    return out

if __name__=='__main__':
    outs=[]
    for ell in ELLS:
        t=time.time(); outs.append(run_ell(ell)); print('SECONDS',ell,time.time()-t,flush=True)
    open('/tmp/es-unitB/phase0-results.json','w').write(json.dumps(outs,indent=2))
    # Descriptive fit only: log A = alpha + beta log log ell.  It is
    # degenerate here because every measured reduced envelope equals one.
    xx=np.log(np.log(np.array([row['ell'] for row in outs],dtype=float)))
    yy=np.log(np.array([row['union'] for row in outs],dtype=float))
    X=np.column_stack((np.ones(len(xx)),xx))
    coeff=np.linalg.lstsq(X,yy,rcond=None)[0]
    resid=yy-X@coeff
    se=np.sqrt((resid@resid)/(len(xx)-2)*np.linalg.inv(X.T@X)[1,1])
    print(f'FIT beta={coeff[1]:.6f} standard_error={se:.6f}')
