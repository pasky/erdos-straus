"""O131: build ES-variant columns and classical arithmetic columns for n <= N (int64), save npz."""
import numpy as np
from exf_load import load_full, gcd_arr
N = 20000
H = np.fromfile('data/exf/H12_1p4e6.bin', dtype='<i4').astype(np.int64)   # 12*H(D)
n = np.arange(N + 1)
ES = {}
def kron(D, m):  # Kronecker symbol (D/m) for fundamental D in {-4,-3,8,-8,5,12,...}, vectorised over m>=0
    from sympy import jacobi_symbol
    out = np.zeros(len(m), np.int64)
    for i, x in enumerate(m):
        x = int(x)
        if x == 0: continue
        out[i] = kr(D, x)
    return out
def kr(D, x):
    from sympy.ntheory import legendre_symbol
    from sympy import factorint
    r = 1
    for p, e in factorint(x).items():
        if p == 2:
            if D % 2 == 0: return 0
            s = 1 if D % 8 in (1, 7) else -1
        else:
            if D % p == 0: return 0
            s = legendre_symbol(D % p, p)
        r *= s ** e
    return r
for pre, s in (('n2e4', 'p'), ('m2e4', 'm')):
    T1, T2 = load_full('data/exf/' + pre, N)
    for fam, T in (('T1' + s, T1), ('T2' + s, T2)):
        nn = T['n'].astype(np.int64); a = T['a'].astype(np.int64); b = T['b'].astype(np.int64)
        c = T['c'].astype(np.int64); d = T['d'].astype(np.int64)
        prim = gcd_arr(gcd_arr(a, b), c) == 1
        def bc(mask=None, w=None):
            if mask is None: mask = np.ones(len(nn), bool)
            return np.bincount(nn[mask], weights=None if w is None else w[mask], minlength=N + 1).astype(np.int64)
        ES[fam] = bc(); ES[fam + '.diag'] = bc(a == b); ES[fam + '.a1'] = bc(a == 1); ES[fam + '.prim'] = bc(prim)
        for k in (1, 2, 3): ES[f'{fam}.d{k}'] = bc(d == k); ES[f'{fam}.c{k}'] = bc(c == k)
        ES[fam + '.sgn_ab'] = bc(w=(-1.0) ** ((a + b) % 2)); ES[fam + '.sgn_c'] = bc(w=(-1.0) ** (c % 2))
        ES[fam + '.sgn_d'] = bc(w=(-1.0) ** (d % 2))
        ES[fam + '.d_odd_sq'] = bc(np.isin(d, [k * k for k in range(1, 200)]))
# classical
C = {'1': np.ones(N + 1, np.int64), 'n': n.copy(), 'sq': np.isin(n, [k * k for k in range(150)]).astype(np.int64)}
C['n_even'] = (n % 2 == 0).astype(np.int64)
for k in (1, 3, 4, 8, 12, 16, 20, 24): C[f'H({k}n)'] = H[k * n]
def sumx(m, step=1, tw=None):
    out = np.zeros(N + 1, np.int64)
    for i in range(1, N + 1):
        M = m * i; xs = np.arange(-int(M ** 0.5), int(M ** 0.5) + 1)
        xs = xs[xs % step == 0]; v = H[M - xs * xs]
        out[i] = v.sum() if tw is None else (v * tw(xs)).sum()
    return out
for m in (1, 4, 8, 12, 16, 20):
    C[f'SH({m}n-x2)'] = sumx(m)
    C[f'SH({m}n-x2)(-1)^x'] = sumx(m, tw=lambda x: (-1) ** (np.abs(x) % 2))
    C[f'SH({m}n-x2)chi-4(x)'] = sumx(m, tw=lambda x: np.where(x % 2 == 0, 0, np.where(x % 4 == 1, 1, -1)))
    C[f'SH({m}n-x2)3|x'] = sumx(m, step=3)
# divisor functions
tau = np.zeros(4 * N * N // 1 if False else 1, np.int64)
def divfun(f, arr):
    from sympy import divisors
    return np.array([f(divisors(int(x))) if x > 0 else 0 for x in arr], np.int64)
C['tau'] = divfun(len, n); C['sigma'] = divfun(sum, n)
C['lambda'] = np.array([sum(min(d, x // d) for d in __import__('sympy').divisors(x)) if x > 0 else 0 for x in n], np.int64)
for D in (-4, -3, 8, -8, 5, 12, -7):
    C[f'sum chi{D}(d)'] = np.array([sum(kr(D, d) for d in __import__('sympy').divisors(x)) if x > 0 else 0 for x in n], np.int64)
for nm, f in (('tau(n+1)', n + 1), ('tau(n-1)', n - 1), ('tau(4n+1)', 4 * n + 1), ('tau(4n-1)', 4 * n - 1), ('tau(n^2+4)', n * n + 4), ('tau(n^2+1)', n * n + 1), ('tau(2n+1)', 2 * n + 1), ('tau(8n+1)', 8 * n + 1)):
    C[nm] = divfun(len, f)
np.savez_compressed('data/exf/columns_2e4.npz', **{'ES:' + k: v for k, v in ES.items()}, **{'C:' + k: v for k, v in C.items()})
print(len(ES), 'ES columns,', len(C), 'classical columns')
