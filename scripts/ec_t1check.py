# ec_t1check.py — T1 control: no ET class (mordell_lib, all seven families) of modulus M <= Mmax contains an odd square.
import sys
import mordell_lib as ML
Mmax = int(sys.argv[1]); bad = 0; ncl = 0
for M in range(3, Mmax + 1):
    if M % 4 not in (0, 3):
        continue
    sq = {(s * s) % M for s in range(1, 2 * M, 2)}
    for fam, P in ML.iter_classes(M):
        ncl += 1
        R = ML.cls_modulus_residues(fam, P)[1]
        if sq & set(R):
            bad += 1; print('BAD', M, fam, P)
print('classes checked', ncl, 'bad', bad)
