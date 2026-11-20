"""Per-prime marginal budgets, exact rational arithmetic. See R17_PUSH."""
from z77_combine import *
from z76_lift import ceildiv
base=Path('data/z78')
p5={r:s for p in (base/'p5').glob('*.txt') for r,*s in rows(p)}

def shiftcap(r,k,sums):
    # r^( (k-1)/2 ) * 2^j small shifts. Both orientations remain inside the same
    # inverse-stable survivor set mod r. Use a complete-block count + remainder.
    live=(r-1)//2-L[r][-1];n=r**k
    return min(s+2*(t//r*live+min(live,t%r)) for j,s in enumerate(sums)
               for t in [(n//(r**((k-1)//2)<<j)+1)//2])

def zbudget(r):
    ps=[];qs=[]
    for T,cap,ls in [(P,800,ps),(Q,100,qs)]:
        for k in range(3,801,2):
            n=r**k
            if n>=1<<cap:break
            # A missing low table row may charge all surviving classes at that depth.
            try:ct=bound(T,n)
            except AssertionError:ct=n if T is Q else r**((k+1)//2)
            if T is P and k==3:ct=min(ct,shiftcap(r,k,S[r]))
            if T is P and k==5 and r in p5:ct=min(ct,shiftcap(r,k,p5[r]))
            ls.append(F(ct,r**((k+1)//2 if T is P else k)))
    tail=F(364,1000*isqrt(r))+F(3,100000)
    if r>=4096:tail=min(tail,F(16,100*isqrt(r))+F(1,25000))
    return [F(L[r][-1],r),ps[0],qs[0],ps[1],sum(ps[2:]),sum(qs[1:]),tail]

if __name__=='__main__':
    import sys
    primes=[r for r in L if r<7219]
    if '--partial' not in sys.argv:assert set(p5)==set(primes)
    fail=[];stats=[]
    for r in primes:
        part=zbudget(r);v=sum(part)
        if v>=F(r-1,2*r):fail.append(r)
        stats.append((v,r,part))
    print('fail',*fail);mx=max(fail); ok=[row for row in stats if row[1]>mx]
    if ok:
        v,r,part=max(ok);print('first',min(r for _,r,_ in ok),'binding',r,ppm(v),*[ppm(x) for x in part])
    print('last failure',mx,*(ppm(x) for x in zbudget(mx)))
