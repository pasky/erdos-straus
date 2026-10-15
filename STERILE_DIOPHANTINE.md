# STERILE_DIOPHANTINE — sterility as Diophantine approximation: games, Cantor sets, percolation (O241, spark relay Z10)

Status: checkpoint 1 (O241), awaiting review; report reviews/agent-reports/AGENT_REPORT_O241.md. **ES is not solved here, nor any
infinite case of ES or ES_q; Conjecture 0.2 (O(3, T²) ≠ ∅) is NOT proved.** Labels as in DISCOVERIES.md.
Builds on FF_THIRDS_CORNER.md (O227, branch side-agent/ff-thirds-corner, merged here for reading), FUNCTIONFIELD_ES2/3.md,
FF_STERILE_PUSH.md, STERILE_EXPLICIT.md, POINTWISE_MORDELL17D.md (= M17D). Memos BRAINSTORM/z16_*.md, scripts scripts/z16_*,
data data/z16/.

## 0. Iteration log

* (I1) Goal: a Schmidt-game proof of O(3, T²) ≠ ∅. Screen: every standard game (Schmidt, absolute, potential, hyperplane)
  has dense winning sets; the uncovered set U is closed and misses an open ball, so U is never winning (Thm 2.1). The
  hypothesis that kills it: the obstacles have *fixed* radii (no shrinking constant κ as in Bad = ∪_κ Bad(κ)).
* (I2) Modification: drop the game, keep the tree. A Cantor/König argument needs only a *windowed, local* count at the
  cylinders it actually visits (Lemma 3.1), not Σ over all levels. But with *global* counts alone every Cantor argument
  collapses back to the tail union bound (Prop 3.2, adversarial placement). So the missing input is local, and it is
  sharp: "no alive cylinder has all three children covered at the next depth" already suffices (sibling lemma).
* (I3) Data (`z16_tree.py`, Case A + Case B complete to depth 9): the alive fraction of each c-slice is 0.517 at depth 9,
  the per-depth covered mass decays ≈ ×1/3 per level, and no alive cylinder ever had 3 covered children (§3).
  Percolation reading: in the independence model O ≠ ∅ needs only p_d < 2/3, not Σ p_d < 1.
* (I4) Liouville spectrum (§4): continued fractions of u decide which levels are protected from balanced tuples; only
  rational points are protected at all large levels.

## 1. Setting

q = 3, A = T², c ∈ {1, 2}. X_c := {u ∈ F₃[[T]] : u ≡ 1 + cT (mod T²)} (the c-slice), ultrametric |u − u'| = 3^{−v_T(u − u')}.
A *cylinder of depth n* is a class mod T^n. By FUNCTIONFIELD_ES3 Lemma 1.1 (and FF_STERILE_PUSH Lemma 2.1) every linear family
F valid somewhere on the slice is valid exactly on one cylinder B_F ⊂ X_c ("tuple ball"): u ≡ −E (mod T^{N(s)+1}) for a Case B
tuple of parameter s (N(s) = ⌈s/2⌉), u ≡ −E (mod T^{α+2}) for a Case A datum of depth α. Let 𝔅 be the set of tuple balls and
  U_c := X_c ∖ ⋃_{B ∈ 𝔅} B = {u : x_u ∈ O(3, T²)} ∩ X_c,
a closed set. Conjecture 0.2 (at the slice) is U_c ≠ ∅. FF_THIRDS_CORNER Lemma 1.1/§6: B_F ∋ u iff the *tuple rational*
−w₁/C₁ agrees with u to order N + 1 (Case B), so U_c is the set of points badly approximable by tuple rationals at the
prescribed orders.

## 2. Games cannot do it (PROVED) — and why

