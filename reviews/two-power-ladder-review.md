# R283 — hostile review of O272 (TWO_POWER_LADDER.md, 2-power ladder)

Reviewer: side-agent/review-two-power. Reviewed: `side-agent/two-power-ladder` at aff44704. Author's document NOT edited.
From-scratch scripts: `scripts/review_r283_*.py` (no reuse of `scripts/z41_*`). ES is not solved; nothing reviewed claims otherwise.

## Summary verdicts
| Claim | Verdict |
|---|---|
| Thm 3.2 Stickelberger dictionary (m = 3, 4), incl. sharpness | **SOUND** (MINOR D1–D4) |
| Thm 3.1 Kummer–Chebotarev ceiling (repaired: ℓ ∤ m, 4 \| lcm(M, m)) | **SOUND** (MINOR D8, D9) |
| Prop 4.1 (a), (b), (b′), (c) | **SOUND** (MINOR D10, D11) |
| Prop 4.2 size obstruction | **SOUND** |
| Lemma 1.1 | **SOUND** (MINOR D7) |
| Lemma 5.1 (n = Dm², 4D \| t) | **SOUND** |
| §5 census (1 298 / 5 320 primes, decade rates) | **SOUND** — reproduced exactly, EVIDENCE/Assessment labels right (MINOR D5, D6) |
| §2 numerics (forced quadratic, free quartic/octic; Gaussian-lift control) | **SOUND** (EVIDENCE; D10) |
| Cor 6.1 cubic layer | **SOUND** in stated scope (MINOR+ D12, MINOR D13) |
| Labels / novelty | **SOUND** — Thm 3.1 correctly disclaimed as (J)93 in level coordinates; Thm 3.2 classical reciprocity, new only as packaging |

**No FATAL, no MAJOR.** 13 MINOR defects, all presentation/scope; none changes a conclusion. Repairs NOT applied by the
reviewer (author active; all defects minor — forwarded via parent).


## Thm 3.2 (Stickelberger dictionary) — verdict: SOUND (m = 3, 4), with MINOR scope/label defects

**Re-derivation.** K = ℚ(ω) or ℚ(i), ℓ ≡ 1 (m), λ primary, ℓ = λλ̄ exactly (both conjugates primary, N > 0); q = ππ̄ exactly.
(q/λ)_m = (π/λ)_m(π̄/λ)_m. Cubic reciprocity (primary, distinct norms) gives (σ_cπ/λ)₃ = (λ/σ_cπ)₃; biquadratic reciprocity gives
the sign (−1)^{((ℓ−1)/4)((q−1)/4)} for c = 1 and for c = 3 — the same sign twice, so it cancels. Galois equivariance
σ_c((α/𝔮)_m) = (σ_cα/σ_c𝔮)_m gives (λ/σ_c𝔮)_m = σ_c((σ_c⁻¹λ/𝔮)_m) = x_{c⁻¹}^c; reindexing a = c⁻¹ gives S = ∏x_a^{a⁻¹}.
D = (ℓ/𝔮)_m = ∏x_a trivially. m = 3: S = x₁x₂², D/S = x₂⁻¹ (free). m = 4: S = x₁x₃⁻¹, D/S = x₃², D² = S² (= quadratic reciprocity,
q ≡ 1 (4)). All correct.

