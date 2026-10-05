"""R36 from-scratch checks for sieve-limits v4 §10 (no reuse of author scripts).

1. Lemma localweight: log m <= log S_y(m) + Z_y(m) log y for y-smooth m (exact check).
2. ElT slip (ii): (-ka/q) vs c(q)(q/k'a) with and without the reciprocity sign.
3. (7.10) uniformity in k: sum_{a<=A} sum_{m<=B} rho_{ka}(m)/m / (A log B log(1+k)).
"""
import math
from sympy import factorint, jacobi_symbol


def check_localweight(N=20000, ys=(2, 3, 5, 7, 11, 13, 30)):
    worst = 0.0
    for y in ys:
        for m in range(1, N + 1):
            f = factorint(m)
            if f and max(f) > y:
                continue
            S = 1
            Zlog = 0.0
            for p, v in f.items():
                if p ** v > y:
                    S *= p ** v
                    assert v >= 2, (m, y)
                # sum of Lambda(p^nu) over nu<=v with p^nu<=y
                nu = 1
                while nu <= v and p ** nu <= y:
                    Zlog += math.log(p)
                    nu += 1
            lhs = math.log(m)
            rhs = math.log(S) + Zlog
            assert lhs <= rhs + 1e-9, (m, y)
            worst = max(worst, lhs - rhs)
    return worst


def kron_neg(D, q):
    # Jacobi symbol (D/q), q odd positive
    return jacobi_symbol(D % q, q)


def check_slip(maxk=40, maxa=40, maxq=400):
    bad_et = 0
    bad_fixed = 0
    tot = 0
    for k in range(1, maxk + 1):
        m = 0
        kk = k
        while kk % 2 == 0:
            kk //= 2
            m += 1
        for a in range(1, maxa + 1, 2):
            ka0 = kk * a
            for q in range(3, maxq, 2):
                if math.gcd(q, 2 * k * a) != 1:
                    continue
                lhs = kron_neg(-k * a, q)
                c = (-1) ** ((q - 1) // 2 + m * (q * q - 1) // 8)
                rhs_et = c * jacobi_symbol(q % ka0, ka0) if ka0 > 1 else c
                sign = (-1) ** (((q - 1) // 2) * ((ka0 - 1) // 2))
                tot += 1
                bad_et += lhs != rhs_et
                bad_fixed += lhs != sign * rhs_et
    return tot, bad_et, bad_fixed


def rho(P_a, mod):
    return sum(1 for b in range(mod) if (P_a * b * b + 1) % mod == 0)


def check_710(A=30, B=3000, ks=(1, 2, 3, 4, 8, 16, 64, 256, 1024, 2**14, 3**9)):
    # rho_{ka}(m) multiplicative in m; compute via factorisation
    out = []
    for k in ks:
        tot = 0.0
        for a in range(1, A + 1):
            ka = k * a
            cache = {}
            for mm in range(1, B + 1):
                r = 1
                for p, e in factorint(mm).items():
                    pe = p ** e
                    if pe not in cache:
                        cache[pe] = rho(ka % pe, pe)
                    r *= cache[pe]
                    if r == 0:
                        break
                tot += r / mm
        out.append((k, tot / (A * math.log(B) * math.log(1 + k))))
    return out


if __name__ == "__main__":
    print("localweight worst lhs-rhs (should be <=0):", check_localweight())
    print("slip (ii): total, mismatches ElT c(q), mismatches corrected:", check_slip())
    for k, r in check_710():
        print(f"(7.10) k={k}: ratio {r:.4f}")
