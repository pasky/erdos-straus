"""R69 from-scratch check of POINTWISE_TYPEI2 §2.2 (first rows) and of the
x7=-1 / w=9 integral-point claim, via Lemma 2.4's parametrisation re-derived:
  c' J J' - u = Lam,  u | J+J',  k'=(J+J')/u,  (c'k',14)=1,  F=c'k'J-1, (F,14)=1,
  Lam = 2^(2+al+2ga) 7^(a+2b), a odd.  Box: x2 == -F (2^(2+al+ga)), x7 == -F (7^(a+b)).
Also re-checks each box directly: F | 1+4ck^2 and F == -1 mod c'k'.
usage: review_ti2_union.py LamMax
"""
import sys
import numpy as np
from sympy import divisors


def boxes(L):
    out = []
    for a in range(1, 40, 2):
        for b in range(0, 20):
            p7 = 7 ** (a + 2 * b)
            if 4 * p7 > L:
                break
            for al in range(0, 60):
                for ga in range(0, 30):
                    Lam = 2 ** (2 + al + 2 * ga) * p7
                    if Lam > L:
                        break
                    for u in range(1, Lam + 5):
                        for cp in divisors(Lam + u):
                            if cp % 2 == 0 or cp % 7 == 0:
                                continue
                            P = (Lam + u) // cp
                            for J in divisors(P):
                                Jp = P // J
                                if (J + Jp) % u:
                                    continue
                                kp = (J + Jp) // u
                                if kp % 2 == 0 or kp % 7 == 0:
                                    continue
                                F = cp * kp * J - 1
                                if F <= 0 or F % 2 == 0 or F % 7 == 0:
                                    continue
                                c = 2 ** al * 7 ** a * cp
                                k = 2 ** ga * 7 ** b * kp
                                assert (1 + 4 * c * k * k) % F == 0
                                assert (F + 1) % (cp * kp) == 0
                                out.append((2 + al + ga, a + b, (-F) % 2 ** (2 + al + ga),
                                            (-F) % 7 ** (a + b), c, k, F))
                if 2 ** (2 + al) * p7 > L:
                    break
    return out


def main():
    L = int(sys.argv[1])
    bx = sorted(set(boxes(L)))
    T = max(b[0] for b in bx)
    S = max(b[1] for b in bx)
    M2, M7 = 2 ** T, 7 ** S
    x2 = np.arange(M2)
    x7 = np.arange(M7)
    in2 = (x2 % 8 == 1)
    nonsq = np.isin(x7 % 7, [3, 5, 6])
    cov = np.zeros((M2, M7), dtype=bool)
    nin = 0
    for t, v, r2, r7, c, k, F in bx:
        if r2 % 8 != 1 or (r7 % 7) not in (3, 5, 6):
            continue
        nin += 1
        cov[np.ix_(x2 % 2 ** t == r2, x7 % 7 ** v == r7)] = True
    sig = np.outer(in2, nonsq)
    unc = (sig & ~cov).sum() / sig.sum()
    print(f"LamMax={L} boxes_in_Sigma'={nin} uncovered={unc:.6f}")
    # integral points w=9 (x7=-1), and the sign point
    for w, z in [(9, -1), (-7, -1), (25, -1), (41, -1), (9, 6), (9, 5)]:
        hit = [b for b in bx if (w - b[2]) % 2 ** b[0] == 0 and (z - b[3]) % 7 ** b[1] == 0]
        print(f"  point (w={w}, x7={z}): covered by {len(hit)} boxes", hit[:2])


if __name__ == "__main__":
    main()
