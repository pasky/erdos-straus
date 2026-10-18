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

## Claim B — Lemma 1.1, Cor 1.2 (k-union = some word coordinate ≡ 0 (mod k)), sign remark
Verdict: **SOUND** (Lemma 1.1, Cor 1.2 hold for every n ≥ 1, not only odd n, and every k ≥ 2).

**Re-derivation.** Lemma 1.1: (T, U, 1) ∈ W(cn) ⟺ U(T − 1) = cn + 1; with T = cs, c(n + s) = (cn + 1) + (cs − 1) and
gcd(c, cs − 1) = 1 give cs − 1 | n + s; inverse as stated; U = cg − 1 ≥ 1 since (c, g) = (1, 1) forces n = −1. Cor 1.2: c = 1 line
n + a + b = kabd ⟺ word (kd, a, b). b = 1 line cn + a + 1 = kacd ⟺ (kcd, a, 1) ∈ W(cn) ⟺ (Lemma 1.1, s = kd) (c, g, kd) ∈ W(n);
conversely (t, u, kd) ∈ W(n) ↦ (c, a) = (t, tu − 1): cn + a + 1 = t(n + u) = t·v(tu − 1) = kacd since n + u = v(tu − 1). The
side condition cs > 1 is automatic for k ≥ 2. u ↔ v symmetry of W(n) gives "k | v ⟺ k | u (for some word)". Correct.

**From-scratch checks.** `scripts/review_r282_lines.py 300 12`: for ALL n ≤ 300 and 2 ≤ k ≤ 12, both lines decided from their
original (a, b, c, d) definitions vs. word coordinates; Lemma 1.1 bijection for n < 120, c ≤ 6 — 0 mismatches (3 300 cases).
`scripts/review_r282_k8.c` (own word enumeration): k = 8 union fails at 35 primes 3 ≤ p < 8000 (22 ≡ 1 (4)), i.e. 34 primes
5 ≤ p < 8000 incl. 131, 241 — matches SPARKS8; k = 4: union never fails for p < 70 000, b = 1 fails exactly at 193, 2521, 66529.
Sign remark ("4 | t ⇒ σ = −1" three-line proof): X = tu − 1 ≡ 3 (4); (X/n) = (n/X) by reciprocity for n ≡ 1 (4); n ≡ −t⁻¹… more
precisely tn ≡ −1 (mod X)·?—not quite: XY = tn + 1 gives tn ≡ −1 (mod X), so (n/X) = (−t/X)·(t⁻²/X) = (−1/X)(t/X) = −(t/X);
(t/X) = (4/X)(C/X) = (C/X) and X = 4Cu − 1 ≡ −1 (mod every odd prime power of C) — for C = 2^e C′, (2/X) = +1 as X ≡ −1 (8)
when e ≥ 1, and (C′/X) = (X/C′)(−1)^{(C′−1)/2} = (−1/C′)·(−1)^{(C′−1)/2} = +1. Correct (the document's sketch elides the
reciprocity sign for C′ but the conclusion holds).

### Defects for Claim B
**D3 (MINOR).** §1 "Checks": "the k = 8 union fails at exactly 34 primes < 8000" — p = 3 also fails; say "34 primes
5 ≤ p < 8000" (as SPARKS8 does) or "35 odd primes < 8000".
**D4 (MINOR).** Cor 1.2 is stated "for every odd n" but the proof never uses oddness (verified for all n ≤ 300); harmless.
