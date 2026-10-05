# Hostile review R40 of EXCEPTIONAL_SPW.md (branch side-agent/spw-proof, O40)

Reviewer branch: side-agent/review-spw. Reviewed commit: 5bc4f0d (merged).
Scripts (from scratch, no reuse of the author's code): `scripts/review_spw_*.py`.

## Verdict summary (filled in claim by claim)

| claim | verdict |
|---|---|
| Definition match with IF2 §9 | (pending) |
| Thm 3.2 | (pending) |
| exact certificates N=300 / N=1150 | (pending) |
| Cor 3.3 | (pending) |
| Lemma 1.4 | (pending) |
| Lemma 1.1, 1.2, 1.3 | (pending) |
| §2: Lemma 2.1, 2.2, Prop 2.3, exact A(N) values | (pending) |

## Per-claim notes

### Definition match (SPW vs IF2 §9)
IF2 §9 (lines 422–428): (P1) exact profile mod every d ≤ N/2; (P2) R(s) ≤ 1 − σ
for every class of modulus d > CN; (P3) |R(s) − c(s)| ≤ Δ₀ for N/2 < d ≤ CN;
R ≥ 0 summable on ℤ. EXCEPTIONAL_SPW.md uses D = ⌊N/2⌋ (same set of d), the
same strict inequality d > CN and the same normalisation 1 − σ. Thm 3.2 and
Lemma 3.1 use only (P1)–(P2), so they refute a *weaker* hypothesis than SPW —
a fortiori SPW. **MATCH.**

### Theorem 3.2 — re-derived line by line
1. *Projection.* ρ(x) = Σ_{y≡x (e)} R(y) ≥ 0. Points of ℤ/e are classes of
   modulus e > CN, so ρ ≤ 1 − σ by (P2). For d | e, class sums of ρ mod d are
   R(b mod d) = c(b,d), which are the class sums of 1_W (W = {1..N} ⊂ ℤ/e,
   e > N). ✔
2. *Pinning.* Class sums mod d | e determine ρ̂(k) exactly for (e/d) | k;
   ∃ d | e, d ≤ D, with (e/d) | k ⟺ gcd(k,e) ≥ e/D (take e/d = gcd(k,e)).
   I verified the converse too (the profile span contains *no other*
   character) numerically on 7 (e, D) pairs by SVD rank
   (`review_spw_basic.py` (b)). For m₀ ≤ |k| ≤ M, |k| | L_M | e so
   gcd(k,e) = |k| ≥ m₀ = e/D. ✔ (M < e/2, so representatives are unique.)
3. *m₀ bound.* e < CN + L_M ≤ (C+1)N, m₀ = e/D ≤ (C+1)(2D+1)/D ≤ 2C+3 once
   D ≥ C+1. ✔
4. *Fejér.* K = (1/(e(M+1)))·(sin(π(M+1)x/e)/sin(πx/e))² ≥ 0, ΣK = 1,
   K(x) ≤ e/(4(M+1)x²) from sin(πx/e) ≥ 2|x|/e on |x| ≤ e/2; two-sided tail
   ≤ 2·e/(4(M+1))·Σ_{t≥a}t^{−2} ≤ e/(2(M+1)(a−1)). All checked numerically
   for 4 (e, M) pairs, every x and every a (`review_spw_basic.py` (c)). ✔
5. *Degree.* T̂ = K̂·f̂ vanishes for |k| > M (Fejér) and for m₀ ≤ |k| ≤ M
   (pinning), so T is the sample of a real trig polynomial of degree
   n ≤ ⌈m₀⌉ − 1 < m₀ (real because f real, K even). ✔
6. *Sup bound.* K∗ρ ∈ [0, 1−σ], φ ∈ [0,1] ⇒ T ∈ [−1, 1−σ] on samples. With
   period-1 variable θ, ‖T′‖ ≤ 2πn‖T‖; nearest sample within 1/(2e) ⇒
   ‖T‖ ≤ 1/(1 − πn/e) ≤ 1/(1 − πm₀/e). ✔
7. *Edge tails.* The set {x_in − y : y ∉ W} is the arc [r+1, e−N+r] of ℤ/e,
   i.e. one-sided runs starting at distance r+1 and N−r ≥ r+2; the set
   {x_out − y : y ∈ W} is the arc [−r−N, −r−1], i.e. runs starting at r+1
   and e−N−r > (C−1)N − r ≥ r+1 (needs 2r+1 < (C−1)N, which is the stated
   range). Each side is a *one-sided* tail ≤ e/(4(M+1)r); the author's
   two-sided bound e/(2(M+1)r) is valid (slightly wasteful). ✔
8. *Jump + Bernstein.* T(x_in) ≤ −σ + ε, T(x_out) ≥ −ε, ε = e/(2(M+1)r);
   |θ_out − θ_in| = (2r+1)/e. Gives σ ≤ e/((M+1)r) + 2πm₀(2r+1)/(e − πm₀). ✔
9. *Optimisation.* a/r + b r with a = e/(M+1), b = 4πm₀/e: at
   r = √(a/b) = e/√(4πm₀(M+1)) each term is √(ab) = 2√(πm₀/(M+1)); total
   4√(πm₀/(M+1)) plus O(m₀/e) and rounding. r ≍ N/√M = o(N), admissible for
   fixed C > 1 once √M ≫ (C+1)/(C−1). ✔
10. *M ≍ log N.* L_M = e^{ψ(M)}, ψ(M) ~ M, so the largest M with L_M ≤ N is
   ~ log N. Hence σ ≤ (4√(π(2C+3)) + o(1))·(log N)^{−1/2}. ✔

**Verdict Thm 3.2: SOUND.** Uniformity: the constant is explicit in C
(≍ √C), N₀ depends on C through the admissibility √M ≫ (C+1)/(C−1) and
D ≥ C+1 only. No circularity; no use of (P3). The theorem is correctly
labelled PROVED. (Minor presentation points: D6, D7 below.)

### Exact local certificates (
s3)
Rebuilt from scratch (`scripts/review_spw_cert.py`): my own dual LP on \u2124/e
(variables a_{d,b} on classes mod d | e, d \u2264 D, and z \u2265 0 on classes mod
e\u2032 | e, e\u2032 > CN, \u03a3z = 1, z-cover \u2265 g pointwise, maximise \u03a3_{n\u2264N} g(n)),
solved with HiGHS, coefficients rounded to rationals, then **the bound
1 \u2212 \u03a3_W g / \u03a3 z recomputed in exact `Fraction` arithmetic** with the cover
re-derived exactly (for e = 630, 2310 the only divisor > CN is e itself, so the
optimal cover is z = g\u207a). Logic re-checked: for any R with (P1)\u2013(P2),
\u03a3_{n\u2264N} g(n) = \u2211 a_{d,b} c(b,d) = \u27e8g,R\u27e9 \u2264 \u27e8g\u207a,\u03c1\u27e9 \u2264 (1\u2212\u03c3)\u03a3g\u207a. \u2714

| N | e | my LP | my exact certificate | author |
|---|---|---|---|---|
| 300 | 630 | 0.389189 | **\u03c3 \u2264 72/185** (identical rational) | 72/185 |
| 1150 | 2310 | 0.381132 | \u03c3 \u2264 0.381132545 (rounded up; 3843-digit denominator) | 0.3811324\u2026 \u2264 0.381133 |

**Verdict: SOUND** (both reproduced independently; my N = 1150 rational differs
from the author's in the 8th digit only because of a different rounding of the
dual \u2014 both are valid upper bounds, and both lie below 0.381133). The LP
values at N = 3300, 4400, 9100 are labelled EVIDENCE and were not re-run.

## Defects
