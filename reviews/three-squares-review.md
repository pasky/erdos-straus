# R224 — hostile review of O217 THREE_SQUARES.md (+ memos BRAINSTORM/y8_*.md, AGENT_REPORT_O217)

Reviewer: R224 (side-agent/review-three-squares). Merged side-agent/three-squares at its tip (README conflict: kept both).
All numerics re-done with from-scratch code `scripts/review_r224_*.py` (author scripts not reused).

## Summary verdicts
| claim | verdict |
|---|---|
| Lemma 1.1, Lemma 1.2 (a)–(c), rank-one sterility | **SOUND** (MINOR D1 wording, D2 two inconsistent "clean" conventions) |
| Prop 1.3 (square test) | **SOUND** (MINOR D2) |
| Prop 3.1 | **SOUND** (MINOR D3 citation/hypothesis) |
| Lemma 3.2 (Mordell 840 = lnr level) | **SOUND** (MINOR D4 "exactly Mordell") |
| SHARP 1 census numbers (lnr buckets 0.645 → 0.430; deciles 0.643–0.647; 2 402 violations) | **reproduced exactly** (independent C census) |
| SHARP 1 / Summary 1 reading "continuity of T1 is adelic, NOT archimedean (corrects O209 §3.2)" | **GAP — overclaimed (MAJOR D5)**: a genuine archimedean (bounded p − m²) effect exists, z ≈ −6, with a PROVED T1-type mechanism the author missed |
| §2 Assessment "each fixed level is clean with probability → 0 (GRH)" | **GAP (MAJOR D6)**: false along the families p = m² + k |
| §2 clean-level law + coin model ("within ≈ 0.03 per lnr bucket") | **SOUND as EVIDENCE, weaker than presented (MINOR D7, D8)**: reproduced exactly on the author's sample and within 0.012 on an independent 1 500-prime sample; but 75–91 % of levels are decided by the exact part, and the coin part over-predicts by ≈ 0.03 (4–8σ) |
| CONJECTURE 3SQ (0 exceptions ≤ 10⁶; 105 not an exception; elementary words; residual class) | **SOUND** (label CONJECTURE correct; all numerics reproduced) |
| §4.1 (α₂, α_p vanish together on χ = −1; r/48 values; r vs r*; withdrawn weighting) | **SOUND** (MINOR D9: stale "built the exact weighting" text; Prop 4.3 is an Assessment, not PROVED) |
| §4.2 conic height bound, boundary genus | **SOUND**; the "observed h = min letter" is in fact **PROVED** (D10, upgrade) |
| §3 numerics "≈ 85 % lnr-level success, stable 10⁶–10¹¹"; translates "k ≤ 26 in 500/500" | **SOUND as EVIDENCE** (reproduced; it slowly *increases*, 0.84 → 0.86 → 0.91 up to 10¹⁵; MINOR D11 on the translate claim and sample sizes) |
| (further rows added below as checked) | |

## Claim-by-claim

### Lemma 1.1 / 1.2 — SOUND
Re-derived. AA* = (tu−1)(tv−1) = t(tuv − u − v) + 1 = tp + 1, so A | tp + 1, gcd(A, p) = 1, AA* ≡ 1 (p) gives
(A/p) = (A*/p); p ≡ 1 (4) gives (−A/p) = (A/p); multiplicativity gives the product. For odd r | tp + 1 (so r ∤ t,
r ≠ p): (r/p) = (p/r) and p ≡ −t⁻¹ (r) gives (p/r) = (−t/r). (a) every prime of A divides tp + 1. (c) ((tp+1)/p) =
(1/p) = 1; if tp + 1 = s·ℓ^e with s (lnr−1)-smooth then (s/p) = 1, so (ℓ/p)^e = 1, e odd ⇒ (ℓ/p) = 1. Correct, and the
"only this exact form" caveat is right (two rough odd-exponent primes can both be −1; even exponent unconstrained).
Checks (`scripts/review_r224_lemmas.py`): every word of every prime p ≡ 1 (4) < 1500 (words enumerated two
independent ways, (t, A)-divisor form and direct (u, v) search — identical sets): χ = (A/p) = (A*/p) = ∏(r/p)^e,
0 failures; reciprocity constraint for t < 60 at all those p, 0 failures; clean ⇒ no χ = −1 word, 0 failures;
(r/p) = (−t/r) for all odd r | tp + 1, 0 failures. Rank-one form (one rough prime ≥ lnr with odd exponent, or none):
667 levels (p ≡ 1 (4) in (2·10⁵, 2.03·10⁵), t < 40), all 667 clean. Counterexample p = 200 881 (prime, lnr 11),
14p + 1 = 3·5·433², (3/p) = (5/p) = 1, (433/p) = −1: confirmed.

