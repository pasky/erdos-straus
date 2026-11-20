"""Recurse in ACTUAL BOX DEPTH. Rational lower bound on alive mass, no assumption
of uniformity. For measure loss monotonicity, evaluate the *survival map* at
our lower bound, not a marginal-cost bound at fictitious lower aliveness."""
from z78_combine import *
from z78_pack import packed
layers={n.bit_length()-1:(cut,v) for p in (base/'layer').glob('*.txt') for n,cut,*v in rows(p)}
small={r:(a,b,c,d) for r,a,b,c,d in [list(map(int,l.split())) for l in (base/'exact/union.tsv').read_text().splitlines()[1:]]}

qcnt=lambda pfx:{r:n for p in (base/'qscan').glob(pfx+'*.txt') for r,n in rows(p)}
qsleft,qshit=qcnt('left'),qcnt('scan')
qrows={r:n for p in (base/'qrows').glob('*.txt') for r,n in rows(p)}
p7={r:v for p in (base/'p7').glob('*.txt') for r,*v in rows(p)}
five={r:v for p in (base/'p5fine').glob('*.txt') for r,*v in rows(p)}
local={}
for path in (base/'local').glob('*.txt'):
    for line in path.read_text().splitlines():
        rr,kk,cc,*arr=line.split();local[int(rr),int(kk)]=[(1<<(int(cc)+i),*map(int,x.split(':'))) for i,x in enumerate(arr)]
def budget2(r):
    parts=zbudget(r)
    if r in qrows:parts[2]=min(parts[2],F(qrows[r]+q3[r][0]+2*q3[r][3],r**3))
    if r in qsleft:parts[2]=min(parts[2],F(qsleft[r]+qshit[r]+q3[r][0]+2*q3[r][3],r**3))
    lv=F(r-1,2*r)-parts[0]
    def step(depth,lower,old,k,splits):
        # Amortised per-parent cap map times inverse-stable live sets.
        W=r**depth; best=lower-old; N=r**k
        for E,s,c in splits:
            T=(N//E+1)//2; per=2*ceildiv(T,W//r)
            best=max(best,lower-F(s+c,W),lower*(1-F(min(per,r),r))-F(s,W))
        return max(F(0),best)
    lv-=parts[1];lv-=parts[2]
    if r in small:
        a,b,c,d=small[r];assert parts[0]==F(a,r**3) and parts[1]==F(b,r**3)
        parts[2]=F(c,r**3);parts[3]=F(d,r**3);lv=F(r-1,2*r)-sum(parts[:4])
    else:
        lv=F(r-1,2*r)-sum(parts[:3]);old=parts[3];ss=p5[r]
        if r in five:
            ss=five[r];old=min(old,F(shiftcap(r,5,ss),r**3))
        x=step(3,lv,old,5,[(r*r<<j,s,r**3) for j,s in enumerate(ss)]) if lv>=0 else lv-old
        parts[3]=lv-x;lv=x
    # For a failed prime we may clip the survival lower bound to zero, but must
    # never count that as success. Later Q terms are subtracted in one charge.
    ps=F(0)
    for k in range(7,801,2):
        n=r**k;b=n.bit_length()
        if b>800:break
        D=(k+1)//2;W=r**D
        old=F(bound(P,n),W) if b>=48 else F(1)
        if lv<=0:ps+=old;lv-=old;continue
        splits=[]
        if b in layers:
            cut,v=layers[b];splits=[(1<<(cut+i),packed(1<<b,cut+i),c) for i,c in enumerate(v)]
        splits+=local.get((r,k),[])
        if k==7 and r in p7:
            splits=[(E,min(s,p7[r][E.bit_length()-1]) if E.bit_length()-1<len(p7[r]) else s,c) for E,s,c in splits]
        x=step(D,lv,old,k,splits);ps+=lv-x;lv=x
    parts[4]=ps
    return parts
if __name__=='__main__':
    primes=[r for r in L if r<7219];assert set(p3)==set(p5)==set(primes) and set(q3)=={r for r in primes if r<=5520}; assert set(small)=={r for r in [5,7,11,13]+primes if r<=211}
    stats=[];fail=[]
    for r in primes:
        p=budget2(r);v=sum(p);stats.append((v,r,p))
        if v>=F(r-1,2*r):fail.append(r)
    ok=[t for t in stats if t[1]>max(fail)];v,r,ps=max(ok)
    print('fail',*fail);print('first',min(r for v,r,p in ok),'binding',r,ppm(v),*[ppm(x) for x in ps]);print('last failure',max(fail),'passes',len(primes)-len(fail));
