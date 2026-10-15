# R227 — hostile review of O230 Synthesis V (SYNTHESIS_SPARKS5.md + BRAINSTORM/s5_*.md)

Reviewer branch side-agent/review-synthesis-five (merged side-agent/synthesis-five at review start). All numerics below
were recomputed with FROM-SCRATCH code (`scripts/review_r227_census.c`, `scripts/review_r227_lemmas.py`, further
`scripts/review_r227_*.py` listed per claim); none of the author's scripts were reused except as a diff target.

**Repairs applied (R227 repair, author idle after checkpoint 1):** SYNTHESIS_SPARKS5 §0 (I2)/(I3), §1, §2, §3, §4 rows
(ii)/(iv)/(v), §5; memos s5_three_sides (D1–D6, D17, D18), s5_unforced_words (D7, D9, D18), s5_scale_law (D8),
s5_reciprocity_forcing (D10, D11), s5_cm_frobenius (D12), s5_sterile_uniform (D14–D16). D13 left as a suggestion.
DISCOVERIES/AGENT_REPORT not edited (parent's ledger; AGENT_REPORT SHARP 2 and the Prop R example list need the same
wording when the parent writes the (J) entry).

**Overall: no FATAL. 6 MAJOR (D4, D5, D10, D14, D15, D18), the rest MINOR.** Every number in the synthesis was
reproduced exactly with independent code; the defects are in interpretation, scope and labels. ES is not solved.

## Summary verdicts
| # | claim | verdict |
|---|---|---|
| 1 | three side numbers, Lemma S, Lemma G, side deformations, N₋ ≤ U | SOUND-AFTER-REPAIRS (minor) |
| 2 | EVIDENCE: 70–80 % residual removal; K0 = 8 defective deformation; corr; N₋/U scale law; hard primes forced | numbers SOUND (all reproduced exactly); interpretation GAP (CONJECTURE D refuted in its stated form; residuals at K0 = 4, 12, 20, 28, 33 unmentioned/unexplained; B2 sentence must be qualified) |
| 3 | CONJECTURE U | SOUND (EVIDENCE extended to 10⁷); MINOR wording on the SQ₅ implication |
| 4 | refutation of N₋ ≥ U/2 | SOUND (all four counterexamples exact; complete list < 10⁷ given) |
| 5 | Prop R | SOUND as a tautology; GAP in scope ("local-invariant" undefined; listed examples not shown to be local invariants); can be strengthened to the genus |
| 6 | Prop C | SOUND (verified for general M); MINOR: the √p twist is redundant for certificates, (c) is a one-way inclusion |
| 7 | uniform profinite sterility, Prop V | GAP (Prop V false/vacuous as literally stated — ℤ ↪ ℤ̂ is injective; conclusion overreaches from "fixed finite family" to "ES"; "sign avoidable" rests on CONJECTURE SQ_±) — repairable, then = B1 (PROVED) + Assessment |
| 8 | novelty vs (J)48/(J)53/(J)55/R225 | partly new; the u-side idea is R225's (who proposed exactly the "u-level clean test"); R225's congruence mechanism is NOT inside Lemma S and is missing from the census (MAJOR for §2/§3 interpretation) |

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
  family is polynomial in m (B1). A second, even simpler example: sides N_u = p + u whose odd primes are all ≡ 1 (4),
  with u ≡ 3 (4): for odd A ≡ −1 (mod u), χ = (−u/A) = (A/u) = (−1/u) = −1 (e.g. p = 17, w = (2, 3, 4), N_u = 20,
  χ = (5/17) = −1). Both are instances of the three-bit law (χ is a function of w mod 8): "forcing" by a side is a
  statement about which cells the side's words can occupy, and the sign it forces depends on the genus character used.
  Repair: "*ψ-clean* sides only force χ = +1 (Lemma S); other side conditions (defects, (−1/·)-cleanliness) combined
  with the side congruence A ≡ −1 (mod u) can force χ = −1, but only conditionally on a divisor in a class (B2)".
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
  χ = −1" (then N₋ ≥ 1 ⇒ U ≥ 1). DISCOVERIES (J)32 (line ≈ 861) also phrases SQ₅ as "χ not identically +1", which at composite n
  allows χ = 0 words — and χ = 0 words can be forced (ψ(r) = 0 counts as clean). Repair: state the implication from the
  χ = −1 form; note that the census shows N₋ ≥ 1 for every non-square n ≢ 105 < 10⁷, so the two forms agree on the range.
  The equivalence is also *only* "⇒" from SQ₅; U(105) = 0 is a computed fact.

## Claim 4 — refutation of N₋ ≥ U/2: SOUND

