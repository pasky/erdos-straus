# THREE_SQUARES — the three-squares side of the ES sign and the adelic "continuity of T1" (task O217, spark relay Y8)

Status: checkpoint 1 (O217), repaired after self-review R-O217 (deep reviewer; repairs marked "R-O217"). **ES is not solved here, nor any infinite case of it.** Labels as in DISCOVERIES.md.
Builds on TWO_FIBRES.md (O209: Thm A, Thm B), SIGN_IDENTITY.md ((J)39), CHI_FLIP.md ((J)33), STERILE_STEER.md ((J)27).
Memos BRAINSTORM/y8_*.md (6); scripts `scripts/y8_*`.
Notation: p ≡ 1 (4) prime (p ≡ 3 (4) is trivial: (p + 2, 1, 1) has χ = −1); word w = (t, u, v), tuv − u − v = p,
A = tu − 1, A* = tv − 1, AA* = tp + 1; χ(w) = (−A/p) = (A/p); level of w := t; q = lnr(p) (least non-residue).

## Summary
1. **The continuity of T1 is adelic at the √p scale, and archimedean only through T1-type levels (EVIDENCE + PROVED
   mechanisms; R224 repair: the checkpoint said "not archimedean").** Over all
   39 174 primes p ≡ 1 (4) below 10⁶, the mean of N₋/N is 0.643–0.647 in every bin of width 0.1 of dist(p, ℤ²)/√p (no
   association detected at that scale), but at bounded p − m² there is a 6–7σ deficit of χ = −1 words (R224: p − m² = 4
   or 16: −0.05 against adelically identical primes), explained by Lemma 1.4: if p = m² + k and tk + 1 = c² then
   tp + 1 = tm² + c² and level t is (odd-)clean — T1's identity tm² + 1 with 1 replaced by c². By lnr the mean falls
   monotonically with lnr(p): 0.645 (q = 3), 0.604, 0.565, 0.516, 0.481, 0.452, 0.442, 0.430 (q ≥ 23), p ≡ 1 (8).
   (Agrees with R214's correction: the worst primes are p ≡ 1 (24) with (p/5) = (p/7) = +1.)
2. **Clean levels (PROVED, §1).** χ(w) = ∏_{r | A} (r/p)^{v_r(A)}; call level t clean if every prime r | tp + 1 has
   (r/p) = +1. Clean ⇒ all level-t words have χ = +1. T1 is "every level clean" (tm² + 1 = 1² + t·m²), and
   conversely **an odd n is a square ⟺ every (odd-)level is clean** (Prop 1.3). Primes r < lnr(p) have (r/p) = +1 (R224 repair), and the
   exact reciprocity constraint ∏_r (r/p)^{v_r(tp+1)} = +1 forces cleanliness when tp + 1 = s·ℓ^e with s
   (lnr − 1)-smooth, ℓ prime, e odd ("rank-one sterility"; R-O217: rough primes with even exponent stay free).
3. **A calibrated law (EVIDENCE, §2).** Model: exact Legendre signs for r ≤ 100, fair coins above, conditioned on the
   reciprocity constraint. Predicted/observed clean-level fractions agree within ≈ 0.035 in every lnr bucket (e.g.
   0.314/0.317 at q = 3, 0.575/0.563 at q = 11; 0.196/0.194 for p ≡ 5 (8); R224, independent 1 500 primes: within 0.012).
   R224 repair: 86 % of the levels are decided exactly by the signs of primes ≤ 100; on the remaining levels the coins
   over-predict (0.495 vs 0.466). Without the constraint the model is off by a factor ≈ 2. The worst sign-dominance
   primes are **clean-level clusters**: 7.3 of the levels t ≤ 10 clean on average (13 worst primes) vs 5.8 (random p
   with lnr ≥ 11; 6.3 size-matched, R224) and 3.95 (random p ≡ 1 mod 8); 5 of the 13 are m² + 24 (T1-type levels 1, 2, 5, 7).
4. **ES-five = the admissible version of the square test (PROVED, §3).** ES-five(p) ⟺ some level has an admissible
   divisor (A ≡ −1 mod t) with (A/p) = −1. Uncleanness is free at every non-square (level t₀ = −p⁻¹ mod q); the
   entire ES content is the admissibility gap. Mordell's 840 theorem = "lnr(p) ≤ 7 ⇒ the lnr level is admissible with
   A = q" (Lemma 3.2); for q ≥ 11 the lnr level succeeds ≈ 85 % of the time, not decaying from 10⁶ to 10¹¹ (R224: ≈ 0.91 at
   10¹⁴–10¹⁵).
