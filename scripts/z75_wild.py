"""Exact finite probes for PROOF_WILD. Standard library, no external data except named screens."""
from math import gcd, isqrt
from itertools import combinations
from pathlib import Path
from sys import argv


def fac(n):
    ans = {}; q = 2
    while q*q <= n:
        while n%q == 0:
            n //= q; ans[q] = ans.get(q, 0)+1
        q = 3 if q == 2 else q+2
    if n > 1: ans[n] = 1
    return ans


def divs(n):
    ds = [1]
    for q,e in fac(n).items(): ds = [d*q**i for i in range(e+1) for d in ds]
    return ds


def jac(a,n):
    a %= n; s = 1
    while a:
        while a%2 == 0:
            a //= 2
            if n%8 in (3,5): s = -s
        if n%4 == a%4 == 3: s = -s
        a,n = n%a,a
    return s if n == 1 else 0


def triples(n):
    # u <= v and min(t,u)^3 <= 2n; at most two passes per triple.
    h=1
    while (h+1)**3 <= 2*n: h+=1
    out=set()
    for i in range(2,h+1):
        for q in divs(n+i):
            if (q+1)%i == 0 and (t:=(q+1)//i) >= 2 and (v:=(n+i)//q) >= i:
                out.add((i,t,v))
        for q in divs(i*n+1):
            s=(i*n+1)//q
            if q<=s and q%i == s%i == i-1 and (u:=(q+1)//i)>=2:
                out.add((u,i,(s+1)//i))
    assert all(t*u*v-u-v==n for u,t,v in out)
    return sorted(out)


def folds(n, ts):
    # Unfold all oriented triples about an interior pivot. Reverse tails via Euclid.
    out=set(); change=set(); proper=set()
    for U,t,V in ts:
        for U,V in {(U,V),(V,U)}:
            for a in divs(V):
                for b in divs(U):
                    L,R=U//b,V//a
                    if not (a<L and b<R and gcd(a,L)==gcd(b,R)==1): continue
                    # R == q L mod n. L need not be invertible for composite n.
                    if gcd(L,n)>1: continue
                    q=R*pow(L,-1,n)%n
                    if gcd(q,n)>1: continue
                    assert jac(q,n)*jac(a*b,n)==jac(U*V,n) or gcd(a*b,n)>1
                    out.add(q)
                    if a*b>1: proper.add(q)
                    if jac(a*b,n)<0: change.add(q)
    return len(out),len(proper),len(change)


def merge_probe(n,k):
    if k%2 or n%2==0: raise ValueError
    a=(n+1)//2
    init=(a,n*a)*(k//2)
    for i in range(len(init)):
        m=init[i]; work={tuple(sorted(init[:i]+init[i+1:]+(m+1,m*(m+1))))}
        while work:
            if len(next(iter(work)))==3: return True
            nxt=set()
            for w in work:
                for s,t in combinations(range(len(w)),2):
                    u,v=w[s],w[t]
                    if u*v%(u+v)==0: nxt.add(tuple(sorted(tuple(x for j,x in enumerate(w) if j not in (s,t))+(u*v//(u+v),))))
            work=nxt
    return False


def cycles(n,k,cap):
    # Return first (r, order) such that a twisted coset is fully occupied modulo sign.
    for r in range((-n)%k, min(cap,(k-1)*n)+1,k):
        if r<3 or gcd(r,n)>1: continue
        x=(n+r)//k
        if x>3*n//k: continue
        D={d%r for d in divs(x)}; v=1; orb=[]
        while True:
            orb.append(v); v=v*n%r
            if v in (1,r-1): break
        if v != r-1 or len(orb)>len(D): continue
        E=D|{-d%r for d in D}
        if any(all(d*h%r in E for h in orb) for d in D):
            assert any((-d)%r in D or (-n*d)%r in D for d in D)
            return (r,2*len(orb))
    return (0,0)


def direct(n,k):
    for x in range(n//k+1,3*n//k+1):
        a,b=k*x-n,n*x; g=gcd(a,b); a//=g; b//=g
        if any((d+b)%a==0 for d in divs(b*b)): return True
    return False


def screen():
    stars=[int(l.split()[0]) for l in Path('data/z58/screens/star_prime_zeros.txt').read_text().splitlines() if l and not l.startswith('#')]
    print('n ts neg odd fold proper flips cyc_r cyc_ord norm2 norm4 merge4')
    for n in sorted(set(stars+[9,25,49,81,121,105,4545,193,2521,3361,66529,214729,131,241])):
        ts=triples(n); neg=sum(jac(u*v,n)<0 for u,t,v in ts); norm=[sum(t==s and jac(u*v,n)<0 for u,t,v in ts) for s in (2,4)]
        print(n,len(ts),neg,neg%2,*folds(n,ts),*cycles(n,4,511),*norm,int(merge_probe(n,4)))
    for n in (131,241): print('numerator8',n,'direct,cycle,merge',direct(n,8),cycles(n,8,n*2),merge_probe(n,8))
    for l in Path('data/z58/screens/r8_zeros_1e10.txt').read_text().splitlines():
        if l and not l.startswith('#'):
            n=int(l.split()[0]); print('R8-control',n,'4-cycle',*cycles(n,4,127),'4-merge',int(merge_probe(n,4)))


def hj(p,q):
    w=[]
    while q:
        v=(p+q-1)//q; w.append(v); p,q=q,v*q-p
    return w


def pivots(w):
    def ks(letters):
        k=[0,1]
        for b in letters: k.append(b*k[-1]-k[-2])
        return k[1:]
    left=ks(w); right=ks(w[::-1])[::-1]; out=[]
    for i in range(1,len(w)-1):
        L,a,R,b=left[i],left[i-1],right[i+1],right[i+2]
        t,rem=divmod(w[i],a*b)
        if not rem and t>=2: out.append((i,(min(b*L,a*R),t,max(b*L,a*R))))
    return out


def double(n,ts):
    pairs=set()
    for U,t,V in ts:
        e=n%U
        if not e or V%e: continue
        W=V//e
        if (W+1)%U: continue
        k=(W+1)//U
        if k<2 or k==t: continue
        for L in divs(U):
            R=U//L
            for a in divs(e):
                b=e//a
                if a<L and b<R and gcd(a,L)==gcd(b,R)==1:
                    pairs.add(tuple(sorted(((U,t,V),(U,k,e*(t*U-1))))))
    return pairs


def deep():
    print('Primes 1 mod 4 in 5..1201: independent HJ traversal vs factor inverse')
    checked=pairn=flips=0; flip0=None
    for n in range(5,1202,4):
        if n not in fac(n): continue
        directq=set(); pairs=set(); ts=triples(n)
        for q in range(1,n):
            ps=pivots(hj(n,q))
            if ps: directq.add(q)
            if len(ps)>1:
                assert len(ps)==2 and ps[1][0]==ps[0][0]+1
                if ps[0][1]!=ps[1][1]: pairs.add(tuple(sorted((ps[0][1],ps[1][1]))))
        assert len(directq)==folds(n,ts)[0] and pairs==double(n,ts)
        checked+=1; pairn+=len(pairs)
        for X,Y in pairs:
            U,t,V=X; s=jac(V*Y[2],n); assert s==jac(U*(n%U),n)
            if s<0:
                flips+=1
                if flip0 is None: flip0=n,X,Y
    print('primes, pairs, flips, first negative switch:',checked,pairn,flips,flip0)
    print('p pairs flip_pairs eg')
    for n in (193,409,2521,3361,5569,9601,19609,66529,214729,8813281,17401609,20840951041,23296553281):
        pairs=sorted(double(n,triples(n))); flips=[(X,Y) for X,Y in pairs if jac(X[2]*Y[2],n)<0]
        print(n,len(pairs),len(flips),flips[:1])
    for m in (20840951041,23296553281): print('extra R8 control',m,'4-cycle',cycles(m,4,127),'4-merge',int(merge_probe(m,4)))
    print('p increasing_crossings negative_switches least_B and witness (V,U,W,t,k,A,B)')
    for n in (193,409,2521,3361,5569,9601,19609,66529,214729,8813281):
        ts=triples(n); crossing=[]; good=[]
        for V,t,U in ts:
            if V>=U: continue
            for u,k,W in ts:
                if U!=u or U>=W: continue
                h=k*U-1; g=gcd(V,h); A,B=V//g,h//g
                assert B>k*A and (t-k)%B==0 and gcd(k*t,B)==1
                row=(V,U,W,t,k,A,B); crossing.append(row)
                if jac(V*W,n)<0:
                    assert jac(U*A*B,n)==-1
                    good.append(row)
        print(n,len(crossing),len(good),min(good,key=lambda r:r[-1]) if good else '-')
    print('full-cycle checks for small misses')
    for n in (193,2521,3361,5569,9601): print(n,cycles(n,4,2*n))


if __name__=='__main__':
    if argv[1:]==['screen']: screen()
    elif argv[1:]==['deep']: deep()
    else: raise SystemExit('usage: screen | deep')
