# AGENT_REPORT_O245 — spark relay Z12: the menu ladder / genus ladder (checkpoint 1)

Branch side-agent/menu-ladder (merged side-agent/menu-sterility first; README conflict with Z10 resolved by keeping both
sections). Deep file MENU_LADDER.md; memos BRAINSTORM/z18_*.md (9, indexed); scripts scripts/z18_* (PARI via
`uv run --with cypari2`). No ES claim; 15·2^s + 1 NOT decided.

**SHARP:**
1. **The genus ladder is flat: descent stops obstructing at D = 2, not at genus 2.** At the unit-square point μ = 0 of
   c₀·2^s + k, the point Y* (= 1 at odd places, 0 at 2) lies in Theorem A's descent set of c₀Y^D + k iff θ(θ − 1) is a
   square in A ⊗ ℚ₂ (Prop 1.1, PROVED; reading: the 2-descent images of P₁ = (1, 2^J) and the ℚ₂-point P₀ = (0, √k)
   agree 2-adically). CERTIFIED (PARI `nfislocalpower`) non-square for all D = 2…10 and (c₀, k) ∈ {(3,1), (15,1), (63,1),
   (7,9), (31,33), (7,57)}; D = 1 is Schinzel; all D ≥ 2 is CONJECTURE (R-O245 scope). So in the tested range O240's spark-3
   prediction holds trivially and is beside the point: whatever keeps 15·2^s + 1 unreachable there is NOT 2-descent.
2. **Rung 2 is sterile for an archimedean reason (Theorem 4.1, PROVED for Type II).** Every Type II polynomial family on
   n = c₀Y² + k (c₀, k > 0) has witness ≡ constant (mod n) (four shapes with deg m ≤ 1 plus the deg m = 2 case added after
   self-review; positivity at real roots kills the rest), and this survives coefficients polynomial in s (§8),
   so no Type II root family of degree 2 reaches a unit-square point — although Y* is outside the descent set (SHARP 1)
   and outside the closure of the Pell T1 points (mod-17 parity, `z18_pell.py`). A fourth kind of sterility beside
   Schinzel/T1, descent and O239's magnitude bound.
3. **Specialisation dictionary (Lemma 2.1, PROVED):** R ∈ ℚ[Y] is integer-valued near μ = 0 iff R(1) ∈ ℤ[1/2] and
   R(0) ∈ ℤ_(2). A root family through μ = 0 = a polynomial interpolation between a ℤ[1/2]-"solution" for n = 4^J (the member
   s = 0) and a ℤ_(2)-solution for n = k; no local obstruction at either end — all difficulty is global-algebraic +
   archimedean.

## Results
* Prop 1.1 + Computation 1.2 (PROVED + CERTIFIED; hand check at D = 2). `z18_descent2.py c₀ k 10`.
* Lemma 2.2 (normal form, a constant): n = σTT′ − T − T′; Lemma 2.3 (PROVED): for even D, T, T′ have no real roots; linear
  shapes impossible.
* Prop 3.1 (PROVED): witness localisation — for k = 1, c₀ odd squarefree the c₀-places are silent (Eisenstein, β = ϖ^{−2}(1−ϖ)),
  W(f) is a parity over primes of Res(f, φ); `z18_witness2.py` confirms on O240 Thm B (W = −1, sign flip +1).
* Theorem 4.1 (PROVED, Type II; Type I (1,0,1) case open) + ladder table Cor 4.2.
* §5 EVIDENCE (negative): exact shape searches (`z18_crt.py`, `z18_quad.py`, `z18_tt.py`, Types I and II, D = 2…8): for
  (15,1) up to 148 exact algebraic D = 4 families, none integral at μ = 0; sanity check recovers O240 Theorem B for (3,1).
* §6 (goal 2): exponential Thm 1.4 (compactness criterion with clopen validity sets V_F read at Y*(μ), PROVED, for s₀ large);
  Theorem A gives V_F ∩ S_D = ∅; the pointwise converse is FALSE for the z14 window menu (O239 Cor 2.8 at μ = 0 ∉ S_2, S_4)
  and for the Type II part of rung 2 (Thm 4.1); global converse open. CONJECTURE 6.4 (weak): μ = 0 of 15·2^s + 1 is reached by no root class of any degree.
