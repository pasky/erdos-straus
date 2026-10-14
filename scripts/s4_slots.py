r"""s4_slots: for odd non-square n = 1 (mod 8), compare the actual existence of a signed chi=-1 word with given t
(|t| in {1,2,3,4,6}) with the predicted genus condition on |t|n +- 1 (SYNTHESIS_SPARKS4 §2.3):
 t=1: n+1 has a prime q=3(4); t=-1: never; t=2: 2n+1 has q=5,7(8); t=-2: 2n-1 has q=3,5(8);
 t=3: 3n+1 has odd q=2(3); t=-3: 3n-1 has q=5,7(12); t=4: 4n+1 has q=3(4); t=-4: never;
 t=6: 6n+1 has q with (-6/q)=-1; t=-6: 6n-1 has q with (6/q)=-1.     usage: s4_slots.py N"""
import sys
from math import isqrt
from sympy import factorint, jacobi_symbol as J

def actual(n, t):
    M = t * n + 1
    ds = [1]
    for q, e in factorint(abs(M)).items(): ds = [d * q ** k for d in ds for k in range(e + 1)]
    for a in ds:
        for A in (a, -a):
            B = M // A
            if A == -1 or B == -1 or (A + 1) % t or (B + 1) % t: continue
            if (A + 1) // t == 0 or (B + 1) // t == 0: continue
            if J(-A % n, n) == -1: return True
    return False

pred = {1: lambda q: q % 4 == 3, -1: lambda q: False, 2: lambda q: q % 8 in (5, 7), -2: lambda q: q % 8 in (3, 5),
        3: lambda q: q % 3 == 2, -3: lambda q: q % 12 in (5, 7), 4: lambda q: q % 4 == 3, -4: lambda q: False,
        6: lambda q: J(-6 % q, q) == -1, -6: lambda q: J(6, q) == -1}
N = int(sys.argv[1]); bad = 0; cnt = 0
for n in range(9, N + 1, 8):
    if isqrt(n) ** 2 == n: continue
    cnt += 1
    for t, f in pred.items():
        p = any(f(q) for q in factorint(abs(t * n + 1)) if q > 2)
        if p != actual(n, t): bad += 1; print("mismatch", n, t, p)
print(f"n = 1 (8) non-squares <= {N}: {cnt}; slot mismatches: {bad}")
