"""z65 LOGIC2 kill test K2 (Theorem T, 'only nonstandard prime' lemma).

Residue law at an odd prime l: (a1, a2) uniform on S_l = {(x, y) in F_l^2 : x + i*y is a unit square in F_l[i]},
a3 uniform on F_l, independent.  (F_l[i] = F_l[X]/(X^2+1); for l = 1 mod 4 it is F_l x F_l, else F_{l^2}.)
For test polynomials f we compute exactly  P_l(f) := P(f(a) = 0 mod l)  and report  l * P_l(f)  averaged over primes.
Lemma claim: for every irreducible f not associate to n = b1^2 + b2^2, l*P_l(f) >= c > 0 on a set of primes of positive
density (so sum P_l = infinity, Borel-Cantelli II gives infinitely many l | phi(f) almost surely); for f = n, P_l = 0.
Usage: uv run --with sympy python scripts/z65_logic2_onlyprime.py [LMAX]
"""
import sys
from sympy import primerange

LMAX = int(sys.argv[1]) if len(sys.argv) > 1 else 400

TESTS = {
    "n = b1^2+b2^2": lambda x, y, z, l: (x * x + y * y) % l,
    "b1": lambda x, y, z, l: x % l,
    "b1+1": lambda x, y, z, l: (x + 1) % l,
    "b1+b2": lambda x, y, z, l: (x + y) % l,
    "b1^2+b2^2+1": lambda x, y, z, l: (x * x + y * y + 1) % l,
    "b1*b2+1": lambda x, y, z, l: (x * y + 1) % l,
    "b1^2+b2^2-2": lambda x, y, z, l: (x * x + y * y - 2) % l,
    "b1^2+b2^2+b3^2": lambda x, y, z, l: (x * x + y * y + z * z) % l,
    "b1^2+b2^2-3*b3^2": lambda x, y, z, l: (x * x + y * y - 3 * z * z) % l,
    "b3": lambda x, y, z, l: z % l,
    "b1+b2*b3": lambda x, y, z, l: (x + y * z) % l,
    "(b1^2+b2^2)^2+b3": lambda x, y, z, l: ((x * x + y * y) ** 2 + z) % l,
}


def unit_squares_gauss(l):
    """Set of (x, y) with x + iy a unit square in F_l[i], via (s+it)^2 = s^2 - t^2 + 2st i, N(s+it) != 0."""
    S = set()
    for s in range(l):
        for t in range(l):
            if (s * s + t * t) % l:
                S.add(((s * s - t * t) % l, (2 * s * t) % l))
    return S


def main():
    rows = {k: [] for k in TESTS}
    for l in primerange(3, LMAX):
        S = unit_squares_gauss(l)
        Sl = list(S)
        for name, f in TESTS.items():
            uses_z = "b3" in name
            zero = 0
            if uses_z:
                for (x, y) in Sl:
                    for z in range(l):
                        if f(x, y, z, l) == 0:
                            zero += 1
                P = zero / (len(Sl) * l)
            else:
                for (x, y) in Sl:
                    if f(x, y, 0, l) == 0:
                        zero += 1
                P = zero / len(Sl)
            rows[name].append((l, l * P))
    print(f"# primes 3 <= l < {LMAX}; entries: mean of l*P_l(f) over l = 1 (4) and l = 3 (4); min over l > 50")
    for name, r in rows.items():
        a = [v for (l, v) in r if l % 4 == 1]
        b = [v for (l, v) in r if l % 4 == 3]
        big = [v for (l, v) in r if l > 50]
        print(f"{name:22s}  l=1(4): {sum(a)/len(a):.4f}   l=3(4): {sum(b)/len(b):.4f}   min(l>50): {min(big):.4f}")


if __name__ == "__main__":
    main()
