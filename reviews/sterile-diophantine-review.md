# R248 — hostile review of STERILE_DIOPHANTINE.md (O241, branch side-agent/sterile-diophantine)

Reviewer: R248 (side-agent/review-sterile-dioph). Scope: STERILE_DIOPHANTINE.md, BRAINSTORM/z16_*.md,
reviews/agent-reports/AGENT_REPORT_O241.md, scripts/z16_*, data/z16/. O227 (FF_THIRDS_CORNER.md) is out of scope except where
cited. From-scratch scripts: `scripts/review_r248_*`; data `data/review_r248/`.

Round 1 complete. **No FATAL defect.** All PROVED statements re-derived and correct as mathematics; the defects are an
incomplete step in Thm 2.1 (density of absolute/potential-winning sets), two strategic overclaims in the readings/report
(D3: Prop 3.2 does not imply "only positional input can pass the barrier"; D5: "protected levels exclude balanced tuples"
ignores exact tuples, which are common), and minor wording/label issues. Both EVIDENCE tables reproduced exactly with
independent code. Repairs applied: none (author's branch had no new commits at review time; parent to forward).

## Summary verdicts

| claim | verdict |
|---|---|
| Thm 2.1 (game barrier) | SOUND-AFTER-REPAIRS (D1 density step for absolute/potential games; D2 "games only give ⋃_k U_c^{(k)}" is Assessment) |
| Lemma 3.1 (windowed König + dimension) | SOUND (minor wording) |
| Prop 3.2 (counts collapse to tail union bound) | SOUND as stated (D4 equality case); its Reading/report consequences OVERCLAIMED (D3, MAJOR) |
| Lemma 4.1, Thm 4.2, Cor 4.3, Cor 4.4 | SOUND (D8 superfluous hypothesis); Reading/SHARP 3 overclaim (D5, MAJOR); Remark density claim false (D6) |
| Prop 5.1 (Frobenius) | SOUND; extends to Case A (D12) |
| EVIDENCE q = 3 tree to depth 9 | CONFIRMED independently (identical ball set and table); p_d definition caveat (D9) |
| EVIDENCE r = 17 tree to depth 7 | CONFIRMED independently (own tree code on R83-engine boxes + stored P K ≥ 9) |
| Conj 3.3 ⟹ Conj 0.2 | SOUND for O(3, T²) ≠ ∅ (D10 naming; D11 vacuous "weaker" form) |
| Percolation reading | Assessment, OK after D9, D13 |

## Defects

1. **D1 (MINOR: proof gap, conclusion true; Thm 2.1, §2 proof and theorem hypothesis).** "A 𝒢-winning set meets every ball (Bob
   opens inside it)" is false for games in which Alice can win *by default* (FSU potential game Def C.4: r_n ↛ 0 or outcome in
   Alice's chosen sets; FSU's own Rem. C.3 says nonemptiness of potential-winning sets is not obvious). Repair: restrict the
   hypothesis to games whose winning sets are known to be dense and add: "for the absolute and potential games density
   follows from FSU Thm C.8 (potential ⇔ absolute winning; Assumption C.6 holds for H = points in the doubling space X_c,
   Obs. C.7) and absolute ⇒ Schmidt winning on the uniformly perfect X_c (FSU Prop 4.4(ii))". Replace "hyperplane-absolute"
   by "(H = points, the only meaningful case on X_c)".
2. **D2 (MINOR, §2 "Which hypothesis kills games", memo z16_game_barrier, report SHARP 2(a)).** "A winning statement … yields at
   most ⋃_k U_c^{(k)} ≠ ∅" / "games only ever give ⋃_k U_c^{(k)}" is a heuristic, not part of the theorem: label Assessment.
   Add that each U_c^{(k)} is itself closed and not winning; only the union could be.
