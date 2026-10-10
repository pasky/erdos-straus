# POINTWISE_SPECTRAL — "flip the average": fixed p, average over the Type I parameters (task O123)

Labels as in DISCOVERIES.md. ET = Elsholtz–Tao arXiv:1107.1010v6. Type I coordinates (ET Prop 2.2/2.3):
`p = 4acd − f`, `f | 4a²d+1`, `e = (4a²d+1)/f`, `b = (pa+c)/f`; equivalently `pe + 1 = 4abd`, `e | a+b`
(c = (a+b)/e). Type II (ET Prop 2.6/2.7): `p + e = 4abd`, `e | a+b`. Throughout f_I(p), f_II(p) count
solutions (x,y,z) with y ≤ z (each once; normalisation a ≤ b, gcd(a,b,c) = 1).

## 1. Numerics (EVIDENCE)

Script `scripts/spec_typecount.c` (exact counts for all n ≤ N; sieve factorisation of 4a²d+1 in two regimes,
a ≤ √N linear in d, a > √N quadratic in a), validated against brute force (`scripts/spec_brute_validate.py`:
all primes ≤ 400, both types, 0 mismatches). Statistics: `scripts/spec_stats.py`, output
`data/spec/t1e7_stats.txt`.

**Result (p ≤ 10⁷, all 664 578 odd primes):** `f_I(p) ≥ 1` and `f_II(p) ≥ 1` for every p; even the a = 1
sub-family (`p = cef − c − f`, `ef ≡ 1 mod 4`, ET Remark 2.5) is non-empty for every p ≡ 1 (mod 4)
(consistent with the literature check of that sub-family to 10¹⁴ cited by ET Remark 2.5). So **numerically Type I
alone always works**; the question "which p fail Type I" has no answer below 10⁷.

Dyadic windows [X, 2X) (L = log(1.5X)):

| X | min f_I (at p) | mean f_I | mean/L² | min f_I/L | min f_II | min f_I^{a=1} (p≡1 mod 4) |
|---|---|---|---|---|---|---|
| 2¹⁰ | 7 (1201) | 52.2 | 0.97 | 0.95 | 4 | 1 |
| 2¹⁴ | 14 (20521) | 114.9 | 1.12 | 1.38 | 9 | 1 |
| 2¹⁸ | 35 (471241) | 220.8 | 1.33 | 2.72 | 17 | 3 |
| 2²⁰ | 57 (1092961) | 291.5 | 1.43 | 3.99 | 18 | 2 |
| 2²² | 62 (4889641) | 376.2 | 1.54 | 3.96 | 30 | 1 |

* All window minimisers from 2⁹ on are Mordell-hard (p mod 840 ∈ {1,121,169,289,361,529}).
* The minimum tracks the mean: min/mean ≈ 0.16–0.2, stable over 2¹² … 2²². mean f_I ≈ 0.1·L³ (ET: Σ_{p≤N} f_I ≍ N L²).
  So min f_I grows like a power of log p (fit ≈ L^{2.5}·const is indistinguishable from c·L³ here); the
  pointwise count is "polylog with a robust constant fraction of the mean".
* The a = 1 sub-family alone has minimum 1–3 throughout: the full 3-parameter family is needed for growth.

## 2. Exact fixed-p forms of Type I (PROVED, elementary)

Fix a prime p ≥ 5. All variables are positive integers.

**Lemma 2.1 (three equivalent shapes).** For a, c, d, f with p ∤ cd, the following are equivalent:
(i) `p = 4acd − f` and `f | 4a²d + 1`;
(ii) `f | ap + c` and `4ac | p + f` (then `d = (p+f)/(4ac)`);
(iii) `f | p² + 4c²d` and `f ≡ −p (mod 4cd)` (then `a = (p+f)/(4cd)`).
In each case `b := (ap+c)/f`, `e := (4a²d+1)/f`, `g := (p²+4c²d)/f = 4bcd − p` are integers with
`4abd − pe = 1`, `a + b = ce`, and every Type I solution of p arises exactly once with `a ≤ b`, `gcd(a,b,c) = 1`
(ET Prop 2.2).
*Proof.* (i)⇒(ii): `c(4a²d+1) = a(4acd) + c = a(p+f) + c`, so `ap + c ≡ c(4a²d+1) ≡ 0 (mod f)`.
(ii)⇒(i): with `4acd = p + f`, `c(4a²d+1) = a(p+f) + c ≡ ap + c ≡ 0 (mod f)` and `gcd(f, c) | gcd(4acd − p, c) | p`;
if `p | f` and `p | c` then `p | cd`, excluded; so `f | 4a²d+1`. (i)⇔(iii): mod f we have `4acd ≡ p`, hence
`4c²d·(4a²d+1) ≡ p² + 4c²d`; `gcd(f, 4c²d) | p` and is 1 unless `p | cd`. The identities are routine
(`bf = ap + c`, ET (2.8), (2.9)). ∎ Checked: `scripts/spec_reform_check.py` (all primes ≤ 300 reproduce the exact
counts f_I(p) of §1).

