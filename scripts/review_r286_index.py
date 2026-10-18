"""R286 check of the SHARP 1 'index calibration' arithmetic (LOWER_TAIL_FABLE §3.2).
G = (Z/4U)^x, H_k = k-th powers. [G : H_k] = prod over cyclic factors C_n of gcd(k, n).
Compare with the pooled try count tau_3(U) * log p (cells (m,u) with mu | U: sum_{k|U} tau(k) = tau_3(U)).
Also: the author's approximation [G:H_k] ~ k^{pi(y)/phi(k)} and the claim '< 3^{pi(y)} = tau_3(U)' for U = prod_{q<=y} q.
"""
from math import gcd, log, prod


def primes(y):
    return [q for q in range(2, y + 1) if all(q % r for r in range(2, int(q ** 0.5) + 1))]


def index_k(U_primes, k):
    # 4U with U squarefree containing 2  -> 8 * prod odd q ;  (Z/8)^x = C2 x C2
    cyc = [2, 2] if 2 in U_primes else [2]
    cyc += [q - 1 for q in U_primes if q != 2]
    return prod(gcd(k, n) for n in cyc)


def phi(k):
    return sum(1 for a in range(1, k + 1) if gcd(a, k) == 1)


if __name__ == "__main__":
    for y in (30, 100, 1000, 10000):
        P = primes(y)
        t3 = 3 ** len(P)
        row = ["y=%d pi=%d log3(tau3)=%d" % (y, len(P), len(P))]
        for k in (2, 3, 4, 5, 6, 8, 12, 24):
            I = index_k(P, k)
            approx = len(P) / phi(k) * log(k) / log(3)
            row.append("k=%d: log3[G:H]=%.0f (author approx %.0f)%s" % (
                k, log(I) / log(3), approx, " > tau3!" if I > t3 else ""))
        print("; ".join(row))
    # small U: tries tau_3(U) log p vs |G| = phi(4U)
    p = 10 ** 9
    for U in (1, 2, 3, 6, 12, 24, 30, 60, 120, 210, 2310):
        t3 = sum(sum(1 for d in range(1, k + 1) if k % d == 0) for k in range(1, U + 1) if U % k == 0)
        G = sum(1 for a in range(1, 4 * U) if gcd(a, 4 * U) == 1)
        print("U=%d tau3=%d tries~tau3*log p=%.0f |G|=%d %s" % (U, t3, t3 * log(p), G, "tries > |G|" if t3 * log(p) > G else ""))