### Prop 1.3 — SOUND
⇒ trivial. ⇐: for odd non-square n write n = m²n′, n′ > 1 squarefree odd; r ↦ (n′/r) is a non-principal character
(Jacobi/Kronecker, modulus | 4n′), so some odd prime r ∤ n has (n/r) = −1; t ≡ −n⁻¹ (r) gives r | tn + 1.
Check: all odd n < 3000: non-squares have an unclean level (found by search), odd squares have no unclean level
t ≤ 300; 0 failures.

### Prop 3.1 — SOUND
Words ↔ pairs (t, A) with A | tp + 1, A ≡ −1 (t) is a bijection (u = (A+1)/t; AA* ≡ 1 (t) ⇒ A* ≡ −1 (t), v = (A*+1)/t;
tuv − u − v = (AA* − 1)/t = p). Verified against direct enumeration above. ES-five ⟺ N₋ ≥ 1 is imported.

### Lemma 3.2 — SOUND
Re-derived the residues: q = 3 ⇒ p ≡ 2 (3) ⇒ t₀ = 1; q = 5 ⇒ p ≡ 2, 3 (5) ⇒ t₀ = 2, 3; q = 7 ⇒ p ≡ 3, 5, 6 (7) ⇒
t₀ = 2, 4, 1; all divide q + 1; A* = (t₀p+1)/q ≡ −1 (t₀) from AA* ≡ 1. The six classes mod 840 are exactly the odd
squares coprime to 105 mod 840 (computed). Check over all 36 805 primes p ≡ 1 (4) < 10⁶ with lnr ≤ 7: the stated word is
a valid χ = −1 word in every case; lnr ≥ 11 ⟺ p mod 840 ∈ {1, 121, 169, 289, 361, 529}: 0 mismatches over all
p ≡ 1 (4) < 10⁶.

### SHARP 1 census (Summary item 1, §2 first half) — numbers reproduced; reading overclaimed
Independent census `scripts/review_r224_census.c` (all ordered positive words via uv | p + u + v; cross-checked against
the (t, A) enumeration of review_r224_lemmas.py at 17 primes), aggregated by `scripts/review_r224_census_agg.py`:
39 174 primes p ≡ 1 (4), 5 < p < 10⁶; 2 402 sign-dominance violations; by (p mod 8, lnr): 0.645 (1,3), 0.604, 0.565,
0.516, 0.481, 0.452, 0.442, 0.430 (1, ≥ 23), 0.685 (5, 2) — **identical to the author's**. Value bins of dist(p, ℤ²)/√p:
0.6432–0.6473 (author: 0.643–0.647), and the same for true quantile deciles and within the homogeneous bucket
(p ≡ 1 (8), q = 3). The author's bins were *value* bins of width 0.1 (≈ 3 900 primes each), not quantile deciles — harmless.
"How was the model fitted": the lnr buckets and deciles are raw means, no fit; fine.

