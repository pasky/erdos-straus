# R257 — hostile review #1 of EXP_OPEN (O246), round 1

Reviewer: R257 (side-agent/review-exp-open). Author branch merged: side-agent/exp-open. From-scratch scripts:
`scripts/review_r257_*.py` (no z19_/z15_/z14_ imports).

## Summary verdicts
| claim | verdict |
|---|---|
| Theorem 3.1 (ES for every 63·2^s + 1) | (in progress) |
| Theorem 2.3 (moving-gap class) | (in progress) |
| Theorem W / Lemmas 1.1–1.5 / Cor 1.7 | (pending) |
| Prop 2.1, Reduction 2.5, Prop 4.1, Comp 4.2 | (pending) |

## 1. Theorem 3.1 / Theorem 2.3 — from-scratch replay

`scripts/review_r257_cert63.py data/z19/cert63_et.json 1500` (pure Fractions; reads only the polynomial DATA of the
certificate). Output:
* Theorem 2.3: Type II identity cn + a + b = 4abcd verified as a polynomial identity in Y; the three factorisation claims
  (n + 4a²d = 63(Y + 3)(Y² − 3Y + 9), 4abd − n = 3(Y² − 3Y + 9), 4acd − 1 = 21(Y + 3)) verified.
  Integrality re-derived by hand: 340 = 4·85; for j = s/3 ≥ 2, Y = 2^j ≡ 0 (mod 4) and the numerators are ≡ 28, 64 ≡ 0
  (mod 4); ord₈₅(2) = lcm(ord₅ 2, ord₁₇ 2) = lcm(4, 8) = 8, so s ≡ 0 (24) ⇔ 8 | j ⇒ Y ≡ 1 (mod 85) ⇒ numerators ≡ 85,
  85 ≡ 0 (mod 85). So b, c ∈ ℤ for EVERY s ≡ 0 (mod 24), s ≥ 24 (for s = 0, Y = 1 fails mod 4: c = 85/340 — correctly
  excluded; s = 0 is handled by brute force). Positivity trivial (all of a, b, c, d > 0 for Y ≥ 1). Among j mod 8 only
  j ≡ 0 works (script: j ∈ [2, 10) → {8}), so the class is exactly s ≡ 0 (mod 24). **SOUND.**
* 18 classes: identity 4xyz = n(xy + yz + zx) verified for each; integer-valuedness on n ≡ r (mod M) verified by
  forward differences of p(r + Mt); positivity for n ≥ 63·2^10 + 1 verified by Taylor shift (all shifted coefficients
  ≥ 0, constant > 0 — stronger than the author's Cauchy bound); odd part of every M has ord(2) | 2520 (periods
  4, 7, 9, 10, 12, 14, 18, 24, 28, 140, 210), 2-part ≤ 2³ and r ≡ 1 mod the 2-part (consistent with n_s ≡ 1 mod 2^s).
  Hence n_s mod M depends only on s mod 2520 for s ≥ 10.
* Coverage: every s ∈ [2520, 5040) with s ≢ 0 (24) lies in some class → no uncovered residue. (The 18 classes even cover
  102 of the 105 residues s ≡ 0 (24); the three left are s ≡ 0, 840, 1680 (mod 2520), i.e. s ≡ 0 (mod 840) — consistent
  with the profinite unit-square point μ = 0.)
* Exact solutions with verified 4xyz = n(xy + yz + zx), all entries > 0, for every 0 ≤ s ≤ 1500 (62 moving, 1429 ET,
  10 brute force for s ≤ 9 with my own brute-force search).
* T1: 63·2^s + 1 = t² for s < 4000 only at s = 0 (n = 64, even) and s = 8 (127²). By hand: t ± 1 = 2A, 2(A + 1) with
  A(A + 1) = 63·2^{s−2}; consecutive integers with odd part 63 split as {63, 64} or {7·9 split…} — only 63·64 (s = 8)
  works. s = 8 is handled by brute force and lies in the divisor class D₁₂₇ (n ≡ 0 mod 127). No T1 tension.

**Verdict Theorem 3.1: SOUND** (computer-assisted proof replayed from scratch; minor wording issues D1–D2 below).
**Verdict Theorem 2.3: SOUND.** The class is genuinely outside the ET/divisor menu: x = 85b = (63Y³ + 3Y² − 9Y + 28)/4 is
not a polynomial in n = 63Y³ + 1, and the class contains s ≡ 0 (mod 840), which (as the replay shows) the 18 fixed-modulus
classes miss — consistent with EXPONENT_COVERING Cor 1.5 (63 + 1 = 4³, so n_s → 64 = 8² at every odd place and n_s → 1
2-adically as s → μ = 0: a profinite unit-square point, no ET/divisor covering).

