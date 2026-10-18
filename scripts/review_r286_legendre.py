"""R286 from-scratch check of LOWER_TAIL_FABLE §2.8 (Legendre form) and §2.9 (mutual-shift graph).

For n = 1 (mod 4) (primes, and optionally all non-square n as a stress test) enumerate the COMPLETE set
   L(n) = {(r, A): r >= 1, A >= 2, A | n + r, A = -1 (mod r)}
(complete: A >= r - 1, and either A = n + r (then r | n + 1) or A <= (n + r)/2, forcing r <= n + 2).
For each pair put a = (n + r)/A, b = (A + 1)/r, c = r, so n = abc - a - c, A = bc - 1, A* = ab - 1.
Five explicit ES constructions (derived independently in the review, exact Fractions):
  S1 4 | A    : 4/n = 1/(A* D n) + 1/(a D) + 1/(A* a D),   D = A/4
  S2 4 | A*   : 4/n = 1/(A D n) + 1/(c D) + 1/(A c D),     D = A*/4
  S3 4 | b    : 4/n = 1/(a c w) + 1/(a n w) + 1/(c n w),    w = b/4
  S4 4 | c    : 4/n = 1/(w A*) + 1/(b n w) + 1/(b n w A*),  w = c/4
  S5 4 | a    : 4/n = 1/(w A) + 1/(b n w) + 1/(b n w A),    w = a/4
Checks: (i) Jacobi (A/n) = -1  <=>  some S_i applies (Thm 4.5 incl. degenerate a, b, c = 1);
(ii) every applicable S_i gives a valid ES identity; (iii) the author's table rows (r mod 4) incl. the r = 3 (4)
explicit formula, and the even-A / odd-r pairs the table does not cover; (iv) existence per prime.
"""
import sys
from fractions import Fraction
from collections import Counter
from review_r286_canon import isprime, divisors, jacobi


def pairs(n):
    for r in range(1, n + 3):
        for A in divisors(n + r):
            if A >= 2 and (A + 1) % r == 0:
                yield r, A


def slices(n, r, A):
    a, b, c = (n + r) // A, (A + 1) // r, r
    assert n == a * b * c - a - c
    As = a * b - 1
    out = []
    if A % 4 == 0:
        D = A // 4; out.append(("S1", (As * D * n, a * D, As * a * D)))
    if As % 4 == 0 and As > 0:
        D = As // 4; out.append(("S2", (A * D * n, c * D, A * c * D)))
    if b % 4 == 0:
        w = b // 4; out.append(("S3", (a * c * w, a * n * w, c * n * w)))
    if c % 4 == 0 and As > 0:
        w = c // 4; out.append(("S4", (w * As, b * n * w, b * n * w * As)))
    if a % 4 == 0:
        w = a // 4; out.append(("S5", (w * A, b * n * w, b * n * w * A)))
    for name, den in out:
        assert all(x > 0 for x in den) and sum(Fraction(1, x) for x in den) == Fraction(4, n), (n, r, A, name)
    return out


def table_row_r3(n, r, A):
    """author's explicit formula for r = 3 (4): x=(p+r)/4, y=pAv(A+1)/(4r), z=pv(A+1)/(4r), v=(p+r)/A"""
    v = (n + r) // A
    if (n + r) % 4 or (n * A * v * (A + 1)) % (4 * r) or (n * v * (A + 1)) % (4 * r):
        return False
    x, y, z = (n + r) // 4, n * A * v * (A + 1) // (4 * r), n * v * (A + 1) // (4 * r)
    return Fraction(1, x) + Fraction(1, y) + Fraction(1, z) == Fraction(4, n)


def run(ns, label, st):
    for n in ns:
        found = False
        for r, A in pairs(n):
            j = jacobi(A, n)
            sl = slices(n, r, A)
            st[label + " pairs"] += 1
            if (j == -1) != bool(sl):
                st[label + " Thm4.5 mismatch"] += 1
                if st[label + " Thm4.5 mismatch"] <= 5:
                    print("mismatch", n, r, A, j, sl)
            if j == -1:
                found = True
                key = ("odd" if A % 2 else "even") + "A r%4=" + str(r % 4)
                st[label + " QNR " + key] += 1
                if r % 4 == 3:
                    st[label + " r=3 row formula ok, " + key] += table_row_r3(n, r, A)
                if r % 2 == 1 and A % 2 == 1:
                    pred = -1 if (A % 4 == 3 or r % 4 == 3) else 1
                    st[label + " 2-adic reading ok"] += (pred == j)
            elif r % 4 == 0 and A % 2 == 1:
                st[label + " r=0(4) but (A/n)=+1 (contradicts 'sign automatic')"] += 1
            elif r % 4 == 3 and A % 2 == 0:
                st[label + " r=3(4), even A, (A/n)=+1 (table row 'none' fails)"] += 1
        st[label + " n with a Legendre certificate"] += found
        st[label + " n"] += 1
        if not found:
            st[label + " FAILS"] += 1
            if label != "prime":
                print(label, "no Legendre certificate at", n)


if __name__ == "__main__":
    P = int(sys.argv[1]) if len(sys.argv) > 1 else 3000
    C = int(sys.argv[2]) if len(sys.argv) > 2 else 0
    st = Counter()
    run([p for p in range(5, P, 4) if isprime(p)], "prime", st)
    if C:
        run([n for n in range(5, C, 4) if not isprime(n) and int(n ** 0.5) ** 2 != n], "composite", st)
        run([m * m for m in range(3, int(C ** 0.5) + 1, 2)], "square", st)
    for k, v in sorted(st.items()):
        print(k, v)