**But the archimedean null is an artefact of bin width** (`scripts/review_r224_near_sq.py`). Residual of N₋/N after
subtracting the mean of its stratum (p mod 8, lnr bucket, p-size bin of width 10⁵; with FULL=1 additionally p mod 16
and the signs (r/p), r = 3, 5, 7, 11, 13), p ∈ (10⁵, 10⁶), z against the global residual s.d.:
| subset | n | residual (FULL strata) | z |
|---|---|---|---|
| dist(p, ℤ²) ≤ 4 | 207 | −0.029 | −6.1 |
| dist ≤ 20 | 1 011 | −0.014 | −6.6 |
| dist/√p < 0.01 | 288 | −0.021 | −5.3 |
| dist/√p < 0.05 | 1 636 | −0.011 | −6.4 |
| p − m² = 4 | 72 | −0.049 | −6.3 |
| p − m² = 16 | 78 | −0.057 | −7.5 |
| p − m² = 1, 9, 25, 49 | 61, 48, 100, 66 | −0.014, −0.016, +0.003, −0.006 | n.s. |
So primes *very* near squares (bounded p − m²) have markedly fewer χ = −1 words than adelically identical primes, and
the effect is concentrated on specific offsets k = p − m².

**Mechanism (PROVED here, elementary; the deformation of T1 the document says does not exist).** Let p = m² + k and t ≥ 1
with tk + 1 = c². Then tp + 1 = t·m² + c². gcd(t, c) = 1, so an odd prime r | tm² + c² with r ∤ c has r ∤ m and −t ≡ (c/m)² (mod r), i.e. (−t/r) = +1,
i.e. (r/p) = +1 by Lemma 1.1; an odd prime r | c dividing tp + 1 must divide m (and then r² | tp + 1). Hence
**level t is odd-clean whenever gcd(m, c) = 1** (clean, if also 2 ∤ tp + 1 or (2/p) = +1); when gcd(m, c) > 1 only the
primes of gcd(m, c) — which divide tp + 1 to exponent ≥ 2 — escape (e.g. p = 1249 = 35² + 24, t = 2, c = 7:
2p + 1 = 3·7²·17 and (7/p) = −1).
This is literally T1's identity tm² + 1 = 1² + t·m² with 1 replaced by c. For k = 4 the levels are t = 2, 6, 12, 20, …
(t even ⇒ tp + 1 odd ⇒ clean); for k = 16, t = 3, 5, 14, 18, … (p ≡ 1 (8) ⇒ clean); for k = 1, 9, 25 the small
levels (3, 8; 7, 11; 23, 27) are odd-clean but can fail at r = 2 (p ≡ 5 (8)) or are large — matching the weaker
residuals. Check (`scripts/review_r224_poly_levels.py`): 40 primes each p = m² + k ∈ (10⁵, 10⁶), all levels
t = (c² − 1)/k < 200: odd-clean 0 failures (no gcd(m, c) > 1 case occurred there) for k = 1, 4, 9, 16, 25; fully clean 520/520 for k = 4 and k = 16.
Removing all words on these levels (all t ≤ p + 2): k = 4: N₋/N 0.636 → 0.690 (stratum mean ≈ 0.686: deficit fully
explained); k = 16: 0.572 → 0.616 (stratum ≈ 0.628: ≈ 3/4 explained). These levels carry ≈ 7.5 % of all words.

### §2 clean-level law and coin model — SOUND as EVIDENCE, weaker than presented
From scratch (`scripts/review_r224_model.py`, own prime selection, own model code; formula re-derived: given the exact
small part is all-clean, k rough odd-exponent coins conditioned on product +1 give 2^{−(k−1)} for k ≥ 1, and s
even-exponent rough coins are free, 2^{−s}; k = 0 is deterministic). Not fitted: the only free choice is the
cutoff Y; Y ∈ {30, 100, 300} all fit (Y = 300 best), so no tuning on the same data.
* On the author's sample (data/y8/y8_sample600.txt, t ≤ 30, Y = 100): all 7 buckets reproduced to the third decimal
  (0.317/0.314, …, 0.602/0.636, 0.194/0.196).
* Independent sample (1 500 random primes p ≡ 1 (4) in (2·10⁵, 10⁶), seed 2240, 45 000 levels), obs/model (Y = 100):
  (1,3) 0.306/0.309, (1,5) 0.425/0.430, (1,7) 0.483/0.492, (1,11) 0.557/0.565, (1,13) 0.571/0.583, (1,≥17) 0.624/0.636,
  (5,2) 0.192/0.194 — **max deviation 0.012**, always model > obs.
