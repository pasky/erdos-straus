"""Opus cross-review of R17_WALK (NOT a certificate): independent checks of the rational Vieta Q bound.
Modes (from repo root, uv run --offline --no-project --with sympy python -B scripts/z80_xr_qwalk.py MODE ...):
  lemma Fmax        brute-force ALL Q tuples for every modulus F<=Fmax (any F coprime to 10, not only
                    prime powers), both x=5 orientations, via (a,d,c) with f=4acd-F, ef=4a^2d+1; check
                    d <= D(F) := min over m of the walk cutoff (independent integer evaluation), and replay
                    the rational walk on each hit asserting alternation, the 5-adic denominator claims and
                    the two inequalities of the dichotomy.  Also prints the largest d/D(F) ratio seen.
  search r kmax     independent Q search at F=r^k, k odd<=kmax: roots of 4pda^2=-q via sympy.sqrt_mod,
                    candidate a<=(F+1)/(2d), and both small-factor branches (f<s or e<s) written separately.
  cut r kmax        print independent D for each k (compare with qwalk.txt column 3)
  vs r kmax         compare independent search with brute force (lemma-style enumeration) for F=r^k
"""
import sys
from fractions import Fraction as Fr
from math import isqrt, gcd

def cutoff(F, mmax=19):
    """independent: smallest D such that every d>D violates both walk alternatives, minimised over m;
    computed by exponential+bisection search on exact integers, also capped by (F+1)//2."""
    best=(F+1)//2
    for m in range(1,mmax+1):
        A=5**m+6               # stopping alternative: need 2d <= A
        def survivesB(d):      # non-stopping alternative allows d iff (4d-6)^(2m) 4d^2 <= 9 (F+1)^2 20^m 25^ceil(m/2)
            return (4*d-6)**(2*m)*4*d*d <= 9*(F+1)**2*20**m*25**((m+1)//2)
        # allowed iff 2d<=A or survivesB(d); both sets are initial segments for d>=2
        dA=A//2
        lo,hi=1,1
        while survivesB(hi):hi*=2
        while hi-lo>1:
            mid=(lo+hi)//2
            if survivesB(mid):lo=mid
            else:hi=mid
        dB=lo if survivesB(lo) else 0
        best=min(best,max(dA,dB,2))
    return best

def walk_check(p,q,a,b,h,d):
    """rational walk from the integer hit; assert every claim used in the dichotomy"""
    V=4*d*h-6; S2=Fr(V*V,5)   # S^2
    A,Bb=Fr(a),Fr(b)
    def wx(A):return p*A*A     # squared weighted coordinates X^2=pa^2, Y^2=qb^2
    def wy(B):return q*B*B
    assert p*A*A+q*Bb*Bb+h==V*A*Bb
    moves=0;last=None;log=[]
    while moves<400:
        X2,Y2=wx(A),wy(Bb)
        # larger exceeds S/2 times smaller  <=> larger^2 > (S^2/4) smaller^2 (all positive)
        if X2>=Y2 and X2>S2/4*Y2 and V>0:
            assert last!='a';A=(V*Bb-A if (p,q)==(1,5) else Fr(V,5)*Bb-A);last='a'
        elif Y2>X2 and Y2>S2/4*X2 and V>0:
            assert last!='b';Bb=(Fr(V,5)*A-Bb if (p,q)==(1,5) else V*A-Bb);last='b'
        else:break
        moves+=1
        assert A>0 and Bb>0 and p*A*A+q*Bb*Bb+h==V*A*Bb
        # denominators: each divides 5^ceil(i/2), product divides 5^i
        for z in (A,Bb):
            t=z.denominator
            while t%5==0:t//=5
            assert t==1 and z.denominator<=5**((moves+1)//2)
        assert (A.denominator*Bb.denominator)<=5**moves and (5**moves)%(A.denominator*Bb.denominator)==0
        log.append((A,Bb))
    assert moves<400
    # stopped pair: h >= (V/2 - sqrt5) A B   <=>  5 (AB)^2 >= (V/2 AB - h)^2  when V/2 AB > h
    t=Fr(V,2)*A*Bb-h
    assert t<=0 or 5*(A*Bb)**2>=t*t
    return moves

def brute(F,mode='all'):
    """all Q tuples a<=b with 4abd=Fe+1, a+b=ce, unit conditions skipped (any F), and pa+qb=0 mod F"""
    out=[]
    for a in range(1,(F+1)//2+1):
        for d in range(1,(F+1)//(2*a)+1):
            s=4*a*d;G=4*a*a*d+1
            # f=s*c-F in [1,F+2]
            c0=F//s+1
            for c in range(c0,(2*F+2)//s+1):
                f=s*c-F
                if f<=0 or G%f:continue
                e=G//f;b=c*e-a
                if b<a:continue
                assert 4*a*b*d==F*e+1
                for p,q in ((1,5),(5,1)):
                    if (p*a+q*b)%F==0:out.append((p,q,a,b,c,d,e))
    return out

def lemma(Fmax):
    worst=Fr(0);n=0;maxmoves=0
    for F in range(3,Fmax+1):
        if gcd(F,10)!=1:continue
        D=cutoff(F)
        for p,q,a,b,c,d,e in brute(F):
            n+=1;H=(p*a+q*b)//F;h=c*H
            assert d<=D,(F,p,q,a,b,c,d,e,D)
            worst=max(worst,Fr(d,D));maxmoves=max(maxmoves,walk_check(p,q,a,b,h,d))
    print('lemma Fmax',Fmax,'hits',n,'max d/D',worst,float(worst),'max walk moves',maxmoves,flush=True)

def search(r,k,Dover=None):
    F=r**k;D=cutoff(F) if Dover is None else Dover;hits=[];pairs=0
    # square roots of a unit u mod r^k without Hensel: t^2=u mod r (search), w=u/t^2 lies in 1+rZ, whose
    # group has odd order r^(k-1), so sqrt(w)=w^((r^(k-1)+1)/2).  Both roots are +-t*sqrt(w).
    ex=(r**(k-1)+1)//2
    sq={}
    for t in range(1,r):sq.setdefault(t*t%r,t)
    def sqrt_mod(u,F,all_roots=True):
        t=sq.get(u%r)
        if t is None:return []
        w=u*pow(t*t,-1,F)%F;x=t*pow(w,ex,F)%F
        assert x*x%F==u%F
        return sorted({x,F-x})
    for p,q in ((1,5),(5,1)):
        for d in range(1,D+1):
            if d%r==0:continue
            # 4 p d a^2 == -q  (mod F)  <=>  a^2 == -q * (4pd)^{-1}
            rhs=(-q*pow(4*p*d,-1,F))%F
            roots=sqrt_mod(rhs,F,all_roots=True) or []
            for a in roots:
                if a==0 or 2*a*d>F+1:continue
                pairs+=1;s=4*a*d;G=4*a*a*d+1
                cands=[]
                # branch 1: f<s, f == -F (mod s)
                f=(-F)%s
                if f and G%f==0:cands.append(f)
                # branch 2: e<s, e*f=G, f == -F (mod s)  => e == -(F^{-1}) (mod s) since G == 1 (mod s)
                e=(-pow(F,-1,s))%s
                if e and G%e==0:cands.append(G//e)
                for f in set(cands):
                    if (f+F)%s:continue
                    c=(f+F)//s;e=G//f;b=c*e-a
                    if b<a or 4*a*b*d!=F*e+1 or (a+b)%e:continue
                    if any(z%r==0 for z in (a,b,c,d,e)):continue
                    if (p*a+q*b)%F:continue
                    hits.append((p,q,a,b,c,d,e))
    return D,pairs,hits

if __name__=='__main__':
    mode=sys.argv[1]
    if mode=='lemma':lemma(int(sys.argv[2]))
    elif mode in('search','cut'):
        r,kmax=int(sys.argv[2]),int(sys.argv[3])
        for k in range(1,kmax+1,2):
            if mode=='cut':print(r,k,cutoff(r**k),flush=True);continue
            D,pairs,h=search(r,k);print(r,k,D,pairs,len(h),h[:3],flush=True)
    elif mode=='lemma2':
        # primes F=r in [lo,hi), step: complete Q search with the trivial cutoff d<=(F+1)/2, then test the walk bound
        import random
        lo,hi,cnt=map(int,sys.argv[2:5]);random.seed(1);n=0;worst=Fr(0);used=0
        from sympy import isprime
        ps=[x for x in range(lo,hi) if isprime(x)];random.shuffle(ps)
        for r in ps[:cnt]:
            D,pairs,h=search(r,1,(r+1)//2);Dw=cutoff(r);used+=Dw<(r+1)//2
            for p,q,a,b,c,d,e in h:
                n+=1;H=(p*a+q*b)//r;assert d<=Dw,(r,p,q,a,b,c,d,e,Dw);worst=max(worst,Fr(d,Dw));walk_check(p,q,a,b,c*H,d)
        print('lemma2',lo,hi,cnt,'primes with nontrivial walk cutoff',used,'hits',n,'max d/D',float(worst),flush=True)
    elif mode=='markov':
        # stress test of the dichotomy on arbitrary positive integer solutions of p a^2+q b^2+h=(4dh-6)ab
        # (no Q-hit structure needed: the lemma only uses this equation and a=min side), incl. far points
        dmax,hmax,amax=map(int,sys.argv[2:5]);pts=set()
        for p,q in ((1,5),(5,1)):
            for d in range(1,dmax+1):
                for h in range(1,hmax+1):
                    V=4*d*h-6
                    if V<=0:continue
                    for a in range(1,amax+1):
                        D=V*V*a*a-4*q*(p*a*a+h)
                        if D<0:continue
                        t=isqrt(D)
                        if t*t!=D:continue
                        for b2 in (V*a-t,V*a+t):
                            if b2>0 and b2%(2*q)==0:
                                b=b2//(2*q);assert p*a*a+q*b*b+h==V*a*b;pts.add((p,q,a,b,h,d))
        base=len(pts)
        # climb: alternately reflect the SMALLER weighted coordinate upward (rational), keep integral points
        for (p,q,a,b,h,d) in list(pts):
            V=4*d*h-6;A,Bb=Fr(a),Fr(b)
            for step in range(14):
                if p*A*A<=q*Bb*Bb: A=(V*Bb-A if (p,q)==(1,5) else Fr(V,5)*Bb-A)
                else: Bb=(Fr(V,5)*A-Bb if (p,q)==(1,5) else V*A-Bb)
                if A.denominator==1 and Bb.denominator==1 and A>0 and Bb>0:pts.add((p,q,int(A),int(Bb),h,d))
        n=0;longest=0
        for (p,q,a,b,h,d) in pts:
            if a>b:continue          # orientation: a is the smaller side
            V=4*d*h-6;mv=walk_check(p,q,a,b,h,d);longest=max(longest,mv);n+=1
            for m in range(1,20):
                if mv<=m: assert 2*d<=5**m+6,(p,q,a,b,h,d,m,mv)
                else:     assert Fr(V*V,20)**m < 5*a*a*25**((m+1)//2),(p,q,a,b,h,d,m,mv)
        print('markov',dmax,hmax,amax,'base solutions',base,'tested points',n,'longest walk',longest,flush=True)
    elif mode=='vs':
        r,kmax=int(sys.argv[2]),int(sys.argv[3])
        for k in range(1,kmax+1,2):
            F=r**k;b=sorted(t for t in brute(F) if all(z%r for z in t[2:]))
            D,pairs,h=search(r,k);h=sorted(h)
            print('vs',r,k,'brute',len(b),'search',len(h),'same' if b==h else 'DIFF',flush=True)
