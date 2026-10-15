"""R219: from-scratch check of SYNTHESIS_SPARKS4 §2.3 slot table at n ≡ 1 (8), non-square, n <= N.
For t in ±{1,2,3,4,6}: brute existence of a word (t,u,v), uv != 0, chi=(-A/n)=-1 [any sign / positive only]
versus the table criterion "some odd prime q | tn+1 with (-t/q) = -1" (Kronecker (-t/q) for odd q)."""
import sys, math
def jac(a,n):
    a%=n; r=1
    while a:
        while a%2==0:
            a//=2
            if n%8 in (3,5): r=-r
        a,n=n,a
        if a%4==3 and n%4==3: r=-r
        a%=n
    return r if n==1 else 0
def fac(m):
    f={};p=2
    while p*p<=m:
        while m%p==0: f[p]=f.get(p,0)+1; m//=p
        p+=1 if p==2 else 2
    if m>1: f[m]=f.get(m,0)+1
    return f
def divisors(f):
    ds=[1]
    for p,e in f.items(): ds=[d*p**k for d in ds for k in range(e+1)]
    return ds
def brute(n,t):
    M=t*n+1; anyw=posw=False
    for d in divisors(fac(abs(M))):
        for A in (d,-d):
            if A==-1 or (A+1)%t: continue
            B=M//A
            if B==-1: continue
            u=(A+1)//t; v=(B+1)//t
            assert u and v and t*u*v-u-v==n
            if jac(-A,n)==-1:
                anyw=True
                if t>0 and u>0 and v>0: posw=True
    return anyw,posw
def crit(n,t):
    return any(q%2 and jac(-t,q)==-1 for q in fac(abs(t*n+1)))
if __name__=="__main__":
    N=int(sys.argv[1]); cnt=0; mism={}; posmism={}
    for n in range(9,N+1,8):
        if math.isqrt(n)**2==n: continue
        cnt+=1
        for t in (1,-1,2,-2,3,-3,4,-4,6,-6):
            a,p=brute(n,t); c=crit(n,t)
            if a!=c: mism.setdefault(t,[]).append(n)
            if t>0 and p!=c: posmism.setdefault(t,[]).append(n)
    print("n count",cnt)
    print("signed/any mismatches:",{t:len(v) for t,v in mism.items()})
    print("positive-only mismatches:",{t:(len(v),v[:5]) for t,v in posmism.items()})
    # positive t=6 slot: claimed repair criterion "6n+1 has a divisor d ≡ 17 or 23 (mod 24)"
    bad=[n for n in range(9,N+1,8) if math.isqrt(n)**2!=n and brute(n,6)[1]!=any(d%24 in (17,23) for d in divisors(fac(6*n+1)))]
    print("positive t=6 vs divisor ≡17,23 (24) criterion mismatches:",len(bad))
