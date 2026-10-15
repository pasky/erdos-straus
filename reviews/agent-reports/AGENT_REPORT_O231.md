# AGENT_REPORT_O231 — Spark relay Z1: forced vs unforced words, CONJECTURE U

Branch side-agent/unforced-words. side-agent/synthesis-five and side-agent/review-synthesis-five (R227) are merged in.

Deliverables:
* deep file UNFORCED_WORDS.md;
* 7 memos BRAINSTORM/z7_*.md, indexed in BRAINSTORM/README.md;
* scripts scripts/z7_* (C censuses and Python checks).

**ES is not solved, and CONJECTURE U is not proved.** No infinite case is claimed.

## SHARP
1. **All 8 known failures of N₋ ≥ U/2 at n ≡ 1 (8) have a defective n + 1 (EVIDENCE + PROVED lemma; necessary in range,
   not sufficient — R233 repair D6).** The ψ-odd part of n + 1 is
   exactly 3² in all 8 cases: R227's full list below 10⁷, plus the primes below 3·10⁷.
   * Lemma 5.2 (PROVED): on the Div(n + 1) family (t = 1 and u = 1, the largest family), the certificate count is
     (τ/2)(1 − ∏_{ψ(r)=−1}[e_r even]/(e_r + 1)). That is exactly half when some ψ-odd prime has odd exponent, and 1/3 for 3².
   * At 5 270 849 the min ≤ 2 strata give 148/333.
   * Split by the profile of p + 1, min N₋/U is: odd exponent present 0.564 (320 343 primes, 0 failures); clean 0.600;
     3² 0.475 (3 failures); other even profiles 0.549.
   * New CONJECTURE: N₋ ≥ U/2 whenever a ψ-odd prime of n + 1 has odd exponent.
2. **"N₋/U ≈ ¾, scale-stable" is a mixture of strata, not a law.**
   * Prop 5.1 (PROVED): the 2-adic Haar mass of the five-slice set on X_p(ℤ₂) is exactly 3/4 for every p ≡ 1 (4).
   * Words with large min(t, u, v) approach it (N₋/N ≈ 0.72–0.75 for min ≥ 10 and min ≥ 50, from 10⁴ to 3·10⁷; slight upward drift, saturating
     ≈ 0.74; R233 repair D7).
   * Almost the entire deficit of N₋/N, and its drift, sits in the min ≤ 2 automatic families. There the sign is a Landau event
     on p + 1, p + 2, 2p + 1, with rate ≤ 1/2 by Lemma 5.2.
   * N₋/U is 0.59 on min = 1 and 0.90 → 0.85 on min ≥ 3. These two drift in opposite directions.
3. **Prop F/F′ (PROVED).** On every family with fixed side X ∈ {p+1, p+2, 2p+1, p+3, 3p+1, p+4, 4p+1, p+7, 7p+1}
   (p ≡ 1 (8)), "certificate ⟺ unforced ⟺ X unclean".
   * Consequence: U(p) = 0 or N₋(p) = 0 forces Landau depth K(p) ≥ 4, plus p + 7 and 7p + 1 clean.
   * CONJECTURE U is *not* weaker than ES-five on any of these families. Its extra content lives on min ≥ 3 words only.
   * The t-side for t ≤ 4 was already in SPARKS4 §2.3. New here: the u/v sides, s = 7, and the equivalence with
     unforcedness.
4. **CONJECTURE U2 (EVIDENCE).** U2 counts words with A and B both unclean.
   * N₋ ≤ U2 ≤ U (PROVED).
   * U2 ≥ 1 for all primes ≡ 1 (8) below 3·10⁷. U2 = 0 only at 105 among n ≡ 1 (8) ≤ 2·10⁵.
   * min N₋/U2 = 0.62.
5. **105 is a Jacobi genus collapse (PROVED lemma + check).** Every side prime of 105's words has (r/3) = (r/5), so U = 0.
   Yet every word has two local signs ε_ℓ = −1. Per-prime forcing (Lemma 6.1) can force ε_ℓ = −1 when ℓ ≡ 3 (4). This
   explains why 3SQ has no 105 exception.

