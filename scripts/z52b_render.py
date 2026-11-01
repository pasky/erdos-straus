"""Render ES_CONNECTIONS_TODO.md from data/z52b/master.jsonl + data/z52b/status/status_*.jsonl.

Each item appears exactly once. Sections:
  §1 Start here   — items proposed independently by >= 2 lanes (not blocked); touched ones carry a Repo pointer
  §2 Untried      — all other untried items, by area
  §3 Touched      — repo has related or prior work (status open/done), by area, with pointer
  §4 Blocked      — repo recorded a failure of essentially this idea (file + quote)
Tag index goes to data/z52b/TAG_INDEX.md.
"""
import json, glob, collections, re

items = [json.loads(l) for l in open('data/z52b/master.jsonl')]
status = {}
for f in sorted(glob.glob('data/z52b/status/status_*.jsonl')):
    for l in open(f):
        l = l.strip()
        if not l:
            continue
        r = json.loads(l)
        status[r['mid']] = r          # later chunks never overlap; last write wins
p1 = {}
for f in sorted(glob.glob('data/z52b/pass1/outcome_*.jsonl')):
    for l in open(f):
        if l.strip():
            r = json.loads(l)
            p1[r['mid']] = r
TRI = json.load(open('data/z52b/pass1/triage_interesting.json')) if glob.glob('data/z52b/pass1/triage_interesting.json') else {}
# z52d: Pass 2 (redo/complete first-step verdicts) — Haiku pass2 outcomes, overridden by the Opus audit records
p2 = {}
for f in sorted(glob.glob('data/z52b/pass2/outcome_*.jsonl')):
    for l in open(f):
        if l.strip():
            r = json.loads(l)
            r['_src'] = 'pass 2'
            p2[r['mid']] = r
for f in sorted(glob.glob('data/z52d/audit/opus_A*.jsonl')):
    for l in open(f):
        if l.strip():
            r = json.loads(l)
            r['_src'] = 'audit (Opus)'
            p2[r['mid']] = r
TRI2 = json.load(open('data/z52b/pass2/triage_interesting.json')) if glob.glob('data/z52b/pass2/triage_interesting.json') else {}
# z52d: proof-avenue layer (Opus): 'if this were part of a proof of ES, what is the missing theorem?'
AV = {}
for f in sorted(glob.glob('data/z52d/avenue/out_*.jsonl')):
    if 'PILOTH' in f:      # Haiku calibration replica, not a record
        continue
    for l in open(f):
        if l.strip():
            r = json.loads(l)
            AV[r['mid']] = r
AVR = json.load(open('data/z52d/avenue/review.json')) if glob.glob('data/z52d/avenue/review.json') else {}

def final(mid):
    """Latest first-step record for an item: Opus audit > Pass 2 > Pass 1."""
    return p2.get(mid) or p1.get(mid)

for it in items:
    s = status.get(it['mid'])
    it['st'] = s['status'] if s else 'unclassified'
    it['st_files'] = (s or {}).get('files', [])
    it['st_ev'] = (s or {}).get('evidence', '')
    it['st_note'] = (s or {}).get('note', '')

def short(t, n):
    t = re.sub(r'\s+', ' ', t or '').strip()
    return t if len(t) <= n else t[:n - 1].rstrip() + '…'

