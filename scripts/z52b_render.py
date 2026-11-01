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
# blind Opus audit redos, kept as separate records together with the audit's own comparison verdict
CMP = {}
for f in sorted(glob.glob('data/z52d/audit/compare_A*.jsonl')) + sorted(glob.glob('data/z52d/audit2/compare_B*.jsonl')):
    for l in open(f):
        if l.strip():
            r = json.loads(l)
            CMP[r['mid']] = r
AUD = {}
for f in sorted(glob.glob('data/z52d/audit/opus_A*.jsonl')) + sorted(glob.glob('data/z52d/audit2/opus_B*.jsonl')):
    for l in open(f):
        if l.strip():
            r = json.loads(l)
            r['_src'] = 'audit (Opus, blind)'
            AUD[r['mid']] = r
TRI2 = {}
for f in sorted(glob.glob('data/z52b/pass2/triage_interesting*.json')):
    TRI2.update(json.load(open(f)))
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
    """Reconciled first-step record: the blind Opus audit unless its own comparison judged the earlier record better;
    else Pass 2 > Pass 1."""
    a = AUD.get(mid)
    if a and CMP.get(mid, {}).get('verdict') != 'HAIKU-BETTER':
        return a
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
    ra = AUD.get(it['mid'])
    rf = final(it['mid'])
    tri = (TRI if rf is r1 else TRI2).get(it['mid'], 'NEW')
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
    if ra:
        cv = CMP.get(it['mid'], {})
        cvs = f" [vs earlier record: {cv['verdict']} — {short(cv.get('why', ''), 160)}]" if cv else ''
        out += f"\n  *Audit (Opus, blind) → {ra['outcome']}{cvs}:* {short(ra['summary'], 300)}"
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
    skipped = sorted(m for m, r in fin.items() if r and r['outcome'] == 'skipped')
    by = {it['mid']: it for it in items}
    L.append("## Wave z52d — audits, Pass 2, proof-avenue layer, depth lanes\n")
    L.append('**Bottom line (Assessment).** No proof avenue for ES was found. Every item now has a first-step verdict and ~94 % have a '
             'proof-avenue row; two independent rankers (Opus, GPT) found no avenue at plausibility ≥ 2; the five top clusters went '
             'to depth lanes and all came back *narrowed* (scoped no-go theorems), none strengthened. ES remains OPEN.\n')
    L.append(f"- **Coverage.** {sum(1 for r in fin.values() if r)}/{len(items)} items have a first-step verdict "
             "(latest of Pass 1 / Pass 2 / Opus audit; outcomes " + ', '.join(f'{k} {v}' for k, v in cF.most_common()) +
             f"). No `needs-compute` remains. Residual `skipped` ({len(skipped)}): {', '.join(skipped)} — each record states "
             "its reason; all are organisational / outreach / decisions for the user (several with the item's mathematical "
             "question answered from the repo). Per-item lines show every record (Pass 1, Pass 2, blind audit with its comparison verdict).")
    L.append('- **Audit of Pass 1** (`data/z52d/audit/report_A*.md`): Opus redid 54 random Haiku nothing/skipped/covered verdicts '
             'blind: 20 AGREE, 29 MISS-MINOR, 2 MISS-MAJOR, 3 WRONG-COVERED; content lost was calibration only, never proof-relevant. '
             'Haiku verdicts are reliable as decisions, weak as records (skips of actionable steps, substituted steps, tiny ranges, '
             'covered-by-own-origin).')
    L.append('- **Pass 2** (`data/z52b/pass2/`, brief hardened against those patterns, plus a lint and fix round): redid every '
             'skipped, every needs-compute, every covered-without-depth-citation, and worked the 908 touched items never worked; '
             'an Opus finisher (batches ZF0/ZF1) did all residual needs-compute and stub records with real computations, and ZF2 redid the '
             '12 §1 items Pass 1 (Opus) had skipped as "not actionable as stated". '
             '**Audit of Pass 2** (`data/z52d/audit2/`): 32 blind Opus redos — 15 AGREE, 15 MISS-MINOR, 1 MISS-MAJOR, 1 HAIKU-BETTER; '
             'again no proof-relevant loss; records still miss repo coverage pointers about half the time.')
    tri2 = collections.Counter(TRI2.values())
    L.append(f"- **Pass-2 'interesting' triage** (Opus, `BRAINSTORM/z52d_pass2_triage_*.md`): {sum(tri2.values())} items — "
             + ', '.join(f'{k} {v}' for k, v in tri2.most_common()) + '. NEW-* items:')
    for mid in sorted(k for k, v in TRI2.items() if v.startswith('NEW') or v.startswith('DEPTH')):
        r = p2.get(mid) or p1.get(mid)
        L.append(f"  - **{mid}** ({TRI2[mid]}) {short(by[mid]['title'], 110)} — {short(r['summary'] if r else '', 260)}")
    if AV:
        cS = collections.Counter(r.get('status') for r in AV.values())
        L.append(f"- **Proof-avenue layer** (`data/z52d/avenue/`, Opus, {len(AV)} items = every proof-attempt item + every item a "
                 "keep-biased structural screen kept): per item the most favourable proof architecture and its missing theorem. "
                 "Statuses: " + ', '.join(f'{k} {v}' for k, v in cS.most_common()) + '. Batch summaries `summary_*.md`. '
                 'Read negative statuses as "dead by the cited argument or by Assessment": an independent GPT audit overturned ~30 % of '
                 'negative *labels* (to open, plausibility ≤ 1), while neither audit found a buried avenue (Opus 0/40 real avenues).')
        L.append('- **Rankings** (independent): `data/z52d/avenue/rank_O/RANKING_O.md` (Opus, 23 clusters) and `rank_A/RANKING_A.md` '
                 '(GPT, 79 clusters). Both: no ES avenue at plausibility ≥ 2; best proof-facing targets are plausibility-1 faces of the '
                 'B2 single-integer lower tail.')
        L.append('- **Depth lanes** (Opus, each cross-reviewed by GPT, fixes applied; FRONTIER §3/§6/§7 updated):')
        L.append('  - `Z52D_HYPERBOLA.md` — §7.1 hyperbola cancellation: **narrowed**. Benchmark p^{1/3}; one-step dualization, '
                 'Erdős–Turán with square-root input, Cauchy–Schwarz all closed (each PROVED for the stated implementation); for '
                 'smoothly weighted blocks the low-conductor part has a common leading expression at primes and rough odd squares up to '
                 'O(m^{−A}) (sharp cutoffs: only O(1/U)).')
        L.append('  - `Z52D_PELLCYCLE.md` — Pell/reduction-cycle forest roots: **dead under H** for the principal-cycle root menu '
                 '(near-square primes m²+1); arbitrary functions of cycle data not covered.')
        L.append('  - `Z52D_FOURIER.md` — bounded-order character obstruction: **strongly narrowed**; signed inverse lemma false for '
                 'B ≤ 952 (all B under Dickson); collapses to §7.3 (genus layer) + B2.')
        L.append('  - `Z52D_PARITY.md` — finite-group / windmill forcing: **narrowed**; ℤ/3, odd-order, A₃, Wielandt m ≥ 3 menus fail '
                 'unconditionally; parity rules = (J)2; no 2-power class-group signal (EVIDENCE to 2·10⁸).')
        L.append('  - `Z52D_THINFAMILY.md` — 15·2^s+1 (side theorem, no transfer): **narrowed**; root-family menu structure theorem, '
                 'menu C empty, certified ranges; open escapes listed in FRONTIER §7.8.')
        L.append('  - `LEAN_Z1546.md` — Lean: C-form ⟹ ES and T1 for C-form/shifted/Type II (Type I needs gcd(f,m)=1); later '
                 'also ES(3·2^s+1) for all s. Standard axioms only.')
        surv = sorted([r for r in AV.values() if int(r.get('plausibility', 0)) >= 2 and int(r.get('novelty', 0)) >= 1
                       and not str(r.get('yield', '')).lower().startswith('none')],
                      key=lambda r: (-int(r['plausibility']), -int(r['novelty']), r['mid']))
        L.append(f"- **Avenue rows with plausibility ≥ 2, novelty ≥ 1 and some yield** ({len(surv)}; all are side theorems — averaged, "
                 "main-term, explicit-constant or thin-family — per both rankings):")
        for r in surv:
            rv = f" **[{AVR[r['mid']]}]**" if r['mid'] in AVR else ''
            L.append(f"  - **{r['mid']}**{rv} (plaus {r['plausibility']}, nov {r['novelty']}, {r.get('status')}) "
                     f"{short(by[r['mid']]['title'], 90)} — *missing theorem:* {short(r.get('missing_theorem'), 220)}")
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
