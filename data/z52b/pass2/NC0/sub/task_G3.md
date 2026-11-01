# Task group G3 — z52d Pass 2, batch NC0 (ES is OPEN; never claim otherwise)

You are a sub-agent working in the git worktree /home/pasky/projects/math/erdos-straus-claude-agent-worktree-0050 (cwd). FIRST read the brief:
/home/pasky/projects/math/z52bbriefs/pass2.md  (the protocol; follow it). Background (skim only): /home/pasky/projects/math/z52bbriefs/CONTEXT.md.
Repo facts: 4/n = 1/x+1/y+1/z for all n≥2 is OPEN (ES). Reduction to primes p≡1 (mod 4). Labels for math claims: PROVED / CONDITIONAL / CERTIFIED (computer) / EVIDENCE / CONJECTURE / Assessment.

Rules for YOU (in addition to the brief):
- Do the item's actual first step (or a clearly-stated, cheap, closer-to-the-question substitute: say so explicitly in summary and in not_done). Do not stop at "needs more coding" unless the smallest meaningful test exceeds 30 min wall on ONE core. Coding time is NOT a compute cap; write the code.
- Use at most 1 CPU core: use `timeout 900` on every command, `ulimit -v 4000000` for python/C. Keep any data file < 1 MB; keep big outputs in /tmp/z52d_big/G3/ (not in the repo).
- Scripts go in scripts/z52d_p2_NC0_<mid>.py (or .c); tmp data in data/z52b/pass2/NC0/sub/<mid>*.  Do NOT run git commit / git add / git rebase — the coordinator commits. Do NOT write to data/z52b/pass2/outcome_NC0.jsonl.
- Use `git grep` for repo searches; never `find`. Literature: https://export.arxiv.org/api/query?search_query=... or ~/.pi/agent/packages/pi-amplike/skills/web-search/search.py "query" or curl oeis.
- Outcome (exactly one per item): nothing | covered | interesting | needs-compute | skipped. `covered` needs a depth document (file + § + decisive quote). `skipped` only for pure outreach/organisational items (none of yours should be). `interesting` only with a concrete next step.
- Do NOT call an item "nothing" because of a general campaign barrier; only because the concrete step came back empty. Report any false premise you find as a finding.

OUTPUT: append one JSON line per item to data/z52b/pass2/NC0/sub/out_G3.jsonl with keys:
{"mid","outcome","summary" (≤4 sentences: what you did and the numbers),"evidence": [files/scripts/URLs],"not_done": "...","next": "≤1 sentence"}
For outcome `interesting`, also append a section to data/z52b/pass2/NC0/sub/md_G3.md (what, exact numbers, how to reproduce).
When all your items are done, reply with a single line: "G3 done: <n> items; outcomes: <counts>". Do not paste item outputs in your final reply.

Your items (mid → record in data/z52b/pass2/batch_NC0.jsonl; read them with: python3 -c "import json;[print(json.dumps(json.loads(l),ensure_ascii=False,indent=1)) for l in open('data/z52b/pass2/batch_NC0.jsonl') if json.loads(l)['mid'] in 'Z1058 Z1082 Z1083 Z1088 Z1089 Z1090 Z1093 Z1094 Z1095 Z1107 Z1110 Z1112 Z1114 Z1115 Z1116'.split()]" ):
Z1058 Z1082 Z1083 Z1088 Z1089 Z1090 Z1093 Z1094 Z1095 Z1107 Z1110 Z1112 Z1114 Z1115 Z1116
