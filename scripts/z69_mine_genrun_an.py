# Coverage table for z69_mine_genrun.py outputs: per generator, fraction of primes with >= 1 word (real), decoy
# coverage, real coverage using non-Lambda letters only (K5), paired McNemar z (real vs decoy), mean #candidates.
import sys, json, math
GENS = ['G', 'N', 'J', 'Q', 'A', 'C', 'ALL'] + (['A_a', 'A_b', 'A_c', 'A_d', 'A_e', 'A_g', 'Apen', 'Anopen'] if '--splitA' in sys.argv else [])
for fn in [a for a in sys.argv[1:] if not a.startswith('--')]:
    R = [json.loads(l) for l in open(fn)]
    n = len(R)
    print('%s: %d inputs' % (fn.split('/')[-1], n))
    for g in GENS:
        real = sum(r['res'][g][1] for r in R); dec = sum(r['res'][g][2] for r in R); nl = sum(r['res'][g][3] for r in R)
        b = sum(1 for r in R if r['res'][g][1] and not r['res'][g][2]); c = sum(1 for r in R if r['res'][g][2] and not r['res'][g][1])
        z = (b - c) / math.sqrt(b + c) if b + c else 0.0
        nc = sum(r['res'][g][0] for r in R) / n
        print('   %-4s cand/prime %6.1f  real %.4f  decoy %.4f  real non-Lambda %.4f  McNemar z %+.2f  failures %d' % (
            g, nc, real / n, dec / n, nl / n, z, n - real))
