"""NL7: primality certificates (finding 8 of the hostile review).
SymPy's isprime is deterministic below 2^64 and a BPSW probable-prime test above.  Here every prime that enters a
headline numerical claim and exceeds 2^64 is PROVED prime by a recursive Lucas (n-1) / Pratt certificate:
n is prime if for some a: a^(n-1) = 1 (mod n) and a^((n-1)/q) != 1 (mod n) for every prime q | n-1 (q proved
recursively; q < 2^64 accepted from the deterministic range of isprime).
Covered: (1) the SG primes of sg_examples (16 s^4 + 1, s < 2e5, s = ±18 mod 126, 5 | s);
(2) the quartic primes p = (840 j)^4 + 1, j < 250, and for the listed rule failures every prime factor of p + L and
    of L p + 1 that was obtained by factorisation (L p + 1 < 10^23), for all candidate letters L;
(3) the three R-G failures on p = t^2 + 16: every prime factor of p + L and L p + 1 for all candidate letters.
"""
import sys
sys.path.insert(0, 'scripts')
from sympy import factorint, isprime, divisors
from z69_nl7_polyrule import RULES
from z69_nl7_quartic import RULES4

B64 = 1 << 64
proved = {}
def prove(n):
    if n < B64:
        return isprime(n)
    if n in proved:
        return proved[n]
    if not isprime(n):
        proved[n] = False
        return False
    qs = list(factorint(n - 1).keys())
    assert all(prove(q) for q in qs), n
    ok = False
    for a in range(2, 200):
        if pow(a, n - 1, n) != 1:
            ok = False; break
        if all(pow(a, (n - 1) // q, n) != 1 for q in qs):
            ok = True; break
    proved[n] = ok
    return ok

big = 0
def check_factors(N):
    global big
    for q in factorint(N):
        if q >= B64:
            big += 1
        assert prove(q), (N, q)

# (1) SG primes
cnt = 0
for s in range(1, 200000):
    if s % 126 in (18, 108) and s % 5 == 0:
        n = 16 * s**4 + 1
        if isprime(n):
            assert prove(n); cnt += 1
print(f"(1) SG primes with 5 | s, s < 2e5: {cnt} proved prime (Pratt certificates above 2^64)")

# (2) quartic
qp = [(840 * j) for j in range(1, 250) if isprime((840 * j)**4 + 1)]
assert all(prove(t**4 + 1) for t in qp)
print(f"(2) quartic primes (840 j)^4 + 1, j < 250: {len(qp)} proved prime")
for rule, fn in (('J', 'data/z69/nl7/quartic_J_840.txt'), ('c', 'data/z69/nl7/quartic_c_840.txt')):
    nf = 0
    for line in open(fn):
        if not line.startswith('FAIL'): continue
        t = int(line.split()[1]); p = t**4 + 1
        if t >= 840 * 250: continue
        assert prove(p)
        letters = set()
        for e in RULES4[rule](t):
            letters |= {d for d in divisors(e) if d <= p + 2}
        for L in sorted(letters):
            check_factors(p + L)
            if L * p + 1 < 10**23:
                check_factors(L * p + 1)
        nf += 1
    print(f"    rule {rule}: {nf} failures (j < 250): all prime factors of p + L and (when factored) L p + 1 proved prime")

# (3) R-G failures on t^2 + 16
for line in open('data/z69/nl7/hsearch_fixb4_G_c15_a.txt'):
    if not line.startswith('FAIL'): continue
    t = int(line.split()[1]); p = t * t + 16
    assert prove(p)
    letters = set()
    for e in RULES['G'](t, 4):
        if e > 0: letters |= set(divisors(e))
    for L in sorted(letters):
        check_factors(p + L); check_factors(L * p + 1)
print(f"(3) the three R-G failures on t^2+16: p and all prime factors of p + L, L p + 1 proved prime")
print(f"prime factors above 2^64 certified: {big}; distinct numbers with a Pratt certificate: {sum(1 for v in proved.values() if v)}")
