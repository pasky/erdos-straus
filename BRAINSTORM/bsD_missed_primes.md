# bsD_missed_primes — the 71 primes missed by the quadratic slices are "locally square", not cubic; the next layer is a lottery (O177)

**ES is not solved here.** Labels as in DISCOVERIES.md. Script `scripts/bsD_missed.py` (≈ 1 min at 10⁶).

## Idea
Direction (c): O176 found that the 9 + 9 "parity-visible" slices 4cd | 24 cover all but 71 of the 9732 primes
p ≡ 1 (24) below 10⁶. If a *cubic* reciprocity governed the next layer, the misses should be structured by cubic
characters and a "cubic layer" (slices with (ℤ/4cd)^× of exponent | 6, i.e. 4cd | 504) should catch them.

## Literature
O176 (`BRAINSTORM/bsC_parity_quadratic_only.md`, Cor 2); (J)11 (SYNTHESIS_SPARKS: locally-square primes);
`BRAINSTORM/adv_stacked_primes.md` (adversaries with many small QRs); GEOMETRY_ES §5 (Type I levels with (−d/p) = +1
are BM-removed).

## Structure (PROVED remark + EVIDENCE)
* **Remark (PROVED, elementary).** For p ≡ 1 (24), (−1/p) = (2/p) = (3/p) = 1, so (−d/p) = +1 for every d | 6: **all
  nine Type I quadratic slices are Brauer–Manin-blocked** (bsD_frobenius_closure Thm 2(a)). Only the nine Type II
  slices f | 1 + 4c²dp, f ≡ −1 (4cd), cd | 6 remain. A prime ℓ can divide N = 1 + 4c²dp only if (−dp/ℓ) = 1; if p
  is a QR mod ℓ this needs (−d/ℓ) = 1, which fails for half the d. So primes that are QRs modulo many small ℓ
  ("locally square", square-mimicking — the B5 shadow) starve the quadratic Type II slices of small factors.
* **EVIDENCE (p ≡ 1 (24) < 10⁶).** Missed primes: mean least QNR 12.0 vs 7.5 (random control of 600); fraction with
  (p/5) = (p/7) = 1: **0.68 vs 0.245**. Cubic data are unbiased: 2 a cubic residue 0.38 vs 0.32, 3: 0.35 vs 0.32,
  p a cube mod 7: 0.37 vs 0.34, mod 9: 0.35 vs 0.35 (n = 71; all within ≈ 1σ).
* **Layers by exponent of (ℤ/4cd)^×** (each layer contains the quadratic one):
  | layer | moduli | #slices (c,d) | missed of 9732 |
  |---|---|---|---|
  | exponent 2 (quadratic) | cd ∣ 6 | 9 (+9 Type I, all blocked) | 71 |
  | exponent 4 (quartic) | cd ∣ 60 | 54 | **2** (76441, 950401) |
  | exponent 6 (cubic/sextic) | cd ∣ 126 | 54 | 12 (3361, 62497, 83449, …) |
  | exponent 12 | cd ∣ 16380 | 972 | 0 |
  (R177 repair: table cells fixed; all numbers reproduced by `scripts/review_ld_missed.py`.)
  The least covering slice of a missed prime is (c,d) = (2,2) (M = 16) or (1,5)/(5,1) (M = 20), Type II, in most cases.

## Barrier screen
* The quartic layer beats the equally large sextic layer (2 vs 12 misses) because its moduli are smaller (≤ 240 vs
  ≤ 504) — the expected lottery ordering (hit probability ≈ decreasing in M), not reciprocity. No cubic structure.
* B2/B1: any finite layer is a fixed finite slice set: fails i.o. under H (redteam-automorphic-2 Thm 2.2). B5: the
  misses are exactly the square-mimicking primes (quadratic data at small ℓ), as T1 predicts for any Type I/II route.

## Assessment
EVIDENCE, negative for direction (c): **the 71 misses are explained by quadratic (locally-square) data; cubic
characters of p are unbiased; there is no cubic layer** — the order-≥3 part R of KUDLA_ES §2 behaves as a lottery.
Promise 0–1.