* But the agreement is mostly exact bookkeeping: at Y = 100, **86 % of levels have model probability exactly 0 or 1**
  (75–91 % per bucket; mostly 0 = a small prime ≤ 100 is unclean, or k = 1 forced clean). On the random part only
  (6 144 levels) obs 0.466 vs model 0.495 (≈ 4.5σ); Y = 30: 0.425 vs 0.467 (10 485 levels, ≈ 8σ). By (k, s)
  (`scripts/review_r224_model_k.py`): k = 2, s = 0: 5 965 levels, obs 0.471 vs 0.500; k = 0, s = 1: 0.42 vs 0.50 (33 levels).
  The "fair coin" part is biased toward −1 by a few per cent; the bias is unexplained.
* The unconstrained model is off by a factor ≈ 2.0 (0.157 vs 0.314 …) in every bucket on both samples, not "≈ 1.6"
  (the factor 2 is forced: the constraint doubles every non-deterministic level with k ≥ 1).

### CONJECTURE 3SQ (§5, memo y8_three_squares_sq) — SOUND
* Criterion check to 10⁶ (`scripts/review_r224_3sq.c`, own word enumeration, Thm A (i): w embeddable ⟺ (−A/ℓ) = +1
  for every odd ℓ with v_ℓ(n) odd): all 499 500 odd non-squares n ≤ 10⁶ have a non-embeddable word; no odd square
  ≤ 10⁶ has one. **0 exceptions** (runs in < 1 s, early exit; terminates — all loops bounded).
* Independent of Thm A, for small n (`scripts/review_r224_direct_embed.py`): direct search for a, b, c ∈ ℤ³ with Gram
  n·G_w, G_w = [[v, −1, 0], [−1, t, −1], [0, −1, u]]: all 11 007 unordered words of all odd n ≤ 1001 — direct result
  = criterion, 0 mismatches; 3SQ holds for every odd n ≤ 1001 by direct embedding.
* 105: 11 ordered words (6 unordered: (107,1,1), (54,1,2), (3,1,53), (2,1,106), (1,2,107), (1,3,54)), each with
  (−A/105) = +1 and exactly two of (−A/3), (−A/5), (−A/7) equal to −1, namely {3, 7} or {5, 7}: confirmed. 525: 27 ordered
  words, 23 non-embeddable: confirmed.
* Elementary words: (1, 2, n + 2) has A = 1, (1, 3, (n + 3)/2) has A = 2 (both valid words for every odd n — checked
  algebraically); they kill every n with an odd-exponent prime ℓ ≢ 1 (8). Residual (all odd-exponent primes ≡ 1 (8)):
  32 050 of the 499 500 odd non-squares ≤ 10⁶ — all covered numerically. The R-O217 caveat (no reduction to a single
  prime) is correct and needed.
* ⇐ is Thm B (R214 SOUND); at n = p ≡ 1 (4) 3SQ(p) ⟺ ES-five(p) (Thm A (i) with n = p is χ = +1): so 3SQ contains the
  open part of ES-five; CONJECTURE is the right label. "Exception-free formulation of SQ" is a fair SHARP (language).

### §4.1 Siegel–Weil — SOUND (labels: D9)
Re-derived: rationally T_w ⊥ ⟨1/(tp)⟩ ≅ I₃ ⊗ ℚ_ℓ iff the even Clifford algebras agree at ℓ; for χ = −1, C₀(L_w) ≅
B_{p,∞} vs B_{2,∞} for I₃, so the local rational representation fails at exactly {2, p} (Hilbert reciprocity forces
an even set), hence α₂ = α_p = 0. The p = 5, (1, 3, 4) mod-4 argument (norm 3 ⇒ three odd coordinates, norm 2 ⇒ two,
dot product even) is correct. Numerics (`scripts/review_r224_sec4.py r 157`, own vector enumeration): all 463 ordered
words of primes p ≡ 1 (4) ≤ 157: r(T_w, I₃) > 0 ⟺ χ = +1 (Thm A (iii)), 0 mismatches; r/48 ∈ {1, 2, 3, 4, 6} exactly;
Σ r/48 vs N₊ = (5: 6/5), (13: 10/7), (17: 16/11), (29: 16/11), (53: 22/13), (61: 16/9) — all as stated; p = 61, (63, 1, 1):
r = 288, r* = 192 — confirmed. Withdrawn weighting: no remaining text *uses* N₊ = Σ r/ρ₊; only stale descriptions
remain (D9).