Exact recomputation (independent enumeration): 5 270 849: N = 505, N₋ = 192, U = 389; 17 188 937: 413 / 164 / 345;
21 387 257: 289 / 126 / 259; 110 897 = 43·2579: 109 / 44 / 97. All primes (`factor`), all ≡ 1 (4). The census of all
928 779 primes ≡ 1 (4) below 3·10⁷ gives exactly these three prime failures, and min N₋/U below 5·10⁶ = 122/241 at
3 103 073. Complete list of failures among all n ≡ 1 (4) < 10⁷: 110 897, 1 512 089, 2 152 097, 3 000 329,
4 095 125 = 5³·181², 5 270 849, 9 948 977 (one prime). The steering note ("no involution") is correctly drawn.

## Claim 5 — Prop R: SOUND as stated for rational local classes; scope GAP

Re-derivation. Q_w = v x² + t y² + u z² − 2xy − 2yz, det = tuv − u − v = p. For odd ℓ ≠ p, L_w ⊗ ℤ_ℓ is unimodular, so
ε_ℓ = 1; ε_p = χ(w) (CHI_FLIP Thm 1.1, ε_ℓ = (−A/ℓ)^{v_ℓ(n)}, valid for signed words — R219); ε_∞ from the signature
(SPARKS4 L1); ternary ℚ_v-spaces are classified by (det, Hasse) ⇔ (det, isotropy); Hilbert reciprocity ε₂ε_pε_∞ = 1.
So the family of ℚ_v-classes is a function of (ε₂, ε_∞), ε₂ of the ℤ₂-class, hence of the Gram matrix mod 8, i.e. of
w mod 8. ✓ From scratch (`scripts/review_r227_propR.py`): all signed words with |t|, |u| ≤ 60 of all odd n < 400
(19 055 words with gcd(A, n) = 1, primes and composites, Jacobi χ): χ is a function of (t, u, v mod 8, sign vector) —
1 270 cells, 0 clashes.

Defects.
* **D10 (MAJOR, scope/label) s5_reciprocity_forcing Prop R and SYNTHESIS §4(ii); AGENT_REPORT "(Hilbert, Maslov,
  Dedekind/Rademacher, theta multiplier)".** "Every function Φ of the local invariants of Q_w" is a tautology once
  the local classes are shown to depend only on (ε₂, ε_∞); the content is entirely the three-bit law (SPARKS4). The
  memo never defines "local-invariant index", and the listed examples are not shown to factor through the local
  classes:
  - "Hilbert symbols": individual symbols (a_i, a_j)_v of a diagonalisation are *not* isometry invariants (they depend
    on the diagonalisation, and at odd ℓ ≠ p they can be −1 in pairs); only the Hasse invariant is. Say "Hasse
    invariants".
  - "Dedekind-sum residues via Rademacher–Grosswald": 12N·s(h, N) ≡ N + 1 − 2(h/N) (mod 8) involves a Jacobi symbol
    (h/N), a *global* reciprocity quantity of the pair (h, N); it is a cell function only for those (h, N) whose
    Jacobi symbol is itself expressible through (ε₂, ε_∞) (e.g. (−u/A) = χ). Dedekind sums themselves (not residues
    mod 8) are not local. State exactly which (h, N).
  - "theta multipliers": the multiplier of θ_{Q_w} depends on the level and the determinant of the *lattice*, not on
    the ℚ_v-classes; it happens to be constant here (level 4p for every w, since det = p and adj(G) ≢ 0 mod p), which
    makes it trivially a cell function, but not "via Prop R".
  - "Maslov/inertia indices": fine if they mean the signature of Q_w ⊗ ℝ; the TRANSPORT_LAW (J)45 Maslov products are
    along *paths of words* and the memo should say which index of which form is meant.
  Repair: define "local invariant of w" := a function of the family of ℤ_v-isometry classes (L_w ⊗ ℤ_v)_v (the genus
  of L_w). Then Prop R holds in that *stronger* form (my derivation, Assessment-level check): at odd ℓ ≠ p, unimodular
  ⇒ class fixed by det; at p, det has v_p = 1 so the ℤ_p-class is fixed by ε_p; at 2 the ℤ₂-class of an odd-det
  (unimodular) lattice is determined by its Gram matrix mod 8, a function of w mod 8. So **the genus of L_w is a
  function of (w mod 8, sgn w)**, and every genus invariant (mass, Siegel–Weil average, theta multiplier, Hasse,
  signature) is a cell function. Replace the list of examples by this definition, and say "non-local" = depends on
  the class of L_w inside its genus (class number data, representation numbers) — which is exactly where (J)48/(J)39
  put the counting input. Label: PROVED (with that definition); the reading "reciprocity relocates signs, never
  creates points" is Assessment.
