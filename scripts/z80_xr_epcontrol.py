"""Opus cross-review of R17_WALK (NOT a certificate): positive containment controls for the reviewer's
independent J/Hd engine (scripts/z80_xr_ep.c compiled with -DGEN: general weights p,q, both roots, e<=E0 := twice the largest listed shift).
Ground truth: the complete M17B P lists data/m17b/p{2L-1}.txt at r=17, L=2..4 (as in z79_r2check.py).
For synthetic endpoints (p,q) with q == -p a/b (mod U) built from each listed tuple, run the engine with the
cutoff equal to that tuple's own index and require  expected <= found <= genuine.
usage: python scripts/z80_xr_epcontrol.py BINARY
"""
import sys,subprocess
from pathlib import Path
exe=sys.argv[1];r=17
fired={'J':0,'Hd':0};checks=0
for L in (2,3,4):
    U=r**L;B=U//r;N=U*B
    data=[tuple(map(int,l.split())) for l in Path(f'data/m17b/p{2*L-1}.txt').read_text().splitlines()]
    E0=2*max(4*a*b*d-N for a,b,c,d in data)   # test universe: hits with e<=E0 (all listed tuples qualify)
    def idx(t,p,q,mode):
        a,b,c,d=t;e=4*a*b*d-N
        if (p*a+q*b)%U:return None
        H=(p*a+q*b)//U;J=(4*p*a*a*d+q*e)//U
        return {'J':J,'Hd':H*d}[mode]
    for p in range(1,40):
        for t in data[::3]:
            a,b,c,d=t;q=(-p*a*pow(b,-1,U))%U
            if not q or p+q>199:continue
            for mode in (('J','Hd') if L<4 else ('Hd',)):
                C=idx(t,p,q,mode)
                if C is None or C>3000000:continue
                for sig in ((12,) if mode=='J' else (3,12,20)):
                    args=[exe,str(r),str(L),str(p),mode,str(C),str(sig),'AB','1','0',str(q),str(E0)]
                    out=subprocess.run(args,capture_output=True,text=True,timeout=300,check=True).stdout.splitlines()
                    got={tuple(map(int,l.split()[1:4])) for l in out if l.startswith('HIT')}
                    exp={(x[0],x[1],x[3]) for x in data if (i:=idx(x,p,q,mode)) is not None and 1<=i<=C}
                    gen={(x[0],x[1],x[3]) for x in data if (x[0]*p+x[1]*q)%U==0}
                    assert exp and exp<=got<=gen,(L,p,q,mode,C,sig,exp-got,got-gen)
                    fired[mode]+=1;checks+=1
    print('L',L,'cumulative checks',checks,fired,flush=True)
print('positive containment checks',checks,fired)
