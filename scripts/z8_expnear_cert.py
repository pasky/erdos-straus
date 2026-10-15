# z8_expnear_cert.py — certify ES for all n = c0*4^s + k (exponential near-squares, m = 2^s):
# search a covering (ec_cover.search, base 4), write data/z8/cert_c{c0}_k{k}.json, run the independent
# checker ec_cert.main (identity, integrality, positivity, periodicity, exact check to s = MMAX, brute force below m0,
# T1 control).  Usage: PYTHONPATH=scripts uv run python scripts/z8_expnear_cert.py c0 k Mmax MMAX L1 L2 ...
import sys, os, json, functools
import mordell_lib as ML
import ec_cover as EC
import ec_cert
ML.residue_table = functools.lru_cache(maxsize=4000)(ML.residue_table)
c0, k, Mmax, MMAX = map(int, sys.argv[1:5])
for L in [int(x) for x in sys.argv[5:]]:
    ch = EC.search(c0, L, Mmax, 4, k, verbose=False)
    if ch:
        break
else:
    print('c0=%d k=%d: no covering found' % (c0, k)); sys.exit(1)
os.makedirs('data/z8', exist_ok=True)
path = 'data/z8/cert_c%d_k%d.json' % (c0, k)
json.dump(EC.certificate(c0, L, ch, 4, k), open(path, 'w'))
ec_cert.main(path, MMAX)