## Goals, honestly
* **(1) Prove U: not achieved.**
  * Proved: n ≡ 5 (8) is trivial (Lemma 1.1).
  * Proved: the automatic families reduce U to ES-five.
  * CONDITIONAL on Dickson: Thm 3.2. For every K, infinitely many p have all min ≤ K words forced. This is a U-analogue
    of B2, and no bounded family suffices.
  * Lemma 2.1: ψ(tn + 1) ≡ 1, so a non-certificate unforced word needs the symbol-blind event tn + 1 ∉ C_n.
  * A U-proof therefore avoids neither B1 nor B2. T1 is automatic.
  * Least-NR families (u = q; q | gcd(A, B); q | tn + 1 with NR u, v) succeed at 76–96 % of primes, never at all of them.
* **(2) Bridge: negative, with exact scope.** The Flip Lemma is an exact criterion for a family to contain a certificate,
  and it is the e-slice divisor-class condition.
  * Numerically, 96 % of non-certificate unforced words have a certificate in one of their three families.
  * Family-exact forcing collapses "unforced" to ES-five, tautologically (Remark 4.1). R227's D4/D5/D18 are
    intermediate forcing notions in this hierarchy.
* **(3)** Answered by SHARP 2 (and SHARP 1 for the refutation).
* **(4)** SQ_± records (18, 15; strictly signed 54, 30, 19, all reproduced) have forced fraction 0.84–0.94, against
  0.24–0.51 at controls. At 9 817 305, unforced words appear from |t| = 7, but the first certificate only at |t| = 54.
  3SQ: see SHARP 5.

## Verification
* z7_types.c, all 464 288 primes ≡ 1 (8) < 3·10⁷ (2 cores, ~10 min):
  * 0 Lemma S violations;
  * U ≥ 1 everywhere;
  * least-min ≥ 3 ⟺ Landau triple, 0 mismatches;
  * O230's three failure primes reproduced (N, N₋, U identical).
* All n ≡ 1 (8) ≤ 2·10⁵ including composites: only 105 has U = 0.
* Prop F/F′ family test: 0 mismatches for s = 1, 2, 3, 4, 7 (primes < 10⁵). Mismatches at s = 5, 6, 8, as expected.
* Haar mass is an exact enumeration mod 2⁵.
* T1: squares are skipped (U = 0 by definition), as in s5_U. R227 computed them.
* Caveats:
  * The stratified tables use windows, not full ranges.
  * The SQ_± split is truncated at |t| ≤ 60.
  * Lemma 5.2's SHARP is an exact count on one family. The "failure ⟹ 3²" pattern is EVIDENCE (8/8).

## Sparks (not pursued)
* Per-prime CONJECTURE U for composites ("∃ ℓ ∥odd n and a word with no ψ_ℓ-clean side"). It should be exception-free,
  like 3SQ. Compute it to 10⁶.
* Prove the refined inequality "N₋ ≥ U/2 when n + 1 has a ψ-odd prime of odd exponent", or find its first failure.
  Then iterate the defect classification to p + 2 and 2p + 1 (do 7² or 3²·7² defects appear next?).
* Automatic families beyond s = 7 in sub-classes of p mod 16 or 32. For example s = 15 when 16 | 15p + 1 makes the whole
  family certificates. Which s are automatic for which p mod 2^k? A complete list would give a Mordell-840-type theorem
  for U/ES-five, pinned 2-adically.
* At large min the forced share is ≈ 12–15 % and slowly falling. Is it ≍ 1/√log p? This would be a cleaner hardness
  law than O230's.
* SQ_± gap: why do unforced words at 9 817 305 precede certificates by |t| 7 → 54? Is it congruence-pinned forcing on
  signed sides?

## R233 repairs (applied)
D2 (ψ(r) = (−s/r) notation), D3 (2-part of M in Thm 3.2), D4 (gcd(uv, n) = 1 in Lemma 2.1; closing sentence labelled
Assessment), D5 (r ∤ 105 at 105), D6 (SHARP 1 restated as 8/8 EVIDENCE, 3² necessary-in-range, not sufficient),
D7 (large-min drift 0.719 → 0.736; window-coincidence reading labelled Assessment), D8 (Remark 4.1 last sentence
restricted to 2-adically pinned cases), D9 (|t| gap not specific to strictly signed; SQ_± claim labelled EVIDENCE),
D10 ("under Dickson's conjecture") — in UNFORCED_WORDS.md, memos z7_haar_strata / z7_symbol_blind / z7_landau_depth /
z7_signed_3sq, and this report.