def line(it, pointer=False):
    r1 = p1.get(it['mid'])
    nl = len(set(it['lanes']))
    meta = [it['confidence_not_nonsense'], it['effort']]
    if nl >= 2:
        meta.append(f'{nl} lanes')
    r2 = p2.get(it['mid'])
    rf = r2 or r1
    tri = (TRI2 if r2 else TRI).get(it['mid'], 'NEW')
    box = 'x' if rf and rf['outcome'] in ('nothing', 'covered', 'skipped') else ' '
    if rf and rf['outcome'] == 'interesting' and tri.split('-')[0] in ('REDISCOVERY', 'EXPLAINED', 'ARTIFACT', 'ARTIFACT/WEAK'):
        box = 'x'
    out = f"- [{box}] **{it['mid']}** {short(it['title'], 140)} — {short(it['connection'], 260)}\n" \
          f"  *First step:* {short(it['first_step'], 260)} ({', '.join(meta)})"
    if pointer:
        files = ', '.join(it['st_files'][:3]) or '—'
        extra = it['st_ev'] or it['st_note']
        out += f"\n  *Repo:* {short(files, 160)} — {short(extra, 220)}"
    if r1:
        tv = f" [triage: {TRI[it['mid']]}]" if it['mid'] in TRI else ''
        out += f"\n  *Pass 1 → {r1['outcome']}{tv}:* {short(r1['summary'], 300)}"
        if r1.get('next') and not r2:
            out += f" *Next:* {short(r1['next'], 200)}"
    if r2:
        tv = f" [triage: {TRI2[it['mid']]}]" if it['mid'] in TRI2 else ''
        out += f"\n  *{r2['_src'][0].upper() + r2['_src'][1:]} → {r2['outcome']}{tv}:* {short(r2['summary'], 300)}"
        if r2.get('next'):
            out += f" *Next:* {short(r2['next'], 200)}"
    av = AV.get(it['mid'])
    if av:
        out += (f"\n  *Avenue:* {av.get('status')}, plaus {av.get('plausibility')}, novelty {av.get('novelty')}, yield "
                f"{short(str(av.get('yield')), 40)} — missing theorem: {short(av.get('missing_theorem'), 220)}")
    return out

def area(it):
    return it['areas'][0] if it['areas'] else 'miscellaneous'

nlanes = lambda it: len(set(it['lanes']))
conf_rank = {'high': 0, 'med': 1, 'low': 2}
eff_rank = {'cheap': 0, 'medium': 1, 'big': 2}
key = lambda it: (-nlanes(it), it['st'] in ('open', 'done'), conf_rank.get(it['confidence_not_nonsense'], 3), eff_rank.get(it['effort'], 3), it['mid'])

start = sorted([it for it in items if it['st'] != 'blocked' and nlanes(it) >= 2], key=key)
start_ids = {it['mid'] for it in start}
untried = [it for it in items if it['st'] in ('untried', 'unclassified') and it['mid'] not in start_ids]
touched = [it for it in items if it['st'] in ('open', 'done') and it['mid'] not in start_ids]
blocked = [it for it in items if it['st'] == 'blocked']

cnt = collections.Counter(it['st'] for it in items)
L = []
L.append('# ES_CONNECTIONS_TODO — candidate connections for Erdős–Straus (wave z52b)\n')
L.append('> **ES is OPEN.** Every line is a *candidate connection to try*, not a result. Nothing was dropped for being weak; '
         'only true duplicates were merged.\n')
L.append('## How to read this\n')
L.append(f'- **{len(items)} distinct items** (3590 raw ideas from 10 breadth-first lanes → duplicates merged). '
         'Each appears **exactly once** below.')
L.append('- Each item: **ID** title — the connection; *First step* = a concrete cheap action; (confidence it is not nonsense, '
         'effort of the first step, number of lanes that proposed it independently).')
L.append('- **Status** (cheap pass by Claude Haiku against the repo, biased against hiding ideas: "when in doubt, untried"):')
L.append('  - **untried** — no repo document examines this connection. → §2 (or §1 if multi-lane).')
L.append('  - **touched** — the repo has related or prior work (open, partial, or the first step already done); the *Repo* line '
         'says where. Still worth doing if the item adds something new. → §3 (or §1 if multi-lane, with a *Repo* line).')
L.append('  - **blocked** — a repo document recorded a concrete failure of essentially this idea (quoted). → §4. Revisit only '
         'with a new ingredient.')
