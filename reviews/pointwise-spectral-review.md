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
  Cor 5.2) is false across d ↦ g²d. Repair (R123 repair): add to Lemma 2.1 "(iii) parametrises all quadruples; the
  solution count f_I(p) is the number with gcd(a,b,c) = 1, and each solution has exactly τ-many dilates, one per
  g with g | gcd(a,c)…"; in Cor 5.2 replace "distinct Type I solutions" by "Type I quadruples, whose number is
  ≤ Σ_{g} f_I-type count ≪ f_I(p)·max multiplicity" — or simply restrict the targets to primitive quadruples.
  Effect on conclusions: only constants (the Markov bound of Thm 5.1 applies to the quadruple count too since
  Σ_p #quadruples ≪ N L² as well — ET's upper bound argument counts quadruples). No conclusion changes.
* **D2 (MINOR) — window f ∈ [1,2p] vs a ≤ b.** The normalisation a ≤ b is exactly f ≤ g, i.e. f ≤ √(p²+4c²d),
  not f ≤ 2p. The window [1,2p] used for the areas in Props 3.1/3.2 also contains reflected copies (b, c, d, g)
  (ET Remark 2.4) whenever g ≤ 2p, so the region counts some solutions twice. Constant-factor only; state it.
