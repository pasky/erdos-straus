# AGENT_REPORT_O197 — what makes 4/n special among m/n? (spark relay R, after B7)

Branch `side-agent/model-specific` (TES_FINITE merged as instructed). Main file **MODEL_SPECIFIC.md**; scripts
`scripts/ms_*`; data `data/ms/` (≈ 1 MB). ES is not solved; no infinite case claimed.

## SHARP:
**Thm 3.1 (PROVED, finite cell check relative to DEDEKIND Cor 4.1 = Hirzebruch–Zagier + Rademacher): m = 4 is the
unique numerator m ≥ 4 whose five length-3 HJ slices are determined by the Jacobi character χ = (−A/n).** For odd n and a word (t,u,v) ≥ 1 with
tuv − u − v = n, A = tu − 1, put χ = (−A/n). The five m-slices (m | tu−1, m | tv−1, m | t, m | u, m | v) each give
an explicit solution of m/n (Lemma 3.0). Then: S_4 = {χ = −1} exactly (all odd n; for n ≡ 3 mod 4 new in this form);
for 4 | m, m ≥ 8: S_m ⊊ {χ = −1} (7/12 of the χ = −1 cells for m = 8, 16/45 for 12, 5/16 for 16; properness proved
for every such m); for 4 ∤ m: S_m contains χ = +1 members and χ = +1 non-members (explicit words, all m). Consequence: **on the
length-3 ball, "T1 is the only obstruction" is an identity for ES and false for 8/n** — the same surface
X_n: tuv − u − v = n carries both, and at n = 131, 241 it has χ = −1 points (29 resp. 12) but none in the 8-target
cells (and 8/n has no solution). So λ(p) ≤ 3 / CONJECTURE SQ₅ is a numerator-free statement (non-residues in the
Farey ball) that implies ES and does not imply 8/n: genuinely model-specific input of the kind B7 demands.
Equivalently (C1): SQ₅ ⟺ "χ is constant on the positive integral points of X_n only for squares (and 105)".
Boundary words handled by Lemma 3.0′ (reduction to length 2). Checked independently on all 35 179 words of odd n ≤ 1500 (sympy Jacobi, every slice solution verified in exact
rationals).

## Results
1. **Censuses (CERTIFIED, complete search, `ms_census.c`)**: failing odd primes p ∤ m ≤ 10⁸ for m = 4..20, 24 (21–23 to 10⁷).
   Exact agreement with Pomerance–Weingartner Table 1 (m ≤ 15); new lists m = 16–24, incl. m = 20 failing at the prime
   **2763601** (≡ 1 mod 840; gap from 90001) and m = 24 at 620929. Largest failures independently re-confirmed by
   O194's `tf_schinzel.count` (0 solutions; next 20 primes solvable). Odd squares ≤ 10⁸ as T1 control.
   Observation (EVIDENCE): multiples of 4 have much longer tails than neighbours (241 vs 2/19; 12241 vs 37/281;
   2763601 vs 353/14051); m = 4 is the only multiple of 4 without failures.
2. **Parity (PROVED, Lemma 2.1)**: for odd n every ES solution is all-even or has exactly one odd denominator;
   all-even ⟺ 8/n (bijection), ⟺ d even in ET coordinates. f_4 = f_8 + f_4^{odd}; all-even share ≈ 0.45.
   **EVIDENCE: the one-odd half alone never fails, primes ≤ 10⁸**; 8/n's own one-odd half fails also at 59, 449.
3. **Count law & luck (EVIDENCE + Assessment, §5)**: mean f_m ≈ c_m log³p/m with c_m/c_4 ∈ [0.7, 1.16] (prime m high,
   divisor-rich m low). Low counts: square coset suppressed to ≈ 0.25–0.33 of the mean for 4 | m, 0.6–0.75 for
   m = 5, 7; min normalised count 0.11 (m = 4) vs 0.02 (m = 8). Hardness correlates along the divisor lattice
   ((4,8) 0.88, (8,16) 0.89, (4,5) 0.41). A pooled failure-rate model F(μ) (binned by fitted mean, validated
   leave-one-out within ×1.3 for the 4 | m pool, ×3–4 for the other pool) predicts **0.84–1.45 ES failures among primes
   5..10⁷, a plug-in ≈ 0.02 of them above p = 100** — ES's clean record is mildly lucky (P ≈ 0.23–0.43 if Poisson)
   and the small-p "luck" is shared (more strongly) by m = 5, 6, 7, so the curve overestimates tiny-p failures. 8/n's failures at 131, 241 are its expected outcome (mean ≈ 13 there). So the
   empirical 4-vs-8 difference is consistent with a mean-count explanation needing no 4-specific structure; the 4-specificity of Thm 3.1 is about *which*
   certificates exist.
4. **B7 screen (§6)**: five slices — 4-specific (S_8 fails at 27 primes ≤ 10⁷, last 259201; S_4 at none ≤ 10⁷);
   one-odd half — 4-specific, numerical only; Type I alone — survives for 8/n too (fails only at the 5 true failures),
   so not a discriminator; Type II alone fails for 8/n (22 primes, last 35569); cube shots p+1, p+m, mp+1 — fail for
   both (942 for ES, reproducing (J)25; 4308 for m = 8; only 102 for m = 5); identity covering at level 840 —
   ES uncovered = exactly Mordell's 6 square classes, 8/n: 35 (29 non-square, containing 131 and 241).

## Honest caveats
* Thm 3.1 rests on DEDEKIND Cor 4.1 ((D2) + Rademacher's congruence, cited from memory there); extended to boundary
  words by Lemma 3.0′; re-verified against sympy on 129 538 words and at word level for n ≤ 1500. Equal cell
  fractions on both χ-halves for 4 ∤ m is a computation for 5 ≤ m ≤ 15 only.
* Self-review (deep reviewer) found 2 P1 + 7 P2 issues, all repaired (MODEL_SPECIFIC §8): a binning bug in ms_tail
  (numbers above corrected), an out-of-sieve read in ms_census (prime censuses provably unaffected, all re-run
  identical), undercounted slice words, boundary words, a withdrawn length-r claim in §7.
* §5's model is an Assessment: μ is a 2-parameter fit extrapolated below p = 100 for m = 4..7; the pooled curve
  overestimates small-p failures for small m (3.4–7.8 expected for m = 4..7 combined, 0 observed).
* Thm 3.1 does not make SQ₅ easier per se; it pins down that a proof via X_n must exploit the χ-fibre target
  (an equidistribution-mod-8 statement for X_p's points is false at 27 primes).

## Sparks (not pursued)
1. **χ-flipping move on X_n** (C3): any map between positive points of tuv − u − v = n flipping χ at prime n proves ES
   on the slices (must fail at n = 105). Search affine/Möbius moves on X_n with χ(w′) = −χ(w).
2. **One-odd half of ES never fails (to 10⁸)**: find its structural reason; check whether the S_4 words whose
   solution is one-odd still fill a χ-fibre (parity of the slice solution is a cell function mod 16).
3. The length-r analogue of Thm 3.1: for which (m, r) is the r-slice certificate set a χ-fibre? If only m = 4 at all
   r, that is a clean "4 is unique" theorem across HJ length.
4. m = 5's identity covering is exceptional (10 uncovered classes of 23040 at level 120120, and S_5 never empty to
   10⁵): Sierpiński 5/n may be the most "identity-like" numerator; compare with PW's 10¹⁸ verification.
5. m = 20's isolated failure at 2763601 ≡ 1 (mod 840): a test case for the pooled tail model at large μ (predicted
   rate ≈ 10⁻⁶ at μ ≈ 50–70; one observed).
