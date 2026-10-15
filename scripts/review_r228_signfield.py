"""R228 from-scratch check of NEAR_SQUARE_EXIST Thm 2.1 / Cor 2.2 / Cor 2.3 / Remark 2.4.

(1) Group criterion computed directly (no 2-adic table): F = Q(sqrt(-D)) is inside Sigma_M = Q(zeta_M, sqrt(-M)) iff
    Kronecker(-D, c) = 1 for every c mod L (L = 4*M*D) with c = 1 mod M and Jacobi(-M, c) = 1.
(2) Compare with the literal statements: Cor 2.2 (t-side: tk+1 square), Cor 2.3 (u-side: K0/2-adic table).
(3) Brute force: n = m^2 + k = 1 mod 4, generic m (gcd(m, b) = 1), all divisors A of N at the level with A = -1 mod M;
    chi = Jacobi(A, n) (valid for composite n too: gcd(A, n) = 1 and Jacobi reciprocity, n = 1 mod 4);
    also the DK table value and whether n is prime.
Usage: review_r228_signfield.py KLIST UMAX TMAX MMAX
"""
import sys
from math import gcd, isqrt
import numpy as np
from sympy import jacobi_symbol, factorint, isprime


def kron(a, n):
    # Kronecker symbol (a/n) for n > 0
    if n == 1:
        return 1
    r = 1
    while n % 2 == 0:
        n //= 2
        if a % 2 == 0:
            return 0
        r *= 1 if a % 8 in (1, 7) else -1
    if n == 1:
        return r
    return r * jacobi_symbol(a % n, n)


def sqfree(n):
    s = 1
    for q, e in factorint(n).items():
        if e % 2:
            s *= q
    return s


_crit_cache = {}


def F_in_Sigma(D, M):
    """D > 0 squarefree: is Q(sqrt(-D)) inside Q(zeta_M, sqrt(-M))?  Direct character check."""
    key = (D, M)
    if key in _crit_cache:
        return _crit_cache[key]
    L = 4 * M * D
    ok = True
    for c in range(1, L, 2):
        if gcd(c, L) != 1 or c % M != 1 % M:
            continue
        if jacobi_symbol((-M) % c, c) if c > 1 else 1:
            pass
        j = 1 if c == 1 else jacobi_symbol((-M) % c, c)
        if j != 1:
            continue
        if kron(-D, c) != 1:
            ok = False
            break
    _crit_cache[key] = ok
    return ok


def cor23(k, u):
    K = k + u
    K0 = sqfree(K)
    for q in factorint(K0):
        if q % 2 == 1 and u % q:
            return False
    if K0 % 2 == 1:
        if K0 % 4 == 3:
            return True
        return u % 4 == 1 or u % 4 == 0
    K1 = K0 // 2
    if u % 8 == 0:
        return True
    if u % 2 == 1 or u % 4 == 0:
        return False
    up = u // 2
    return up % 4 == (1 if K1 % 4 == 1 else 3)


def table_chi(t, u, v, A, As):
    return -1 if any(z % 4 == 0 for z in (t, u, v, A, As)) else 1


def divisors_from(f):
    ds = [1]
    for q, e in f.items():
        ds = [d * q ** i for d in ds for i in range(e + 1)]
    return ds


def main():
    klist = [int(x) for x in sys.argv[1].split(",")]
    UMAX, TMAX, MMAX = map(int, sys.argv[2:5])
    LIM = max(TMAX * (MMAX * MMAX + max(klist)) + 2, MMAX * MMAX + max(klist) + UMAX + 2)
    spf = np.zeros(LIM + 1, dtype=np.int32)
    for i in range(2, isqrt(LIM) + 1):
        if spf[i] == 0:
            sl = spf[i * i::i]
            sl[sl == 0] = i
    def fac(n):
        f = {}
        while n > 1:
            q = int(spf[n]) or n
            f[q] = f.get(q, 0) + 1
            n //= q
        return f
    tot_mismatch_c23 = tot_mismatch_c22 = 0
    for k in klist:
        mpar = 0 if k % 4 == 1 else 1  # n = 1 mod 4
        assert k % 4 in (0, 1)
        for side, LMAX in (("u", UMAX), ("t", TMAX)):
            pred_clean, emp_clean, notyet = [], [], []
            bad = []
            nolit = []
            for M in range(1, LMAX + 1):
                if side == "u":
                    a, b = 1, k + M
                else:
                    a, b = M, M * k + 1
                D = sqfree(a * b)
                pc = F_in_Sigma(D, M)
                if side == "u" and pc != cor23(k, M):
                    tot_mismatch_c23 += 1
                    print("COR2.3 MISMATCH", k, M)
                if side == "t" and pc != (isqrt(b) ** 2 == b):
                    tot_mismatch_c22 += 1
                    print("COR2.2 MISMATCH", k, M)
                dirty_odd = dirty_even = 0
                evenA_neg_prime = 0
                tab_mis = 0
                lit_generic = 0
                for m in range(1, MMAX + 1):
                    if m % 2 != mpar:
                        continue
                    g = gcd(m, b)
                    while g % 2 == 0 and g > 0:
                        g //= 2
                    if g != 1:  # generic := no ODD prime common to m and b (R228 D-def)
                        continue
                    if gcd(m, b) == 1:
                        lit_generic += 1
                    n = m * m + k
                    N = n + M if side == "u" else M * n + 1
                    for A in divisors_from(fac(N)):
                        if (A + 1) % M:
                            continue
                        chi = jacobi_symbol(A % n, n)
                        if side == "u":
                            u, t, v = M, (A + 1) // M, N // A
                        else:
                            t, u = M, (A + 1) // M
                            v = (N // A + 1) // M
                        As = t * v - 1
                        assert t * u * v - u - v == n
                        if isprime(n) and table_chi(t, u, v, A, As) != chi:
                            tab_mis += 1
                        if chi == -1:
                            if A % 2:
                                dirty_odd += 1
                            else:
                                dirty_even += 1
                if lit_generic == 0:
                    nolit.append(M)
                if pc:
                    pred_clean.append(M)
                if dirty_odd == 0:
                    emp_clean.append(M)
                if pc and dirty_odd:
                    bad.append(M)
                if not pc and not dirty_odd:
                    notyet.append(M)
                if pc and dirty_even:
                    print(f"  k={k} {side}={M}: predicted clean, {dirty_even} even-A chi=-1 words")
                if tab_mis:
                    print(f"  TABLE MISMATCH k={k} {side}={M}: {tab_mis}")
            print(f"k={k} side={side}: predicted clean {pred_clean}")
            print(f"   predicted clean but dirty (odd A): {bad};  predicted dirty, not yet dirty: {notyet}")
            print(f"   levels with NO m satisfying the literal gcd(m,b)=1: {len(nolit)} of {LMAX}")
    print("Cor2.3 table mismatches vs direct criterion:", tot_mismatch_c23, " Cor2.2:", tot_mismatch_c22)


main()
