"""R90 from-scratch checks for EXCEPTIONAL_WEIGHTS2 (prime slices R(l)).

Usage: uv run python review_weights2_slices.py LMAX_QNR YMAX
 * for all primes l = 3 (4), l <= LMAX_QNR: build R(l) twice, (a) from the definition
   {-u/v mod l : gcd(u,v)=1, 4uv | l+1} and (b) as {-4D : D | A^2}; check (a)=(b),
   |R(l)| vs tau(A^2), (tau(A^2)+1)/2 lower bound, all classes QNR (Euler criterion);
 * composite M = 3 (4), M <= LMAX_QNR/10: Jacobi(-u/v | M) = -1 for every class;
 * mass S(Y) = sum_{l<=Y} |R(l)|/l and self-overlap O_h(Y), dyadic increments.
"""
import sys
from math import gcd, log


def primes_upto(n):
    s = bytearray([1]) * (n + 1)
    s[0:2] = b"\x00\x00"
    for i in range(2, int(n ** 0.5) + 1):
        if s[i]:
            s[i * i::i] = bytearray(len(s[i * i::i]))
    return [i for i in range(n + 1) if s[i]]


def factor(n):
    f = {}
    d = 2
    while d * d <= n:
        while n % d == 0:
            f[d] = f.get(d, 0) + 1
            n //= d
        d += 1
    if n > 1:
        f[n] = f.get(n, 0) + 1
    return f


def divisors_from(f):
    ds = [1]
    for p, a in f.items():
        ds = [d * p ** k for d in ds for k in range(a + 1)]
    return ds


def jacobi(a, n):
    a %= n
    r = 1
    while a:
        while a % 2 == 0:
            a //= 2
            if n % 8 in (3, 5):
                r = -r
        a, n = n, a
        if a % 4 == 3 and n % 4 == 3:
            r = -r
        a %= n
    return r if n == 1 else 0


def R_def(M):
    """from the (u,v) definition"""
    B = (M + 1) // 4
    out = set()
    for q in divisors_from(factor(B)):
        for u in divisors_from(factor(q)):
            v = q // u
            if gcd(u, v) == 1:
                out.add((-u * pow(v, -1, M)) % M)
    return out


def R_D(M):
    A = (M + 1) // 4
    fA = factor(A)
    f2 = {p: 2 * a for p, a in fA.items()}
    return {(-4 * D) % M for D in divisors_from(f2)}, f2


def main():
    LQ = int(sys.argv[1])
    Y = int(sys.argv[2])
    P = [l for l in primes_upto(max(LQ, Y)) if l % 4 == 3]
    bad_eq = bad_qnr = bad_lb = 0
    n_cls = 0
    eq_tau = 0
    for l in P:
        if l > LQ:
            break
        a = R_def(l)
        b, f2 = R_D(l)
        tau = 1
        for e in f2.values():
            tau *= e + 1
        if a != b:
            bad_eq += 1
        if len(b) < (tau + 1) // 2:
            bad_lb += 1
        if len(b) == tau:
            eq_tau += 1
        for r in b:
            n_cls += 1
            if pow(r, (l - 1) // 2, l) != l - 1:
                bad_qnr += 1
    nL = sum(1 for l in P if l <= LQ)
    print(f"primes l=3(4) <= {LQ}: {nL}; classes {n_cls}; def!=D-form {bad_eq}; "
          f"|R|<(tau+1)/2 {bad_lb}; |R|=tau(A^2) in {eq_tau}; non-QNR classes {bad_qnr}")
    # composite M: Jacobi symbol
    badj = 0
    nc = 0
    for M in range(3, LQ // 10 + 1, 4):
        for r in R_def(M):
            nc += 1
            if jacobi(r, M) != -1:
                badj += 1
    print(f"all M=3(4) <= {LQ//10}: classes {nc}; Jacobi != -1: {badj}")
    # mass and overlaps
    hs = [1, 2, 3, 6, 10]
    S = 0.0
    O = {h: 0.0 for h in hs}
    nxt = 100
    for l in P:
        if l > Y:
            break
        while l > nxt:
            print(f"Y={nxt:>9} S={S:8.3f} S/(logY)^2={S/log(nxt)**2:.4f} "
                  + " ".join(f"O{h}={O[h]:.3f}" for h in hs))
            nxt *= 10
        F, _ = R_D(l)
        S += len(F) / l
        for h in hs:
            O[h] += len(F & {(x - h) % l for x in F}) / l
    print(f"Y={Y:>9} S={S:8.3f} S/(logY)^2={S/log(Y)**2:.4f} "
          + " ".join(f"O{h}={O[h]:.3f}" for h in hs))


if __name__ == "__main__":
    main()
