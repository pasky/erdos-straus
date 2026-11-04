# Z56_SUMMARY — wave z56: two papers, unconditional K(4), a big-main-term family, gap-1 hardness, prime T1, Lean

**ES is OPEN.** Every result here is internal. Wave z56 (brief `z52bbriefs/z56_lanes.md`) ran twelve lanes in six tracks:
papers (PAPERCOUNT, PAPERHC); unconditional K(4) = P(4,15) (K4BILIN, K4CHEN, K4LIT, tryhard K4TRY); a (★) family with a
big main term / full (★) positivity (FAMDESIGN, FAMATTACK, tryhard FAMTRY); gap-1 hardness (CENTRAL); disproof direction
(PRIMET1); Lean (LEAN). Each analytic/statistical memo had internal hostile review(s) and a cross-model review
(`data/z56/xreview/REVIEW_<LANE>.md`); all nine were ACCEPT-WITH-FIXES and were merged after the fixes. Each paper had one
internal hostile referee and one cross-model referee (`paper/<name>.REVIEW.md`, `paper/<name>.XREFEREE.md`). The Lean lane
has no cross-model review; its verification is the Lean kernel check. This summary carries scopes only loosely; each
memo's own statement governs.

## 0. Bottom line

**Neither unconditional K(4) nor eventual full-(★) positivity was proved.** Unconditional K(4) (= P(4,15)) and "R(p) ≥ 1 for every large prime p ≡ 1 (4)" (full
(★)) both remain open; gap 1 (pointwise TD / NC) is untouched as a positivity question. **Nothing has been posted.**
What the wave produced:

* **Two paper drafts, not posted.** `paper/es-count-note` (25 pp.; cross-model referee: MAJOR REVISION, for a missing
  literature comparison, all proofs CORRECT) and `paper/es-hc-note` (21 pp.; cross-model referee: MINOR REVISION, no
  GAP/WRONG). Both were revised after the referee; neither revision was re-refereed. The count note had to be
  **repositioned against Akaka's unrefereed Zenodo 22754703 claim** of an almost-all-primes cubic lower bound for the full
  strict Type II count (§1).
* **Genus main term: 5/6 of the expected (★) count, unconditionally (FAMDESIGN Theorem V, PROVED).** M_gen(p) ≥
  (5/(4π²) − o(1))log²p = (5/6 − o(1))M₀(p) at every large prime p ≡ 1 (4) (Burgess + Heath-Brown's quadratic large
  sieve); with Burgess alone 29/(30π²) ≈ 0.0979 log²p, effective. This is 18.5 × Thm U's 2/(3π⁴). **Main term only**: the
  order-≥3 remainder (B2) is untouched, so R ≥ 1 does not follow. The family 𝔊* has exactly 38 zero primes ≤ 10¹⁰
  (CERTIFIED), the last 564 661 441.
* **Exceptional set for (★) (FAMTRY Theorem A, PROVED rel. BV + large sieve).** #{p ≤ X : R(p) = 0} ≤ X·exp(−0.08√log X)
  for X ≥ X₀ (ineffective), uniformly in intervals of length X. Average statement (B6); capped at √X by odd squares for
  this argument; novelty unverified.
* **K(4): narrowed.** New PROVED side results: K4TRY Theorem AA (generic shift pairs (a, b) work; nothing about (4, 1));
  K4BILIN Lemma T\* and Prop P (both shifts in S with n a P₁₂, not necessarily prime); K4LIT Lemma P / Prop P′ (1/2 is the
  infimum level exponent for the stated one-component data-only guarantee; endpoint open); K4CHEN Lemma D. The model
  deficit Ω_𝒬(4p + 1) improves 10 → 6 (K4CHEN), but only as a **CONDITIONAL numerical witness on Hypothesis MT and the
  stated numerical inequality** (the enclosure is evaluated in floating point, not interval-certified) — no unconditional
  explicit bound.
* **Gap 1 (CENTRAL): calibrated.** Under EPC, a uniform length-decoupled CNT would give SID (a pointwise power-saving
  short-interval divisor asymptotic at length x^{1/4}), not established in the checked sources; unconditionally
  |E1(p, U)| ≪ U(log log U)^{5/2} pointwise for primes p in the fourth-root range c₁p^{1/4} ≤ U ≤ c₂p^{1/4}, 16U³ ≤ p
  (Prop P, rel. de la Bretèche–Tenenbaum 2025).
