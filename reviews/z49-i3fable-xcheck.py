"""Independent bounded checks for z49-i3fable-xreview; Python standard library only."""
from math import gcd, isqrt, lcm, log
from pathlib import Path
import array

SOURCE = Path('/home/pasky/projects/math/erdos-straus-claude-agent-worktree-0044')

def divisors(n):
    out = []
    for d in range(1, isqrt(n) + 1):
        if n % d == 0:
            out.append(d)
            if d*d != n:
                out.append(n//d)
    return out

def words(n):
    """All unordered positive words, independently via divisors of n+u."""
    out = []
    for u in range(1, isqrt(n+1)+2):
        for v in divisors(n+u):
            if v >= u and (n+u+v) % (u*v) == 0:
                out.append(((n+u+v)//(u*v), u, v))
    return out

def interior(n):
    return [(t,u,v) for t,u,v in words(n) if min(t,u,v) >= 3]

def isprime(n):
    return n >= 2 and all(n%d for d in range(2,isqrt(n)+1))

def pow2(n):
    return n >= 2 and n & (n-1) == 0

def jacobi(a,n):
    assert n > 0 and n%2
    a %= n; sign=1
    while a:
        while a%2 == 0:
            a//=2
            if n%8 in (3,5): sign=-sign
        a,n=n,a
        if a%4 == n%4 == 3: sign=-sign
        a%=n
    return sign if n == 1 else 0

def square_allowed(t,u,odd):
    t %= 8; u %= 8
    return ((t in (1,5) and (u%4 == 2 or (odd and u == 3)))
            or (t == 3 and odd and u%4 == 1)
            or (t in (2,6) and u%4 in (1,2)))

seen = [set(),set()]
seen2 = [set(),set()]
for m in range(1,241):
    for t,u,v in words(m*m):
        for x in (u,v):
            assert square_allowed(t,x,m%2), (m,t,u,v)
            seen[m%2].add((t%8,x%8))
    for t,u,v in words(2*m*m):
        for x in (u,v):
            allowed = (t%2 and x%8 in (2,4)) or (t%8 in (2,4) and x%2)
            assert allowed, (m,t,u,v)
            seen2[m%2].add((t%8,x%8))
for parity in (0,1):
    allowed = {(t,u) for t in range(8) for u in range(8) if square_allowed(t,u,parity)}
    assert seen[parity] == allowed
print('Square cells through m=240:', list(map(len,seen)), '; 2m²:', list(map(len,seen2)))
for u in range(3,9):
    for v in range(u,9):
        assert all(((2*r)**2+u+v) % (u*v) for r in range(u*v))
print('Cor 2.1b: all 21 endpoint pairs disjoint from even squares modulo uv')

for n in range(3,1001):
    ws = words(n)
    i3 = any(min(t,u,v)>=3 for t,u,v in ws)
    w2 = any(min(t,u,v)>=2 for t,u,v in ws)
    mp = any(min(u,v)>=3 for t,u,v in ws)
    assert (not w2) == (not i3 and isprime(2*n+1) and (pow2(n+2) or isprime(n+2)))
    q = 2*n+1
    assert (not mp) == (not i3 and isprime(n+1) and (isprime(q) or (q%3==0 and isprime(q//3)) or q in (9,27)))
    for t,u,v in ws:
        for u,v in {(u,v),(v,u)}:
            A=t*u-1
            if n%4 == 1 and A%2:
                assert jacobi(A,n) == jacobi(-t,A)
            if A%2 and t>=3 and jacobi(-t,A) == 1:
                assert t%4 != 0 and t%4 != 3
            if (v+1)%u == 0:
                tt,vv = (v+1)//u, t*u-1
                assert tt*u*vv-u-vv == n
                assert (vv+1)//u == t and tt*u-1 == v
print('Prop 4.3, Lemmas 5.3/5.4/7.1: all n=3..1000 passed')
for k in (1,2,3,5,6,7,10,14,15):
    for m in range(1,31):
        for t,u,v in words(k*m*m):
            A=t*u-1; g=gcd(k,t); t1=t//g; k1=k//g
            assert ((g*t1*k1*m)**2+t1*k1)%A == 0
            if k1 == 1:
                assert square_allowed(t1,g*u,(g*m)%2)
print('Lemma 2.0 / Thm 2.2 norm identity and case (a): k=1,2,3,5,6,7,10,14,15; m<=30 passed')

families = [
 (1,-1,6,[(3,3),(3,5),(3,6),(4,5),(3,9),(4,13),(3,18),(26,37)]),
 (1,1,6,[(3,3),(3,4),(3,6),(3,9),(3,18),(9,21)]),
 (1,3,6,[(3,5),(4,5),(3,7),(5,6),(4,9),(4,13)]),
 (1,-3,5,[(3,4),(3,8)]),
 (7,-1,8,[(3,3),(3,6),(4,5),(3,11),(5,10),(4,13),(5,12),(8,9),(5,15),(5,20),(8,65),(15,65)]),
 # Review-discovered counterexamples to the scope suggested by Thm 5.5(c).
 (3,1,5,[(3,14),(7,8),(3,5),(5,6),(5,27),(6,17),(9,38),(5,5),(4,11),(5,10),(5,15),(5,195)]),
 (5,-1,6,[(5,6),(3,3),(3,6),(6,15)])]
for c,d,start,pairs in families:
    cert = []
    for u,v in pairs:
        w = u*v; a = 0
        while w%2 == 0:
            w //= 2; a += 1
        # Reduce c*2^k = -s mod w by gcd(c,w); don't discard nonunit c.
        reduced = w//gcd(c,w)
        period=1
        while pow(2,period,reduced) != 1:
            period += 1
        residues = [r for r in range(period) if (c*pow(2,r,w)+d+u+v)%w == 0]
        assert (d+u+v)%(2**a) == 0 and len(residues) == 1
        cert.append((u,v,a,period,residues[0]))
    L = lcm(*(q[3] for q in cert))
    assert start >= max(q[2] for q in cert)
    # Proves every exponent: divisibility repeats with L, t increases with k.
    for k in range(start,start+L):
        assert any((c*2**k+d+u+v)%(u*v) == 0 and (c*2**k+d+u+v)//(u*v)>=3 for u,v in pairs)
    exceptions = [k for k in range(1,start) if not any((c*2**k+d+u+v)%(u*v)==0 and (c*2**k+d+u+v)//(u*v)>=3 for u,v in pairs)]
    print(f'Cover {c}*2^k{d:+}: period={L}, threshold={start}, listed-pair exceptions={exceptions}')
    print('  (u,v,2-adic threshold,period,residue):', cert)
print('All five claimed coverings and two review-discovered coverings proved by a complete period plus monotonicity')

# Exact truncated Haar integrals: sum ell^a 1[ell^a | n+u], restricted to a<J.
for p,J in ((2,6),(3,4),(5,3)):
    mod=p**J
    for n in (0,1,p,p+1):
        total=0
        for t in range(mod):
            for u in range(mod):
                z=(t*u-1)%mod
                if z == 0:
                    continue
                a=0
                while z%p == 0:
                    z//=p; a+=1
                if (n+u)%(p**a) == 0:
                    total+=p**a
        value=total/(mod*mod)
        exact=1-(p-1)/p**2 if n%p == 0 else 1+1/p**2-p**(-J)
        assert abs(value-exact)<1e-12
print('Prop 2.3: exact finite Haar sums at primes 2,3,5 passed (analytic tail p^-J)')

# Independent compare to the C engine after bounded small run, if present.
prefix = Path('/tmp/z49-i3-xcount_i3.u16')
if prefix.exists():
    ar=array.array('H'); ar.frombytes(prefix.read_bytes())
    targets=list(range(3,1001))+[1225,19600,36078,2433600,193,409,577,2521,3361,5569,9601,66529]
    for n in targets:
        count=sum(1 if u==v else 2 for t,u,v in interior(n))
        assert count == ar[n], (n,count,ar[n])
    print('Independent word enumerator agrees with C engine at',len(targets),'targets, including 1560²')
print('DONE')
