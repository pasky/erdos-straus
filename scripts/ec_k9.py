# ec_k9.py — two-level exponent covering for n = 9*2^m + 1: L0 = 72 covering except m = 41 (mod 72), then refine to L = 25848.
import sys, json, functools
import mordell_lib as ML
import ec_cover as EC
ML.residue_table = functools.lru_cache(maxsize=None)(ML.residue_table)
k, L0, L = 9, 72, 25848
Mmax = int(sys.argv[1]) if len(sys.argv) > 1 else 400000
ch0 = EC.search(k, L0, 300000, restrict=(L0, set(range(L0)) - {41}), verbose=False)
print('level-72 part:', len(ch0), 'classes')
ch1 = EC.search(k, L, Mmax, restrict=(L0, {41}), verbose=True, Mfilter=lambda M: M % 241 == 0 or M % 433 == 0 or M % 38737 == 0)
if ch1 is None:
    sys.exit('refinement failed')
# lift level-72 classes to level L
lift = []
for M, cls, s in ch0:
    S = sorted({m for m in range(L) if m % L0 in set(s)})
    lift.append((M, cls, S))
cert = EC.certificate(k, L, lift + ch1)
json.dump(cert, open('../data/ec/cert_k9.json', 'w'))
print('written', len(cert['classes']), 'classes')
