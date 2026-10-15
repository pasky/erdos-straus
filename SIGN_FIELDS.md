# SIGN_FIELDS — exponential near-squares, sign fields of other numerators, the non-genus layer (task O232, spark relay Z2)

Status: checkpoint 1 (O232), awaiting review. **ES is not solved here, nor any infinite case of it unless stated with a
complete proof.** Labels as in DISCOVERIES.md. Builds on NEAR_SQUARE_EXIST.md (O225, sign fields Σ_M = ℚ(ζ_M, √−M)),
NEAR_SQUARE.md ((J)55), EXPONENT_COVERING.md ((J)22: Thm 1.4 compactness criterion, ec_cover / ec_cert), DEDEKIND_ES
Thm 4.5 (five-slice sign table), FOUR_SPECIFIC ((J)46). Memos BRAINSTORM/z8_*.md, scripts `scripts/z8_*`, certificates
`data/z8/`.

## 1. Exponential near-squares n_s = c₀·4^s + k (goal 1, O225 spark S4)

Setting. n_s = c₀m² + k with m = 2^s. EXPONENT_COVERING Thm 1.4 applies verbatim with base b = 4 and additive constant
k (its proof is family-agnostic): a finite covering of {n_s : s ≥ s₀} by ET classes and divisor classes exists iff the
limit set Λ = {ν(μ) : μ ∈ Ẑ}, ν(μ)_2 = k, ν(μ)_q = c₀·4^μ + k (q odd), avoids the sterile set S′.

**Lemma 1.1 (which families are non-trivial; PROVED, elementary).** For s ≥ 2, n_s ≡ k (mod 8) and n_s ≡ c₀ + k (mod 3).
Unless k ≡ 1 (mod 8) and c₀ + k ≡ 1 (mod 3), every n_s with s ≥ 2 lies outside Mordell's six classes mod 840 that are
≡ 1 (mod 24), hence is ES-solvable by a fixed congruence identity. (Odd n ≢ 1 mod 8 or ≢ 1 mod 3: classical.)
So the interesting offsets are k ≡ 1 (8) with c₀ + k ≡ 1 (3); for c₀ = 1: k ≡ 9 (mod 24). Note Lemma 2.3 of NEAR_SQUARE:
Z_k^□ ≠ ∅ for all these k (k ≡ 1 mod 8), so **no finite set of polynomial families in m covers n = m² + k for all m**
(NEAR_SQUARE Thm 2.2); the question is whether the exponential subfamily m = 2^s escapes.

**Lemma 1.2 (no integer unit-square points; PROVED).** Let c₀ = 1 and k ≥ 3 odd. For ℓ ∈ ℤ, ν(ℓ) is never a profinite
unit square. *Proof.* ℓ ≥ 0: the odd components are the odd integer N = 4^ℓ + k ≥ 4; a square in every ℤ_q (q odd) and a
unit at every odd q forces N = s² with s a power of 2, i.e. N = 1: impossible. ℓ = −a < 0: components (1 + k·4^a)/4^a;
as before 1 + k4^a = s² with s a unit at all odd primes, s odd ⇒ s = 1: impossible. ∎
So the Cor 1.5 obstruction of (J)22 never occurs here; what remains are *non-unit* square points
(4^ℓ + k = s² or 1 + k4^a = s², covered by D_q for q | s but making coverings expensive, cf. EXPONENT_COVERING §4.3) and
the non-square sterile part of S′.