### §4.2 conic — SOUND, and the observed equality is a theorem (D10)
For a compatible pair the proof of Thm A (iii)⇒(iv) gives M = ℤx + ℤy + ℤγ with z·x = z·y = 0, z·γ = |z|²/t = p, so
z/p is the dual vector of γ and pM^# = pℤ³ + ℤz = L_ℓ (z ≢ 0 (p): a word with p | t would need t = p and then
p(kj − 1) = k + j for A = kp − 1, A* = jp − 1, impossible for p ≥ 5). Hence (L_ℓ, |·|²/p) ≅ (ℤ³, Q_w) and
h(ℓ(w)) = min Q_w ≤ min(t, u, v): correct. Bound (3p + 4)^{1/3}: if all letters ≥ 2 then u + v ≤ uv ≤ tuv/2, so
tuv ≤ 2p; correct (and m³ ≤ 2p is the sharper form).
**Upgrade (PROVED here): h(ℓ(w)) = min(t, u, v) for every compatible embedding**, so the "observed" 15/15, 5/5 is a
theorem and h is independent of the compatible pair. Proof: h = min Q_w, Q_w = vx² + ty² + uz² − 2xy − 2yz. With
m = min letter: m = 1 trivial (Q integral, ≥ 1). m ≥ 3: Q ≥ (v−1)x² + (t−2)y² + (u−1)z² (AM–GM on the cross terms); one
non-zero coordinate gives a letter ≥ m, two or more give ≥ (m − 2) + (m − 1) ≥ m. m = 2: Q − (2x² + 2y² + 2z² − 2xy − 2yz)
= (v−2)x² + (t−2)y² + (u−2)z² ≥ 0 and the A₃-type form 2x² + 2y² + 2z² − 2xy − 2yz is even positive definite, so Q ≥ 2.
∎ Numerics (`review_r224_sec4.py h`): p = 61, all 5 χ = +1 words (u ≤ v); p = 1009, all 17 χ = +1 words with
max(A, A*) ≤ 3·10⁴: h = min letter for every compatible pair; non-compatible pairs give other heights (e.g. p = 1009,
(102, 1, 10): 9; (169, 2, 3): 1), confirming that the R-O217 compatibility caveat is needed.
Boundary genus: u = 1 reduction ⟨1⟩ ⊥ [[v, −1], [−1, t − 1]], (t − 1)v = p + 1, form (v, 2, t − 1) of disc −4p ↔ ideal
(v, 1 + √−p) (1 ≡ −p mod v), genus character (v/p) = ((t−1)/p) = χ: correct. "Principal genus = three-squares genus":
checked that z^⊥ (z primitive, |z|² = p) represents only residues mod p, all p ≡ 1 (4) ≤ 300, 0 failures (consistent with
the Gauss statement; not a full proof check of art. 291–292 — sources not accessed).