5. **Three-squares side (§4).** No exact Siegel–Weil weighting beyond the indicator: on χ = −1 words α₂ and α_p
   vanish together (R-O217: the checkpoint-1 weighting was 0/0 and is withdrawn); conic point ℓ(w) = (x × y) mod p
   for a compatible pair, height = min(t, u, v) (R224 repair: PROVED, Lemma 4.2); boundary words = ideals dividing
   (1 + √−p) in the principal (= three-squares) genus.
6. **3SQ (CONJECTURE, EVIDENCE to 10⁶, no exceptions; §5).** For odd n: every path lattice of X_n embeds in ℤ³
   (n·G_w ∈ Gram(ℤ³)) ⟺ n is a square. Equals ES-five at primes and T1 at squares; **105 is not an exception**
   (all its 11 words have χ = +1 but are ramified at two odd primes).
* Assessment: the three-squares side gives clean dictionaries and one exception-free conjecture, and the "continuity of
  T1" is well described (EVIDENCE; a fitted heuristic, not a proof) by Legendre symbols of the prime factors of
  tp + 1 plus one exact reciprocity constraint, plus the T1-type levels tm² + c² at p = m² + k (R224). No
  mechanism closes the admissibility gap (B2).

## 0. Iteration log (construction first; barrier as steering wheel)
(I1) Goal (a): Siegel–Weil for the one-class genus I₃. Tried an exact weighting (withdrawn, R-O217; §4.1). Barrier: term-by-term; the
family {T_w} is not an orbit (B2/B6). Violate "term by term": sum over the family as a lattice count of (x, y, t) —
the level t is a modulus inside the conditions (Prop 4.3); dead.
(I2) Goal (b), archimedean version: tested the O209 hypothesis at the √p scale — no association (bins flat); R224
repair: at bounded p − m² the hypothesis is TRUE, via T1-type levels (Lemma 1.4). Pivot to the
adelic version: χ = Legendre over prime factors of A ⇒ smooth A forced +.
(I3) Smooth-word removal explains the averages but not the extremes (2521: 27 unforced words, only 4 negative).
Inspection: the extremes have whole levels clean (p + 1 = 2·13·97, 2p + 1 = 3·41²). Built the level-cleanliness
model; the naive coin model under-predicted by 1.6× → found the missing exact input: the reciprocity constraint
((tp + 1)/p) = 1. Calibrated model fits (§2).
(I4) Tried to turn uncleanness (free at non-squares) into ES-five: the lnr level t₀. Works for free exactly when
t₀ | q + 1 — this is Mordell's theorem (§3.2); beyond, lottery with success ≈ 0.85 per translate (B2/B4).
(I5) Goal (c): conic heights (§4.2) — dictionary, B6 at fixed p.
(I6) Composite n: replaced the product of local signs (χ) by the signs themselves (ℤ³-embeddability) → 3SQ, which has
no exceptions to 10⁶ (§5).

## 1. Clean levels (PROVED)

**Lemma 1.1.** For a word w of p: χ(w) = (A/p) = (A*/p) = ∏_{r^e ∥ A} (r/p)^e. For an odd prime r ∤ t with
r | tp + 1: (r/p) = (p/r) = (−t/r).
*Proof.* p ≡ 1 (4) gives (−A/p) = (A/p) and reciprocity (r/p) = (p/r); AA* ≡ 1 (mod p); −tp ≡ 1 (mod r) gives
(p/r) = (−t/r). ∎

**Definition.** Level t is *clean* (for p) if (r/p) = +1 for all primes r | tp + 1.