* **Disproof direction (PRIMET1): narrowed, EVIDENCE.** In the tested ranges and fitted models, the linear batteries
  leave one small unexplained candidate association with large prime factors of p − 1 (≈ +0.6 % of E[R] per SD). A small
  nonlinear Hecke-angle signal is consistent with square-offset near-squares, but absorption remains untested. Consistent
  with ‘local main term × lottery’; not an exclusion.
* **Lean.** Coordinate-form certificates ⟹ ES, HCKILL Lemma 1.1, Theorem Q and UPPER2 Prop 3.1 machine-checked, standard
  axioms, no `sorry`.

## 1. Papers (PAPERCOUNT, PAPERHC; internal; nothing posted — the user decides)

**`paper/es-count-note.{tex,pdf}`** — "Counting Erdős–Straus solutions on one Type II line" (25 pp.). Review record
`paper/es-count-note.REVIEW.md`; cross-model report `paper/es-count-note.XREFEREE.md`.
* **Contents (PROVED in the paper relative to the cited classical inputs).**
  * Thm A / Thm 3.12: R(n) ≪_ε n^{12/37+ε} for every n (from `Z53_SQSIEVE.md`); Thm 3.14: general exponent pairs,
    n^{21/65+ε} relative to Bourgain's Thm 6 (sketched proof, phase class), n^{4/13+ε} under the exponent-pair conjecture;
    Thm 3.8 (first step, `Z53_HYPSUMPROD.md` Thm 1): R(n) ≪ n^{1/3−1/225}(log n)².
  * Thm B / Thm 4.8 (`Z53_GENUSLVAL.md` Thm U): M_gen(p) ≥ (2/(3π⁴) − ε)log²p, unconditional, effective; Prop 4.10 (slice
    formula, squarefree u ≡ 1 (4), u ≤ p^α, α < 3/5, L′ and H′ terms kept); Thm 4.12 (`Z53_GENUSX.md` Thm X; density-weighted,
    not exact divisibility).
  * Thm C (`Z53_PZ.md` Thm A): for every η ∈ (0, 1), R(p) ≥ (1 − η)log²p/64 for all but O(η⁻²π(X)/log X) primes p ≤ X,
    X ≥ X₀(η) (ineffective). Average statement (B6).
  * Not claimed: ES; R(p) ≥ 1 at any prescribed prime; any bound for X(p) = R(p) − M_gen(p) beyond Thm 4.12; a
    balanced-block barrier (heuristic remark only).
* **Referees.** Internal hostile referee (deep mode): MINOR REVISION (false exponent-pair ancestry, Type II coprimality
  qualification, odd-prime domain, etc.; all applied). Cross-model referee: **MAJOR REVISION**, all proofs CORRECT
  (Thm 3.14 CORRECT-WITH-FIX: rounding in the W/Q step, no exponent change), major for a material literature omission.
* **Akaka repositioning (required fix 1; applied).** Akaka, "A cubic lower bound for strict Erdős–Straus solution counts
  at almost all primes", Zenodo 22754703, v0.7, 2026-09-14, Theorem 1, claims #{p ≤ N : R_II(p) < c(log p)³} ≪ N/(log N)⁴
  for the actual strictly ordered Type II count (`LITERATURE_2026.md` §2.4: unrefereed, declared AI-assisted, Lean
  certificate claimed). The earlier lead had been seen only as an X-post snippet in z53; the record was already archived
  in the repo. Changes: the abstract's "improves ET's almost-all exponent 0.549 to 2 for the solution count" is removed;
  §1.4 states Akaka's claim (labelled unrefereed, not checked by us, nothing depends on it) and proves that his family
  and the line R are **disjoint**, so a bound for his count or for f_II gives none for R; methods compared (shared:
  truncation to small moduli, primitive-character variance, weighted BV with a divisor-moment budget; different variance
  bound); §1.6's search account rewritten ("bounded search, not a priority certificate"); §7(4) no longer presents the
  full-Type-II cubic bound as untouched. **Thm C is now positioned as a statement about the c = 1 line R only; as a
  statement about f_II or f it is superseded if Akaka's claim is correct.**
* Other fixes: Thm 3.14 rounding; §§6–7 overclaims ("consistent with that order", improvement routes not a necessity);
  HLMLT author order. The 65-slice L-value percentages are an internal sanity check (generator named, not regenerated).

