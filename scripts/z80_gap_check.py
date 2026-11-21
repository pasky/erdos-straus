"""Independent per-prime certificates for g=4xmin-p (all smaller windows
exhausted) and e*=0 (the minimum feasible cap). No ET parametrisation or
AP covering used. PARI factor_proven = 1. No run above 128MB PARI stack.
"""
from math import lcm,log,exp,sqrt
from pathlib import Path
import csv,sys
from cypari2 import Pari
P=Pari();P.allocatemem(128000000,silent=True);P.default('factor_proven',1)
D=Path('data/z80/gap')
def xyz(p):
    for m in range(3,4096,4):
        x=(p+m)//4;s=p*x
        assert m<p and p%4==1 and int(P.gcd(m,s))==1
        for d in P.divisors(x*x).python():
            for h in [d,p*d]:  # h<=px, never p^2 | h as p>x.
                if h>s or (h+s)%m:continue
                y=(h+s)//m;z,r=divmod(s+s*s//h,m)
                assert not r and x<=y<=z and 4*x*y*z==p*(x*y+x*z+y*z)
                return m,x,y,z
    raise RuntimeError(f'not decided {p}')

def inputs():
    for line in (D/'deep.txt').read_text().splitlines():
        if line.startswith('REC'):
            _,p,m=line.split();yield 'record',int(p),int(m)
    for r in csv.DictReader(Path('data/z80/extreme/panel.csv').open()):
        if r['family']=='L' and r['prime']=='1':yield 'L',int(r['n']),None
    for line in Path('data/z58/screens/r8_zeros_1e10.txt').read_text().splitlines():
        if not line.startswith('#'):yield 'R8',int(line.split()[0]),None
    for p in (20840951041,23296553281,25277866681,25606400401,27112836481,28154878561,37165786681,39919266721,179530327201,452438542081,1218367081201,1511088831001,1590284203561,6955940568721):yield 'R8',p,None
    # Prescribed, no outcome selection: first 16 primes in progression >=10^e.
    q=lcm(*range(1,41))
    for e in (18,24,30,36):
        t=(10**e-1+q-1)//q;done=0
        while done<16:
            p=1+t*q;t+=1
            if P.isprime(p):yield 'L40e'+str(e),p,None;done+=1

def run():
    print('tag,p,g,x,y,z,e_star,U7_f,U7_u',flush=True)
    for tag,p,expected in inputs():
        assert P.isprime(p)
        m,x,y,z=xyz(p);assert expected in (None,m)
        for f in range(7,1000000,8):
            r=f-p%f
            if (f+1)%r==0:
                t=(f+1)//r;v=(p+r)//f
                assert v>=1 and t*r*v-r-v==p and (t*r)%8==0
                break
        else:raise RuntimeError('U7 unresolved '+str(p))
        print(tag,p,m,x,y,z,0,f,r,sep=',',flush=True)

def stats():
    rows=list(csv.DictReader((D/'checks.csv').open()));recs=[]
    for tag in dict.fromkeys(r['tag'] for r in rows):
        s=[r for r in rows if r['tag']==tag];print(tag,len(s),'max g',max(int(r['g']) for r in s),'max cap',max(int(r['e_star']) for r in s),'max first U7',max(int(r['U7_f']) for r in s))
        if tag=='record':recs=[(int(r['p']),int(r['g'])) for r in s]
    # Cummax on geometric endpoints rather than conditioning fit on record times.
    hi=int((D/'deep.txt').read_text().splitlines()[-1].split('hi=')[1].split()[0]);ns=[10**j for j in range(4,len(str(hi)))]+[hi]; s=[(log(n),max(g for p,g in recs if p<=n)) for n in ns]
    print('endpoints',ns,'maxima',[v for _,v in s]);
    for name,F in [('log/loglog',lambda t:t/log(t)),('log',lambda t:t),('log^2',lambda t:t*t),('exp(sqrt(log))',lambda t:exp(sqrt(t)))]:
        # One free multiplicative constant, least squares on a logarithmic scale.
        resid=[log(g/F(t)) for t,g in s];avg=sum(resid)/len(s);rmse=sqrt(sum((v-avg)**2 for v in resid)/len(s));print(name,'coefficient',round(exp(avg),6),'log-RMSE',round(rmse,6))
if __name__=='__main__':stats() if sys.argv[1:]==['stats'] else run()
