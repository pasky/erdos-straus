"""R273 from-scratch: size of L_{<=3}(p) = {A in [1,p): HJ (negative CF) length of p/A <= 3} and its QNR part,
for checking the O261 'no M1' claim (count ~ log^2 p on average, not a power).
Usage: PYTHONPATH=scripts uv run python scripts/review_r273_hjcount.py
"""
import math
import random


def hj_len(n, a, cap=4):
    """length of negative continued fraction n/a = b1 - 1/(b2 - ...), b_i >= 2 (except last may be >=2; n/a>1)."""
    r = 0
    while a:
        b = -(-n // a)  # ceil
        r += 1
        if r > cap:
            return r
        n, a = a, b * a - n
    return r


def is_prime(n):
    if n < 2:
        return False
    for q in (2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37):
        if n % q == 0:
            return n == q
    d, s = n - 1, 0
    while d % 2 == 0:
        d //= 2
        s += 1
    for b in (2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37):
        x = pow(b, d, n)
        if x in (1, n - 1):
            continue
        for _ in range(s - 1):
            x = x * x % n
            if x == n - 1:
                break
        else:
            return False
    return True


def divisors_of(n):
    from sympy import divisors
    return divisors(n)


def L3_fast(p):
    """L_{<=3}(p).  length 1: A=1.  length 2: A | p+1, A>=2, (p+1)/A>=2.
    length 3: p = b1*b2*b3 - b1 - b3 with b_i>=2, A = b2*b3 - 1; min(b1,b3) <= sqrt(p)."""
    out = {1}
    for A in divisors_of(p + 1):
        if A >= 2 and (p + 1) // A >= 2:
            out.add(A)
    r = math.isqrt(p) + 2
    for b1 in range(2, r + 1):  # (b1*b2 - 1)*b3 = p + b1
        for b3 in divisors_of(p + b1):
            if b3 >= 2:
                m = (p + b1) // b3
                if (m + 1) % b1 == 0 and (m + 1) // b1 >= 2:
                    b2 = (m + 1) // b1
                    out.add(b2 * b3 - 1)
    for b3 in range(2, r + 1):  # b1*(b2*b3 - 1) = p + b3
        for b1 in divisors_of(p + b3):
            if b1 >= 2:
                A = (p + b3) // b1
                if (A + 1) % b3 == 0 and (A + 1) // b3 >= 2:
                    out.add(A)
    return {A for A in out if A < p}


def main():
    random.seed(273)
    # (a) validate fast enumerator against brute HJ length for small p
    for p in [q for q in range(5, 3000) if is_prime(q) and q % 4 == 1]:
        brute = {A for A in range(1, p) if hj_len(p, A) <= 3}
        fast = L3_fast(p)
        assert brute == fast, (p, sorted(brute ^ fast)[:10])
    print("L3 enumerator agrees with brute HJ length for all p=1 mod 4 < 3000")
    # (b) lambda(p)<=3 <-> some QNR in L3, compare with Cor 4.6 boundary criterion for p=1 mod 8
    # (c) sizes
    for e in [4, 5, 6, 7, 8, 9, 10]:
        ps = []
        while len(ps) < 12:
            p = random.randrange(10**e, 2 * 10**e) | 1
            if p % 8 == 1 and is_prime(p):
                ps.append(p)
        sz = [len(L3_fast(p)) for p in ps] 
        if sz is None:
            break
        qn = []
        for p in ps:
            L = L3_fast(p)
            qn.append(sum(1 for A in L if pow(A, (p - 1) // 2, p) == p - 1))
        lg = math.log(ps[0]) ** 2
        print(f"p~1e{e}: |L3| mean {sum(sz)/len(sz):.1f} min {min(sz)} max {max(sz)}; QNR mean {sum(qn)/len(qn):.1f} "
              f"min {min(qn)}; log^2 p = {lg:.0f}; mean/log^2 = {sum(sz)/len(sz)/lg:.3f}")


if __name__ == "__main__":
    main()
