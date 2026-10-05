"""R57 from-scratch checks of POINTWISE_OMEGA15 Lemma 2.3 and the local bounds of Thm 3.1 / Def 1.0.

(A) Lemma 2.3 with actual primes: fibre H = {n = r mod Q}, primes p <= x in H, modulus q > x,
    gcd(q,Q)=1.  Checks (a) some unit class mod q has |count - N/phi(q)| >= 1/2;
    (b) max_{chi != chi0} |sum chi(p)|^2 >= N'(phi-N')/(phi-1) and the exact identity
    sum_chi |sum chi(p)|^2 = phi(q) N'; additive: max_{a!=0} |S(a) - N c_q(a)/phi(q)|^2 >= N(1-N/phi(q)).
    Characters are built for q prime or q = q1*q2 (q1,q2 distinct primes) from primitive roots.
(B) Local factor bounds: |mean of e(a x / b^v)| over units <= 1/(b-1) (a !=0 mod b^v);
    |sum_{x unit mod b^v} chi(x) e(a x/b^v)| / phi(b^v) vs the author's sqrt(b^v)/phi(b^v) and vs
    sqrt(b)/(b-1).
"""
import cmath, math, sys
from sympy import primerange, primitive_root, isprime, totient, factorint


def e(t):
    return cmath.exp(2j * math.pi * t)


def chars_prime(q):
    g = primitive_root(q); ind = {}
    x = 1
    for a in range(q - 1):
        ind[x] = a; x = x * g % q
    return [(lambda n, j=j: 0 if n % q == 0 else e(j * ind[n % q] / (q - 1))) for j in range(q - 1)]


def chars(q):
    f = factorint(q)
    ps = list(f)
    if len(ps) == 1 and f[ps[0]] == 1:
        return chars_prime(q)
    assert len(ps) == 2 and all(v == 1 for v in f.values())
    A, B = chars_prime(ps[0]), chars_prime(ps[1])
    return [(lambda n, a=a, b=b: a(n) * b(n)) for a in A for b in B]


def ramanujan(q, a):
    return sum(e(a * x / q) for x in range(1, q + 1) if math.gcd(x, q) == 1).real


def check_A(Q, r, x, q):
    assert math.gcd(q, Q) == 1 and q > x
    P = [p for p in primerange(2, x + 1) if p % Q == r % Q and math.gcd(p, Q) == 1]
    N = len(P); Np = sum(1 for p in P if q % p)
    ph = int(totient(q))
    if N == 0 or N > ph / 2:
        return None
    # (a)
    cnt = {}
    for p in P:
        if math.gcd(p, q) == 1:
            cnt[p % q] = cnt.get(p % q, 0) + 1
    erra = max(abs(c - N / ph) for c in cnt.values()) if cnt else 0
    assert Np == 0 or erra >= 0.5
    # (b) characters
    X = chars(q)
    vals = [sum(ch(p) for p in P) for ch in X]
    tot = sum(abs(v) ** 2 for v in vals)
    assert abs(tot - ph * Np) < 1e-6 * max(1, ph * Np), (tot, ph * Np)
    nontriv = [abs(v) ** 2 for v, ch in zip(vals, X) if any(abs(ch(n) - 1) > 1e-9 for n in range(1, q) if math.gcd(n, q) == 1)]
    mc = max(nontriv)
    lbc = Np * (ph - Np) / (ph - 1)
    assert mc >= lbc - 1e-9
    # additive
    ma = max(abs(sum(e(a * p / q) for p in P) - N * ramanujan(q, a) / ph) ** 2 for a in range(1, q))
    lba = N * (1 - N / ph)
    assert ma >= lba - 1e-9
    return N, Np, erra, mc, lbc, ma, lba


def check_B():
    worst_add = 0; viol_author = []; worst_gauss = {}
    for b in [3, 5, 7, 11, 13]:
        for v in [1, 2, 3]:
            m = b ** v
            if m > 1400:
                continue
            ph = m - m // b
            units = [x for x in range(m) if x % b]
            for a in range(1, m):
                s = abs(sum(e(a * x / m) for x in units)) / ph
                worst_add = max(worst_add, s * (b - 1))
            # all characters mod b^v via primitive root (b odd)
            g = primitive_root(m); ind = {}
            y = 1
            for t in range(ph):
                ind[y] = t; y = y * g % m
            for j in range(1, ph):
                for a in range(1, m):
                    G = abs(sum(e(j * ind[x] / ph) * e(a * x / m) for x in units)) / ph
                    if G > math.sqrt(m) / ph + 1e-9:
                        viol_author.append((b, v, j, a, round(G, 4), round(math.sqrt(m) / ph, 4)))
                    worst_gauss[b] = max(worst_gauss.get(b, 0), G * (b - 1) / math.sqrt(b))
    return worst_add, viol_author, worst_gauss


def main():
    n = 0
    for Q, r in [(1, 0), (3, 1), (4, 3), (5, 2), (7, 3)]:
        for x in [30, 60, 100, 150]:
            for q in [x + 1, x + 7, 2 * x + 1, 3 * x + 5, 5 * x + 3]:
                if isprime(q) or (len(factorint(q)) == 2 and all(v == 1 for v in factorint(q).values())):
                    if math.gcd(q, Q) != 1:
                        continue
                    res = check_A(Q, r, x, q)
                    if res:
                        n += 1
    print(f"(A) Lemma 2.3: {n} (Q,r,x,q) cases, all assertions (a),(b),identity passed")
    wa, viol, wg = check_B()
    print(f"(B) max |mean e(ax/b^v)|*(b-1) over units = {wa:.6f} (<=1 claimed)")
    print(f"(B) author's bound |tau|/phi <= sqrt(b^v)/phi violated in {len(viol)} cases, e.g. {viol[:3]}")
    print(f"(B) max |tau|/phi / (sqrt(b)/(b-1)) by b: {{{', '.join(f'{b}: {w:.4f}' for b, w in wg.items())}}}")


if __name__ == "__main__":
    main()
