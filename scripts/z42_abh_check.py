"""O273 item (1): numerical sanity checks for the ABH transfer (EVIDENCE only).

For primes p and all quadratic non-residues A mod p:
  * HJ length r(p/A) (negative continued fraction length) vs E(A) := sum of even-index
    partial quotients c_j of A/p = [0; c_1, c_2, ...] (canonical last quotient > 1);
    checks r(p/A) <= 1 + E(A)  (ZAREMBA_TRANSFER Thm B formula) and records r - 1 - E.
  * ABH transfer identity: E = (S + S_alt)/2 with S_alt = sum (-1)^i c_i, and
    S_alt = -12 D(A/p) + O(1) (Barkan-Hickerson, ABH (5)): records max |S_alt + 12 D|.
  * "Convergent Legendre invariant": (A/p) = (sigma/p)(q_{i-1} rho_{i-1}/p) at every step.
  * median and min over QNR of r(p/A), vs (6/pi^2) L log L.
"""
import math
import sys
from fractions import Fraction


def hj_len(n, d):
    # n/d = b1 - 1/(b2 - 1/...), b_i >= 2 except possibly ... ; standard ceiling algorithm
    r = 0
    while d:
        b = -(-n // d)
        n, d = d, b * d - n
        r += 1
    return r


def cf(a, p):
    out = []
    n, d = a, p  # a/p = [0; c1, c2, ...]
    n, d = d, n
    while d:
        out.append(n // d)
        n, d = d, n % d
    return out  # c1, c2, ..., canonical (last > 1 unless single 1)


def dedekind(a, n):
    # exact s(a,n) via reciprocity (Euclid), as Fraction
    s = Fraction(0)
    sign = 1
    while n > 1 and a:
        a %= n
        if a == 0:
            break
        s += sign * (Fraction(a * a + n * n + 1, 12 * a * n) - Fraction(1, 4))
        a, n = n, a
        sign = -sign
    return s


def legendre(a, p):
    t = pow(a % p, (p - 1) // 2, p)
    return -1 if t == p - 1 else t


def isprime(n):
    if n < 2:
        return False
    i = 2
    while i * i <= n:
        if n % i == 0:
            return False
        i += 1
    return True


def run(p, dedek=True):
    bad_hj = 0
    gaps = set()
    worst_d = 0.0
    inv_bad = 0
    rs = []
    for A in range(1, p):
        if legendre(A, p) != -1:
            continue
        c = cf(A, p)
        E = sum(c[j] for j in range(1, len(c), 2))  # c_2, c_4, ... (1-based even)
        S = sum(c)
        Salt = sum(((-1) ** (i + 1)) * c[i] for i in range(len(c)))  # i 1-based: (-1)^i
        assert 2 * E == S + Salt
        r = hj_len(p, A)
        rs.append(r)
        if r > 1 + E:
            bad_hj += 1
        gaps.add(1 + E - r)
        if dedek:
            D = dedekind(A, p)
            worst_d = max(worst_d, abs(float(Salt + 12 * D)))
        # convergent Legendre invariant
        rho_prev, rho = p, A
        q_prev, q = 0, 1
        i = 0
        while rho:
            i += 1
            ci = rho_prev // rho
            sigma = (-1) ** (i - 1)
            # step i uses x = q_{i-1} (= q), y = rho_{i-1} (= rho)
            if legendre(sigma, p) * legendre(q * rho, p) != -1:
                inv_bad += 1
            rho_prev, rho = rho, rho_prev - ci * rho
            q_prev, q = q, ci * q + q_prev
    rs.sort()
    L = math.log(p)
    return dict(p=p, nqnr=len(rs), lam=rs[0], med=rs[len(rs) // 2],
                abh=6 / math.pi ** 2 * L * math.log(L), bad_hj=bad_hj,
                gap_range=(min(gaps), max(gaps)), max_Salt_plus_12D=worst_d,
                invariant_violations=inv_bad)


if __name__ == "__main__":
    ps = [int(x) for x in sys.argv[1:]] or [1009, 10009, 100049]
    for p in ps:
        assert isprime(p)
        print(run(p, dedek=p < 200000))
