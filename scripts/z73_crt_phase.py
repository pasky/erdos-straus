"""Replay composite-shift tests, in integer phase units. uv run python scripts/z73_crt_phase.py"""
from itertools import product, combinations
from math import prod, lcm, gcd
from sympy import primitive_root, isprime, divisors


def chars(primes, gens):
    # Product of cyclic character groups: evaluate only characters odd on -1.
    ms = [p-1 for p in primes]
    L = lcm(*ms)
    logs = [{pow(int(primitive_root(p)),j,p):j for j in range(m)} for p,m in zip(primes,ms)]
    for J in product(*map(range,ms)):
        if sum(J)%2:
            angles = [sum(j*(L//m)*d[q%p] for j,m,d,p in zip(J,ms,logs,primes))%L for q in gens]
            yield tuple(min(a,L-a) for a in angles), L


def reaches(mod, gens, v):
    return any(prod(pow(q,i,mod) for q,i in zip(gens,I))%mod==mod-1
               for I in product(*(range(-w,w+1) for w in v)))


def check_example():
    for p,primes,qs in [(1201,(3,13),(5,31)),(3117161329,(5,11,13),(2729,285559))]:
        c=prod(primes); K=(p+c)//4
        assert isprime(p) and all(isprime(q) for q in qs) and K%prod(qs)==0
        v=(1,1)
        S,L=min((sum((w+1)*e for w,e in zip(v,a)),L) for a,L in chars(primes,qs))
        print('p, c, T:', p,c,f'{S}/{L}', 'hit',reaches(c,qs,v))
        if c==715:
            assert K==prod(qs) and gcd(p*K,c)==1
            assert all(reaches(prod(sub),qs,v) for sub in combinations(primes,2))
            # Direct denominator factorization test (includes Type I as well as Type II).
            H=p*K
            assert all((H+d)%c for d in divisors(H**2))
            print('No triple at x=K, divisors tested:',len(divisors(H**2)))


def small_regression():
    cases=miss_at_boundary=0
    for primes in ((3,5),(3,13),(5,7),(3,5,7)):
        c=prod(primes); units=[q for q in range(1,c) if gcd(c,q)==1]
        for q,r in combinations(units,2):
            table=list(chars(primes,(q,r))); L=table[0][1]
            for v,w in product(range(1,4),repeat=2):
                S=min((v+1)*a+(w+1)*b for (a,b),_ in table)
                ok=reaches(c,(q,r),(v,w))
                # Rectangular kernel iff exact axis parity and correct quotient order.
                V,W=v+1,w+1
                rect=(pow(q,V,c)==pow(r,W,c)==c-1 and len({sgn*pow(q,i,c)*pow(r,j,c)%c
                    for i in range(V) for j in range(W) for sgn in (-1,1)})==2*V*W)
                assert (S!=L or (not ok)==rect) and (S<=L or ok)
                cases+=1; miss_at_boundary+=S==L and not ok
    print('composite regression:',cases,'cases,',miss_at_boundary,'endpoint misses')


if __name__=='__main__':
    check_example(); small_regression()
