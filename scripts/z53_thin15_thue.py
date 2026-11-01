# z53_thin15_thue.py — menu B' (II-cd) at mu = 0 of 15*2^s+1 reduces (Z53_THIN15.md Prop 8) to
#   15 r^p - v^p = h, h in {1,3,5,15}, v even, r odd, gcd(r,v)=1    (u = r/v, p odd prime)
#   r^4 - 13500 k^4 = 1, k even, k >= 1                               (Sophie-Germain shape)
# Solved with PARI thue via cypari2; thueinit(...,1) = unconditional (no GRH).  Usage: z53_thin15_thue.py PMIN PMAX [SG]
import sys, time, cypari2
pari = cypari2.Pari(); pari.allocatemem(3 * 10**9)
PMIN, PMAX = int(sys.argv[1]), int(sys.argv[2])
for p in [int(q) for q in pari.primes([PMIN, PMAX])]:
    if p < 3: continue
    t0 = time.time()
    T = pari('thueinit(15*x^%d - 1, 1)' % p)
    for h in (1, 3, 5, 15):
        S = pari.thue(T, h)
        good = [(int(s[0]), int(s[1])) for s in S]
        relevant = [(r, v) for (r, v) in good if r > 0 and v > 0 and v % 2 == 0]
        print('p=%d h=%d all integer solutions %s ; with r,v>0, v even: %s' % (p, h, good, relevant), flush=True)
    print('   p=%d done in %.1fs' % (p, time.time() - t0), flush=True)
if len(sys.argv) > 3:
    T = pari('thueinit(x^4 - 13500, 1)')
    print('SG: r^4 - 13500 k^4 = 1: all integer solutions', pari.thue(T, 1))
