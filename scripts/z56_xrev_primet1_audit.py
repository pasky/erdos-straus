"""Independent ledger/split/table/census audit; optional T2T refit + sandwich CI.
Run under ulimit -v 6000000 and timeout, with OPENBLAS_NUM_THREADS=2:
uv run --with numpy --with scipy python scripts/z56_xrev_primet1_audit.py \
    /home/pasky/scratch_z56_primet1 /tmp/xrev_PRIMET1 [--t2t]
The second path contains the archived reviewed scripts/data (a2f8ba5b).
No dense full-sample design or Cartesian-product allocation is used.
"""
import argparse
import csv
import math
from pathlib import Path
import subprocess
import sys

import numpy as np


def hash64(p):
    z = np.asarray(p, dtype=np.uint64) + np.uint64(0x9E3779B97F4A7C15)
    z = (z ^ (z >> 30)) * np.uint64(0xBF58476D1CE4E5B9)
    z = (z ^ (z >> 27)) * np.uint64(0x94D049BB133111EB)
    return z ^ (z >> 31)


def holm(p):
    order = sorted(range(len(p)), key=p.__getitem__)
    out = np.empty(len(p)); last = 0.0
    for j, i in enumerate(order):
        last = max(last, min(1.0, (len(p) - j) * p[i])); out[i] = last
    return out


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument('scratch', type=Path); ap.add_argument('source', type=Path)
    ap.add_argument('--t2t', action='store_true')
    a = ap.parse_args()
    sys.path.insert(0, str(a.source / 'scripts'))
    for ref in ['6ddab6c0', '345fbe79', '45c5895f', 'da4971f4', '4fa8b3a6',
                'b1d357c3', '1789ce0c', '073515c3']:
        text = subprocess.check_output(['git', 'show', ref + ':Z56_PRIMET1.md'],
                                       text=True, timeout=15)
        headers = [line for line in text.splitlines() if line.startswith('**Amendment')]
        print('LEDGER', ref, 'characters', len(text), 'amendment headers', len(headers))
    for name, mod, allowed in [('h0', 4, [0]), ('h1', 4, [1]), ('h2', 4, [2]),
                               ('h3p', 16, [7, 11, 15]), ('s3t', 16, [3]),
                               ('b2h1', 64, [1]), ('b2h3', 64, [3])]:
        d = np.load(a.scratch / f'pred_{name}.npy', mmap_mode='r')
        assert np.all(np.isin(hash64(d['p']) % np.uint64(mod), allowed))
        assert np.all(np.diff(d['p'].astype(np.int64)) > 0)
        print('SPLIT', name, len(d), int(d['p'].min()), int(d['p'].max()))
    s2 = np.load(a.scratch / 's2_setp.npy')
    b23 = np.load(a.scratch / 'pred_b2h3.npy', mmap_mode='r')['p']
    assert len(np.intersect1d(s2, b23)) == 337
    assert np.count_nonzero(hash64(s2) % np.uint64(64) == 2) == 330
    print('OVERLAPS S2/B23=337, S2/Bulk2-fit=330')
    # Recalculate multiplicity adjustments independently from rounded raw p-values.
    for path in sorted((a.source / 'data/z56/primet1').glob('*.tsv')):
        with path.open() as f:
            rows = list(csv.DictReader((s for s in f if not s.startswith('#')), delimiter='\t'))
        if not rows:
            continue
        for raw, adj in [('p_raw', 'p_holm'), ('p_robust', 'p_holm_rob')]:
            if raw not in rows[0] or adj not in rows[0]:
                continue
            p = [float(r[raw]) for r in rows]
            if not np.isfinite(p).all():
                continue
            calc = holm(p); stored = [float(r[adj]) for r in rows]
            assert np.allclose(calc, stored, rtol=0.003, atol=1e-300), path
            print('HOLM', path.name, len(rows), 'tests OK')
    dtype = np.dtype([('p', '<u8'), ('r', '<u2')])
    for name in ['r_1e8.bin', 'r_1e7_1e9.bin', 'r_1e9_1e10.bin']:
        d = np.memmap(a.scratch / name, dtype=dtype, mode='r')
        zeros = []; minimum = 65535; minimizers = []
        for st in range(0, len(d), 1000000):
            block = d[st:st + 1000000]
            zeros.extend(block['p'][block['r'] == 0].tolist())
            rmin = int(block['r'].min())
            if rmin < minimum:
                minimum = rmin; minimizers = []
            if rmin == minimum:
                minimizers.extend(block['p'][block['r'] == minimum].tolist())
        print('CENSUS', name, len(d), 'zeros', zeros, 'min', minimum, minimizers)
    assert 37379**2 + 360 == 1397190001
    if a.t2t:
        from z56_primet1_local import Design, fit
        from scipy.stats import norm
        for filename in ['s3t_rone.txt', 'high_rone.txt']:
            d = np.loadtxt(a.scratch / filename, dtype=np.int64)
            assert np.all(d[:, 1] == d[:, 2:5].sum(axis=1))
            p = d[:, 0].astype(np.uint64); train = hash64(p) % np.uint64(32) < 16
            ev = ~train; des = Design(); residuals = []; means = []; phis = []
            for col in [2, 3]:
                beta, _, phi, _ = fit(p[train], d[train, col].astype(float), des, iters=12)
                mu = np.exp(des.build(p[ev]) @ beta)
                residuals.append((d[ev, col] - mu) / np.sqrt(phi * mu))
                means.append(mu); phis.append(phi)
            x, y = [(r - r.mean()) / r.std() for r in residuals]
            rho = np.mean(x * y); n = len(x)
            influence = x*y - rho * (x*x + y*y) / 2
            se = influence.std() / math.sqrt(n)
            hi = rho + norm.ppf(0.995) * se
            sensitivity = math.sqrt(max(hi, 0) * math.sqrt(phis[0]*phis[1] /
                                 (d[ev, 2].mean()*d[ev, 3].mean())))
            print('T2T', filename, 'n', n, 'rho', rho,
                  'sandwich99', (rho - norm.ppf(0.995)*se, hi),
                  'FisherSE', 1/math.sqrt(n-3), 'sandwichSE', se,
                  'SDH_sensitivity', sensitivity,
                  '(conditional on fitted models; not a validated bound)')


if __name__ == '__main__':
    main()
