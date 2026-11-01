"""Shared loader for z52d rank_O (reviewer O)."""
import json, glob, os
ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
AV = os.path.join(ROOT, 'data/z52d/avenue')
OUT = os.path.join(AV, 'rank_O')

def load_rows():
    rows = []
    for f in sorted(glob.glob(os.path.join(AV, 'out_*.jsonl'))):
        b = os.path.basename(f)[4:-6]
        if b == 'PILOTH':
            continue  # Haiku calibration replica
        for l in open(f):
            l = l.strip()
            if l:
                r = json.loads(l); r['_batch'] = b; rows.append(r)
    return rows

def load_master():
    m = {}
    for l in open(os.path.join(ROOT, 'data/z52b/master.jsonl')):
        if l.strip():
            r = json.loads(l); m[r['mid']] = r
    return m

NEG = {'circular', 'known-false', 'harder-than-open'}

def is_none_ing(s):
    return str(s).strip().lower().startswith('none')
