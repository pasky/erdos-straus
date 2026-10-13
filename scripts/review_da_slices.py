"""review_da_slices.py (R178, from scratch): check the slicing identities of DEPTH_ASPECT §1 (table 1.1) on all
Type I / Type II parameter tuples of small primes n:
  Type I : 4abd = tn+1, ct = a+b;  claim f := 4acd - n satisfies f | n^2 + 4c^2 d and f = -n mod 4cd.
  Type II: 4abd = n+e,  ce = a+b;  claim f = 4acd-1, f' = 4bcd-1 satisfy ff' = 1 + 4c^2 d n.
Also: Type II forces e <= (n+4)/3 (used by review_da_qpow.py)."""
from sympy import primerange, divisors

bad = 0; cnt = 0
for n in primerange(5, 400):
    for t in range(1, 9 * n * n // 2 + 2):          # complete Type I bound (see review_da_qpow.py)
        if (t * n + 1) % 4: continue
        M = (t * n + 1) // 4
        for a in divisors(M):
            for b in divisors(M // a):
                if (a + b) % t: continue
                d = M // (a * b); c = (a + b) // t; f = 4 * a * c * d - n; cnt += 1
                if f <= 0 or (n * n + 4 * c * c * d) % f or (f + n) % (4 * c * d): bad += 1; print("I bad", n, t, a, b, c, d, f)
    for e in range(1, 2 * n):
        if (n + e) % 4: continue
        M = (n + e) // 4
        for a in divisors(M):
            for b in divisors(M // a):
                if (a + b) % e: continue
                d = M // (a * b); c = (a + b) // e; cnt += 1
                if e > (n + 4) // 3: bad += 1; print("II e-bound violated", n, e)
                if (4*a*c*d - 1) * (4*b*c*d - 1) != 1 + 4 * c * c * d * n: bad += 1; print("II bad", n, e, a, b)
print("tuples checked", cnt, "violations", bad)
