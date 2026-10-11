"""O136 §4 F4 / Thm 3.1(b) (EVIDENCE): fibre counts for the Type II pair encoding at (c,d) = (1,1).
Orbits of SL2(Z) on pairs (Q,S) with Gram 4[-n,1,1] <-> base pairs (Q_A, S_1), S_1 = [0,2,1],
Q_A = [A, A+1, ((A+1)^2+4n)/(4A)], A odd, A | 4n+1 (both signs).  ES (Type II, c=d=1) orbits:
A > 0, A = 3 mod 4 (level datum 4 | B).  For each orbit count #{g in SL2(Z) : max|coeff of (Q,S)g| <= H}
and compare across orbits (Thm 3.1(b) predicts equal asymptotics)."""
import sys, math
from sympy import divisors

def act(F, g):
    A, B, C = F; a, b, c, d = g
    return (A*a*a + B*a*c + C*c*c, 2*A*a*b + B*(a*d + b*c) + 2*C*c*d, A*b*b + B*b*d + C*d*d)

def count_orbit(Q, S, H, R):
    cnt = 0
    for a in range(-R, R + 1):
        for c in range(-R, R + 1):
            if math.gcd(a, c) != 1: continue
            # particular (b0,d0) with a*d0 - b0*c = 1
            if c == 0:
                if abs(a) != 1: continue
                b0, d0, step = 0, a, (a, 0)
            else:
                # solve a*d - c*b = 1
                g, x, y = ext(a, -c)  # a*x + (-c)*y = 1 -> d=x, b=y
                b0, d0 = y, x
            # all solutions (b,d) = (b0 + t a, d0 + t c)
            # scan t in a window where |b|,|d| <= R
            ts = []
            if a != 0: ts += [(-R - b0) / a, (R - b0) / a]
            if c != 0: ts += [(-R - d0) / c, (R - d0) / c]
            lo, hi = math.floor(min(ts)) - 1, math.ceil(max(ts)) + 1
            for t in range(lo, hi + 1):
                b, d = b0 + t*a, d0 + t*c
                if abs(b) > R or abs(d) > R: continue
                g4 = (a, b, c, d)
                q, s = act(Q, g4), act(S, g4)
                if max(map(abs, q + s)) <= H: cnt += 1
    return cnt // 2  # g and -g act identically

def ext(a, b):
    if b == 0: return (a, 1, 0) if a > 0 else (-a, -1, 0)
    g, x, y = ext(b, a % b)
    return g, y, x - (a // b) * y

H = int(sys.argv[1]) if len(sys.argv) > 1 else 3000
R = int(2 * math.isqrt(H)) + 2
for n in [29, 41, 53, 9, 25, 49]:
    N = 4*n + 1
    rows = []
    for A in sorted(set(divisors(N)) | {-x for x in divisors(N)}):
        if A % 2 == 0: continue
        num = (A + 1)**2 + 4*n
        if num % (4*A): continue
        Q = (A, A + 1, num // (4*A)); S = (0, 2, 1)
        es = A > 0 and A % 4 == 3
        rows.append((A, es, count_orbit(Q, S, H, R)))
    print(f"n={n} N=4n+1={N}  F_ES={sum(r[1] for r in rows)}  orbits(genus-full)={len(rows)}")
    for A, es, k in rows:
        print(f"   A={A:6d} ES={es!s:5} count(H={H})={k}  count/H={k/H:.4f}")
    sys.stdout.flush()
