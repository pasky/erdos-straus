# R175 — hostile review of O175 (SIGNLAYER_DEEP.md + BRAINSTORM/bsB_*.md)

Reviewer: R175 (branch side-agent/review-signlayer). Author files merged from side-agent/spark-signlayer.
From-scratch scripts: `scripts/review_sl_*.py` (own F₃[T] arithmetic; nothing imported from `scripts/bsB_*`).
Data: `data/review_sl_*`.

## Summary verdicts

| Claim | Verdict |
|---|---|
| SIGNLAYER Lemma 1.1 (Case B on the slice = finite search per level K; L'', r, g' forced by (h₁, h₁', K)) | SOUND (re-derived; brute-force verified against direct factorisation of D); MINOR wording defects D1–D3 |
| §2 complete enumeration, CERTIFIED through K = 17 / 19 | SOUND-AFTER-REPAIRS: counts and exact measures reproduced independently through K = 13; the translation "K ≤ 17 ⇒ all N ≤ 18 (j ≤ 17), every L', g" is wrong (D4, MAJOR) |
| Covered measure 0.333 → 0.4906, "≈ 50 % stays uncovered" | numbers SOUND (exact rationals through K = 13); labels EVIDENCE/Assessment acceptable after D5–D6 |
| Lemma 3.1 (symmetries u ↦ u⁻¹, u(T) ↦ u(−T)) | (i) SOUND; (ii) true but the written proof has a GAP (needs FF2's QR degree parity) (D7) |
| "x* orbit = the four height-1 slice points" | FALSE as stated (six height-1 points; two are covered) (D8) |
| Lemma 3.2 (degree imbalance at x*) | SOUND; "necessarily lopsided" slightly overclaimed (D9) |

(Memo verdicts follow in later sections.)

## SIGNLAYER Lemma 1.1 — SOUND

*Dependence on FF2.* The lemma takes as input FF2 §0.2's Case B reduction (validity of a family at x_u ⟺ D = 1 + T^k a0 b0
= 1 + T^{N+1}L'g has a monic divisor E with E ≡ −u (mod T^{N+1}), E ≡ −1 (mod L')), which R166 re-derived and found
SOUND, and which only uses x ≡ 1 at every prime ≠ T (so it holds at every slice point x_u, not only x*). Note
lc E = 1 because the two terms of the Case B sum have different degree, so the cofactor E' is monic as well. I accept
the reduction. Lemma 1.1 is valid only for the **sub-slice u ≡ 1 (mod T), u ≢ 1 (mod T²)** (v(0) ≠ 0). This is
where h₁(0) ≠ 0 is used (D5).

*Re-derivation.* E = −1 + L'h, E' = −1 + L'h' (from E ≡ −1 mod L'; this also holds for E' because D ≡ 1 mod L').
EE' = D ⟺ L'hh' − h − h' = T^{N+1}g. E ≡ −u (mod T^{N+1}) ⟺ L'h ≡ −Tv, so h = Th₁ with h₁L' ≡ −v (mod T^N) and
h₁(0) ≠ 0. Reducing the identity mod T gives T | h'. (The proof says "same for E'". That step needs this one-line
argument, which the proof leaves out. MINOR, D2.) So h' = Th₁' and T h₁h₁'L' − h₁ − h₁' = T^{N+γ}g', where
N + γ = K + 1. The leading term T h₁h₁'L' cannot cancel. This gives a + b + deg L' = K + deg g', i.e.
a + b + deg L'' = K. Since gcd(g', T) = 1, Tg' | h₁ + h₁'. That gives r and (I), (II). r ≠ 0, because r = 0 forces
h₁h₁'L'' = T^K with all three factors T-free, so K = 0 and h₁ = h₁' = 1, contradicting h₁(0) = −h₁'(0).
deg r ≤ max(a, b) − 1 − deg g' < a + b. So L'' = quo(T^K, h₁h₁') and r = L''h₁h₁' − T^K are forced. **In addition,
g' = (h₁ + h₁')/(T r) is forced**, so the whole tuple is a function of (h₁, h₁', K). This is how the enumeration
uses it; the statement lists g' as a free coordinate. The admissible N are exactly ⌈K/2⌉ + 1 ≤ N ≤ K + 1, from
0 ≤ γ = K + 1 − N ≤ N − 1. The cylinders for different N are nested, so the union over N is the N₀ cylinder,
N₀ = max(2, ⌈K/2⌉ + 1). D = 1 + T^{K+2}L'g' does not depend on N. The converse direction checks out. As a
by-product, j = 0 (N = 1) is impossible: it would force K = 0. This proves one of FF2's unproved "consequences"
(R166 D5) on the slice.

*Bound.* deg L' = deg g' + deg L'' ≤ (max(a, b) − 1) + (K − a − b) ≤ K − 1. The stated "deg L' ≤ 2K" is true but
loose (MINOR, D3).

*Independent machine check* (`scripts/review_sl_caseB.py brute 6 3`, `data/review_sl_brute_6_3.txt`). For every
N ≤ 6, 0 ≤ γ ≤ N − 1, monic T-free L' of degree ≤ 3 and every monic g' | L', I factored D = 1 + T^{N+1+γ}L'g'
completely, by trial division with my own irreducibles. For each monic divisor E with E(0) = −1, E ≡ −1 (mod L')
and v(0) ≠ 0, I recorded (N, γ, L', g', E). Result: **126 families**, identical as a set to those predicted by
Lemma 1.1 (enumerating (h₁, h₁') with K ≤ 10 and expanding over N). Nothing is missing and nothing is extra. So
Lemma 1.1 is correct both as algebra and as a search reduction.

**D1 (MINOR, wording).** "correspond bijectively to tuples (h₁, h₁', g', L'', r)". The bijection is with the data
(N, γ, L', g', E). A Case B *family* also carries (a0, b0, types), and many (a0, b0) share the same L = lcm and
g = gcd. Also, g' and L'' are functions of (h₁, h₁', K). Repair: "with the divisor data (N, γ, L', g', E); moreover
the whole tuple is determined by (h₁, h₁', K)".
**D2 (MINOR).** Proof: write the line "mod T, h' ≡ 0, so h' = Th₁'".
**D3 (MINOR).** Replace "deg L' ≤ K + max deg h ≤ 2K" with the sharp bound deg L' ≤ K − 1 − min(a, b).