**Lemma 1.2.** (a) If level t is clean, every word of level t has χ = +1. (b) Every prime r < lnr(p) has (r/p) = +1, so a level
with tp + 1 (lnr − 1)-smooth is clean (R224 repair: wording).
(c) (Reciprocity constraint) ∏_{r} (r/p)^{v_r(tp+1)} = ((tp + 1)/p) = (1/p) = +1. Hence if tp + 1 = s·ℓ^e with s
(lnr − 1)-smooth, ℓ prime and e odd, level t is clean. (Only this exact form: a rough prime with even exponent is
unconstrained, e.g. p = 200 881, t = 14, tp + 1 = 3·5·433², (433/p) = −1. Some fixed levels are never clean:
t = 1 for p ≡ 5 (8), since 2 | p + 1.)
*Proof.* (a) Lemma 1.1. (b) definition of lnr. (c) multiplicativity of the Legendre symbol; then (ℓ/p)^e = (s/p) = 1. ∎

**Prop 1.3 (square test).** For odd n, put level t *odd-clean* if (n/r) = +1 for all ODD primes r | tn + 1 (prime 2
excluded by convention; R224 repair: for n = p ≡ 1 (4) this differs from the Definition above only at r = 2, e.g. odd t
for p ≡ 5 (8); §2 uses the Definition, including r = 2). Then n is a
perfect square ⟺ every level is clean. (Proof in BRAINSTORM/y8_square_test_gap.md: ⇒ trivial; ⇐ take r with
(n/r) = −1 and t ≡ −n⁻¹ mod r.) At p = m² this is T1 in its most primitive form: tm² + 1 = 1² + t·m² is a norm
from ℤ[√−t], so all its prime factors split in ℚ(√−t).

**Lemma 1.4 (T1-type levels; PROVED, R224).** Let p = m² + k (k ≥ 1) and t ≥ 1 with tk + 1 = c². Then tp + 1 = tm² + c²;
every odd prime r | tp + 1 with r ∤ c has (−t/r) = +1, i.e. (r/p) = +1; a prime r | c dividing tp + 1 divides m (and
r² | tp + 1). So level t is odd-clean if gcd(m, c) = 1 (clean if moreover 2 ∤ tp + 1 or (2/p) = +1).
*Proof.* gcd(t, c) = 1 since c² − tk = 1; if r ∤ c then r ∤ tm and −t ≡ (c/m)² (mod r); Lemma 1.1. If r | c, then
r | tm², r ∤ t, so r | m. ∎ (k = 4: levels 2, 6, 12, 20, …; k = 16: 3, 5, 14, 18, …; k = 24: 1, 2, 5, 7, 12, ….)
EVIDENCE (R224, reviews/three-squares-review.md): for p ∈ (10⁵, 10⁶) the residual of N₋/N against primes with the same
p mod 16, lnr bucket, signs (r/p) (r ≤ 13) and size is −0.049 (p − m² = 4, 72 primes) and −0.057 (p − m² = 16, 78 primes),
6–7σ; removing the words on the T1-type levels removes the deficit (fully for k = 4, ≈ 3/4 for k = 16). 5 of the 13
worst sign-dominance primes below 10⁶ are m² + 24. This is an archimedean (bounded p − m²) continuity of T1.

## 2. The adelic law (EVIDENCE)

