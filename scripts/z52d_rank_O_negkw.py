"""Pool-wide keyword screen of the negative pool (status in NEG, plaus 0): what does each verdict rest on?"""
import re, collections
from z52d_rank_O_common import load_rows, NEG
rows = [r for r in load_rows() if r['status'] in NEG and r['plausibility'] == 0]
def has(r, pat): return re.search(pat, (r.get('status_ref','') + ' ' + r.get('missing_theorem','') + ' ' + r.get('note','')), re.I) is not None
cats = {'cond_H_Dickson': r'Hypothesis H|under H\b|CONDITIONAL on (H|Dickson)|Dickson', 'cond_GRH': r'GRH',
        'assessment': r'Assessment', 'evidence_only': r'EVIDENCE|Pass 1', 'mordell_schinzel': r'Mordell|Schinzel',
        'T1': r'T1|odd square', 'B3': r'\bB3\b', 'privacy': r'privacy|Privacy', 'restatement': r'restatement|verbatim|literally|is \(★\)|IS ES'}
c = collections.Counter()
for r in rows:
    for k, p in cats.items():
        if has(r, p): c[(r['status'], k)] += 1
print(len(rows)); print(collections.Counter(r['status'] for r in rows))
for k in sorted(c): print(k, c[k])
