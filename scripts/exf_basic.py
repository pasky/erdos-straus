"""O131: basic counts T1, T2 (full algebraic, a<=b, no gcd), f_I-type with gcd(a,b,c)=1; square sanity."""
import numpy as np, sys
from exf_load import load_full, gcd_arr
N = int(sys.argv[1]) if len(sys.argv) > 1 else 20000
T1, T2 = load_full('data/exf/n2e4', N)
t1 = np.bincount(T1['n'], minlength=N+1); t2 = np.bincount(T2['n'], minlength=N+1)
sq = [m*m for m in range(1, int(N**0.5)+1)]
print('odd squares T1:', [(s, t1[s]) for s in sq if s % 2][:12])
print('odd squares T2:', [(s, t2[s]) for s in sq if s % 2][:12])
print('even squares T1,T2:', [(s, t1[s], t2[s]) for s in sq if s % 2 == 0][:10])
print('first n: T1', t1[1:41].tolist()); print('first n: T2', t2[1:41].tolist())
np.save('data/exf/t1_2e4.npy', t1); np.save('data/exf/t2_2e4.npy', t2)
