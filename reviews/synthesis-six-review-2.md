# Hostile review #2 of O238 Synthesis VI (SYNTHESIS_SPARKS6.md + BRAINSTORM/s6_*.md) — R246, round 1

Reviewer: R246 (independent; no author files edited). From-scratch scripts: `scripts/review_r246_*.py`.

## Summary verdicts
(filled in progressively)

## Thm 1.1 (ES for every 4^s + 105) — checks

### C1. Certificate, from-scratch checker (`scripts/review_r246_cert105.py`, no s6_/z8/ec_cover imports)
Reads only `data/s6_cert105_et.json`. Results (all assertions pass, 1.5 s):
* all 13 classes: 4xyz = n(xy+yz+zx) as a polynomial identity in n (sympy expand);
* integer-valued on n = r + Mt: each of x, y, z expanded in t is integral at deg+2 consecutive t (⟹ integer-valued on ℤ);
* positivity: every coefficient (in n) of every x, y, z is ≥ 0 and not all zero ⟹ positive for all n > 0 (so no
  "n ≥ 4⁴" restriction is needed);
* all M odd; ord_M(4) ∈ {5, 6, 9, 10, 15, 20, 30} all divide 360 (lcm = 180), so n_s mod M depends only on s mod 180
  for EVERY s ≥ 0 — the "(for s ≥ 64)" in Thm 1.1(a) is unnecessary (harmless);
* uncovered s mod 360 = exactly {34, 124, 214, 304} = {s ≡ 34 (mod 90)};
* exponential class: identity (sympy simplify), 4x − n = 151, 2(32u+33)(u²−u+1) = 151A, A integer-valued on 32 + 151ℤ,
  A > 0 for u ≥ 1; ord₁₅₁(4) = 15, 4¹⁰ ≡ 32 (mod 151), and for s ≡ 34 (mod 45): 3 | s − 4, (s−4)/3 ≡ 10 (mod 15);
* exact solutions built and checked for every 0 ≤ s ≤ 2000 (22 of them via the exponential class).
