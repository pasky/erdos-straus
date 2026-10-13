# ec_batch.py — produce certificates for a list of (k, L, Mmax) and run the independent checker on each (subprocess).
import sys, json, subprocess, functools
import mordell_lib as ML
import ec_cover as EC
ML.residue_table = functools.lru_cache(maxsize=4000)(ML.residue_table)
JOBS = [(1, 12, 1000), (9, 72, 470000), (21, 12, 1000), (27, 12, 1000), (57, 60, 3000), (231, 84, 20000),
        (315, 420, 100000), (393, 132, 150000), (171, 36, 300000), (495, 396, 220000)]
for k, L, Mmax in JOBS:
    ch = EC.search(k, L, Mmax, verbose=False)
    if not ch:
        print(k, 'no covering found'); continue
    path = '../data/ec/cert_k%d.json' % k
    json.dump(EC.certificate(k, L, ch), open(path, 'w'))
    out = subprocess.run(['uv', 'run', 'python', 'ec_cert.py', path, '2000'], capture_output=True, text=True)
    print(k, L, len(ch), (out.stdout + out.stderr).strip().splitlines()[0][:150], flush=True)
