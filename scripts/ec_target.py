# ec_target.py — find an ET class (or divisor class) containing n_m for ALL large m = m* (mod L), searching moduli M that
# are multiples of a given prime q (where n_m is a quadratic non-residue).  Usage: ec_target.py k L mstar q Mmax [b c]
import sys
import mordell_lib as ML
from ec_cover import candidate_moduli
k, L, ms, q, Mmax = map(int, sys.argv[1:6])
b = int(sys.argv[6]) if len(sys.argv) > 6 else 2
c = int(sys.argv[7]) if len(sys.argv) > 7 else 1
base = 10 * L + 64
mm = base + ((ms - base) % L)
Ms = [M for M in candidate_moduli(k, b, c, L, Mmax) if M % q == 0 and (M % 4 == 0 or M % 4 == 3)]
print(len(Ms), 'moduli')
for M in Ms:
    r = (k * pow(b, mm, M) + c) % M
    for fam, P in ML.iter_classes(M):
        if r in ML.cls_modulus_residues(fam, P)[1]:
            print('FOUND M=%d %s %s' % (M, fam, P)); sys.exit()
print('none')
