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
