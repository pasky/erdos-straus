#!/usr/bin/env python3
"""Reproducible independent R=A selection; stdlib only, bounded input size."""
import argparse
import collections
import hashlib
import json
import random
from pathlib import Path

BASE = Path('data/z52d/avenue')
OUT = BASE / 'rank_A'
SEED = 52041031
NEG = {'circular', 'known-false', 'harder-than-open'}


def load():
    rows = []
    for path in sorted(BASE.glob('out_*.jsonl')):
        if path.stem == 'out_PILOTH':
            continue
        for line in path.read_text().splitlines():
            row = json.loads(line)
            row['batch'] = path.stem.removeprefix('out_')
            rows.append(row)
    assert len({r['mid'] for r in rows}) == len(rows), 'duplicate source mids'
    return rows


def gates(r):
    y = r['yield'].strip().lower()
    # Literal union requested by the brief, including explanatory 'none (...)'
    # ingredient strings: these are retained, not silently interpreted away.
    return [r['plausibility'] >= 2 and r['novelty'] >= 1 and y != 'none',
            y.startswith('es') and r['status'] in {'open-plausible', 'unclear', 'known-true'} and r['plausibility'] >= 1,
            r.get('new_ingredient', 'none').strip().lower() != 'none']


def semantic_gates(r):
    """Sensitivity check only: collapse explanatory 'none (...)' to none."""
    return [r['plausibility'] >= 2 and r['novelty'] >= 1 and not r['yield'].strip().lower().startswith('none'),
            gates(r)[1],
            not r.get('new_ingredient', 'none').strip().lower().startswith('none')]


def dump(path, rows):
    path.write_text(''.join(json.dumps(r, ensure_ascii=False) + '\n' for r in rows))


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--reading', action='store_true', help='also write disposable human reading aids')
    args = parser.parse_args()
    OUT.mkdir(exist_ok=True)
    rows = load()
    strata = collections.defaultdict(list)
    for r in rows:
        if r['status'] in NEG and r['plausibility'] == 0:
            strata[r['batch']].append(r)
    rng = random.Random(SEED)
    # Equal allocation, one per nonempty batch then a random extra stratum
    # allocation without replacement. Within each stratum sample uniformly.
    names = sorted(strata)
    quota = {b: 1 for b in names}
    while sum(quota.values()) < 40:
        eligible = [b for b in names if quota[b] < len(strata[b])]
        rng.shuffle(eligible)
        for b in eligible[:40 - sum(quota.values())]:
            quota[b] += 1
    sample = [r for b in names for r in rng.sample(strata[b], quota[b])]
    dump(OUT / 'negative_sample.jsonl', sample)
    audit_path = OUT / 'negaudit.jsonl'
    overturned = set()
    if audit_path.exists():
        audit = [json.loads(l) for l in audit_path.read_text().splitlines()]
        assert {r['mid'] for r in audit} == {r['mid'] for r in sample}
        overturned = {r['mid'] for r in audit if r['verdict_ok'] is not True}
    candidates = []
    for r in rows:
        g = gates(r)
        if any(g) or r['mid'] in overturned:
            candidates.append(dict(r, selection_gates=[i + 1 for i, yes in enumerate(g) if yes],
                                   semantic_selection_gates=[i + 1 for i, yes in enumerate(semantic_gates(r)) if yes],
                                   audit_rescue=r['mid'] in overturned))
    dump(OUT / 'F.jsonl', candidates)
    stats = dict(seed=SEED, source_rows=len(rows), excluded_batch='PILOTH',
                 master_sha256=hashlib.sha256(Path('data/z52b/master.jsonl').read_bytes()).hexdigest(),
                 negative_population=sum(map(len, strata.values())),
                 strata={b: {'population': len(strata[b]), 'sample': quota[b]} for b in names},
                 gate_counts=[sum(gates(r)[i] for r in rows) for i in range(3)],
                 original_union=sum(any(gates(r)) for r in rows),
                 audit_rescues=sorted(overturned), candidate_count=len(candidates),
                 new_ingredient_rule='literal case-insensitive != none; explanatory none (...) strings retained',
                 sample_design='equal batch allocation + seeded random extra strata, uniform without replacement within batch',
                 semantic_sensitivity=dict(gate_counts=[sum(semantic_gates(r)[i] for r in rows) for i in range(3)],
                     original_union=sum(any(semantic_gates(r)) for r in rows),
                     with_audit=sum(any(semantic_gates(r)) or r['mid'] in overturned for r in rows)),
                 source_sha256={str(path): hashlib.sha256(path.read_bytes()).hexdigest()
                     for path in sorted(BASE.glob('out_*.jsonl')) if path.stem != 'out_PILOTH'})
    (OUT / 'selection.json').write_text(json.dumps(stats, indent=2) + '\n')
    master = {r['mid']: r for r in map(json.loads, Path('data/z52b/master.jsonl').read_text().splitlines())} if args.reading else {}
    for name, data in ([('sample_reading', sample), ('candidate_reading', candidates)] if args.reading else []):
        with (OUT / (name + '.txt')).open('w') as f:
            for r in data:
                m = master[r['mid']]
                f.write(f"\n{r['mid']} [{r['batch']}] {m['title']}\nMASTER: {m['connection']} | {m['why']}\nFIRST: {m['first_step']}\n")
                f.write('AVENUE: ' + json.dumps(r, ensure_ascii=False) + '\n')
    print(json.dumps(stats, indent=2))


if __name__ == '__main__':
    main()
