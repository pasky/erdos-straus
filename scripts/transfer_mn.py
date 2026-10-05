"""O42 toy checks for the m/n witness family (POINTWISE_TRANSFER §5.1).

For m >= 4 and M ≡ -1 (mod m), A = (M+1)/m:
  (i)  {-u v^{-1} mod M : uvw = A} == R_m(M) := {-m D mod M : D | A^2}
  (ii) 1 not in R_m(M)                                  (class of one)
  (iii) identity: if n ≡ -u v^{-1} (M), s=(nv+u)/M, then
        m/n = 1/(suw) + 1/(nsvw) + 1/(nuvw)            (exact, Fractions)
  (iv) map D -> A^2/D preserves gcd(M, mD+1)          (mass-bound step)
Run: PYTHONPATH=scripts uv run python scripts/transfer_mn.py
"""
from fractions import Fraction
from math import gcd

def divisors(x):
    return [d for d in range(1, x + 1) if x % d == 0]

def check(m, Mmax):
    cnt = 0
    for M in range(m - 1, Mmax + 1, m):
        if M < 3:
            continue
        A = (M + 1) // m
        R = {(-m * D) % M for D in divisors(A * A)}
        fam = set()
        for u in divisors(A):
            for v in divisors(A // u):
                w = A // (u * v)
                fam.add((-u * pow(v, -1, M)) % M)
                # identity on a few n in the class
                c = (-u * pow(v, -1, M)) % M
                for n in (c, c + M, c + 7 * M):
                    if n == 0:
                        continue
                    assert (n * v + u) % M == 0
                    s = (n * v + u) // M
                    lhs = Fraction(m, n)
                    rhs = Fraction(1, s*u*w) + Fraction(1, n*s*v*w) + Fraction(1, n*u*v*w)
                    assert lhs == rhs, (m, M, u, v, w, n)
        assert fam == R, (m, M)
        assert 1 % M not in R, (m, M)
        for D in divisors(A * A):
            assert gcd(M, m*D+1) == gcd(M, m*(A*A//D)+1), (m, M, D)
        cnt += 1
    return cnt

if __name__ == "__main__":
    for m in (4, 5, 6, 7, 8, 11):
        print(f"m={m}: checked {check(m, 3000)} moduli M <= 3000: (i)-(iv) OK")
