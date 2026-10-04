# AGENT_REPORT_O8 — sieve-limits paper (checkpoint 1)

Branch `side-agent/sieve-limits-paper`. Deliverable: `paper/sieve-limits-note.tex`
(+ `.pdf`, 21 pp). It compiles clean with pdflatex (3 passes, 0 errors, 0
overfull boxes, no undefined references). Author is "Anonymous". TODOs appear
only as `%` comments.

## What the paper contains

| § | content | source | label in paper |
|---|---|---|---|
| 2 | forced classes: identity, ℛ(M) = {−4D}, (a,D)-classes, Case-A classes, n=1 never covered, Mordell Jacobi lemma (all with proofs) | LL 2.1, notes 18.1, ET 3.2/§3, TW 1.1 | PROVED |
| 3 | prime-slice systems, majorants, level; **Definition 3.3 (architecture class (A1)–(A3))**; Lemma 3.4 = ET Lemma 2.9 (budget ⇒ level), Cor 3.5; positivity-on-ℤ remark | ET §1, §2.4, §2.7 | PROVED |
| 4 | Lemmas 2.1–2.3, Prop 2.4, **Thm 2.5**, large-sieve remark, **Thm 2.7**, Lemma 2.8 (full proofs) | ET §2 | PROVED |
| 5 | profiles: Lemma 3.1 (Shiu), (a,D) profile, Lemma 3.7 | ET §3 | PROVED; 3.7 mod Elsholtz–Tao Prop 1.4 |
| 6 | Cor 3.4, **Cor 3.6** (proofs), **Main Thm 6.3**: (i) dominant-prime families, (ii) (η,B)-gapped ℛ(M)-families, via Cor 3.5 | ET, TW | PROVED (Case A mod ET Prop 1.4) |
| 7 | gapped moduli: EB Lemma 2.1, QR base, capped measure, leak/inflation, **TW Thm 2.3**, Lemma 2.4, **TW Thm 2.7** (proofs incl. the EB window sum); TW Thm 4.4 stated, proof cited | EB §2, TW §§1–2, 4 | PROVED |
| 8 | 3/4 note in the class (ET Lemma 4.1 + Lemma 2.9: budget T_abs ≤ N^{1/2} is the binding constraint); Bonferroni depth; EH/BV non-binding; 2/3 note via Remark LS + Cor 3.5 (ET Lemma 4.4) | ET §4 | PROVED; attainability EVIDENCE |
| 9 | exclusions list (ET §6.1, updated for TW); Lemma 3.8 (balanced cubic supply; proof sketched, cited) | ET §6.1, §3.8 | PROVED / EVIDENCE |
| 10 | ET Thm 5.5 (proof), H_MS^Sel (OPEN), fibre tilting (TW 6.6/TW2 2.1), TW2 Thm 1.4, Thm 5.1, Lemma 5.4, (H_O^≠) (OPEN), **Cor 5.2 CONDITIONAL on (H_O^≠)** | ET §5.7, TW §6.6, TW2 | as in sources |
| 11 | open: H_MS, Conj 6.4, Prop 6.5 (CONDITIONAL on 6.4 + K2), Conj 6.8, H_div | ET §5.6, TW §6, TW2 §5.5 | OPEN / CONDITIONAL |

## Points for the referee

1. **Remark 4.8 (large sieve).** The source states the Rankin step
   `S_c(Q) ≤ exp{α log Q + 2Σ p_ℓ(c) ℓ^{−α}}` without a condition. I made
   explicit the condition `p_ℓ(c) ≤ 1/2`, which gives `g_ℓ ≤ 2p_ℓ`. It is
   flagged with a `%` comment.
2. **Main theorem, case (i), and the admissible set.** The cap holds with the
   specific R of Cor 3.6 (selector P_{w0} plus small-modulus avoidance). For
   selectors with growing y (the 3/4 note), the paper routes through
   Cor 3.4 (prime-slice), whose selector term is log log y. This is stated
   after the theorem.
3. **η-dependence in case (ii).** I removed the claim "linear in η^{−1}". The
   budget bootstrap gives `s ≪ η^{−1}L^{3/4} + O(η^{−4})`, so the dependence
   is only "depending on η".
4. Lemma 3.8, TW Thm 4.4, TW2 Thm 1.4/5.1 and Lemma 5.4 are **stated with
   proof sketches and cited**, not reproduced in full. Everything in §§2–7 on
   the 3/4 cap itself is proved in full in the paper.
5. Bibliography. BBMST is given without page numbers, because I was unsure
   of them. Hough's pages (361–382) are from memory and should be checked.
   Internal documents are cited as repository files; the citation form is
   left as a `% TODO(submission)`.
6. Nothing is strengthened beyond the sources, to the best of my checking.
   Statement-by-statement re-verification against ET/EB/TW/TW2 is the
   natural referee task.

Status: checkpoint, waiting for parent review.

