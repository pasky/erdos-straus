"""O136 §5.3 (EVIDENCE): the ES genus G^- = {Q of disc -4dn : chi_{-4d}(Q) = -1}.
For n prime and n = odd square, d <= DMAX (gcd(d,n)=1): h^- = #reduced primitive forms in G^-,
and F_d(n) = #Type II quadruples (a,b,c) with this d (4abcd = a+b+nc, no gcd condition)."""
import sys, math
from sympy import primerange, jacobi_symbol

def kron_m4d(d, k):  # chi_{-4d}(k) for odd k coprime to d: Jacobi (-d/k)
    return jacobi_symbol((-d) % k, k) if k > 1 else 1

def genus_minus(d, n):
    D = 4 * d * n; hm = h = 0
    A = 1
    while 3 * A * A <= D:
        for B in range(-A + 1, A + 1):
            if (B * B + D) % (4 * A): continue
            C = (B * B + D) // (4 * A)
            if C < A or (C == A and B < 0): continue
            if math.gcd(math.gcd(A, abs(B)), C) != 1: continue
            h += 1
            # find a represented odd k coprime to 4dn
            k = next(v for v in (A, C, A + B + C, A - B + C, 4*A + 2*B + C, A + 2*B + 4*C, 9*A+3*B+C, A+3*B+9*C)
                     if v % 2 and math.gcd(v, D) == 1)
            if kron_m4d(d, k) == -1: hm += 1
        A += 1
    return h, hm

def F_typeII(d, n):  # (a,c): f=4acd-1 divides a+nc ; b=(a+nc)/f
    cnt = 0
    for c in range(1, n + 1):
        if 4 * c * d - 1 > n * c + c * n: break
        for a in range(1, 10**9):
            f = 4 * a * c * d - 1
            if f > a + n * c: break
            if (a + n * c) % f == 0: cnt += 1
    return cnt

ns = [("p", p) for p in [1009, 2689, 4729, 9601, 10009]] + [("sq", m*m) for m in [31, 41, 73, 97, 101]]
for tag, n in ns:
    row = []
    for d in range(1, 9):
        if math.gcd(d, n) > 1: continue
        h, hm = genus_minus(d, n)
        row.append(f"d={d}: h={h} h-={hm} F={F_typeII(d, n)}")
    print(tag, n, " | ".join(row), flush=True)
