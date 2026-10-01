# AGENT REPORT B: paper on why the pointwise signed-graph approach is blocked

Branch `side-agent/pointwise-obstruction-paper`, own worktree only. Nothing was
merged and nothing was written in the parent checkout or in `../erdos-straus-astra`.
Astra was only read; its checker was run on a copy in `/tmp/astra-copy`, and
`git status` in astra is clean.

## Deliverable

`paper/pointwise-obstruction.tex` and its PDF: 27 pages in amsart 11pt.
`pdflatex` ×2 gives no errors, no undefined references and no overfull boxes.
The style follows `paper/vaughan-loglog-note.tex` (author "Anonymous" with a TODO).

Structure:

1. **Introduction.** The graph, the seed, Conjecture 1.2 (which implies ES for
   p≡1 (4)), and the "formal blindness" principle. The principle is marked
   **informal**, and its precise content is listed. Results A–C follow, with what
   is not claimed and the credits.
   * Theorem C(1) is the astra result, stated **first** and called "the stronger
     version".
   * Theorem C(2) is ours, presented as an independent confirmation.
2. **The signed graph.** Fibres, the valuation lemma, types and labels, the
   small-anchor bound, and the character dichotomy. The dichotomy is
   Bright–Loughran Thm 1.2+1.5 via Lemma 3.4 and (3.1), checked against the PDF;
   Yamamoto is credited for the positive direction, BL Cor 1.3/App. A, and
   Br = Z/2 is BL Thm 1.6. The section also has Type II homogeneity, the Type I
   chart (EST coordinates), the seed, hubs and bridge, Type II fibres ≤ 2, and the
   outer-anchor theorem: SR §5 plus WINDMILL Thm 7, with the full Vieta/Jacobi
   proof.
3. **Short escapes.**
   * DEPTH3 Thm 1 (depth ≤ 3 classification) and Lemma 5 (fresh non-residue).
   * Forced exits: the Lemma 4 table, re-derived by hand, and the Mordell-class
     corollary.
   * The half-dimension lemma, adapted from Dahan Lemma 4.2, and the sieve bounds
     11/2 and 10, given a standard upper-bound sieve.
4. **Formal genericity.** This is a unified write-up of DEPTH3 §3 and
   FORMAL_CLOSURE §1.
   * Frames and formal integers. H gives admissible q.
   * The formal-fibre lemma, with the aux polynomials not required to be prime.
   * Proposition 4.6: in a square class no formal vertex is formally positive.
     This is unconditional; it is Schinzel's theorem, proved via BL with Dirichlet.
   * Theorem 4.7 (closed explorations): CONDITIONAL.
   * Theorem 4.9 (DEPTH3 Thm 2, unbounded seed distance): CONDITIONAL on H.
   * Then the whole seed component: **Theorem 4.11 (astra, Dickson, 159 linear
     forms, positive witness outside)** first, then Theorem 4.13 (= Theorem F, H
     for 6402 polynomials), with the certificate, what is checked, and replay.
5. **Further obstructions.**
   * The leaf lemma (WINDMILL L6) and edge structure.
   * Dead hubs: SIZE Lemmas A, B, C (descent) and E (sign flip), with all proofs
     re-done via Lemma 2.1. The certified sterile table includes 30035 > 10155.
   * Parity: WINDMILL Lemma 1, Lemmas 3–4, Prop 2 and Prop 5.
   * Each part says what it kills.
6. **Numerical evidence** (EVIDENCE): the 10^12 survey with 44197 distance-3
   primes and none of distance ≥ 4, the sparse q ≤ 10^13 survey, anchor counts and
   component sizes.
7. **Discussion.** A pointwise proof must control the actual factorisations of
   specific shifted integers.

Acknowledgements and the [AS] bibitem carry an explicit **TODO(parent)** for the
citation/authorship form of the companion. Appendix A gives replay commands.

## Verification done for this paper

