# R123 — hostile review of O123 (POINTWISE_SPECTRAL.md, AGENT_REPORT_O123.md, scripts/spec_*)

Reviewer branch `side-agent/review-spectral`, merged `side-agent/spectral-flip`. All numerical checks below use
from-scratch code `scripts/review_r123_*.py` (no reuse of `scripts/spec_*`). Sources: ET = `sources/elsholtz-tao-1107.1010.pdf`
(read directly).

## Claim 1 — Lemmas 2.1–2.4 (fixed-p forms)

**Verdict: SOUND (minor presentational defects D1, D2).**

Independent check `scripts/review_r123_lemmas.py 3000 400` (10.6 min, one core):
* Route 1 (ET parametrisation, enumerate (a,c,d) with acd = y < 2n/3, f | 4a²d+1, n = 4acd − f) for **all n ≤ 3000**:
  every quadruple with gcd(c,n) = 1 gives an exact rational solution 4/n = 1/(abdn) + 1/(acd) + 1/(bcd) (Fraction
  arithmetic); (ii) `f | an + c` held in all cases; `g = (n²+4c²d)/f = 4bcd − n`, `4abd − ne = 1`, `a+b = ce`.
* Lemma 2.1(iii) re-enumerated independently (c, d, divisors f of p²+4c²d with f ≡ −p mod 4cd, f ≤ g ⇔ a ≤ b):
  identical solution sets for **all primes p ≤ 3000** (0 mismatches).
* Lemma 2.2: `4ad·b − pe = 1` and the polynomial identity `Q'(X,Y) = Q₋(X+2bdY, pY)` checked at 4 points (enough
  for a binary quadratic form identity: 3 coefficients) for every quadruple, n ≤ 3000. I also re-derived both
  coefficient computations by hand: correct.
* Lemma 2.3(a): the a = 1 slice equals the set of factorisations `(tu−1)(tv−1) = tp+1`, tv ≡ 1 (4), for all primes ≤ 3000.
* Lemma 2.3(b) and f_I: a raw ES brute force (all 4/p = 1/u+1/v+1/w, u ≤ v ≤ w, classified by the number of
  multiples of p) agrees with the Type I count (route 1, primitive) and with the Type II factorisation count
  `cqp+1 = (aq−1)(bq−1)` for **all primes p ≤ 400** (0 mismatches each).
* Lemma 2.4: 50 896 quadruples of odd n ≤ 3000 with gcd(n,2cd) = 1: 0 violations of χ_{−4d}(−n) = 1 (own Kronecker
  symbol); no odd square ≤ 3000 has any Type I quadruple. Proof re-derived: f odd, gcd(f,d) = 1 from f | 4a²d+1,
  gcd(f,c) = 1 since q | f, q | c ⇒ q | n²; (−4d/·) is a character mod 4d (−4d ≡ 0 mod 4) and odd. Correct.

Defects:
* **D1 (MINOR) — non-primitive quadruples.** Lemma 2.1(iii) and Prop 3.1/3.2 parametrise *quadruples*, not
  solutions. A quadruple with g = gcd(a,b,c) > 1 is the dilate `(a/g, c/g, g²d, f)` of a primitive one (ET (2.10))
  and gives the *same* (x,y,z). They are not rare: 6 315 non-primitive quadruples (a ≤ b) for primes ≤ 3000 (first
  at p = 19). So "point in R_c ⇔ Type I quadruple" is right, but "distinct points ⇒ distinct solutions" (used in
  Cor 5.2) is false across d ↦ g²d. Repair (R123 repair): add to Lemma 2.1 "(iii) parametrises all quadruples; f_I(p) counts those with
  gcd(a,b,c) = 1 (b = (ap+c)/f). A primitive solution with parameter d₀ has exactly #{g ≥ 1 : g² | d₀} quadruples
  (g·a, g·c, d₀/g², f)"; in Cor 5.2 replace "distinct points give distinct Type I solutions" by "the number of
  points is the number of Type I quadruples, ≤ f_I(p)·max_d #{g : g² | d}", or restrict the targets to primitive
  quadruples (an extra gcd condition, invisible to the spectral side). Effect on conclusions: only constants (the Markov bound of Thm 5.1 applies to the quadruple count too since
  Σ_p #quadruples ≪ N L² as well — ET's upper bound argument counts quadruples). No conclusion changes.
* **D2 (MINOR) — window f ∈ [1,2p] vs a ≤ b.** The normalisation a ≤ b is exactly f ≤ g, i.e. f ≤ √(p²+4c²d),
  not f ≤ 2p. The window [1,2p] used for the areas in Props 3.1/3.2 also contains reflected copies (b, c, d, g)
  (ET Remark 2.4) whenever g ≤ 2p, so the region counts some solutions twice. Constant-factor only; state it.

## Claim 2 — Props 3.1/3.2 (point-in-wedge ⇔ Type I; areas; widths)

**Verdict: SOUND (minor imprecision D3 on widths).**

Re-derived by hand: for z = (2ad + i√d)/f, (2c√d x − √d − p y)/y = 4acd − f − p; for z' = (−2cd + ip√d)/f (root of
[f, 4cd, dg], since fg = p² + 4c²d gives disc. −4dp²), (p/y')(−2a√d x' − √d − y') = 4acd − f − p. Widths at height y:
y/(c√d), resp. y'/(a√d p); areas log(2p)/(c√d), log(2p)/(a√d p) for the stated y-windows. All correct.

Independent numerics `scripts/review_r123_areas.py` (2-D midpoint quadrature of the region's indicator in (x, log y),
no use of the width formula; hyperbolic widths by direct minimisation of arccosh(1+|z−w|²/(2 Im z Im w))):
* areas, A: (p,c,d) = (101,1,1): 5.3103 vs 5.3083; (101,2,3): 1.5329 vs 1.5324; (1009,3,2): 1.8035 vs 1.7937 (grid
  resolution); (257,5,7): 0.4714 vs 0.4719. B: four cases agree to 4 digits.
* point-in-wedge (floating test) vs 4acd − f = p (integer test), all primes ≤ 400, d, a, c < 60, f ≤ 2p: 0 mismatches,
  1962 hits.
* widths: A: p·width = 2.00000 (K = 2c√d = 2), 1.99961 (K = 20), 1.96183 (K = 200), 0.90085 (K = 2000, p = 1009);
  exactly p·(arcsinh((p+1)/K) − arcsinh((p−1)/K)) ≈ 2p/√(p²+K²). B: p·width = 2/√(1+4a²d) to 5 digits.

* **D3 (MINOR).** (a) Prop 3.1: "width 2/p + O(c√d/p²)" is true only for c√d ≪ p; the exact width is
  ≈ 2/√(p² + 4c²d), so for c√d ≍ p (allowed: c ranges up to ≍ p/(ad)) the "tube" is a genuinely different shape. The
  error term is actually O(c²d/p³) in the range c√d ≤ p. (b) Prop 3.2 and §4: the width of R'_a is
  ≈ 2/(p√(1+4a²d)) ≍ 1/(a√d·p), **not ≍ 1/p uniformly** — it shrinks with a. (R123 repair): replace "tube of hyperbolic
  width ≍ 1/p" by "≍ 1/(a√d p)", and "minimal width w ≍ 1/p" in §3/§4 by "width ≤ 1/p (≍ 1/p only for a√d ≍ 1)".
  This makes the targets *narrower*, so it strengthens, not weakens, the negative conclusion.
