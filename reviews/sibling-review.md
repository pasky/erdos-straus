# R249 — hostile review of O242 (SIBLING.md, BRAINSTORM/z17_*.md, AGENT_REPORT_O242.md)

Reviewer: R249 (side-agent/review-sibling). Author branch merged: side-agent/sibling-conj.
Status: in progress.

## Summary verdicts
(filled claim by claim below)

## Claim-by-claim

### Lemma 1.1 (≤ 2 balls per key (m', g', s, a) in a parent) — SOUND
Re-derived: EE' = T²L'²w₁C₁ − TL'(w₁ + C₁) + 1 = T^sL'g' + T²L'g'v₁ − T²L'g'v₁ + 1 = 1 + T^s m'g'² (using L'²/m' = L'g').
E + 1 = T m'g'w₁ ⟹ E ≡ −1 (mod m'g'); B_τ ⊂ V fixes E mod T^N (N = N(s)), gcd(T, m'g') = 1, so E lies in one unit class mod
Q = T^N m'g' (unit: E(0) = −1, E ≡ −1 mod m'g'). ρ = N + z + y, n = deg F = s + z + 2y, 3ρ − n = 3N − s + 2z + y ≥ s/2 > 0;
deg E = a + y + z fixed by the key. SP Lemma 1.4 (checked: hypotheses "F ≠ 0, ρ ≥ 1, σ unit, 3ρ > n", conclusion ≤ 2 divisors of
degree d in the class, monic or not) applies verbatim. No hidden hypothesis; the key must include a (it does) and s (it does).
From-scratch check (`scripts/review_r249_caseb.py`: own Case B enumerator, route E·C₁ = g'T^{s−1} + w₁ with a ≤ b plus the
w₁ ↔ C₁ swap, validated against an unpruned brute force over (m', w₁, C₁) for s ≤ 9 — identical tuple sets; dump
`scripts/review_r249_dump.py`, check `scripts/review_r249_check11.py`): q = 3, all 274 Case B tuples with s ≤ 15 — the maximum
number of distinct E per (key, parent) is **1** (the bound 2 is never attained in this range).
Remark (not a defect): the lemma is correct but, as the author says, bounds a quantity that the data show to be irrelevant
(siblings never share a key).

### Prop 1.3 (Klein symmetry of Case B balls) — SOUND
Re-derived the sign bookkeeping: (B₁) sign (−1)^{z+a+b−2} = (−1)^s; (B₂) needs a ≡ b (from a + b + z = s and z ≡ s) and
a + y + s ≡ 0 (from y + t = max(a, b), t ≡ s); E^σ sign y + z + a ≡ 0. All three use OA Cor 1.7 (z ≡ t ≡ s mod 2), which I
checked is stated for all odd q and k ≥ 2 (FF_ODD_ABSENCE.md l.110). The swap is an obvious symmetry of (B) and
(−E)(−E') = EE' ≡ 1 (mod T^s), s ≥ N + 1, so the inverse ball is the E'-ball of the same level. The maps are isometries of
T-adic cylinders, so "ball set invariant" is meaningful level by level.
From-scratch check (same 274 tuples, s ≤ 15, `scripts/review_r249_check11.py`): parity law holds on every tuple; y + t =
max(a, b) on every tuple; τ^σ is a valid Case B tuple and E^σ = E(−T) for every tuple (asserted); the 128 Case B balls of depth
≤ 9 (depths 3..8 complete; 9 partial until s = 16 is added) are invariant under u ↦ u(−T), u ↦ 1/u and ι; 32 are ι-fixed.
"Reading" (an involution fixing V fixes a child, so symmetry never forbids a triple): correct and trivially so.
