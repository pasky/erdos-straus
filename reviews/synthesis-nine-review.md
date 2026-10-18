# R282 — hostile review of O271 SYNTHESIS_SPARKS9 (synthesis IX)

Reviewer branch: side-agent/review-synth-nine (merged side-agent/synthesis-nine at 572d541b; BRAINSTORM/README.md conflict
resolved by keeping both the z39 and s9 tables). From-scratch scripts: `scripts/review_r282_*`. ES is not solved anywhere.

## Summary verdicts (filled in claim by claim)

| claim | verdict |
|---|---|
| Prop 2.1 (a)–(d) (M^{lev}_t ≥ 0, = 0 at squares) | SOUND (as statements about the defined quantity M^{lev}) |
| Prop 2.2 (∃ 4 \| t with M^{lev}_t > 0 ⟺ non-square; witness t ≤ 4ℓ(n)) | SOUND |
| "in level coordinates BL's class IS χ_{−t}" (I2, §2 Reading, §5, memo title, README "PROVED") | GAP → SOUND-AFTER-REPAIRS (true only for n ≡ 1 (4), and never proved in the document; see D1) |
| 0 failures over 499 500 odd non-squares ≤ 10⁶; 73.4 % witness-level hit rate | SOUND (reproduced exactly) |

## Claim A — Prop 2.1, Prop 2.2 and the "BL's class is χ_{−t}" dictionary

**Re-derivation.** For 4 | t, D = −t ≡ 0 (4) is a discriminant, so χ_{−t} = (−t/·) is a real character mod t with
χ_{−t}(−1) = sign(D) = −1. (a) d ≡ −1 (t) ⇒ χ(d) = −1; #{d | N : χ(d) = −1} = (τ − σ_χ)/2 since gcd(N, t) = 1; positivity ⟺ an
inert prime factor (multiplicativity: σ_χ(ℓ^e) = e + 1 iff χ(ℓ) = 1). (b) orthogonality, trivial. (c) ℓ | 1 + tm² ⇒ ℓ odd, ℓ ∤ tm,
−t ≡ (m⁻¹)² — fine. (d) Dirichlet's formula, fine (gcd(N, t) = 1). Prop 2.2: n = n₀s² with n₀ > 1 squarefree; ℓ ↦ (n₀/ℓ) is a
non-principal character mod 4n₀ on odd primes, so infinitely many odd primes ℓ ∤ s with (n/ℓ) = −1 exist; multiples of 4 in
[4, 4ℓ] cover every residue mod ℓ (and −n⁻¹ ≢ 0, so in fact t ≤ 4(ℓ − 1)); (−t/ℓ) = (n⁻¹/ℓ) = (n/ℓ) = −1. Burgess applies to the
least ODD prime non-residue (restrict the Vinogradov argument to odd integers: Σ_{m≤x, m odd} χ(m) = S(x) − χ(2)S(x/2) = o(x));
GRH: Bach's "least prime outside a proper subgroup of (ℤ/8n₀)^*" gives an odd prime ≪ log² n. Both asides are fine.

**From-scratch checks.**
* `scripts/review_r282_levelbm.c` (own primality, Euler criterion, own witness search, own (★)-divisor scan): all 499 500 odd
  non-squares ≤ 10⁶: 0 failures, max ℓ = 71; witness level carries a (★) word for 366 491 = **73.37 %** (≤ 2·10⁵: 72.13 %) —
  matches the author's 73.4 % / 72.1 %. (Author's square counts 223 / 499 exclude n = 1; I count 224 / 500. Cosmetic.)
* `scripts/review_r282_levelbm2.py` (own Kronecker symbol; NO use of the witness formula): for every odd n ≤ 20 001, brute
  force over 4 | t ≤ 400 for an inert prime factor of tn + 1: found at every non-square (max minimal level 72), never at a
  square; D⁻_t(m²·t + 1) = 0 for t ≤ 40; Prop 2.1(a) inequality, parity of τ − σ and "τ − σ > 0 ⟺ inert factor" for all odd
  n < 400, t ≤ 120; χ_{−t} periodic mod t, multiplicative, odd for t ≤ 200. Odd squares ≤ 10⁶ × 4 | t ≤ 400: 0 inert levels.