### §3 numerics (lnr level) — SOUND as EVIDENCE
How 10¹¹ was sampled (read `scripts/y8_lnr_level.py`): uniform random odd integers in (10¹⁰, 10¹¹), kept if prime
≡ 1 (4); 3 000 such primes, of which only ≈ 100 per bucket q = 11 / q ≥ 13 (SE ≈ 0.03). Legitimate but thin.
From scratch (`scripts/review_r224_lnr_level.py`): sample directly in the six classes mod 840 (⟺ lnr ≥ 11, verified
above), 800 primes per range (seed 224; sampling with replacement — 2 duplicates in the lowest range, negligible):
| range | q = 11 | q ≥ 13 | t₀ ∣ q + 1 (d = 1 works) | no success for k ≤ 60 |
|---|---|---|---|---|
| (10⁵, 10⁶) | 0.832 ± 0.018 | 0.841 ± 0.019 | 0.449 | 17/800 |
| (10¹⁰, 10¹¹) | 0.860 ± 0.017 | 0.867 ± 0.017 | 0.461 | 1/800 |
| (10¹⁴, 10¹⁵) | 0.897 ± 0.015 | 0.922 ± 0.014 | 0.486 | 0/800 |
Author's 0.845/0.811 and 0.872/0.909 agree within their SE. "Not decaying" is right; the rate actually rises slowly
(more divisors of t₀p + 1). Translates: at (10⁵, 10⁶), 17/800 primes (e.g. 132 721, 154 849, 229 849, 316 801) have
NO successful translate t₀ + kq for k ≤ 60 (they still have N₋ ≥ 22 from other levels); at 10¹⁰–10¹¹ one of 800 needs
k > 60. The author's "k ≤ 26 in 500/500, never > 40" is a sample property, not a stable bound.

## Defects
D1 (MINOR) — Lemma 1.2(b) and Summary item 2: "Every prime r < lnr(p) is clean" mixes the level notion with primes.
Repair: "(b) every prime r < lnr(p) has (r/p) = +1, so a level t with tp + 1 (lnr − 1)-smooth is clean."

D2 (MINOR) — two different definitions of "clean": §1 Definition (all primes r | tp + 1, INCLUDING 2, symbol (r/p)) and
Prop 1.3 (ODD primes only, symbol (n/r)). For p ≡ 5 (8) and odd t these differ (2 | tp + 1, (2/p) = −1: unclean in
§1, possibly clean in Prop 1.3); the §2 statistics use the §1 notion. Summary item 2 and the AGENT_REPORT juxtapose them
as one notion. Repair: call the Prop 1.3 notion "odd-clean" (or state that for n = p ≡ 1 (4) the two notions agree
except at r = 2), and say Prop 1.3 is stated for the odd-clean notion.

D3 (MINOR) — Prop 3.1 cites "CHI_FLIP + TWO_FIBRES Thm A"; the needed input is ES-five(p) ⟺ N₋(p) ≥ 1, which is
MODEL_SPECIFIC Thm 3.1(a) (with CHI_FLIP Cor 1.3), as TWO_FIBRES Cor A1 itself says after R214 D4; the (t, A)
bijection is elementary. Also state the hypothesis p ≡ 1 (4) prime in the Prop (χ = (A/p) uses it).

D4 (MINOR) — Lemma 3.2 "this is exactly Mordell's congruence theorem on ES-five": it recovers the prime case of Mordell's
covering set (same exceptional classes), via different (one-word) certificates; Mordell's theorem is a statement about
polynomial identities for all n. Repair: "recovers, at primes, the covering set of Mordell's theorem".

D5 (MAJOR) — Summary item 1 title "The continuity of T1 is adelic, not archimedean (… corrects O209 §3.2)", §0 (I2)
"tested the O209 hypothesis directly — refuted", AGENT_REPORT SHARP 1 / answer (b) "no dependence on p − m²". The test
(ten bins of width 0.1 in dist/√p) cannot see an effect confined to dist ≪ √p. At bounded p − m² there is a 6–7σ
deficit of χ = −1 words, with a proved mechanism (T1-type clean levels tk + 1 = c², see above). The correct statement:
*generic* archimedean proximity (dist ≍ √p scale) shows no association; *polynomial* proximity p = m² + k carries
infinitely many deterministically clean levels — an archimedean continuity of T1, realised through the same
norm-form identity. Repair: retitle item 1 ("adelic at the √p scale; at bounded p − m² T1 deforms to tm² + c²"),
add the lemma (p = m² + k, tk + 1 = c², gcd(m, c) = 1 ⇒ level t odd-clean) as PROVED, add the residual table as EVIDENCE, and drop
"refuted"/"corrects O209" or restrict it to the √p scale.

