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

## Claim 3 — §4 gap numbers

**Verdict: SOUND as Assessment (labelling correct; one overstated sentence D4, one bookkeeping remark D5).**

Sources: Young 2017 (arXiv 1405.5457) — abstract checked online, theorem content as recorded (parent-checked PDF) in
`LITERATURE_AUTOMORPHIC.md` l. 72: Thm 2.1 error `‖φ‖₂ D^{5/12+ε} V^{1+ε}` (D^{1/4} under Lindelöf), odd fundamental
D; balls V ≪ D^{1/24} (Lindelöf D^{1/8}); cusp strips V ≪ D^{1/18} (Prop 1.2: b ≈ D^η, η > 4/9 ⇔ width D^{−1/18}).
Humphries–Radziwiłł (arXiv 1910.01360v2, PDF downloaded and read, p. 6–7): Thm 1.12(1) — unconditional, squarefree
fundamental D, inner radius r ≫ |D|^{−1/12+δ}, µ(A_{r,R}) ≫ |D|^{−1/2+δ}, **almost all centres w**. The table row
matches this exactly.

Exponent arithmetic re-done with D = |D'| = 4dp² (d bounded, so D^{1/2} ≍ p): ball radius D^{−1/24} ⇒ area D^{−1/12}
= p^{−1/6}, vs. µ ≈ L²/p: gap p^{5/6} ✓; width p^{−1/12} vs p^{−1}: p^{11/12} ✓; Lindelöf: D^{−1/8} ⇒ p^{−1/4}, area
p^{−1/2}: gaps p^{1/2} ✓ / p^{3/4} ✓; cusp strip D^{−1/18} = p^{−1/9}: p^{8/9} ✓. Least d with (−d/p) = −1:
p^{1/4+ε} is a valid (weaker than Burgess' p^{1/(4√e)+ε}) bound; ≪ L² under GRH (Ankeny/Bach) ✓. Hecke-orbit
computation: with (p+1)·area ≈ L, ‖φ‖₂ ≈ (L/p)^{1/2}, T ≍ p, local Weyl Σ_{t_j≤T}|u_j(z₀)|² ≍ T²:
√p·p·(L/p)^{1/2} = p√L ✓ (arithmetic correct).

* **D4 (MINOR, overclaim in wording).** §0 "Even Ramanujan + Lindelöf Hecke-orbit bounds miss by ≈ p" and Verdict
  reason 2 "even assuming Ramanujan + Lindelöf the Hecke-orbit spectral error exceeds the main term by ≈ p". The
  displayed computation uses only |λ_j(p)| ≤ 2 and Cauchy–Schwarz over j; **Lindelöf enters nowhere**, and the
  computation is an upper bound for one crude method (the report's "points for the reviewer" says so, the main
  document does not). Under a random-wave heuristic for the signs of λ_j(p)u_j(z₀) the error would be ≈ √p‖φ‖₂ ≈ √L,
  i.e. the *truth* is Poisson-scale, consistent with the observed empty rates. (R123 repair): replace by "the
  Ramanujan-only, Cauchy–Schwarz-over-the-spectrum bound for one Hecke orbit exceeds the main term by ≈ p (a
  limitation of termwise spectral bounds, not of the truth; Lindelöf does not improve this estimate)".
* **D5 (MINOR, bookkeeping).** The table converts Young's *ball* thresholds into "gaps" for a *tube* target. Plugging
  the tube data directly into Thm 2.1 (‖φ‖₁ ≈ L/p, ‖φ‖₂ ≈ (L/p)^{1/2}, V ≈ p, h ≈ p) gives error/main ≈
  p^{5/6}·p·(L/p)^{1/2}/L ≈ p^{4/3}L^{−1/2} unconditionally and ≈ p·L^{−1/2} under Lindelöf — i.e. the honest
  "power gap" depends on the metric chosen; the table should say "scale exponents for the ball-equivalent target"
  and add the direct Thm 2.1 ratio. Also Young needs odd fundamental D; D' = −4dp² is neither odd nor fundamental and
  the points Λ'_{d,p} are level-d (Γ₀(d)-type) points — the table already flags non-fundamentality; add "even" and
  "level d". None of this changes the conclusion (all gaps are positive powers of p).

## Claim 4 — Thm 5.1, Prop 5.3, Prop 5.4

**Thm 5.1: SOUND.** (D)32b (DISCOVERIES l. 201; EXCEPTIONAL_TYPEI_LOGLOG l. 43, 451) is `Σ_{p≤N} f_I(p) ≪ N log²N` with
ET's f_I (ordered (y,z); bounded there by 2Σ_c w_c(p), w_c counting *all* (a,d,f), primitive or not). The O123 f_I
(y ≤ z, primitive) is ≤ ET's f_I, so Markov gives #{p ≤ N : f_I(p) > ψL³} ≤ C N L²/(ψL³) ≤ C'π(N)/ψ. ✓ The f(p)
variant: ET Thm 1.1 (checked in the PDF) gives Σ_{p≤N} f_I(p) ≪ N L² log log N and Σ_{p≤N} f_II(p) ≪ N L², and
f(p) = 3f_I(p) + 3f_II(p); so #{f(p) > ψ L³ log log N} ≪ π(N)/ψ ✓ (read "threshold ψL³ replaced by ψL³ log log N").
Since w_c counts non-primitive quadruples too, the same Markov bound holds for the quadruple count of D1.

**Prop 5.3: SOUND-AFTER-REPAIRS (D6).** Re-derived: on x = 12k+5, P(k) = x(x²+12) has no fixed prime divisor
(q = 2: both factors odd; q = 3: x ≡ 2, x²+12 ≡ 1; q ≥ 5: cubic in k with leading coefficient 12³ ≢ 0, ≤ 3 < q roots),
x²+12 irreducible, so Schinzel H applies ✓. χ_{−12}(−p): −p ≡ 7 (mod 12), (−12/7) = (2/7) = +1 ✓ (genus-allowed).
Divisors of the prime p²+12 are 1 and p²+12 ≡ 1 (mod 12), neither ≡ −p ≡ 7 (mod 12), so the target is empty in
*every* f-window ✓ (the proof does not even need f ≤ p).
* **D6 (MINOR, wrong constant).** "expectation ≈ 0.52 L": the data line `d= 3 c=1 … mean= 2.381 mean*cd/L= 0.517`
  (`data/spec/target_mean_1e6.txt`) means mean·cd/L = 0.52 with cd = 3, i.e. **expectation ≈ 0.17 L** (= 2.38 at
  L ≈ 13.8). (R123 repair): replace "≈ 0.52 L" by "≈ 0.17 L (≈ 2.4 at p ≈ 10⁶)" in Prop 5.3 and the report. The
  claim "expectation ≍ L" is unaffected. Also note the emptiness is *structural* (an algebraic reason), so the
  example shows that the per-target Poisson expectation is the wrong model for a thin set of p, not that targets
  fail "randomly".
* Data re-checked from scratch (`scripts/review_r123_prop53.py`, own Miller–Rabin): exactly **3630** primes
  p ≡ 5 (12) in [10⁶, 3·10⁶) with p²+12 prime; target (1,3) empty for all 3630 ✓.

**Prop 5.4: SOUND-AFTER-REPAIRS (D7).** The integer identity is right: for z = (2ad + i√d)/f ∈ Λ_d,
(2c√d x − √d − p y)/y = 4acd − f − p = n − p with n := 4acd − f (hand derivation as in Claim 2; also the floating
test in `review_r123_areas.py` is the K = 0 case). So {|k| ≤ K} picks exactly the points with |n − p| ≤ K, and the
hyperbolic width of the thickened wedge is ≈ (2K+1)/p (Claim 2's width formula with p ± 1 → p ± (K+1/2)).
* **D7 (MINOR, overstated "exactly averaging f_I").** For n ≠ p the point counts the ET N-points (a,c,d,f) of n,
  not Type I *solutions* of n: (i) for composite n the condition gcd(c,n) = 1 (ET Prop 2.3) is not imposed by the
  region, (ii) non-primitive quadruples are counted (D1), (iii) the f-window is tied to p (f ≤ 2p), not to n's own
  normalisation a ≤ b. So the thickened count is Σ_{|n−p|≤K} N_{c,d}(n) with N_{c,d}(n) ≥ (Type I count of n with
  these c, d), equality failing for composite n. (R123 repair): replace "counts exactly Σ_{|n−p|≤K} #{Type I quadruples
  of n …}" by "counts exactly Σ_{|n−p|≤K} #{(a,f) : f | 4a²d+1, 4acd − f = n, f ≤ 2p}, which for prime n differs from
  the Type I count only by non-primitive quadruples and the window". The structural consequence (spectral scale V ⇒
  information only about averages over |n−p| ≲ p/V) is unaffected and is in fact the cleanest point of the document.

