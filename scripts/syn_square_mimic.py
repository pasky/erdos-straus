"""O171 §2 checks: Lemma 2.2 (T1 for e-slices) and Theorem 2.3 (square-mimic: no Y-block witness at
Y-smooth slices when p = 1 (8) and n_p > Y).  Usage:
  syn_square_mimic.py lemma MMAX EMAX
  syn_square_mimic.py thm PMAX EMAX Y1,Y2,...
"""
import sys
from sympy import factorint, primerange, legendre_symbol, primefactors


def divisors_from_fac(fac):
    ds = [1]
    for q, k in fac.items():
        ds = [d * q**i for d in ds for i in range(k + 1)]
    return ds


def sigma_has_minus1(fac, e):
    """-1 in Sigma_e(N): exists a, b with ab | N, a + b = 0 mod e."""
    ds = divisors_from_fac(fac)
    N = 1
    for q, k in fac.items():
        N *= q**k
    for a in ds:
        rest = N // a
        for b in ds:
            if rest % b == 0 and (a + b) % e == 0:
                return True
    return False


def block_witness(N, e, Y):
    """Y-block witness: -1 in Sigma_e(s)*{1, P^{+-1}} with s the Y-smooth part, P the rough part."""
    s, P = 1, N
    for q in primerange(2, Y + 1):
        while P % q == 0:
            P //= q
            s *= q
    fac = factorint(s)
    ds = divisors_from_fac(fac)
    for a in ds:
        rest = s // a
        for b in ds:
            if rest % b:
                continue
            for (x, y) in ((a, b), (a * P, b), (a, b * P)):
                if (x + y) % e == 0:
                    return True
    return False


def is_smooth(e, Y):
    return all(q <= Y for q in primefactors(e))


def least_qnr(p):
    n = 2
    while legendre_symbol(n, p) == 1:
        n += 1
    return n


def main():
    mode = sys.argv[1]
    if mode == "lemma":
        M, E = int(sys.argv[2]), int(sys.argv[3])
        bad = cnt = 0
        for m in range(1, M + 1, 2):
            for e in range(3, E + 1, 4):
                if __import__("math").gcd(m, e) != 1:
                    continue
                N = (m * m + e) // 4
                cnt += 1
                if sigma_has_minus1(factorint(N), e):
                    bad += 1
                    print("VIOLATION", m, e)
        print(f"lemma2.2: {cnt} (m,e) pairs, violations={bad}")
    elif mode == "thm":
        PM, E = int(sys.argv[2]), int(sys.argv[3])
        Ys = [int(y) for y in sys.argv[4].split(",")]
        for Y in Ys:
            es = [e for e in range(3, E + 1, 4) if is_smooth(e, Y)]
            nprimes = viol = checks = 0
            ctrl_p = ctrl_hit = 0
            for p in primerange(Y + 2, PM):
                if p % 8 != 1:
                    continue
                ls = least_qnr(p)
                if ls > Y:
                    nprimes += 1
                    for e in es:
                        if e >= p:
                            break
                        checks += 1
                        if block_witness((p + e) // 4, e, Y):
                            viol += 1
                            print("VIOLATION", p, e, Y)
                elif ctrl_p < 3000:
                    ctrl_p += 1
                    if any(block_witness((p + e) // 4, e, Y) for e in es if e < p):
                        ctrl_hit += 1
            print(f"Y={Y}: {len(es)} Y-smooth slices e<={E}; {nprimes} primes p=1(8), n_p>Y, p<{PM}; "
                  f"{checks} slice checks, violations={viol}; control (n_p<=Y): {ctrl_hit}/{ctrl_p} have a block witness")


if __name__ == "__main__":
    main()
