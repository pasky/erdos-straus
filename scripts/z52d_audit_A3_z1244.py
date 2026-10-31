"""z52d audit A3, item Z1244: 'LLM proposes encodings, algebraic gate = written map + toy check'.
Gate applied to five encodings of the residual factor equation 4uBC - u - B = p (FRONTIER §2.1):
 E1 triples (u,B,C); E2 pair form; E3 divisor form; E4 trial form; E5 SL2 form.  Check equal counts p<=3000."""
from math import gcd, isqrt
from sympy import primerange, divisors

def E1(p):
    n = 0
    for C in range(1, p + 1):
        for u in range(1, p + 1):
            # 4uBC - u - B = p  ->  B(4uC-1) = p+u
            m = 4 * u * C - 1
            if m > p + u: break
            if (p + u) % m == 0: n += 1
        if 4 * C - 1 > p + 1: break
    return n

def E2(p):
    n = 0
    for u in range(1, p + 1):
        if 4 * u - 1 > p + u + 1: break
        for B in range(1, p + 1):
            q = 4 * u * B
            if q > p + u + B: break
            if gcd(u, B) == 1 and (p + u + B) % q == 0: n += 1
    return n

def E3(p):  # divisor form; E4 (trial form) is E1's inner loop: 1[(4uC-1) | p+u]
    n = 0
    C = 1
    while (4 * C - 1) ** 2 <= 4 * C * p + 1:
        N = 4 * C * p + 1
        n += sum(1 for d in divisors(N) if d % (4 * C) == 4 * C - 1)
        C += 1
    return n

def E5(p):  # [[a,p],[c,d]] in SL2(Z), c=4C>0, a,d>=1, a=d=-1 mod c ; ad = pc+1
    n = 0
    c = 4
    while (c - 1) ** 2 <= p * c + 1:
        N = p * c + 1
        for a in divisors(N):
            d = N // a
            if a % c == c - 1 and d % c == c - 1: n += 1
        c += 4
    return n

bad = 0
for p in primerange(5, 3000):
    if p % 4 != 1: continue
    r = (E1(p), E2(p), E3(p), E5(p))
    if len(set(r)) != 1:
        bad += 1; print("MISMATCH", p, r)
print("primes p=1 mod 4 < 3000 checked; mismatches:", bad)
print("examples", {p: (E1(p), E2(p), E3(p), E5(p)) for p in (409, 577, 3361)})
