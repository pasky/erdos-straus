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

## Update after the parent's decisions

* **[AS] citation:** set to the provisional form, "Companion project,
  `erdos-straus-astra` repository: SIGNED_SEED_COUNTEREXAMPLE.md and
  PRIMARY_SEED_PACKET.md (unpublished computational campaign, 2026)". Exactly one
  `% TODO(parent)` comment remains, and it does not appear in the PDF. The author
  stays "Anonymous".
* **PAPER_B_ISSUES propagated:** items 1, 2, 4, 7, 8, 9, 10 and 11 went into
  DEPTH3, FORMAL_CLOSURE, LITERATURE_2026, DISCOVERIES (G), STATUS and
  SIGNED_REFACTOR. These are minimal edits, each citing its item number.
* **Length:** 27 pages kept. The build is clean.

Stopping here, waiting for the hostile referee's findings.

## Revision 1 (referee report `reviews/pointwise-obstruction-paper-review.md`, branch side-agent/review-obstruction-paper)

All of D1–D22 are applied. The build is clean: two pdflatex passes, no errors,
no undefined references, no overfull boxes. The paper is now 29 pages. The two
remaining TODOs are LaTeX comments only, for authorship and for the [AS] form;
neither appears in the PDF.

| item | fix |
|---|---|
| D1 | Thm 2.10, case 2t<z<p: new display (eq:sixt) `x+z≤6t` with two proofs. The direct one: x∈[1,2t] by Lemma 2.4, since z∉[1,2t], and z≤p−1=4t. The referee's convexity bound g(z)=4z²/(4z−p−1/3) is added as an independent check. All three later uses now cite (eq:sixt). **WINDMILL Thm 7 has no real gap**: its setup states `1≤x≤2t` and z<p. The bound was left implicit, so I added a one-line parenthetical citing the review. Note that the paper's "gap" came from my transcription dropping x≤2t from the setup sentence. |
| D2 | BL Cor 1.4 is no longer cited for the polynomial-identity obstruction; that now cites ET p. 8. BL Cor 1.4 is cited separately as the Brauer–Manin proof of ET Prop 1.6. |
| D3 | The main message cites ET Prop 1.6 (vanishing), ET p. 6 (covering congruences) and ET p. 8 (polynomial identities) separately. |
| D4 | The status vocabulary gains **reported** (proved elsewhere; what was re-checked is stated). Thm 4.11 header: "reported [AS]; conditional on Dickson", with a status line "finite packet re-checked here; eventual-closure argument not re-verified here". Thm C(1) is labelled the same way. Thm C's conclusion, the §4.7 preamble and §7 now say that "Conjecture 1.2 false under H" rests on **Theorem 4.13 alone**. |
| D5 | Author stays Anonymous. Both TODOs are `%` comments; the PDF contains no "TODO". |
| D6 | Shared early history is stated (signed graph, seed, outer-anchor cases z<0 and z≥p, all predating the separation; the Vieta–Jacobi case is this project's only). Remark 4.12 says astra uses only the z<0 / z≥p cases. A timeline is added: 800-form version before Thm 4.13; 159-form reduction after it. The acknowledgements carry the same wording. |
| D7 | "ES holds at the primes of the subprogression n≡507 (mod 857)", in Thm C, in the paragraph after it, and in Remark 4.12. |
| D8 | Sieve: ω(ℓ) is defined explicitly. Ω₁ (ω≤19<ℓ), Ω₂(κ) via the prime number theorem in progressions mod each K_b, and R (\|r_d\|≤ω(d)) are verified. Cites HR Thm 2.2. That number is recalled, not checked against the book, which is not archived; this is still PAPER_B_ISSUES item 5. "p≡1 (4)" is added to Thm A(4) and Thm 3.6. |
| D9 | ET coordinates are subscripted a_ET…f_ET, with the explicit maps (abdp, acd, bcd) / (abd, acdp, bcdp), H=e_ET, 4x−p=f_ET, e=a_ET²d_ET. |
| D10 | The four-parameter model is defined, mapped to ET (2.3)/(2.15)/(2.22), and the maps are AGL₄(ℤ). |
| D11 | Added Vaughan 1970 (Mathematika 17) and BGS arXiv:1607.01530 (title verified on arXiv). |
| D12 | Permutation invariance cites BL Prop 2.6. The unsupported "elementary proof" sentence is deleted. |
| D13 | Elsholtz is cited at §3. |
| D14 | The h=1 exponent is compared with Dahan Thm 4.3 (single pair). Thm 4.14 is described as a two-sided estimate for shift c=7. Prop 3.8 is described as a finite computed list. |
| D15 | Guarded-hub count: hypotheses stated (squarefree x; ℓ_i≡1 mod 4𝓜; guard ≡1 mod 𝓜 and ≡3 mod 4). The hub and descent counts are derived; the closure is labelled **evidence** (122/126 instances). |
| D16 | Replay appendix rewritten: a `PY=PYTHONPATH=scripts uv run --with python-flint python` line, `scripts/` prefixes, build lines for depth3_allp/depth3_sieve/windmill_singleton (T mandatory), usage of every binary, and measured runtimes (details below). It explains how certificate.json.gz relates to lam_final.json + closure_final.json.gz, and points formal2_iter to FORMAL_CLOSURE §6. |
| D17 | Removed the redundant "j≥2". |
| D18 | Title: "Under Hypothesis H, formally generic primes block the pointwise signed-graph approach to the Erdős–Straus conjecture". The first claim sentence of the abstract is conditional on H. The abstract also says the astra result is reported, not re-proved. |
| D19 | The Jaroma identity is displayed for odd n≥3, attributed via BL §1 and its ref. 14. |
| D20 | The "Elsholtz–Tao principle in graph form" sentence now refers only to Prop 4.6 and Thm 4.9. Thm 4.13 is explicitly not a square-class instance (Remark 4.14). |
| D21 | V_{j+1} ⊇ V_j. (B) is decided after the E_ℓ are raised to the (F2) precision. |
| D22 | The anchor criterion cites ET Prop 2.3 (Type I: p=4acd−f, f\|4a²d+1) and Prop 2.7 (Type II). |

Measured replay runtimes (D16), all re-run for this revision with ≤4 cores:

* Python checks: 3–34 s each.
* `d3allp 13 1e8`: 2 s; 179468 tested, 70 candidates.
* `depth3_batch`: 2 s; all distance 3.
* `d3sieve … hard`: 217 survivors.
* `formal2_realq`: 6 s.
* Sterile certificates:
  * the 2192… certificate: 11 s;
  * the tests and typeI variants: about 40 s each;
  * the 30035-vertex certificate: 4.5 min (the referee's figure);
  * the **seed certificate: 23 min (OK; 10155 vertices)**.
* `wm_single 2500000`: 1 s, 0 hits.
