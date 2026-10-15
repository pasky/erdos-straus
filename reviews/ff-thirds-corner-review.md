# R247 — hostile review of O227 (FF_THIRDS_CORNER.md, branch side-agent/ff-thirds-corner)

Reviewer: R247. Status: IN PROGRESS (round 1). From-scratch scripts: scripts/review_r247_*.

## Summary verdicts
(filled in claim by claim below)

## Claim-by-claim

### Setting / "covers at level N" (FUNCTIONFIELD_ES3 Lemmas 1.1, 2.1, 3.1)
Re-derived: a family (L', j, γ, g', E) has s = N + 1 + γ, 0 ≤ γ ≤ j = N + 1 − k, so a tuple of parameter s lives on the
levels N(s) = ⌈(s + k − 2)/2⌉ ≤ N ≤ s − 1; the cylinders are nested decreasing in N, so "tuple covers x_u" ⟺
E ≡ −u (mod T^{N(s)+1}). (B) gives T ∤ m', g', w₁, C₁ and v₁(0) ≠ 0. SOUND.

### Lemma 1.1 (R3 identity) — SOUND
Re-derived: E·C₁ = (Tg'm'w₁ − 1)C₁ = Tg'(T^{s−2} + v₁) − C₁ = g'T^{s−1} + w₁; symmetric for E'. Also re-derived
EE' = 1 + T^sL'g' (used in Prop 2.1) and R4: Ev₁ = m'w₁(w₁ + C₁) − v₁ = T^{s−2} + m'w₁² (used in Prop 5.1).

### Lemma 1.2 (Liouville lemma) — SOUND
Re-derived line by line. Mod T^m (m ≤ s − 1) EC₁ ≡ w₁, so E ≡ −u gives T^m | w₁ + uC₁, a polynomial of degree
≤ max(a − 1, b − 1 + h); nonzero ⇒ degree ≥ m. Exact case for u = 1 + cT: monic w₁, C₁ force c = −1, w₁ = (T − 1)C₁,
TC₁ = Tg'v₁, gcd(C₁, v₁) = 1 (a common prime divides T^{s−2}, and T ∤ C₁ by (B)) ⇒ v₁ = 1, then (T − 1)m'g'² = T^{s−2} + 1,
0 = 2 at T = 1. Correct. Numerical confirmation: brute-force census (own code `review_r247_census.c`, enumerates all
(m', w₁, C₁), no CRT/Liouville input) — see the census section below.

### Cor 1.3 — SOUND (one MINOR)
Correct for k = 2 (s ≥ 4). The cyclotomic paragraph is correct: v₁ = −1 ⇒ lc(w + C) = −lc g' = 2 ⇒ a = b (unequal degrees
give lc 1) ⇒ 2(a − 1) ≤ s − 2 ⇒ max(a − 1, b) = a ≤ s/2 < N(s) + 1. Every equal-degree tuple misses x*_c. (Note: the
conclusion is not w ↔ C symmetric — correct, because covering is E ≡ −u while E' ≡ −u^{−1} is not a polynomial point.)
* MINOR-1 (statement): "k ≥ 2, s ≥ 4 so that N(s) + 1 ≤ s − 1" is only right for k = 2; in general N(s) + 1 ≤ s − 1 ⟺
  s ≥ k + 2 (as the proof says). E.g. k = 3, s = 4: N = 3, N + 1 = 4 > s − 1. Repair: write "s ≥ k + 2".

### Prop 1.4 (exact tuples) — SOUND-AFTER-REPAIRS (MINOR)
The forward direction is correct (re-derived: C₁ | g' from gcd(C₁, Tv₁) = 1; g₂v₁ = −(u − 1)/T; lc u = −1;
E = Tg₂(T^{s−2} + v₁) − 1 = g₂T^{s−1} − u). The h = 1 reading (T ≡ 1 mod u ⇒ 2 ≢ 0) is correct.
* MINOR-2: the converse ("iff … then the displayed data satisfy (B₁)") omits needed side conditions: T ∤ g₂ (else T | g'),
  deg v₁ < s − 2 (else the product has the wrong degree/leading coefficient and the tuple's parameter is not s), and
  T ∤ (T^{s−2} + v₁)/u, i.e. v₁(0) ≠ 0 (automatic when u'(0) ≠ 0 and T ∤ g₂, not in general since Prop 1.4 does not assume
  u'(0) ≠ 0). Repair: add "T ∤ g₂, deg v₁ < s − 2, v₁(0) ≠ 0" to the converse.
Numerics: my full search (no Liouville input) finds exact tuples (w₁ = −uC₁) only at points with lc u = −1 (levels 3..8,
54 points), consistent with Prop 1.4.
