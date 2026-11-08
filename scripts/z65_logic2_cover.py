"""z65 LOGIC2: profinite covering probe for Theorem D / question Q_U.

ET Prop 1.9 lists seven families of residue classes solvable by polynomials (T1a-T1d Type I, T2a-T2c Type II).
For a modulus Q and a target set K of unit residues mod Q, mark every residue mod Q lying in some family class whose
modulus divides Q, and report how much of K is covered.  If ALL of K is covered at some level Q, then K is a finite union
of polynomially solvable classes and IOpen proves ES on K for n >= N0 (U64 Thm B); see Z65_LOGIC2.md Theorem D.
Uncovered residues at level Q prove nothing by themselves (they may be covered at a higher level).

Families (ET Prop 1.9, sources/elsholtz-tao-1107.1010.pdf p. 8):
 T1a  n = -f mod 4ad,                         f | 4a^2 d + 1
 T1b  n = -f mod 4ac  and  n = -c/a mod f,    (4ac, f) = 1
 T1c  n = -f mod 4cd  and  n^2 = -4c^2 d mod f, (4cd, f) = 1
 T1d  n = -1/e mod 4ab,                       e | a+b, (e, 4ab) = 1
 T2a  n = -e mod 4ab,                         e | a+b, (e, 4ab) = 1
 T2b  n = -4a^2 d mod f,                      4ad | f+1
 T2c  n = -4a^2 d - e mod 4ade,               (4ad, e) = 1
Usage: uv run --with numpy --with sympy python scripts/z65_logic2_cover.py Q TARGET
  TARGET = "1mod840_nr11" (n = 1 mod 840, n a non-residue mod 11), or "nonsq" (all unit non-squares mod Q),
  or "sq" (control: unit squares mod Q; must stay 0% covered).
"""
import sys
from math import gcd

import numpy as np
from sympy import divisors, factorint
from sympy.ntheory.residue_ntheory import sqrt_mod


def is_qr(x, p):
    return pow(x % p, (p - 1) // 2, p) == 1


def mark_class(cov, Q, c, m):
    cov[c % m::m] = True


def mark_crt(cov, Q, c1, m1, c2_list, m2):
    """mark n = c1 mod m1 and n mod m2 in c2_list (gcd(m1, m2) = 1, m1*m2 | Q)."""
    M = m1 * m2
    inv = pow(m1, -1, m2)
    for c2 in c2_list:
        x = (c1 + m1 * (((c2 - c1) * inv) % m2)) % M
        cov[x::M] = True


def run(Q, target):
    cov = np.zeros(Q, dtype=bool)
    divs = [d for d in divisors(Q)]
    divset = set(divs)
    # moduli of the form 4*X with 4X | Q
    four = [m for m in divs if m % 4 == 0]
    cnt = 0
    for m in four:           # m = 4*P, P = ad / ac / cd / ab
        P = m // 4
        for a in divisors(P):
            d = P // a
            # T1a: n = -f mod 4ad, f | 4a^2 d + 1  (classes -f mod m for f | 4a^2d+1)
            for f in divisors(4 * a * a * d + 1):
                mark_class(cov, Q, -f, m); cnt += 1
            # T2a / T1d with (a, b) = (a, d): e | a+b, gcd(e, 4ab) = 1
            b = d
            for e in divisors(a + b):
                if gcd(e, 4 * a * b) == 1:
                    mark_class(cov, Q, -e, m); cnt += 1
                    mark_class(cov, Q, -pow(e, -1, m), m); cnt += 1
            # T1b with (a, c) = (a, d): f | Q, gcd(f, m) = 1, n = -f mod m, n = -c/a mod f
            # T1c with (c, d) = (a, d): n = -f mod m, n^2 = -4c^2 d mod f
            for f in divs:
                if f == 1 or gcd(f, m) != 1 or (m * f) not in divset:
                    continue
                c = d
                if gcd(a, f) == 1:
                    mark_crt(cov, Q, -f % m, m, [(-c * pow(a, -1, f)) % f], f); cnt += 1
                cc, dd = a, d
                rhs = (-4 * cc * cc * dd) % f
                roots = [x for x in (sqrt_mod(rhs, f, all_roots=True) or []) if gcd(x, f) == 1]
                if roots:
                    mark_crt(cov, Q, -f % m, m, roots, f); cnt += 1
    # T2b: n = -4a^2 d mod f, 4ad | f+1, f | Q
    for f in divs:
        if (f + 1) % 4:
            continue
        P = (f + 1) // 4
        for a in divisors(P):
            for d in divisors(P // a):
                if gcd(a, f) == 1:
                    mark_class(cov, Q, -4 * a * a * d, f); cnt += 1
    # T2c: n = -4a^2 d - e mod 4ade, gcd(4ad, e) = 1
    for m in four:
        P = m // 4
        for e in divisors(P):
            ad = P // e
            if gcd(4 * ad, e) != 1:
                continue
            for a in divisors(ad):
                d = ad // a
                mark_class(cov, Q, -4 * a * a * d - e, m); cnt += 1
    units = np.array([gcd(x, Q) == 1 for x in range(Q)]) if Q <= 3_000_000 else None
    if units is None:
        units = np.ones(Q, dtype=bool)
        for p in factorint(Q):
            units[::p] = False
    xs = np.arange(Q)
    if target == "1mod840_nr11":
        assert Q % 9240 == 0
        r11 = xs % 11
        nr = np.isin(r11, [x for x in range(1, 11) if not is_qr(x, 11)])
        K = units & (xs % 840 == 1) & nr
    elif target in ("sq", "nonsq"):
        sq = np.zeros(Q, dtype=bool)
        for x in range(Q):
            if gcd(x, Q) == 1:
                sq[(x * x) % Q] = True
        K = units & (sq if target == "sq" else ~sq)
    else:
        raise SystemExit("unknown target")
    nK = int(K.sum()); ncov = int((K & cov).sum())
    print(f"Q={Q} ({dict(factorint(Q))}) target={target} family_members={cnt} |K|={nK} covered={ncov} "
          f"uncovered={nK - ncov} frac_covered={ncov / max(nK, 1):.4f}")


if __name__ == "__main__":
    run(int(sys.argv[1]), sys.argv[2])
