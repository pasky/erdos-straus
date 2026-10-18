"""R274 from-scratch check of DISPROOF_AVENUES Prop 3.1 (n = 1 shadow).

(1) Symbolic: the row identities (sympy).
(2) Slice counts by DIRECT search in the ET equations (fix two variables, loop a third over a rigorous range, solve the
    fourth linearly, verify exactly) -- no use of the N_theta / divisor-class table.
(3) For each test set Theta: primes p = 1 + Q t (Q = lcm of q_theta * N_theta(1), as literally stated in Prop 3.1) with
    every P_theta = N_theta(p)/N_theta(1) a (integer) prime; report the max slice count (Prop 3.1 says 0), plus controls
    (same p-class with some P_theta composite) to show the hypothesis is not vacuous.
Type II: 4abcd = a + b + c p.   Type I: 4abcd = p(a + b) + c.
"""
import math, sys
import numpy as np
import sympy as sp
from sympy import isprime

def sym_checks():
    a, b, c, d, p = sp.symbols('a b c d p', positive=True)
    II = 4*a*b*c*d - (a + b + c*p)          # = 0 on Type II
    I = 4*a*b*c*d - (p*(a + b) + c)         # = 0 on Type I
    out = {}
    # II{c,d}: (4cda-1)(4cdb-1) - (4c^2dp+1) should be a multiple of II
    out['II{c,d}'] = sp.simplify((4*c*d*a - 1)*(4*c*d*b - 1) - (4*c**2*d*p + 1) - 4*c*d*II)
    out['II{a,d}'] = sp.simplify((4*a*c*d - 1)*(4*a*b*d - p) - (p + 4*a**2*d) - 4*a*d*II)
    out['I{c,d}'] = sp.simplify((4*c*d*a - p)*(4*c*d*b - p) - (p**2 + 4*c**2*d) - 4*c*d*I)
    out['II{a,c}'] = sp.simplify(b*(4*a*c*d - 1) - (c*p + a) - II)
    out['I{a,c}'] = sp.simplify(b*(4*a*c*d - p) - (a*p + c) - I)
    out['I{a,b}'] = sp.simplify(c*(4*a*b*d - 1) - p*(a + b) - I)
    out['I{a,d}'] = sp.simplify((4*a*c*d - p)*(4*a*b*d - 1) - p*(4*a**2*d + 1) - 4*a*d*I)
    return out

def divisors(n):
    ds = [1]; m = n; q = 2
    while q * q <= m:
        if m % q == 0:
            e = 0
            while m % q == 0: m //= q; e += 1
            ds = [x * q**k for x in ds for k in range(e + 1)]
        q += 1
    if m > 1: ds = ds + [x * m for x in ds]
    return ds

def solve_lin(num, den):
    """positive integer solutions v = num/den (arrays), mask"""
    ok = (den > 0) & (num > 0) & (num % np.where(den > 0, den, 1) == 0)
    return ok

