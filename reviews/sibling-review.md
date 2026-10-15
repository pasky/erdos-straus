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

### Lemma 1.2 (≤ 6 P-boxes per key (c, d) in a class mod r^{L−1}) — SOUND (one MINOR wording defect, m1)
Re-derived: Σ^II gives 4abd = N + e, e = (a + b)/c ≤ a + b ≤ 2b ≤ 2abd, so abd ≤ N/2 and a² ≤ N/2 for a ≤ b, i.e.
a ≤ √(r/2)·r^{L−1} (2.915·r^{L−1} at r = 17). −(4acd − 1) ≡ x (mod r^{L−1}) puts a in one class mod r^{L−1} (r ∤ 4cd), and
b(4acd − 1) = a + Nc fixes b. (4acd − 1)(4bcd − 1) = 4cd(4abcd − a − b) + 1 = 4c²dN + 1 ≡ 1 (mod r^L) (2L − 1 ≥ L), so the
second box lies in x iff the first lies in x^{−1}. Number of a ∈ [1, X] in one class mod M is ≤ ⌈X/M⌉ = ⌈√(r/2)⌉: 3 for
r ∈ {11, 13, 17}, 2 for r ∈ {5, 7}, 4 for r ∈ {19, 23}. Bound 2⌈√(r/2)⌉ per key; "six" is right for r ≤ 17.
Level-L boxes come only from K = 2L − 1 (K = 2L is empty by the r-free reciprocity of M17 Lemma 1.3), so restricting to
"P-data of level L" loses nothing for the per-level statement.
From-scratch P-enumerator (`scripts/review_r249_rbox.c`, naive (a, b) scan; reproduces D_P(K) = 2, 32, 121, 258 at r = 17,
K = 1..7, and D_Q = 2, 73 (k = 1, 3, a ≤ b) of M17) — not separately tested for the per-key bound (it is a two-line argument).

### Prop 3.1 (window (n, 5n]: "every route-type bound inside a depth-n cylinder is ≥ 3^{2s/5}") — GAP (D1, D2)
What is right: at p* = (s; s/5, s/5, s/5, 2s/5) (b = 3s/5) the *fixed-data* counts of the listed routes R1 (3^{t−2}), R2
(3^{z+y}), R3 (3^{a−1+y}), R4 (3^{z+a−1}), R4L (3^{a+z−1+max(0, y−n+1)}) are all 3^{2s/5 − O(1)}, and so are those of every
other route of SP Lemma 1.6 that the text does not mention (I checked T0 3^{3s/5}, R4′/X1/X2 3^{4s/5}, R5a 3^{3s/5},
R6a ≥ 3^{2s/5}, R8a 3^{3s/5}, R9a/R10a ≥ 3^{3s/5}, R10b ≥ 3^{2s/5}). The arithmetic 2s/5 ≤ s/2 − n ⟺ s ≥ 10n ⟺ N ≥ 5n is
right, and so is "the global bound already reaches this threshold". The exponent-level conclusion for the listed routes holds.
Caveat on the citation: SS Cor 4.2 labels "the unique maximiser (1/5,1/5,1/5,2/5), value 2/5" as **EVIDENCE (grid)**; only the
bound q^{2s/5+o(s)} is PROVED there. Prop 3.1 does not actually need the maximiser property (it only evaluates routes at p*),
so this is a citation-label slip (m2), not a gap.
What is wrong: the proof's key sentence "their localised forms only change the multiplicity factor" is false in general —
R4L itself changes the fixed data, and so does the equally natural route **R2L**: fix m′ (3^z), then P := g′w₁ satisfies
m′P ≡ (e₀ + 1)/T (mod T^{n−1}) (E + 1 = T m′g′w₁, E ≡ e₀ mod T^n), so P (monic, degree y + a − 1) has ≤ 3^{max(0, y+a−n)}
choices; (m′, P) fixes E, and g′ | P is a divisor choice, q^{o(s)} by SS Lemma 4.1. Hence
  N_V(p*) ≤ 3^{s/5 + max(0, 2s/5 − n) + o(s)},
which is **< 3^{2s/5 − O(1)} as soon as n > 2s/5 + o(s)** (i.e. in the sibling regime n ≈ N(s) − 1 ≈ s/2). So the displayed
claim "every route-type bound for N_V(p*), localised or not, is ≥ 3^{2s/5 − O(1)}" is false for a natural localised route.
The *mass* conclusion survives for R2L: its relative-mass exponent is z + max(0, y + a − n) + n − s/2 ≥ s/10 > 0 for every n
(it is effectively a count of E in V), and the same holds for the analogous "fix one of (m′, g′, w₁), the product of the other
two in its class" routes and for counting E directly (3^{deg E − n}). So the window statement is plausibly true for a much wider
class, but the proposition as written proves it only for an explicit finite list, and its central inequality is false beyond it.
Severity MAJOR (the report's SHARP 2 headline "counts do not localise … every route-type bound" and the PROVED label in §6).
Repair (D1): restate Prop 3.1 as: "For each route of SP Lemma 1.6 (all rows), its modulus-localisations, R4L and R2L
(and the variants obtained by fixing one or two of m′, g′, w₁ and constraining the rest mod T^{n−1}), the bound on the relative
mass N_V(p*)·3^{n−N(s)} at p* is ≥ 3^{min(n − s/10, s/10) − o(s)}; hence < 1 only if s > (10 + o(1))n." Label PROVED for that
explicit list; "every route-type count / counts do not localise / Lemma 3.1 must be fed by positional information" → Assessment.
Replace "localised forms only change the multiplicity factor" by the R2L/R4L case analysis. (D2, MINOR) Cite SS Cor 4.2 only for
the PROVED upper bound; drop "unique maximiser" or label it EVIDENCE.
*Explicit form (Assessment).* Per-level terms of SS §5.3 confirmed (26.3, 9.15, 2.43, 0.60, 0.15, 0.039 at s = 40..90); they are
union-bound terms over both slices without the parity filter, so using them for one cylinder is conservative. Decay 3^{−0.127 s}
per level ⇒ tail ≈ 7.7·term(s₁); tail < 3^{2−n} gives s₁ ≈ 65 + 8n, not 80 + 9n (depth ≈ 33 + 4n rather than 40 + 4.5n; with
OA's parity factor ≈ 4 another ≈ 10 levels lower). Order of magnitude unaffected (m3).