* §7 (goal 3): Prop 7.1 (PROVED, narrow): with Y = 2^{v₂(n−1)}, u = (n−1)/Y (defined at every odd n), an (n, Y)-polynomial
  family whose valid set contains a FULL slice progression is an ET identity there, and near unit-square points such
  progressions contain odd squares ⇒ impossible; exponential families escape because u is frozen. "The ladder stops at the
  first positive-density rung; only B2 or norm-form data remain" is Assessment (R-O245 downgrade).
* §8: s-deformation (coefficients polynomial in s) decouples integrality (s = 0 slice) from positivity (s → ∞); rung 2 stays
  closed (Type II, F·G = 1 argument); blocked for windows/SG by s-polynomiality; open for D ≥ 3 shapes.
* 7·4^s + 9 was decided by O239 (EXP_105 Thm 2.6), not here.

## Self-review (codex deep, R-O245) — repairs applied
No FATAL. MAJOR repaired: Thm 4.1 missed the deg m = 2 case (added; theorem survives); descent computation no longer
extrapolated to all D; §6 converse statements narrowed (pointwise, Type II, no classification); Prop 7.1 narrowed to full slice
progressions, its prime-level conclusion downgraded to Assessment; s-deformation memo corrected (rung 2 closed);
`z18_famsearch.py` j = ±D specialisation bug fixed (only j = 0; it had 0 hits anyway). Minors: N(θ − 1) = ±4^J/c₀, P₀ is a
ℚ₂-point, s₀ large in Thm 6.2, search-coverage exclusions stated, witness-parity reading marked heuristic.

## Honest caveats for the reviewer
* Theorem 4.1 is Type II only. Its proof is a short case analysis; please re-derive the shapes (especially the
  "deg(abd) ≠ 2" exclusion, the deg m = 2 case and (1,0,1)).
* Prop 1.1 uses: a local square at all odd places ⇒ global square (Chebotarev, exponent 2). Real places: real roots of
  c₀Y^D + k are negative, 1 − θ > 0. Please check the reduction "γ ∈ (1 − θ)A^{×2}".
* Prop 3.1 assumes k = 1 and c₀ squarefree (for (7,9), (31,33) etc. the places above k need their own computation).
* Searches are bounded heights; their negativity is EVIDENCE only. `z18_tt.py` Type I and Type II modes gave identical
  algebraic counts at D = 4 (118/148) — possibly a genuine duality, not investigated; the integrality filter is shared.
* `z18_crt.py`'s λ/ratio handling for windows scans r over {p/q ≤ 16} only (constant-m windows are better covered by O239's
  exhaustive Cor 2.8).

## Sparks (not pursued)
1. Type I half of Theorem 4.1 (NEAR_SQUARE (1,0,1) Λ-argument for c₀Y² + k).
2. A positivity/size theorem for all D = 4 shapes at μ = 0 of (15,1) would prove CONJECTURE 6.4 at rung 4; the 2-adic
   failure pattern (99/110 algebraic families fail at Y = 0) suggests a 2-adic + archimedean mechanism worth isolating.
3. Polynomial curves on the shape varieties (s-deformation, §8): does any shape variety contain an A¹ from an integral
   non-positive point into the positive region? That would be a genuinely new menu (escapes Lemma 2.3, Thm 4.1 per slice).
4. Type I/Type II count coincidence in `z18_tt.py` (a duality n e + 1 = T(σe − 1) ↔ n = σTT′ − T − T′?).
5. Descent at other profinite points of Λ (not unit-square): is S_D ever non-empty for D ≥ 2 on the Proth families? (Prop 1.1
   says at μ = 0 it is a single 2-adic square class; elsewhere γ is not pinned by a rational point.)
6. For (c₀, k) where SG works ((3,1), (7,9), (23,41), (39,25)) versus fails ((15,1), …): is there an invariant of the
   specialisation pair (n = 4^J over ℤ[1/2], n = k over ℤ_(2)) that predicts it (e.g. the ℤ[1/2]-solution sets of 4/4^J of
   bounded shape)?
