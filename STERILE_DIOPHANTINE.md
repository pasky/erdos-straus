# STERILE_DIOPHANTINE — sterility as Diophantine approximation: games, Cantor sets, percolation (O241, spark relay Z10)

Status: checkpoint 1 (O241); hostile review R248 (`reviews/sterile-diophantine-review.md`): no FATAL; MAJOR D3, D5 and minors
D1–D14 applied in place, marked "(R248 repair)". Report reviews/agent-reports/AGENT_REPORT_O241.md. **ES is not solved here, nor any
infinite case of ES or ES_q; neither Conjecture 0.2 (x*_c ∈ O(3, T²)) nor its conclusion O(3, T²) ≠ ∅ is proved.** Labels as in DISCOVERIES.md.
Builds on FF_THIRDS_CORNER.md (O227, branch side-agent/ff-thirds-corner, merged here for reading), FUNCTIONFIELD_ES2/3.md,
FF_STERILE_PUSH.md, STERILE_EXPLICIT.md, POINTWISE_MORDELL17D.md (= M17D). Memos BRAINSTORM/z16_*.md, scripts scripts/z16_*,
data data/z16/.

## 0. Iteration log

* (I1) Goal: a Schmidt-game proof of O(3, T²) ≠ ∅. Screen: every standard game (Schmidt, absolute, potential, hyperplane)
  has dense winning sets; the uncovered set U is closed and misses an open ball, so U is never winning (Thm 2.1). The
  hypothesis that kills it: the obstacles have *fixed* radii (no shrinking constant κ as in Bad = ∪_κ Bad(κ)).
* (I2) Modification: drop the game, keep the tree. A Cantor/König argument needs only a *windowed, local* count at the
  cylinders it actually visits (Lemma 3.1), not Σ over all levels. But with *global* counts alone every Cantor argument
  collapses back to the tail union bound (Prop 3.2, adversarial placement). So beyond the per-depth counts themselves, the
  extra input a Cantor argument can use is positional (R248 repair D3: sharper per-depth counts would also do), and a sharp
  positional input is: "no alive cylinder has all three children covered at the next depth" already suffices (sibling lemma).
* (I3) Data (`z16_tree.py`, Case A + Case B complete to depth 9): the alive fraction of each c-slice is 0.517 at depth 9,
  the per-depth covered mass decays ≈ ×1/3 per level, and no alive cylinder ever had 3 covered children (§3).
  Percolation reading: in the independence model p_d ≤ 2/3 − δ eventually suffices for O ≠ ∅, while positive measure needs
  Σ p_d < ∞ (R248 repair D13: "suffices", not "iff").
* (I4) Liouville spectrum (§4): continued fractions of u decide which levels are protected from balanced **non-exact** tuples;
  only rational points are protected (from non-exact tuples) at all large levels. Exact tuples (−w₁/C₁ = best approximant)
  are common and are not excluded (R248 repair D5).

## 1. Setting

q = 3, A = T², c ∈ {1, 2}. X_c := {u ∈ F₃[[T]] : u ≡ 1 + cT (mod T²)} (the c-slice), ultrametric |u − u'| = 3^{−v_T(u − u')}.
A *cylinder of depth n* is a class mod T^n. By FUNCTIONFIELD_ES3 Lemma 1.1 (and FF_STERILE_PUSH Lemma 2.1) every linear family
F valid somewhere on the slice is valid exactly on one cylinder B_F ⊂ X_c ("tuple ball"): u ≡ −E (mod T^{N(s)+1}) for a Case B
tuple of parameter s (N(s) = ⌈s/2⌉), u ≡ −E (mod T^{α+2}) for a Case A datum of depth α. Let 𝔅 be the set of tuple balls and
  U_c := X_c ∖ ⋃_{B ∈ 𝔅} B = {u : x_u ∈ O(3, T²)} ∩ X_c,
a closed set. (R248 repair D10) Conjecture 0.2 of FUNCTIONFIELD_ES2 is "x*_c ∈ O(3, T²)", i.e. x*_c ∈ U_c; its conclusion
O(3, T²) ≠ ∅ follows from U_c ≠ ∅ for one c. Below "⟹ O(3, T²) ≠ ∅" never decides x*_c. FF_THIRDS_CORNER Lemma 1.1/§6: B_F ∋ u iff the *tuple rational*
−w₁/C₁ agrees with u to order N + 1 (Case B), so U_c is the set of points badly approximable by tuple rationals at the
prescribed orders.

