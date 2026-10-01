# AUDIT_REPORT_A1: blind audit of `paper/es-threequarter-note.tex`

**Verdict (blind, committed before reading any earlier review in `886ed70`): SOUND.**
No load-bearing defect was found. There are five cosmetic or expository
items (B1–B5). B1, B2 and B5 are repaired on this branch. The label is
unchanged and should stay "INTERNALLY PROVED; internal checks only, not
externally refereed". This audit is one more internal check, not an
external referee report.

## Deliverables (branch of worktree 0004)

* `reviews/es-threequarter-blind-audit.md` contains:
  * the blind verdict;
  * a 10-step re-derivation of the load-bearing route
    (§5 → Cor 4.3 → Thm 6.3 (conditional independence) → Lemma 7.1 →
    Lemma 8.1 / Thm 8.2 → §9);
  * the defect table with lines and quotes;
  * the post-blind comparison with the two earlier reviews.
* `scripts/es34_blind_audit_checks.py` contains 16 exact or toy checks,
  all passing. Run it with
  `PYTHONPATH=scripts uv run python scripts/es34_blind_audit_checks.py`
  (about 1 min, under 1 GB). It covers:
  * the Bonferroni identities;
  * `E(H)_m = m! e_m ≤ μ^m`;
  * toy-family distinctness, with exact CRT `E H` and `E(H)_2`, and
    Monte Carlo `P(H=0)`, checked against the fibre formulas;
  * `h(𝒦(K)) − (2/π²) log K`;
  * the prime-power table (34);
  * the Euler ratio and the unit-pair count;
  * the §10 classes;
  * the pair sum;
  * the 3/4 bookkeeping.

  These checks cover algebra and probability only. They are not evidence
  for the asymptotic regime.
* `paper/es-threequarter-note.tex` and the `.pdf` have three cosmetic
  edits:
  * B1: the requirement `D log(3/2) > 1` replaces the unexplained "`>1+2`";
  * B2: the stray space in the title is removed;
  * B5: an explicit Lemma 2.2 cross-reference is added in the ordered-atom
    iteration.

  The note compiles cleanly: 21 pages, no warnings.

## The points the brief asked to concentrate on

* **Moment-order uniformity.** Conditional on `c mod L_K`,
  `E[(H)_m|c] = m! e_m ≤ μ_c^m` holds exactly. The only base constant is
  `C_u` from the all-fibre BT upper bound `μ_c ≤ C_u t³`. It is absorbed
  by `D_B > e C_u`. There is no hidden `C^r`.
* **Level budget.** The Bonferroni moduli `≤ P_y(KX)^r = e^{O(t⁴)}` are
  never fed to BV or BT. Each class is counted exactly on `[1,N]` as
  `N/q + O(1)`, which holds for every q. The ledger `T_abs = e^{O(rt)}`
  is paid honestly.
* **BV and BT.** Both are used only at scale `x ∈ [√X, X]` with moduli
  `4uv ≤ 4x^{1/3}`, under the level `x^{1/2}(log x)^{-A}`. The composite
  moduli carry multiplicities that are handled by Cauchy–Schwarz:
  `Σ W²E*` is bounded by BT plus the weighted second moment (Shiu for
  `2^ω n/φ(n)` modulo `d ≤ K²`, plus an elementary `d = 1` case), and
  `Σ E*` by BV with fixed `R = 26`. Siegel zeros affect only
  effectivity, and the note disclaims effectivity.
* **Passage to integers, void, and independence.**
  * The space is an exact CRT space.
  * Same-ℓ atoms are distinct because `z² < ℓ` and `4H² > K`.
  * The ℓ-coordinates are independent given `c` and the selector.
  * Non-reduced `c` is handled through `J_c ∋ 1`.
  * Bad fibres are made exponentially rare by `y = Bt³`.
  * Moduli sharing factors are handled exactly through `c`. The
    ordered-atom replay's prime-power table was also verified by brute
    force.
* **Optimisation and transfer.** With `t = α L^{1/4}`, the cost is
  `C_L α⁴ L ≤ L/2` and the saving is `c α³ L^{3/4}`. That gives exactly
  3/4, with no ε loss. The Rankin transfer with `δ = η₀ L^{-1/4}` is
  correct.

## Comparison with earlier reviews

There is no mathematical disagreement. Every earlier repair is already in
the text, and both earlier SOUND-AFTER-REPAIRS reviews' defects are
resolved there. I found only cosmetic items that they had not flagged.
Details are in §"Comparison with earlier reviews" of the audit file.

## Suggested parent actions

1. Merge the branch.
2. Optionally cite `reviews/es-threequarter-blind-audit.md` in DISCOVERIES
   (B)11 and in the internal-record sentence of Theorem 1.1, as "a blind
   internal audit (agent a1)". I did not edit DISCOVERIES.md or the
   Theorem 1.1 record myself; that decision is the parent's.
3. External expert reading remains the outstanding step.

Stopping here for parent review.