* **D11 (MINOR) Prop R statement "p an odd prime".** The local computation also holds for odd composite n with
  gcd(A, n) = 1 (my check covers composites); say so or keep prime but note it.

## Claim 6 — Prop C: SOUND, with two scope remarks

Re-derivation. p ∤ M ⇒ ℚ(√p) ⊄ ℚ(ζ_M) (p ramifies in ℚ(√p) only), so Gal(K_M/ℚ) = (ℤ/M)^× × {±1}, g = (−1, −1) of
order 2; α = √p(ζ − ζ⁻¹) is g-fixed, α² = p(ζ − ζ⁻¹)² = p(θ² − 4) < 0 at every real embedding of ℚ(ζ)⁺ (|θ| < 2);
[F_M : ℚ] = φ(M) = 2[ℚ(ζ)⁺ : ℚ] (M ≥ 3); CM ✓. (b) Frob_h = (h mod M, (p/h)) and (p/h) = (h/p) ✓; "splits completely
in F_M" ⟺ Frob ∈ ⟨g⟩, and "not in ℚ(ζ)⁺(√p)" excludes Frob = 1 ✓. (d) θ = 0 for M = 4: F₄ = ℚ(√−4p) = ℚ(√−p) ✓;
non-principal genus of −4p ✓.
From scratch (`scripts/review_r227_propC.py`): actual splitting (root count of the characteristic polynomial of a
primitive element of F_M mod h) vs the Frobenius prediction, for M ∈ {5, 7, 9, 15, 16, 20, 24} (odd M and non-
squarefree M included), p ∈ {5, 13, 17, 29, 37, 41}, primes h < 1500: 9 128 checks, 0 mismatches. Remark: for
M = 16, α alone generates only a quartic subfield (α² = p(√2 − 2) ∈ ℚ(√2)), so "F_M = ℚ(ζ_M)⁺(α)" must not be read as
"F_M = ℚ(α)" — the author's formula is correct as written.

Defects.
* **D12 (MINOR) Prop C(c), reason for inertness.** For h prime, h | p + 4c²d and h ≡ −1 (mod 4cd): (p/h) = (−d/h) = −1
  by BRIDGE_WORLDS Thm (i) (line ≈ 136); this is why the twist bit is automatic. The memo's "automatic … χ = ψ(h) = −1"
  cites the wrong reason (h is not the A of a word). Consequence: **the √p-twist carries no information beyond (J)50**
  — "Frob = g in K_{4cd}" ⟺ "Frob = c_∞ in ℚ(ζ_{4cd})" for primes dividing p + 4c²d. The CM field F_M is a
  repackaging; state that explicitly (PROVED dictionary, zero new content). The brief's / table's "certificate primes ⟺
  Frobenius c_∞σ_p" is only "⟹"; "⟸" needs h | p + 4c²d (B2), which the memo does say in the next bullet.
* **D13 (MINOR) T1 reading.** "At p = m², g is not an element of Gal(K_M/ℚ)" is right, but the operative T1 fact is
  again BRIDGE_WORLDS (i): h | m² + 4c²d makes −d a QR mod h, contradicting (−d/h) = −1. Cite it; the field-theoretic
  phrase is a restatement (Assessment).

## Claim 7 — (v) uniform profinite sterility, Prop V: GAP (label)

Re-derivation of what is true: a fixed finite family F of linear/ET families covers a finite union of residue classes
U_F ⊂ R̂, which is **clopen**; if s ∈ 𝒮 (so s ∉ U_F) then a whole neighbourhood s + Nℝ̂ avoids U_F, and it contains
infinitely many primes (Dirichlet / Kornblum, s a unit). Hence no fixed finite family covers the cell — this is B1,
PROVED (given (J)51/(J)54/(J)56 for 𝒮 ≠ ∅).

Defects.
* **D14 (MAJOR) s5_sterile_uniform Prop V and "Consequence (formal)".** (a) "P determined by the image of p in R̂" is
  vacuous: ℤ → ℤ̂ and F_q[T] → F_q[T]^ are injective, so *every* property of p is a function of its image (including
  ES-five(p) itself, and |p|). Taken literally, Prop V says that no true property of primes implies ES on the cell —
  which is false if ES is true (take P = ES). Repair: "P is **locally constant** on R̂ (equivalently, depends only on
  p mod N for one fixed N)". Same repair for "data that is not a function of the image of p in R̂" → "not locally
  constant on R̂". (b) The proof's "a certificate in a fixed family is an open condition, and s ∉ ⋃U_f" does not give
  a neighbourhood of s avoiding ⋃U_f — an open set can accumulate at s. It needs U_f **closed** too (true: finite unions
  of residue classes are clopen); say so. (c) The conclusion "P does not imply ES on that cell, because the primes near
  s have no certificate in any fixed finite family" is a non sequitur: ES at those primes may use families outside F.
  What is proved is "P does not imply a certificate from a fixed finite family" (B1). Label: PROVED only after
  (a)–(c); then it is B1 restated, as the memo itself says.