**`paper/es-hc-note.{tex,pdf}`** — "The least certificate coordinate for the Erdős–Straus equation at a prime" (21 pp.).
Review record `paper/es-hc-note.REVIEW.md`; cross-model report `paper/es-hc-note.XREFEREE.md`.
* **Contents.** Lemma 2.1/Prop 2.2 (for n ≥ 5, n ≡ 1 (4), a word has a coordinate in 𝒞_n ⟺ a slot divisible by 4; five
  identities), Lemma 2.3 (lines U/T), Lemma 2.7/Cor 2.8 (reciprocity; HC(m²) = ∞ for odd m — Yamamoto's obstruction
  written for the two lines), Prop 3.1 (HC(p) ≤ 8 for primes p > 7, p ≡ 1 (4), outside the six Mordell classes mod 840),
  Lemma 4.1 (K(4) ⟺ P(4,15)), Remark 4.2 (det-15 shell), Theorem Q (Bunyakovsky ⟹ infinitude),
  Prop 4.8 (#{p ≤ x prime : p ≡ 1 (4), HC(p) > 4} ≪ x/log²x), **Theorem E (CONDITIONAL on EH(1 − η₀))**, **Theorem U** (P415's unconditional half of
  P(4,15); proof simplified; η₀, δ not computed; model numerics deliberately omitted), Prop 5.1 (CONDITIONAL on Dickson:
  HC unbounded), Theorem W, **Theorem N / Cor 6.1** (HCF: fixed finite coverings fail on non-square classes),
  Computation 7.1 (HC(p) ≤ 64 for primes p ≡ 1 (4) below 10¹²; one program with cross-checks; the full 10¹² range was not independently rerun).
