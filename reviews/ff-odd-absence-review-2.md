# Hostile review #2 of FF_ODD_ABSENCE.md (O226) — R241, round 1

Reviewer: R241 (independent; no edits to the author's files in round 1). Scope: Lemma 1.1, Thm 1.2, Cor 1.3, Thm 1.4,
Cor 1.5, Prop 1.6, Cor 1.7, Lemma 2.1, Thm 2.2 (certificate), consistency with (J)56 Thm 8.1.
From-scratch scripts: `scripts/review_r241_*.py`.

## Summary verdicts
| Claim | Verdict |
|---|---|
| Lemma 1.1 (root-product identity) | SOUND (re-derived line by line, §1) |
| Thm 1.2 (Case B law) + Cor 1.3 | SOUND (§1; brute-force EVIDENCE reproduced from scratch) |
| Thm 1.4 (Case A law) | SOUND, modulo the inherited input lc K = lc E ∈ F₃^* ((J)56 Lemma 7.2) (§2) |
| Cor 1.5 (vanishing law) | SOUND (§2) |
| (further claims) | (in progress) |

## §1. Lemma 1.1, Theorem 1.2, Corollary 1.3

**Re-derivation of Lemma 1.1 (independent).** Over an algebraic closure write V = λ∏(T − β_i), W = μ_W∏(T − γ_j). At a root β of V:
C(β) = −W(β) (from W + C = GV; G is never used otherwise, so G = 0 is harmless) and M(β)W(β)C(β) = β^s, so
−M(β)W(β)² = β^s; multiplying, (−1)^t P_M P_W² = (∏β_i)^s = (−1)^{ts}V(0)^s λ^{−s}, with P_X := ∏_i X(β_i). At a root γ of W,
V(γ) = −γ^s, so ∏_{i}(γ_j − β_i) = V(γ_j)/λ gives P_W = μ_W^t(−1)^{ta}λ^{−a}∏_j V(γ_j) = μ_W^{t−s}(−1)^{ta+a+as}λ^{−a}W(0)^s,
and likewise P_M = μ_M^{t−s}(−1)^{tz+z+zs}λ^{−z}M(0)^s (the identity at roots of M is the same, MWC = 0 there). Substituting,
using V(0) = M(0)W(0)C(0) and M(0) ≠ 0:
  (W(0)/C(0))^s = (−1)^{t+tz+z+zs+ts} λ^{z+2a−s} μ_M^{s−t} μ_W^{2(s−t)}  —  exactly the stated formula.
No hypothesis on lc C, on deg(MWC) or on G is used; repeated roots are fine (products with multiplicity); t = 0 / z = 0 / a = 0
give empty products and the formula still holds. **SOUND.**

**Theorem 1.2.** Lemma 1.1 with M = m', W = w, V = v, μ = 1; λ = lc v = lc(w + C)/lc g' = lc(w + C) ∈ {1 (a ≠ b), 2 (a = b)}
(q odd, no cancellation). The λ-exponent z + 2a − s equals a − b because z + a + b = s ((J)56 Lemma 7.1(i); re-checked by
brute force below: no tuple with deg(m'wC) ∈ {s + 1} at the tested sizes, and the enumerator below never finds a tuple outside
z + a + b = s). Hence ε = (−1)^{t+tz+z(1+s)+ts} for every odd q (the R-O226 repair is correct). E(0) = w(0)/C(0) follows from
Ev = T^s + m'w² at 0 (v(0) = m'(0)w(0)C(0)); E(0) ≠ −1 because w(0) + C(0) = g'(0)v(0) ≠ 0. **SOUND.**

**Cor 1.3.** gcd(2s, q − 1) = 2 ⟺ gcd(s, (q−1)/2) = 1; instances q = 9, 27, 81, 243 re-checked arithmetically. For q = 9:
odd s: E(0)^s = ±1 with E(0) ∈ μ_8 forces E(0) = ±1; s ≡ 2 (4): E(0)² ∈ μ_4 to an odd power, so E(0) = ±i (and E(0) = 1 is
on u₀ = −1 ∈ F₃^*), sign (±i)^s = −1 = ε; s ≡ 0 (8): E(0)^s = 1 = ε. **SOUND.**

**From-scratch verification (EVIDENCE; R241 code, no author code).**
* `scripts/review_r241_enum.py` (python-flint factorisation over F_q; five complete routes V[t], (m',w), (m',C), (w,g'), (C,g'),
  each candidate re-verified against the full definition (B^{k=1}); ORDERED tuples, both orientations).
* `scripts/review_r241_brute.py` (naive: all monic T-free (m', w, C) with deg sum ≤ s + 1, v := m'wC − T^s). Agreement of the full
  (pattern, E(0)) histograms: q = 9 (s ≤ 4), 5 (s ≤ 6), 7 (s ≤ 5), 27 (s ≤ 3): **exact match**, and 0 tuples with deg(m'wC) = s + 1.
  (A first version of my brute force forgot T ∤ g' and found E(0) = −1 tuples — confirming that the T ∤ g' condition is what
  excludes E(0) = −1.)
* Law check (both the unsimplified Lemma 1.1 form and the simplified ε form) on every tuple: q = 9, s ≤ 12 (15 701 ordered
  tuples), q = 5, s ≤ 14 (4 224), q = 7, s ≤ 12 (2 835), q = 25, s ≤ 6 (1 644), q = 27, s ≤ 9 (625): **0 failures**.
* The author's counts are reproduced exactly: oriented (a ≤ b), 2 ≤ s: q = 9, s ≤ 12: 8 915; q = 27, s ≤ 9: 340
  (the author's 305/645 for q = 5/7 also match my 307/647 minus the two s = 1 tuples with a ≤ b).
* q = 9 E(0)-distribution (my run): odd s only E(0) = 1; s ≡ 2 (4) only {1, ±i}; s ≡ 0 (4) all classes except −1;
  q = 27, s ≤ 9: only E(0) = 1. As claimed.

## §2. Theorem 1.4 and Corollary 1.5

**Re-derivation.** From E + 1 = a1'b1K and EF = T^αa1' + b1: mod a1', E ≡ −1 so −F ≡ b1, i.e. a1' ∣ F + b1 (z polynomial);
b1KF = (E+1)F/a1' = (T^αa1' + b1 + F)/a1' = T^α + z (A3, checked symbolically and on every enumerated datum by assertion). So
(M, W, C, G, V, s) = (K, b1, F, a1', z, α) satisfies (R), V(0) = z(0) = b1(0)K(0)F(0) ≠ 0 since E(0)F(0) = b1(0) ≠ 0. Lemma 1.1
gives the stated formula with μ_M = lc K, μ_W = 1. lc F = lc(T^αa1' + b1)/lc E ∈ F₃^* when lc E ∈ F₃^*; λ = lc(F + b1) is in
F₃^* unless deg F = β and lc F = −1, in which case κ + 2β − α = β − f = 0. Correct. **Dependency:** lc K = lc E ∈ {1, 2} is an input
from (J)56 Lemma 7.2 / DEPTH_ASPECT Lemma 2.4 (not re-proved here; for general q the right side need not be in F₃^*). In addition
β + κ ≤ α always (deg E ≤ deg(T^αa1' + b1), and β > α + deg a1' forces a1' = 1, K const and −1/c = T^α: impossible) — this
justifies my enumeration route below. **SOUND.**

**From-scratch check** (`scripts/review_r241_caseA.py`: all (b1, K), β + κ ≤ α, lc K ∈ {1, 2}; E | T^α + b1²K, which I derived:
E(Fb1K − T^α) = T^α + b1²K; a1' = (E+1)/(b1K)): q = 9, α ≤ 5 (505 data): unsimplified formula and E(0)^{2α} = 1 hold for every
datum, 0 failures. The off-F₃ counts per pattern at α ≤ 4 equal `data/zc/caseA9_4.txt` exactly (α = 2: 18, α = 4: 268); the
P₈ part at α = 4 is only 174 (the author's use of 268 is a valid over-count).

**Cor 1.5.** ord(−u₀) ∣ 2n is a restatement; q = 27: −u₀ ∉ {±1} has order 13 or 26 ⇒ 13 ∣ n; q = 9: ord 4 (±i) ⇒ 2 ∣ n, ord 8
(P₈) ⇒ 4 ∣ n. **SOUND.**

## Defects
(in progress)
