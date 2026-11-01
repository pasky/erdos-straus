"""Independent exact checks of C3's scope, not a test of ES positivity.
Run: ulimit -v 2097152; timeout 90s uv run python scripts/z53_xrev_sqsieve_scope.py
Streaming: O(P0) auxiliary memory, no pair-by-point array.
"""
from fractions import Fraction
from math import isqrt


def legendre(a, q):
    r = pow(a % q, (q - 1) // 2, q)
    return -1 if r == q - 1 else r


def profile(a, primes):
    values = [legendre(a, q) for q in primes]
    return sum(values), values.count(0)


def is_square(a):
    return a > 0 and isqrt(a) ** 2 == a


def finite_examples():
    # All nonsquares; H holds with x0=2 and epsilon0=0.
    primes = [3, 5, 7, 11]
    support = [15, 21, 33]
    rows = [profile(a, primes) for a in support]
    assert rows == [(2, 2), (0, 2), (-2, 2)]
    assert all(not is_square(a) for a in support)
    diagonal = sum(-4 + len(primes) - nu for sigma, nu in rows)
    signed = sum(sigma * sigma - (len(primes) - nu) for sigma, nu in rows)
    minorant = sum(sigma * sigma - 4 for sigma, nu in rows)
    assert (diagonal, signed, minorant) == (-6, 2, -4)
    print('C3 with H, D=x^2-4, no squares:',
          'diagonal=', diagonal, 'signed=', signed, 'full=', minorant)

    # H does not prohibit a successful quadratic minorant with signed inputs.
    primes = [3, 5, 7, 11, 13]
    examples = {}
    for a in range(2, 10000):
        sigma, nu = profile(a, primes)
        if not is_square(a) and nu == 0 and sigma in (-3, -1, 1, 3):
            examples.setdefault(sigma, a)
        if len(examples) == 4:
            break
    assert len(examples) == 4
    weighted = [(1, 2)] + [(a, 1) for a in examples.values()]
    total = Fraction(0)
    for a, weight in weighted:
        sigma, nu = profile(a, primes)
        value = Fraction(sigma * sigma - 9, 16)
        assert value <= int(is_square(a)) and nu <= 4
        total += weight * value
    assert total == 1
    print('C3 with H, D=(x^2-9)/16: support/weights=', weighted,
          'positive full minorant=', total, '(signed estimates remain possible)')


def square_strip():
    # Independently enumerate the memo's odd-square balanced strip using Python
    # integers; recover the ordered pair sum via sigma^2-(P0-nu), not C code.
    n, W, lo, hi, P = 10000000200000001, 6250000, 20000, 40000, 1000
    assert isqrt(n) ** 2 == n
    primes = [q for q in range(P + 1, 2 * P + 1)
              if all(q % d for d in range(2, isqrt(q) + 1))]
    count = squares = lam = sum_nu = max_nu = 0
    nonsquare_sigmas = set()
    for C in range(W + 1, 2 * W + 1):
        for k in range((n + lo) // (4 * C) + 1, (n + hi) // (4 * C) + 1):
            s = 4 * C * k - n
            f = s * s - 4 * k
            assert f != 0
            sigma, nu = profile(f, primes)
            count += 1
            squares += is_square(f)
            lam += sigma * sigma
            sum_nu += nu
            max_nu = max(max_nu, nu)
            if not is_square(f):
                nonsquare_sigmas.add(sigma)
    p0 = len(primes)
    x0 = isqrt(p0)
    while x0 * x0 < p0 or (x0 - p0) % 2:
        x0 += 1
    H = ({-x0, x0} <= nonsquare_sigmas
         and (0 in nonsquare_sigmas or {-1, 1} <= nonsquare_sigmas))
    assert H and max_nu <= p0 - 1 and squares == 0
    M = max(map(abs, nonsquare_sigmas))
    diagonal = (p0 - M * M) * count - sum_nu
    signed = lam - p0 * count + sum_nu
    full = lam - M * M * count
    assert full == diagonal + signed and full <= 0 and signed > 0
    print('Independent odd-square strip:', dict(n=n, P0=p0, A=count,
          squares=squares, Lambda=lam, sum_nu=sum_nu, max_nu=max_nu, H=H))
    print(f'Valid minorant D=x^2-{M*M}: diagonal={diagonal}, '
          f'signed={signed}>0, full={full}<=0')


if __name__ == '__main__':
    finite_examples()
    square_strip()
