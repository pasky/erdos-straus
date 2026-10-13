# ec_screen.py — square-obstruction screen for exponential families n_m = k*b^m + c (c = +-1).
# For exponent period L, a residue m mod L "survives" if n_m is a square modulo every prime power
# q^j (q < QMAX, q not dividing b) whose b-order divides L (i.e. n_m mod q^j depends only on m mod L).
# Zero survivors at some L  <=>  the family's closure avoids the profinite squares (no T1-type obstruction
# visible at that level).  Usage: PYTHONPATH=scripts uv run python scripts/ec_screen.py b c kmax [Ls...]
import sys
from math import gcd


def primes_upto(N):
    s = bytearray([1]) * (N + 1); s[0] = s[1] = 0
    for i in range(2, int(N ** .5) + 1):
        if s[i]:
            s[i * i::i] = bytearray(len(s[i * i::i]))
    return [i for i in range(N + 1) if s[i]]


def admissible_prime_powers(b, L, QMAX=200000, PRIMES=None):
    out = []
    for q in PRIMES or primes_upto(QMAX):
        if b % q == 0:
            continue
        if pow(b, L, q) != 1:
            continue
        Q = q
        while pow(b, L, Q * q) == 1 and Q * q < 10 ** 7:
            Q *= q
        out.append((q, Q))
    return out


def squares_mod(Q):
    return {(x * x) % Q for x in range(Q)} if Q < 10 ** 6 else None


_SQC = {}


def is_sq(r, q, Q):
    """is r a square mod Q = q^j (q odd)?"""
    if Q < 10 ** 6:
        if Q not in _SQC:
            _SQC[Q] = squares_mod(Q)
        return r % Q in _SQC[Q]
    r %= Q
    if r == 0:
        return True
    v = 0
    while r % q == 0:
        r //= q; v += 1
    if v % 2:
        return False
    return pow(r, (q - 1) // 2, q) == 1


UNIT_ONLY = [True]   # obstruction = unit squares (n = 0 mod q is handled by divisor classes)


def survivors(k, b, c, L, pps, base=None):
    base = base if base is not None else 10 * L + 64   # representative exponent >= 2-adic thresholds
    S = []
    for m in range(L):
        mm = base + ((m - base) % L)
        ok = True
        for q, Q in pps:
            v = k * pow(b, mm, Q) + c
            if (UNIT_ONLY[0] and v % q == 0) or not is_sq(v, q, Q):
                ok = False
                break
        if ok:
            S.append(m)
    return S


if __name__ == '__main__':
    b, c, kmax = int(sys.argv[1]), int(sys.argv[2]), int(sys.argv[3])
    Ls = [int(x) for x in sys.argv[4:]] or [12, 24, 36, 48, 60, 72, 120, 144, 180, 240, 360, 720]
    P = primes_upto(200000)
    PP = {L: admissible_prime_powers(b, L, PRIMES=P) for L in Ls}
    for k in range(1, kmax + 1):
        if k % b == 0:
            continue
        res = None
        for L in Ls:
            S = survivors(k, b, c, L, PP[L])
            if not S:
                res = L
                break
        last = S if res is None else []
        print(k, k % 3 == 0, 'Lmin=%s' % res, '' if res else 'surv@%d=%s' % (Ls[-1], last[:8]))
