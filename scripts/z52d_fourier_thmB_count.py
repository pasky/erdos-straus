"""Counts Theorem B windows in a scan (forced prime q, (q−1)/2 prime, obstructed, H = G) and large-box statistics."""
import sys, json, gzip
from collections import Counter
from z52d_fourier_lib import isprime
n = 0; qs = {}; bigM = 0; absc = Counter(); minabs = (9, None)
st = {t: [0, 0, 0, 0] for t in (1, 2, 4)}
for l in gzip.open(sys.argv[1], 'rt'):
    r = json.loads(l); q = r['e']
    if r['prime_e'] and r['forced'] and r['type'] != 'ok' and r['Hfull'] and isprime((q - 1) // 2):
        n += 1; qs.setdefault(q, (r['p'], r['M'])); bigM += r['M'] >= q - 1
        a = abs(r['c_jac']); absc[round(1 / a)] += 1
        if (q - 1) // 2 > 24 and a < minabs[0]: minabs = (a, (r['p'], q))
    if r['forced'] and r['Hfull']:
        for t in st:
            if r['M'] >= t * r['phi']:
                s = st[t]; s[0] += 1
                if r['type'] != 'ok':
                    s[1] += 1; s[2] += (r['mx12'] or -1) >= 0.1; s[3] += (r['mxo12'] or -1) >= 0.1
print('Thm B windows', n, 'distinct q', len(qs), 'max q', max(qs), qs[max(qs)], 'with M >= |G|:', bigM)
print('  1/|c(chi_-q)| distribution', sorted(absc.items()), ' min |c| with (q-1)/2 > 24:', minabs)
for t, s in st.items():
    print(f'forced H=G windows with M >= {t}·φ: {s[0]}, obstructed {s[1]}; L(12,.1) holds all {s[2]/max(1,s[1]):.2f} odd {s[3]/max(1,s[1]):.2f}')