**Sharpness, re-derived independently (stronger than the author's one-line sketch).** B = ⟨σ_aλ⟩ ⊂ K^×/K^{×m} is free over ℤ/m
(valuations). For cyclic H = Gal(K/ℚ) (m = 3, 4), K(β^{1/m})/ℚ is abelian iff σ_cβ ≡ β^c (mod K^{×m}) for all c (central
extension with cyclic quotient ⇒ abelian). Writing β = ∏(σ_aλ)^{i_a}, the condition is i_{c⁻¹a} ≡ c·i_a, i.e. i_a = a⁻¹·i₁: the
maximal abelian-over-ℚ subfield of K((σ_aλ)^{1/m} : a) is K(β₀^{1/m}), β₀ = ∏(σ_aλ)^{a⁻¹}, whose Frobenius at 𝔮 is exactly S.
Hence NO congruence on q (any modulus) sees more of the vector (x_a) than S, and by Chebotarev every vector with prescribed S
occurs with equal density. So "S determines D exactly mod μ_m^{gcd(2,m)}" is sharp for m = 3, 4. ✔

**From-scratch numerics** (`scripts/review_r283_stickel.py`, `logs/review_r283_stickel.txt`; own ℤ[ω], ℤ[i] arithmetic, symbols by
reduction ζ ↦ r mod p, both primes 𝔮 | q tested):
* m = 3: 4 120 pairs (ℓ < 80, q < 3000) + 18 078 pairs (ℓ < 20, q < 6·10⁴): **0 failures** of k_S = k₁ + 2k₂; S ≠ D in 2 754 / 12 070
  of them (the identity is discriminating, not a disguised S = D).
* m = 4: 3 780 + 18 102 pairs: **0 failures** of k_S = k₁ + 3k₃ (the exact sign cancellation holds).
* Primarity of λ is essential: replacing λ by a non-±1 unit multiple breaks the identity in ≈ 2/3 (m = 3) resp. ≈ 1/2 (m = 4) of
  pairs. The theorem does say "λ primary", so fine, but see D2.
* Sharpness: in every cell (ℓ, q mod ℓ) with ≥ 4m² samples (36 cells m = 3, 32 cells m = 4) S is constant and **all m vectors**
  (x₁, x_{−1}) with that S occur.

**Defects.**
* **D1 (MINOR, §3 Thm 3.2 bullet 3 and "Hence …").** "The exponents 1 − a⁻¹ generate gcd(2, m)·ℤ/m … for m odd S says nothing
  about D" is phrased for general m, but the identity S = ∏x_a^{a⁻¹} is only proved for m = 3, 4 (for general m Eisenstein
  reciprocity needs m = odd prime, ideal-theoretic symbols, and the primary normalisation of λ is not available as an element
  identity). Repair: state the conclusion for m = 3, 4, and say for general m odd only the conjugacy-invariant consequence
  that Thm 3.1 already gives.
* **D2 (MINOR, Thm 3.2 statement).** The x_a depend on the element λ, not just the ideal: λ ↦ uλ multiplies ∏x_a^{a⁻¹} by
  (u ū²/𝔮)₃ (m = 3) resp. (u ū³/𝔮)₄ = (u²/𝔮)₄ (m = 4), generally ≠ 1 (confirmed numerically), while S and D are unchanged. Add
  "(the x_a depend on the primary normalisation of λ; S and D do not)".
* **D3 (MINOR, Thm 3.2 proof, *Realisability*).** "the commutator argument of Thm 3.1 applied to β" only gives the necessary
  condition; the identification of the abelian subfield as exactly K(β₀^{1/m}) needs the converse (central + cyclic quotient
  ⇒ abelian) and the computation i_a = a⁻¹i₁ above. Repair: insert those two lines.
* **D4 (MINOR, label, "Reading").** "that is the whole reason the BM layer is free … and the whole reason T1 exists" is an
  interpretation (Assessment), not part of the PROVED statement. Relabel.

## §5 census (2-group levels) — verdict: SOUND (numbers reproduced exactly); Assessment label appropriate

From scratch (`scripts/review_r283_census.py`, `logs/review_r283_census.txt`): own T2 generator, residue-class **sieve** via Lemma 1.1
(mark n ≡ −u mod tu − 1, n ≥ 2(tu−1) − u) instead of the author's enumeration, plus an **independent divisor-based** check
(factor tp + 1, look for d ≡ −1 (t), d, N/d ≥ 2t − 1) on 150 random failing and 150 random hit primes per range.
* |T2 ∩ [4, X+2]| = 169 (X = 10⁶), 237 (X = 10⁷) ✔. Failing primes: **1 298** ≤ 10⁶ (largest 999 979), **5 320** ≤ 10⁷ (largest
  9 994 727) ✔. Decade rates 0.2168, 0.0688, 0.0293, 0.0136, 0.0069 ✔. Odd non-squares ≤ 10⁶ failing: 20 325 ✔. Squares hit: 0 (10⁶
  and 10⁷) ✔. Baseline all 4 | t: 118 primes, 1 939 non-squares, 0 squares; 1 180 T2-failing primes have a 4 | t word ✔.
  131: no 8 | t word, has a 4 | t word; 241: neither ✔.
