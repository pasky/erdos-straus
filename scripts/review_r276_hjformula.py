"""R276: test the formula r(n/A) = 1 + sum_{i odd} a_i (canonical regular CF, last digit >= 2) against the true
Hirzebruch-Jung length; test the corrected formula r = 1 + sum_{i odd} a_i - [last index odd]; recompute the
ladder table |S_L| (true HJ length) at n = 10009 and the QNR shares."""
import sys, math
def cf(a, b):
    out = []
    while b:
        q, r = divmod(a, b); out.append(q); a, b = b, r
    return out
def hjlen(a, b):
    L = 0
    while b:
        c = -(-a // b); L += 1; a, b = b, c*b - a
    return L
def jac(a, n):
    a %= n; s = 1
    while a:
        while a % 2 == 0:
            a //= 2
            if n % 8 in (3, 5): s = -s
        a, n = n, a
        if a % 4 == 3 and n % 4 == 3: s = -s
        a %= n
    return s if n == 1 else 0
N = int(sys.argv[1])
mis = mis2 = tot = 0
for n in range(3, 400):
    for A in range(1, n):
        if math.gcd(A, n) != 1: continue
        c = cf(n, A); tot += 1
        f = 1 + sum(c[1::2]); h = hjlen(n, A); s = len(c) - 1
        mis += f != h; mis2 += (f - (s % 2)) != h
print(f"n<400: pairs {tot}, formula mismatches {mis}, corrected-formula mismatches {mis2}")
for n in (N,):
    true = {}; form = {}
    for A in range(1, n):
        if math.gcd(A, n) != 1: continue
        c = cf(n, A); true[A] = hjlen(n, A); form[A] = 1 + sum(c[1::2])
    for L in (3, 4, 6, 8):
        St = [A for A in true if true[A] <= L]; Sf = [A for A in form if form[A] <= L]
        qt = sum(jac(A, n) == -1 for A in St) / max(1, len(St)); qf = sum(jac(A, n) == -1 for A in Sf) / max(1, len(Sf))
        print(f"n={n} L={L}: |S_L| true-HJ {len(St)} (QNR share {qt:.2f}); via formula {len(Sf)} (QNR share {qf:.2f})")
    lam_t = min(true[A] for A in true if jac(A, n) == -1) if any(jac(A, n) == -1 for A in true) else None
    lam_f = min(form[A] for A in form if jac(A, n) == -1) if any(jac(A, n) == -1 for A in form) else None
    print(f"lambda true {lam_t}, via formula {lam_f}")
