"""O131: validate exf_engine dumps (a) against spec_typecount f_I/f_II (gcd-filtered), (b) brute force n<=150."""
import numpy as np, sys
from exf_load import load, gcd_arr, expand_T1
N = 20000
T1, T2 = load('data/exf/n2e4')
# (a)
g1 = gcd_arr(gcd_arr(T1['a'], T1['b']), T1['c'])
fI = np.bincount(T1['n'][g1 == 1], minlength=N+1)
g2 = gcd_arr(gcd_arr(T2['a'], T2['b']), T2['c'])
ok2 = (g2 == 1) & (gcd_arr(T2['a'], T2['n'])==1) & (gcd_arr(T2['b'].astype(np.int64) % T2['n'], T2['n'])==1) & (gcd_arr(T2['d'], T2['n'])==1)
fII = np.bincount(T2['n'][ok2], minlength=N+1)
FI = np.fromfile('/tmp/exf/s.FI.bin', dtype='<u4'); FII = np.fromfile('/tmp/exf/s.FII.bin', dtype='<u4')
print('fI match', np.array_equal(fI, FI), 'fII match', np.array_equal(fII, FII))
# (b) brute force: 4abcd = n(a+b)+c  and 4abcd = a+b+nc, a<=b.
M = 150
t1 = np.bincount(T1['n'][T1['n'] <= M], minlength=M+1); t2 = np.bincount(T2['n'][T2['n'] <= M], minlength=M+1)
b1 = np.zeros(M+1, int); b2 = np.zeros(M+1, int)
for n in range(1, M+1):
    # Type I: for (c,d), X=4cd a-n, Y=4cd b-n, XY=n^2+4c^2 d, X<=Y, X>0 (shown positive). bound: X>=4cd-n, so 4cd-n <= n (X<=sqrt) roughly; brute in c,d with 4cd <= n + sqrt(n^2+4c^2d)
    for c in range(1, M+2):
        for d in range(1, 4*M):
            q = 4*c*d; m = n*n + 4*c*c*d
            if (q - n)**2 > m and q > n: break
            X0 = (-n) % q or q
            for X in range(X0, int(m**0.5)+1, q):
                if m % X == 0 and (m//X + n) % q == 0: b1[n] += 1
            # Type II: (qa-1)(qb-1) = q c n + 1
            m2 = q*c*n + 1
            if (q-1)**2 <= m2:
                for X in range(q-1, int(m2**0.5)+1, q):
                    if m2 % X == 0 and (m2//X + 1) % q == 0: b2[n] += 1
T1 = expand_T1(T1, N); t1 = np.bincount(T1['n'][T1['n'] <= M], minlength=M+1)
print('brute T1 match', np.array_equal(b1, t1), 'T2 match', np.array_equal(b2, t2))
bad = np.nonzero(b1 != t1)[0]; print('T1 mismatches at n =', bad[:20], 'brute', b1[bad[:20]], 'engine', t1[bad[:20]])
