# R92 from-scratch check of TYPEI5 Lemma 1.1 / Cor 1.2.
# (1) brute force: for 7|Q, all solutions of 16PX^2 - Q u^2 = 1 with u <= U (direct search over u);
#     check: any solution with u a power of 7 is the minimal one; all u are multiples of u_1;
#     u_n/u_1 = L_n == n (mod 7) where n is the index (recomputed by exact powering of alpha).
# (2) index k of {A+4B sqrt d} in norm-one units of Z[sqrt d] for odd d: claim k in {1,2,4}; we test k in {1,2}.
import sys
from math import isqrt

def is_sq(n):
    if n < 0: return False
    r = isqrt(n); return r * r == n

def brute(P, Q, U):
    sols = []
    for u in range(1, U + 1):
        num = 1 + Q * u * u
        if num % (16 * P): continue
        x2 = num // (16 * P)
        if is_sq(x2): sols.append((isqrt(x2), u))
    return sols

def is7pow(u):
    while u % 7 == 0: u //= 7
    return u == 1

def check1(Pmax, Qmax, U):
    nsys = nsol = nmulti = n7 = 0; bad = []
    for P in range(1, Pmax + 1):
        for Q in range(7, Qmax + 1, 7):
            if is_sq(P * Q): continue
            s = brute(P, Q, U)
            if not s: continue
            nsys += 1; nsol += len(s)
            X1, u1 = s[0]
            if len(s) > 1: nmulti += 1
            # exact powers alpha^n in basis (sqrt P, sqrt Q): (a sqrtP + b sqrtQ)
            # alpha^n = alpha^(n-2) * alpha^2, alpha^2 = A2 + B2 sqrt(PQ)
            A2 = 16 * P * X1 * X1 + Q * u1 * u1; B2 = 8 * X1 * u1
            a, b = 4 * X1, u1; n = 1; pw = {}
            while b <= U:
                pw[b] = (n, a); n += 2
                a, b = a * A2 + b * B2 * Q, a * B2 * P + b * A2
            if sorted(pw) != [u for _, u in s]:
                bad.append(("powers", P, Q, s, pw)); continue
            for X, u in s:
                nn = pw[u][0]
                if u % u1 or (u // u1 - nn) % 7: bad.append(("Ln", P, Q, X, u))
                if is7pow(u):
                    n7 += 1
                    if u != u1: bad.append(("7pow-nonmin", P, Q, X, u))
    print(f"(1) systems with sols={nsys} sols={nsol} with >=2 sols in range={nmulti} 7pow-sols={n7} bad={bad[:5]} nbad={len(bad)}")

def fund_unit(d):
    # minimal x>1 with x^2 - d y^2 = 1 via continued fraction
    a0 = isqrt(d); m, q, a = 0, 1, a0
    p0, p1 = 1, a0; q0, q1 = 0, 1
    while True:
        if p1 * p1 - d * q1 * q1 == 1: return p1, q1
        m = a * q - m; q = (d - m * m) // q; a = (a0 + m) // q
        p0, p1 = p1, a * p1 + p0; q0, q1 = q1, a * q1 + q0

def check2(dmax):
    from collections import Counter
    cnt = Counter()
    for d in range(3, dmax + 1, 2):
        if is_sq(d): continue
        x, y = fund_unit(d); A, B = x, y; k = 1
        while B % 4:
            A, B = A * x + d * B * y, A * y + B * x; k += 1
        cnt[k] += 1
    print("(2) index k distribution over odd nonsquare d <=", dmax, dict(cnt))

if __name__ == "__main__":
    check1(int(sys.argv[1]), int(sys.argv[2]), int(sys.argv[3]))
    check2(int(sys.argv[4]))

def check3(Xmax, Qmax, bmax):
    # systems constructed to HAVE a solution with u = 7^b; Lemma 1.1 says no smaller positive u exists.
    nsys = 0; bad = []
    for b in range(0, bmax + 1):
        u = 7 ** b
        for X in range(1, Xmax + 1):
            m = 16 * X * X
            for Q in range(7, Qmax + 1, 7):
                if (1 + Q * u * u) % m: continue
                P = (1 + Q * u * u) // m
                if is_sq(P * Q): continue
                nsys += 1
                for up in range(1, u):
                    num = 1 + Q * up * up
                    if num % (16 * P) == 0 and is_sq(num // (16 * P)):
                        bad.append((P, Q, X, u, up)); break
    print(f"(3) constructed systems with u=7^b (b<={bmax}): {nsys}, smaller-u solutions found: {bad[:5]} n={len(bad)}")

if __name__ == "__main__" and len(sys.argv) > 5:
    check3(int(sys.argv[5]), int(sys.argv[6]), int(sys.argv[7]))
