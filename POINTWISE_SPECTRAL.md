# POINTWISE_SPECTRAL — "flip the average": fixed p, average over the Type I parameters (task O123)

Labels as in DISCOVERIES.md. ET = Elsholtz–Tao arXiv:1107.1010v6. Type I coordinates (ET Prop 2.2/2.3):
`p = 4acd − f`, `f | 4a²d+1`, `e = (4a²d+1)/f`, `b = (pa+c)/f`; equivalently `pe + 1 = 4abd`, `e | a+b`
(c = (a+b)/e). Type II (ET Prop 2.6/2.7): `p + e = 4abd`, `e | a+b`. Throughout f_I(p), f_II(p) count
solutions (x,y,z) with y ≤ z (each once; normalisation a ≤ b, gcd(a,b,c) = 1).

## 0. Summary

* **Numerics (§1, EVIDENCE).** For every prime p ≤ 10⁸, f_I(p) ≥ 1 and f_II(p) ≥ 1; even the a = 1 slice of
  Type I never fails. The window minimum of f_I grows (62 at X = 2²², 105 at 2²⁵) and stays ≈ 0.16–0.2 × the mean ≈ 0.1 L³.
  So "Type I alone fails for infinitely many p" has no numerical support; Type I ∪ Type II is never needed.
* **Exact fixed-p forms (§2, PROVED).** Type I ⇔ `f | p² + 4c²d`, `f ≡ −p (mod 4cd)` (Lemma 2.1). The disc −4dp²
  form of a solution is the T_p-Hecke translate `Q₋∘[[1,2bd],[0,p]]` of the level-d Heegner form (Lemma 2.2). The
  genus condition `χ_{−4d}(−p) = +1` (Lemma 2.4) is the step that fails at every odd square (ET Prop 1.6).
* **Targets (§3, PROVED geometry).** Formulation A: points of disc −4d in a wedge at the cusp 1/(2c), of hyperbolic
  area `log(2p)/(c√d)`. It is a tube of width 2/p around a hypercycle of length ≈ pL/(c√d). Formulation B: disc
  −4dp² (T_p-translated) points in a tube of width ≍ 1/p and area `log(2p)/(a√d p)`. In both, the expected count per
  target is ≈ κ_d(1+χ_{−4d}(−p))L/(cd), and 13–89 % of the single targets are empty in the data.
* **Gap (§4, Assessment).** In the best family the relative target measure is ≈ L²·|D'|^{−1/2} and the width is
  |D'|^{−1/2}, i.e. Planck scale up to a polylog. That is p^{5/6} beyond Young unconditionally and p^{1/2} under
  Lindelöf (in area), p^{8/9} beyond Young's cusp-strip existence theorem (in width). Even Ramanujan + Lindelöf
  Hecke-orbit bounds miss by ≈ p.
* **Step (5) (§5).** Thm 5.1 (PROVED rel. (D)32b): f_I(p) ≤ ψL³ outside a proportion O(1/ψ) of primes. Prop 5.3
  (CONDITIONAL on H): single targets with expectation ≍ L are empty infinitely often. Prop 5.4 (PROVED): thickening
  the target to width K/p is exactly averaging f_I over |n − p| ≤ K, so spectral scale V gives only averages over
  intervals of length p/V. **Verdict (Assessment): no standard hypothesis (GRH, GLH/Lindelöf in any aspect,
  Ramanujan, Selberg, twisted Linnik) suffices by this route.** The sufficient statement is a Planck-scale,
  polylog-accuracy, genus-aware aggregate, i.e. Type I for large p restated. Negative result; ES not proved.

## 1. Numerics (EVIDENCE)

Script `scripts/spec_typecount.c` (exact counts for all n ≤ N; sieve factorisation of 4a²d+1 in two regimes,
a ≤ √N linear in d, a > √N quadratic in a), validated against brute force (`scripts/spec_brute_validate.py`:
all primes ≤ 400, both types, 0 mismatches). Statistics: `scripts/spec_stats.py`, output
`data/spec/t1e7_stats.txt`.

**Extension to 10⁸ (`data/spec/t1e8_stats.txt`; the 10⁸ arrays agree exactly with the 10⁷ run on n ≤ 10⁷):** all
5 761 454 odd primes p ≤ 10⁸ have f_I(p) ≥ 1, f_II(p) ≥ 1 and a non-empty a = 1 slice.

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
| 2²⁴ | 98 (20322481) | 474.4 | 1.63 | 5.75 | 37 | 3 |
| 2²⁵ | 105 (37117609) | 529.8 | 1.69 | 5.92 | 44 | 5 |

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