* Divisor spot check: 0/150 failing primes actually have a word, 0/150 hit primes lack one (both X) ✔.
* **D5 (MINOR, §7 "rate halving per decade").** The ratios are ÷3.2, ÷2.3, ÷2.2, ÷2.0 — "roughly halving in the last decades" is
  accurate; "halving per decade" overstates the regularity on 5 data points. The heuristic "expected hits ≍ c·log n ⇒ infinitely
  many failures" is correctly labelled Assessment (failure rate ≈ n^{−0.3} under a naive Poisson model; Lemma 5.1 shows the hits
  are not Poisson-independent, so this is a heuristic only).
* **D6 (MINOR, §5 bullet 1).** "(of 499 500)" counts odd non-squares including n = 1 as a square and n = 3,… — fine, but the census
  ranges are "odd non-squares n ≤ 10⁶" vs primes "5 ≤ p" (2, 3 excluded silently; 3 has no T2 word). Cosmetic.

## Lemma 1.1 — verdict: SOUND
a(tn+1) − n(ta−1) = n + a and t(n+a) = (tn+1) + (ta−1), with gcd(a, ta−1) = gcd(t, ta−1) = 1: both directions ✔. MINOR (D7): the
lemma is stated for D⁻_t > 0 (a ≥ 1, includes the boundary d = t − 1); the ES word event R_t > 0 is the sub-union a ≥ 2 with the
extra condition n + a ≥ 2(ta − 1). Still a congruence union (above a threshold), so the conclusion stands; say so.

## Thm 3.1 (Kummer–Chebotarev ceiling, repaired hypotheses) — verdict: SOUND (MINOR omissions)

**Re-derivation.** ℓ ∤ m ⇒ ℓ unramified in K; v_λ(ℓ) = 1 ⇒ ℓ has order exactly m in K^×/K^{×m} ⇒ [L : K] = m (this also
disposes of the −4K^{×4} clause of Capelli/Lang, since −4 = (1+i)⁴ ∈ K^{×4} when 4 | m). Subfields of L/K are K(ℓ^{1/d}). The
commutator computation is right: σ̃τα = ζ_d⁻¹ζ′α, τσ̃α = ζ′ζ_dα, so abelian ⇒ ζ_d² = 1. F = L ∩ ℚ(ζ_{M′}) ⊇ K is abelian, hence
F = K (m odd) or K ⊆ F ⊆ K(√ℓ) ⊆ ℚ(ζ_{M′}) (needs ℓ | M and 4 | M′ — the repaired hypotheses are exactly what is used). Within
a fibre, ψ_𝔮(ℓ) is Haar-uniform on μ_m (m odd) resp. on {ζ^{m/2} = (ℓ/q)}; "ℓ ∈ F_q^{×e}" ⟺ ψ^{m/e} = 1 gives 1/e resp. 2/e. ✔
The m = 12, ℓ = 3 and m = 6, M = 7 counterexamples to the unrepaired version are correct (√3 ∈ ℚ(ζ₁₂); q mod 4 free).
**From scratch** (`scripts/review_r283_ceiling.py`, `logs/review_r283_ceiling.txt`, q < 4·10⁵, per class c of q mod M):
(ℓ, m) = (7, 3), (13, 3): e = 3 at 0.324–0.343 in every class; (7, 6) with M = 28: (ℓ/q) fixed per class, e = 3 ≈ 1/3 in every
class, e = 6 ≈ 1/3 resp. 0; (11, 4): e = 4 ≈ 1/2 / 0; (7, 8): e = 4 ≈ 1/2, e = 8 ≈ 1/4; (5, 12), M = 20: e = 12 at 0.151, 0.163 vs 2/12. ✔
* **D8 (MINOR, Thm 3.1 first bullet).** For m even and e odd the density (1/e, unconditionally on (ℓ/q)) is not stated; the
  proof gives it (μ_{m/e} meets each fibre in half its elements). Add it (numerics: (7, 6), c = 5, (ℓ/q) = −1, e = 3: 0.334).
* **D9 (MINOR, Thm 3.1 *Scope*).** "Chebotarev in the compositum for several level primes is the same argument" — not quite: for
  t = 4q₁q₂ the forcing is the coupled condition q₁q₂ ≡ c (mod ℓ), a condition on PAIRS of primes. The conclusion still holds
  (split c = a·(c/a), apply Chebotarev to each prime separately in its class, sum over a; the pair-count needs an explicit
  ordering, e.g. q₁, q₂ ≤ X), but it is a two-line argument, not "the same". Write it.
