# z53 NONCRTSMOOTH: fixed class modulus q threshold (Theorem B).
# For prime p and q in 4N, j(p,q) := least j >= 1 such that 4/(jp)-type equation q*u*B - u - B = j*p has a solution,
# i.e. q*j*p + 1 has a divisor x ≡ -1 (mod q) (then y = (qjp+1)/x ≡ -1 (mod q) automatically).
# Trivial CRT bound (Thm B(a)): j(p,q) <= q - 2 when p does not divide q(q-1); trivial_ok checks the CRT witness has
# cofactor in [1, q-2] and that jmin <= q-2.
# Also N_q = #{(j, x) : j <= q, x | qjp+1, x ≡ -1 (mod q)}: ordered witnesses (x,y), not distinct cofactors j.
# Usage: uv run --with cypari2 python scripts/z53_noncrtsmooth_fixedq.py OUT.csv
import sys, cypari2, math
pari = cypari2.Pari(); pari.allocatemem(2*10**9)
out = sys.argv[1]
primes = [int(pari.nextprime(10**6 + 1000*k)) for k in range(40)]
primes = [p for p in primes if p % 4 == 1][:20] + [409, 577, 5569, 9601, 23929, 83449, 102001, 329617, 712321, 8813281]
qs = [8, 12, 16, 24, 40, 60, 100, 200, 400, 1000]
rows = ['p,q,jmin,N_q4,N_q,trivial_ok']
for p in primes:
    for q in qs:
        jmin = None; cnt_q4 = 0; cnt_q = 0
        for j in range(1, q + 1):
            N = q * j * p + 1
            c = sum(1 for d in pari.divisors(N) if (int(d) + 1) % q == 0)
            if c and jmin is None: jmin = j
            if j <= max(1, q // 4): cnt_q4 += c
            cnt_q += c
        # trivial construction check: x = q-1, y ≡ -1 (q), y ≡ (q-1)^{-1} (p), y < qp
        x = q - 1
        y = int(pari.chinese(pari.Mod(-1, q), pari.Mod(pow(x, -1, p), p)).lift())
        k = (x * y - 1) // (q * p)
        ok = (x * y - 1) % (q * p) == 0 and 1 <= k <= q - 2 and jmin is not None and jmin <= q - 2
        rows.append(f'{p},{q},{jmin},{cnt_q4},{cnt_q},{int(ok)}')
    print(p, file=sys.stderr, flush=True)
open(out, 'w').write('\n'.join(rows) + '\n')
