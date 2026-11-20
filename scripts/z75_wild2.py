"""Round 2 exact finite probes. Invoke python -B so the import leaves no worktree cache."""
from math import gcd, comb, isqrt as isqrt_exact
from z75_wild import triples, fac, divs, jac, direct


def seed(n,ts):
    out=[]
    for u,t,v in ts:
        if (n-1)%(t+1) or jac(u*v,n)!=-1: continue
        b=(n-1)//(t+1); A=t+1; B=t*b+1; C=t*u-1; D=t*v-1
        assert A*B==C*D and (t*b+b+1)==n
        if jac(-A,n)!=1: continue
        g=gcd(A,C); i=A//g; j=C//g; h=B//j
        assert g*j==C and i*h==D and h*j==B and (i+j)%t==0 and jac(i*j,n)==-1
        out.append((u,t,v,b,(g,i,j,h)))
    return out


def rank(mat,p):
    if not mat: return 0
    r=0
    for c in range(len(mat[0])):
        row=next((i for i in range(r,len(mat)) if mat[i][c]%p),None)
        if row is None: continue
        mat[r],mat[row]=mat[row],mat[r]; a=mat[r]; inv=pow(a[c],-1,p)
        for j in range(r+1,len(mat)):
            k=mat[j][c]*inv%p
            if k:
                v=mat[j]; mat[j]=[(x-k*y)%p for x,y in zip(v,a)]
        r+=1
        if r==len(mat): break
    return r


def jets(p,ts,m=3):
    h=(p-1)//2
    S={t*z-1 for u,t,v in ts for z in (u,v)}
    Q=sorted(a for a in S if pow(a,h,p)==1)
    assert all(1<a<p and pow(a,-1,p) in S for a in S)
    C=[[pow(a,h,p),1] for a in S]; cr=rank(C,p)
    d=min(len(Q)-1,7)
    columns=[(i,j) for i in range(d+1) for j in range(m)]
    mat=[]
    for a in Q:
        for k in range(m):
            # coefficient of Z^k in (a+Z)^i * ((a+Z)^h-1)^j
            mat.append([sum((-1)**(j-b)*comb(j,b)*comb(i+b*h,k)*pow(a,i+b*h-k,p)
                            for b in range(j+1))%p for i,j in columns])
    R=rank(mat,p); assert R==m*min(d+1,len(Q))
    return len(S),len(Q),cr,d,R


def flat_check(p,m):
    h=(p-1)//2; D=(2*((m+1)//2)-1)*h
    for d in (D-1,D):
        exps=[e for e in range(-d,d+1) if (e-h)%(2*h)==0]
        # (X d/dX)^j is equivalent to Hasse jets for j<p
        mat=[[pow(e,j,p) for e in exps] for j in range(m)]
        ext=[row+[int(j==0)] for j,row in enumerate(mat)]
        assert (rank(mat,p)==rank(ext,p))==(d==D)
    return D


def catalogue(cap):
    ns=set()
    for a in range(2,cap+1):
        if a**3-(a-1)**3>cap: break
        for b in range(1,a):
            A=a**3; B=b**3
            while A-B<=cap:
                ns.add(A-B)
                if A+B<=cap: ns.add(A+B)
                A*=a; B*=b
    return ns


def core_probe(n,ns,ts):
    # Reverse engine: for each exact word, possible N are multiples of d dividing n+u
    out=set()
    for U,t,V in ts:
        for u,v in {(U,V),(V,U)}:
            d=t*u-1
            if jac(d,n)!=-1: continue
            for f in divs(v):
                N=d*f
                if N in ns: out.add((N,u,t,v))
    return out


def forward(n,ns):
    out=set()
    for N in ns:
        if N>2*n+1: continue
        u0=(-n)%N
        if u0<2 or 2*u0>N+1: continue
        for d in divs(N):
            if (d+1)%u0 or jac(d,n)!=-1: continue
            t=(d+1)//u0; v=(n+u0)//d
            if min(t,v)>=2: out.add((N,u0,t,v))
    return out


def coupled(n,k,H):
    # Exact enumeration of both ratio hits with coprime a,b <=H
    hits=set(); slots=set()
    for a in range(1,H+1):
        for b in range(1,H+1):
            if gcd(a,b)!=1: continue
            L=a*b
            for x in range((n//(k*L)+1)*L,3*n//k+1,L):
                if gcd(k*x-n,n*x)==1: slots.add(x)
            for N in (a+b,a+n*b):
                for r in divs(N):
                    if r>2*n or (r+n)%(k*L): continue
                    x=(r+n)//k
                    if gcd(r,n*x)==1: hits.add(x)
    assert hits<=slots
    for x in hits:
        r=k*x-n
        A=set(d%r for d in divs(x) if d<=H)
        assert any((-v)%r in A or (-n*v)%r in A for v in A)
    return len(slots),len(hits)


def main():
    cap=50000; ns=catalogue(cap)
    print('N catalogue, bound and count:',cap,len(ns))
    print('n seed_count first(u,t,v,b,(g,i,j,h)); core_count max_core')
    inputs=(9,25,49,81,121,105,4545,193,409,2521,3361,5569,9601,18169,21841,1269241,8813281,131,241)
    for n in inputs:
        ts=triples(n); s=seed(n,ts); c=core_probe(n,ns,ts)
        if n<=2521: assert c==forward(n,ns)
        print(n,len(s),s[:1],len(c),max(c,default=(0,))[0])
        if n in (193,409,2521): print('slope,QR,rank[chi,1],d,QR-jet-rank',*jets(n,ts))
        if n in (193,409,2521,3361,5569,9601,21841,4545,49): print('kd ratio H=8 slots,hits',*coupled(n,4,8))
    for n in (131,241): print('8-controls',n,'exact',direct(n,8),'slots,hits',*coupled(n,8,8))
    print('flat mask checks (m=1..7)')
    for p in (17,41,193,409,2521): print(p,[flat_check(p,m) for m in range(1,8)])
    print('signed-seed census, primes 1 mod 840 <=200000')
    ps=[p for p in range(841,200001,840) if p in fac(p)]
    misses=[p for p in ps if not seed(p,triples(p))]
    print(len(ps),len(misses),misses[:15])
    for p in (18169,1269241):
        # independent fixed signed seed enumeration of all possible positive outputs
        out=[(t,d) for z in divs(p-1) if (t:=z-1)>=2 and jac(-z,p)==1
             for d in divs(t*p+1) if 2*t-1<=d<=isqrt_exact(t*p+1) and d%t==t-1 and jac(d,p)==-1]
        print('independent signed-seed zeros',p,out)
        assert not out and p in fac(p)


if __name__=='__main__': main()