## Checkpoint 2 (after parent updates)

1. **TWIN3 incorporated.** I added Theorem 10.6, which is (H_O) =
   TW3 Thm 4.1, PROVED, with a proof sketch. I also added **Theorem 10.7**:
   the two-prime Λ² cap `≪ L^{3/4}(log L)^{O(1)}`, now **PROVED**
   (TW2 Cor 5.2 + TW3 Cor 4.2). Its exact scope: ℛ(M)-classes, M ≤ X,
   M ≤ P(M)^{1+B} with B fixed, at most two prime factors above (log X)^8,
   twins/dominant/prime powers included, level λ ≤ A₀L, Λ² majorants only.
   Remark 10.8 records that (H_O^≠) and H_div are **bypassed, not proved**,
   and remain open as stated (TW3 review E5). The old TW2 Lemma 5.4,
   (H_O^≠) hypothesis and conditional corollary were removed. I updated
   the abstract, the results list, §9 item 4 and §11.
   * Still open in §11: general majorants with twin moduli (Conj 6.4 /
     Prop 6.5) and Λ² with three or more large primes. TW3 §6 is reported
     as internal and *not yet reviewed*: Lemmas 6.1–6.2, Prop 6.3
     (implication), and Prop 6.4 with the balanced-partner residual OPEN.
   * One added observation of my own, marked as such in a `%` comment: the
     coarsening of Lemma 2.9 does not preserve squares, so for Λ² the level
     hypothesis is assumed directly.
2. **Bibliography.**
   * Hough is dropped. It had been cited only as a historical attribution
     for the distortion method. BBMST is kept as the direct model for the
     capped measure.
   * Page numbers remain only for Shiu (161–170). I checked them against
     `sources/shiu-1980.pdf`: the article starts on its first page, and the
     last page is numbered 170 and ends with the references.
   * Omitted because there is no archived text: Vaughan (DOI given instead;
     see `sources/vaughan-1970-access-log.md`), Montgomery, and
     Elsholtz–Tao. For Elsholtz–Tao the arXiv v6 PDF is archived but
     carries no journal pages; it is cited as arXiv:1107.1010v6.
   * BBMST: I dropped the unverified journal reference. The arXiv number was
     confirmed on arxiv.org.
3. The paper compiles clean (3 passes, 0 errors/overfull/undefined) to
   22 pp.

## Checkpoint 3 (referee report `reviews/sieve-limits-note-review.md`, MINOR REVISION)

All defects D1–D14 applied:
* **D1/D11.** The abstract, Results item 2, §9 item 4 and the §11 opening
  now carry the full scope:
  * Λ² cap: ℛ(M), M ≤ X, M ≤ P(M)^{1+B} with B fixed, level O(log X);
  * gapped cap: (η,B)-gapped with B fixed, and the specified admissible set;
  * "family primes ≤ N^{O(1)}" now matches (A3).
* **D2.** Cor 3.5 is restated in the referee's addendum form: coarsen at
  λ = (A+2) log N, so Eν' ≤ Eν + 1/N, and min(s, log N) ≤ log 2 +
  C(log N)^{3/4} + C'. The cap is needed only at level (A+2) log N. The
  main-theorem proof uses Cor 6.2 with A+2, and Thm 7.6 at λ = (A+2) log N.
* **D3.** Vaughan's method is attributed via the reconstruction in PW §4
  (`sources/pw.txt` l. 454–456); Montgomery is cited for the inequality
  only.
* **D4.** The Cor 6.1/6.2 headers now say "Case A proved mod Elsholtz–Tao
  Prop 1.4".
* **D5.** Results item 1 states the conditions for the O(log²λ) error term
  and its general size λ log λ (Remark 4.6).
* **D6.** The `% TODO` is removed; the p ≤ 1/2 reading is now cited to
  ETrev item 3.4.
* **D7.** η₀ is removed ("every η < 1 with η ≤ 1/C − 1").
* **D8.** The 2/3-note sentence is now phrased as a cap on its saving.
* **D9.** Lemma 8.1 explains why the majorant is 1 on the whole avoider set
  (ETrev item 3.1) and notes that TQ itself only states ≥ 1 on exceptional
  primes.
* **D10.** The TW3 §6 status is updated to match main:
  * Lemmas 6.1–6.2: PROVED; Prop 6.3: PROVED as an implication; both
    reviewed in round 2.
  * Prop 6.4: SKETCH, conditional on the unwritten any-arity fibre law.
  * Residual: corrected to ℓ_a ≤ ℓ_b < w₂q, OPEN.
* **D12.** The level-hypothesis observation is marked in the text as the
  note's own.
* **D13.** TW3 and TW3rev are now cited as files on main; TW3rev rounds 1–2.
* **D14.** Hough is credited by name: Ann. of Math. 181 (2015), no pages,
  "in the form of BBMST".

The paper compiles clean (3 passes, 0 errors/overfull/undefined) to 22 pp.