3. **D3 (MAJOR, Prop 3.2 Reading in §3, §7 bullet 2, report SHARP 2(b), memos z16_windowed_konig/z16_zz_sibling).** Prop 3.2 is
   conditional on the per-depth bounds n_d used; it does not show that *true* counts violate the tail union bound. Hence
   "the q = 3 union-bound barrier … and the r₀ = 2³² limit … can only be passed with positional input" and "any improvement to
   r = 17 must use positional information" do not follow — sharper per-depth counts (negative route exponent; better
   constants at r = 17) would also pass. The q = 3 data (conditional p_d ≤ 10/1140 at depth 9, decaying) are compatible with
   the true tail being far below the alive mass. Also "class-divisor bounds, any counting certificate" are mislisted as
   count-only inputs: residue-class divisor counts are positional (they count balls in a prescribed cylinder). Repair: "can
   only be passed by sharper per-depth counts or by positional input; Cantor/game constructions on top of fixed per-depth
   counts add nothing", and drop the mislisted examples.
4. **D4 (MINOR, Prop 3.2 statement).** Equality case: with Σ n_d3^{−(d−2)} = μ_A and infinitely many n_d > 0 covering is
   impossible (compactness), so counts *can* certify non-emptiness there. Replace "< μ_A" in the "unless" clause by "< μ_A, or
   = μ_A with infinitely many n_d > 0".
5. **D5 (MAJOR, Reading after Thm 4.2, memo z16_liouville_spectrum Idea/Assessment, report SHARP 3, §8).** "Level N is
   protected from balanced tuples when η_u(N + 1) < (N + 1)/3" and "only rational points are protected at all large levels"
   drop Thm 4.2's exception ρ_τ = best approximant. Exact tuples are common because w₁, C₁ often share factors: explicit
   counterexample s = 14, w₁ = 2 + 2T + T⁴ + T⁵, C₁ = 1 + 2T + 2T⁴ + T⁵ (gcd 1 + 2T⁴), E = −1 + T + … + T¹², covering the
   height-1 rational u = (1 + T)/(1 − T) at level N = 7 (N + 1 = 8 > 3h = 3, a "protected" level) with H_τ = 5 ≈ 2(N + 1)/3 (`scripts/review_r248_exact.py`,
   dozens of such tuples for s ≤ 17). Repair: "protected from **non-exact** tuples"; add that rational/Liouville points
   additionally need an exact-case analysis (−w₁/C₁ = best approximant), classified only for polynomial u (FF_THIRDS_CORNER
   Prop 1.4).
6. **D6 (MINOR, §4 Remark, memo z16_liouville_spectrum).** "Protected on all but a density-zero set of levels" is false for
   natural density: unprotected levels have upper density ≥ 1/3 for every irrational u and ≥ 2/3 when h_{k+1}/h_k → ∞.
   Repair: "logarithmic density zero".
7. **D7 (MINOR, §4 Check / `z16_thm42_check.py`).** The rational loop uses non-reduced (P, Q) and takes the height of the
   representative, so "2636 pairs" counts repeats with inflated heights (weaker test). My reduced-rational test (560 pairs +
   94 exact, 0 violations, min slack 0) should replace or accompany it.
8. **D8 (MINOR, Cor 4.4).** Hypothesis N ≥ 2h is unused (Thm 4.2 with ρ = u, δ = ∞ needs only N + 1 ≤ s − 1). Drop it or say
   it is only there to make the exact rational unique.
9. **D9 (MINOR, §3 Data table and Percolation reading, memos).** p_d = mass of all distinct depth-d balls includes balls
   inside already-dead cylinders (e.g. both depth-4 balls); the model's p_d is the conditional ball fraction among children of
   alive parents (1/3, 0, 1/9, 1/12, 1/66, 1/39, 1/114 for d = 3..9). Add that row; "Σ p_d = 0.955" is neither a covered mass nor
   a union-bound quantity relevant here.
10. **D10 (MINOR, §1, Conj 3.3, §8, report).** Conjecture 0.2 (FUNCTIONFIELD_ES2) is "x*_c ∈ O(3, T²)"; Conj 3.3 implies only its
   conclusion O(3, T²) ≠ ∅. Reword.