# ---- direct slice counters (all positive integer solutions, ordered, no gcd conditions) ----
def cnt_II_ac(p, a, c):
    D = np.arange(1, (a + c*p + 1)//(4*a*c) + 2, dtype=np.int64)
    num = a + c*p; den = 4*a*c*D - 1
    ok = solve_lin(num, den); b = num // np.where(den > 0, den, 1)
    ok &= (4*a*b*c*D == a + b + c*p)
    return int(ok.sum())
def cnt_II_ad(p, a, d):
    C = np.arange(1, a + (p + a)//(4*a*d - 1) + 2, dtype=np.int64)
    num = C*p + a; den = 4*a*C*d - 1
    ok = solve_lin(num, den); b = num // np.where(den > 0, den, 1)
    ok &= (4*a*b*C*d == a + b + C*p)
    return int(ok.sum())
def cnt_II_cd(p, c, d):
    A = np.arange(1, (c*p + 1)//(4*c*d - 1) + 2, dtype=np.int64)
    num = A + c*p; den = 4*A*c*d - 1
    ok = solve_lin(num, den); b = num // np.where(den > 0, den, 1)
    ok &= (4*A*b*c*d == A + b + c*p)
    return int(ok.sum())
def cnt_II_ab(p, a, b):
    n = 0
    for d in range(p//(4*a*b) + 1, (p + a + b)//(4*a*b) + 2):
        k = 4*a*b*d - p
        if k >= 1 and (a + b) % k == 0:
            cc = (a + b)//k; n += (4*a*b*cc*d == a + b + cc*p)
    return n
def cnt_I_cd(p, c, d):
    # unordered-min bound: min(a,b) <= (p + sqrt(p^2+4c^2d))/(4cd) (from the symbolically checked I{c,d} identity)
    A0 = int((p + math.isqrt(p*p + 4*c*c*d) + 1)//(4*c*d)) + 2
    A = np.arange(1, A0 + 1, dtype=np.int64)
    num = p*A + c; den = 4*A*c*d - p
    ok = solve_lin(num, den); b = num // np.where(den > 0, den, 1)
    ok &= (4*A*b*c*d == p*(A + b) + c) & (b >= A)
    return int(2*ok.sum() - (ok & (b == A)).sum())
def cnt_I_ac(p, a, c):
    D = np.arange(1, (p*(a + 1) + c)//(4*a*c) + 2, dtype=np.int64)
    num = p*a + c; den = 4*a*c*D - p
    ok = solve_lin(num, den); b = num // np.where(den > 0, den, 1)
    ok &= (4*a*b*c*D == p*(a + b) + c)
    return int(ok.sum())
def cnt_I_ad(p, a, d):
    C = np.arange(1, p*(a + 1)//(4*a*d - 1) + 2, dtype=np.int64)
    num = p*a + C; den = 4*a*C*d - p
    ok = solve_lin(num, den); b = num // np.where(den > 0, den, 1)
    ok &= (4*a*b*C*d == p*(a + b) + C)
    return int(ok.sum())
def cnt_I_ab(p, a, b):
    D = np.arange(1, (p*(a + b) + 1)//(4*a*b) + 2, dtype=np.int64)
    num = p*(a + b); den = 4*a*b*D - 1
    ok = solve_lin(num, den); c = num // np.where(den > 0, den, 1)
    ok &= (4*a*b*c*D == p*(a + b) + c)
    return int(ok.sum())
def cnt_e(p, e, typ):
    M = p + e if typ == 'II' else p*e + 1
    if M % 4: return 0
    N = M // 4; n = 0
    for a in divisors(N):
        for b in divisors(N // a):
            if (a + b) % e == 0:
                d = N // (a*b); c = (a + b)//e
                lhs = 4*a*b*c*d
                n += (lhs == (a + b + c*p) if typ == 'II' else lhs == p*(a + b) + c)
    return n

# slice spec: (name, counter, q, N1, Np(p) or None)
def spec(kind, x, y):
    if kind == 'IIac': return (f'II{{a,c}}=({x},{y})', lambda p: cnt_II_ac(p, x, y), 4*x*y, x + y, lambda p: y*p + x)
    if kind == 'IIad': return (f'II{{a,d}}=({x},{y})', lambda p: cnt_II_ad(p, x, y), 4*x*y, 1 + 4*x*x*y, lambda p: p + 4*x*x*y)
    if kind == 'IIcd': return (f'II{{c,d}}=({x},{y})', lambda p: cnt_II_cd(p, x, y), 4*x*y, 1 + 4*x*x*y, lambda p: 4*x*x*y*p + 1)
    if kind == 'IIab': return (f'II{{a,b}}=({x},{y})', lambda p: cnt_II_ab(p, x, y), 4*x*y, 1, None)
    if kind == 'Icd': return (f'I{{c,d}}=({x},{y})', lambda p: cnt_I_cd(p, x, y), 4*x*y, 1 + 4*x*x*y, lambda p: p*p + 4*x*x*y)
    if kind == 'Iac': return (f'I{{a,c}}=({x},{y})', lambda p: cnt_I_ac(p, x, y), 4*x*y, x + y, lambda p: x*p + y)
    if kind == 'Iad': return (f'I{{a,d}}=({x},{y})', lambda p: cnt_I_ad(p, x, y), 4*x*y, 1, None)
    if kind == 'Iab': return (f'I{{a,b}}=({x},{y})', lambda p: cnt_I_ab(p, x, y), 4*x*y, 1, None)
    if kind == 'IIe': return (f'II e={x}', lambda p: cnt_e(p, x, 'II'), x, (1 + x)//4, lambda p: (p + x)//4 if (p + x) % 4 == 0 else None)
    if kind == 'Ie': return (f'I e={x}', lambda p: cnt_e(p, x, 'I'), x, (1 + x)//4, lambda p: (p*x + 1)//4 if (p*x + 1) % 4 == 0 else None)

def cofactors_prime(p, Theta):
    for (_, _, q, N1, Np) in Theta:
        if Np is None: continue
        v = Np(p)
        if v is None or v % N1 or not isprime(v // N1): return False
    return True

def run(label, Theta, Q=None, nprimes=4, ncontrols=3, pmax=3 * 10**7):
    if Q is None:
        Q = 1
        for (_, _, q, N1, _) in Theta: Q = math.lcm(Q, q * N1)
    hits, ctrl = [], []
    t = 1
    while (len(hits) < nprimes or len(ctrl) < ncontrols) and 1 + Q*t <= pmax:
        p = 1 + Q*t; t += 1
        if not isprime(p): continue
        if cofactors_prime(p, Theta):
            if len(hits) < nprimes: hits.append(p)
        elif len(ctrl) < ncontrols and p > 1000: ctrl.append(p)
    print(f'== {label}: Q = {Q}')
    for p in hits:
        print('  shadow p', p, {n: f(p) for (n, f, *_ ) in Theta})
    for p in ctrl:
        print('  control p (some P composite)', p, {n: f(p) for (n, f, *_ ) in Theta})
    sys.stdout.flush()

if __name__ == '__main__':
    print('symbolic residues (all must be 0):', sym_checks())
    # sanity of the direct counters: total over all slices is not tested here; spot check vs brute ES for small p
    run('II{a,d} (1,1)', [spec('IIad', 1, 1)])
    run('II{a,d} (2,1)', [spec('IIad', 2, 1)])
    run('II{a,d} (1,3)', [spec('IIad', 1, 3)])
    run('II{a,d} (3,2)', [spec('IIad', 3, 2)], pmax=10**9)
    run('I{c,d} (1,1)', [spec('Icd', 1, 1)])
    run('I{c,d} (1,2)', [spec('Icd', 1, 2)])
    run('I{c,d} (2,1)', [spec('Icd', 2, 1)])
    run('I{a,b} (1,1)', [spec('Iab', 1, 1)])
    run('I{a,b} (1,2)', [spec('Iab', 1, 2)])
    run('I{a,b} (2,3)', [spec('Iab', 2, 3)])
    run('I{a,b} (3,5)', [spec('Iab', 3, 5)])
    run('II{a,c} (1,2)', [spec('IIac', 1, 2)])
    run('II{c,d} (1,2)', [spec('IIcd', 1, 2)])
    run('II{a,b} (2,3)', [spec('IIab', 2, 3)])
    run('I{a,c} (2,1)', [spec('Iac', 2, 1)])
    run('I{a,d} (1,2)', [spec('Iad', 1, 2)])
    run('II e=7 (Q = e*N(1) = 14, literal)', [spec('IIe', 7, 0)])
    run('I e=11 (Q = e*N(1) = 33, literal)', [spec('Ie', 11, 0)])
    run('combo', [spec('IIad', 1, 1), spec('Icd', 1, 1), spec('Iab', 1, 2), spec('IIac', 1, 1), spec('IIe', 3, 0)], pmax=10**9, nprimes=2, ncontrols=2)

def crosscheck(ps):
    """alternative loop variable for II{a,d}, I{c,d}, I{a,b} (pure-Python), must equal the numpy counters"""
    bad = 0
    for p in ps:
        for (a, d) in [(1, 1), (2, 1), (1, 3)]:
            n = 0
            for b in range(1, (p + a)//(4*a*d - 1) + 2):          # c(4abd - p) = a + b
                k = 4*a*b*d - p
                if k >= 1 and (a + b) % k == 0: n += 1
            bad += n != cnt_II_ad(p, a, d)
        for (c, d) in [(1, 1), (1, 2), (2, 1)]:
            n = 0
            for a in range(1, p*p + 3):                              # loop a; max(a) <= (p^2+4c^2d+p)/(4cd) < p^2+3
                den = 4*a*c*d - p
                if den > 0 and (p*a + c) % den == 0: n += 1
            bad += n != cnt_I_cd(p, c, d)
        for (a, b) in [(1, 1), (1, 2), (2, 3)]:
            n = 0
            for c in range(1, p*(a + b) + 1):                        # loop c, d from 4abcd = p(a+b)+c
                if (p*(a + b) + c) % (4*a*b*c) == 0: n += 1
            bad += n != cnt_I_ab(p, a, b)
    return bad
