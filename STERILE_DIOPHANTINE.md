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
cylinders of depth n₀ of relative mass μ_A, and let (n_d)_{d > n₀} be non-negative integers. If Σ_{d > n₀} n_d 3^{−(d−2)} ≥ μ_A,
then there is a set 𝔅' of cylinders, with exactly n_d of depth d (as long as n_d ≤ 3^{d−2}), such that ⋃𝔅' ⊃ A. Hence no
argument that uses only (i) the exact alive set at depth n₀ and (ii) upper bounds on the number of tuple balls of each depth
d > n₀ can prove U_c ≠ ∅ unless it proves the tail union bound Σ_{d > n₀} n_d 3^{−(d−2)} < μ_A.
*Proof.* Greedy: list the alive cylinders of A; for d = n₀ + 1, n₀ + 2, … place the n_d depth-d cylinders disjointly inside
the not-yet-covered part of A, filling A from left to right (always possible while uncovered mass remains, since every
uncovered region at depth d − 1 is a union of depth-d cylinders); surplus cylinders go anywhere. The masses add until A is
exhausted; if the series reaches μ_A at a finite stage, A is covered. If it reaches μ_A only in the limit, place cylinders so
that the uncovered part at stage d is a single cylinder-union shrinking to one point x, and add one extra depth-d₁ ball at x
from the surplus of some later n_d (if all n_d are used exactly, the limit point survives: the statement "Σ ≥ μ_A ⇒ covered"
needs Σ > μ_A or a surplus ball; we state it with >). ∎
(Precise form: if Σ_{d>n₀} n_d 3^{−(d−2)} > μ_A, an adversarial 𝔅' with these counts covers A.)
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
