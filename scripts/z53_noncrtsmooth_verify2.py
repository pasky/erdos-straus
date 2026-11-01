# Second engine (divisor form via PARI), independent of z53_noncrtsmooth_lottery.cpp:
# R(p)   = #{(C, d): d | 4Cp+1, d ≡ -1 (mod 4C)}            (ordered (★) triples, x = d)
# Rp(p)  = # of those with d prime or (4Cp+1)/d prime;  Rbp(p) = # with both prime.
# Usage: uv run --with cypari2 python scripts/z53_noncrtsmooth_verify2.py IN.txt START STOP OUT.csv
import sys, cypari2
pari = cypari2.Pari(); pari.allocatemem(10**9)
ns = [int(l) for l in open(sys.argv[1]) if l.strip()][int(sys.argv[2]):int(sys.argv[3])]
with open(sys.argv[4], 'w') as out:
    out.write('n,R,Rp,Rbp\n')
    for p in ns:
        R = Rp = Rbp = 0
        for C in range(1, (p + 2) // 4 + 1):
            N = 4 * C * p + 1
            for d in pari.divisors(N):
                d = int(d)
                if (d + 1) % (4 * C) == 0:
                    R += 1
                    a, b = bool(pari.isprime(d)), bool(pari.isprime(N // d))
                    Rp += (a or b); Rbp += (a and b)
        out.write(f'{p},{R},{Rp},{Rbp}\n'); out.flush()
