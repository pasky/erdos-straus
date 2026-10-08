"""Independent check of Theorem 3.1 (MORDELL13B) with the stand-alone sympy engine of mordell_check.py
(ET coordinates rebuilt from the paper's parametrisation; does not use mordell_lib).
For each class: polynomial identity 4xyz = n(xy+yz+zx), positivity for n >= n0, and integrality of
x,y,z on the progression t + L Z with L = M (the class modulus) and t = the CRT lift of x*
(t = 1 mod M', t = 2 mod M_T).  usage: PYTHONPATH=scripts uv run python scripts/m13b_check_hit.py"""
from mordell_check import check_class, integral_on
from sympy.ntheory.modular import crt
for fam, P, M, MT in [('II3', (8, 33, 11999), 12670944, 1859), ('I2', (125, 88, 11999), 527956000, 1859)]:
    polys, n0 = check_class(fam, P)
    t = int(crt([M // MT, MT], [1, 2])[0])
    ok = integral_on(polys, t, M)
    print(fam, P, 'n0 =', n0, 'x* lift t =', t, 'integral on t+MZ:', ok)
    assert ok
