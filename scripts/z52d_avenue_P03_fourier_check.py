# Z3003: check r(-1) = phi(e)^-1 * sum_chi chi(-1) prod_s (1 + 2 Re chi(s)) for prime e (cyclic group)
import itertools, cmath, random
from sympy import primerange, primitive_root, discrete_log, factorint
random.seed(2)
bad=0
for trial in range(300):
    e = random.choice(list(primerange(7, 200)))
    primes = random.sample([q for q in primerange(3, 400) if q % e], random.randint(2, 6))
    g = primitive_root(e); n = e-1
    # direct count
    r = sum(1 for d in itertools.product((-1,0,1), repeat=len(primes))
            if (lambda v: v % e)(eval('*'.join(f'pow({s},{k},{e})' if k>=0 else f'pow({s},-1,{e})' for s,k in zip(primes,d)) or '1')) == e-1)
    logs = [discrete_log(e, s % e, g) for s in primes]
    tot = 0
    for j in range(n):  # chi_j(g^a) = exp(2 pi i j a / n)
        chim1 = cmath.exp(2j*cmath.pi*j*(n//2)/n)
        prod = 1
        for a in logs: prod *= 1 + 2*cmath.cos(2*cmath.pi*j*a/n)
        tot += chim1*prod
    if abs(tot/n - r) > 1e-6: bad += 1
print('mismatches', bad, 'of 300')
