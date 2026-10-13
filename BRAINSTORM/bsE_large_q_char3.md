# bsE_large_q_char3 — no finite linear covering of ES_q(T^k) for q = 3^r, r ≥ 27 (O178)

## Idea
The brief asked for a "large-q theorem" for O(3^r, T²). The union bound over all linear families valid on a c-slice has exponents
⌊2(s−3)/5⌋ + 1 − ⌈s/2⌉ ≤ −1 (Case B) and ⌊(α−1)/2⌋ − α ≤ −1 (Case A), with q-independent divisor constants. So for q large the
covered mass is < 1 (DEPTH_ASPECT Thm 2.5).
## Literature
O140 Thm 2.1 (fixed degree, q → ∞: most P fail), O140 Prop 4.1 (char ≥ 5: point 1 obstructed), FUNCTIONFIELD_ES2 §0.1
(compactness). Large-q short-interval divisor theory (Keating–Rodgers–Roditty-Gershon–Rudnick, Math. Z. 2018; Sawin, Duke 2021)
was *not* needed.
## Barrier screen
It obstructs certificates, not ES (the lottery remains). In char ≥ 5 the conclusion was already known; char 3 is new, because
there the class-1 obstruction vanishes (FUNCTIONFIELD_ES §6.1(a)).
## Cheap numerics
`scripts/bsE_largeq.py`: totals 2.6·10⁻² (r = 27), 1.9·10⁻⁷ (r = 28), crude closed form < 1 for all q ≥ 1.3·10^16. Empirical
union-bound masses (Case B, s ≤ 8–11): q = 5: 0.11, q = 7: 0.015, q = 11: 0.03; q = 3: 1.74 (no conclusion).
## Assessment
PROVED (relative to O173 Lemmas 1.1, 2.1, 3.1 and R166 Case A steps), under review. Function-field only.
