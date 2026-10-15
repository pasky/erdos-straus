# R227 — hostile review of O230 Synthesis V (SYNTHESIS_SPARKS5.md + BRAINSTORM/s5_*.md)

Reviewer branch side-agent/review-synthesis-five (merged side-agent/synthesis-five at review start). All numerics below
were recomputed with FROM-SCRATCH code (`scripts/review_r227_census.c`, `scripts/review_r227_lemmas.py`, further
`scripts/review_r227_*.py` listed per claim); none of the author's scripts were reused except as a diff target.

## Summary verdicts (filled in claim by claim)
| # | claim | verdict |
|---|---|---|
| 1 | three side numbers, Lemma S, Lemma G, side deformations, N₋ ≤ U | SOUND-AFTER-REPAIRS (minor) |
| 2 | EVIDENCE: 70–80 % residual removal; K0 = 8 defective deformation; corr; N₋/U scale law; hard primes forced | numbers SOUND (all reproduced exactly); interpretation GAP (CONJECTURE D refuted in its stated form; residuals at K0 = 4, 12, 20, 28, 33 unmentioned/unexplained; B2 sentence must be qualified) |
| 3 | CONJECTURE U | SOUND (EVIDENCE extended to 10⁷); MINOR wording on the SQ₅ implication |
| 4 | refutation of N₋ ≥ U/2 | SOUND (all four counterexamples exact; complete list < 10⁷ given) |
| 5 | Prop R | (pending) |
| 6 | Prop C | (pending) |
| 7 | uniform profinite sterility, Prop V | (pending) |
| 8 | novelty vs (J)48/(J)53/(J)55/R225 | (pending) |

## Claim 1 — side numbers, Lemma S, Lemma G, deformations, N₋ ≤ U: SOUND-AFTER-REPAIRS

Re-derivation.
* AB = (tu−1)(tv−1) = t²uv − tu − tv + 1 = t(tuv − u − v) + 1 = tp + 1; Av = tuv − v = p + u; Bu = p + v. ✓
* Lemma G: gcd(tp+1, p+u) = gcd(tp+1 − t(p+u), p+u) = gcd(tu − 1, p+u) = A because A | p+u. Holds for every n, not
  only primes. Converse (A | p+u ⇒ word) trivial. ✓ (It is a dictionary: "gcd = tu − 1" is the same as "tu − 1 | p + u".)
* Lemma S(a): ψ(A)ψ(B) = ψ(tp+1) = 1, and (−1/p) = 1. ✓ S(b): t-side (p/r) = (−t⁻¹/r) = (−t/r); u-side (p/r) = (−u/r),
  with r ∤ u (else r | p). Reciprocity (r/p) = (p/r) uses p ≡ 1 (4); for the Jacobi version at composite n ≡ 1 (4) the
  same holds by Jacobi reciprocity. ✓ S(c): **does not need (b) or reciprocity at all** — it is just multiplicativity
  of ψ and A | N_t, N_u (B | N_t, N_v). ✓ Hence N₋ ≤ U is PROVED, at primes and (Jacobi, zeros allowed) at composites.
* Role of 2: cleanliness requires ψ(2) = +1, i.e. p ≡ 1 (8) whenever N_X is even; the census includes 2. ✓
* u-side deformation: p = m² + K, s = K + u, us = □, gcd(m, s) = 1 ⇒ N_u = m² + s; an odd prime r | N_u has r ∤ ms,
  (−s/r) = 1 and (u/r) = (s/r), so ψ(r) = (−u/r) = 1. ✓ The parametrisation u = d a², K + u = d b², K = d(b−a)(b+a) is
  correct; the solution set is finite (u ≤ K²/4).
* t-side ((J)53): tK + 1 = c², gcd(m, c) = 1 ⇒ N_t = t m² + c². ✓

