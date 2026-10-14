# R215 — from-scratch checks for SEVEN_SIBLING §1 (free slices / odd quadratic characters), §5 (order-3 double
# failure rates), §4 (solution counts f_M(p) at small primes, exact divisor method).
import sys
from math import gcd
import sympy as sp

# ---- §1 Prop 1.1: non-free unit classes = kernel of an odd quadratic character mod M ?
def prop11(Mmax=60):
    hits = []
    for M in range(3, Mmax+1):
        U = [r for r in range(1, M) if gcd(r, M) == 1]
        free = {(-1) % M}
        if gcd(2, M) == 1:
            free |= {(-2) % M, (-pow(2, -1, M)) % M}
        nonfree = set(U) - free
        # all real (quadratic) characters mod M: enumerate homomorphisms U -> {±1} by brute force via generators
        # (small M: test every subset S of U of size |U|/2 that is a subgroup of index 2 not containing -1)
        if 2*len(nonfree) != len(U): continue
        S = nonfree
        sub = all((a*b) % M in S for a in S for b in S) and 1 in S
        if sub and (M-1) not in S:
            hits.append(M)
    return hits
print("§1: M ≤ 60 whose non-free unit classes form an index-2 subgroup not containing −1 (odd quadratic kernel):", prop11())
for M, D in ((4, -4), (6, -3), (7, -7)):
    U = [r for r in range(1, M) if gcd(r, M) == 1]
    free = sorted({(-1) % M} | ({(-2) % M, (-pow(2, -1, M)) % M} if M % 2 else set()))
    inert = sorted({r % M for r in range(1, 2000) if sp.isprime(r) and M % r and sp.kronecker_symbol(D, r) == -1})
    print(f"   M={M}: free classes {free}; residues mod M of primes inert in Q(sqrt({D})) {inert}")

# ---- §5 order 3
def all1mod3(N):
    return all(q % 3 == 1 for q in sp.factorint(N))
def order3(X):
    c4 = d4 = c7 = d7 = 0
    for p in sp.primerange(5, X+1):
        if p % 12 == 1:
            c4 += 1; d4 += all1mod3((p+3)//4) and all1mod3((3*p+1)//4)
        if p % 21 == 1:
            c7 += 1; d7 += all1mod3((p+6)//7) and all1mod3((6*p+1)//7)
    return c4, d4, c7, d7
# also: for p ≡ 1 (7), p ≡ 2 (3), the e=6 Type II slice always fires (N_II has a prime ≡ 2 mod 3)
def check_e6(X):
    for p in sp.primerange(5, X+1):
        if p % 7 == 1 and p % 3 == 2:
            assert not all1mod3((p+6)//7), p
    return True

# ---- §4 exact solution counts f_M(n) = #{x ≤ y ≤ z : 1/x + 1/y + 1/z = M/n}
def f(M, n):
    cnt = 0
    x0 = n // M + 1
    for x in range(x0, 3*n//M + 1):
        num, den = M*x - n, n*x          # 1/y + 1/z = num/den
        g = gcd(num, den); a, b = num//g, den//g
        # (a y - b)(a z - b) = b^2, y >= x, y <= z
        for d1 in sp.divisors(b*b):
            d2 = b*b//d1
            if d1 > d2: break
            if (d1 + b) % a or (d2 + b) % a: continue
            y = (d1 + b)//a
            if y >= x: cnt += 1
    return cnt

if __name__ == "__main__":
    X = int(sys.argv[1]) if len(sys.argv) > 1 else 10**6
    print("§5 e=6 Type II slice fires whenever p ≡ 1 (7), p ≡ 2 (3), p ≤ %d:" % X, check_e6(X))
    c4, d4, c7, d7 = order3(X)
    print(f"§5 M=4: p≡1 (12): {c4}, double failures {d4} ({100*d4/c4:.2f}%);  M=7: p≡1 (21): {c7}, double {d7} ({100*d7/c7:.2f}%)")
    P = int(sys.argv[2]) if len(sys.argv) > 2 else 1500
    ones = [p for p in sp.primerange(11, P+1) if f(7, p) <= 1]
    print(f"§4 M=7, 11 ≤ p ≤ {P}: f ≤ 1 at", [(p, f(7, p)) for p in ones])
    print("   f7(211) =", f(7, 211), " f8 at 11,17,131,241:", [f(8, p) for p in (11, 17, 131, 241)])
    print(f"   min f4 over 11 ≤ p ≤ {P}:", min((f(4, p), p) for p in sp.primerange(11, P+1)))
