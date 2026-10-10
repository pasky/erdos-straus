"""O131: check Prop 4.1 (sum over (c,d) of A_{+1} - 2 - A_{-1}  ==  2(T2- - T2+) - (diag- - diag+)) for n <= 40."""
import numpy as np
from sympy import divisors
A = np.load('data/exf/arrays_2e4.npz')
ok = True
for n in range(1, 41):
    s = 0
    for c in range(1, 400):
        for d in range(1, 4 * n + 4):
            q = 4 * c * d; N = q * c * n + 1
            if (q - 1) ** 2 > N: break
            ds = divisors(N); s += sum(1 for X in ds if X % q == 1) - 2 - sum(1 for X in ds if X % q == q - 1)
    rhs = 2 * (A['T2m'][n] - A['T2p'][n]) - (A['T2m_diag'][n] - A['T2p_diag'][n])
    ok &= (s == rhs)
print('Prop 4.1 check n<=40 (c<400):', ok)
