# AGENT_REPORT_O96 — consolidation after the 2026-10-08 round (branch `side-agent/consolidate-oct8`)

No new mathematics. ES is not solved; the labels follow DISCOVERIES.md.

## (1) Propagating the refutation of POINTWISE_MORDELL Conj 4.2 (x* sterile)
* **POINTWISE_MORDELL.md §4.** A prominent "REFUTED (O95)" box gives the II3 class (8,33,11999), modulus 12670944,
  residue 12650497, and the I2 class (125,88,11999). It cites MORDELL13B Thm 3.1 and (F)11. Other changes:
  * the header label line and the Conj 4.2 heading are marked REFUTED;
  * the "In particular … cannot be improved" consequence is now marked open (it would need another sterile point,
    e.g. x**);
  * "Why Theorem C does not explain it" is kept as a historical remark;
  * the remark under Thm 3.1(b) ("apparently never to zero") now reads "open", with the reason.
* **paper/es-coverings-note.tex.**
  * §5.3 is renamed "The point x* and the candidate x**".
  * Comp 5.2 and Cor 5.3 are unchanged.
  * Former Conj 5.4 is replaced by Prop 5.4 (`prop:xstarcovered`, PROVED), with a self-contained proof (CRT
    conditions, side condition, explicit prime solution); it cites [PM13B].
  * New Comp 5.5 (`comp:xss`, the CERTIFIED search ranges at x**).
  * New Conj 5.6 (`conj:xss`, "x** sterile", explicitly EVIDENCE only), followed by its implication-only
    discussion.
  * The "odd-square" paragraph is retargeted to x**, with the warning from x*.
  * The data paragraph adds the 4.64% figure, labelled an upper bound.
  * Also updated: the abstract, the r = 13 Results bullet, Remark 3.3, the Salez "apparently never" sentence,
    Problems 1 and 5, and a new bibitem PM13B.
  * Build: two passes give 24 pp, 0 undefined references and 0 overfull boxes. One new harmless underfull vbox
    appears at a page break; the underfull hbox and the hyperref warnings were there before.
  * The PDF is updated.
  * `reviews/es-coverings-note-referee.md` has a "Post-referee correction (O96)" section.
* **STATUS.md, CAMPAIGN_SUMMARY.md, paper/README.md.** All x*/Conj 4.2 mentions are fixed.
* **Repo-wide grep.** The only other stale wording was in DISCOVERIES (H)34 ("The obstruction is … TYPEI2 rigidity"),
  now marked as a moot Assessment. Historical agent reports and reviews are left untouched, and so is the TYPEI2
  `x*`, which is a different object.

## (2) STATUS + CAMPAIGN_SUMMARY refresh (ledger through (D)31 and the 2026-10-08 follow-ups)
* **STATUS (refresh 5).**
  * New exceptional-line bullet for (D)31 (EXCEPTIONAL_MN).
  * Follow-up paragraphs for TYPEI5 ((H)17 f-up 4) and MORDELL17B ((H)34 f-up 2).
  * The r = 13 bullet is rewritten: refutation, new candidate x**, question open again.
  * The candidate list and the coverings-note entries are updated (24 pp; O91/O96 not re-refereed).
* **CAMPAIGN_SUMMARY.**
  * Title and §1 are updated, and a new §2.6 covers m/n.
  * §3.3 gains TYPEI5 follow-up 4 and MORDELL17B follow-up 2, and the r = 13 bullet is rewritten.
  * Table rows: E29 (MN) and P51–P53 (TYPEI5, MORDELL17B, MORDELL13B) are added, and P47 is marked refuted.
  * Also updated: the open-problems item, the not-audited list and the reading guide.

## (3) verify.py blocks (ed)–(eg), ≈ 29 s added; full run passes
* **(ed) MORDELL13B (4.6 s).**
  * R95 `review_m13b_thm31.py` and the author's `m13b_check_hit.py`.
  * R95 Lemma 1.1/1.2 table and Lemmas 2.1–2.4 random tests.
  * Inline from scratch: x* in both classes (CRT split M'/M_T); the stated Lemma 1.1 conditions; exact π^II / π^I
    solutions at 5 class members each; p = 12650497 prime with the stated solution; Lemma 2.1 at the datum
    (4/1859, j = 3).
* **(ee) EXCEPTIONAL_MN (11.7 s).**
  * Author scripts plus R94A/R94B lemma scripts.
  * Inline exhaustive Lemma 1.1 (m = 4..9) and inline Lemma 2.1(a),(b).
  * Toy fibre mass via `emn_mass2.py` (x = 10⁵): 1/m scaling, φ(m) scaling rejected (EVIDENCE).
* **(ef) TYPEI5 (1.9 s).**
  * R92 Lehmer/index/constructed-system checks and the author's check.
  * Inline minimal-solution brute force.
  * Inline sympy (H), (Lin) (exact: (definition of Δ)·Δ = (Lin)) and the Prop 3.3(iii) factorisation.
  * At L = 7: regimes (ii)/(iii) complete (author and R92), and R92's complete engine finds 0 certificates for
    b ≤ 3. Positive controls (11,0), (13,1), (14,0), (16,0) give 1, 1, 2, 3 solutions.
* **(eg) MORDELL17B (10.3 s).**
  * Lemma 2.1 enumerator = R93 naive C scan = stored data as sets at K = 5, 7; the author's naive scan agrees at
    K = 5.
  * SHA256SUMS.
  * ρ₀, ρ₁, ρ₂ are exact with both union scripts.
  * Tail tables are floor-rounded, checked against inline closed forms. C = 1.41 at θ = 0.4 is confirmed
    inadmissible.
  * **Deviation.** Regenerating the level-7 Q/U data takes 60–80 s per mode and engine (> 2 min in total). So I
    stored both engines' level-7 outputs in `data/m17b/qu7_{o93,r83}/`, with SHA256SUMS and a README. The block
    re-validates every stored datum against its defining equations and checks that the two engines' box sets
    coincide; levels ≤ 5 are regenerated fresh by both engines. Completeness at level 7 therefore rests on the
    two engines' offline runs (O96, 2026-10-08), not on a run inside verify.py.
* **Full run.** `OMP_NUM_THREADS=2 OPENBLAS_NUM_THREADS=2 timeout 2400 uv run --with scipy --with mpmath python
  verify.py` under `ulimit -v 8000000` printed "all checks passed", exit 0, in ≈ 6.6 min.
* A STATUS Housekeeping bullet is added.

## Notes for the parent
* POINTWISE_MORDELL13B.md and POINTWISE_TYPEI5.md still carry "Status: work in progress … Not reviewed" headers,
  although both are reviewed. I did not touch them (out of scope).
* The paper changes are post-referee and not re-refereed. A short hostile pass on §5.3 (Prop 5.4 / Comp 5.5 /
  Conj 5.6) is advisable before any external use.
