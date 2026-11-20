"""For all small p5 data at 17 with e<=W synthesize nontrivial endpoints
via short rational reconstruction and compare each of the THREE index searches
against its own domain in the stored complete solution list. Not an independent
large-depth census; testcut is explicit and the q/p=5 size theorem unused here."""
from z78_point import search
from pathlib import Path
from io import StringIO
from contextlib import redirect_stdout
from math import gcd
D=[tuple(map(int,s.split())) for s in Path('data/m17b/p5.txt').read_text().splitlines()];N=17**5;W=17**3;X=300
hits=[0,0,0];tests=0
for p in range(1,21):
 for q in range(1,101):
    if gcd(p,q)>1:continue
    d=[v for v in D if (p*v[0]+q*v[1])%W==0 and (v[0]+v[1])//v[2]<=W];
    if not d:continue
    for i,mode in enumerate(('Ha','Hd','J')):
        def key(v):
            a,b,c,d=v;H=(p*a+q*b)//W;J=(4*p*a*a*d+q*((a+b)//c))//W
            return {'Ha':H*a,'Hd':H*d,'J':J}[mode]
        want={v for v in d if key(v)<=X};out=StringIO()
        with redirect_stdout(out):search(17,3,p,q,mode,1,X,testcut=X)
        got={tuple(map(int,l.split()[-4:])) for l in out.getvalue().splitlines() if l.startswith('hit')}
        # Ha does not filter on e<=W; include those in its expected output.
        if mode=='Ha':want={v for v in D if (p*v[0]+q*v[1])%W==0 and key(v)<=X}
        assert got==want,(p,q,mode,got,want);hits[i]+=len(want);tests+=1
assert all(hits)
print('domain comparisons',tests,'matching positive hits Ha Hd J',*hits)