* Novelty: correctly disclaimed — this is CLASS_FORCING Thm 2.1(b)(c) / Thm 5.1(c) with datum and moving prime swapped.

## Prop 4.1 (a), (b), (b′), (c) — verdict: SOUND
(a) Jacobi (n/x) is a character mod 4n on positive odd x; if trivial on primes ≡ 3 (4) then (Dirichlet) on classes ≡ 3 (4), hence
(x ≡ (4n−1)·(−x)) on all classes, so n is a square ✔. (b) compatibility field F = K(√−ℓ) = K(√ℓ) for m ≥ 4; the forcing gives
(q/ℓ) = (−(4n)⁻¹/ℓ) = (−1/ℓ)(n/ℓ) = 1 ✔; relative density 1/[L : F] = 2/m ✔. (b′) the extra congruence q ≡ 1 + 2^j (2^{j+1}) is
harmless because ℚ(ζ_{2^{j+1}}) ∩ L ⊆ K(√ℓ) ∩ ℚ(ζ_{2^∞}) = K (K(√ℓ)/K ramified at ℓ) ✔. (c) (−ℓ/q) = −(ℓ/q) = (q/ℓ) = 1 and
−ℓ ≡ 1 (4), 2-Sylow of G_{4q} = (ℤ/2)² ✔.
From scratch (q < 4·10⁵): m = 2 all forced q; m = 4, 8, 16: 1405/2819, 350/1406, 82/713 for (13, 7) (author's numbers reproduced
exactly), similar for (7, 11), (101, 7), (131, 11), (21, 19); (b′) j = 1: all (c); j = 2, 3, 4: ≈ 1/2, 1/4, 1/8 ✔.
* **D10 (MINOR, §4 numerics and §2).** (241, 7) is the SAME forced progression as (101, 7) (241 ≡ 101 ≡ 3 mod 7): the rows are
  identical (my log: 1410/2797, 338/1390, 87/684 for both), so it is not independent evidence. More generally, the forcing
  depends on n only through n mod ℓ; "uniformly in n (including n = 9, a square, and n = 131, 241)" in §2 is automatic once
  the residues n mod ℓ are covered — and n = 9 a square is not special at the 4th-power layer. Say "for every residue n mod ℓ".
* **D11 (MINOR, (b′) for j = 1).** Thm 3.1 needs m ≥ 3, so the "(b′) Same, …" proof does not cover j = 1; that case is (c).
  Say so.

## Prop 4.2 — verdict: SOUND (trivial, correctly labelled)
(a), (b): d | tn+1 ⟺ t ≡ −n⁻¹ (d); d ≡ −1 (t), d > t − 1 ⇒ t < d ⇒ t = least residue ✔. The "τ(d+1)/d" probability is
explicitly heuristic ✔. The repaired cofactor statement [N/ℓ] = [ℓ]⁻¹ (N ≡ 1 (t)) is right.

## Lemma 5.1 — verdict: SOUND
−tDm² ≡ 1 (ℓ) ⇒ (−t/D / ℓ) = 1 for each prime ℓ | N; χ_{−t/D} is the Kronecker character of the discriminant −t/D ≡ 0 (4), a
character mod t/D | t, odd ⇒ no d | N has d ≡ −1 (t) ✔. D need not be squarefree. From scratch: 4 320 (D, m, t) with
D ∈ {3, 5, 7, 9, 15, 17, 21, 45, 255}, m < 40 odd, t = 4Dk ≤ 96D: 0 violations (all divisors enumerated, incl. boundary d = t − 1);
control with 4D ∤ t: words do occur. ✔

