# AGENT REPORT O203 — composition as a generator of ES certificates on V_n (spark relay X)

Main file: COMPOSITION_ES.md. Scripts: scripts/cp_law.py, cp_census.py, cp_cross.py, cp_typeii.py. Data: data/cp/.
**ES not solved; no infinite case claimed.** Outcome: a precise fixed-μ negative theorem, an exact reduction of
the across-μ question to the Type II divisor problem, and an exact (equivalent) Machin-type dictionary.
Self-review (deep reviewer, R-O203) found 3 MAJOR + 3 MODERATE + minor defects; all repaired in place, marked
"R-O203 #k" (main ones: fixed-μ scope of the no-go; primitivity in Prop 2.1(b); "decomposable" ≠ composition of
V_n points; depth-1 case μ ≤ 2n; even n' = pd in Prop 4.1; no "log³ main term" claim).

**SHARP: none of breakthrough type.** Two clean items worth a relay look:
1. (negative, PROVED, elementary — Thm 1.3/Cor 1.4/Prop 4.1) **The B = 1 slot at μ is ONE explicit element**
   ε_μ = 1 − 2jη̄ ∈ ℤ[2√(μ² − n)] (μ = nj + t, 1 ≤ t ≤ n), existing for every μ > n, always of narrow class δ;
   ES point at μ ⟺ |N(ε_μ)| = 4tj − 1 divides μ. So B = 1 is not a class condition, and at a fixed μ composition
   (or any operation inside O'_μ) can never create an ES point — impossible where 4tj − 1 ∤ μ, superfluous
   elsewhere. Across μ/d the question is exactly the Type II divisor problem (B2); that composition cannot help
   select μ is an Assessment, not a theorem. R202 M2 (ES = unit × three deeper points) is real but a re-expression.
2. (dictionary, PROVED, equivalent to the Type II cube — Prop 5.1) **Type II ⟺ two-term Machin/arccot relations**:
   (2cd + √−pd)(2sd + √−pd) = (d(c+s)/j)(1 + 2j√−pd) ⟺ arccot(2c√(d/p)) + arccot(2s√(d/p)) = arccot(1/(2j√(pd)))
   ⟺ 4csdj = pj + c + s, with 4/p = 1/(cds) + 1/(pdsj) + 1/(pdcj). New to the campaign (grep), but no existence
   theorem from Størmer theory transfers (2-term relations = divisors of 1 + c², i.e. B2).

## Results
* §1 Composition law (PROVED): V_n points at μ = primitive negative-norm elements of O'_μ = ℤ[2√f] with norm | μ;
  product formula A₃ = A₁B₂ + A₂B₁ − 2μA₁A₂, B₃ = B₁B₂ − nA₁A₂; r-fold product is a point iff r odd, primitive,
  ∏D_i | μ; O' has no norm −1 unit, sign(N α) = χ₋₄(|N α|).
* §2 (PROVED): V_n values at μ = δ-fibre of the box of primitive ideals of norm | μ in Cl⁺(O'); T1: box fibre empty
  at squares (χ₋₄ ≡ 1). ES slot = third reduced principal ideal (after 1, 2η̄ − 1, 2η̄).
* §3 (PROVED negative): Davenport pigeonhole in Cl⁺ gives positive-norm elements; δ is a target-sum not forced by
  any count of split primes (explicit group example); and would give ES^{[2]} only.
* §4 (PROVED): B = 1 locus finite, μ ≤ n² + n + (n+1)/4; all Type II = d-sliced B = 1 points of V_{pd} (d | λ).
  Checks: cp_law 401 12 (804 B = 1 points, 0 mismatches; product formula); cp_typeii 200 (602 cube points, 0
  mismatches).
* Census (EVIDENCE, cp_census 5 1000): 166 primes, 1736 ES points, 690 with D prime; 284 of 1046 composite-D ES
  ideals have a principal proper divisor; 41 are unit × three V_n points at the same μ (R202 shape); 88/166 primes
  have ≥ 1 decomposable ES point. T1: 0 ES points at 21 odd squares ≤ 1849. (A p ∈ [1000, 3000] run was started,
  output data/cp/census_1000_3000.txt, may not have finished.)
* §5 (EVIDENCE): composition in ℤ[√−n] (sees all μ) maps V_n points to V_n points 0 times (pairs and 20 000
  triples, n = 13, 59, 97, 101), same as size-matched random baseline.
* §6 Barrier screen: fully inside B2; B3's large ES^{[2]} main term cannot be transported to B = 1 since B = 1 is
  not an ideal/class condition; T1 consistent.

## Iterations (construction attempts)
X1 composition law → X2 kill (slot rigidity; hypotheses: one order, target exactly B = 1) → modification 1:
unbounded box + Davenport (fails: wrong sign, target-sum) → modification 2: across μ via ℤ[√−n] (Machin
dictionary; composition does not preserve V_n) → modification 3: weaker target B ≡ 1 (mod n) = ray class mod (η̄)
(class-group addressable but gives ES^{[2]} only).

## Sparks (not pursued)
1. Type I analogue: is there a 3-fold V^I_n whose B = 1 slice is Type I, with its own quadratic-order slot? If its
   slot were NOT a single element (e.g. a class condition), composition might matter there.
2. Angles: Prop 5.1 makes Type II an angle-addition problem for elements of imaginary-part-1 shape; Hecke
   Grössencharacter equidistribution sees ideal angles, not element shapes — is there a shape-free version?
3. Ray class mod (η̄) for ES^{[2]} with B ≡ 1 (mod n): count/structure of such points in the λ-direction.
4. Decomposable share (27%) vs wide class number h(O'_μ): a Cohen–Lenstra check, purely descriptive.
