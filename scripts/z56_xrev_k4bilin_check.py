"""Independent bounded-memory arithmetic checks for REVIEW_K4BILIN.md.

Run under an external timeout and virtual-memory limit using uv run python.
The lane's segmented sieve and factorization code are deliberately not reused.
"""

from math import prod, exp, log
from fractions import Fraction

# Independent trial division; no arrays growing with the main x.
primes = []
for p in range(2, 31624):
    if all(p % q for q in primes if q*q <= p):
        primes.append(p)

def factor(n):
    out = {}
    for p in primes:
        if p*p > n:
            break
        while n % p == 0:
            out[p] = out.get(p, 0) + 1
            n //= p
    if n > 1:
        out[n] = out.get(n, 0) + 1
    return out

def weights(n):
    ff = factor(n)
    r = 4 * prod(e+1 for p,e in ff.items() if p % 4 == 1)
    if any(p % 4 == 3 and e % 2 for p,e in ff.items()):
        r = 0
    star = 0 if any(p % 4 == 3 for p in ff) else 4 * 2**sum(p % 4 == 1 for p in ff)
    return r, star

s = dict(a=0, positive=0, pairs=0, prime_pairs=0, mu_a=0, lambda_a=0, star=0, mu_star=0, prime_a=0, prime_star=0)
for n in range(97, 1000001, 120):
    f = factor(n)
    omega = sum(f.values())
    mu = 0 if any(e>1 for e in f.values()) else (-1)**omega
    r1, t1 = weights(n+4)
    r2, t2 = weights(4*n+1)
    a, star = r1*r2, t1*t2
    s['a'] += a
    s['positive'] += a>0
    s['pairs'] += star>0
    s['prime_pairs'] += star>0 and omega==1
    s['mu_a'] += mu*a
    s['lambda_a'] += (-1)**omega*a
    s['star'] += star
    s['mu_star'] += mu*star
    s['prime_a'] += a*(omega==1)
    s['prime_star'] += star*(omega==1)
print('Independent 1e6 census:', s)
expected = dict(a=352832, positive=2254, pairs=2037, prime_pairs=535, mu_a=-3904, lambda_a=-4800, star=313920, mu_star=-576, prime_a=95296, prime_star=82688)
assert s == expected
for p in (7,11,13,17,19,23,29,31):
    chi = 1 if p%4==1 else -1
    roots = {-4%p, -pow(4,-1,p)%p}
    w = [(1+chi if c in roots else 1) for c in range(p)]
    assert Fraction(w[0],sum(w)) == Fraction(1,p+2*chi)
    delta = [Fraction(p*v,sum(w)) for v in w]
    l1 = sum(abs(v-1) for v in delta)/p
    print('local', p, 'g=', Fraction(w[0],sum(w)), 'mean |delta-1|=',l1,'exceeds 3/p:', l1>Fraction(3,p))
print('f(2.1)=',2*exp(0.5772156649015329)*log(1.1)/2.1)
print('budget gap=',Fraction(3,4)-Fraction(66,107))
assert weights(101)[1] > 0 and weights(389)[1] > 0
print('Prop P roughness counterexample: n=97, x=98**13=',98**13,'so x**(1/13)=98>97')
M,N = 3000,83333
pairs=0
mass=0.0
for m in range(M+1,2*M+1):
    if m%840 != 1:
        continue
    for n in range(N+1,2*N+1):
        if n%840 != 577:
            continue
        t=m*n
        assert t<=10**9 and (t+4)%7==0 and t%120==97
        pairs+=1
        mass+=prod((p-1)/(p-1+2*(1 if p%4==1 else -1)) for p in factor(t))
print('Lemma N box: pairs=',pairs,'a* mass=0, model mass=',mass)
assert pairs==396
