# ZF0 finisher — sub-worker brief

You are one of several workers on the Pass-2 FINISHER batch ZF0 of the Erdős–Straus (ES) campaign.
Repo/worktree (work ONLY here): /home/pasky/projects/math/erdos-straus-claude-agent-worktree-0053
ES is OPEN; never claim otherwise. Labels for any mathematical claim: PROVED / CONDITIONAL / CERTIFIED (computer) /
EVIDENCE / CONJECTURE / Assessment.

1. Read the master brief FIRST and follow it exactly: /home/pasky/projects/math/z52bbriefs/pass2.md
   (background if needed: /home/pasky/projects/math/z52bbriefs/CONTEXT.md, FRONTIER.md §§1–2 in the repo).
2. Your items are given by `mid` in your task. Their full records are lines of
   `data/z52b/pass2/batch_ZF0.jsonl` (python: filter by `mid`). Field `pass1` = latest earlier record — it was
   either `needs-compute` or a STUB (e.g. "not run", "arXiv lookup: no match", a bogus `covered` citing a file that does
   not actually do the step, or `nothing` without doing the step). Earlier workers (Haiku) over-estimated cost and
   under-did steps. YOUR JOB: actually do the item's `first_step` (or an alt step), within the cap.
   - Compute cap per item: 30 min wall, ≤ 4 cores, 8 GB (`ulimit -v 8000000`; `timeout` on every command; run heavy
     jobs under `nice -n 10`; the machine is shared). Write C (gcc -O2) for sieves/loops; Python via
     `uv run --with numpy --with sympy ...`. PARI/gp is not installed; `uv run --with cypari2` may work, or write your
     own reduced-form / class-group code (small discriminants are easy). Lean 4 is at ~/.elan/bin/lean; Java at
     /usr/bin/java.
   - Reuse repo code/data: `git grep -n <keyword>` (do NOT use `find`). Many quantities (U(n), R(n), I3, words
     p = tuv − u − v, (★) n = 4abC − a − b, divisor form d | 4Cp+1 with d ≡ −1 mod 4C) already have scripts in
     scripts/ and data in data/.
   - Literature lookups ARE steps: arXiv API https://export.arxiv.org/api/query?search_query=...&max_results=..., web
     search `~/.pi/agent/packages/pi-amplike/skills/web-search/search.py "query"`, page fetch per
     ~/.pi/agent/packages/pi-amplike/skills/visit-webpage/SKILL.md. A previous "no match" from a bad arXiv query is
     NOT a done step — search properly (authors' names, abstract keywords, web search), read the abstract/main theorem,
     and then do the ES-side check the step asks for (state precisely what the theorem gives and what it would need).
   - "covered" only with a depth document (file + § / line) that actually does the item's step; quote the decisive
     line. Verify any covered claim from pass1 yourself — many are bogus.
   - If a convention (matrix convention, pairing definition, lattice) is "not in the cited line", go read the cited
     memo(s) in BRAINSTORM/ and fix it yourself; that is part of the step, not a reason to stop.
   - `needs-compute` again ONLY with real partial results beyond pass1 AND a hard, measured cost justification.
3. Output: one JSON line per item to YOUR part file (given in the task), exactly the format of pass2.md:
   {"mid","outcome","summary" (≤ 4 sentences, numbers/ranges/file §),"evidence":[...],"not_done","next","prev_outcome"}
   prev_outcome = pass1.outcome. Validate with `python3 -c "import json;[json.loads(l) for l in open(F)]"`.
   Scripts: `scripts/z52d_p2_ZF0_<mid>_*`; data: `data/z52b/pass2/ZF0/<mid>/` (< 5 MB per item).
   For `interesting` items write a section (what, exact numbers, how to reproduce) to the md file given in your task.
4. Do NOT git commit, do NOT touch other workers' files; the coordinator commits. Append each item's line as soon as
   it is done (so partial progress survives). Work through all your items continuously, then end with a ≤ 15-line
   summary (mid → outcome, one phrase each).
