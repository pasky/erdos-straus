# Second engine (divisor form via PARI): for each p, R(p) = #{(C, d): d | 4Cp+1, d ≡ -1 (mod 4C)} and
# Rp = #{such pairs with d prime or (4Cp+1)/d prime}. Cross-checks lot_*.csv columns R and Rp.
import sys, cypari2, csv
pari = cypari2.Pari(); pari.allocatemem(10**9)
rows = list(csv.DictReader(open(sys.argv[1])))
sel = [r for r in rows if int(r['R']) > 0 and int(r['Rp']) == 0 and int(r['n']) > int(sys.argv[2])]
sel += [r for r in rows if int(r['n']) > int(sys.argv[2])][:5]
bad = 0
for r in sel:
    p = int(r['n']); R = Rp = 0
    for C in range(1, (p + 2) // 4 + 1):
        N = 4 * C * p + 1
        for d in pari.divisors(N):
            d = int(d)
            if (d + 1) % (4 * C) == 0:
                R += 1
                if pari.isprime(d) or pari.isprime(N // d): Rp += 1
    ok = (R == int(r['R']) and Rp == int(r['Rp']))
    bad += (not ok)
    print(p, R, Rp, 'OK' if ok else 'MISMATCH', flush=True)
print('mismatches', bad)
