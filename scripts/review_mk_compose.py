"""R202: does composition of V_n points reach ES points? (test of MARKOFF_ES Prop 7.1(c))
For odd n <= nmax and 2n < mu <= Mf*n, take the ES point (B = 1, depth 3, D = Q_3) and look for V_n points at the
SAME mu with norms -D1, -D2, -D3 (Di > 1, D1 D2 D3 = D). Then verify explicitly that some product
a1^(+-) a2^(+-) a3^(+-) times a unit of Z[sqrt N] equals the ES element (B - mu A) - A sqrt(f), f = mu^2 - n.
Usage: review_mk_compose.py nmax Mf"""
import sys
from math import isqrt, gcd
sys.path.insert(0, "scripts")
from review_mk_cf import cf_upto


def mul(a, b, f):  # (x + y sqrt f)(u + v sqrt f)
    return (a[0] * b[0] + f * a[1] * b[1], a[0] * b[1] + a[1] * b[0])


def reps(n, mu):
    """all odd-k CF hits with Q_k | mu, gcd(Q_k, n) = 1, within 2 periods: dict D -> (x, z) with x^2 - 4f z^2 = -D."""
    N = 4 * (mu * mu - n)
    out = {}
    per = None
    for k, Q, p, q in cf_upto(N, 10 ** 10 ** 6, 2):
        if Q == 1 and per is None:
            per = k
        if k % 2 == 1 and Q % 2 == 1 and mu % Q == 0 and gcd(Q, n) == 1:
            out.setdefault(Q, (p, q))
        if per is not None and k >= 2 * per:
            return out


def main():
    nmax, Mf = map(int, sys.argv[1:3])
    found = 0
    for n in range(3, nmax + 1, 2):
        for mu in range(2 * n + 1, Mf * n + 1):
            t = mu % n or n
            j = (mu - t) // n
            D = 4 * t * j - 1
            if mu % D:
                continue
            f = mu * mu - n
            R = reps(n, mu)
            Ds = sorted(d for d in R if 1 < d < D and D % d == 0)
            for i, d1 in enumerate(Ds):
                for d2 in Ds[i:]:
                    if D % (d1 * d2) or D // (d1 * d2) not in R or D // (d1 * d2) < d2:
                        continue
                    d3 = D // (d1 * d2)
                    # elements x + 2 z sqrt f  (norm x^2 - 4 f z^2 = -d), i.e. in Z[2 sqrt f]
                    el = [(R[d][0], R[d][1]) for d in (d1, d2, d3)]
                    es = (2 * mu * j - 1, j)  # p_2 + q_2 sqrt N, norm -(4tj - 1)
                    ok = False
                    for s1 in (1, -1):
                        for s2 in (1, -1):
                            for s3 in (1, -1):
                                a = (el[0][0], 2 * s1 * el[0][1])
                                b = (el[1][0], 2 * s2 * el[1][1])
                                c = (el[2][0], 2 * s3 * el[2][1])
                                P = mul(mul(a, b, f), c, f)  # in Z[sqrt f] coords (x, y): x + y sqrt f
                                E = (es[0], 2 * es[1])
                                # P / E = P * conj(E) / N(E); unit iff divisible
                                num = mul(P, (E[0], -E[1]), f)
                                nE = E[0] ** 2 - f * E[1] ** 2
                                if num[0] % nE == 0 and num[1] % nE == 0:
                                    u = (num[0] // nE, num[1] // nE)
                                    if u[0] ** 2 - f * u[1] ** 2 in (1, -1) and u[1] % 2 == 0:
                                        ok = True
                    if ok:
                        found += 1
                        if found <= 10:
                            print("ES point reached by composition: n", n, "mu", mu, "D", D, "=", d1, "*", d2, "*", d3)
    print("total ES points that are (unit x) products of three V_n points at the same mu:", found)


if __name__ == "__main__":
    main()