**The sufficient statement (S) (exact; Formulation B).** Let `φ_a ≥ 0` be smooth with `φ_a = 1` on
`{|k'| ≤ 1/2}` and `supp φ_a ⊂ {|k'| < 1}`, where `k'(z') := (p/y')(−2a√d x' − √d − y')` (so `k' = 4acd − f − p ∈ ℤ` on
Λ'_{d,p}), cut off to `y' ∈ [√d/2, p√d]`. Then `Σ_{d} Σ_a Σ_{z' ∈ Λ'_{d,p}} φ_a(z') > 0 ⇒ f_I(p) > 0`, since φ_a(z') > 0
forces k' = 0. Data of (S) for one (a, d): number of points ≍ h(−4dp²) ≍ p√d L(1, χ_{−4d}); `‖φ_a‖₁ ≍ L/(a√d p)`,
`‖φ_a‖₂ ≍ ‖φ_a‖₁^{1/2}`, and `‖Δ^k φ_a‖₂ ≍ p^{2k}‖φ_a‖₂` (derivative scale V ≍ p across the tube, O(1) along it);
main term `λ_{a,d} ≍ L/(ad)` per (a, d), `≍ L²/d` per d after summing a ≤ p. (S) needs, for the aggregate,
error < main ≍ L³ — no power saving is needed, but the error must be polylogarithmic (§5).

**Consequence (the decisive numbers).** In Formulation B the number of points is `h(−4dp²) ≍ p√d·L(1,χ_{−4d})`, so the
relative measure of one target is
`μ_{a,d} = λ_{a,d}/h(−4dp²) ≍ L/(a d^{3/2} p) = (Planck scale |D'|^{−1/2}) × O(L/(a d))`,
and its minimal width is `≍ 1/p ≍ |D'|^{−1/2}`. In Formulation A, D = 4d is tiny (only d ≲ L² have λ ≳ 1/L), the
target is a 2/p-tube along a hypercycle of length ≍ pL, and the large parameter enters only through the shape.

## 4. The cleanest family, and the gap to what is known (Assessment unless stated)

**Which family.** Of the brief's candidates:
* (b) is realised exactly by **Formulation B**: for fixed p and d, the Type I solutions are points of the
  **T_p-Hecke orbit of the level-d Heegner points of discriminant −4d** (Lemma 2.2(b) exhibits each solution point
  as such a translate) (equivalently Heegner points of discriminant
  `D' = −4dp²`, conductor p) lying in the tubes R'_a (Prop 3.2, Lemma 2.2(b)); the genus factor `1 + χ_{−4d}(−p)`
  (Lemma 2.4) is the only arithmetic of p visible in the main term. Discriminants −p, −4p, −16p themselves do not
  occur; p enters as the Hecke index.
* (a) Kuznetsov with p as frequency: by Lemma 2.2(a) the relevant matrices have `γ₁₂ = p`, i.e. points (A, D) of the
  modular hyperbola `AD ≡ 1 (mod p)`; the box counts are controlled by Weil (`√p log²p`), but the Type I condition
  ("a | A/4, a ≡ −D mod (AD−1)/p") is a divisor condition, not a box; after summing it over a one is back to the
  counts of §3 (same λ's). No new slack.
* (c) is the a = 1 slice (Lemma 2.3(a)): `λ ≍ L²` in total, minimum 1–3 in the data (§1); strictly worse.

**Decisive numbers (Formulation B, best case).** Take d the least integer with `(−d/p) = −1` (so d ≪ p^{1/4+ε}
unconditionally — Burgess; d ≪ L² under GRH — and typically d ≤ 3) and the union over a of the tubes R'_a:
expected count `λ_d ≈ κ_d L²/d`, number of points `h(D') ≍ p√d`, relative measure
`μ_d ≈ L²/(p d^{3/2}) ≈ L²·|D'|^{−1/2}`, minimal width `w ≍ 1/p ≍ |D'|^{−1/2}`. Against the thresholds of
`LITERATURE_AUTOMORPHIC.md` (all for one discriminant; Young/Humphries need D fundamental, D' is not — via T_p
one can transfer, at the cost of Ramanujan-type input for λ_j(p)):

| input | admissible targets (D = |D'| ≍ 4dp²) | ours | gap (powers of p) |
|---|---|---|---|
| Duke / Iwaniec (fixed nice sets, rate D^{−1/28}-type) | μ ≍ 1 | μ ≈ L²/p | p¹ |
| Young Thm 2.1, balls, unconditional | radius ≥ D^{−1/24}, μ ≥ D^{−1/12} | μ ≈ L² D^{−1/2}, w ≈ D^{−1/2} | μ: p^{5/6}; w: p^{11/12} |
| Young Thm 2.1 under Lindelöf | radius ≥ D^{−1/8}, μ ≥ D^{−1/4} | same | μ: p^{1/2}; w: p^{3/4} |
| Young Prop 1.2, cusp strips (existence, single D) | width ≥ D^{−1/18} | width D^{−1/2} | p^{8/9} |
| Humphries–Radziwiłł Thm 1.12 (annuli, **almost all centres**) | μ ≥ D^{−1/2+δ}, r ≥ D^{−1/12+δ} | μ = D^{−1/2}·L² (fixed centre, tube) | p^{2δ}/L² in μ, plus "almost all"→"this target", plus shape |
| Liu–Masri–Young (joint level–disc.) | level q < D^{1/20}, compact targets | level d (fine), Planck targets | as Duke |
| Sardari / BKS optimal covering (S³, SL₂ lifts) | caps of volume N^{−3/4} (N points); exponent 4/3 is *sharp* (big holes) | Planck × polylog (exponent 1) | beyond what is true for worst-case caps |

**Hecke-orbit version with Ramanujan (a standard conjecture) still fails by ≈ p.** For a single z₀ of disc −4d,
`Σ_{w ∈ T_p z₀} φ(w) = (p+1)⟨φ⟩ + √p Σ_j λ_j(p)⟨φ,u_j⟩u_j(z₀)`. For φ = 1_{tube}: `(p+1)⟨φ⟩ ≈ λ ≈ L`, while
`|⟨φ,u_j⟩|` does not decay before `t_j ≍ 1/w ≍ p`; with `|λ_j(p)| ≤ 2` and the local Weyl law
`Σ_{t_j≤T}|u_j(z₀)|² ≍ T²` the Cauchy–Schwarz error is `≍ √p·‖φ‖₂·p ≈ √p·(L/p)^{1/2}·p = p√L` vs main term L.

**Where the slack is (and is not).** The only slack is in the *count*: union over a gives L² per family (one d),
union over d gives `Σ_d λ_d ≈ mean f_I ≈ 0.1 L³`. There is **no power of p** anywhere: hits are distinct Type I
solutions, and §5 shows `f_I(p) ≤ ψ L³` for all but a proportion O(1/ψ) of primes. Positivity ("one point in one
of many targets") does not change the scale: it lowers the needed relative accuracy from o(1) to < 1, which at
expected count L³ is still a Planck-scale statement.

## 5. Conditional theorem? — why no standard hypothesis suffices (precise parts PROVED; verdict Assessment)

**Theorem 5.1 (the count to be certified is polylogarithmic; PROVED relative to (D)32b).** There is an absolute C
such that for every N ≥ 3 and ψ ≥ 1, `#{p ≤ N : f_I(p) > ψ L³} ≤ C·π(N)/ψ` (L = log N). With ET Thm 1.1 in place of
(D)32b the same holds for the total ES count f(p) with ψ replaced by ψ·log log N.
*Proof.* Markov's inequality applied to `Σ_{p≤N} f_I(p) ≪ N L²` ((D)32b; our f_I counts y ≤ z and is at most ET's
f_I) and `π(N) ≫ N/L`. ∎
**Corollary 5.2.** In Formulations A and B (and in any formulation where distinct points in the target give
distinct Type I solutions) the targets attached to p contain ≤ ψL³ points in total, for all but a proportion C/ψ of
primes. A certificate of `f_I(p) > 0` from an equidistribution statement with the local-density main term
`M(p) = Σ λ_{c,d}(p)` (≈ 0.1 L³ on average, §1) therefore needs an additive error `< M(p) ≪ L³`: a **Planck-scale
statement with polylogarithmic (not power) accuracy.**

**Proposition 5.3 (single targets fail at expected count ≍ L; CONDITIONAL on Schinzel's Hypothesis H).** There are
infinitely many primes p ≡ 5 (mod 12) for which the genus-allowed target (c, d) = (1, 3) (expectation `≈ 0.52 L`,
§3) is empty.
*Proof.* x(x² + 12) on the progression x ≡ 5 (mod 12) has no fixed prime divisor (mod 2, 3: x odd, x ≡ 2 (3) give
x² + 12 ≡ 1; for q ≥ 5 at most 3 roots), so H gives infinitely many primes p ≡ 5 (12) with p² + 12 prime.
`χ_{−12}(n) = (n/3)` for n coprime to 6, and −p ≡ 1 (mod 3), so `χ_{−12}(−p) = 1`. By Lemma 2.1(iii) the target counts divisors f ≤ p of
p² + 12 with f ≡ −p ≡ 7 (mod 12); the only divisor ≤ p is 1 ≢ 7. ∎ EVIDENCE: all 3630 such p in [10⁶, 3·10⁶) have
this target empty (one-liner in the commit log of §5; `scripts/spec_target_mean.py` gives the 17 % empty rate among
all allowed p). Applying H to several polynomials p² + 4c²d at once empties any fixed finite set of targets
(this is the campaign's formal-obstruction mechanism, POINTWISE_SIZE Thms M/C, seen from the fixed-p side).

**Proposition 5.4 (thickening = averaging over n; PROVED).** In Formulation A, for z ∈ Λ_d the integer
`k(z) := (2c√d x − √d − p y)/y = 4acd − f − p` is the offset n − p of the integer n = 4acd − f for which (a,c,d,f) is a
Type I quadruple. Hence the thickened target `R_c^{(K)} = {|2c√d x − √d − p y| ≤ K y}` (hyperbolic width
≈ (2K+1)/p) counts exactly `Σ_{|n−p| ≤ K} #{Type I quadruples of n with this c, d}`. *Proof.* Prop 3.1 with ℤ ∋ k.
∎ *Consequence (Assessment).* A spectral bound at Sobolev scale V (target width ≍ 1/V) controls only averages of
f_I(n) over `|n − p| ≲ p/V`. Young's admissible V ≪ D^{1/24} (and V ≪ D^{1/8} under Lindelöf) — whatever the
discriminant D of the family — therefore yields at best statements about intervals of length `p^{1−κ}`, a range where
the campaign already has unconditional short-interval exceptional-set bounds (EXCEPTIONAL_SHORT, (D)30) and where
nothing pointwise follows. The pointwise problem is exactly K = 0.

**Verdict on step (5) (Assessment, with the precise reasons above).** No standard hypothesis — GRH, GLH/Lindelöf in
the discriminant, level or joint aspect, Ramanujan–Petersson, Selberg's eigenvalue conjecture, or a twisted-Linnik
Kloosterman bound `≪ (mnX)^ε` — suffices by itself to give ES (or Type I) for all large p by this route:
1. the quantity to certify is ≤ ψL³ (Thm 5.1), while every such hypothesis enters with a loss `X^ε` (or, made
   effective under GRH, `exp(c log X/log log X)`), which exceeds any power of log p; individual central values are
   not polylogarithmically bounded (resonance Ω-results), so no termwise use of them can reach this scale;
2. the target width is exactly the Planck width `1/p ≍ |D'|^{−1/2}` (Props 3.1/3.2, 5.4), and even assuming
   Ramanujan + Lindelöf the Hecke-orbit spectral error exceeds the main term by ≈ p (§4);
3. single targets at expected count ≍ L are empty for infinitely many p under H (Prop 5.3), so any sufficient
   statement must aggregate ≳ L² targets, across different discriminants (d) and cusps (c or a), with the genus
   factor `1 + χ_{−4d}(−p)` built in (Lemma 2.4; without it the statement is false at n = p²).
A hypothesis that does suffice must be of "Planck-scale, polylogarithmic-accuracy, genus-aware, aggregated" type —
e.g. `Σ_{d ≤ L²} #(T_p Heeg_d(−4d) ∩ ⋃_a R'_a) ≥ (1 − o(1))·M(p)` for all large p — which is ES-Type-I for large
p restated, not a standard conjecture. The implication from such a statement is trivial (Prop 3.2) and is not
claimed as a result.