* **D15 (MAJOR, label) s5_sterile_uniform "Reading" and Assessment; SYNTHESIS §4(v).** "(J)52 shows that dropping
  positivity … does not help (SQ_±)" and "sign data (positivity) is avoidable (SQ_±)" rest on **CONJECTURE SQ_±**
  (EVIDENCE only, DISCOVERIES (J)52). Must read "conditionally on SQ_±" / Assessment. Likewise "the only such data
  available in either ring is the place at infinity" is an Assessment (no classification of non-locally-constant
  data is proved; e.g. lnr(p) is not locally constant at a sterile point and is not "the place at ∞").
* **D16 (MINOR) s5_sterile_uniform.** "(J)56 (F_q[T], every q = 3^r except q = 3)" omits "(and q = 9 at k = 1)"
  (DISCOVERIES (J)56 title); the ℤ column "ES^{(S)}, |S| ≥ 4" is a mute *set* result for non-square n coprime to 2S,
  ineffective ((J)23 Thm 2.4(a)) — add these qualifiers to the comparison table.

## Claim 8 — novelty vs (J)48/(J)53/(J)55 and R225

* t-side: THREE_SQUARES Lemma 1.4 / NEAR_SQUARE Prop 4.1, correctly credited.
* **u-side: R225 (reviews/near-square-review.md, "Partial mechanism for the beyond-clean gradient") already had
  (i) the observation p + u = A·v ⇒ χ = (−u/A) by reciprocity, (ii) the deformation K0 + u = s², and (iii) the explicit
  proposal "that u-level 'clean' test (the analogue of Prop 4.1 on the u-side) is the natural next candidate for the
  remaining gradient".** O230 executes that proposal in the ψ-form (Lemma S on N_u, N_v) and adds the u(K + u) = □
  deformation and the census. Credit should say "R225 proposed the u-level clean test; O230 carries it out
  symmetrically" rather than "R225 had the u-side idea in the narrower form K + u = s²" (D17, MINOR).
* **D18 (MAJOR for the interpretation of §2/§3) R225's mechanism is not a sub-case of Lemma S and is missing from the
  census.** R225's forcing uses the *side congruence* A ≡ −1 (mod u) together with (−1/·)-cleanliness of p + u, not
  ψ-cleanliness; such words are counted as *unforced* in U. From scratch (`scripts/review_r227_r225side.py`, primes
  p = m² + K0 in (10⁵, 5·10⁶), u = s² − K0, s < 60, gcd(m, s) = 1, all u incl. even): unforced words on these sides
  per K0 = 4, 12, 20, 28, 8, 16, 24: 772, 232, 266, 480, 74, 234, 56, **all with χ = +1 (0 exceptions in 2 114)**.
  Removing them raises N₋/U at K0 = 4: 0.709 → 0.728, 12: 0.723 → 0.730, 20: 0.691 → 0.705, 28: 0.719 → 0.726 (the
  p ≡ 5 (8) baseline is 0.740), i.e. a sizeable part of the residuals of D6 is R225's mechanism. Consequences: (a) U
  over-counts the genuinely undetermined words, so "N₋ ≤ U" is not the sharpest bound and the forced fraction is
  under-counted; (b) "three-side cleanliness explains …" should become "three-side ψ-cleanliness plus R225's
  congruence-pinned u-sides explain …"; (c) the scale-law and hard-prime statements are unaffected numerically
  (they are about U as defined) but their "forced = all deterministic χ = +1" reading is wrong. Repair: add R225-type
  sides (and, generally, sides whose ψ-odd part is pinned by A ≡ −1 (mod u)) as a second forcing class, or state that
  U counts only ψ-clean forcing.
* Lemma G, Prop R, Prop C, (v): dictionaries over (J)40, SPARKS4 three-bit law, (J)50, B1 respectively; the memos say
  so. The forced/unforced split, CONJECTURE U and the N₋ ≥ U/2 refutation are new to the campaign as far as I can see
  (grep of DISCOVERIES/BRAINSTORM for "unforced", "U(n)": no earlier occurrence).
