"""z53 HYPSUMPROD: exponent bookkeeping for the square-sieve bound on a block (U,V,W), U=n^a, V=n^b (a<=b), W=n^c, c=1-a-b.
All quantities are exponents base n (log factors and constants ignored). See Z53_HYPSUMPROD.md section 4.
A   = {(C,k): C ~ W, 4Ck-n in (U+V,2U+2V]};   |A| <= V + E1,  E1 = psi-discrepancy at Q=1.
Per class (c0,k0) mod Q (Q=n^q): E <= L/H + sum_{h<=H} h^-1 |sum_j e(h g(j))|, L=W/Q, g(j)=(n+s)/(4Q(c0+Qj)):
   lambda_r = h*(UV)*Q^(r-1)/W^r  (r=1,2,3).
Exponential-sum tests: trivial L; Kusmin-Landau 1/lambda1 (if lambda1<=1/2); 2nd deriv L l2^1/2 + l2^-1/2; 3rd deriv L l3^1/6 + L^1/2 l3^-1/6.
Square sieve (P=n^rho primes, Q=P^2): N <= |A|/P + max_Q( |A|/Q + Q^2 * E ).   Output: theta_sq(a,b) vs trivial t=min(a,b,c)."""
import itertools, math, json, sys
def es(L, l1, l2, l3):
    # exponent of best available bound for |sum_{j~L} e(h g(j))|
    c=[L]
    if l1 < 0: c.append(-l1)                       # Kusmin-Landau (needs lambda1 <= 1/2; exponents: l1<0)
    c.append(max(L + l2/2, -l2/2))                 # second derivative test
    c.append(max(L + l3/6, L/2 - l3/6))            # third derivative test (Titchmarsh 5.11)
    return min(c)
def per_class(a,b,c,q,eH):
    L=c-q
    if L < 0: return None
    best=None
    worst=L-eH
    for eh in [0.0, eH]:                           # endpoints suffice: each test is max of two monotone pieces in h
        l1=eh+a+b-c; l2=eh+q+a+b-2*c; l3=eh+2*q+a+b-3*c
        worst=max(worst, es(L,l1,l2,l3))
    # interior h: the bound max(.,.) of monotone pieces is quasi-convex; check a few interior points too
    for t in [0.25,0.5,0.75]:
        eh=t*eH; l1=eh+a+b-c; l2=eh+q+a+b-2*c; l3=eh+2*q+a+b-3*c
        worst=max(worst, es(L,l1,l2,l3))
    return worst
def theta(a,b):
    c=1-a-b
    best=(9,None)
    for rho in [i/2000 for i in range(0,401)]:
        q=2*rho
        if q > c: break
        for eH in [i/400 for i in range(0,201)]:
            e1=per_class(a,b,c,0.0,eH)
            if e1 is None: continue
            A=max(b,e1)
            eq=per_class(a,b,c,q,eH)
            if eq is None: continue
            th=max(A-rho, A-q, 2*q+eq)
            if th < best[0]: best=(th,(rho,eH))
    return best
if __name__=="__main__":
    out=[]
    step=float(sys.argv[1]) if len(sys.argv)>1 else 1/60
    pts=[]
    a=0.0
    N=int(round(1/step))
    for i in range(N+1):
        for j in range(i,N+1):
            a=i*step; b=j*step
            if a+b>1+1e-12: continue
            pts.append((a,b))
    res=[]
    for (a,b) in pts:
        c=1-a-b; t=min(a,b,c)
        th,par=theta(a,b)
        res.append(dict(a=round(a,4),b=round(b,4),c=round(c,4),trivial=round(t,5),sq=round(th,5),gain=round(t-th,5),par=par))
    json.dump(res,open(sys.argv[2] if len(sys.argv)>2 else "/tmp/sqmap.json","w"))
    win=[r for r in res if r['gain']>1e-9]
    print("points",len(res),"square-sieve beats trivial at",len(win))
    for r in sorted(win,key=lambda r:-r['trivial'])[:40]: print(r)
    # global exponent: max over simplex of min(trivial, sq)
    g=max(min(r['trivial'],r['sq']) for r in res)
    print("max over grid of min(trivial,sq) =",g, " (1/3 =",1/3,")")
