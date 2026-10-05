"""O31 (POINTWISE_TYPEI.md Lemma 1.1): check M_{c,k}(p) (divisor count) == dual count over j."""
import sys
from sympy import primerange, divisors


def M_div(p, c, k):
    h, N = 4 * c * k, p * p + 4 * c * k * k
    return sum(1 for d in divisors(N) if (d + p) % h == 0)


def M_dual(p, c, k):
    h, N = 4 * c * k, p * p + 4 * c * k * k
    cnt, j = 0, p // h + 1
    while h * j - p <= N:
        D = h * j - p
        if (4 * c * j * j + 1) % D == 0:
            cnt += 1
        j += 1
    return cnt


if __name__ == "__main__":
    X = int(sys.argv[1]) if len(sys.argv) > 1 else 400
    L = int(sys.argv[2]) if len(sys.argv) > 2 else 12
    bad = tot = 0
    for p in primerange(3, X):
        for c in range(1, L + 1):
            for k in range(1, L + 1):
                if (c * k) % p == 0:
                    continue
                tot += 1
                if M_div(p, c, k) != M_dual(p, c, k):
                    bad += 1
    print(f"dual check: {tot} (p,c,k) triples, mismatches {bad}")
    sys.exit(1 if bad else 0)