L.append(f"- Counts: untried {cnt['untried'] + cnt['unclassified']}, touched {cnt['open'] + cnt['done']} "
         f"(open {cnt['open']}, first step done {cnt['done']}), blocked {cnt['blocked']}"
         + (f" (unclassified {cnt['unclassified']})" if cnt['unclassified'] else '') + '.')
L.append('- Where to start: §1 (proposed independently by ≥ 2 lanes; untried first in each tier). Then pick an area in §2.')
L.append('- Status overrides from the parent review are in `data/z52b/status/status_zz_parent_overrides.jsonl` '
         '(12 Haiku "blocked" calls resting on memo-level verdicts were downgraded to touched; 36 self-referential calls reset to untried).')
L.append('- Full records (why, refs, tags, alternative first steps, status evidence): `data/z52b/master.jsonl` and '
         '`data/z52b/status/`. Tag index: `data/z52b/TAG_INDEX.md`. Lane memos: `BRAINSTORM/z52b_*.md`. '
         'Rebuild: `python3 scripts/z52b_render.py`.')
L.append('- When you work an item: tick it, and record the outcome in a memo citing its ID.\n')

if p1:
    c1 = collections.Counter(r['outcome'] for r in p1.values())
    L.append(f"## Pass 1 results ({len(p1)} items worked: " + ', '.join(f'{k} {v}' for k, v in c1.most_common()) + ')\n')
    L.append('Pass 1 ran the first step of every §1 item (Opus) and of every untried §2 item (Haiku, with a correction round) (outcomes in `data/z52b/pass1/`, memos `BRAINSTORM/z52b_pass1_*.md`). '
             'Ticked items are closed (nothing / covered / skipped). Open follow-ups:\n')
    by = {it['mid']: it for it in items}
    tri = json.load(open('data/z52b/pass1/triage_interesting.json')) if glob.glob('data/z52b/pass1/triage_interesting.json') else {}
    nc = sum(1 for r in p1.values() if r['outcome'] == 'needs-compute')
    L.append(f'- **needs-compute: {nc} items** — plausible but the first meaningful test exceeds the cheap time box; each item below '
             'carries its *Pass 1* line with the computation spelled out. Grep `Pass 1 → needs-compute`.')
    L.append('- **interesting:** every item a worker flagged as interesting was re-triaged by Opus '
             '(`data/z52b/pass1/triage_interesting.json`): verdicts REDISCOVERY / EXPLAINED-BY / ARTIFACT / NEW-CALIBRATION / '
             'NEW-STRUCTURAL. Only the untriaged or NEW-* ones are listed here; NEW-STRUCTURAL count: '
             f"{sum(1 for v in tri.values() if v == 'NEW-STRUCTURAL')}.")
    for r in sorted(p1.values(), key=lambda r: r['mid']):
        v = tri.get(r['mid'])
        if r['outcome'] == 'interesting' and (v is None or v.startswith('NEW') or v.startswith('DEPTH')):
            L.append(f"- **{r['mid']}** ({tri.get(r['mid'], r['outcome'])}) {short(by[r['mid']]['title'], 120)} — {short(r['summary'], 350)} "
                     f"*Next:* {short(r.get('next', ''), 220)}")
    L.append('')