## Cor 6.1 (cubic layer) — verdict: SOUND in its stated narrow scope; MINOR presentation defects
The proof is Thm 3.1 with m = 3 (ℓ ≡ 1 (3) ⇒ ℓ ∤ 3; the forcing q ≡ −(4wn)⁻¹ (ℓ) is a congruence) ✔. From scratch: fraction of
forced q (t = 4qw, w = 1, 2) with ℓ a cube mod q: 915/2804, 472/1397, 323/955, 184/554 (w = 1); 925/2796, 452/1396, 317/936,
180/579 (w = 2) ≈ 1/3 ✔. Conductor example: 757 prime, 27² + 27 + 1 = 757, 7^252 ≡ 27 (mod 757) ✔.
* **D12 (MINOR+, "What a cube DOES force" and §3 Checks).** "S is constant for each (n, ℓ)" is true for EVERY n (S = (q/λ)₃ is a
  function of q mod ℓ, which the forcing fixes); it is not a feature of cubes and the logged constancy is vacuous as evidence.
  What cubes add is that the pinned value S = (−4w/λ)₃⁻¹ is independent of r — and at w = 2 (t = 8q, −8 = (−2)³) one gets
  **S = 1 at every forced split ℓ, for every cube n** — the literal cubic analogue of T1, with D still uniform (my w = 2 rows).
  That is the sharp form of the paragraph's point; state it.
* **D13 (MINOR, conductor).** "conductor dividing 9t" is true but loose: by cubic reciprocity α ↦ (q/α)₃ has conductor dividing
  3q (α ≡ 1 (3) ⇒ α primary up to the cube −1). From scratch (`scripts/review_r283_conductor.py`): trivial on all primes α ≡ 1
  (mod 3q) for q = 7, 13, 19, 31 (465, 113, 52, 21 cases); nontrivial on many α ≡ 1 (mod q) except q = 19 ≡ 1 (9), where
  the conductor is q itself.

## §2 numerics, labels, novelty — verdict: SOUND
* §2 positive control reproduced from scratch (`scripts/review_r283_gauss.py`, `logs/review_r283_gauss.txt`): [ℓ a 4th power mod q]
  is a function of (a mod ℓ, b mod ℓ, a mod 8, b mod 8), π = a + bi primary: 64, 128, 384, 960, 1 152 keys for ℓ = 3, 5, 7, 11,
  13, **0 clashes** ✔ (author's counts). Extra: without the 2-adic part, (a, b) mod ℓ alone already suffices for ℓ ≡ 1 (4)
  (ℓ = 5, 13: 0 clashes) but not for ℓ ≡ 3 (4) (ℓ = 3, 7, 11: half the keys clash) — consistent with the primary-associate sign
  of (J)96 / MODP_RECIPROCITY R275; worth one sentence.
* Labels: PROVED items (Lemma 1.1, Thm 3.1, Thm 3.2 for m = 3, 4, Props 4.1, 4.2, Lemma 5.1, Cor 6.1) are proved; EVIDENCE (§2,
  §5) and Assessment ("infinitely many failures expected") correctly used, except D4 (interpretive "whole reason" sentence
  inside a PROVED block). "ES is not solved" stated; no overclaim found.
* Novelty vs (J)93 / (J)96: Thm 3.1 is CLASS_FORCING Thm 2.1(b)(c)/5.1(c) in level coordinates (disclaimed ✔). Thm 3.2 is
  cubic/biquadratic reciprocity plus the standard Kummer computation of the abelian part (my derivation above); (J)96 already
  used the m = 4 instance (Burde) in p-coordinates. New as an ES-facing dictionary (the forcing reads ∏x_a^{a⁻¹}, ES reads ∏x_a),
  not as mathematics. The agent report's "SHARP (modest)" is fair.
* Circularity / hidden hypotheses: none found. Uniformity: all densities are for FIXED (n, ℓ) and one varying level prime, and
  the document now says so everywhere (scope repairs ⟨rep⟩ verified in §3, §4, §6, §7).

## Defect list (consolidated)
FATAL: none. MAJOR: none.
MINOR: D1 (general-m phrasing of Thm 3.2 conclusion), D2 (λ-normalisation dependence of x_a), D3 (sharpness proof needs converse
+ i_a = a⁻¹i₁ computation — supplied above), D4 (interpretive sentence in PROVED block), D5 ("halving per decade"), D6 (census
bookkeeping), D7 (Lemma 1.1 vs R_t > 0), D8 (m even, e odd density), D9 (several level primes: coupled pair count), D10
((241, 7) ≡ (101, 7); "uniformly in n" = in n mod ℓ), D11 (j = 1 of (b′) is (c)), D12 (S constant for every n; the cube-specific
statement is S ≡ 1 at t = 8q — the formal cubic T1 with D uniform), D13 (conductor | 3q, sharper than 9t).
