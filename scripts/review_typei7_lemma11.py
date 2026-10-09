"""R109: from-scratch generation of small fibre certificates (direct divisor enumeration of N=1+4ck^2,
no use of the Pell/Lemma-2.4 machinery) and brute-force test of TYPEI7 Lemma 1.1 / criterion (1.2).

Usage: review_typei7_lemma11.py X   (all (c,k) with ck <= X, v_7(c) odd, level L=alpha+2gamma >= 7)
"""
import sys, math
from sympy import divisors

sys.path.insert(0, __file__.rsplit('/', 1)[0])
from review_typei7_check import v, cert_at


def main():
    X = int(sys.argv[1])
    certs = []
    for c in range(7, X + 1, 7):
        if v(7, c) % 2 == 0:
            continue
        al = v(2, c)
        for k in range(1, X // c + 1):
            ga = v(2, k)
            L = al + 2 * ga
            if L < 7:
                continue
            N = 1 + 4 * c * k * k
            ck = c * k
            m7 = 7 ** v(7, ck)
            rest = ck >> v(2, ck)
            rest //= m7
            for F in divisors(N):
                if F % 16 != 7 or (F + 1) % rest or (F - 1) % m7:
                    continue
                assert cert_at(c, k, F, -F)
                certs.append((c, k, F, L))
    print("fibre certificates found:", len(certs))
    bad = 0
    nchk = 0
    for c, k, F, L in certs:
        al, ga = v(2, c), v(2, k)
        co, ko = c >> al, k >> ga
        n = co * ko
        N = 1 + 4 * c * k * k
        e = N // F
        assert (e - F) % (16 * n) == 0
        delta = (e - F) // (16 * n)
        assert delta % 2 == 1 and v(2, e - F) == 4
        E = 5 - 9 * n * delta - 2 ** (L - 2) * co * ko * ko
        if v(2, F + 9) != 3 + v(2, E):
            bad += 1; print("Lemma1.1 FAIL", c, k, F)
        # criterion: for every split (alpha',gamma') of L, direct cert_at(.,9) vs congruence mod 2^{t-3}
        for a2 in range(L % 2, L + 1, 2):
            g2 = (L - a2) // 2
            c2, k2 = co << a2, ko << g2
            t = 2 + a2 + g2
            direct = cert_at(c2, k2, F, 9)
            cong = (9 * n * delta + 2 ** (L - 2) * co * ko * ko - 5) % (2 ** (t - 3)) == 0
            nchk += 1
            if direct != cong:
                bad += 1; print("criterion FAIL", c, k, F, a2)
        # (1.2) form at every modulus 2^j, j <= ceil(L/2)-1 ... and beyond up to L-2 where 2^{L-2} term vanishes
        inv = lambda j: (5 * pow(9, -1, 2 ** j)) % 2 ** j
        for j in range(1, L - 1):
            lhs = v(2, F + 9) >= j + 3
            rhs = (n * delta - inv(j)) % 2 ** j == 0
            nchk += 1
            if lhs != rhs:
                bad += 1; print("(1.2) FAIL", c, k, F, j)
        # cofactor orientation
        if v(2, e + 9) != 3 + v(2, 5 + 9 * n * delta - 2 ** (L - 2) * co * ko * ko):
            bad += 1; print("cofactor FAIL", c, k, F)
        print(f"L={L} c={c} k={k} F={F} e={e} v2(F+9)={v(2, F + 9)} v2(e+9)={v(2, e + 9)} tmin={2 + (L + 1) // 2}")
    print("checks:", nchk, "failures:", bad)


if __name__ == "__main__":
    main()
