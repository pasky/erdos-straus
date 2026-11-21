"""Effective constants, per-orientation completeness cutoffs, and nonempty
C results in each of the four domains vs existing independent small P data."""
from fractions import Fraction as F
from math import isqrt
from pathlib import Path
import subprocess,sys
exe=sys.argv[1];cases=[(12,60000,10**6,1500,3000000),(13,160000,3000000,11000,7400000),(14,160000,8000000,70000,29000000)]
for L,E,J,V,Y in cases:
    U=17**L;N=U*U//17;em=466*(1+isqrt(U));assert 500*E*J*V*Y**2>=U**2
    for p,q in [(1,5),(5,1)]:
        # For Hd>Y, a/b <= (p+q)^2*(1+em/N)/(68 H^2 d).
        ratio=F(36,68*Y)*(1+F(em,N));hh=(1+F(p,q)*ratio)*(1+F(em,N));jj=1/(1-F(q*em,U));zz=1+F(q,p)*(hh*jj-1)
        assert int(subprocess.check_output([exe,str(L),str(p),str(q),'bound','1','0'],timeout=30))==466*(isqrt(U-1)+1)
        assert hh<=F(1001,1000) and jj<=F(1001,1000) and zz<=F(102,100)
        assert 4*p**3*q**3*hh**3*jj*zz*500<68**3
    print('cutoff ok',L,E,J,V,Y)

def run(*args,inp=''):
    return subprocess.run(args,input=inp,check=True,timeout=300,capture_output=True,text=True).stdout
for mode in ('e','J','Hd','HZ'):
    fired=0
    for L in (2,3):
        W=17**L;N=W*W//17;B=W//17
        data=[list(map(int,l.split())) for l in Path(f'data/m17b/p{2*L-1}.txt').read_text().splitlines()]
        def domain(t,p,q):
            a,b,c,d=t;e=4*a*b*d-N
            if (p*a+q*b)%W:return 10**20
            H=(p*a+q*b)//W;J=(p*4*d*a*a+q*e)//W;S=(p*4*a*d*c+q-p)//W;Z=(p*a*S+q*H)//B
            return {'e':e,'J':J,'Hd':H*d,'HZ':H*Z}[mode]
        for p in range(1,90):
            for t in data:
                a,b,_,_=t;q=(-p*a*pow(b,-1,W))%W
                if not q or p+q>199:continue
                C=domain(t,p,q)
                if not 1<=C<=100:continue
                args=[exe,str(L),str(p),str(q),mode,str(C)];inp='' if mode=='Hd' else run('factor',inp=run(*args,'1'))
                lines=run(*args,'0',inp=inp).splitlines();got={tuple(map(int,l.split()[1:])) for l in lines if l.startswith('hit ')}
                expected={(a,b,d) for a,b,c,d in data if 0<domain((a,b,c,d),p,q)<=C}
                genuine={(a,b,d) for a,b,c,d in data if (p*a+q*b)%W==0}
                assert expected and expected<=got<=genuine;fired+=1;break
            if fired>=3:break
        if fired>=3:break
    assert fired>=3;print('positive comparisons',mode,fired)
for L,*_ in cases:
    lines=[l.split() for l in Path(f'data/z79/r2/point/{L}.txt').read_text().splitlines()]
    assert len(lines)==8 and {(int(p),int(q),m) for _,_,p,q,m,_,_,_,_ in lines}=={(p,6-p,m) for p in (1,5) for m in ('e','J','Hd','HZ')}
    for kind,l,p,q,m,c,keys,vis,hits in lines:
        assert kind=='end' and int(l)==L and int(c)==dict(zip(('e','J','HZ','Hd'),_))[m] and int(hits)==0