11. **D11 (MINOR, Conj 3.3 last sentence).** The "weaker" path form is equivalent to U_c ≠ ∅ itself; replace by a genuinely
   weaker hypothesis (sibling condition for all alive V ⊂ V₀ of depth ≥ n₁).
12. **D12 (MINOR, improvement, §5 and S5).** Prop 5.1 holds for Case A too (cube the Case A data; congruences only strengthen),
   so drop "Case A not checked" and the "for Case B" qualifier.
13. **D13 (MINOR, Percolation reading).** "Survives iff 3(1 − p_d) eventually ≥ 1 + δ" is only "if" for varying environments.
14. **D14 (MINOR, Lemma 3.1 proof).** "the depth-d cylinder of x, alive by construction" — only the depths n₀ + jm are visited;
   aliveness of the depth-d cylinder follows because ancestors of alive cylinders are alive (or use the visited cylinder of
   depth ≥ d directly). Also make explicit that n ∈ n₀ + mℕ includes n = n₀.

## Independent recomputation: q = 3 survivor tree to depth 9

`scripts/review_r248_caseB.c` enumerates every Case B tuple of parameter s ≤ SMAX from scratch via the (w, C) parametrisation
(L' = g'm' monic, w = Tw₁, C = TC₁ monic, m'wC = T^s + v, w + C = g'v). Key re-derived fact: deg v ≤ max(a, b) < a + b = deg wC,
so m' is the polynomial quotient of T^s by wC — one division per (w₁, C₁, s). Every hit is checked against EE' = 1 + T^sL'g'.
Ball of a tuple: u ≡ −E (mod T^{⌈s/2⌉+1}) (a family at level N needs γ = s − N − 1 ∈ [0, N − 1], so N ≥ ⌈s/2⌉; depth ≤ 9 needs
s ≤ 16). Result: 312 tuples for s ≤ 16, **348 for s ≤ 17 (= the author's count in §4)**.
`scripts/review_r248_tree.py` adds Case A data re-derived from the definition (a₀ = T^α a₁', b₀ = b₁ monic, γ = 0, g' = 1; EF = T^α a₁' + b₁,
E = a₁'b₁K − 1, z := (F + b₁)/a₁', b₁KF = T^α + z, T | z ≠ 0; λ, β, deg z ≤ α − 1), enumerating z and ordered monic
factorisations of T^α + z. The resulting distinct-ball set to depth 9 is **byte-identical** to `data/z16/balls_d9.txt` (172 balls),
and the per-depth table (balls 1, 2, 4, 12, 13, 28, 26; alive fraction .667 … .5167; sibling profiles incl. two parents with
2 covered children at depth 6, none with 3) reproduces §3 exactly for both c. Copy: `data/review_r248/balls_d9.txt`.
Caveat (MINOR, see D-list): "p_d = relative mass of distinct depth-d balls" counts balls lying inside already-covered
cylinders (e.g. both depth-4 balls lie inside the depth-3 ball: profile [2, 0, 0, 0] at depth 4), so Σ p_d = 0.955 is not
a covered mass and not the quantity of the percolation model (where p_d should be the fraction of *alive* depth-d cylinders
that are balls).

## Thm 2.1 (game barrier) — SOUND-AFTER-REPAIRS

Re-derivation. Topology: U_c = X_c ∖ ⋃𝔅 is closed (𝔅 a set of clopen cylinders). X_c contains the s = 4 ball: E = T² − cT − 1,
L' = g' = 1, j = γ = 1, N = 2, D = 1 + T⁴ = (T² + T − 1)(T² − T − 1) over F₃ (checked by hand and found by
review_r248_caseB as the two s = 4 tuples, balls 112, 122 of depth 3). So U_c ≠ X_c and U_c ∩ V ≠ V for V ⊇ that ball. A
dense closed set is everything. The theorem is therefore correct **provided every listed game has dense winning sets**.

* Schmidt (α, β) game, McMullen strong game: Bob's first ball is arbitrary, radii are forced/choosable → 0, outcome ∈ Bob's
  balls; winning sets are dense. ✓
* **Absolute and potential games: the given proof ("Bob opens inside it") is incomplete.** In Fishman–Simmons–Urbański
  (arXiv 1301.5630v11, App. C, Defs C.1, C.4 — accessed) Alice also wins *by default* (if r_n ↛ 0, or if the outcome lies in one
  of her chosen sets N(A_{i,n}, r_{i,n})). FSU themselves remark (Rem. C.3) that "it is not immediately obvious … that sets
  which are winning for the new [potential] game are nonempty"; this follows only via Thm C.8 (potential ⇔ absolute winning
  under Assumption C.6, which holds for H = points in a doubling space, Obs. C.7 — X_c ≅ ℤ₃ is doubling) and absolute ⇒
  Schmidt winning on uniformly perfect spaces (FSU Prop 4.4(ii), cited in Rem. C.3; X_c is uniformly perfect). With that
  chain the density, hence the theorem, holds. The hypothesis class as worded ("any target game in which Bob's first move may
  be any ball and the outcome lies in Bob's first ball") is *not* sufficient: a game with Alice-default-wins satisfies it
  but need not have dense winning sets. → D1.
* "Hyperplane-absolute game" on X_c: hyperplanes are not defined on ℤ₃-like ultrametric spaces; in dimension 1 / H = points it
  is the absolute game. Harmless; say so. → D1.
* "Which hypothesis kills games … a winning statement … yields at most ⋃_k U_c^{(k)} ≠ ∅": this is a heuristic (no theorem says
  every game argument outputs exactly a union over shrink levels; nor is ⋃_k U_c^{(k)} shown to be winning). Inside a PROVED
  block it must be labelled Assessment. Also note that each U_c^{(k)} is itself closed and misses the shrunk s = 4 ball, so
  it too is not winning — only the non-closed union could be. → D2.

## Lemma 3.1 (windowed König lemma) — SOUND

Re-derived. (i) Ancestors of alive cylinders are alive (a ball containing the ancestor contains the descendant and has
depth ≤ the ancestor's). (ii) A depth-(n+m) descendant D of alive V is dead only via a ball B ⊇ D of depth ≤ n+m; B is
comparable with V, and depth B ≤ n would kill V; so B ⊂ V, n < depth B ≤ n+m, killing ≤ 3^{n+m−depth B} descendants;
(W) leaves ≥ K alive. (iii) Limit point x: if x ∈ B ∈ 𝔅 of depth d ≥ n₀, choose j with n₀ + jm ≥ d; the visited
cylinder of x at that depth is alive but ⊂ B — contradiction (the text's "the depth-d cylinder of x, alive by construction"
is right only via (i); MINOR wording). d < n₀: B ⊇ V₀ contradicts V₀ alive. ✓ (iv) Dimension: the uniform measure μ on the
K-ary tree; for 3^{−t}-balls with n₀ + jm ≤ t < n₀ + (j+1)m, μ ≤ K^{−j} ≤ K·(3^{−t})^{s}, s = log K/(m log 3), after
absorbing 3^{n₀ s}; mass distribution principle (Falconer, Prop 4.2 form) gives dim_H ≥ s. ✓ (Metric 3^{−v_T}; constants
depend only on n₀, K, m — legitimate.) (W) for m = 1, K = 1 is "at most 2 children in 𝔅" ✓.
Notes: "n ∈ n₀ + mℕ" must include n = n₀ (ℕ ∋ 0) — V₀ itself must satisfy (W). The parenthetical "it suffices: for the alive V
the construction visits" is correct but makes the hypothesis depend on choices; fine as stated. Nested balls in (W) are
over-counted, which only weakens (W) — harmless.

## Prop 3.2 (global counts collapse to the tail union bound) — SOUND as a statement; its Reading/report use is OVERCLAIMED (MAJOR, D3)

Re-derived. Greedy: before stage d the uncovered part of A is a union of depth-(d−1) cylinders of mass
μ_A − S_{d−1} (S_d = Σ_{n₀<d'≤d} n_{d'}3^{−(d'−2)}), i.e. (μ_A − S_{d−1})3^{d−2} depth-d cylinders; at the first d* with
S_{d*} ≥ μ_A that number is ≤ n_{d*}, so A is covered. ✓ The configuration only adds balls of depth > n₀, so it is
consistent with (i) the exact alive set at depth n₀ and with (ii) the counts. As an *information* statement ("an argument
whose only inputs about 𝔅 beyond depth n₀ are per-depth upper bounds n_d") the proposition is legitimate: the adversary
need not be realisable by actual tuples, because the claim is about what such inputs can certify. ✓
Defects:
* Equality case (MINOR, D4). With Σ = μ_A and infinitely many n_d > 0 no configuration covers A (A compact, balls clopen:
  a finite subcover would have total mass ≥ μ_A, leaving the infinitely many other balls total mass ≤ 0). So the exact
  dichotomy is: counts certify U_c ∩ A ≠ ∅ iff Σ < μ_A, or Σ = μ_A with infinitely many nonzero n_d. "Unless it proves the
  tail union bound ... < μ_A" should be "≤ (with …)". Cosmetic.
* **Scope of the consequences (MAJOR, D3).** Prop 3.2 is conditional on the *given* bounds n_d. It does not say that the
  tail union bound fails for the true counts, so it cannot imply that the barrier "can only be passed with positional
  input". Report SHARP 2 ("Hence the q = 3 union-bound barrier (+0.167 / 0.000 exponents) and the r₀ = 2³² limit of
  STERILE_EXPLICIT can only be passed with positional input") and §7 ("any improvement to r = 17 must use positional
  (sibling-type) information") are non sequiturs: a sharper per-depth count (a route bound with negative exponent, or better
  constants at r = 17 where the measure route "fails by constants") passes the barrier without any positional input. The data
  even suggest the true counts are union-bound-good at q = 3 (p_d ≈ ×1/3 per level, observed tail Σ_{d>9} p_d small against
  alive mass 0.517) — so the barrier is in the *upper bounds*, exactly what Prop 3.2 does not address. Also SHARP 2 lists
  "class-divisor bounds, any counting certificate" as count-only inputs: class-divisor bounds (FF_STERILE_PUSH Lemmas 1.4/1.5:
  divisors in a residue class) count E in a prescribed class mod T^{N+1}, i.e. balls inside a prescribed cylinder — that is
  positional information and is outside the hypothesis of Prop 3.2.
  Repair: replace by "… can only be passed by (a) per-depth count bounds strong enough that the tail union bound holds, or
  (b) positional input; Cantor/game cleverness on top of fixed per-depth counts adds nothing." Remove "class-divisor bounds,
  any counting certificate" from the count-only list (or restrict to the global totals they produce).

## §4 Liouville spectrum — Lemma 4.1, Thm 4.2, Cor 4.3, Cor 4.4: SOUND; Reading/report overclaim (MAJOR, D5); Remark density claim false (D6)

Re-derivation.
* Lemma 4.1: ρ₁ − ρ₂ = (P₁Q₂ − P₂Q₁)/(Q₁Q₂), numerator ≠ 0 of degree ≤ H₁ + H₂ ⇒ v_T ≤ H₁ + H₂; T ∤ Q₁Q₂. ✓
  Brute force (`scripts/review_r248_liouville.py`, all 1641 distinct reduced rationals of height ≤ 3 with T ∤ Q,
  1 345 620 pairs): 0 violations, 3279 equality cases (sharp).
* Thm 4.2: identity re-derived from Lemma 2.1 of FUNCTIONFIELD_ES3: E·C = L'wC − C = g'(m'wC) − C = g'T^s + g'v − C = g'T^s + w,
  divide by T: EC₁ = g'T^{s−1} + w₁, C₁ a T-unit ⇒ E ≡ w₁/C₁ (mod T^{s−1}). Covering (u ≡ −E mod T^{N+1}) and N + 1 ≤ s − 1
  give δ(u, ρ_τ) ≥ N + 1; deg w₁ = a − 1, deg C₁ = b − 1 so H(ρ_τ) ≤ H_τ (cancellation only lowers it); then Lemma 4.1. ✓
  N + 1 ≤ s − 1 with N = ⌈s/2⌉ ⟺ s ≥ 4 — every tuple satisfies it, so the hypothesis is vacuous for the tuple ball itself.
  Checks on my own 348 tuples (s ≤ 17): δ(−E, −w₁/C₁) ≥ s − 1 always; 560 (tuple, reduced rational ρ ≠ ρ_τ of height ≤ 3 in
  the tuple ball) pairs: 0 violations of H_τ ≥ N + 1 − H(ρ), **min slack 0** (the bound is attained); 20 random u per ball
  × all 1641 rationals for the general form H_τ ≥ min(N+1, δ(u, ρ)) − H(ρ): 0 violations, min slack 0.
  (The author's `z16_thm42_check.py` loops over non-reduced (P, Q) with height taken as max(deg P, deg Q) of the
  representative, so its "2636 pairs" contains repeats of the same rational and uses inflated heights for non-reduced
  representatives — a weaker test than stated. MINOR, D7.)
* Cor 4.3: ρ_D, ρ_{D+1} agree to order D, H(ρ_D) + H(ρ_{D+1}) < D/2 − 1 + (D+1)/2 − 1 < D ⇒ equal by Lemma 4.1; constant
  sequence ⇒ δ(u, ρ) = ∞ ⇒ u = ρ. ✓ ("protected" ⇒ hypothesis needs the O(1) in "η < (N+1)/3 + O(1)" to be < D/6 eventually —
  fine.)
* Cor 4.4: immediate from Thm 4.2 with ρ = u (δ = ∞). ✓ The hypothesis N ≥ 2h is not used (MINOR, D8: drop it or say why).

**D5 (MAJOR): "protected levels exclude balanced tuples" ignores the exact case, which is common.** Thm 4.2 has the exception
ρ_τ = (best approximant). The Reading after Thm 4.2, memo z16_liouville_spectrum ("Level N is protected from the thirds corner
when η_u(N + 1) < (N + 1)/3"), and report SHARP 3 ("balanced tuples are excluded at levels with η_u(N + 1) < (N + 1)/3") drop it.
But w₁, C₁ frequently share a factor, so a tuple can have small H(ρ_τ) and balanced H_τ. In my s ≤ 17 data (`scripts/review_r248_exact.py`)
there are dozens of tuples with H(ρ_τ) < H_τ, e.g. s = 14, a = b = 6, w₁ = 2 + 2T + T⁴ + T⁵, C₁ = 1 + 2T + 2T⁴ + T⁵,
gcd = 1 + 2T⁴, ρ_τ = (1 + T)/(1 − T) (height 1), E = −1 + T + T² + … + T¹² ≡ −ρ_τ (mod T¹³). So the height-1 rational point
u = (1 + T)/(1 − T) ∈ X₂ is covered at level N = 7 (N + 1 = 8 > 3h = 3: a "protected" level) by a tuple with H_τ = 5 ≈ 2(N+1)/3 —
exactly a thirds-corner tuple. Hence: Cor 4.3's slogan "only rational points are protected at all large levels" is correct only
for **non-exact** tuples; rational points are *not* protected from exact tuples (and FF_THIRDS_CORNER Prop 1.4 classifies those
only for polynomial u). Repair: everywhere "protected (from non-exact tuples)"; state that a rational point u needs in addition
an exact-case analysis (tuples with −w₁/C₁ = u, i.e. w₁Q = −PC₁), which is open for non-polynomial u; correct SHARP 3.
(This point is also covered by the depth-3 ball 122, so it is not a new covered point — the issue is the claimed mechanism.)

**D6 (MINOR, Assessment remark false as stated).** "A T-adic Liouville number (heights growing super-exponentially) is protected
on all but a density-zero set of levels." The unprotected window at a new convergent of height h' is (D_h, 3h'] with
D_h ≈ h + h' ≈ h', i.e. ≈ (h', 3h']; precisely, for successive best approximants of heights h_k < h_{k+1}, D_k = δ(ρ_k, ρ_{k+1}) ≤ h_k + h_{k+1}
(Lemma 4.1), and all D ∈ (D_k, min(D_{k+1}, 3h_{k+1})] are unprotected; at D = 3h_{k+1} (or D_{k+1}) this gives a fraction
≥ (2h_{k+1} − h_k)/(3h_{k+1}) ≥ 1/3 of unprotected levels, → 2/3 when h_{k+1}/h_k → ∞. So the upper natural density of
unprotected levels is ≥ 1/3 for *every* irrational u and ≥ 2/3 for exactly the Liouville-type points in question (the
logarithmic density is 0 for super-exponential heights). Repair: "protected on a set of levels of logarithmic density 1;
the unprotected levels have upper natural density ≥ 2/3". z16_mahler_points' "relative length 2/9" (window (9ⁿ, 3·9ⁿ] inside (9ⁿ, 9ⁿ⁺¹]) is
consistent with this and already contradicts "density-zero" for that family; also note there the best height on
(9ⁿ, 2·9ⁿ] may be < 9ⁿ (Lemma 4.1 only gives η ≥ 8·9ⁿ⁻¹), harmless.

## Prop 5.1 (Frobenius, Case B) — SOUND; the "Case A not checked" caveat can be removed

Re-derived. Char 3: f ↦ f³ is an injective ring endomorphism of F₃[T], F₃[[T]] and of R̂ (so x_u³ = x_{u³}). Validity
(FUNCTIONFIELD_ES3 Lemma 1.1, k = 2): monic E | D = 1 + T^{N+1+γ}L'g', E ≡ −u (T^{N+1}), E ≡ −1 (L'), g' | L', T ∤ L'g',
0 ≤ γ ≤ j = N + 1 − k, monic cofactor. Cubing: E³ monic, D³ = 1 + T^{3(N+1+γ)}L'³g'³ (char 3), E³ ≡ −u³ (T^{3N+3}),
E³ + 1 = (E + 1)³ ≡ 0 (L'³), g'³ | L'³; with N'' = 3N + 2, γ'' = 3γ: N'' + 1 + γ'' = 3(N + 1 + γ) ✓, j'' = N'' + 1 − k =
3(N + 1) − k ✓, γ'' ≤ j'' ⟸ 3γ ≤ 3(N + 1 − k) ≤ 3(N + 1) − k ✓. Converse of Lemma 1.1 applies. ✓
Case A (author: "not done"; S5): the same works trivially — E | a₁ + b₁ ⇒ E³ | a₁³ + b₁³; a₀³, b₀³ monic, coprimality, the
lc condition and E³ ≡ −1 (mod L'³) are preserved, and the required congruence E³ ≡ −u³ (mod T^{k + 3j}) is implied by
E³ ≡ −u³ (mod T^{3(k + j)}). So Frobenius maps *every* linear family valid at a slice point x_u to one valid at x_{u³}, and
**O ∩ X_c ⊇ Frob^{−1}(O)** holds without the "for Case B" qualifier (MINOR improvement, D12). The "wrong direction"
assessment (balls shrink r ↦ r³; image leaves X_c) is correct.

## EVIDENCE claims

* q = 3 tree to depth 9: **CONFIRMED** from scratch (see top section; identical ball set and table).
* r = 17 cell C₅ (and C₇) tree to depth 7: **CONFIRMED** with own tree code (`scripts/review_r248_ztree.py`, which never
  materialises the 16·10⁶ alive cylinders: dead mass = Σ over boxes not inside a lower box) on boxes from the *R83
  from-scratch engine* `scripts/review_m17_enum.c` (S/U levels 1, 3, 5 and P for K ≤ 7 regenerated here; P line counts 2, 32,
  121, 258 = M17B D_P), plus stored P-data K = 9, 11, 13 and stored R83 level-7 S/U data (K = 9 regeneration timed out
  at 15 min). Result identical to `data/z16/ztree17.txt`: boxes 4, 32, 50, 158, 161, 485; alive fraction .7647, .6851,
  .6782, .6772, .6771, .6771; max boxed children 4, 4, 2, 2, 2, 1. Log `data/review_r248/ztree17_C5.txt`. dim bound
  log 13/log 17 = 0.905 ✓ (arithmetic). Completeness through depth 7 rests on M17/M17B (odd K only, P/Q/U exhaust the
  boxes), not re-reviewed here.
* §6 rational-point alive fractions: not recomputed (low stakes; the author already states no signal).
* §4 check (`z16_thm42_check.py`): passes, but see D7 (non-reduced representatives).

## Percolation reading (Assessment) — mostly fine; two inaccuracies

* The model's p_d must be the probability that an **alive** depth-d cylinder (child of an alive parent) is a ball; the
  table's p_d (all distinct depth-d balls, including those inside already-dead cylinders) is a different quantity (D9).
  The conditional values from the same data are: depth 3: 1/3; 4: 0/6; 5: 2/18; 6: 4/48; 7: 2/132; 8: 10/390; 9: 10/1140 —
  still ≤ 1/3, so the conclusion stands.
* "Survives with positive probability iff 3(1 − p_d) is eventually ≥ 1 + δ": for a varying environment this is sufficient,
  not necessary (survival is governed by the growth of ∏ 3(1 − p_d), e.g. p_d ↑ 2/3 slowly can survive). Say "if". (D13)

## Conjecture 3.3 ⟹ Conjecture 0.2 — the implication is SOUND for "O(3, T²) ≠ ∅"; two wording defects

Re-derived: by the (complete, checked above) depth-3 census, each slice has an alive depth-3 cylinder V₀ (2 of 3 alive; the
only depth ≤ 3 balls are the two s = 4 balls, Case A data have α ≥ 3, i.e. depth ≥ 5). Conj 3.3 gives (W) with m = 1, K = 1
at every alive V of depth ≥ 3, Lemma 3.1 gives U_c ∩ V₀ ≠ ∅, and u ∈ U_c means no linear family is valid at x_u (Lemma 1.1:
every family valid at a slice point is Case A or B and valid exactly on its ball), so O(3, T²) ≠ ∅. ✓
* D10 (MINOR): FUNCTIONFIELD_ES2 Conjecture 0.2 is literally "x*_c ∈ O(3, T²)"; O(3, T²) ≠ ∅ is its *conclusion* (as
  FUNCTIONFIELD_ES3 §2 Assessment calls it). Conj 3.3 does not decide x*_c. Write "⟹ O(3, T²) ≠ ∅ (the conclusion of
  Conjecture 0.2)" throughout (§1 "Conjecture 0.2 (at the slice) is U_c ≠ ∅", Conj 3.3, §8, report).
* D11 (MINOR): "The weaker 'eventually, for the alive cylinders along some path' suffices" is vacuous as a weakening: the
  existence of an infinite path of alive cylinders is *equivalent* to U_c ≠ ∅ (König/compactness). State a genuinely weaker
  hypothesis instead, e.g. "for all alive V of depth ≥ n₁ inside some alive V₀ of depth n₁".

## §7 ℤ face — Assessment-level claims

* "Lemma 3.1 holds verbatim on ℤ_r (r-ary tree)" ✓ (the proof uses only the tree structure).
* "Prop 3.2 applies too … So the explicit-r₀ question is limited by the union-bound form of the argument, and any improvement
  to r = 17 must use positional (sibling-type) information" — non sequitur, see D3: better per-level counts (the M17 route
  "fails by constants") would also do.
* ℤ gap principle: for p₁/q₁ ≠ p₂/q₂ agreeing r-adically to order D, r^D | p₁q₂ − p₂q₁ ≠ 0 gives r^D ≤ 2H₁H₂ — the
  ℤ form is multiplicative (D log r ≤ log 2H₁H₂), not the additive "N ≤ H₁ + H₂"; the text's "|qa − pb| ≤ (|p| + q)·max(a, b)"
  is the right shape. Fine as Assessment.
