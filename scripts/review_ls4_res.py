"""R62 from-scratch arithmetic checks for EXCEPTIONAL_LARGESIEVE4 (EVIDENCE).
[3.2]  Lemma 3.2: for Q = 3 mod 4, A=(Q+1)/4, unit v: v in R(Q) iff rt | A^2 or st | A^2,
       rt, st least positive residues of -v/4, -1/(4v) mod Q.
[5.3a] H-small classes: #{-r/s mod l : 0<=r<=H, 1<=s<=H} <= (H+1)H <= z^{1/2} when H <= z^{1/4}/2,
       and U(Res_l) <= (#proj)/l for classes mod l^v (exact count over Z/l^2).
[5.3b] the named examples are H-small with the stated heights (-4, -1, -1/4, -4d, -1/(4d), -d (d|A)).
[5.3c] Remark (c): -4 in R(15) and -4 = 1 mod 5; projections mod l of R(l*q) over primes q fill Z/l.
"""
from math import gcd
from sympy import divisors, primerange, isprime

def R(M):
    A = (M + 1) // 4
    return {(-4 * D) % M for D in divisors(A * A)}

def lemma32(Qmax):
    n = 0
    for Q in range(3, Qmax, 4):
        A = (Q + 1) // 4; RQ = R(Q); A2 = A * A
        inv4 = pow(4, -1, Q)
        for v in range(1, Q):
            if gcd(v, Q) != 1: continue
            rt = (-v * inv4) % Q; st = (-pow(4 * v, -1, Q)) % Q
            rhs = (rt != 0 and A2 % rt == 0) or (st != 0 and A2 % st == 0)
            assert (v in RQ) == rhs, (Q, v)
            n += 1
    print(f"[3.2] ok on {n} (Q,v) pairs, Q < {Qmax}")

def hsmall(H, l):
    return {(-r * pow(s, -1, l)) % l for r in range(H + 1) for s in range(1, H + 1) if s % l}

def cor53():
    for z in [16, 81, 256, 1296, 4096]:
        H = int(z ** 0.25 / 2)
        for l in primerange(z + 1, z + 200):
            P = hsmall(H, l)
            assert len(P) <= (H + 1) * H <= z ** 0.5
            # classes mod l^v (v=1,2) with residue -r/s: fraction of Z/l^2 covered
            L2 = l * l
            cov = set()
            for r in range(H + 1):
                for s in range(1, H + 1):
                    b = (-r * pow(s, -1, L2)) % L2
                    cov |= {b}  # v = 2 class
                    cov |= {(b + l * k) % L2 for k in range(l)}  # v = 1 class
            assert len(cov) / L2 <= len(P) / l + 1e-15 and len(P) / l <= l ** -0.5
    print("[5.3a] ok")
    for M in [m for m in range(3, 4000, 4)]:
        A = (M + 1) // 4; RM = R(M)
        assert (-4) % M in RM and (-1) % M in RM
        if gcd(4, M) == 1:
            assert (-pow(4, -1, M)) % M in RM
        for d in divisors(A):
            assert (-d) % M in RM
        for d in divisors(A * A):
            assert (-4 * d) % M in RM and (-pow(4 * d, -1, M)) % M in RM
    print("[5.3b] ok (M < 4000)")
    assert (-4) % 15 in R(15) and ((-4) % 15) % 5 == 1
    for l in [11, 19, 23]:
        proj = set()
        for q in primerange(3, 3000):
            M = l * q
            if q == l or M % 4 != 3: continue
            proj |= {x % l for x in R(M)}
        print(f"[5.3c] l={l}: projections of R(l q), q<3000, cover {len(proj)}/{l} residues mod l")

if __name__ == "__main__":
    lemma32(400)
    cor53()
