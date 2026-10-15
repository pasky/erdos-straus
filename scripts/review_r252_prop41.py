"""R252: brute check of the Jacobi core of Prop 4.1.
Claim: m = 3 (4), N0 = 4^i + m, d = D*2^e (D odd positive, all primes of D divide N0), d == -4^{i-1} (mod m)
  ==> m = 3 (mod 8) and e odd.  Also test negative D (sign gap): -D*2^e == -4^{i-1}."""
from sympy import factorint
bad_pos, bad_neg = [], []
for i in (1, 2, 3):
    for m in range(3, 3000, 4):
        N0 = 4**i + m
        ps = list(factorint(N0))
        divs = [1]
        for q in ps:
            divs = [d*q**k for d in divs for k in range(4)]
        tgt = (-pow(4, i-1, m)) % m
        for D in divs:
            for e in range(-6, 7):
                v = (D * pow(2, e, m)) % m if e >= 0 else (D * pow(pow(2, -e, m), -1, m)) % m
                if v == tgt and not (m % 8 == 3 and e % 2 == 1):
                    bad_pos.append((i, m, D, e))
                if (-v) % m == tgt and m % 8 == 7:
                    bad_neg.append((i, m, -D, e))
print("counterexamples (positive d):", bad_pos[:10], len(bad_pos))
print("negative d with m = 7 mod 8 firing (would break Prop 4.1 if atoms could be negative at rho):", bad_neg[:5], len(bad_neg))
