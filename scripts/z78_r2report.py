"""Exact rational audit; native depths and ppm printed separately. Row header for ledger.tsv:
r exact_live_after3 live_ppm P7_ppm P9_ppm P11plus_ppm Q5plus_ppm tails_ppm residual_ppm pass
Positive values in ppm rounded upwards; exact fractions used for comparisons.
"""
from z78_r2ledger import *
primes=[r for r in range(17,919) if all(r%i for i in range(2,isqrt(r)+1))];assert set(primes)<=small.keys()
rowsout=[];stats=[];fail=[]
with (R/'ledger.tsv').open('w') as f,(R/'small.tsv').open('w') as sm:
    print('r live_fraction live_ppm P7 P9 P11 P13_later Qfinite Ptail Qtail residual_ppm binding_level',file=sm)
    for r in primes:
        a,p,q,t,u=budget(r);res=sum(p)+q+t+u;ok=res<a
        print(r,a,ppm(a),ppm(p[0]),ppm(p[1]),ppm(sum(p[2:])),ppm(q),ppm(t+u),ppm(res),int(ok),file=f,flush=True)
        if not ok:fail.append(r)
        h=F(r-1,2*r);c1,c2,c3,c5=small[r];row=[F(c1,r),F(c2,r*r),F(c3,r**3),F(c5,r**3),p[0],p[1],sum(p[2:]),q,t,u]
        assert h-sum(row)==a-res
        stats.append((r,h,a-res,row))
        if r<=211:
            groups=list(zip(p,[f'P{k}' for k in range(7,7+2*len(p),2)]))+[(q,'Q5+'),(t,'Ptail'),(u,'Qtail')]
            print(r,a,ppm(a),ppm(p[0]),ppm(p[1]),ppm(p[2]),ppm(sum(p[3:])),ppm(q),ppm(t),ppm(u),ppm(res),max(groups)[1],file=sm)
last=max(fail);ok=[x for x in stats if x[0]>last];r,h,m,row=min(ok,key=lambda x:x[2]);print('first',ok[0][0],'binding_by_margin',r, 'margin_ppm_floor',int(m*1000000),'total',ppm(sum(row)), 'parts',*[ppm(x) for x in row]);print('failing_primes',*fail)
