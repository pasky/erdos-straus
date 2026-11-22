"""Precommitted R2 marked vs unmarked pair transition forecast (no prime training)."""
from math import log
from random import Random
from subprocess import check_output
from collections import defaultdict
from pathlib import Path
P=Path('data/z81/gap');RS=(1,121,169,289,361,529);rng=Random(81081)
def extract(a,b,B,table):
    for line in check_output([str(P/'controls.bin'),str(a),str(b),str(B),'phase'],text=True).splitlines():
        r,k,s,n,first,x,y=map(int,line.split());v=table[r,k,s];v[0]+=n;v[1]+=first;v[2]+=x;v[3]+=y

def rates(table):
    out=[defaultdict(float) for _ in range(3)];back=0
    for r in RS:
        for variant in range(3):
            phases=[1/6,0]
            for k in range(3,124,8):
                marginal=table[r,k,-1];unmarked=[a+b for a,b in zip(table[r,k,0],table[r,k,1])]
                nxt=[0.,0.]
                for phase,mass in enumerate(phases):
                    if not mass:continue
                    row=marginal if k==3 or variant==0 else unmarked if variant==1 else table[r,k,phase]
                    if not row[0]:back+=1;row=unmarked if unmarked[0] else marginal
                    n,f,a,b=row;out[variant][k+4]+=mass*f/n;nxt[0]+=mass*a/n;nxt[1]+=mass*b/n
                if k+4<=123:out[variant][k+8]+=sum(nxt)
                phases=nxt
    return out,back

def experiment(a,b):
    table=defaultdict(lambda:[0]*4);B=int(log(b));w=min(1<<20,(b-a)//4)
    for j in range(4):
        l=a+(b-a)*j//4;h=a+(b-a)*(j+1)//4;L=rng.randint(l,h-w);extract(L,L+w,B,table)
    return rates(table)
if __name__=='__main__':
    table=defaultdict(lambda:[0]*4);extract(10**7+1,2*10**7+1,16,table);out,back=rates(table)
    print('bulk threshold independent linked-unmarked linked-phase; backoffs',back)
    for k in range(7,128,4):print(k,*(f'{u[k]*18878:.6g}' for u in out))
    counts=[defaultdict(float) for _ in range(3)];start=10**6;rec=(8803369,119945383009,1889389369729,3153419441929,5000000000000)
    knots=sorted(set(rec)|{start*2**h for h in range(23) if start*2**h<rec[-1]});total_back=0
    print('endpoint; threshold: independent,linked-unmarked,linked-phase (integral since 1e6)')
    for a,b in zip(knots,knots[1:]):
        out,back=experiment(a+1,b+1);total_back+=back;width=(b-a)/128;mass=sum(width/(32*log(a+width*(j+.5))) for j in range(128))
        for i,u in enumerate(out):
            for k,val in u.items():counts[i][k]+=val*mass
        if b in rec:
            print(b,*(str(k)+':'+','.join(f'{c[k]:.6g}' for c in counts) for k in (59,107,111,119,127)),'highest mean>=1',*[max(k for k,v in c.items() if v>=1) for c in counts])
    print('total positive-weight empty-cell backoffs',total_back)