* `scripts/review_r282_blevel.py` — **the dictionary itself**, by evaluating BL's α = (−x/z, −y/z) at the level-slicing rational
  points (C = t/4, u = (δ+1)/t, v = (N/δ+1)/t, α(P) = (−v/n, −v/u)) with an explicit odd-p Hilbert symbol, p < 400, t ≤ 60:
  p ≡ 1 (4): inv_p α = χ_{−t}(δ) at 2928/2932 points; p ≡ 3 (4): inv_p α = **−χ_t(δ)** (EVEN character) at 3052/3060 points
  (χ_{−t}(δ) only at 1074/3060). All 12 mismatches are p | t (non-generic); 6 points with p | δ + 1 skipped.

**Hand proof of what the dictionary really is.** For p ∤ t(δ+1)uv-denominators: inv_p α(P) = ((−v/u)/p) = (−uv/p), and mod p,
N ≡ 1 gives uv ≡ (δ + 1)²/(δt²), so inv_p = (−δ/p) = (−1/p)(δ/p). Quadratic reciprocity with tp ≡ −1 (mod δ):
(p/δ) = (−t⁻¹/δ) = χ_{−t}(δ), so **inv_p α(P) = (−1/p)·(−1)^{(δ−1)(p−1)/4}·χ_{−t}(δ)**, i.e. χ_{−t}(δ) for p ≡ 1 (4) and
−χ_{−4}χ_{−t}(δ) = −χ_t(δ) for p ≡ 3 (4). The BM factor 1 + inv_∞·inv_p is then 1 − χ_{−t}(δ) resp. **1 + χ_t(δ)** — for
p ≡ 3 (4) it is the {1, χ_t} projection, which never vanishes (σ_{χ_t}(N) > −τ(N) as χ(1) = 1). (For composite n the same
computation with the Jacobi symbol gives the same n mod 4 dichotomy at the product of the inv_ℓ, ℓ | n, at generic points.)

### Defects for Claim A
**D1 (MAJOR — overclaimed/unproved dictionary).** Locations: §1 (I2) "Answer (§2): one odd quadratic character χ_{−t} ∈ O_t …";
§2 "Reading" ("level slicing … χ_{−t}(d) (Prop 2.1)"); §4 row "Thm K × BM class … PROVED"; §5 first bullet; memo
`s9_level_bm_character.md` title + "PROVED dictionary"; BRAINSTORM/README s9 row label PROVED. (i) Nothing in §2 proves that
χ_{−t} is BL's class: Prop 2.1 only DEFINES M^{lev} as the {1, χ_{−t}} part; no local invariant is ever computed. (ii) The
claim is false as stated for odd n ≡ 3 (mod 4): there BL's class at the level points is the EVEN character χ_t ∈ E_t (with a
sign), see above. Prop 2.1/2.2 remain correct as statements about M^{lev}, but the sentence "the BM layer is χ_{−t} ∈ O_t" and
"Prop 2.2 proves the BM relaxation at every non-square" need the restriction n ≡ 1 (4) (for n ≡ 3 (4) the true BL factor is
trivially positive, so nothing is lost for ES). *Repair:* add a Lemma 2.0 with the inv_p computation above (generic points
p ∤ t, p ∤ δ + 1), state "for n ≡ 1 (mod 4) BL's class at level t is χ_{−t}; for n ≡ 3 (mod 4) it is −χ_t", restrict the
"twin of O268 Thm 1.1" claims to n ≡ 1 (4), and relabel the dictionary "PROVED (generic points, n prime ≡ 1 (4))".

**D2 (MINOR).** §2 Check: "odd squares … 223 squares … 499 squares" — these exclude n = 1 (224 / 500 odd squares ≤ 2·10⁵ / 10⁶).
Say "odd squares > 1". Also "t ≤ 4ℓ" can be sharpened to t ≤ 4(ℓ − 1).