## 2. Theorem W, Lemmas 1.1–1.5, Corollary 1.7 — re-derivation

Re-derived line by line:
* L1.1: m = 4x − n > 0 since 1/x < 4/n. Rav step correct; N ≡ N(1) = 4^{J−1}(4^J + m) (mod m) is a unit mod m because
  m is odd and gcd(m, 4^J + m) = 1. y′ = U(Y)/gcd(U(Y), V(Y)) and the gcd divides a fixed resultant-type integer R
  (R = AU + BV), so it depends only on Y mod R, constant on a smaller neighbourhood. Division argument d₁d₂ | N ✓.
* L1.2: positivity (factors with positive leading coefficient of n, n + m have no root in (0, ∞)) ✓; ρᵢ ∈ ℤ[1/2] by the
  q-adic limit Y → 1 (and m | ρ₁ + ρ₂ by closedness of m-ideals in ℤ_q) ✓; quadratic reciprocity step:
  q | M ⇒ m ≡ −4^J (q) ⇒ (q/m) = (−1/q)(−1)^{(q−1)/2} = 1 ✓ (q ∤ m since q | 4^J otherwise). Conclusion m ≡ 3 (8),
  e₁ − e₂ odd ✓.
* L1.3: N(0) = k(k + m)/4 is odd since k + m ≡ 4 (8) ✓; dᵢ(0) ∈ ℤ₂ by the 2-adic limit Y → 0, product a unit ⇒ each a
  unit ✓; root valuations: roots of n + m have v₂(α) = 2/D > 0 (contribution −2/D each), roots of n are units
  (contribution ≥ 0, total v₂(4^J/k) = 2J) ✓; n and n + m coprime and squarefree ✓.
* L1.4 (Capelli): −K, K = (k + m)/c₀ > 0, v₂(K) = 2: not a square (negative), not an odd p-th power (v₂ = 2), so only
  −4ℚ⁴, 4 | D ✓; β = w/u, u odd, u⁴ | c₀ ⇒ u = 1 ✓. Note D ≡ 2 (4) is also excluded (x irreducible) ✓.
* L1.5: both cases re-derived; the bound uses only a₁a₂a₃ = M and M ≡ 4^J (mod m), so it holds for ARBITRARY odd
  divisors aᵢ (any fixed-prime splits, any mixed sub-products). This is exactly what repairs the R253 D1 gap of EXP_105
  Cor 2.8: the 2-power exponents are now bounded by the Newton polygon (eᵢ ∈ [−2, 2J], E = 2J + 2), not by the piece
  shapes. B depends on m through r = M/m ≤ 1 + 4^J, but B(m) is decreasing and m increasing in w, so the cutoff is a
  genuine finite bound ✓.
* Theorem W assembly: νᵢ ∈ {0, 2J} (n irreducible), eᵢ ∈ ℤ ⇒ 2δᵢ ∈ ℤ; e₁ − e₂ odd ⇒ exactly one δᵢ = ½ ⇒ L1.4 ✓.
  Hypotheses checked for all six pairs: c₀ ∈ {15, 31, 7, 63, 47, 55} odd and 4th-power-free; k ∈ {1, 33, 57, 1, 17, 9}
  ≡ 1 (8); c₀ + k ∈ {16, 64}; c₀Y^D + k irreducible for all D (k/c₀ not ± an odd prime power-ratio, v₂(k/c₀) = 0 ≠ 2).
* Cor 1.7: ε = 4t − 1; n irreducible ⇒ dᵢ ∈ {λᵢ, λᵢn}, λᵢ ∈ ℤ_{>0} (2-adic integrality from n(0) = k odd), λ₁λ₂λ₃ = t;
  odd q | t ⇒ (q/ε) = 1; 2 | t ⇒ ε ≡ 7 (8); so (ρ₁ρ₂/ε) = 1 ≠ −1 ✓. (x/n constant forces an integer ratio: an odd
  denominator would have to divide n ≡ 4^J near μ = 0.)

**From-scratch finite check** `scripts/review_r257_thmW.py` (own divisor enumeration; superset: does NOT impose
m ≡ 3 (8) or e₁ − e₂ odd; `--strict` imposes them; `--wmax W` ignores the bound B and scans all odd w ≤ W):
* all six pairs: 0 relations (default, strict, and unbounded w ≤ 61).
* positive controls: (3,1) m = 11 (12 relations), (7,9) m = 19 (6), (23,41) m = 51 (4), (39,25) m = 131 (4) — identical
  counts to the author's data/z19/thmW.txt; nothing else up to w = 61.
The author's "superset" claim is confirmed independently (my enumeration is weaker than theirs and still finds 0).

**Verdict Theorem W + Cor 1.7: SOUND** for the stated menu (root families in ℚ[Y], Y = 2^{s/D}). Scope caveat D3 below.