**Lemma 2.2 (SL₂ with a fixed entry; Hecke form).** (a) `γ = [[4ad, p],[e, b]] ∈ SL₂(ℤ)`; conversely Type I is
"γ ∈ SL₂(ℤ) with upper-right entry p, 4 | γ₁₁, and a divisor a of γ₁₁/4 with a ≡ −γ₂₂ (mod γ₂₁)".
(b) With `Q₋ = [f, −4ad, de]` (disc −4d) and `Q' = [f, 4cd, dg]` (disc −4dp²):
`Q'(x, y) = Q₋(x + 2bd·y, p·y)`, i.e. `Q' = Q₋ ∘ [[1, 2bd],[0, p]]`; so the disc −4dp² form of a solution is a
**T_p-Hecke translate** of the level-d Heegner form of disc −4d; roots `z_{Q'} = p·z_{Q₋} − 2bd`.
*Proof.* (a) det = 4abd − pe = 1. (b) Expand: middle coefficient `2f·2bd − 4adp = 4d(bf − ap) = 4cd`; last
coefficient `4b²d²f − 8abd²p + dep² = d(4bd(ap+c) − 8abdp + ep²) = d(4bcd − p(4abd − pe)) = d(4bcd − p)`. ∎
(Identity asserted for every solution in `spec_reform_check.py`.)

**Lemma 2.3 (the a = 1 and Type II "hyperbola" forms).** (a) a = 1 Type I solutions of p ↔ `p = tuv − u − v` with
`tv ≡ 1 (mod 4)` ↔ `(tu − 1)(tv − 1) = tp + 1` (t = e, u = c, v = f): divisors X of `tp+1` with `X ≡ −1 (mod t)`
— this is candidate (c) of the brief, and it is only the a = 1 slice. In general (`t = e`): `tp + 1 = X·Y` with
`X = b`, `Y = 4ad`, and a divisor a of Y/4 with `a ≡ −X (mod t)`.
(b) Type II (ET (2.15), (2.21)): with `q = 4cd`, Type II solutions of p ↔ factorisations
`c·q·p + 1 = (aq − 1)(bq − 1)` (a ≤ b, gcd(a,b,c) = 1, p ∤ abd). Same shape as (a) with p ↦ cp.
*Proof.* (a) `p + c = f(ce − 1)` (ET Remark 2.5) and `(tu−1)(tv−1) = t(tuv − u − v) + 1`. (b) expand
`(aq−1)(bq−1) = q(abq − a − b) + 1` and use `4abcd = a + b + cp`. ∎ (Type II form checked against the exact
f_II(p), p ≤ 300, in `spec_reform_check.py`.)