| p mod 8, lnr | primes | clean fraction (t ≤ 30) | model | √(log q / log tp) |
|---|---|---|---|---|
| 1, 3 | 4 500 levels | 0.317 | 0.314 | 0.269 |
| 1, 5 | 1 860 | 0.446 | 0.455 | 0.325 |
| 1, 7 | 1 110 | 0.514 | 0.506 | 0.358 |
| 1, 11 | 630 | 0.563 | 0.575 | 0.397 |
| 1, 13 | 270 | 0.585 | 0.602 | 0.411 |
| 1, ≥ 17 | 450 | 0.602 | 0.636 | 0.439 |
| 5, 2 | 9 180 | 0.194 | 0.196 | 0.214 |
(600 random primes p ≡ 1 (4) in (2·10⁵, 10⁶), data/y8/y8_sample600.txt; column 2 counts levels;
`scripts/y8_levels.py data/y8/y8_sample600.txt 30 100`.) Model: exact (r/p) for r ≤ 100, fair coins for r > 100,
conditioned on Lemma 1.2(c): P(clean) = 1[small primes clean]·2^{−s−(k−1)⁺}, k = #{r > 100 : v_r(tp + 1) odd},
s = #{r > 100 : v_r(tp + 1) even} (R-O217 repair; values moved ≤ 0.002). Heuristically (Sathe–Selberg; Assessment) P(level t clean | lnr = B) ≍
(log B / log tp)^{1/2}, which → 1 as B → p (the square limit) — the quantitative "continuity of T1". Under GRH
(lnr ≪ log²p) the clean probability of a fixed level tends to 0 as p → ∞, so the pre-asymptotic hardness of
near-square primes is a small-p effect at each level (Assessment).

Further evidence: removing words with A or A* (lnr − 1)-smooth (forced +; 0 exceptions in 1 500 primes) flattens
N₋/(N − S) to ≈ 0.66 for every lnr bucket q ≤ 13 (p ≡ 1 mod 8; 0.698 for p ≡ 5 mod 8), i.e. the average lnr effect is
entirely the forced words; the extremes are clean-level clusters (Summary item 3; `scripts/y8_clean_clusters.py`).

## 3. Admissibility: ES-five as the admissible square test (PROVED)

**Prop 3.1.** ES-five(p) ⟺ ∃ t ≥ 1 and A | tp + 1 with A ≡ −1 (mod t) and (A/p) = −1. For t ∈ {1, 2} the congruence is
void; for t | 24 it is one residue class. (CHI_FLIP + TWO_FIBRES Thm A; AA* ≡ 1 mod t gives A* ≡ −1.)
So, comparing with Prop 1.3: uncleanness of some level is automatic at every non-square, and ES-five is the
statement that some unclean prime (or product) can be placed in an admissible divisor.

