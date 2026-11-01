"""z53 FORESTCLASS Theorem 1: CERTIFIED instances.

For given H, K, prime q ≡ 3 (mod 4) and a non-residue class c mod q, search primes p ≡ 1 (mod M1), p ≡ c (mod q)
(M1 as in the proof: p ≡ 1 modulo every prime power needed so that all primes < qK+2 other than q are residues,
L_x ≡ 1 mod x, and v_l(p+x) = v_l(1+x) for x in {1..H} ∪ {qj : j ≤ K}), and test DIRECTLY (no primality of the L's
assumed) that every component of F_p meeting {1..H} ∪ {K least non-residues of p} is monochromatic (full component
exploration).  Also reports whether the Dickson forms (p+x)/(1+x) are all prime (the theorem's hypothesis), the actual
least non-residues, and least non-principal-genus reduced-form minima.
Usage: uv run --with sympy python scripts/z53_forestclass_thm1inst.py H K q c NFOUND [maxtries] [dickson]
(with 'dickson': only primes p at which every form (p+x)/(1+x), x in X, is prime -- the theorem's exact hypothesis)
"""
import sys
sys.path.insert(0, __file__.rsplit("/", 1)[0])
from math import gcd
from sympy import isprime, factorint, primerange
from z52d_pellcycle_lib import explore, chi


def lcm(a, b):
    return a * b // gcd(a, b)


def setup(H, K, q, c):
    xs = list(range(1, H + 1)) + [q * j for j in range(1, K + 1)]
    M1 = 24
    for x in xs:
        for l, e in factorint(x).items():
            if l != q:
                M1 = lcm(M1, l ** e)
        for l, e in factorint(1 + x).items():
            M1 = lcm(M1, l ** (e + 1))
    for l in primerange(2, q * K + 2):
        if l != q:
            M1 = lcm(M1, l)
    assert M1 % q
    # p ≡ 1 mod M1, p ≡ c mod q
    t = ((c - 1) * pow(M1, -1, q)) % q
    p0 = 1 + M1 * t
    return xs, M1 * q, p0


def least_nonresidues(p, K):
    out, a = [], 2
    while len(out) < K:
        if chi(p, a) == -1:
            out.append(a)
        a += 1
    return out


def main():
    H, K, q, c, NF = map(int, sys.argv[1:6])
    maxtries = int(sys.argv[6]) if len(sys.argv) > 6 else 10 ** 6
    need_dickson = len(sys.argv) > 7 and sys.argv[7] == "dickson"  # require all Dickson forms prime first
    xs, Q, p0 = setup(H, K, q, c)
    print(f"# H={H} K={K} q={q} c={c} modulus Q={Q} p0={p0}")
    found = tries = 0
    s = 0
    while found < NF and tries < maxtries:
        s += 1
        p = p0 + Q * s
        if not isprime(p):
            continue
        tries += 1
        if need_dickson and not all(isprime((p + x) // (1 + x)) for x in xs):
            continue
        nr = least_nonresidues(p, K)
        menu = list(range(1, H + 1)) + nr
        ok = True
        for a in menu:
            st = explore(p, a, depth=None, cap=10 ** 6)[0]
            if st != "mono":
                ok = False
                break
        if ok:
            found += 1
            dick = all(isprime((p + x) // (1 + x)) for x in xs)
            print(f"INSTANCE p={p} s={s} least_NR={nr} dickson_forms_all_prime={dick}", flush=True)
    print(f"# tested {tries} primes in the class, found {found}")


if __name__ == "__main__":
    main()
