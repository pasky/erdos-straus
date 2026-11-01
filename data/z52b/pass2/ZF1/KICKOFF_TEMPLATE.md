# ZF1 sub-shard kickoff (Pass 2 finisher, Erdős–Straus repo)

You are a worker on the z52d Pass-2 FINISHER batch ZF1 of the Erdős–Straus (ES) research repo. ES is OPEN; never claim otherwise.

1. Read the brief `/home/pasky/projects/math/z52bbriefs/pass2.md` carefully (rules 1–6, compute rules C, output format) —
   it is binding. Background: `/home/pasky/projects/math/z52bbriefs/CONTEXT.md`, `FRONTIER.md` §§1–2 (definitions of
   R(p), C-form, Type I/II, ES₅/words, I3 …) — skim, `git grep` for anything else.
2. Your items are the lines of `data/z52b/pass2/batch_ZF1.jsonl` whose `mid` is in YOUR LIST (below). Each record has the
   idea, `repo_status` and `pass1` = the latest earlier record. These are FINISHER items: the previous record is either
   `needs-compute` (earlier workers over-estimated cost; most fit the cap with a sensible C/numpy implementation) or a
   STUB ("arXiv lookup: no match", "not run", "not computed", a one-liner reused from another item). Earlier "arXiv lookup:
   no match" records were broken searches, not findings. Do the item's actual `first_step` for real:
   - literature items: find and actually read the paper/theorem (arXiv API `https://export.arxiv.org/api/query?search_query=...`,
     `~/.pi/agent/packages/pi-amplike/skills/web-search/search.py "query"`, the visit-webpage skill
     `~/.pi/agent/packages/pi-amplike/skills/visit-webpage/` for abstracts/PDF text); state the exact theorem/hypotheses
     you verified, then carry out the ES-side check the first_step asks for (often a short derivation or a small
     numerical test against repo definitions). A literature lookup that only finds a title is NOT a completed step.
   - computation items: write C (gcc -O2) or numpy code, run the largest meaningful version within the cap (30 min
     wall per item, ≤ 3 cores, `ulimit -v 8000000`, `timeout` on every command). Reuse repo programs (`git grep`), e.g.
     `scripts/z52b_fingerprint_count.c` (U(p) = # unordered solutions; linear in p per prime), `scripts/bs_adv_count.c`
     (exact f_II at one prime), FRONTIER §2.1 for R(p) forms. No Sage/Magma/PARI/Lean binaries are installed; Python
     packages via `uv run --with numpy --with sympy ...` (try `--with python-flint` or `--with cypari2` if you need
     number-field/quadratic-form machinery). If an object (Brandt matrix, Ẑ-series, μ-invariant, topograph …) needs ~1 h
     of implementation, that is fine — implementing it IS the step; budget up to ~45 min per heavy item, not more.
   - premise check first (rule 5); explicitly say what you did not do (rule 6).
   - `needs-compute` again ONLY with partial results and a hard, measured justification. `covered` needs a depth
     document (file + § / line) that actually does the item's step, with the decisive line quoted.
3. Output (do NOT touch other workers' files):
   - one JSON line per item appended to `data/z52b/pass2/ZF1/parts/outcome_<SHARD>.jsonl` with exactly the fields
     `{"mid","outcome","summary","evidence","not_done","next","prev_outcome"}` (prev_outcome = the record's `pass1.outcome`);
     summary ≤ 4 sentences with numbers/ranges/file §; evidence = list of repo paths (scripts, data, docs §).
   - scripts `scripts/z52d_p2_ZF1_<mid>_*`, data `data/z52b/pass2/ZF1/<mid>/` (< 5 MB per item).
   - for every `interesting` item a section in `data/z52b/pass2/ZF1/parts/md_<SHARD>.md` (what, exact numbers, how to
     reproduce, why it might matter for ES, next step).
   - Labels for mathematical claims: PROVED / CONDITIONAL / CERTIFIED / EVIDENCE / CONJECTURE / Assessment.
4. Commit your own files after every ~3 items (`git add` only your paths; never `git add -A`). When all your items have
   exactly one output line each (check with a script), commit, report a 3-line summary (counts per outcome, interesting
   items) and then WAIT for the parent; when told "LGTM, merge", merge into the parent branch as instructed by the
   side-agent tooling.
5. Run continuously through all your items; never stop to ask whether to continue. Keep per-item notes terse but never
   shortcut the step itself.