* All algebraic identities were checked symbolically with sympy: the seed and
  bridge, the chart identity and its symmetric form, Lemma C(i), both astra
  positive witnesses, the Thm 7 algebra and the Lemma 5 products.
* Theorem F certificate:
  * `formal2_verify_extra.py`: OK in 4 min.
  * Reviewer's `review_fc_global.py`: OK.
  * Reviewer's from-scratch fibre engine `review_fc_fibres.py --all --jobs 4`:
    **9961/9961 fibres equal**, 533,011,471 candidates pass (A), 0
    precision/aux/c_r failures. Output in `/tmp/pb/review_fc_fibres_all.json`;
    the reviews/ file was not overwritten.
* Astra 159-form packet checker, run on a copy:
  `VERIFIED_PRIMARY_PACKET_EVENTUAL`, sha256 62a88612…c2f2. The astra eventual
  closure argument was **not** re-derived. The paper says so explicitly.
* Every attribution was re-checked against the PDFs:
  * BL Thm 1.2/1.5/1.6, Cor 1.3/1.4, Lemmas 3.2/3.4/3.10, (3.1), App. A.
  * EST (2.1)/(2.6)/(2.7)/(2.18)/(2.21), Prop 1.6 and the odd-square remark,
    which is on p. 6 of v6, not p. 5.
  * Dahan Lemma 4.2, Thm 4.3/4.14, Prop 3.8.
  * Jiang Thm 3.2 (v1, withdrawn); Monks–Velingker Thm 2.1(i); Mihnea–Dumitru
    10^18.
* A self-review by a deep reviewer subagent found real defects in my draft, and
  all of them are fixed:
  * a missing `t+a≠0` in the chart converse;
  * a "distinct formal integers have distinct values" statement without a fixed
    finite set and threshold;
  * a missing C_P=1 in the formal-fibre lemma;
  * a base point not forced to be a unit;
  * the astra positive witness, which needs Dickson for the restricted tuple;
  * a wrong node count (159, not 302);
  * an overstated provenance for the sterile certificates;
  * overbroad wording in the principle, the size and parity sections and the
    discussion.

  The reviewer confirmed Thm 2.10, Thm 3.1, Thm 3.6, Lemma 4.5, Prop 4.6,
  Thm 4.7 and Thm 4.9 after these fixes, together with all BL/EST/Dahan citations
  and the companion credit.

## Issues found in our markdown (see `PAPER_B_ISSUES.md`)

No mathematical gap was found in any source proof. The citation and precision
items are these:

* EST page 6, not 5.
* FC (C1) should require both D and s²/D to pass. Both engines already do this.
* FC §1.1 has a redundant gcd step.
* **The Theorem F class q0 is not a square class**: 24q0+1 is a non-residue
  mod 870 of the 2036 primes of Λ. So the "every prime met is a residue"
  explanation does not literally apply to Theorem F. (C4) is checked directly,
  so the theorem is unaffected, and the paper says this.
* The HR theorem number is unverified.
* The Dahan adaptation should be credited precisely.
* The Mihnea–Dumitru names in LITERATURE_2026 need correcting.
* The SR §5 width step needs stating.
* DEPTH3's "all 1113907 escape through A" cannot be checked from the repo. The
  paper restricts that claim.
* DEPTH3 Thm 2's "explicit family" is non-constructive.
* The astra witness needs the restricted tuple.

## For the parent to decide

1. The citation and authorship form of the companion [AS], and the author
   metadata (TODOs in the .tex).
2. Whether to propagate PAPER_B_ISSUES items 1, 4, 7, 9, 10 and 11 into
   DEPTH3/FC/LITERATURE_2026/STATUS. I did not touch the source markdown.
3. Length: 27 pages, against the target of about 15–25. If a shorter version is
   wanted, the obvious cuts are §5.3 parity, Evidence 6.2–6.3 and the
   appendix.

Stopping here for parent review.