**Lemma 3.2 (Mordell's theorem as the lnr level).** Let q = lnr(p), t₀ = (−p⁻¹ mod q) ∈ [1, q − 1]. If t₀ | q + 1 then
(t₀, (q + 1)/t₀, ((t₀p + 1)/q + 1)/t₀) is a χ = −1 word (A = q). If q ≤ 7, t₀ | q + 1 always (q = 2, 3: t₀ = 1;
q = 5: t₀ ∈ {2, 3}; q = 7: t₀ ∈ {1, 2, 4}). Since lnr(p) ≥ 11 ⟺ p ≡ 1, 121, 169, 289, 361, 529 (mod 840), this is
exactly Mordell's congruence theorem on ES-five. For q ≥ 11 and t₀ ∤ q + 1 one needs d | (t₀p + 1)/q with
qd ≡ −1 (mod t₀) and (d/p) = +1 (B2). ∎
Numerics (`scripts/y8_lnr_level.py`): success of the lnr level 0.845/0.811 (q = 11/≥ 13) for p ∈ (10⁵, 10⁶) and
0.872/0.909 for p ∈ (10¹⁰, 10¹¹); over translates t₀ + kq the first success has k ≤ 26 in 500/500 cases near 10¹⁰.

## 4. The three-squares side

**4.1 Siegel–Weil (PROVED, memo y8_siegel_weil_sign; R-O217 repaired).** r(T_w, I₃) = c_∞ ∏_ℓ α_ℓ(T_w, I₃) (one
class); on χ = −1 words both α_p and α₂ vanish (Hilbert reciprocity; p = 5, (1,3,4) has no solution mod 4), so no
positive "χ = +1 extension" of the weight exists; the checkpoint-1 formula N₊ = Σ r/ρ₊ (0/0 on negative words) is
withdrawn. Exact: N₊ = #{w : r(T_w, I₃) > 0}; r/48 ∈ {1, 2, 3, 4, 6} for p ≤ 157 (source of O209's 5-vs-6); r ≠ r*
in general (p = 61, (63,1,1): 288 vs 192). Brute-force check of Thm A: 166 words of primes ≤ 61, 0 mismatches.
**Prop 4.3 (circularity).** An independent evaluation of Σ_w r(T_w, I₃) is the count of (x, y, t) with x·y = 1,
|x × y|² = tp, t | |x|² + 1, |y|² + 1 — the level t is a modulus inside the conditions; not an arithmetic-group orbit.
**4.2 Conic (memo y8_conic_height).** For a compatible pair (x × y ≡ x + y mod t; an arbitrary z with z^⊥ ≅ T_w
does not suffice — R-O217 counterexample p = 61, (63,1,1), height 2), ℓ(w) = (x × y) mod p, height h(ℓ) = min L_ℓ ≤ min(t, u, v) ≤ (3p + 4)^{1/3};
observed h = min letter (p = 1009, 15/15; p = 61, 5/5; repaired script). Boundary words u = 1 ↔ ideals (v, 1 + √−p) | (1 + √−p) in the principal
genus of discriminant −4p, which is the three-squares genus; at most τ(p + 1) of its ≈ h(−4p)/2 classes.

## 5. 3SQ — the exception-free three-squares SQ (CONJECTURE; memo y8_three_squares_sq)
For odd n: every word w ∈ X_n has n·G_w ∈ Gram(ℤ³) ⟺ n is a square. ⇐ = Thm B; at primes = ES-five; trivial for
n with an odd-exponent prime ≡ 3 (4) (word (1, 2, n + 2), A = 1). `scripts/y8_embed_sq.c`: all odd n ≤ 10⁶ —
0 non-square n with every word embeddable, 0 squares with a non-embeddable word. 105: 11 words, all χ = +1, all
ramified at {3, 7} or {5, 7}. After the elementary words (A = 1, A = 2) the residual case is n all of whose
odd-exponent primes are ≡ 1 (8) (possibly several; no reduction to a single prime is proved).

## 6. Barrier summary
* B2: §3 is the precise location of ES: admissibility (A ≡ −1 mod t) of an unclean divisor. §4 restates it as ideal
  divisors of (1 + √−tp) of norm ≡ −1 (t) in the non-principal p-genus.
* B1: Lemma 3.2 is Mordell's covering; for lnr ≥ 11 no congruence covering (y4_mordell_witness).
* B3/B6: the §2 law and the conic/Siegel–Weil statements are averages; at a single p the lnr pattern only predicts
  probabilities.
* B4: clean-level clusters arise exactly when tp + 1 has few rough prime factors — the pigeonhole over divisor
  classes has nothing to work with (the near-profinite-square primes are the B4-hard ones, quantitatively).
* T1: every statement is checked against squares: all levels clean (Prop 1.3), 3SQ ⇐ is Thm B.

## 7. Numerics index (tiny outputs; heavy files in /tmp only)
| check | script | range | result |
|---|---|---|---|
| sign ratio vs lnr / vs dist to squares | y8_census_features.py on si_census | primes ≡ 1 (4) < 10⁶ | flat in distance, monotone in lnr |
| forced-+ words | y8_smooth.c | 1 500 primes in (2·10⁵, 10⁶) | 0 exceptions; N₋/(N − S) ≈ 0.66 |
| clean-level law | y8_levels.py | 600 primes, t ≤ 30 | model within 0.04 |
| clean clusters | y8_clean_clusters.py | 13 worst primes | 7.3/10 clean vs 3.95 |
| admissibility gap | y8_admissible.py | p ∈ (10⁵, 1.2·10⁵), t ≤ 30 | 0.692 unclean, 0.316 χ = −1 |
| lnr level | y8_lnr_level.py | 3 000 + 3 000 primes | Lemma 3.2; 0.81–0.91 for q ≥ 11 |
| Thm A brute force, weights | y8_gauss_weight.py | primes ≤ 61 (157) | 0 mismatches |
| conic heights | y8_conic_words.py | p = 1009 | h = min letter |
| 3SQ | y8_embed_sq.c | odd n ≤ 10⁶ | 0 exceptions |