From-scratch checks (`scripts/review_r227_lemmas.py`; brute-force word enumeration over (t, u), not divisor-based):
all 4 280 words of primes p ≡ 1 (4) < 1200: 0 violations of Lemma G, S(a), S(b) (every odd prime of every side), S(c).
Deformations: every p ≡ 1 (8) < 1200, **every** m < √p (not only ⌊√p⌋), the complete finite u-list (via the d | K
parametrisation) and t < 200: 0 unclean u-sides, 0 unclean t-sides under the gcd conditions. K = 24 u-list
{1, 3, 8, 25} and t-list {1, 2, 5, 7, 12, …} reproduced. `scripts/review_r227_census.c` (divisor enumeration over u,
sides cleaned via the factorisations A·B, A·v, B·u) reproduces s5_sides.c column for column at all 8 976 primes
p ≡ 1 (4) < 2·10⁵ (N, N₋, N_t-clean, N_any-clean; 0 mismatches), with 0 Lemma S violations up to 3·10⁷ (see claim 4).

Defects (claim 1).
* **D1 (MINOR) s5_three_sides, Lemma S proof (b).** "r = p would force p | u, and then v(tp − 1) = 2p" treats only
  u = p. Repair: "if u = kp then A = tkp − 1 is prime to p and divides p(k+1), so tkp − 1 ≤ k + 1, impossible for
  p > 3." (And note (c) does not need (b).)
* **D2 (MINOR) s5_three_sides "Side deformations" / SYNTHESIS §1.** "t-side solutions form Pell-type infinite
  families" — tK + 1 = c² is c² ≡ 1 (mod K), i.e. finitely many quadratic progressions t = (c² − 1)/K in c; no Pell
  equation is involved. Repair: "quadratic families t = (c² − 1)/K, c² ≡ 1 (mod K)". Likewise "about τ(K)" u-side
  solutions is a heuristic; the exact count is #{(d, e, f): d | K, ef = K/d, e < f, e ≡ f (2)} (Assessment).
* **D3 (MINOR) s5_three_sides "Mechanism" (K0 = 8) and SYNTHESIS §2.** "the t-sides with 8t + 1 = c², t ≡ 1 (mod 9),
  are clean apart from an exact factor 9" is false as stated. From scratch (p = m² + 8 prime, m < 3000, 159 primes,
  c < 400, c ≡ 3 (6)): when gcd(m, c) = 3 the side is exactly 3²·(clean) in 8 709/8 709 cases; when gcd(m, c) > 3
  (e.g. 9 | m, c) the 3-adic valuation is 2, 4, 6, 8, 10 and in 629 of 1 944 cases another ψ-odd prime appears.
  Repair: add "with gcd(m, c) = 3". (The u = 1 side is always 9·(clean): 159/159.) The census numbers are unaffected
  because s5_defect.c classifies sides by actual factorisation, not by this description.

## Claim 2 — the EVIDENCE claims: numbers SOUND, interpretation GAP

From-scratch reproduction (`review_r227_census.c` mode 0, extended with square-defect columns; `review_r227_resid.py`
with leave-one-out cell means; `review_r227_k0.py`):
* (10⁵, 5·10⁶): 169 410 primes, 32 947 010 ordered words, 0 Lemma S violations; 384 cells. The residual table of
  s5_three_sides is reproduced to the 4th decimal in every row (e.g. K0 = 24: −0.1697 / −0.0826 / +0.0141; K0 = 8:
  −0.0940 / −0.0709 / −0.0737). Leave-one-out baselines change nothing visible.
* Removal shares on N₋/U vs N₋/N: [1,5) 75 %, [5,10) **22 %**, [10,17) 84 %, [17,30) 66 %, [30,100) 72 %,
  [100,300) 81 %. "≈ 70–80 % for 10 ≤ K0 < 300" is fair (66–84 %).
* K0 = 16: +0.0083 ± 0.0039, K0 = 24: +0.0141 ± 0.0060 (2.1σ, 2.4σ *positive*): "explained completely" is fair, but it
  slightly over-corrects; say "explained (small positive overshoot)".
* Square-defect: K0 = 8 share 0.451, χ = −1 rate 0.485 vs 0.784; generic (K0 ≥ 300) 0.743 vs 0.755, share 0.113 —
  all reproduced.
* (0, 3·10⁷): 928 779 primes, 220 667 727 words, 0 violations; scale table (forced 0.209 → 0.114, N₋/N 0.591 → 0.668,
  N₋/U 0.747 → 0.754, forced·√log 0.56 → 0.47) reproduced; p mod 8 split 0.7699 / 0.7398.