**Theorem 2.1 (game barrier; PROVED).** Let 𝒢 be any target game on X_c in which Bob's first move may be any ball of X_c and the
outcome lies in Bob's first ball (Schmidt's (α, β)-game, McMullen's absolute game, the hyperplane-absolute game, the potential
game of Fishman–Simmons–Urbański, the strong game). Then U_c is not 𝒢-winning, and for a cylinder V ⊂ X_c, U_c ∩ V is
𝒢-winning on V iff V ⊂ U_c.
*Proof.* A 𝒢-winning set S meets every ball (Bob opens inside it), so it is dense; U_c is closed, so a winning U_c would be
X_c. But X_c contains a tuple ball: the s = 4 Case B tuples cover u ≡ 1 + cT + 2T² (mod T³) (FUNCTIONFIELD_ES3 §2; `z16_tree`
depth 3: one ball per c). The same argument inside V gives the second statement. ∎
*Which hypothesis kills games.* Games prove things like Bad = ⋃_{κ>0} Bad(κ), Bad(κ) = X ∖ ⋃ B(x_i, κρ_i): Alice's strategy
picks κ = κ(α, β) small. A winning statement about the tuple balls therefore yields at most ⋃_k U_c^{(k)} ≠ ∅, where
U_c^{(k)} avoids the balls shrunk by k digits (tuples counted as covering only at precision N + 1 + k). Since U_c = U_c^{(0)} and
U_c^{(0)} ⊂ U_c^{(k)}, this is strictly weaker. To bridge one would need a renormalisation Φ: X_c → X_c with
Φ^{−1}(B) ⊂ (some tuple ball shrunk by k) for every B ∈ 𝔅; the only natural candidate, Frobenius, goes the wrong way (§5).
*Dimension is not killed.* Bad(κ) for fixed κ is not winning but has positive Hausdorff dimension (Jarník). The analogue for
U_c is a Cantor construction, §3.

## 3. Cantor constructions: what they need, and what global counts cannot give

Call a cylinder V of depth n *alive* if no B ∈ 𝔅 of depth ≤ n contains V.

**Lemma 3.1 (windowed König lemma; PROVED).** Let V₀ be alive of depth n₀, m ≥ 1, K ∈ {1, 2, …}. Suppose for every alive
cylinder V of depth n ∈ n₀ + mℕ inside V₀ (it suffices: for the alive V the construction visits)
  Σ_{B ∈ 𝔅, B ⊂ V, n < depth B ≤ n + m} 3^{n + m − depth B} ≤ 3^m − K.                                    (W)
Then U_c ∩ V₀ ≠ ∅, and if K ≥ 2, dim_H(U_c ∩ V₀) ≥ log K/(m log 3). For m = 1, K = 1, (W) says: **no alive cylinder has all
three children in 𝔅** (sibling condition).
*Proof.* A depth-(n + m) descendant D of an alive V is not alive only if some B ∈ 𝔅 of depth ≤ n + m contains D; B is an
ancestor-or-self of D, and if depth B ≤ n it would contain V. So B ⊂ V with depth in (n, n + m], and B contains
3^{n + m − depth B} of the 3^m descendants. By (W) at least K descendants are alive. Choose K of them for every alive V visited:
a K-ary subtree of alive cylinders. Any point x of the limit set lies in no B ∈ 𝔅 (if x ∈ B, depth d, then the depth-d
cylinder of x, alive by construction, is ⊂ B, contradicting aliveness when d ≥ n₀, and B ⊃ V₀ is excluded by V₀ alive when
d < n₀). For K ≥ 2 the uniform measure on the K-ary subtree gives mass K^{−j} to cylinders of diameter 3^{−(n₀+jm)}; the
mass distribution principle gives dim ≥ log K/(m log 3). ∎

