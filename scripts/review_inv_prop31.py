"""R158 from-scratch check of INVOLUTION_ES Prop 3.1 (T1 for divisor-type counts).

Part A (free model): residues are powers a^r, a of infinite order. For a pattern (classes c_i, exponents e_i),
with q_j >> prod_{i<j} q_i^{2e_i}, the comparison d < m^2/d is decided at the largest index where f_i != e_i.
Expand D(m^2) - c over GF(2) in variables phi_r = phi(a^r, a^{2-r}) and psi = psi(a); sum the 4 patterns.
Also: GF(2) span search over many patterns, with classes restricted to a given exponent set, to test
whether the vector phi_0 is reachable (claim: not with classes {0,1}, yes with {-1,0,1,2}).

Part B (actual integers): choose real primes in the classes with the size condition, random phi/psi/c tables
mod M, compute D(m^2) directly (pairs u<v over all divisors) and check sum_i D(m_i^2) = phi(1,h) mod 2.
"""
import itertools, random, sys
from collections import Counter
from sympy import isprime, divisors


def expand(pattern):
    cls = [c for c, e in pattern]; ex = [e for c, e in pattern]
    assert sum(c * e for c, e in pattern) == 1, "m must be = a"
    cnt = Counter()
    for f in itertools.product(*[range(2 * e + 1) for e in ex]):
        diff = [i for i in range(len(ex)) if f[i] != ex[i]]
        if not diff:
            cnt["psi"] += 1
            continue
        j = max(diff)
        if f[j] < ex[j]:
            cnt["phi%d" % sum(c * fi for c, fi in zip(cls, f))] += 1
    return frozenset(k for k, v in cnt.items() if v % 2)


PATTERNS = {
    "P1": [(-1, 2), (1, 3)],
    "P2": [(-1, 1), (2, 1)],
    "P3": [(0, 1), (1, 1)],
    "P4": [(-1, 2), (1, 1), (2, 1)],
}


def partA():
    tot = frozenset()
    for k, p in PATTERNS.items():
        e = expand(p)
        print(k, sorted(e))
        tot = tot ^ e
    print("sum of 4 expansions:", sorted(tot), "(+4c = 0)")


def span_search(classes, maxexp, maxlen):
    vecs = []
    for L in range(1, maxlen + 1):
        for cl in itertools.product(classes, repeat=L):
            for ex in itertools.product(range(1, maxexp + 1), repeat=L):
                if sum(c * e for c, e in zip(cl, ex)) != 1:
                    continue
                v = set(expand(list(zip(cl, ex))))
                v ^= {"c"}  # each pattern carries one c
                vecs.append(frozenset(v))
    # GF(2) elimination with dict basis
    keys = sorted(set().union(*vecs) | {"phi0"})
    idx = {k: i for i, k in enumerate(keys)}
    basis = {}
    def reduce(x):
        while x:
            h = x.bit_length() - 1
            if h in basis:
                x ^= basis[h]
            else:
                return x
        return 0
    for v in vecs:
        x = sum(1 << idx[k] for k in v)
        r = reduce(x)
        if r:
            basis[r.bit_length() - 1] = r
    target = 1 << idx["phi0"]
    return len(vecs), reduce(target) == 0


def next_prime_in_class(lo, r, M):
    x = lo + 1
    while True:
        if x % M == r % M and isprime(x) and x % 2:
            return x
        x += 1


def D(n, M, phi, psi, c):
    s = c[n % M]
    for u in divisors(n):
        v = n // u
        if u < v:
            s ^= phi[(u % M, v % M)]
        elif u == v:
            s ^= psi[u % M]
    return s


def partB(M, a, trials=5):
    units = [x for x in range(M) if __import__('math').gcd(x, M) == 1] if M > 1 else [0]
    ainv = pow(a, -1, M) if M > 1 else 0
    h = a * a % M if M > 1 else 0
    cls = {-1: ainv, 0: 1 % M, 1: a % M, 2: a * a % M}
    ms = []
    for k, p in PATTERNS.items():
        qs, prodsq = [], 1
        for c, e in p:
            q = next_prime_in_class(max(prodsq, 2 * M + 2), cls[c], M)
            qs.append(q); prodsq *= q ** (2 * e)
        m = 1
        for q, (c, e) in zip(qs, p):
            m *= q ** e
        assert m % M == a % M if M > 1 else True
        ms.append(m)
    ok = True
    for _ in range(trials):
        phi = {(x, y): random.randint(0, 1) for x in range(M) for y in range(M)}
        psi = {x: random.randint(0, 1) for x in range(M)}
        c = {x: random.randint(0, 1) for x in range(M)}
        s = 0
        for m in ms:
            s ^= D(m * m, M, phi, psi, c)
        ok &= (s == phi[(1 % M, h)])
    print("actual integers M=%d a=%d: m's =" % (M, a), [len(str(m)) for m in ms], "digits; identity", ok)


if __name__ == "__main__":
    partA()
    for cl in ([0, 1], [-1, 0, 1], [0, 1, 2], [-1, 0, 1, 2]):
        print("span search classes", cl, "(exp<=3, len<=3): vectors=%d, phi0 reachable=%s" % span_search(cl, 3, 3))
    for M, a in [(24, 5), (120, 7), (7, 3), (40, 3)]:
        partB(M, a)