* p < 10⁶: corr(N₋, U) = 0.966, corr(N₋, N) = 0.904, N₋/U mean 0.768, sd 0.077; the 13 primes with N₊ ≥ 4N₋ have
  U − N₋ ∈ {0, 2} (= N₊ − N_forced) and forced fraction 0.78–0.89; 21 of 39 095 primes (0.05 %) have forced ≥ 0.78;
  16 primes with U < 16, 15 with N₋ = U. All reproduced, **but only on (10³, 10⁶)**: p < 10⁶ has 39 175 primes and then
  24 primes with U < 16, 18 with N₋ = U.
* Block minima to 3·10⁷ (my least-N₋ prime per dyadic block, b = 10..24): forced fraction 0.547–0.892, U − N₋ ≤ 4. The
  catalogue's 8 rows are a subset of the 15 blocks (blocks 10, 12, 15, 16, 18, 20, 21 omitted: 1 201, 5 569, 43 969,
  76 441, 351 289, 1 095 481, 4 149 601 — same pattern).

Statistics. Naive SEs are honest per bin; the per-K0 table is a post-hoc selection of 3 of ~20 occupied K0 values, so
the K0 = 16/24/8 statements need a multiple-testing caveat; the large effects (K0 = 8 at 14σ) survive any Bonferroni.
The "after removing clean sides" statistic N₋/U is not the same statistic as N₋/N; its near-zero residual says that
**unforced words at near-squares are not depleted**, which is the right (and non-circular) reading; the author's
wording "removes 70–80 % of the depletion" should say that.

Defects (claim 2).
* **D4 (MAJOR) s5_three_sides "Mechanism"/CONJECTURE D and SYNTHESIS §2, §5(a): the "defective deformation" story is
  mis-located and CONJECTURE D is false as stated.** From scratch (`review_r227_k0.py`): at K0 = 8 the depleting side is
  the **u = 1 side** N₁ = p + 1 = m² + 9 = 9(m′² + 1), which carries ≈ 62 of the ordered words per prime (no congruence
  restriction on A = t − 1 | p + 1); on it χ = −1 iff 3 ‖ A, and the observed rate is **exactly 1/3 (0.333)**, the
  divisor count of 3² · (clean). The control K0 = 48 (p + 1 = m² + 49, ψ(7) = −1) shows the same law: u = 1 side rate
  0.333 when 7 | m (32 primes), 0.000 when 7 ∤ m (130 primes). But the other defective deformation with forced 3 | m,
  **K0 = 20** (u = 16: p + 16 = 9(m′² + 4), m′ odd), has χ = −1 rate **1.000** on its words (204 words / 70 primes), and
  K0 = 20's square-defect words overall have rate 0.794 (not depleted). Proof of the K0 = 20 enrichment (elementary,
  my derivation): every odd prime r | m′² + 4 is ≡ 1 (4) with ψ(r) = (−16/r) = 1; A | p + 16, A ≡ −1 (mod 16) forces
  A ≡ 3 (mod 4), hence an odd power of 3, hence 3 ‖ A, and ψ(3) = (20/3) = −1. So a defective side forces χ = −1 when
  the congruence A ≡ −1 (mod u) pins the parity of the defect. Repair: replace CONJECTURE D by "a defective side with
  an unrestricted divisor set (u = 1: p + 1 = r²·clean, ψ(r) = −1) gives χ = −1 rate 1/3 (K0 = 8, 48: verified);
  defective sides with u > 1 can force χ = −1 outright (K0 = 20, proved)".
* **D5 (MAJOR) SYNTHESIS (I2), §4(i), s5_three_sides "Barrier screen" B2: "cleanliness only ever forces χ = +1 … the
  three-side theory cannot produce a certificate" is contradicted by D4.** Defective cleanliness plus the side
  congruence forces χ = −1 on all words of the side (K0 = 20, u = 16). This does not escape B2 (a word with u = 16
  still needs a divisor A ≡ 15 (mod 16) of p + 16, i.e. 3c with c ≡ 5 (mod 16) built from primes of m′² + 4), and the
  family is polynomial in m (B1). Repair: "clean sides only force χ = +1; *defective* sides can force χ = −1 under the
  side congruence, but only conditionally on a divisor in a class (B2)".
