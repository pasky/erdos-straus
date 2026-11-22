"""z81: direct positive fractions, origin-centred divisor boxes, and a cheap growth rule.
Stdlib only. Counts are per window, not per solution. No factor of n is
needed, except for the separate strictness check on composite controls.
"""
from collections import Counter
from functools import lru_cache
from math import gcd, isqrt
from pathlib import Path


@lru_cache(maxsize=4096)
def factors(n):
    a = []
    l = 2
    while l*l <= n:
        if n % l == 0:
            b = 0
            while n % l == 0:
                n //= l
                b += 1
            a.append((l, b))
        l = 3 if l == 2 else l + 2
    if n > 1:
        a.append((n, 1))
    return tuple(a)


def divisors2(fac):
    d = [1]
    for l, b in fac:
        d = [u*l**a for a in range(2*b+1) for u in d]
    return d


def window(n, m, x, full=False):
    k = m*x-n
    if gcd(n, x) != 1 or gcd(n,m) != 1:
        return set()
    out = set()
    for D in divisors2(factors(x)):
        for name, h, c in [('I', n*n*D, m*D+1), ('II', n*D, D+x)]:
            if c % k:
                continue
            s = n*x
            y, rem = divmod(s+h, k)
            z, rem2 = divmod(s+s*s//h, k)
            assert rem == rem2 == 0 and m*x*y*z == n*(x*y+y*z+z*x)
            assert ((gcd(n,y), gcd(n,z)) == ((n,1) if name == 'I' else (n,n)))
            out.add(name)
            if not full:
                return out
    return out


def direct(n, m):
    # Independent, unrestricted sorted test at the small controls.
    out = set()
    for x in range(n//m+1, 3*n//m+1):
        k, s = m*x-n, n*x
        for y in range(max(x, s//k+1), 2*s//k+1):
            z,r = divmod(s*y,k*y-s)
            if r == 0:
                assert z >= y
                common = [gcd(n,d) for d in (x,y,z)]
                out.add(('I' if common.count(n)==1 else 'II') if all(u in (1,n) for u in common) and common.count(n) in (1,2) else 'mixed')
    return sorted(out)


@lru_cache(maxsize=2048)
def prime(k):
    return k > 1 and factors(k) == ((k,1),)


def elementary_rule(n,m,x,k):
    # One-generator targeted order, not generating the whole divisor box:
    # if ord_k(l) is even with l^(ord/2)=-1 and ord/2 <= v_l(x), hit.
    # m-specific second shot: (mD+1)=0 with D=l^a, 0<=a<=2b.
    for l,b in factors(x):
        u = 1
        for a in range(2*b+1):
            if (m*u+1)%k == 0 or (a <= b and (u+1)%k == 0):
                return True
            u = u*l%k
    return False


def run_panel(n,m,cap):
    ans = {'I': None, 'II': None, 'single': None}
    for x in range(n//m+1, min(3*n//m,(n+cap)//m)+1):
        if gcd(x,n)>1:
            continue
        k = m*x-n
        for name in window(n,m,x,True):
            if ans[name] is None:
                ans[name] = k
        if ans['single'] is None and elementary_rule(n,m,x,k):
            ans['single'] = k
            assert ans['I'] is not None or ans['II'] is not None
        if all(a is not None for a in ans.values()):
            break
    return ans


def main():
    stars = [int(v) for v in Path('data/z58/screens/star_prime_zeros.txt').read_text().splitlines() if v and not v.startswith('#')]
    z7 = [105,1465,3865,4545,10305,12145,39361,67425]
    print('n m cap first-type-I first-type-II first-single; None = no hit to cap')
    for m, cases in [(4, [9,25,49,81,121,169,225]+z7+stars+[17401609,193,2521,3361,5101441,3153419441929]), (8,[11,17,131,241,1590284203561,6955940568721])]:
        for n in cases:
            cap = min(2*n,4095)
            a = run_panel(n,m,cap)
            print(n,m,cap,*a.values())
            if n <= 241:
                print('direct',n,m,direct(n,m))
    N=10**7
    sieve = bytearray(b'\1')*(N+1)
    sieve[:2] = b'\0\0'
    for q in range(2,isqrt(N)+1):
        if sieve[q]:
            sieve[q*q:N+1:q] = b'\0'*((N-q*q)//q+1)
    counts = Counter()
    misses=[]
    for a in (1,121,169,289,361,529):
        for n in range(a,N+1,840):
            if not sieve[n]: continue
            # Proposed before test: increasing lookahead in the bit length of p;
            # never build a divisor table in this search.
            cap = min(2*n,n.bit_length()**2)
            for k in range(3,cap+1,4):
                if elementary_rule(n,4,(n+k)//4,k):
                    counts['single']+=1
                    break
            else: misses.append(n)
            counts['total']+=1
    print('Mordell primes to 1e7',dict(counts),'misses',len(misses),sorted(misses)[:20])


if __name__ == '__main__':
    main()