* **Referees.** Internal: revision required, no FATAL, one MAJOR (the Dickson-prime modulus claim was false; replaced by
  log p > (1/4 + o(1))X; Prop 5.1 and Thm W unaffected); applied. Cross-model: **MINOR REVISION**, every result CORRECT
  (conditional ones relative to their hypotheses; the census as computational evidence). Applied: Yamamoto attribution
  (Lemma 4 / Thm 2, numbers from the referee's OCR, not re-inspected); η fixed before x → ∞ in E/U; a checked census
  wrapper (`paper/es-hc-note.census-check.sh`, nonzero exit on any failure) and a SHA-256 manifest. A stable public
  archive has **not** been made. The referee places the contribution at E/U/N (§§2–3 are infrastructure; López and
  Yamamoto overlap acknowledged); novelty "plausible, not established exhaustively". Akaka is not relevant to this note.

## 2. Unconditional K(4) = P(4,15) (K4BILIN, K4CHEN, K4LIT; tryhard K4TRY)

Notation as `Z55_P415.md`: S = {n : all prime factors ≡ 1 (4)}, 𝒬 = primes ≡ 3 (4), Ω_𝒬 with multiplicity.
P(4,15): infinitely many primes p ≡ 1 (8) with p + 4 ∈ S and 4p + 1 ∈ S (= K(4), HCKILL Lemma 1.1). **Not proved.**

**K4TRY (`Z56_K4TRY.md` §3; cross-review: AA survives, sources [S1–S3] audited at source level).**
* **Theorem AA (PROVED, unconditional; rel. Barban–Davenport–Halberstam, the linear beta sieve, Ford's upper sieve).**
  For every ε ∈ (0, 1) there are η ∈ (0, 1/10], c > 0, x₀ such that for x ≥ x₀ and H = x^{1−η}, all but at most εH²
  admissible pairs (a, b) ∈ [1, H]² (a ≡ 0 (4), b ≡ 1 (4), 3 | ab(a − b)) satisfy
  #{p ≤ x : p ≡ 1 (8), p + a ∈ S, 4p + b ∈ S} ≥ c·x/(log x)². It never selects a fixed pair; nothing about (4, 1).
* Hybrid route (r\* on one shift, semi-linear sieve + switching on the other): model level 0.908 (pen 1) / 0.958
  (pen 2.35). **Proposed route only; no conditional theorem** (hypothesis 𝒟 remains schematic and does not supply the
  required moving-endpoint control;
  local densities unevaluated; Lemma S unproved).
* CERTIFIED counts to 2·10⁸ (reproduced byte-for-byte): 2 769 023 primes p ≡ 1 (8), 232 258 with both shifts in S.
  EVIDENCE: model switched masses agree in order only (relative deviations −1 % to −19.5 %).
* Do not export: "only obstruction", "no unconditional progress is possible", "at least as hard as FI" — the det-1
  comparison is an analogy, not a reduction.

**K4BILIN (`Z56_K4BILIN.md`; cross-review ACCEPT-WITH-FIXES).** a\*_n := r\*(n + 4)r\*(4n + 1)·1[n ≡ 97 (120)];
a\*_p > 0 ⟺ p is a P(4,15) prime in that class.
* **Lemma T\* (PROVED rel. FI 2009 Lemma 4.1 = Smith):** level x^{1/6−ε} for moduli coprime to 30 (with ε loss; not the
  endpoint), density g\*(ℓ) = 1/(ℓ + 2χ₋₄(ℓ)).
* **Prop P (PROVED):** ≫ x/(log x)⁹ integers n ≤ x, n ≡ 97 (120) with n + 4, 4n + 1 ∈ S, Ω(n) ≤ 12 **and** all prime
  factors > x^{1/13} (roughness holds for this constructed subset, not for every n satisfying the other conditions alone;
  n = 97 disproves that stronger assertion for x > 97¹³). No ES content (n not required to be prime).
* **Lemma N (PROVED, negative):** a\* vanishes on inert-prime shift classes, so the multiplicative comparison model fails
  every Type II hypothesis with logarithmic saving; a comparison must address this local obstruction (W-tricking is one
  way; others not ruled out).
* **V′ is a proposed implication, not a theorem:** (TII_W) ⟹ P(4,15) additionally needs two unproved model lemmas
  (model Type I, model prime mass) and a weighted Harman sieve. The claimed necessary W-exponent was withdrawn.
* Route P (Assessment, one architecture): the FI full-range budget is > 3/4 for primes in CRT-mixed classes; known
  dispersion levels ≈ 0.617 for a single fixed residue (Lichtman, abstract-only tag), 1/2 + δ for mixed residues.
  Diagnostics to 10¹⁰ (approximately 0.4 %) cannot validate an all-coefficient Type II statement.

**K4CHEN (`Z56_K4CHEN.md`; cross-review ACCEPT-WITH-FIXES).** C(r): ≫ x/(log x)² primes p ≤ x, p ≡ 1 (8), p + 4 ∈ S,
Ω_𝒬(4p + 1) ≤ r.
* **Lemma D (PROVED, exact reduction)** for Chen-type switching on 4p + 1; **normalisation lemma (PROVED):**
  C_S = (A/2)c_W.
* **Proposition K6: C(6) in the BV-level model, CONDITIONAL numerical witness on Hypothesis MT and the stated numerical
  inequality** (BV-type remainder control for the
  structured switched sets *and* local-factor/main-term evaluation ≤ 2.35 × model). Its numerical inequality rests on the
  cross-reviewer's positive log-box enclosure (exact-arithmetic construction; the enclosure is evaluated in floating
  point, not interval-certified; lower margin +0.0355).
* Model (Assessment): 10 → 6 surviving pen 2.35; → 4 only on a knife-edge (pen ≤ 1.1); C(2) grid witnesses at level 0.68
  (0.65 with switched sums at level θ); no C(0) witness through level 1 (P415's ≈ 0.996 stands). Additive-weight LPs:
  EVIDENCE, not an impossibility theorem.
* **No unconditional explicit Ω_𝒬 bound** (6, 8 or 10) is established. The cross-review independently re-established
  P415 Theorem U's *unspecified* absolute bound via Ford's uniform sieve, independent of MT.

**K4LIT (`Z56_K4LIT.md`; cross-review ACCEPT-WITH-FIXES).**
* **Lemma P (PROVED) + Prop P′ (PROVED rel. Iwaniec 1976 Thm 1)**, for one parity-forced semi-linear component with
  admissible density g(q) = (1 + c_q)/(q + c_q), 0 ≤ c_q ≤ C/q (includes 1/q and 1/(q − 1); a bare "g ≥ 1/q,
  g = 1/q + O(1/q²)" is not enough, g(3) = 1 counterexample): below every fixed level < 1/2 a hidden 𝒬-prime gives a
  nonnegative sequence with the prescribed local density, stated remainder bounds and no element in S; above 1/2, under
  Prop P′'s support and remainder hypotheses, the S-mass is ≫ X(log x)^{−1/2}. Endpoint open; nothing for joint data.
* Literature (Assessment, bounded searches, provenance-tagged): P(4,15) and its det-1 analogue were not located as
  unconditional theorems. FI 2009 Thm 4 (Σ Λ(n)r(n−2)r(n+2) ≍ x) has its lower bound under A(θ) for one fixed θ < 1
  sufficiently close to 1 (upper bound unconditional). Nath–Xie v3 has Ω(p + 2) ≤ 9 (P415 cited v1's 11). No 2018–2026
  result located supplies the missing input; 2026 abstract-only items (GMPP, Lü–Wang–Wu, Banks) are reports of claims.
* (★K): an incomplete research specification, not a proved implication (the complementary-divisor transfer is unproved).
* Do not export: "EH-hard" beyond "every exact two-component sieve implementation audited needs EH-strength input"
  (Assessment; Theorem Q's Bunyakovsky route is a different hypothesis); "probability 0, unconditionally"; K4LIT's
  recommendation to "bank the K4CHEN explicit bound" (that bound is model-level / a CONDITIONAL numerical witness on MT and the stated
  numerical inequality, with a floating-point, not interval-certified, enclosure).

**Assessment (track).** Kill side moved only on averaged or relaxed versions (AA: average over shifts; P: n not required to
be prime; model: C(6) a conditional numerical witness on MT and the stated numerical inequality). The fixed pair (4, 1)
remains at "EH-strength level in CRT-coupled classes, or new Type II input for the det-15 shell" for the audited methods.

## 3. Big-main-term family and full (★) positivity (FAMDESIGN, FAMATTACK; tryhard FAMTRY)

M₀(p) = Σ_{𝒫(p)} 1/φ(4uB) = (3/(2π²) + o(1))log²p is the expected (★) count. All three lanes: **(★) at every large prime
NOT proved.**

**FAMDESIGN (`Z56_FAMDESIGN.md`; cross-review: Theorem V CORRECT, numerics ACCEPT-WITH-FIXES).** Solutions
(o, e, C), o odd, e even, p = 4oeC − o − e; 𝔊* := {(o, e) : max(o, e)⁴ > min(o, e)·p} (integer inequality, o = 1 allowed).
* **Theorem V (PROVED; Burgess + Heath-Brown's quadratic large sieve; §3).** For every η > 0 and every prime p ≡ 1 (4),
  p ≥ p₀(η, λ): M_{A∩G_λ}(p) ≥ ((3/π²)area(G_λ) − η)log²p, where, in log coordinates,
  G_λ = {(a,b) ∈ (0,1)² : a+b < 1, max(a,b) > (1+min(a,b))/4, min(a,b) > λ}, with λ > 0 fixed before p → ∞.
  λ = 1/15 with Burgess only: 29/(30π²) ≈ 0.0979, p₀ effective. With HB, → 5/(4π²) ≈ 0.1267 as λ → 0. On every closed
  rectangle inside G_λ the genus main term is an asymptotic (3/π²)·area·log²p.
  **Corollary: M_gen(p) ≥ (5/(4π²) − o(1))log²p = (5/6 − o(1))M₀(p).** Cor V1: 64/(45π⁴) ≈ 0.0146 on Thm U's admissible
  trapezoid.
* The excluded density-area sixth is the **Burgess corner** max(o, e) ≤ (min(o, e)·p)^{1/4} (large C), where the cross terms
  are **not controlled by this argument** (no impossibility or optimality theorem). PROVED: every solution with 64C³ ≤ p
  lies in 𝔊*. T1: §3.8 names the false step at squares.
* **CERTIFIED:** R_𝔊*(p) = 0 at exactly 38 primes p ≡ 1 (4) ≤ 10¹⁰ (last 564 661 441, with R = 2 and its unique solution in
  the corner); none at the 57 806 sampled primes above 10¹⁰ up to 10¹⁴. Burgess-only family 𝔊*_{1/15}: 317 zeros ≤ 10¹⁰,
  last 6 122 428 657. The cross-review reproduced the stored unions and all four F4 zeros above 10⁷ but did not
  independently rescan (10⁶, 10¹⁰]. Its H3-overflow finding (signed 128-bit) was fixed; only the 10¹⁴ H3 column changed.
* EVIDENCE: means R_𝔊*/log²p ≈ 0.134 → 0.126 (≤ 10⁷ → 10¹⁴); strong overdispersion (var(hits)/E[hits] 2.4 → 4.9, where hits = R_𝔊*/2). Assessment
  (crude two-parameter fit): last-zero scale ~10^{8.3} for 𝔊* vs ~10^{118} for the Thm U standard window.
* Verdict: strengthened, main-term side only; B2 untouched.

**FAMATTACK (`Z56_FAMATTACK.md`; cross-review ACCEPT-WITH-FIXES).**
* **Prop T (PROVED, effective):** tiling Thm U: M_gen(p) ≥ (64/(45π⁴) − ε)log²p ≈ 0.0146 log²p (same constant as
  FAMDESIGN Cor V1; superseded in size by Theorem V). **Prop T′ (PROVED):** tiling GENUSX Thm X: exact-class density main
  term ≥ (28/(75π⁴) − ε)log²p ≈ 0.00383 log²p, with T_u = O(p^{−δ}log p) on every tile. Lower-bound coefficients, not
  ceilings.
* **Thm J (PROVED reduction):** R(p) ≥ Σ_t M^cls_t + Σ_t E_t over a finite tiling; (★) eventually ⇐ (CU_𝒯):
  Σ_t E_t ≥ −(1 − ε)Σ_t M^cls_t (CONJECTURE-strength, sufficient, not necessary). Vacuous at odd squares.
* **Lemma L (PROVED):** exact cross-window links — the switch (hit matrix symmetric; maps a hit at u to one at u′ = B),
  privacy, a parity law for the odd part of p + u (p ≡ 1 (4), p ∤ u, multiplicities). Assessment: none of the analysed
  links forces a first hit when all windows are empty; other links not excluded.
* **Prop V (PROVED):** a pointwise variance criterion across windows implies a weighted first-moment lower bound; the
  Poisson criterion is Σ w_jM_j(M_j − 1) > 0 (every M_j > 1 is sufficient, not necessary).
* EVIDENCE (F1, pre-registered; ≈ 180 000 primes at 10⁸–1.2·10⁹): leads triggered, kill condition not met. Negative pairs:
  the u-window lead −0.02…−0.08, and C(3,4) −0.15 (within 840, 10⁸), −0.157 / −0.125 with L-proxy controls; but net
  positive residual covariance and excess pooled joint emptiness (ratio 1.01 at k = 2 up to 1.6–3.4 at k = 8).
* CERTIFIED counts: among n ≡ 1 (4), 5 ≤ n ≤ 7 999 801, R(n) = 0 exactly at 13 primes, all 1 413 odd squares in that
  range, and 285 non-square composites. EVIDENCE (floating-point evaluations of exact finite sums): composite-zero M_gen
  reaches 24.3 at 810 001 = 241·3361; at the prime zero 8 813 281, M_gen ≈ 29.1. A transfer
  X ≥ −(1 − ε)M_gen asserted uniformly for non-squares is false; eventual statements are not refuted.
* Assessment: union over size windows reduces to (CU_𝒯), B2 in tied form; the dead-end line is method-scoped.

**FAMTRY (`Z56_FAMTRY.md`; cross-review: Theorem A CORRECT, target INCONCLUSIVE).**
* **Theorem A (PROVED rel. BV and Montgomery's large sieve):** #{p ≤ X : R(p) = 0} ≤ X·exp(−0.08√log X) for X ≥ X₀
  (ineffective), with the same bound in every interval of length X. The same holds for the odd integers avoiding the
  prime-modulus hit classes, a set containing all odd squares, so this argument cannot go below √X. B6 applies.
  **Novelty unverified** (the lane rules forbade reading the project's barrier memos).
* PROVED: Lemma 1.4 (R(p) ≥ 1 iff some d ≡ 3 (4) has (−p mod d) nonzero and dividing (d + 1)/4); Prop 2.1 (p ≡ 5 (8),
  2 (3), 5 or 6 (7) ⟹ R ≥ 1); Prop 2.2 (no fixed finite covering of the primes ≡ 1 (8) by solvable classes or finite
  polynomial menus with eventual positive integral validity on the stated classes); Lemma 4.1 (structure forced by R(p) = 0); §4.4(ii) log L(Q) ≍ √log Q (two-sided order; optimality
  for this denominator / large-sieve bound only).
* CERTIFIED (independent engine, to 10⁸): the 14 zeros up to 8 813 281 and R(m²) = 0 for all odd 3 ≤ m ≤ 9999.
  EVIDENCE: 422 primes p ≡ 1 (8) in [10⁷, 10⁸] have no prime-modulus hit — finite only; eventual prime-modulus sufficiency
  is open.
* Do not export: "any proof must use composite / linear-size moduli", universal sieve barriers, and the original
  random-model claim (the prime-only model gives Θ(log p) expected hits, not exp(−c log²p)).

**Status (track).** Proved main terms now cover 5/6 of M₀ (Thm V) and the exceptional set of (★) has upper bound
X·exp(−0.08√log X) (Thm A), a saving beyond every fixed logarithmic power but not a fixed-power saving. Positivity at every large p needs the remainder (B2); FAMATTACK's union-over-windows idea found no
mechanism. Recommended targets for problem CROSS (FAMDESIGN, Assessment): 𝔊* and its complete-level part H3.

## 4. CENTRAL — gap-1 hardness (`Z56_CENTRAL.md`; cross-review ACCEPT-WITH-FIXES, two minor)

Upper-bound calibration only; silent on positivity. SID: D(x, y) = Main(x, y) + O(x^{(1−η)/4}) for some η > 0, uniformly
for all large real x and y ∈ [x^{1/4}/K, Kx^{1/4}], with K ≥ 1 fixed. Throughout these reductions, 0 < δ < 1/4.
* **Theorem L (PROVED identity):** D(x, y) − Main = E_band(δ) − 2F_L + O(1), E_band the central band
  m ∈ (x^{1/2−δ}, x^{1/2+δ}]. CONDITIONAL on EPC: F_L ≪ x^{1/4−δ/2+ε}; hence SID ⟺ a power saving for some central band
  (Cor L2), CNT_unif ⟹ SID (Cor L1), CNT_poly ⟹ SID (Cor L1′). CNT_unif / CNT_poly are stronger than TDCAL's CNT (all real
  x, length decoupled from position, uniform thresholds); CNT_unif contains CNT provided K > max(1, 2c₂, 1/(2c₁)); this is a sufficient condition, not a
  necessary threshold.
* **Cor L3 (PROVED; Trudgian–Yang pair (715/10238 + ε, 7955/10238 + ε), ε > 0 sufficiently small):** this argument gives
  the equivalence unconditionally for 6387/28960 < δ < 1/4 (lower threshold ≈ 0.2205; finite pair search, no optimality
  claim).
* **Theorem U (PROVED implication):** power-saving short-interval asymptotics for τ_t(n) = Σ_{de=n}(d/e)^{it}, uniformly
  for |t| ≤ x^c, imply CNT_unif. **Theorem E (CONDITIONAL on EPC):** the converse (Cor E1: equivalence, existence of
  exponents only).
* **Prop P (PROVED rel. de la Bretèche–Tenenbaum 2025 Cor 1.2):** |E1(p, U)| ≪ U(log log U)^{5/2} pointwise for primes p in the fourth-root
  range c₁p^{1/4} ≤ U ≤ c₂p^{1/4}, 16U³ ≤ p (was U^{1+ε}).
  **Cor P2 (PROVED implication):** TD(η) ⟹ DC(2U^{−η}) with a (log log U)^{5/2} loss.
* Remark H: the dual phase's Hessian has rank one (PROVED); non-applicability of 2D methods is Assessment.
* EVIDENCE: identity residual ≤ 0.632 at 10¹⁰ (2 400 cases, recomputed in 60-digit arithmetic); slice errors at √y scale
  (within sq12/nsq12, y ranges from 2000 to 2188, a 9.4 % increase; sq10/nsq10 range from 632 to 1410); the 10¹²–10¹⁶ datasets were checked via
  statistics and one raw sample per family, not fully recomputed.
* SID "not established": Assessment, search-limited. The fixed tied/prime CNT problem is **not** shown equivalent to SID.
* Assessment: the count enters gap 1 only as a zero mode, for which Prop P suffices; CNT-type asymptotics should not be on
  the route to TD/NC.

## 5. PRIMET1 — is (★)-hardness a lottery? (`Z56_PRIMET1.md`; EVIDENCE lane; cross-review ACCEPT-WITH-FIXES)

* Design: 16 invariant families committed before outcomes (G17 added by amendment), held-out primary block with Holm;
  eight dated amendments; data: 6.7·10⁶ primes p ≡ 1 (24) in [10⁷, 10¹⁰] with exact R, 25 000 at 10¹²–10¹³, the hardest
  0.01 % of (10⁹, 10¹⁰], the 14 zeros, HC at 10¹². Real-field class-number/L-value computations use GRH-conditional
  PARI output; the R counts are exact. PROVED side fact: a (★)-zero prime p ≡ 1 (4) is ≡ 1 (24).
* **Findings (EVIDENCE).** Most detected associations beyond the pre-registered local model track local data, an L-value
  main term (BM; genus-layer L(1, χ_{−4p}) ∝ h(−4p), ≈ +4.6–4.8 % of E[R] per SD given exact BM — the largest omitted
  main-term effect), near-squares (square-offset near-squares look harder: post-hoc, nominal z), or the u = 1 / B = 1
  tickets 2τ₃(p + 1). Class-group parts, h(p), power residuosity of 2 and 3, Frobenius in non-abelian cubic/quartic
  fields, Hecke and Sato–Tate angles: no significant *linear* association in A5/A6 after the stated local and L-value
  adjustments. A small nonlinear
  Hecke-angle signal is consistent with square-offset near-squares; augmented-null replication pending.
* **Candidate signal A9:** large prime factors of p − 1, ≈ +0.6 % of E[R] per SD. Pre-specified two-feature B₂₃
  confirmation p_Holm = 0.01397 (over 2); post-hoc complete-null robustness 0.004058 (over 2), 0.03043 (over 15 rerun
  families) — not a second independent confirmation; B₂₃ had 337 rows overlapping S2 (excluded in the robust rerun);
  h₃′ is exploratory, not an independent replication; High p ≈ 0.87 (underpowered). No mechanism; confounding by local
  data at larger moduli unresolved. A small bulk association, not an observed kill.
* **T2T (sensitivity analysis, not a bound):** disjoint ticket families 4Cp + 1 and p + u show no positive residual
  correlation (ρ̂ = −0.005, nominal Fisher 99 % CI [−0.011, 0.001], conditional on fitted means and sampling assumptions); a common multiplier e^H would have SD(H) ≲ 1.1 % / 3 % only under the
  working model. Opposite-sign factors can mask coupling (explicit log-normal countermodel).
* CERTIFIED (this engine): the 14 zeros ≤ 10¹⁰ exactly, none in (10⁸, 10¹⁰]; min R = 2 on (10⁹, 10¹⁰] at
  1 397 190 001 = 37379² + 360.
* **Restrictions (cross-review):** Holm levels are blockwise, no study-wide alpha plan; registration is local git
  provenance, not external; the withdrawn "four orders too small" comparison and "must have density ≲ 10⁻⁴ / act only
  above 10¹³" must not be exported; S4b-r's nuisance fit is in-sample. Rare, nonlinear, density-zero or unsampled-range
  (10¹⁰–10¹² mostly unsampled) mechanisms are not excluded. B6: nothing about a fixed prime.

## 6. Lean (`LEAN_Z56.md`; Lean 4 v4.34.1 + mathlib, same pin as Z1546; no cross-model review)

* PROVED in Lean (file `lean/ES/ES/HC.lean`; audit `lean/ES/ES/AxiomsHC.lean`; 31 theorems; 26 report
  [propext, Classical.choice, Quot.sound], 3 report [propext, Quot.sound], 2 no axioms; no `sorry`, no `native_decide`):
  * (a) the five slot identities (certificate ⟹ ES); FABLE Theorem 1's coordinate form in **both** directions for every n ≡ 1 (4) (no
    coprimality, no primality); Z53_UPPER Lemma 1.1 lines U/T (no c ≥ 2 needed); HC(n) < ∞ ⟹ ES(n) for n ≡ 1 (4);
  * (b) Theorem Q: 4 | m, p = 5m² + 1 prime ⟹ p ≡ 1 (8), 12 | m, p + 4, 4p + 1 ∈ S, HC(p) ≥ 7;
  * (c) HCKILL Lemma 1.1 for every n ≡ 1 (8), prime or not;
  * (d) UPPER2 Prop 3.1: (a), (b) need neither primality nor p > 7; (c) HC(p) ≤ 8 for every prime p > 7, p ≡ 1 (4),
    p mod 840 ∉ {1, 121, 169, 289, 361, 529}.
* No discrepancy with the repo statements; several hypotheses shown unnecessary. Not formalised: the Jacobi form of
  Theorem 1, infinitude statements (Bunyakovsky, K(4)), censuses, Z53_UPPER Lemma 1.2.
* Build: `ulimit -v` makes Lean abort; a cgroup memory cap (systemd-run, MemoryMax=16G) was used instead.

## 7. Honest assessment

Wave z56 again moved main terms, averages and calibrations, not positivity at a prescribed prime. Durable outputs:
* the unconditional genus main term M_gen ≥ (5/6 − o(1))M₀ (FAMDESIGN Thm V) and a family 𝔊* whose certified zero set
  ends (so far) at 564 661 441 — the best-posed target for problem CROSS, with B2 untouched;
* FAMTRY's exceptional-set bound X·exp(−0.08√log X) for (★) (B6; novelty unverified);
* kill-side averaged/relaxed theorems (K4TRY AA, K4BILIN T\*/P, K4LIT P/P′) and a conditional model improvement
  (K4CHEN K6 on MT and the stated numerical inequality; a floating-point, not interval-certified, enclosure); K(4)
  itself unchanged;
* a two-sided calibration of the central slice (CENTRAL; EPC-conditional equivalences, unconditional Prop P);
* an EVIDENCE-level null for prime T1 with one unexplained sub-percent p − 1 signal;
* two paper drafts with referee records, unposted; the count note's almost-all theorem is now explicitly a statement
  about the line R only, in view of Akaka's (unrefereed) stronger claim for the full Type II count;
* Lean certificates for the elementary HC infrastructure.

No unconditional theorem guaranteeing positivity at an arbitrary prescribed prime, or at every sufficiently large prime,
is obtained. ES remains OPEN.