* **D6 (MINOR→MAJOR for the synthesis) unexplained residuals are not listed.** Per-K0 residuals of N₋/U (my run):
  K0 = 4: −0.016 ± 0.004, 12: −0.025 ± 0.004, **20: −0.039 ± 0.007**, **28: −0.032 ± 0.003**, 33: −0.023 ± 0.005
  (all ≥ 4σ), and the [5, 10) bin keeps 78 % of its residual. The memo mentions 4, 12, 28 as "weaker"; 28 is 10σ and 20,
  33 are not mentioned. At K0 = 4, 12, 20, 28 the square-defect words are *not* depleted (rates 0.76–0.79); the deficit
  sits on the other unclean words (0.67–0.71). Repair: list these in §2 as open residuals not explained by any side
  mechanism; drop "explains most of the near-square depletion" from §5(a) or qualify it with "aggregated over K0 bins".
* **D7 (MINOR) s5_unforced_words:** "over the 39 095 primes p ≡ 1 (mod 4), p < 10⁶" → "(10³, 10⁶)"; the "16 primes with
  U < 16, 15 with N₋ = U" is also for (10³, 10⁶). SYNTHESIS §3 bullet 1 "(median ≈ 0.12)" is attached to the block
  minima but is the all-prime median (0.109 for p < 10⁶, 0.090 to 3·10⁷); reword. The catalogue omits 7 of 15 blocks
  (say "selected blocks" or add them). §3 "0.739" vs memo "0.740" (pooled 0.7398).
* **D8 (MINOR) s5_scale_law "the whole drift is the forced fraction".** N₋/N = (N₋/U)(1 − f) is an identity; the
  content is only that N₋/U drifts less (0.747 → 0.754, monotone, not flat). forced·√log p falls 0.56 → 0.47 (−16 %), so
  "≈ 0.5/√log p" is a rough description, not a fit; the Landau/Serre (log)^{−1/2} order for *three correlated sides of
  sizes p and p²* is a heuristic (Assessment), and the prediction "N₋/N → 0.75" is a CONJECTURE, not EVIDENCE.

## Claim 3 — CONJECTURE U: SOUND (EVIDENCE extended)

From scratch (`review_r227_census.c` mode 1, Jacobi ψ, zeros allowed in "clean"): **all 2 498 419 odd non-square
n ≡ 1 (4), 5 ≤ n < 10⁷: U(n) = 0 only at n = 105**, and N₋(n) = 0 only at n = 105 (i.e. χ-form SQ₅ also holds there);
0 Lemma S violations. T1 control: all 1 580 odd squares < 10⁷ computed (not assumed) with U = N₋ = 0.
* **D9 (MINOR) s5_unforced_words "CONJECTURE U is implied by SQ₅".** True only for SQ₅ in the form "∃ word with
  χ = −1" (then N₋ ≥ 1 ⇒ U ≥ 1). DISCOVERIES (J)… also phrases SQ₅ as "χ not identically +1", which at composite n
  allows χ = 0 words — and χ = 0 words can be forced (ψ(r) = 0 counts as clean). Repair: state the implication from the
  χ = −1 form; note that the census shows N₋ ≥ 1 for every non-square n ≢ 105 < 10⁷, so the two forms agree on the range.
  The equivalence is also *only* "⇒" from SQ₅; U(105) = 0 is a computed fact.

## Claim 4 — refutation of N₋ ≥ U/2: SOUND

Exact recomputation (independent enumeration): 5 270 849: N = 505, N₋ = 192, U = 389; 17 188 937: 413 / 164 / 345;
21 387 257: 289 / 126 / 259; 110 897 = 43·2579: 109 / 44 / 97. All primes (`factor`), all ≡ 1 (4). The census of all
928 779 primes ≡ 1 (4) below 3·10⁷ gives exactly these three prime failures, and min N₋/U below 5·10⁶ = 122/241 at
3 103 073. Complete list of failures among all n ≡ 1 (4) < 10⁷: 110 897, 1 512 089, 2 152 097, 3 000 329,
4 095 125 = 5³·181², 5 270 849, 9 948 977 (one prime). The steering note ("no involution") is correctly drawn.
