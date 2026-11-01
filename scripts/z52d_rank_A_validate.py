#!/usr/bin/env python3
"""Validate provenance, coverage, rankings and audit estimators, not source truth.

Finite arithmetic is independently exercised by z52d_rank_A_checks.py. This
validator addresses a different failure mode: silently dropped/mutated rows,
wrong partitions, stale scoring/rates or an incomplete final deliverable.
"""
import collections
import hashlib
import json
from pathlib import Path
from z52d_rank_A_build import load, gates, semantic_gates, NEG, SEED

OUT = Path('data/z52d/avenue/rank_A')


def jsonl(name):
    return [json.loads(line) for line in (OUT/name).read_text().splitlines()]


def main():
    source = {r['mid']:r for r in load()}
    master = {r['mid']:r for r in map(json.loads, Path('data/z52b/master.jsonl').read_text().splitlines())}
    selection = json.loads((OUT/'selection.json').read_text())
    sample, audit, candidates = map(jsonl, ['negative_sample.jsonl','negaudit.jsonl','F.jsonl'])
    data = json.loads((OUT/'clusters.json').read_text())
    assert selection['seed'] == SEED
    assert selection['master_sha256'] == hashlib.sha256(Path('data/z52b/master.jsonl').read_bytes()).hexdigest()
    assert len(sample) == len(audit) == 40
    assert len({r['mid'] for r in sample}) == len(sample)
    assert {r['mid'] for r in sample} == {r['mid'] for r in audit}
    population = [r for r in source.values() if r['status'] in NEG and r['plausibility']==0]
    strata = collections.Counter(r['batch'] for r in population)
    sample_sizes = collections.Counter(r['batch'] for r in sample)
    assert set(sample_sizes) == set(strata)
    assert selection['negative_population'] == len(population)
    for r in sample:
        assert r == source[r['mid']]
        assert r['status'] in NEG and r['plausibility']==0
    for b,n in strata.items():
        assert selection['strata'][b] == {'population':n,'sample':sample_sizes[b]}
    for r in audit:
        assert r['mid'] in master and type(r['verdict_ok']) in {bool,str}
        assert r['verdict_ok'] is True or r['verdict_ok'] is False or r['verdict_ok']=='partly'
        assert len(r['why'])>80 and r['should_be']
    rescues = {r['mid'] for r in audit if r['verdict_ok'] is not True}
    wanted = {m for m,r in source.items() if any(gates(r)) or m in rescues}
    assert len({r['mid'] for r in candidates})==len(candidates)
    assert {r['mid'] for r in candidates} == wanted
    for r in candidates:
        m = r['mid']
        assert m in master
        assert {k:r[k] for k in source[m]} == source[m], f'source mutation: {m}'
        assert r['selection_gates'] == [i+1 for i,g in enumerate(gates(r)) if g]
        assert r['semantic_selection_gates'] == [i+1 for i,g in enumerate(semantic_gates(r)) if g]
        assert r['audit_rescue'] == (m in rescues)
    assert selection['candidate_count'] == data['candidate_count'] == len(wanted)
    assert set(selection['audit_rescues']) == rescues
    assert selection['original_union'] == sum(any(gates(r)) for r in source.values())
    assert selection['gate_counts'] == [sum(gates(r)[i] for r in source.values()) for i in range(3)]
    sensitivity = selection['semantic_sensitivity']
    assert sensitivity['original_union'] == sum(any(semantic_gates(r)) for r in source.values())
    assert sensitivity['with_audit'] == sum(any(semantic_gates(r)) or r['mid'] in rescues for r in source.values())
    for path, digest in selection['source_sha256'].items():
        assert hashlib.sha256(Path(path).read_bytes()).hexdigest()==digest, f'source changed: {path}'
    clusters = data['clusters']
    membership = collections.Counter(m for c in clusters for m in c['members'])
    assert set(membership)==wanted and all(v==1 for v in membership.values())
    assert len({c['id'] for c in clusters})==len(clusters)==data['cluster_count']
    for c in clusters:
        assert c['band'] in {'i','ii','iii'} and 0<=c['plausibility']<=3
        for key in ['clean_statement','yield_for_ES','frontier','obstruction',
                    'ingredient_can_beat_obstruction','genuinely_new','assessment']:
            assert c[key], (c['id'],key)
        s = c['score_components']
        assert s['tractability']==c['plausibility']
        assert c['proof_priority_score']==5*s['relevance']+2*s['tractability']+2*s['one_day_information']+s['novelty']-3*s['unsupported_bridges']
        assert set(c['audit_rescues'])==set(c['members'])&rescues
    for band in ['i','ii','iii']:
        cs = [c for c in clusters if c['band']==band]
        assert cs==sorted(cs,key=lambda c:(-c['proof_priority_score'],c['id']))
        assert [c['rank_in_band'] for c in cs]==list(range(1,len(cs)+1))
    report = (OUT/'RANKING_A.md').read_text()
    assert len(report.splitlines())<=150 and 'ES remains OPEN' in report
    for c in clusters:
        assert report.count(f'**{c["id"]}** S=')==1
    verdict = {r['mid']:r['verdict_ok'] for r in audit}
    audit_summary = {}
    for name,pred in [('strict_overturn',lambda v:v is False),
                      ('including_partial',lambda v:v is not True)]:
        hits = sum(pred(v) for v in verdict.values())
        estimate = sum(strata[b]*sum(pred(verdict[r['mid']]) for r in sample if r['batch']==b)/sample_sizes[b] for b in strata)/len(population)
        audit_summary[name] = dict(sample_count=hits, sample_rate=hits/len(sample),
                                    stratum_weighted_rate=estimate)
    summary = dict(label='CERTIFIED structural validation; not mathematical certification of candidate conjectures',
        sources=len(source), candidates=len(candidates), clusters=len(clusters),
        bands=dict(collections.Counter(c['band'] for c in clusters)),
        report_lines=len(report.splitlines()), audit=audit_summary,
        candidate_source_fields_preserved=True, candidate_partition_exact=True,
        input_hashes_verified=True, scores_and_ranks_verified=True)
    (OUT/'validation.json').write_text(json.dumps(summary,indent=2)+'\n')
    print(json.dumps(summary,indent=2))


if __name__ == '__main__':
    main()