D6 (MAJOR) — §2 Assessment "Under GRH the clean probability of a fixed level tends to 0 as p → ∞, so the
pre-asymptotic hardness of near-square primes is a small-p effect at each level" (also AGENT_REPORT Results). False
along p = m² + k: level t with tk + 1 = □ is clean for every p in the family (Bunyakovsky-type families are
conjecturally infinite; no density statement makes them negligible for the question "which primes are hardest").
The heuristic is about a *random* p. Repair: restrict to "for p outside the families p = m² + k with tk + 1 = □
(heuristic, random p)", and record that these families have infinitely many deterministically clean levels
(≍ √T of the t ≤ T, carrying ≈ 7.5 % of all words at p ≈ 10⁵–10⁶), i.e. near-square hardness is NOT purely
pre-asymptotic there.

D7 (MINOR) — §2 / Summary item 3 / AGENT_REPORT SHARP 1: the model's agreement is quoted as "within ≈ 0.035" (Summary),
"within 0.04" (§7) and "within ≈ 0.03" (report) — make consistent; more importantly add that 86 % of the levels
(t ≤ 30, Y = 100) are decided exactly (model ∈ {0, 1}), so the test of the coin hypothesis is on the remaining 14 %,
where the model over-predicts (0.495 vs 0.466; k = 2: 0.500 vs 0.471). "Without the constraint off by ≈ 1.6" should be
"≈ 2 (exactly 2 on every non-deterministic level with k ≥ 1)". Label stays EVIDENCE.

D8 (MINOR) — §2 "Heuristically (Sathe–Selberg …) P ≍ (log B/log tp)^{1/2}": the relevant tool is Wirsing /
Selberg–Delange (integers all of whose prime factors lie in a set of relative density 1/2 beyond B), and tp + 1 runs
over shifted primes (needs Bombieri–Vinogradov-type input even heuristically); the table column is 15–40 % below the
observed fractions (the ≍ constant, incl. the factor-2 constraint, is not modelled). Fine as Assessment; cite
correctly and say "up to a constant".

D9 (MINOR) — stale text about the withdrawn weighting: §0 (I1) "Built the exact weighting (§4.1)"; header comment of
`scripts/y8_gauss_weight.py` ("checks r*/|SO| == chi_plus * C(tp)", which the code no longer does). Nothing uses the
weighting any more. Also Prop 4.3 ("not an arithmetic-group orbit; Siegel–Weil does not apply to the family") and the
memo's "nothing can be compared with |X_p| without B2 information" are Assessments, but the AGENT_REPORT lists
"§4.1 (… circularity)" under PROVED. Repair: reword (I1) to "tried an exact weighting (withdrawn, §4.1)", fix the
script comment, label Prop 4.3 "Assessment (the lattice-point description itself is PROVED, trivially)".

D10 (MINOR, upgrade) — §4.2 / memo y8_conic_height / report: "observed h = min letter" can be stated as PROVED (proof
above: h = min Q_w = min(t, u, v)); in particular h is independent of the compatible pair, and the B6 remark "the
height reading" becomes exact. Repair: replace "observed" by the lemma; keep the p = 1009/61 numerics as a check.

D11 (MINOR) — §3 numerics / memo y8_lnr_level: (a) state that the 10¹⁰–10¹¹ figures rest on ≈ 100 primes per bucket
(SE ≈ 0.03); (b) "stable" → "not decaying (slowly rising: ≈ 0.91 at 10¹⁴–10¹⁵, R224)"; (c) the translate statistic
"first success k ≤ 26 in 500/500; never > 40" must not be read as a bound: R224 finds primes with no success for k ≤ 60
(2 % at 10⁵–10⁶, 1/800 at 10¹⁰–10¹¹). The B3/B4 reading in the memo ("union over k is the polylog lottery") is the right one.
