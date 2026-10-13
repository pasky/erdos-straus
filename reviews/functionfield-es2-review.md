# R166 — hostile review of FUNCTIONFIELD_ES2.md (O166, branch side-agent/ff-extinction)

Reviewer: R166. Reviewed commit: merge of side-agent/ff-extinction as of review start.
From-scratch scripts: `scripts/review_ff2_*.py` (own F_q[T] arithmetic, no author code imported).

## Summary verdicts (filled in claim by claim)

| Claim | Verdict |
|---|---|
| §0.1 compactness criterion | (pending) |
| §0.1 tree plateau "partly an artefact" | (pending) |
| §0.2 Case A impossibility at x*_c | (pending) |
| §0.2 Case B normal form + searches | (pending) |
| Conjecture 0.2 labels | (pending) |
| Prop 1.1 | (pending) |
| Prop 3.1 | (pending) |
| Novelty / labels | (pending) |

## Defects

(numbered below as found)

### Claim §0.2 Case A impossibility at x*_c (odd q, A = T^k, k ≥ 2) — SOUND-AFTER-REPAIRS

Conclusion is TRUE (re-proved below), but the written sketch is not a proof and one intermediate assertion is
false as stated.

**D1 (MINOR→MAJOR for the label).** §0.2 "comparing EF = a1 + b1 with E ≡ −(1 + cT) (mod T^{α+2}) forces
b1 = 1, L' = a1' = 1, E = −(1 + cT)". False before the leading-coefficient condition is used: for α = 1 every
a1' ≡ c (mod T^{k+j−1}) gives a congruence-valid divisor E = −(T a1' + 1) = −(a1 + b1). Counterexample found by
`scripts/review_ff2_caseA.py 3 2 1,1 3`: q = 3, k = 2, c = 1, a0 = 1, b0 = T³ + T (L' = T² + 1 ≠ 1),
E = −(T³ + T + 1); it is killed only by lc(E) = −1 ≠ 1 = lc(s). Also "(−c)^α = −1" is not what the algebra
gives (see below: μ = (−c)^α and lc forces μ = c). The label "PROVED, sketch to be written out" is therefore
premature. Repair: replace by the proof below (R166 has checked every step), or relabel "CLAIM (sketch)".

*Repair proof (R166).* Setting: x ≡ u = 1 + cT (mod T^∞), x ≡ 1 at every prime ≠ T, q odd, k ≥ 2.
Validity forces T^{k+j} | u + E and L' | 1 + E, hence T ∤ E, x ≡ 1 (mod E), and in Case A E | a1 + b1
(a0 = g a1, b0 = g b1, gcd(E, L) = 1). Let s be the family sum: in Case A lc(s) = lc(a1 + b1) when the two
terms have equal type, else 1.
(1) E + 1 ≡ −cT (mod T^{k+j}), k + j ≥ 2, so E + 1 = T·L'·H with T ∤ H ≠ 0, hence deg E ≥ 1 + deg L'
= 1 + deg g' + deg a1' + deg b1'. With deg a1 ≥ deg b1 (WLOG) and deg E ≤ deg(a1 + b1) ≤ deg a1 = α + deg a1'
(T^α ∥ a1): α ≥ 1 + deg g' + deg b1' ≥ 1, so T ∤ b1 and v_T(L) = j = γ + α, k + j ≥ α + 2.
(2) F := (a1 + b1)/E has deg F ≤ α − 1 − deg b1 − deg g'. Mod T^α: −(1 + cT)F ≡ b1. Thus (1 + cT)F + b1 is
≡ 0 (mod T^α) and of degree ≤ max(α − deg b1, deg b1) ≤ α, so (1 + cT)F + b1 = μT^α, μ ∈ F_q, and μ = 0 if
deg b1 ≥ 1.
(3) a1 = EF − b1 = F(E + 1 + cT) − μT^α with T^{α+2} | E + 1 + cT, so a1' ≡ −μ (mod T²); T ∤ a1' gives μ ≠ 0,
hence b1 = 1 and (1 + cT) | μT^α − 1, i.e. μ = (−c)^α, F = (μT^α − 1)/(1 + cT), deg F = α − 1, lc F = μ/c.
(4) deg a1 ≥ 1 > deg b1, so lc(s) = 1 in all Case A type combinations; lc(E) = lc(s) = 1, and lc(E)lc(F) = lc(a1)
= 1 gives μ = c. Degrees: deg E = deg a1 − deg F = 1 + deg a1', so (1) forces g' = 1, deg H = 0, E = T a1' − 1.
(5) a1 = EF − 1 gives a1'(T^α − TF) = −(F + 1). Multiplying by (1 + cT) and using μ = c:
(1 + cT)(T^α − TF) = T(T^{α−1} + 1) and (1 + cT)(F + 1) = cT(T^{α−1} + 1). Hence a1' = −c, so c = −1 (a1' monic),
and then μ = (−c)^α = 1 ≠ −1 = c (q odd). Contradiction. ∎
Independent EVIDENCE (`scripts/review_ff2_caseA.py`, all monic a0, b0 of degree ≤ 4 (q = 3) / ≤ 3 (q = 5) / ≤ 2
(q = 7), all divisors E with every leading coefficient): congruence-valid Case A divisors exist (10, 4, 4, 5, 1, 1,
0 for the runs in `data/review_ff2_caseA_log.txt`), but **none** with admissible lc; sanity: u = 2 + T (q = 3)
yields admissible hits (e.g. a0 = T, b0 = T + 1, E = 2T + 1 with lc(a0 + b0) = 2).