**Theorem 1.3 (PROVED, computer-assisted; certificates checked by ec_cert.py).** ES holds for every n = 4^s + k, s ≥ 0, for
k ∈ {9, 57, 81, 129, 153, 177, 201, 225, 249}. Certificates `data/z8/cert_c1_k*.json` (L ∈ {6, 24, 30}; 2–8 classes),
produced by `scripts/z8_expnear_cert.py` and checked by `ec_cert.main` (polynomial identity, integrality on the class,
positivity bound, periodicity M′ | 4^L − 1, exact verification for all s ≤ 600, brute force below s₀, T1 control).
Of these, k = 57, 153, 177, 225 have members in Mordell's hard classes mod 840 (s ≡ 3 mod 6: n ≡ 121; s ≡ 2 mod 6:
n ≡ 169; s ≡ 5 mod 6: n ≡ 361; s ≡ 0 mod 3: n ≡ 121, 289), the others are covered by mod-840-type classes. These are
*near-square* infinite families n = m² + k on which polynomial families in m provably cannot cover (Z_k^□ ≠ ∅):
the exponential coupling of EXPONENT_COVERING Prop 2.2 is what makes them coverable.
Survey (`scripts/z8_expnear_survey.py 1 300 30000 6 12 18 30 36 60`; EVIDENCE): of the 13 non-trivial k ≤ 300, 9 are
covered (above; 225 needs L = 24), 4 are OPEN at the search limits: k = 33, 105, 273, 297.

**1.4 The OPEN offsets (EVIDENCE + PROVED pieces).** Integer *non-unit* square points: k = 33: 4² + 33 = 7², 4⁴ + 33 = 17²,
1 + 33·4² = 23²; k = 105: 4² + 105 = 11², 4³ + 105 = 13², 4⁴ + 105 = 19², 1 + 105·4² = 41²; k = 273: 4² + 273 = 17²;
k = 297: 4³ + 297 = 19². (Same pattern as (J)22 §4.2: every OPEN k has an integer square point.)
* **k = 105 is the "maximally hard" offset** (PROVED, trivial): 105 = 3·5·7 ≡ 1 (mod 8), so n_s ≡ (2^s)² (mod 105) and
  n_s ≡ 1 (mod 8): **every** member lies in one of Mordell's six hard classes mod 840 (all six occur), and n_s is a square
  modulo every prime of k — the near-square T1-mimicking at the primes of the offset.
* Unit-square screen (`scripts/z8_expnear_screen.py 1 105 3000000 … 360 …`, CERTIFIED finite computation): at L = 360
  every residue s mod 360 has n_s ≡ 0 or a non-residue modulo some prime q < 3·10⁶ with ord_q(4) | 360. Hence
  **Λ₁₀₅ ∩ Sq^× = ∅** (the square half (EH) of (J)22's criterion holds); only the non-square part of S′ can obstruct.
  (k = 33: the screen leaves exactly s ≡ −2 (mod L) at every L tested — the point μ = −2, n = 23²/16, a non-unit square,
  killed by D₂₃ only when 11 | L.)
* The obstruction is the *class supply*, at **mixed points**: the general search leaves s ≡ 124 (mod 360), and refines
  to s ≡ 844 (mod 2520). These exponents are the CRT gluing μ* = "4 in every ℓ-adic component except ℓ = 3, where
  μ* = −2" (`scripts/z8_point.py`): at primes q with 3 ∤ ord_q(4), n ≡ 4⁴ + 105 = 19²; at q with ord_q(4) a 2·3-power,
  n ≡ 4⁻² + 105 = (41/4)²; only at q whose order mixes 3 with another prime is n_q generic (non-residue at q = 181,
  ord 90, but no ET class of admissible modulus ≤ 2·10⁶ hits it). The point μ* itself lies in the II2 class
  (2, 23, 919) (ord_919(4) = 153), so μ* is NOT sterile; but its neighbours with other 17-adic components are again
  uncovered (L = 42840). An adaptive "lifting" covering (`scripts/z8_adaptive.py`, ordered class lists, independent
  replay checker `scripts/z8_cert_tree.py`) drives the uncovered Haar measure of the exponent space down
  monotonically — 8.3·10⁻³ (L = 360) → 1.2·10⁻³ (75 600) → 7·10⁻⁴ (982 800) → 8·10⁻⁵ (17 463 600) — without
  terminating within the run (EVIDENCE that k = 105 is coverable, at large cost; not a certificate).
* Assessment. Mixed points are the exponential analogue of (J)22 §4.3's near-square points: an exponent that imitates
  *different* integer square points in different ℓ-adic components of Ẑ. They are where coverings get expensive;
  whether some mixed point is sterile (which would make "all 4^s + 105" uncoverable) is open. No mixed point found so far
  is sterile.
