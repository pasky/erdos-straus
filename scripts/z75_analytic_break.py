"""Replay local inputs of ANALYTIC_BREAK.md; exact stdlib arithmetic, no GRH tests."""
from collections import Counter, deque
from fractions import Fraction
from math import gcd, isqrt, prod
from pathlib import Path


def sieve(n):
    a = bytearray(b'\x01')*(n+1)
    a[:2] = b'\x00\x00'
    for s in range(2, isqrt(n)+1):
        if a[s]:
            a[s*s::s] = bytes((n-s*s)//s+1)
    return a


prime = sieve(2000000)
primes = [i for i in range(len(prime)) if prime[i]]


def factor(n):
    f = Counter()
    for s in primes:
        if s*s > n:
            break
        while n % s == 0:
            f[s] += 1
            n //= s
    if n > 1:
        f[n] += 1
    return f


def nr(t, q):
    return pow(t, (q-1)//2, q) == q-1


def half_order(s, q):
    j = (q-1)//2
    for v in factor(j):
        while j % v == 0 and pow(s, j//v, q) == q-1:
            j //= v
    assert pow(s, j, q) == q-1
    return j


def witness(p, q, s, j, extra, scale=1):
    K = (p+q)//4
    assert 4*K == p+q and nr(s, q) and j % 2
    assert factor(K)[s] % 2 == 1 and s % 2
    d = K*s**j*prod(v**(2*a) for v, a in extra.items())
    A, rem = divmod(K+d, q)
    assert rem == 0
    n, x, y, z = p*scale, K*scale, p*A*scale, Fraction(scale*p*K*A, d)
    assert Fraction(4, n) == Fraction(1, x) + Fraction(1, y) + 1/z
    r = isqrt(z.denominator)
    assert r*r == z.denominator and gcd(r, 2*n) == 1
    # Independently strip the reduced denominator root, do not factor huge numbers.
    cap = 0
    for t, b in factor(K).items():
        a = 0
        while r % t == 0:
            r //= t
            a += 1
        predicted = max(0, (int(t == s)*j + 2*extra.get(t, 0)-b)//2)
        assert a == predicted and (a == 0 or y % t == 0)
        cap = max(a, cap)
    assert r == 1
    return cap


def explicit():
    screen = Path(__file__).resolve().parents[1]/'data/z58/screens/gstar_zeros.txt'
    targets = sorted({p for p in primes if p <= 200000 and p % 8 == 1} |
                     {int(v) for v in screen.read_text().splitlines()
                      if v and v[0] != '#' and int(v) % 8 == 1})
    largest = (0, 0, 0)
    for p in targets:
        q = next(q for q in primes if q % 4 == 3 and nr(q, p))
        assert 3*q*q <= 4*p
        K = (p+q)//4
        s = next(s for s, b in factor(K).items() if s % 2 and b % 2 and nr(s,q))
        e = witness(p,q,s,half_order(s,q),{})
        assert 3*(4*e+3)**2 <= 4*p
        largest = max(largest,(e,q,p))
    print('Explicit bound, least window and exact rational: inputs, max (cap,q,p):',len(targets),largest)
    # Enumerate reduced forms independently of finding the least q.
    events = Counter()
    for p in targets:
        if p > 3000:
            break
        count = 0
        for a in range(1, isqrt(4*p//3)+1):
            for b in range(a//2+1):  # ±b symmetric
                c, rem = divmod(p+b*b,a)
                if rem or c<a or gcd(gcd(a,2*b),c)>1:
                    continue
                n = a if a%2 else c
                if not nr(n,p):
                    continue
                assert nr(a,p)
                assert any(q % 4 == 3 and nr(q,p) for q in factor(a))
                count += 1
                events[a%2] += 1
        assert count
    print('Reduced nonprincipal forms up to sign b: even a, odd a:', events[0],events[1])


def planted():
    stats = Counter()
    dead = None
    for p in primes:
        if p>30000:
            break
        if p%8!=1:
            continue
        s = next(s for s in primes if nr(s,p))
        if s%4 != 1:
            continue
        m=3*s
        if dead is None and p%840 in (1,121,169,289,361,529) and not nr(3,p):
            K=(p+m)//4
            if all(t%3==1 for t in factor(K)):
                dead=(p,s,m,K,dict(factor(K)))
        # Search just the planted progression; impose no (q/p) sign condition.
        mod=4*s*s
        base=next(b for b in range((4*s-p)%(s*s), mod,s*s) if b%4==3)
        q=next(q for q in range(base,len(prime),mod) if prime[q])
        e=witness(p,q,s,half_order(s,q),{})
        assert 4*e<=q-3
        stats[nr(q,p)]+=1
    assert min(stats.values())>0 and len(stats)==2 and dead
    print('Planted least non-residue 1 mod 4: windows with (q/p)=+1,-1:',stats[False],stats[True])
    print('Composite dead (p,s,m,K,factor(K)):',dead)


def correction():
    counts = Counter()
    example = None
    for S in ((3,5),(5,7),(3,11)):
        for q in primes:
            if q>600:
                break
            if q%4!=3 or q in S:
                continue
            # Independent constructive table: BFS gives positive-exponent vectors in H.
            reps={1:(0,0)}
            work=deque([1])
            while work:
                t=work.popleft()
                for i,v in enumerate(S):
                    u=t*v*v%q
                    if u not in reps:
                        a=list(reps[t]); a[i]+=1
                        reps[u]=tuple(a); work.append(u)
            j,rem=divmod((q-1)//2,len(reps))
            assert rem==0 and j%2
            for s in primes:
                if s>200:
                    break
                if s==2 or s in S or not nr(s,q):
                    continue
                K=s*prod(S)**2*(1 if q%8==3 else 2)
                p=4*K-q
                if not 0<p<len(prime) or not prime[p] or p%8!=1 or not nr(q,p):
                    continue
                a=reps[pow(-s,-j,q)]
                e=witness(p,q,s,j,dict(zip(S,a)))
                old=witness(p,q,s,half_order(s,q),{})
                counts['checked']+=1
                counts['proper']+=int(j>1)
                counts['proper_drop']+=int(j>1 and e<old)
                if j>1 and e<old and min(a)>0 and (example is None or old-e>example[0]):
                    example=(old-e,p,q,s,S,j,a,e,old)
    assert counts['proper_drop'] and example
    print('Index correction:',dict(counts))
    print('Proper-subgroup example (drop,p,q,s,S,j,a,new cap,one-prime cap):',example)


def radicals():
    hard = [p for p in primes if p<=300 and p%8==1]
    counts=Counter()
    for i,p in enumerate(hard):
        for t in hard[:i]:
            R=p*t
            q=next(q for q in primes if q%4==3 and nr(q,p)!=nr(q,t))
            s=next(s for s,b in factor((R+q)//4).items() if s%2 and b%2 and nr(s,q))
            for scale in (1,p,R):  # n=R, Rp, R²
                cap=witness(R,q,s,half_order(s,q),{},scale)
                counts[cap>0]+=1
    assert counts[True]>0
    print('Radical/radical scaling: integral, positive-cap reconstructions:',counts[False],counts[True])


if __name__=='__main__':
    explicit()
    radicals()
    planted()
    correction()
