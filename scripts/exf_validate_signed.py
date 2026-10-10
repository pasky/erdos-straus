"""O131: brute-force validation (n<=M) of the engine for both signs:
T1+: 4abcd = n(a+b)+c ; T1-: 4abcd + c = n(a+b) ; T2+: 4abcd = a+b+nc ; T2-: 4abcd + a + b = nc ; a<=b."""
import numpy as np
from exf_load import load_full
M, N = 120, 20000
def brute(n):
    t1p = t1m = t2p = t2m = 0
    for a in range(1, 2*n+2):
        for d in range(1, 2*n+2):
            if 4*a*d > 2*n + 1 + 4*d: break
            for c in range(1, 4*n*n):
                g = 4*a*c*d - n
                if 4*a*c*d > 2*n + c/a: break
                if g >= 1:
                    if (n*a + c) % g == 0 and (n*a + c)//g >= a: t1p += 1
                    if n*a - c > 0 and (n*a - c) % g == 0 and (n*a - c)//g >= a: t1m += 1
    for a in range(1, n+1):
        for b in range(a, 4*n*n):
            if 4*a*b > n + a + b: break
            for d in range(1, n+1):
                if 4*a*b*d > n + a + b: break
                e = 4*a*b*d - n
                if e >= 1 and (a+b) % e == 0: t2p += 1
                e = n - 4*a*b*d
                if e >= 1 and (a+b) % e == 0: t2m += 1
    return t1p, t1m, t2p, t2m
B = np.array([brute(n) for n in range(M+1)])
for pre, col in (('n2e4', (0, 2)), ('m2e4', (1, 3))):
    T1, T2 = load_full('data/exf/'+pre, N)
    e1 = np.bincount(T1['n'][T1['n'] <= M], minlength=M+1); e2 = np.bincount(T2['n'][T2['n'] <= M], minlength=M+1)
    print(pre, 'T1 ok', np.array_equal(e1, B[:, col[0]]), 'T2 ok', np.array_equal(e2, B[:, col[1]]))
