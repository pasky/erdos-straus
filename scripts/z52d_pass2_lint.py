"""Lint Pass-2 outcome records for the audit's failure patterns (z52d).
Usage: python3 scripts/z52d_pass2_lint.py <outcome.jsonl> [batch.jsonl]  -> prints flagged mids with reasons.
Flags: step-not-done records (summary opens with 'Not done'/'Did not'/...), stub summaries (< 90 chars),
'covered' without a depth citation (only z52b lane lists / TODO / no file), missing input lines, duplicates."""
import json, re, sys
LAZY = re.compile(r'^\s*(Not done|Did not|Not run|Not performed|Not enumerated|Not computed|Not checked|Not read|Not attempted)', re.I)
LANES = re.compile(r'BRAINSTORM/z52b_(signature|upgrades|fingerprint|analogues|translate|dividing|free_\w+|tools)\.md')
def flags(r):
    s = r.get('summary', '')
    out = []
    if LAZY.search(s) or re.search(r'\bNot done\b', s[:120]):
        out.append('step-not-done')
    if len(s) < 90:
        out.append('stub')
    if r.get('outcome') == 'covered':
        txt = ' '.join(r.get('evidence', [])) + ' ' + s
        files = set(re.findall(r'[A-Za-z0-9_./-]+\.(?:md|py|json|jsonl|txt|lean|c)', txt))
        if not [f for f in files if not LANES.fullmatch(f) and 'ES_CONNECTIONS_TODO' not in f and 'master.jsonl' not in f]:
            out.append('covered-no-depth-cite')
    return out
if __name__ == '__main__':
    rs = [json.loads(l) for l in open(sys.argv[1]) if l.strip()]
    seen = {}
    for r in rs:
        seen[r['mid']] = seen.get(r['mid'], 0) + 1
    bad = {r['mid']: flags(r) for r in rs if flags(r)}
    for m, c in seen.items():
        if c > 1:
            bad.setdefault(m, []).append(f'duplicate x{c}')
    if len(sys.argv) > 2:
        want = [json.loads(l)['mid'] for l in open(sys.argv[2]) if l.strip()]
        for m in want:
            if m not in seen:
                bad[m] = ['missing']
    for m in sorted(bad):
        print(m, ','.join(bad[m]))
    print(f'# {len(bad)} flagged of {len(rs)}', file=sys.stderr)
