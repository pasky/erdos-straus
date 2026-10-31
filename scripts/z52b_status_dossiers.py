"""Build per-item dossiers (item text + top repo files by TF-IDF) for status classification."""
import json, glob, re, os, sys
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import linear_kernel
import numpy as np
files = [f for f in sorted(glob.glob('*.md') + glob.glob('BRAINSTORM/*.md'))
         if not f.startswith('BRAINSTORM/z52b_') and f not in ('ES_CONNECTIONS_TODO.md',)]
docs, heads = [], []
for f in files:
    t = open(f, errors='ignore').read()
    docs.append(t[:20000])
    lines = [l.strip() for l in t.splitlines() if l.strip()][:4]
    heads.append(' | '.join(lines)[:300])
items = [json.loads(l) for l in open('data/z52b/master.jsonl')]
itext = [f"{it['title']} {it['connection']} {' '.join(it['tags'])}" for it in items]
vec = TfidfVectorizer(stop_words='english', sublinear_tf=True, min_df=2, max_df=0.5, ngram_range=(1, 2), max_features=200000)
X = vec.fit_transform(docs + itext)
D, I = X[:len(docs)], X[len(docs):]
S = linear_kernel(I, D)
out = []
for k, it in enumerate(items):
    top = np.argsort(-S[k])[:6]
    cands = [{'file': files[j], 'score': round(float(S[k, j]), 3), 'head': heads[j]} for j in top]
    seen = [t[5:] for t in it['tags'] if t.startswith('seen:')]
    out.append({'mid': it['mid'], 'title': it['title'], 'connection': it['connection'], 'first_step': it['first_step'],
                'lane_seen_tags': seen, 'candidate_files': cands})
n = int(sys.argv[1]) if len(sys.argv) > 1 else 8
chunk = (len(out) + n - 1) // n
for b in range(n):
    with open(f'data/z52b/status/dossier_{b:02d}.jsonl', 'w') as fh:
        for r in out[b*chunk:(b+1)*chunk]:
            fh.write(json.dumps(r, ensure_ascii=False) + '\n')
print(len(files), 'files;', len(out), 'items;', n, 'chunks of', chunk)