## Claim 5 — the verdict and its three reasons (Assessment)

**Verdict: the conclusion ("no standard hypothesis suffices *by this route*") is a fair Assessment, correctly
labelled; but reason 1 is weaker than stated (D8, MAJOR as an argument defect) and reason 3 overstates what H gives
(D9).** Reason 2 carries the verdict.

* **D8 (MAJOR — reason 1 does not cover non-termwise uses of GRH).** Reason 1 says every standard hypothesis "enters
  with a loss X^ε (or exp(c log X/log log X) under GRH)". That is true for *individual* L-values, and the text
  restricts the conclusion to "termwise use". But GRH also enters with only (log log)- or polylog losses in two
  standard ways: (a) effective Siegel: under GRH L(1,χ_D) ≫ 1/log log D (Littlewood), so h(D') and every main-term
  normalisation lose only log log; (b) *moments*: under GRH, Soundararajan/Harper-type upper bounds give
  Σ_{t_j≤T} L(½,u_j)L(½,u_j⊗χ_D) ≪ T²(log)^{O(1)}-type bounds (the spectral second-moment in the Planck range is
  only conjectural, but it is the natural "standard-type" input and it is polylog). So "X^ε loss" is not why the
  route fails. What actually fails is the *use* of the spectral expansion at Planck scale: with Waldspurger,
  |W_j|² ≍ D^{1/2} L(½,u_j)L(½,u_j⊗χ_D)/L(1,sym²u_j) for the Weyl sums W_j = Σ_{z∈Λ_{D'}} u_j(z), and Cauchy–Schwarz
  over t_j ≤ T ≍ p,
  |error| ≤ ‖φ‖₂ (Σ_{t_j≤p}|W_j|²)^{1/2} ≈ (L/p)^{1/2} · p^{1/2} · p · (log)^{O(1)} = p·L^{O(1)}
  against a main term ≈ L: **even with polylog (GRH-moment) L-value input the loss is ≈ p**, coming from
  Cauchy–Schwarz over ≍ p² spectral terms (no cancellation among the signs of ⟨φ,u_j⟩W_j is available from any
  standard hypothesis). (R123 repair): rewrite reason 1 as "(1) the quantity to certify is ≤ ψL³ (Thm 5.1). Individual
  central values are not polylog-bounded even under GRH (exp(c log X/log log X); resonance Ω-results), so termwise use
  fails; and the averaged (moment) use — where GRH does give polylog losses, as do GRH-effective Siegel bounds — still
  loses ≈ p at Planck scale through Cauchy–Schwarz over the ≍ p² spectral terms with t_j ≤ p (displayed computation),
  i.e. reason 1 reduces to reason 2." With this repair the verdict stands as an Assessment about this route.
* **D9 (MINOR — reason 3 overstated).** "any sufficient statement must aggregate ≳ L² targets": Prop 5.3 (and H
  applied to *finitely many* polynomials p² + 4c_i²d_i) only shows that every *fixed finite* set of targets is empty
  for infinitely many p. Emptying a growing number (≍ L²) of targets would need H for a growing family of polynomials,
  which is not a standard consequence of H. (R123 repair): "must aggregate an unbounded number of targets (under H:
  more than any fixed finite set)"; keep "≳ L²" only as the Assessment that the aggregate should be of the full
  family's size.
* Reason 2: sound as an Assessment (Claims 2–3; with D3 the widths are even ≤ 1/p). The document correctly says
  the implication from a Planck-scale aggregate statement is trivial and claims no theorem.
* Label check (§0/§5): "Verdict (Assessment)" ✓; Thm 5.1 "PROVED rel. (D)32b" ✓ (and in fact ET's own upper bound
  ≪ N L² log log N gives the same with ψ → ψ log log N unconditionally of (D)32b); Prop 5.3 "CONDITIONAL on H" ✓;
  Prop 5.4 "PROVED" ✓ after D7 wording. No over-labelled PROVED found.