**Lemma 2.4 (genus condition; the step that fails at odd squares).** If (a,c,d,f) is a Type I solution of an odd n
with `gcd(n, 2cd) = 1`, then `χ_{−4d}(−n) = +1`, where `χ_{−4d} = (−4d/·)` (Kronecker).
*Proof.* f is odd and `gcd(f, 2cd) = 1`. Every prime q | f divides `n² + 4c²d`, so `−4c²d ≡ n²` is a non-zero square
mod q, so `(−4d/q) = 1`; hence `χ_{−4d}(f) = 1`. As `f ≡ −n (mod 4cd)` and `χ_{−4d}` has period 4d,
`χ_{−4d}(−n) = χ_{−4d}(f) = 1`. ∎
*Consequences.* (1) For an odd square n = m², `χ_{−4d}(−m²) = χ_{−4d}(−1) = −1` for **every** d (the character of a
negative discriminant is odd), so n = m² has no Type I solution with `gcd(m, 2cd) = 1`; in particular n = p² has
none with p ∤ cd — the Type I half of ET Prop 1.6 in this case (the case p | cd is ET's). **Any fixed-p method
must therefore carry the factor `(1 + χ_{−4d}(−p))/2` in its d-th main term**; an "area" main term that does not
see χ_{−4d}(−p) is false (it would predict solutions for p²).
(2) For p prime only the d with `(−4d/p)·(−1) = +1`, i.e. `(−d/p) = −1` (p inert in ℚ(√−d)) contribute; e.g.
d = 1 contributes iff p ≡ 3 (mod 4). Check: `scripts/spec_genus_check.py` (all 1615 solutions for p ≤ 400: 0
violations; shares by d: d=1 22% (all from p ≡ 3 mod 4), d=2 15%, d=3 8%, …).

## 3. The fixed-p target regions (PROVED geometry; counts are EVIDENCE/Assessment)

Two "Heegner" formulations; both are exact (point in region ⇔ Type I quadruple).

**Prop 3.1 (Formulation A: level-d points of disc −4d, wedge at the cusp 1/(2c)).** Let
`Λ_d = {z = (2ad + i√d)/f : a, f ≥ 1, f | 4a²d+1}` (roots of `[f, −4ad, de]`, the family 𝓕_d of TYPEI_LOGLOG §2).
For z ∈ Λ_d and c ≥ 1, `(2c√d·x − √d − p·y)/y = 4acd − f − p ∈ ℤ`. Hence
`(a,c,d,f)` is a Type I quadruple of p ⇔ `z ∈ R_c := {x+iy : |2c√d x − √d − p y| < y}`.
R_c is the wedge at the boundary point `1/(2c)` between the Euclidean lines of slopes `2c√d/(p±1)`; its horizontal
width at height y is `y/(c√d)`, so
`area_hyp(R_c ∩ {y₁ ≤ y ≤ y₂}) = log(y₂/y₁)/(c√d)`; with the size window `f ∈ [1, 2p]` (y ∈ [√d/2p, √d]):
**area(R_c) = log(2p)/(c√d).**
Shape: both edges are hypercycles of the geodesic `x = 1/(2c)` at distances `arcsinh((p±1)/(2c√d))`, so R_c is a
**tube of hyperbolic width 2/p + O(c√d/p²)** around a hypercycle arc of length `≈ p·log(2p)/(2c√d)`.
*Proof.* For z ∈ Λ_d: `x/y = 2a√d`, `√d/y = f`; substitute. An integer of absolute value < 1 is 0. The width and
area are direct integrations (`dx dy/y²`); the hypercycle distance of the ray at angle θ is `arcsinh(cot θ)`. ∎

**Prop 3.2 (Formulation B: disc −4dp² points = T_p-translates, wedge at the cusp −1/(2a)).** Let
`Λ'_{d,p} = {z' = (−2cd + ip√d)/f : c, f ≥ 1, f | p² + 4c²d}` (roots of `Q' = [f, 4cd, dg]`, disc −4dp²; by
Lemma 2.2(b) these are T_p-images of disc −4d points). For z' ∈ Λ'_{d,p} and a ≥ 1,
`(p/y')·(−2a√d x' − √d − y') = 4acd − f − p ∈ ℤ`, so Type I ⇔ `z' ∈ R'_a := {|2a√d x' + √d + y'| < y'/p}`, the wedge at
`−1/(2a)` between lines of slopes `−2a√d/(1 ± 1/p)` (moderate angle). Width at height y' is `y'/(a√d p)`, and for
`y' ∈ [√d/2, p√d]` (f ∈ [1, 2p]): **area(R'_a) = log(2p)/(a√d·p)**; shape: a tube of hyperbolic width ≍ 1/p around a
hypercycle arc of length ≍ log p that runs from the cusp −1/(2a) up to height `√|D'|/2 = p√d` (the top of the
Heegner set of D' = 4dp²). ∎ (Same computation.)

**Expected counts (Assessment + EVIDENCE).** The point density of Λ_d is `ρ̄_d/(2√d)` per unit hyperbolic area
(ρ̄_d = mean number of a mod f with 4a²d ≡ −1 (f)), and Λ'_{d,p} is p(1+O(1/p)) times denser. Both formulations give
the same per-target expectation, which must carry the genus factor of Lemma 2.4:
`λ_{c,d}(p) ≈ κ_d·(1 + χ_{−4d}(−p))·log p/(c d)` (Formulation A; for B read a for c).
EVIDENCE (`scripts/spec_target_mean.py`, primes in [10⁶, 10⁶+2·10⁴], `data/spec/target_mean_1e6.txt`): among genus-
allowed p, `mean·cd/L` is ≈ constant in c for each d (d=3: 0.52, 0.51, 0.53, 0.70 for c=1,2,3,5; d=6: 0.74, 0.80,
0.76, 0.68), while the **fraction of empty targets is 13–89 %** (e.g. d=10, c=5: λ ≈ 0.13, empty 89 %; d=3, c=1:
λ ≈ 2.4, still empty 17 %). Summing, `Σ_{c,d} λ_{c,d} ≈ mean f_I ≈ 0.1 L³` (§1).

**Consequence (the decisive numbers).** In Formulation B the number of points is `h(−4dp²) ≍ p√d·L(1,χ_{−4d})`, so the
relative measure of one target is
`μ_{a,d} = λ_{a,d}/h(−4dp²) ≍ L/(a d^{3/2} p) = (Planck scale |D'|^{−1/2}) × O(L/(a d))`,
and its minimal width is `≍ 1/p ≍ |D'|^{−1/2}`. In Formulation A, D = 4d is tiny (only d ≲ L² have λ ≳ 1/L), the
target is a 2/p-tube along a hypercycle of length ≍ pL, and the large parameter enters only through the shape.