**Proposition 3.2 (global counts collapse to the tail union bound; PROVED).** Let n₀ ≥ 2, let A ⊂ X_c be a union of
cylinders of depth n₀ of relative mass μ_A, and let (n_d)_{d > n₀} be non-negative integers. If Σ_{d > n₀} n_d 3^{−(d−2)} > μ_A,
then there is a set 𝔅' of cylinders, with exactly n_d of depth d (as long as n_d ≤ 3^{d−2}), such that ⋃𝔅' ⊃ A. Hence no
argument that uses only (i) the exact alive set at depth n₀ and (ii) upper bounds on the number of tuple balls of each depth
d > n₀ can prove U_c ≠ ∅ unless it proves the tail union bound Σ_{d > n₀} n_d 3^{−(d−2)} < μ_A.
*Proof.* State it with ">" (the case "=" can leave one point). Greedy: for d = n₀ + 1, n₀ + 2, … the uncovered part of A
is a finite union of depth-(d − 1) cylinders, i.e. of depth-d cylinders; place min(n_d, their number) depth-d cylinders on
uncovered ones (the rest anywhere). As long as nothing runs out, the uncovered mass after stage d is μ_A − Σ_{n₀<d'≤d} n_{d'}3^{−(d'−2)},
a multiple of 3^{−(d−2)}. The partial sums increase to a limit > μ_A, so at the first stage d* where the partial sum reaches ≥ μ_A, the number of uncovered depth-d* cylinders is ≤ n_{d*}: A is covered. ∎
*Reading.* The union-bound barrier of FF_STERILE_PUSH / STERILE_EXPLICIT §4 (exponent +0.167, after O219's refinements
0.000 at the thirds corner) cannot be bypassed by any Cantor/game cleverness that only knows counts per depth. What Lemma 3.1
exploits is *where* the balls are: they must not exhaust a whole alive cylinder within a window.

**Data (EVIDENCE; `scripts/z16_tree.py` on the census `bsE_famcount 3 2 17 print` + Case A `bsE_caseA.route_A4`, complete for
ball depth ≤ 9; log `data/z16/tree_d9.txt`).** Identical for c = 1, 2:
| depth d | 3 | 4 | 5 | 6 | 7 | 8 | 9 |
|---|---|---|---|---|---|---|---|
| distinct balls of depth d | 1 | 2 | 4 | 12 | 13 | 28 | 26 |
| their relative mass p_d | 0.333 | 0.222 | 0.148 | 0.148 | 0.054 | 0.038 | 0.012 |
| alive fraction | 0.667 | 0.667 | 0.593 | 0.543 | 0.535 | 0.521 | 0.517 |
| alive parents with 0/1/2/3 covered children | 0/1/0/0 | 2/0/0/0 | 4/2/0/0 | 14/0/2/0 | 42/2/0/0 | 120/10/0/0 | 370/10/0/0 |
So through depth 9 the sibling condition holds everywhere (never 3, twice 2), the distinct-ball mass Σ p_d = 0.955 < 1 (the
census "cumulative 1.75" counts tuples, many sharing a ball), and about 48 % of each c-slice is covered. Of the 26 depth-9 balls
only 10 fall in the alive part (52 % of the mass): balls fall where coverage already is, mildly.

**Percolation reading (Assessment).** In the independence model (each depth-d cylinder is a ball with probability p_d), alive
cylinders form a branching process with mean offspring 3(1 − p_d). It survives with positive probability iff 3(1 − p_d) is
eventually ≥ 1 + δ, i.e. p_d ≤ 2/3 − δ, and then U_c has dimension → 1 − log₃(1/(1 − p_d)); it has positive measure iff
Σ p_d < ∞. **So in the model, O(3, T²) ≠ ∅ is a percolation statement (p_d < 2/3), not a measure statement (Σ p_d < 1).** The
route-bound exponent of the union-bound barrier (B3-type main-term certificates) controls Σ p_d and is irrelevant for
percolation. Observed p_d ≤ 1/3, decaying. The proof gap is that Lemma 3.1 needs a *deterministic* local statement; the
natural one is the sibling condition (Conjecture 3.3).

**Conjecture 3.3 (sibling conjecture; CONJECTURE, EVIDENCE to depth 9).** No cylinder of X_c of depth n ≥ 3 that is alive has
all three children in 𝔅. (By Lemma 3.1 this implies U_c ≠ ∅, hence Conjecture 0.2.) The weaker "eventually, for the alive
cylinders along some path" suffices.

## 4. The Liouville spectrum: which levels a point protects from balanced tuples (PROVED)

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
*Reading.* At the thirds corner H_τ ≈ s/3 ≈ 2(N + 1)/3, so a level N is **protected** from balanced tuples when
η_u(N + 1) < (N + 1)/3 (up to O(1)): u then has a rational approximant of height < (N + 1)/3 at order N + 1. FF_THIRDS_CORNER
Lemma 1.2 is the case u polynomial, η_u ≤ deg u for all orders. M17D Lemma 2.2(iii) is the ℤ twin (rational u = −p/q, P- and
Q-data with z ≠ 0 have max(a, b) ≥ W/(|p| + q)).

**Corollary 4.3 (only rational points are protected at all large levels; PROVED).** If η_u(D) < D/2 − 1 for all D ≥ D₀
(in particular if all large levels are protected), then u is rational, of height η_u(D₀).
*Proof.* Let ρ_D realise η_u(D). For D ≥ D₀, ρ_D and ρ_{D+1} both agree with u to order D and H(ρ_D) + H(ρ_{D+1}) < D,
so ρ_D = ρ_{D+1} by Lemma 4.1. Hence ρ_D = ρ is constant and δ(u, ρ) = ∞. ∎
*Remark (Assessment; T-adic continued fractions).* For irrational u, η_u is a step function that jumps at the convergent
depths; on a stretch where the best approximant has height h and holds up to order D_h, the protected levels are
3h < N + 1 ≤ D_h, and each new convergent of height h' opens an *unprotected window* N + 1 ∈ (D_h, 3h']. A T-adic
"Liouville number" (heights growing super-exponentially) is protected on all but a density-zero set of levels; a generic
u (η_u(D) = D/2 + O(1), metric Dirichlet) is protected nowhere. This makes Liouville-type points the natural candidates for
explicit sterile points beyond rationals (spark).

**Corollary 4.4 (rational points; PROVED).** Let u = P/Q ∈ X_c, H(u) = h. A tuple covering x_u at level N ≥ 2h with
N + 1 ≤ s − 1 has H_τ ≥ N + 1 − h or ρ_τ = u ("exact": w₁Q = −PC₁). (FF_THIRDS_CORNER Prop 1.4 classifies the exact case
for polynomial u.) ∎ Immediate from Theorem 4.2 with ρ = u.

## 5. Frobenius: covering propagates from u to u³ (PROVED for Case B)

**Proposition 5.1 (PROVED).** Let (E, L', j, γ, g') be a Case B family valid at the slice point x_u (k ≥ 1, FUNCTIONFIELD_ES3
Lemma 1.1). Then (E³, L'³, j'', 3γ, g'³) with j'' := 3(N + 1) − k, N = k + j − 1, is a Case B family valid at x_{u³}, of level
N'' = 3N + 2. So Frob maps every Case B tuple ball B(−E, N + 1) into the tuple ball B(−E³, 3N + 3).
*Proof.* In characteristic 3, f ↦ f³ is an injective ring endomorphism of F₃[T] and of F₃[[T]]. E³ is monic, T ∤ L'³,
g'³ | L'³; E ≡ −u (T^{N+1}) gives E³ ≡ −u³ (T^{3N+3}) = (T^{N''+1}); E ≡ −1 (L') gives E³ ≡ −1 (L'³);
E | D = 1 + T^{N+1+γ}L'g' gives E³ | D³ = 1 + T^{3(N+1+γ)}L'³g'³ = 1 + T^{N''+1+3γ}L'³g'³. Finally 3γ ≤ j'' since
γ ≤ j = N + 1 − k gives 3γ ≤ 3(N + 1) − 3k ≤ 3(N + 1) − k. The converse part of Lemma 1.1 applies. ∎
*Consequences and limits.* x_u³ = x_{u³} lies in the slice u ≡ 1 (mod T²) (the c = 0 slice), not in X_c. So: **if a cube
point x_{u³} is in O(3, T²) for Case B, then x_u is (Case B-)uncovered** — O ∩ X_c ⊇ Frob^{−1}(O ∩ Frob(X_c)) for Case B.
This is a renormalisation in the *wrong* direction for §2 (it maps covered to covered, levels N ↦ 3N + 2, i.e. ball radii
r ↦ r³/3^?·… are shrunk, not enlarged), and Case A at the image needs a separate check (not done). The tuple equations
themselves are not Frobenius-stable: (B₁) needs w₁ + C₁ = T·g'v₁ with T ∤ g', while cubing gives T³; the char-2
Frobenius family of FF_STERILE_PUSH §4 is the case where the valuation bookkeeping closes.