if p2 or AV:
    fin = {it['mid']: final(it['mid']) for it in items}
    cF = collections.Counter(r['outcome'] if r else 'none' for r in fin.values())
    L.append(f"## Pass 2 and the proof-avenue layer (wave z52d)\n")
    L.append(f"- **First-step verdict coverage:** {sum(1 for r in fin.values() if r)}/{len(items)} items have a recorded verdict "
             f"(latest of Pass 1 / Pass 2 / Opus audit): " + ', '.join(f'{k} {v}' for k, v in cF.most_common()) + '.')
    L.append('- **Audit** (`data/z52d/audit/`, reports `report_A*.md`): Opus redid 54 random Haiku nothing/skipped/covered verdicts '
             'blind. 20 AGREE, 29 MISS-MINOR, 2 MISS-MAJOR, 3 HAIKU-WRONG-COVERED; no lost item bore on a proof of ES. '
             'Pass 2 (`data/z52b/pass2/`, brief-hardened against the audit\'s failure patterns) redid every skipped, every needs-compute, '
             'every "covered" without a depth citation, and worked the touched items Pass 1 never did.')
    if AV:
        cS = collections.Counter(r.get('status') for r in AV.values())
        L.append(f"- **Proof-avenue layer** (`data/z52d/avenue/`, Opus, {len(AV)} items: every proof-attempt item plus every item a "
                 "keep-biased structural screen kept): per item the most favourable proof architecture, its missing theorem, and whether "
                 "that theorem is known-false / circular / harder than a famous open problem / open. Statuses: "
                 + ', '.join(f'{k} {v}' for k, v in cS.most_common()) + '. Batch summaries: `data/z52d/avenue/summary_*.md`.')
        surv = sorted([r for r in AV.values() if int(r.get('plausibility', 0)) >= 2 and int(r.get('novelty', 0)) >= 1
                       and not str(r.get('yield', '')).lower().startswith('none')],
                      key=lambda r: (-int(r['plausibility']), -int(r['novelty']), r['mid']))
        by = {it['mid']: it for it in items}
        L.append(f"- **Survivors** (plausibility ≥ 2, novelty ≥ 1, some proof yield; {len(surv)}). Parent review verdicts in "
                 "`data/z52d/avenue/review.json` where present:")
        for r in surv:
            rv = f" **[{AVR[r['mid']]}]**" if r['mid'] in AVR else ''
            L.append(f"  - **{r['mid']}**{rv} (plaus {r['plausibility']}, nov {r['novelty']}, {r.get('status')}) "
                     f"{short(by[r['mid']]['title'], 90)} — *missing theorem:* {short(r.get('missing_theorem'), 260)} "
                     f"*yield:* {short(str(r.get('yield')), 100)}")
    L.append('')
L.append('## Contents\n')
L.append(f'- §1 Start here — multi-lane ({len(start)})')
L.append(f'- §2 Untried, by area ({len(untried)})')
L.append(f'- §3 Touched in the repo, by area ({len(touched)})')
L.append(f'- §4 Blocked ({len(blocked)})\n')

L.append(f'## §1 Start here — proposed independently by ≥ 2 lanes ({len(start)})\n')
L += [line(it, it['st'] in ('open', 'done')) for it in start]
L.append('')

def by_area(lst, pointer):
    groups = collections.defaultdict(list)
    for it in lst:
        groups[area(it)].append(it)
    for a in sorted(groups, key=lambda a: -len(groups[a])):
        L.append(f'### {a} ({len(groups[a])})\n')
        L.extend(line(it, pointer) for it in sorted(groups[a], key=key))
        L.append('')

L.append(f'## §2 Untried, by area ({len(untried)})\n')
by_area(untried, False)
L.append(f'## §3 Touched in the repo, by area ({len(touched)})\n')
by_area(touched, True)
L.append(f'## §4 Blocked ({len(blocked)})\n')
L += [line(it, True) for it in sorted(blocked, key=key)]
L.append('')
open('ES_CONNECTIONS_TODO.md', 'w').write('\n'.join(L))

tags = collections.defaultdict(list)
for it in items:
    for t in it['tags']:
        tags[t].append(it['mid'])
T = ['# Tag index for ES_CONNECTIONS_TODO.md (tag → item IDs)\n']
for t in sorted(tags, key=lambda t: (-len(tags[t]), t)):
    T.append(f"- **{t}** ({len(tags[t])}): {', '.join(tags[t])}")
open('data/z52b/TAG_INDEX.md', 'w').write('\n'.join(T) + '\n')
print(cnt, 'start', len(start), 'untried', len(untried), 'touched', len(touched), 'blocked', len(blocked))
