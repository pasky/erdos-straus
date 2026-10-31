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
    box = 'x' if r1 and r1['outcome'] in ('nothing', 'covered', 'skipped') else ' '
    out = f"- [{box}] **{it['mid']}** {short(it['title'], 140)} — {short(it['connection'], 260)}\n" \
          f"  *First step:* {short(it['first_step'], 260)} ({', '.join(meta)})"
    if pointer:
        files = ', '.join(it['st_files'][:3]) or '—'
        extra = it['st_ev'] or it['st_note']
        out += f"\n  *Repo:* {short(files, 160)} — {short(extra, 220)}"
    if r1:
        out += f"\n  *Pass 1 → {r1['outcome']}:* {short(r1['summary'], 300)}"
        if r1.get('next'):
            out += f" *Next:* {short(r1['next'], 200)}"
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
    L.append('Pass 1 ran the first step of every §1 item (outcomes in `data/z52b/pass1/`, memos `BRAINSTORM/z52b_pass1_*.md`). '
             'Ticked items are closed (nothing / covered / skipped). Open follow-ups:\n')
    by = {it['mid']: it for it in items}
    for r in sorted(p1.values(), key=lambda r: r['mid']):
        if r['outcome'] in ('interesting', 'needs-compute'):
            L.append(f"- **{r['mid']}** ({r['outcome']}) {short(by[r['mid']]['title'], 120)} — {short(r['summary'], 350)} "
                     f"*Next:* {short(r.get('next', ''), 220)}")
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
