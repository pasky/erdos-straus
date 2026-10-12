# Brainstorm O141(b): definability / o-minimal counting for ES

Verdict: **COLLAPSES**. Pila–Wilkie-type results give only upper bounds and are vacuous on algebraic
sets. o-minimal lattice-point lower bounds of Barroero–Widmer type die on scale constraint B3. That
happens at a precise step: the thickening needed to obtain volume is interval averaging (Prop 5.4).

## 1. Idea

The ES solution sets S_n = {(x,y,z) ∈ N³ : 4xyz = n(xy+yz+zx)} form a semialgebraic, hence o-minimally
definable, family. Two tools from o-minimal counting could plausibly give lower bounds:
* (O1) Pila–Wilkie / Bombieri–Pila counting of rational or integer points on definable sets.
* (O2) Lattice-point asymptotics in definable families (Davenport; Barroero–Widmer):
  #(Λ ∩ Z_T) = vol(Z_T)/det Λ + O(Σ_j V_j(Z_T)/(λ₁⋯λ_j)), uniformly in o-minimal families. If the volume
  dominates the error, this is a lower bound.

To prove ES(p) one would need a definable region Z(p) of positive volume and a lattice Λ(p) with
Λ(p) ∩ Z(p) ⊆ {ES witnesses of p} and vol/det ≫ error.

## 2. Literature anchor (from memory, not re-verified this session)

* Pila–Wilkie, Duke Math. J. 133 (2006): there are ≪ T^ε rational points of height ≤ T on the
  *transcendental part* of a definable set.
* Bombieri–Pila (1989): determinant method on curves.
* Barroero–Widmer, "Counting lattice points and o-minimal structures", IMRN 2014. Lattice counting in
  definable families with the error term above.
* Wilkie's conjecture (polylog bounds in R_exp); proved for some Pfaffian curves (Binyamini–Novikov and
  others), from memory.

## 3. Barrier screen

* **(O1) is the wrong direction and the wrong set.** S_n is algebraic, so its algebraic part is all of it
  and Pila–Wilkie says nothing. Determinant-method upper bounds for f(n) exist (ET give f(n) ≪ n^{3/5+o(1)}),
  but upper bounds cannot prove existence.
  * The "polylog" coincidence is cosmetic: Wilkie-type (log T)^c bounds and the average f(n) ≍ log³ n
    are both polylog. A Wilkie bound is an *upper* bound on points of a transcendental curve, and ES
    witnesses are not points of one. (Encoding them via log-coordinates turns algebraic relations into
    linear ones; the set stays semialgebraic in the original coordinates.)
* **(O2) collapses to B3.** Every encoding reduces at fixed p to "N_θ(p) has a divisor in a class mod q"
  (B2, Thm 2.2). Take the Type II slice ff' = N := 1 + 4c²dp, with f ≡ f' ≡ −1 (mod q), q = 4cd.
  * Witnesses are lattice points on a hyperbola, a set of measure zero. Thicken it to
    Z_δ = {(u,v) ∈ [1,N]² : |uv − N| ≤ δN}.
  * vol(Z_δ)/q² ≍ δN log N/q², while V₁(Z_δ)/q ≍ N/q. Hence the main term dominates only if
    δ ≫ q/log N ≥ 1/log N.
  * Then Z_δ contains the factorisations of every N' with |N' − N| ≤ δN, i.e. ≫ N/log N other integers.
    This is exactly Prop 5.4 ("thickening = interval averaging") and the scale constraint
    (main term M ≤ p^{o(1)} for bounded multiplicity).
  * The failing step: "o-minimal error ≤ volume" requires a thickness that destroys pointwise
    information.
* **B5.** At n = m² the thickened counts are positive (other N' nearby), while the exact count is 0, so
  "count in Z_δ > 0 ⇒ witness for m²" is the false step.
* **B6.** The volume main term is an average over N' in an interval: a pure T7 leak.
* **B1/B2.** Not reached; the angle dies before them.
* **Definability of the set {n : ES(n)} itself.** It is Diophantine, hence definable in (N, +, ·)
  trivially. In o-minimal expansions of R the integers are not definable, so no "uniform definability"
  statement can carry arithmetic information about which n are hit. See `logic_divisibility_lgp.md` for
  the more informative definability angle in (N, +, |).

## 4. Experiment

None needed; the collapse is structural. The volume/boundary comparison is elementary.

## 5. Viability Assessment: **COLLAPSES** to B3 (at the step "volume dominates boundary"), and (O1) is
inapplicable (upper bounds, algebraic sets). There is no by-product theorem.