## 2. Games cannot do it (PROVED) — and why

**Theorem 2.1 (game barrier; PROVED).** Let 𝒢 be one of: Schmidt's (α, β)-game, McMullen's strong game, McMullen's absolute
game, the potential game of Fishman–Simmons–Urbański (FSU) with H = points (the hyperplane-absolute game on X_c is the
absolute game, H = points being the only meaningful case on X_c) (R248 repair D1). Then U_c is not 𝒢-winning, and for a
cylinder V ⊂ X_c, U_c ∩ V is 𝒢-winning on V iff V ⊂ U_c.
*Proof.* Every 𝒢-winning set is dense. For the Schmidt and strong games Bob's first ball is arbitrary, the radii tend to 0 and
the outcome lies in Bob's balls. (R248 repair D1) For the absolute and potential games Alice may also win "by default", so
density is not immediate (FSU Rem. C.3); it follows from FSU Thm C.8 (potential ⇔ absolute winning under Assumption C.6,
which holds for H = points in the doubling space X_c ≅ ℤ₃, FSU Obs. C.7) and absolute ⇒ Schmidt winning on the uniformly
perfect X_c (FSU Prop 4.4(ii)), Schmidt-winning sets being dense. (A general "target game whose first move is an arbitrary
ball" need not have dense winning sets; the theorem is stated only for the listed games.) Now U_c is closed, so a winning U_c would be
X_c. But X_c contains a tuple ball: the s = 4 Case B tuples cover u ≡ 1 + cT + 2T² (mod T³) (FUNCTIONFIELD_ES3 §2; `z16_tree`
depth 3: one ball per c). The same argument inside V gives the second statement. ∎
*Which hypothesis kills games (Assessment; R248 repair D2: this paragraph is a heuristic, not part of the theorem).* Games prove things like Bad = ⋃_{κ>0} Bad(κ), Bad(κ) = X ∖ ⋃ B(x_i, κρ_i): Alice's strategy
picks κ = κ(α, β) small. A winning statement about the tuple balls therefore yields at most ⋃_k U_c^{(k)} ≠ ∅, where
U_c^{(k)} avoids the balls shrunk by k digits (tuples counted as covering only at precision N + 1 + k). Since U_c = U_c^{(0)} and
U_c^{(0)} ⊂ U_c^{(k)}, this is strictly weaker. Each U_c^{(k)} is itself closed and misses the shrunk s = 4 ball, so it is
not winning either (Thm 2.1's argument); only the non-closed union ⋃_k U_c^{(k)} could be. To bridge one would need a renormalisation Φ: X_c → X_c with
Φ^{−1}(B) ⊂ (some tuple ball shrunk by k) for every B ∈ 𝔅; the only natural candidate, Frobenius, goes the wrong way (§5).
*Dimension is not killed.* Bad(κ) for fixed κ is not winning but has positive Hausdorff dimension (Jarník). The analogue for
U_c is a Cantor construction, §3.

## 3. Cantor constructions: what they need, and what global counts cannot give

Call a cylinder V of depth n *alive* if no B ∈ 𝔅 of depth ≤ n contains V.

**Lemma 3.1 (windowed König lemma; PROVED).** Let V₀ be alive of depth n₀, m ≥ 1, K ∈ {1, 2, …}. Suppose for every alive
cylinder V of depth n ∈ n₀ + mℕ (ℕ ∋ 0, so V₀ itself included; R248 repair D14) inside V₀ (it suffices: for the alive V the construction visits)
  Σ_{B ∈ 𝔅, B ⊂ V, n < depth B ≤ n + m} 3^{n + m − depth B} ≤ 3^m − K.                                    (W)
Then U_c ∩ V₀ ≠ ∅, and if K ≥ 2, dim_H(U_c ∩ V₀) ≥ log K/(m log 3). For m = 1, K = 1, (W) says: **no alive cylinder has all
three children in 𝔅** (sibling condition).
*Proof.* A depth-(n + m) descendant D of an alive V is not alive only if some B ∈ 𝔅 of depth ≤ n + m contains D; B is an
ancestor-or-self of D, and if depth B ≤ n it would contain V. So B ⊂ V with depth in (n, n + m], and B contains
3^{n + m − depth B} of the 3^m descendants. By (W) at least K descendants are alive. Choose K of them for every alive V visited:
a K-ary subtree of alive cylinders. Any point x of the limit set lies in no B ∈ 𝔅: if x ∈ B, depth d ≥ n₀, choose j with n₀ + jm ≥ d; the
visited cylinder of x of depth n₀ + jm is alive but lies inside B (depth ≤ its depth) — contradiction (R248 repair D14:
only the depths n₀ + jm are visited; equivalently, ancestors of alive cylinders are alive); if d < n₀, B ⊃ V₀ contradicts
V₀ alive. For K ≥ 2 the uniform measure on the K-ary subtree gives mass K^{−j} to cylinders of diameter 3^{−(n₀+jm)}; the
mass distribution principle gives dim ≥ log K/(m log 3). ∎

**Proposition 3.2 (global counts collapse to the tail union bound; PROVED).** Let n₀ ≥ 2, let A ⊂ X_c be a union of
cylinders of depth n₀ of relative mass μ_A, and let (n_d)_{d > n₀} be non-negative integers. If Σ_{d > n₀} n_d 3^{−(d−2)} > μ_A,
then there is a set 𝔅' of cylinders, with exactly n_d of depth d (as long as n_d ≤ 3^{d−2}), such that ⋃𝔅' ⊃ A. Hence no
argument that uses only (i) the exact alive set at depth n₀ and (ii) upper bounds on the number of tuple balls of each depth
d > n₀ can prove U_c ≠ ∅ unless it proves the tail union bound Σ_{d > n₀} n_d 3^{−(d−2)} < μ_A, or = μ_A with infinitely
many n_d > 0 (R248 repair D4: in that equality case no configuration covers A, by compactness — a finite subcover would
already use mass ≥ μ_A).
*Proof.* State it with ">" (the case "=" can leave one point). Greedy: for d = n₀ + 1, n₀ + 2, … the uncovered part of A
is a finite union of depth-(d − 1) cylinders, i.e. of depth-d cylinders; place min(n_d, their number) depth-d cylinders on
uncovered ones (the rest anywhere). As long as nothing runs out, the uncovered mass after stage d is μ_A − Σ_{n₀<d'≤d} n_{d'}3^{−(d'−2)},
a multiple of 3^{−(d−2)}. The partial sums increase to a limit > μ_A, so at the first stage d* where the partial sum reaches ≥ μ_A, the number of uncovered depth-d* cylinders is ≤ n_{d*}: A is covered. ∎
*Reading (R248 repair D3, MAJOR: the earlier reading overclaimed).* Prop 3.2 is conditional on the per-depth bounds n_d
used; it does not say the *true* counts violate the tail union bound. So the union-bound barrier of FF_STERILE_PUSH /
STERILE_EXPLICIT §4 (exponent +0.167, after O219's refinements 0.000 at the thirds corner) can be passed only by (a) per-depth
count bounds strong enough that the tail union bound holds (e.g. a route bound with negative exponent, or better constants),
or (b) positional input; **Cantor/game cleverness on top of fixed per-depth counts adds nothing.** Class-divisor bounds
(divisors in a residue class mod T^{N+1}) count balls inside a prescribed cylinder and are thus positional, outside Prop 3.2's
hypothesis. The q = 3 data (conditional ball fractions decaying, below) are compatible with the true tail being far below the
alive mass: the barrier is in the upper bounds. What Lemma 3.1 exploits is *where* the balls are: they must not exhaust a
whole alive cylinder within a window.

**Data (EVIDENCE; `scripts/z16_tree.py` on the census `bsE_famcount 3 2 17 print` + Case A `bsE_caseA.route_A4`, complete for
ball depth ≤ 9; log `data/z16/tree_d9.txt`).** Identical for c = 1, 2:
| depth d | 3 | 4 | 5 | 6 | 7 | 8 | 9 |
|---|---|---|---|---|---|---|---|
| distinct balls of depth d | 1 | 2 | 4 | 12 | 13 | 28 | 26 |
| their relative mass p_d | 0.333 | 0.222 | 0.148 | 0.148 | 0.054 | 0.038 | 0.012 |
| alive fraction | 0.667 | 0.667 | 0.593 | 0.543 | 0.535 | 0.521 | 0.517 |
| conditional p_d = balls among children of alive parents (R248 repair D9) | 1/3 | 0/6 | 2/18 | 4/48 | 2/132 | 10/390 | 10/1140 |
| alive parents with 0/1/2/3 covered children | 0/1/0/0 | 2/0/0/0 | 4/2/0/0 | 14/0/2/0 | 42/2/0/0 | 120/10/0/0 | 370/10/0/0 |
So through depth 9 the sibling condition holds everywhere (never 3, twice 2). (The census "cumulative 1.75" counts tuples,
many sharing a ball.) (R248 repair D9) The row "relative mass p_d" counts all distinct depth-d balls, including those inside
already-dead cylinders (e.g. both depth-4 balls lie in the depth-3 ball), so Σ p_d = 0.955 is neither a covered mass nor the
quantity of the percolation model; the model's p_d is the conditional row. Altogether about 48 % of each c-slice is covered. Of the 26 depth-9 balls
only 10 fall in the alive part (52 % of the mass): balls fall where coverage already is, mildly.

**Percolation reading (Assessment).** In the independence model (each alive depth-d cylinder is a ball with probability p_d,
the conditional row above), alive cylinders form a branching process with mean offspring 3(1 − p_d). It survives with positive
probability if 3(1 − p_d) is eventually ≥ 1 + δ, i.e. p_d ≤ 2/3 − δ (R248 repair D13: "if", not "iff" — in a varying
environment survival is governed by the growth of ∏ 3(1 − p_d)), and then U_c has dimension → 1 − log₃(1/(1 − p_d)); it has positive measure iff
Σ p_d < ∞. **So in the model, O(3, T²) ≠ ∅ is a percolation statement (p_d ≤ 2/3 − δ suffices), not a measure statement (Σ p_d < 1).** The
route-bound exponent of the union-bound barrier (B3-type main-term certificates) controls Σ p_d and is irrelevant for
percolation. Observed conditional p_d ≤ 1/3, decaying. The proof gap is that Lemma 3.1 needs a *deterministic* local statement; the
natural one is the sibling condition (Conjecture 3.3).

**Conjecture 3.3 (sibling conjecture; CONJECTURE, EVIDENCE to depth 9).** No cylinder of X_c of depth n ≥ 3 that is alive has
all three children in 𝔅. (By Lemma 3.1 this implies U_c ≠ ∅, hence O(3, T²) ≠ ∅ — the conclusion of Conjecture 0.2; it does
not decide x*_c, R248 repair D10.) (R248 repair D11) A genuinely weaker sufficient form: for some n₁ and some alive V₀ of
depth n₁, no alive V ⊂ V₀ of depth ≥ n₁ has all three children in 𝔅. (The earlier "along some path" form was equivalent to
U_c ≠ ∅ itself.)

## 4. The Liouville spectrum: which levels a point protects from balanced non-exact tuples (PROVED)

For u ∈ F₃[[T]] and a rational ρ = P/Q (P, Q ∈ F₃[T] coprime, T ∤ Q) put H(ρ) := max(deg P, deg Q), δ(u, ρ) := v_T(u − ρ), and
  η_u(D) := min{H(ρ) : δ(u, ρ) ≥ D}   (least height of a rational agreeing with u to order D).
For a Case B tuple τ (notation of FF_THIRDS_CORNER) put ρ_τ := −w₁/C₁ and H_τ := max(a − 1, b − 1).

**Lemma 4.1 (gap principle; PROVED).** For rationals ρ₁ ≠ ρ₂ (denominators prime to T), δ(ρ₁, ρ₂) ≤ H(ρ₁) + H(ρ₂). Hence for
D > 2η, at most one rational of height ≤ η agrees with u to order D.
*Proof.* ρ₁ − ρ₂ = (P₁Q₂ − P₂Q₁)/(Q₁Q₂), a nonzero numerator of degree ≤ H₁ + H₂, and Q₁Q₂ is a T-unit. ∎

**Theorem 4.2 (protected levels; PROVED).** If τ (parameter s) covers x_u at level N with N + 1 ≤ s − 1, then for every rational
ρ ≠ ρ_τ:  H_τ ≥ min(N + 1, δ(u, ρ)) − H(ρ). In particular
  H_τ ≥ N + 1 − η_u(N + 1),   unless ρ_τ is the (then unique, if 2η_u(N+1) < N + 1) least-height approximant of u at order N + 1.
*Proof.* By FF_THIRDS_CORNER Lemma 1.1, EC₁ = g'T^{s−1} + w₁, so E ≡ w₁/C₁ (mod T^{s−1}); covering (E ≡ −u mod T^{N+1}) gives
δ(u, ρ_τ) ≥ N + 1. Then δ(ρ_τ, ρ) ≥ min(N + 1, δ(u, ρ)), and Lemma 4.1 with H(ρ_τ) ≤ H_τ (w₁, C₁ coprime up to a common
factor, which only lowers the height). ∎
*Reading.* At the thirds corner H_τ ≈ s/3 ≈ 2(N + 1)/3, so a level N is **protected** from balanced **non-exact** tuples
(ρ_τ ≠ the best approximant) when η_u(N + 1) < (N + 1)/3 (up to O(1)): u then has a rational approximant of height
< (N + 1)/3 at order N + 1. (R248 repair D5, MAJOR) Exact tuples are *not* excluded and are common, because w₁, C₁ often share a
factor, so H(ρ_τ) < H_τ: e.g. s = 14, w₁ = 2 + 2T + T⁴ + T⁵, C₁ = 1 + 2T + 2T⁴ + T⁵ (gcd 1 + 2T⁴), ρ_τ = (1 + T)/(1 − T) of
height 1, covers the height-1 rational point u = (1 + T)/(1 − T) ∈ X₂ at level N = 7 (a "protected" level, N + 1 > 3h) with
H_τ = 5 ≈ 2(N + 1)/3 — a thirds-corner tuple (`scripts/review_r248_exact.py`; dozens of such tuples for s ≤ 17; that point is
anyway covered by a depth-3 ball). So a rational or Liouville-type point needs, besides Thm 4.2, an exact-case analysis
(tuples with −w₁/C₁ = the approximant), classified only for polynomial u (FF_THIRDS_CORNER Prop 1.4). FF_THIRDS_CORNER
Lemma 1.2 is the case u polynomial, η_u ≤ deg u for all orders. M17D Lemma 2.2(iii) is the ℤ twin (rational u = −p/q, P- and
Q-data with z ≠ 0 have max(a, b) ≥ W/(|p| + q)).

*Check (EVIDENCE, `scripts/z16_thm42_check.py` on the census s ≤ 17, all **reduced** rationals of height ≤ 3; R248 repair D7:
the first version looped over non-reduced (P, Q) with the representative's height and reported 2636 pairs with repeats):*
654 (tuple, reduced rational in its ball) pairs, of which 94 exact (ρ = ρ_τ) and 560 non-exact, 0 violations; R248's independent test (`scripts/review_r248_liouville.py`): 560 pairs + 94 exact, 0 violations, min slack 0
(the bound is attained); Lemma 1.1's agreement δ(−E, −w₁/C₁) ≥ s − 1 on all 348 tuples.

**Corollary 4.3 (only rational points are protected (from non-exact tuples) at all large levels; PROVED).** If η_u(D) < D/2 − 1 for all D ≥ D₀
(in particular if all large levels are protected), then u is rational, of height η_u(D₀).
*Proof.* Let ρ_D realise η_u(D). For D ≥ D₀, ρ_D and ρ_{D+1} both agree with u to order D and H(ρ_D) + H(ρ_{D+1}) < D,
so ρ_D = ρ_{D+1} by Lemma 4.1. Hence ρ_D = ρ is constant and δ(u, ρ) = ∞. ∎
*Remark (Assessment; T-adic continued fractions).* For irrational u, η_u is a step function that jumps at the convergent
depths; on a stretch where the best approximant has height h and holds up to order D_h, the protected levels are
3h < N + 1 ≤ D_h, and each new convergent of height h' opens an *unprotected window* N + 1 ∈ (D_h, 3h']. A T-adic
"Liouville number" (heights growing super-exponentially) is protected on a set of levels of logarithmic density 1 (R248 repair
D6: not natural density — the unprotected levels have upper natural density ≥ 1/3 for every irrational u and ≥ 2/3 when
h_{k+1}/h_k → ∞); a generic
u (η_u(D) = D/2 + O(1), metric Dirichlet) is protected nowhere. This makes Liouville-type points the natural candidates for
explicit sterile points beyond rationals (spark).

**Corollary 4.4 (rational points; PROVED).** Let u = P/Q ∈ X_c, H(u) = h. A tuple covering x_u at level N with
N + 1 ≤ s − 1 (R248 repair D8: the former hypothesis N ≥ 2h is not needed) has H_τ ≥ N + 1 − h or ρ_τ = u ("exact": w₁Q = −PC₁). (FF_THIRDS_CORNER Prop 1.4 classifies the exact case
for polynomial u.) ∎ Immediate from Theorem 4.2 with ρ = u.

## 5. Frobenius: covering propagates from u to u³ (PROVED; Case A added by R248 repair D12)

**Proposition 5.1 (PROVED).** Let (E, L', j, γ, g') be a Case B family valid at the slice point x_u (k ≥ 1, FUNCTIONFIELD_ES3
Lemma 1.1). Then (E³, L'³, j'', 3γ, g'³) with j'' := 3(N + 1) − k, N = k + j − 1, is a Case B family valid at x_{u³}, of level
N'' = 3N + 2. So Frob maps every Case B tuple ball B(−E, N + 1) into the tuple ball B(−E³, 3N + 3).
*Proof.* In characteristic 3, f ↦ f³ is an injective ring endomorphism of F₃[T] and of F₃[[T]]. E³ is monic, T ∤ L'³,
g'³ | L'³; E ≡ −u (T^{N+1}) gives E³ ≡ −u³ (T^{3N+3}) = (T^{N''+1}); E ≡ −1 (L') gives E³ ≡ −1 (L'³);
E | D = 1 + T^{N+1+γ}L'g' gives E³ | D³ = 1 + T^{3(N+1+γ)}L'³g'³ = 1 + T^{N''+1+3γ}L'³g'³. Finally 3γ ≤ j'' since
γ ≤ j = N + 1 − k gives 3γ ≤ 3(N + 1) − 3k ≤ 3(N + 1) − k. The converse part of Lemma 1.1 applies. ∎
(R248 repair D12) Case A likewise: cubing the data, E | a₁ + b₁ gives E³ | a₁³ + b₁³; monicity, coprimality, the lc condition and
E³ ≡ −1 (mod L'³) are preserved, and the required E³ ≡ −u³ (mod T^{k+3j}) follows from E³ ≡ −u³ (mod T^{3(k+j)}). So
Frobenius maps every linear family valid at a slice point x_u to one valid at x_{u³}.
*Consequences and limits.* x_u³ = x_{u³} lies in the slice u ≡ 1 (mod T²) (the c = 0 slice), not in X_c. So: **if a cube
point x_{u³} is in O(3, T²), then x_u ∈ O(3, T²)** — O ∩ X_c ⊇ Frob^{−1}(O) ∩ X_c (all families, R248 repair D12).
This is a renormalisation in the *wrong* direction for §2 (it maps covered to covered, ball depth N + 1 ↦ 3N + 3, i.e. radius r ↦ r³: balls shrink). The tuple equations
themselves are not Frobenius-stable: (B₁) needs w₁ + C₁ = T·g'v₁ with T ∤ g', while cubing gives T³; the char-2
Frobenius family of FF_STERILE_PUSH §4 is the case where the valuation bookkeeping closes.

## 6. Numerics at chosen points (EVIDENCE; `scripts/z16_points.py`, balls `data/z16/balls_d9.txt`, log `data/z16/points_d9.txt`)

Alive to depth 9 (Case A + B complete through ball depth 9), rational points u = P/Q ∈ X₁ ∪ X₂ by height:
h = 1: 4/6 (0.667); h = 2: 20/36 (0.556); h = 3: 160/324 (0.494); h = 4: 1496/2916 (0.513); cylinder average 0.517.
x*_c, 1 + cT + T⁹ (+T⁸¹) and 1 + cT + T³ + T⁹ + T²⁷ are alive to depth 9 for both c. *Reading:* at depth ≤ 9 low-height
rationals are not visibly more sterile than average. This is expected, not a counterexample to §4: coverage at depth ≤ 9 is
dominated by low levels (the balls of depth ≤ 6 carry 0.85 of the distinct-ball mass), where a height-h point is protected only for N + 1 > 3h. The
Liouville advantage of FF_THIRDS_CORNER (x*_c uncovered to level 20) lives at high levels, which the complete tree cannot reach.

## 7. The ℤ face (goal 2)

* The ℤ Liouville lemma is already PROVED: M17D Lemmas 2.1–2.3 (O139) — a rational point u = −p/q lies in a P/Q-box of level L
  iff qa ≡ pb (mod 17^L); non-resonant data (z ≠ 0) have max(a, b) ≥ W/(|p| + q); rays (z = 0, exact) need u < 0 (the sign;
  FF twin: lc(u) = −1, FF_THIRDS_CORNER Prop 1.4). Its proofs are r-free. M17D §3 certified chosen rational points pointwise
  to P-level 10. Theorem 4.2 above is the FF form with the general profile η_u; the ℤ form with η_u (least height of a rational
  agreeing r-adically to order D) holds by the same gap principle |qa − pb| ≤ (|p| + q)·max(a, b).
* Lemma 3.1 holds verbatim on ℤ_r (r-ary tree): a sterile point exists if no alive cylinder has all r children in boxes.
  For r = 17 this asks that 17 boxes of one level never fill an alive cylinder — percolation threshold p < 16/17 in the
  independence model, against the measure route, whose cell-wide tail bound must stay below 0.677 and fails by constants (M17 §4, M17D §1). Prop 3.2 applies
  too: global box-count bounds (D_P, D_Q) alone cannot do better than the cell-wide union bound. (R248 repair D3) **So the
  explicit-r₀ question (r₀ = 2³² in STERILE_EXPLICIT) can be improved either by sharper per-level counts (the r = 17 measure
  route fails by constants, so better constants would do) or by positional (sibling-type) information about where the boxes
  sit; Cantor/game arguments on top of fixed per-level count bounds add nothing.** (Assessment.) The ℤ gap principle is
  multiplicative: r^D ≤ 2H₁H₂ for distinct rationals agreeing r-adically to order D.
* **ℤ sibling census at r = 17 (EVIDENCE; `scripts/z16_ztree.py` on data/m17b P-data K ≤ 13 and Q/U boxes k ≤ 7 regenerated by
  `m17_enum`, complete through depth 7; log `data/z16/ztree17.txt`).** Cell C₅ (C₇ identical, by inversion):
  | depth n | 2 | 3 | 4 | 5 | 6 | 7 |
  |---|---|---|---|---|---|---|
  | boxes in the cell | 4 | 32 | 50 | 158 | 161 | 485 |
  | alive fraction | 0.765 | 0.685 | 0.678 | 0.6772 | 0.6771 | 0.6771 |
  | max boxed children of an alive parent (of 17) | 4 | 4 | 2 | 2 | 2 | 1 |
  So the 17-ary sibling condition holds through depth 7 with a huge margin (≤ 4 of 17), i.e. the window condition (W) of
  Lemma 3.1 holds with m = 1, K = 13 at every visited depth so far (if it held forever: dim ≥ log 13/log 17 ≈ 0.905 for the
  sterile set in C₅). The alive fraction has plateaued at 0.6771 (the cell-wide union-bound target of M17, "0.677").
  The ℤ sibling conjecture (no 17 boxes of one level fill an alive cylinder) would give a sterile 17-generic point; the
  gap principle |a_ib_j − a_jb_i| ≥ 17^{L−1} for two boxes in one parent is no contradiction (P-data have ab up to 17^{2L−1}/4),
  so a proof needs positional/correlation input here too (Assessment).

## 8. Conclusions (exact scope)

PROVED: Theorem 2.1 (the listed games — Schmidt, strong, absolute, potential with H = points — cannot show U_c ≠ ∅: U_c is
closed and not winning); Lemma 3.1 (windowed König: a local window condition at visited alive cylinders suffices, with
dimension bound); Proposition 3.2 (an argument fed only by per-depth count bounds can certify U_c ≠ ∅ only if those bounds
satisfy the tail union bound — the matching barrier for Cantor/game arguments; it does not say the true counts fail it, R248
repair D3); Lemma 4.1, Theorem 4.2, Corollaries 4.3, 4.4 (Liouville spectrum: protected levels for **non-exact** tuples;
only rational points protected at all large levels; exact tuples not excluded, R248 repair D5); Proposition 5.1 (Frobenius
propagation, all linear families, R248 repair D12).
EVIDENCE: alive fraction 0.517 at depth 9, conditional ball fractions ≤ 1/3 and decaying, sibling condition holds to depth 9
(§3, §6); at r = 17 the 17-ary sibling condition holds through depth 7 with ≤ 4 of 17 children boxed (§7). Both tables
reproduced independently by R248.
CONJECTURE: 3.3 (sibling; ⟹ O(3, T²) ≠ ∅, not x*_c ∈ O). Conjecture 0.2 (x*_c ∈ O(3, T²)) and O(3, T²) ≠ ∅ remain CONJECTURE.
