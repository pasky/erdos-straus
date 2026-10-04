# Referee report: papers v3 (branch `side-agent/papers-v3`, head `999393c`)

Subject: `paper/sieve-limits-note.tex` v3 (new §10, main theorem = KARY2 Thm 5.1/5.2/Cor 6.1),
the new sharpness remark in `paper/es-threequarter-note.tex` §9, and the changelog
`reviews/agent-reports/PAPERS_V3.md`.
Sources checked against: `EXCEPTIONAL_KARY2.md` (all), `reviews/exceptional-kary2-review.md`,
`reviews/exceptional-kary2-review-2.md` (incl. round 2, R2-1), `DISCOVERIES.md` (D)18,
`EXCEPTIONAL_THETA.md` §5.6/§6, `reviews/sieve-limits-note-review-v2.md`,
`reviews/novelty-audit-2026-10.md`, and the v2 text (`git show HEAD:paper/sieve-limits-note.tex`).
Reviewer branch: `side-agent/review-papers-v3`.

## 1. Compilation and cross-references

* Both papers compile clean with 3 `pdflatex` passes (in `/tmp`): 0 warnings, no undefined
  references, no overfull boxes. The 3/4 note has no underfull boxes.
* The sieve note has 4 underfull boxes, not 3 as the changelog says. Three are bibliography
  lines. The fourth is in the body (lines 2008–2014, badness 2050, "Under Hypothesis 12.2,
  Theorem 12.1 …"). It was already present in v2 at lines 1684–1690. It is cosmetic.
* The hard-coded numbers are correct for v3. The `.aux` gives `sec:noB` = §10,
  `thm:main` = Theorem 10.8 and `rem:TQcovered` = Remark 10.9. These match
  `[SL, Theorem 10.8, Remark 10.9]` in the 3/4 note.
* Changelog nit: the dominant-prime section is §6, not "§5".
