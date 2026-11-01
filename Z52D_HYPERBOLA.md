# Z52D_HYPERBOLA — depth lane C1 (rank_O) = A01 (rank_A): fixed-p cancellation on the height-tied hyperbola

ES is OPEN. Nothing here proves or disproves it, and nothing here is progress on 4/p. Labels: PROVED / CONDITIONAL / CERTIFIED /
EVIDENCE / CONJECTURE / Assessment. Internal results are internally reviewed only (not refereed).

Lane brief: `z52bbriefs/depth_z52d.md`, LANE = HYPERBOLA. The cluster's members are Z1034, Z1855, Z2997, Z0211, Z1480, Z2958 and Z3149.
Its targets are FRONTIER §7.1, `data/z52d/avenue/rank_O/RANKING_O.md` §C "C1" and `rank_A/RANKING_A.md` "A01". Scripts are
`scripts/z52d_hyperbola_*` and data are in `data/z52d/hyperbola/` (2.2 MB).

## 0. Summary

Fix a prime p. A (★) triple is (u, B, C) ∈ ℕ³ with 4uBC − u − B = p. The **block count** is
N(U, V) := #{(u, B) ∈ (U, 2U] × (V, 2V] : 4uB | p + u + B}. The **balanced block** is U = V ≈ p^{1/4}, so C ≍ p^{1/2}. Its
mean is O(1): ≈ 3(log 2)²/π² ≈ 0.146.

1. **PROVED (elementary, folklore).** N(U, V) ≤ p^{o(1)}·min(U, V, p/(UV) + 1), N(U, U) ≤ U, and R(p) ≪ p^{1/3+o(1)}
   (Thm 1).
   * A01's test "prove or refute a p^{2/5−δ} block bound" is therefore **vacuous**: the bound holds trivially for every
     δ < 1/15.
   * FRONTIER's benchmark "the best pointwise bound for E(p) is p^{2/5+o(1)}" should read p^{1/3+o(1)}. The p^{2/5} is
     Elsholtz–Tao's bound for the full Type II count, not for (★).
2. **PROVED.** In the balanced block (integer U ≥ 1 with 2U < p), u | p + B forces B = f(u). Here f is the partial map
   x ↦ the unique element of (U, 2U] that is ≡ −p (mod x), or ⊥ if there is none. So the block's (★) pairs are exactly the
   2-cycles of f that also satisfy the 4-condition 4 | (p+u+B)/(uB). Each divisibility relation is the graph of f in one
   direction. So a dispersion that applies Cauchy–Schwarz in the variable in which the relation is a function has **no
   off-diagonal terms** (Prop 2). This is a statement about that implementation only.
3. **PROVED (at fixed p). The low-conductor part is a universal constant up to a negligible error.** Expand 1[4uB | n] with
   additive characters mod 4uB and group the frequencies by conductor d. For smooth weights and every D ≤ min(U, V)^{1−ε}, the
   d ≤ D part L_D(n) equals J·Σ_{d≤D, d odd} μ²(d)/d² + O_A(min(U,V)^{−A}). This holds for every integer n coprime to all
   d ≤ D: every prime p > D, and every odd square m² with m free of prime factors ≤ D (Thm 3).
   * Consequence (Cor 3.2). (★) vanishes at squares (T1), so at such squares the high-conductor remainder
     H_D = N_w − L_D equals −L_D + O(min^{−A}). So a uniform estimate |H_D(n)| ≤ X, valid for all D-rough n, cannot be used
     with the common leading term L_D to prove N > 0 with a margin bounded away from 0. Such a positivity argument has to use
     the primality of p beyond D-roughness. (Such bounds can still serve upper-bound purposes.)
   * Corollary 4 (PROVED, for the product local model). In any block with min(U, V) → ∞, the class-conditioned model M_q
     (p mod q, q fixed) is flat in the class up to O_q(min(U,V)^{−1+ε}), uniformly in p. So in that pair-product model F(p)
     cannot enter the main term of a block with min(U, V) → ∞.
   * Check: with smooth weights at 12 primes near 10¹², L₄₀(p) agrees with the prediction 0.0200825840 to relative 6·10⁻⁹
     (45-digit recomputation by the reviewer: spread 1.3·10⁻¹⁰). This is consistent with the error term.
4. **PROVED. No free variable at high conductor (Thm 5).** All but a τ(q)/K fraction of the frequencies mod q = 4uB have conductor
   ≥ q/K. Each such conductor is shared by ≤ K·p^{o(1)} pairs (u, B).
   * At fixed conductor d the sum over the residue a is complete and equals the Ramanujan sum c_d(n). Only summing these over
     all d | q returns the original indicator. So a complete-sum or Poisson step *at fixed conductor* has ≤ K·p^{o(1)} terms to act on. This is Z1034's
     "dual at least as long as the original" in this precise, scoped sense.
   * It does not exclude cancellation *across* conductors. That would be a different method, and none is known.
5. **Thm 6 (ψ / exponential-sum route).**
   * PROVED: N is given exactly by sawtooth functions of F = (p + u + B)/(4uB), and Erdős–Turán/Vaaler gives
     N ≤ UV/(H+1) + 1/16 + 2.5·max_{1≤h≤H} |S_h|.
   * PROVED: for H ≥ 2UV, max |S_h| ≥ (UV)^{1/2}/2. Square-root bounds fed into this inequality give only ≍ (UV)^{1/2}. That
     is ≥ min(U, V), so it never beats Thm 1, and in the balanced block it equals the trivial bound p^{1/4}.
   * So max-bounds with H ≥ 2UV have a provable square-root floor, and square-root max input gives no power saving for any H.
   * Still open: beyond-square-root max-bounds on a shorter segment H ≈ (UV)^{1/2+η} (R1), and cancellation between
     frequencies.
   * Assessment (full-box stationary-phase count): the 2D Poisson (B-process) dual of S_h has ≈ 0.016·h²ρ²·UV terms, with
     ρ = p/(UV)². It is shorter than the original only for h ≲ 7.9/ρ; in the balanced block, only h ≤ 7 out of the
     ≍ 16UV ≈ 1.6·10⁷ frequencies needed.
   * **EVIDENCE** at p = 10¹² + 39, U = 1000: |S_h| is square-root size (rms 1.77·U for h ≤ 2000; rms 1.42·U for sampled h up to
     1.6·10⁷; max 5.8·U). The best bound obtained from the Vaaler inequality over H ≤ 2000 is 13 448, i.e. 13.4 × the trivial
     bound U.
6. **EVIDENCE (falsifier: 10⁵ consecutive primes from 10¹² + 39, plus 2·10⁴ primes each at 10⁸, 10¹⁶, 10¹⁸).**
   * **Variance = swap-Poisson.** In the balanced block, var/(2M₀) = 0.97, 1.03, 0.98, 0.96 in the four windows.
     N/2 ~ Poisson(mean/2) is not rejected (pooled bins, fitted rate, df = 1: p = 0.65, 0.94, 0.39, 0.13). Plain Poisson
     is rejected (χ² ≈ 10⁴). On the interior region u, B, C ≥ T₀ = 1000, var/(2M₀) = 1.01.
   * **No class structure in the interior.**
     * Correlation of the balanced-block error with log F(p): r = 0.001 (t = 0.27).
     * Interior region: log-linear coefficient on log F c = −0.02 ± 0.03. Class means mod 3, 5, 7, 8, 16 are flat (all
       p ≥ 0.43).
     * Boundary R − N_int: c = 1.00 ± 0.01, class χ² up to 2546 on 5 df. RESIDUE_HARDNESS's mod-7 factors reappear there with
       the predicted 1/L rescaling.
   * **The Brauer term is negligible in the block** at 10¹² (|T| ≤ 0.02, sd 5·10⁻⁴; at 10⁸, |T| ≤ 0.053, sd 0.004).
   * The interior carries only 3.8 % of R(p) at 10¹². It is **empty for 9.8 % of primes**; swap-Poisson predicts 9.85 %.

**Verdict: narrowed.** Four specific implementations of the cluster's first lemma are closed by scoped theorems:

* one-step dualization at fixed conductor (Poisson/Voronoi/Ramanujan in (u, B), (u, C) or the divisor form; Thm 5, §3.7);
* dispersion by Cauchy–Schwarz in the function variable (Prop 2);
* the majorant route with max |S_h| input, when that input is square-root size (any H), or when H ≥ 2UV (Thm 6). This leaves
  R1 open;
* a main term built from low-conductor or class-conditioned local data. That data is p-independent up to negligible error and
  agrees at rough squares (Thm 3, Cor 3.2), and the product model is class-flat (Cor 4). The data agree.

What survives:
* cancellation across conductors or across frequencies, for which no method is known;
* in particular (R1), beyond-square-root bounds for S_h on h ≤ (UV)^{1/2+η}, which is *sufficient* for a saving through
  Thm 6(a) (the numerics show square-root size);
* (R2), a bound for the 2-cycles of f that satisfy the 4-condition, which *is* equivalent to the balanced-block count.

FRONTIER §7.1's "only lead not ruled out" should be rescoped (§7). The p^{2/5} → p^{1/3} benchmark correction stands
independently.

## 1. Statements attacked

* **(S1) C1 first lemma / A01.** For U = V = ⌊p^{1/4}⌋, show |N(U,U) − M(U)| ≪ p^{1/4−δ} *by cancellation*, for some δ > 0
  and every large p. Here M is a class-aware local main term (M₀, M_BM or M_F). The trivial bound is N ≤ U.
  **Status: OPEN.** It is not proved here. The standard one-step implementations listed in the verdict are closed below
  (§3); cancellation across conductors or frequencies is not excluded.
* **(S1′) A01's specific test.** "A p^{2/5−δ} block bound." **Status: PROVED trivially** (Thm 1); the test is vacuous.
* **(S2) Z1034 no-go.** "The Voronoi/Ramanujan dual is at least as long as the original." **Status: PROVED in the scoped sense
  of Thm 5** (at fixed conductor ≥ q/K there are ≤ K·p^{o(1)} terms; the complete a-sum gives c_d(n), and summing over d | q
  returns the original indicator)
  **and §3.7** (divisor/Voronoi form: one integer per modulus). The B-process length (Thm 6(e)) and the conductor-block ratio
  D³/(UV)² (§3.5) are Assessment computations.
* **(S3) Falsifier.** Over ~10⁴ primes near 10¹² (we used 10⁵), compute the block errors N − M_F, compare the variance with
  Poisson, and correlate with F(p). **Status: EVIDENCE**, §5.

## 2. Exact forms of the block count

Notation:
* p ≥ 5 prime; 𝔅 = 𝔅(U,V) = (U, 2U] × (V, 2V] ∩ ℤ², so |𝔅| = UV for integers U, V.
* q = q(u,B) = 4uB and n = n(u,B) = p + u + B.
* "adm" means gcd(u, B) = 1 and u + B odd.
* ρ := p/(UV)².
* c_d(·) is the Ramanujan sum; e(x) = e^{2πix}; ψ(x) = x − ⌊x⌋ − 1/2.
* W(u,B) = w₁(u/U)w₂(B/V) with w_i ∈ C_c^∞((1,2)), w_i ≥ 0, and N_w = Σ W·1[q | n]. Sharp cutoffs are w_i = 1_{(1,2]}.

**Lemma 0 (PROVED).** If 4uB | p + u + B then (u, B) is adm, and C = n/q is the unique third coordinate. R(p) is the sum of N over
the dyadic blocks U, V ∈ {2^k : k ≥ −1}; the block (1/2, 1] = {1} covers the coordinate 1.

*Proof.* g = gcd(u, B) divides n − u − B = p. If g = p then u, B ≥ p ≥ 5, and 4uB ≥ 10B + 10u > p + u + B, which is
impossible. So g = 1. Also 4 | n and p is odd, so u + B is odd. ∎

**(E1) Additive characters mod 4uB.** Since 1[q | n] = q⁻¹ Σ_{h mod q} e(hn/q) = q⁻¹ Σ_{d|q} c_d(n),

  N_w = Σ_{u,B} (W(u,B)/q) Σ_{d | q} c_d(p + u + B) = Σ_{d ≥ 1} Σ*_{a mod d} e(ap/d) Σ_{(u,B): d | 4uB} (W/q)·e(a(u + B)/d).   (2.1)

The second form is the dual, indexed by the frequency (d, a) with d the conductor. The first form is the same dual after the
complete a-sum has been evaluated.

**(E2) Trial form (A01's coordinates, m = 4uC − 1).**
* N(U,V) = #{(u, C) : U < u ≤ 2U, m | p + u, (p+u)/m ∈ (V, 2V]}.
* Since 4C(p + u) = (4Cp + 1) + m, we have p + u ≡ \overline{4C}(4Cp + 1) (mod m) and \overline{4C} ≡ u (mod m). So
  1[m | p+u] = 1[m | 4Cp + 1]: the divisor form. Its additive expansion is m⁻¹ Σ_{h mod m} e(h(p+u)/m), a Kloosterman
  fraction whose modulus and inverse are tied to the summation variables.
* In the balanced block m ≍ p^{3/4}, so the conductors are ≍ p^{3/4}. Each value of m comes from ≤ τ((m+1)/4) pairs (u, C),
  because 4uC = m + 1.

**(E3) Sawtooth form (PROVED, exact).** Let F(u,B) := n/q = (p + u + B)/(4uB). For integers n, q ≥ 1 we have
1[q | n] = ⌊n/q⌋ − ⌊(n−1)/q⌋, and ⌊x⌋ = x − 1/2 − ψ(x). Hence

  N(U,V) = Σ_{𝔅} [ 1/(4uB) − ψ(F(u,B)) + ψ(F(u,B) − 1/(4uB)) ].   (2.2)

Also, for every 0 < δ < 1/(16UV),

  N(U,V) = #{(u,B) ∈ 𝔅 : ‖F(u,B)‖ ≤ δ}.   (2.3)

Reason: F ∈ q⁻¹ℤ with q ≤ 16UV, so F ∉ ℤ implies ‖F‖ ≥ 1/q ≥ 1/(16UV). Put S_h := Σ_{𝔅} e(hF(u,B)) (sharp) or its smoothed
version. The phase is hF = hp/(4uB) + h/(4B) + h/(4u).

**(E4) 2-cycle form (balanced block with integer U ≥ 1 and 2U < p; PROVED, Prop 2).**
N(U, U) = #{x ∈ (U, 2U] : f(x) ≠ ⊥, f(f(x)) = x, 4 | (p + x + f(x))/(x f(x))}, where f is the partial remainder map of
§3.2 (with f(⊥) = ⊥). The 4-condition is part of the count: for p = 17, U = 2, {3, 4} is a 2-cycle of f, but
(17 + 3 + 4)/12 = 2, so it does not contribute.

**(E5) Hyperbola (Weil) form.**
* The block maps by (u, B) ↦ (x, y) = (4Cu − 1, 4CB − 1) into {xy ≡ 1 (mod 4p)}. Since x = (p + u)/B and y = (p + B)/u,
  the image lies in [(p+U)/(2V), (p+2U)/V] × [(p+V)/(2U), (p+2V)/U]. The class condition is x ≡ −1 (mod (xy − 1)/p)
  (FRONTIER §7.1).
* In the balanced block this box has area ≍ p^{3/2}. That is (up to constants) the **self-dual box** of the modular hyperbola
  mod 4p: 2D Poisson maps an X × Y box with ≈ XY/(4p) points to (4p/X)(4p/Y) dual terms, and the two agree at XY = (4p)^{3/2}.
* It is also exactly Shparlinski's area-m^{3/2} threshold ("out of reach" below it; PARITY_AUDIT row B1). The box main term
  ≍ p^{1/2}/8 is already below the Weil error p^{1/2+o(1)} before the height condition is imposed.

## 3. Theorems

### 3.1 Elementary bounds (Theorem 1; PROVED, folklore)

**Theorem 1.**
(a) N(U, V) ≤ Σ_{U<u≤2U} (⌊V/u⌋ + 1) ≤ U + V. In particular N(U, U) ≤ U.
(b) N(U, V) is at most each of the following:
* Σ_{U<u≤2U} τ(p + u);
* Σ_{V<B≤2V} τ(p + B);
* Σ_{C ∈ I} τ(4Cp + 1), where I = [p/(16UV), (p + 2U + 2V)/(4UV)] is the block's level range.

(c) N(U, V) ≤ p^{O(1/log log p)}·min(U, V, p/(UV) + 1), and R(p) ≤ p^{1/3 + O(1/log log p)}.

*Proof.*
(a) If 4uB | n then u | p + B, i.e. B ≡ −p (mod u). An interval of V consecutive integers contains ≤ ⌊V/u⌋ + 1 integers of a
residue class mod u. For V = U and u > U this count is ≤ 1.

(b) There are three cases.
* B | p + u gives ≤ τ(p + u) values of B for each u. Symmetrically, u | p + B gives ≤ τ(p + B) values of u for each B.
* For fixed C, (4Cu − 1)(4CB − 1) = 4C(4uBC − u − B) + 1 = 4Cp + 1. So x = 4Cu − 1 is a divisor of 4Cp + 1, and x determines
  (u, B).

(c) τ(m) ≤ m^{O(1/log log m)}, and all the arguments are ≤ p³. A hit needs C ≥ 1, i.e. 4uB ≤ p + u + B, so UV ≤ p. Then
min(U, V, p/(UV) + 1) ≤ (2p)^{1/3}. Finally, R(p) is a sum of O(log² p) dyadic blocks. ∎

*Remarks.*
* The bound R(p) ≪ p^{1/3+o(1)} is recorded in the repo as a by-product (`reviews/agent-reports/AGENT_REPORT_O178.md`:
  #{(c,f,g) : cfg − c − f = n} ≪ n^{1/3+o(1)}), yet FRONTIER §3 and PARITY_AUDIT Lemma 2.1′ still quote p^{2/5+o(1)}.
* p^{2/5} is Elsholtz–Tao Prop. 1.7 for f_II (checked in `sources/elsholtz-tao-1107.1010.pdf`: "f_II(n) ≪ n^{2/5+O(1/log log n)}").
  (★) is the c = 1 subfamily, for which the divisor bound gives 1/3 directly.
* So the benchmark "beat the divisor bound by cancellation" is p^{1/3}, attained only in the cube block U = V = p/(UV) = p^{1/3}.
  In the balanced block U = V = p^{1/4} the trivial bound is U = p^{1/4}, with no p^{o(1)} loss.

### 3.2 The balanced block is a 2-cycle count; dispersion is empty (Proposition 2; PROVED)

Let U = V be an integer with 1 ≤ U and 2U < p; this holds in the balanced regime. For x ∈ (U, 2U], let f(x) be the unique
y ∈ (U, 2U] with y ≡ −p (mod x), or ⊥ if there is none, and set f(⊥) = ⊥. Uniqueness holds because (U, 2U] has U < x
consecutive integers. f is genuinely partial: for p = 101, U = 3, x = 4, no element of (3, 6] is ≡ −101 (mod 4).
The hypothesis 2U < p is needed: for p = 5, U = 3 we get f(5) = 5.

**Proposition 2.**
(a) For (u, B) ∈ 𝔅(U,U): u | p + B ⟺ B = f(u), and B | p + u ⟺ u = f(B).
(b) 4uB | p + u + B ⟺ f(u) = B, f(B) = u and 4 | n/(uB). The case f(u) = u never occurs. Hence N(U,U) is twice the number of
2-cycles {u, B} of f that satisfy the 4-condition.
(c) Let 𝓛₁ := {(u,B) ∈ 𝔅 : u | p+B} and 𝓛₂ := {(u,B) ∈ 𝔅 : B | p+u}.
* 𝓛₁ is the graph of u ↦ f(u), so it has ≤ 1 element in each row u.
* 𝓛₂ is the transposed graph of B ↦ f(B), so it has ≤ 1 element in each column B.
* The (★) set 𝓛₁ ∩ 𝓛₂ ∩ {4-condition} is a partial matching.

Hence Σ_u (Σ_B a_{u,B})² = Σ_{u,B} a_{u,B}² for any coefficients a supported on 𝓛₁, and Σ_B (Σ_u a_{u,B})² = Σ a² for a
supported on 𝓛₂. A dispersion (Cauchy–Schwarz in the variable in which the relation is a function, then opening the square) has
no off-diagonal term, so it returns N ≤ #𝓛₁ ≤ U.

*Proof.*
(a) This is the definition of f together with uniqueness. By symmetry, B | p + u ⟺ u ≡ −p (mod B).

(b) If u | p + B and B | p + u, then gcd(u, B) | p. Since u, B ≤ 2U < p, gcd(u, B) = 1, and then uB | p + u + B. Next,
4uB | n ⟺ uB | n and 4 | n/(uB). Finally, f(u) = u would mean u | p, which is impossible for 1 < u < p.

(c) Both graph statements are (a). The identity Σ_u (Σ_B a)² = Σ a² holds because each inner sum has ≤ 1 term. The other
direction may fail: for fixed B, several u ∈ (U, 2U] can divide p + B, so 𝓛₁ need not be column-unique. Dispersion is therefore
run in u on 𝓛₁, or in B on 𝓛₂. Either way it has no off-diagonal term. ∎

*Reading (Assessment).* The heuristic for a random partial map gives E[#2-cycles] ≍ Σ_{x,y} 1/(xy) = (log 2)². With the
4-condition and the adm density this is the observed mean ≈ 0.146. The cluster plan's "bilinear dispersion in (u, B), the one
range where both modulus factors vary" has no room in this block *in the Cauchy–Schwarz implementation of (c)*: each
divisibility relation is the graph of a function.

### 3.3 The low-conductor part is a universal constant (Theorem 3; PROVED)

For n ∈ ℤ and d ≥ 1 put A_d(n) := Σ_{(α,β) mod d, d | 4αβ} c_d(n + α + β).

**Lemma 3.1.** If gcd(n, d) = 1, then A_d(n) = μ²(d)·1[d odd].

*Proof.*

*Multiplicativity.* Let d = d₁d₂ with gcd(d₁, d₂) = 1. Under CRT, pairs mod d correspond to pairs of pairs mod d₁ and mod d₂.
The condition d | 4αβ splits into d₁ | 4α₁β₁ and d₂ | 4α₂β₂. Also c_d = c_{d₁}c_{d₂}, and c_{d_i}(m) depends only on m mod d_i.
So A_d = A_{d₁}A_{d₂}.

*Complete sums.* If the condition is vacuous (all pairs allowed), then A = Σ_{α,β} c_d(n+α+β) = d·Σ_{m mod d} c_d(m) = 0 for d > 1.

*ℓ odd, k = 1.* Let d = ℓ. The allowed pairs are those with α ≡ 0 or β ≡ 0 (mod ℓ). By inclusion–exclusion,
A = Σ_β c_ℓ(n+β) + Σ_α c_ℓ(n+α) − c_ℓ(n) = 0 + 0 − μ(ℓ) = 1.

*ℓ odd, k ≥ 2.* Let d = ℓ^k. The allowed pairs fall into three sets.
* α ≡ 0 (mod ℓ^k), β arbitrary: contributes 0 (complete sum in β).
* β ≡ 0 (mod ℓ^k), α arbitrary: contributes 0 likewise. The overlap α ≡ β ≡ 0 contributes c_{ℓ^k}(n) = μ(ℓ^k) = 0, and is
  subtracted.
* The remaining allowed pairs: ℓ | α and ℓ | β. For these, n + α + β is a unit mod ℓ, so c_{ℓ^k} = μ(ℓ^k) = 0.

Hence A = 0.

*ℓ = 2.* Let d = 2^k. For k ≤ 2 the condition 2^k | 4αβ is vacuous, so A = 0. For k ≥ 3 the condition is 2^{k−2} | αβ.
* c_{2^k}(m) = 0 unless 2^{k−1} | m. Since n is odd, a nonzero term needs α + β odd: exactly one of α, β is odd and the other
  is ≡ 0 (mod 2^{k−2}).
* Take α odd and β = 2^{k−2}b with b mod 4. For fixed b, n + α + β runs over all even residues mod 2^k exactly once as α runs
  over the odd residues. Moreover Σ_{m even} c_{2^k}(m) = Σ_{all m} c_{2^k}(m) − Σ_{m odd} c_{2^k}(m) = 0 − 2^{k−1}μ(2^k) = 0.
* The symmetric case (β odd) is the same. So A = 0. ∎

**Theorem 3.** Fix ε > 0. Let D ≤ min(U, V)^{1−ε}, and let n be any integer coprime to every d ≤ D (for example a prime p > D,
or m² with m odd and free of prime factors ≤ D). Write L_D(n) for the d ≤ D part of (2.1):
L_D(n) := Σ_{d ≤ D} Σ_{(u,B): d | 4uB} (W/q)·c_d(n + u + B). Then

  L_D(n) = J·Σ_{d ≤ D, d odd} μ²(d)/d² + O_{ε,A,w}(min(U,V)^{−A}),  J := (1/4)∫w₁(t)dt/t·∫w₂(t)dt/t.

*Proof.*
* Group (u, B) by (α, β) = (u mod d, B mod d). Then L_D = Σ_{d≤D} Σ_{(α,β): d | 4αβ} c_d(n + α + β)·Σ_{u≡α, B≡β (d)} W/(4uB).
* Apply Poisson to g(x) = w₁(x/U)/x, whose transform satisfies ĝ(ξ) ≪_A (U|ξ|)^{−A}. This gives
  Σ_{u≡α (d)} g(u) = d⁻¹[∫w₁(t)/t dt + O_A((d/U)^A)], and likewise for B.
* So the inner double sum is J/d² + O(d⁻²(d/min(U,V))^A).
* By Lemma 3.1 the main term is J·Σ_{d≤D} A_d(n)/d² = J·Σ_{d≤D, d odd} μ²(d)/d².
* The error is ≪ Σ_{d≤D} d²·d·d⁻²(D/min(U,V))^A ≪ D²·min(U,V)^{−εA}. ∎

**Corollary 3.2 (T1 lives at high conductor; PROVED).**
* For m odd with no prime factor ≤ D, n = m² has N_w(m²) = 0. Reason: no f | m² + u with f ≡ −1 (mod 4u), by PARITY_AUDIT
  Lemma 3.2.
* By Thm 3, L_D(m²) = L_D(p) + O(min(U,V)^{−A}) for every prime p > D.
* So the high-conductor part H_D := N_w − L_D equals −J·Σ_{d≤D, d odd} μ²(d)/d² + O(min(U,V)^{−A}) at every such square.
* Consequence. Suppose a bound |H_D(n)| ≤ X is proved uniformly for all n coprime to every d ≤ D. Then the squares force
  X ≥ L_D − O(min^{−A}). So the positivity strategy "N ≥ L_D − X > 0", built on the common leading term, cannot produce a
  margin bounded away from 0. A positivity argument of that shape must use the primality of p, beyond D-roughness, in the
  conductor range > min(U,V)^{1−ε}.
  * This does not restrict other strategies. Such uniform bounds remain usable for upper bounds.
* This concerns the low-conductor *leading term*. The exact low-conductor values at different n differ by
  O(min(U,V)^{−A}); they are not literally equal.

*Values.*
* Σ_{d odd} μ²(d)/d² = ∏_{ℓ>2}(1 + ℓ⁻²) = (15/π²)·(4/5) = 12/π².
* For the sharp balanced block the integral J is (log 2)²/4 + O(1/U), and J·12/π² → 3(log 2)²/π² = 0.1460402. The exact
  class-blind prime density M₀(U) := Σ_{𝔅, adm} 1/φ(4uB) equals 0.145941 (U = 10³), 0.146031 (U = 10⁴) and 0.146036
  (U = 31622) (`z52d_hyperbola_m0.c`).
* EVIDENCE: these are consistent with M₀ → 3(log 2)²/π² at rate O(1/U), but no proof of that identification was written. It is
  not needed: Thm 3 is stated with its own constant.

*Numerical check* (`scripts/z52d_hyperbola_lowcond.py`, `data/z52d/hyperbola/lowcond_check*.json`): U = 1000, D = 40, 12 primes
p ≈ 10¹² in 12 different classes mod 840.
* Smooth bump weights: L₄₀(p) = 0.020082584 at all 12 primes, against the predicted 0.0200825840. The script's J is the discrete
  weight sum Σ W/(4uB), which equals the integral up to a negligible error for smooth W. A 45-digit recomputation by the
  reviewer shows a spread of 1.3·10⁻¹⁰ between primes: nonzero and consistent with the error term.
* Sharp cutoffs: L₄₀ ∈ [0.14433, 0.14542] against 0.14474. Here the prediction uses the discrete sum Σ_{𝔅} 1/(4uB); the
  integral version is 0.14484. The maximal relative deviation is 0.47 %, consistent with the O(D/U) boundary error of sharp
  cutoffs.

### 3.4 The class-conditioned pair-product model is flat in interior blocks (Corollary 4; PROVED)

Fix q ≥ 1 and a unit r mod q. The class-conditioned prime local density of the block is

  M_q(r) := Σ_{(u,B), adm} W·λ_q(u,B; r)/φ(4uB),  λ_q := φ(g)·1[g | r + u + B],  g := gcd(4uB, q).

**Model.** Let L be a common multiple of q, lcm(1, …, D) and every 4uB in the block. Let p be uniform over the units mod L with
p ≡ r (mod q).
* For adm pairs, P(p ≡ −(u+B) mod 4uB) = λ_q/φ(4uB), by φ(lcm)φ(gcd) = φ(a)φ(b) and CRT.
* For non-adm pairs this probability is 0, because −(u+B) is then not a unit mod 4uB.
* Hence M_q(r) = E[N_w(p)] with N_w summed over **all** pairs. This is the "M_F" of the brief.

**Corollary 4.** max_{r, r′} |M_q(r) − M_q(r′)| ≪_{q,ε,w} min(U, V)^{−1+ε}, uniformly in p. So in this pair-product model the
RESIDUE_HARDNESS factor (q | 840·16·11·13) has no main-term effect on a block with min(U, V) → ∞.

*Proof.* Take D = min(U,V)^{1−ε} and write E[N_w] = E[L_D(p)] + E[H_D(p)].

(i) *The low part.* Every p in the model is coprime to every d ≤ D. So Theorem 3 gives L_D(p) = J·Σ_{d≤D, d odd} μ²/d² +
O(min^{−A}) pointwise, and therefore in expectation. This part is independent of r.

(ii) *The high part.* E[H_D] = Σ_{(u,B)} (W/q′) Σ_{d | q′, d > D} E[c_d(p + a)], where q′ = 4uB and a = u + B. Write d = d₁d₂,
with d₁ composed of the primes dividing q and gcd(d₂, q) = 1.
* *Independence.* By CRT, p mod d₂ is a uniform unit independent of p mod d₁. Since c_d = c_{d₁}c_{d₂},
  E[c_d] = E[c_{d₁}]·E[c_{d₂}].
* *The d₂ factor.* E[c_{d₂}(p+a)] = μ(d₂)c_{d₂}(a)/φ(d₂), so |E[c_{d₂}]| ≤ gcd(a, d₂)/φ(d₂).
* *The d₁ factor.* E[c_{d₁}(p+a)] = 0 unless d₁ | q. By multiplicativity it suffices to treat d₁ = ℓ^k with ℓ^j ∥ q,
  k > j ≥ 1.
  * There c_{ℓ^k}(m) = ℓ^k·1[ℓ^k | m] − ℓ^{k−1}·1[ℓ^{k−1} | m].
  * Given p ≡ r (mod ℓ^j), p mod ℓ^k is uniform over its ℓ^{k−j} lifts, all of which are units. So
    P(ℓ^i | p + a) = ℓ^{j−i}·1[ℓ^j | r + a] for i ≥ j.
  * Hence E = ℓ^j·1[…] − ℓ^j·1[…] = 0.
  * If d₁ | q then c_{d₁}(p + a) = c_{d₁}(r + a), so |E[c_{d₁}]| ≤ d₁ ≤ q.
* *Combining.* Because of μ(d₂), only squarefree d₂ contribute. There are ≤ τ(q) choices of d₁ | q, each with
  |c_{d₁}| ≤ q and d₂ > D/q. Hence |E[H_D]| ≤ q·τ(q)·T(D/q), where
  T(X) := Σ_{(u,B)∈𝔅} (W/(4uB)) Σ_{d₂ | 4uB, d₂ > X, d₂ squarefree} gcd(u+B, d₂)/φ(d₂).

(iii) *Tail lemma: for X ≥ 3, T(X) ≪ (log 2UV)⁸·(log log X)/X.*
* *Per pair.* Let d₂ | 4uB be squarefree.
  * An odd prime ℓ dividing both d₂ and u + B divides u or B (since ℓ | 4uB), hence both. So
    gcd(u+B, d₂) ≤ 2·rad(gcd(u,B)) ≤ 2·gcd(u,B).
  * There are ≤ τ(4uB) ≤ 3τ(u)τ(B) such d₂.
  * For d₂ > X, 1/φ(d₂) ≪ (log log X)/X.
  * So the inner sum is ≪ gcd(u,B)τ(u)τ(B)(log log X)/X.
* *Sum over pairs.* Since W ≤ 1, write g = gcd(u,B), u = gu′, B = gB′ and use τ(gu′) ≤ τ(g)τ(u′):
  Σ_{𝔅} gcd(u,B)τ(u)τ(B)/(uB) ≤ Σ_{g≤2U} τ(g)²/g · Σ_{u′≤2U} τ(u′)/u′ · Σ_{B′≤2V} τ(B′)/B′ ≪ (log 2UV)⁸. ∎

*Illustration* (EVIDENCE, `scripts/z52d_hyperbola_cor4check.py`, sharp cutoffs): the relative class spread
max_r M_q(r)/min_r M_q(r) − 1 is 0.080, 0.016 and 0.0028 for q = 7 at U = V = 50, 200 and 800, and 0.095, 0.013 and 0.0021 for
q = 16. This decays roughly like 1/U, as the corollary predicts.

*(Review-2 fix: an earlier outline wrongly lifted prime divisibility to prime powers. Restricting to squarefree d₂, which the
factor μ(d₂) allows, removes the problem, and the crude per-pair bound needs no boundary bookkeeping.)*

With X = D/q and D = min(U,V)^{1−ε}, this gives |E[H_D]| ≪_q (log 2UV)⁸·min(U,V)^{−1+ε}, uniformly in r and in p. Adding (i),
whose error is O(min^{−A}), proves the corollary after renaming ε. ∎

*Scope.* Corollary 4 is a statement about the **pair-product densities** M_q(r). These depend on U, V, q, W and r, but not on
the size of p or on any restriction on C. It is not a statement about counts in an actual window of primes.
* The class dependence of RESIDUE_HARDNESS comes from two sources: its *level term* (its Lemma 1: the level c* = −(4r)⁻¹
  carries q extra cells, which matters when C ranges over fewer than ≍ q values) and its *pair term* (small shifts B or
  u < q).
  * The level term needs a level-conditioned model; M_q does not see it.
  * The pair term is visible in M_q only for blocks with min(U, V) ≲ q, outside the corollary's range.
* The picture "F(p) is confined to the boundary strips min(u, B, C) ≲ q" is therefore a *synthesis*: Cor 4 for interior
  pair-product densities, RESIDUE_HARDNESS's level and pair terms for the strips, and the EVIDENCE of §5. It is not a theorem.
  The strips are single-integer divisor-class counts (fixed u: divisors of p + u; fixed C: divisors of 4Cp + 1).

### 3.5 No free variable at fixed high conductor (Theorem 5; PROVED; the length ratio is an Assessment computation)

**Theorem 5.** Let q = 4uB and K ≥ 1.
(a) #{h mod q : the reduced denominator of h/q is ≤ q/K} ≤ τ(q)·q/K.
(b) For every d, #{(u,B) ∈ 𝔅 : d | 4uB, 4uB ≤ Kd} ≤ Σ_{k≤K} τ(kd/4)·1[4 | kd] ≤ K·max_{m ≤ 4KUV} τ(m) = K·p^{o(1)} (for UV ≤ p).
(c) For fixed (u, B) and d, the sum over a in (2.1) is complete and equals c_d(n). Moreover Σ_{d|q} c_d(n) = q·1[q | n].

*Proof.*
(a) The frequencies with reduced denominator d number φ(d). Writing e = q/d, Σ_{d | q, d ≤ q/K} φ(d) ≤ Σ_{e|q, e≥K} q/e
≤ τ(q)q/K.

(b) If 4uB = kd then uB = kd/4, and an integer has τ divisors.

(c) Standard. ∎

*Reading (scoped).* In the dual (2.1), all but a τ/K fraction of the frequency count sits on conductors d ≥ 4UV/K. In the
balanced block those are ≍ p^{1/2}.
* Each conductor is attached to ≤ K·p^{o(1)} pairs, and these pairs form a set of factorisations of kd, not an interval or a
  lattice. So a Poisson, Weil, Pólya–Vinogradov or large-sieve step *at fixed modulus* has no variable of length
  > K·p^{o(1)} to act on.
* The a-sum is already complete. It evaluates to c_d(n), and only the sum over all d | q returns the original indicator
  1[q | n].
* In this sense the dual of the dominant range, taken conductor by conductor, is the original problem. That is Z1034's "dual at
  least as long as the original" in precise form.

The theorem does **not** exclude cancellation between different conductors, i.e. a method that sums c_d(p + u + B) over (u, B)
and d jointly with d varying. That is the original sum, and no such method is known.

*One off-diagonal conductor block (the A01 plan "track conductor/dual length").* This is an Assessment computation (a
heuristic count). It uses the standard Poisson tail as in Thm 3 and is restricted to coprime splits whose lattice is
populated.
* Take d ~ D with U^{1−ε} ≤ D ≤ 16UV and a split d = d₁d₂ with d₁ | 4u, d₂ | B and gcd(d₁′, d₂) = 1, where
  d₁′ = d₁/gcd(d₁, 4). Assume d₁′ ≤ U and d₂ ≤ V, so that the lattice is populated. Write u = d₁′u′ and B = d₂B′.
  * For adm pairs the odd parts of d₁ and d₂ are automatically coprime.
  * Non-coprime splits, and splits with a spacing exceeding its interval, are left unanalysed. Their congruence windows are
    not independent, and their lattices need not be small.
* The pairs on such a split form a lattice with ≍ (U/d₁′)(V/d₂) ≍ UV/D points.
* The phase e(a(u+B)/d) = e(a d₁′u′/d)·e(a d₂B′/d) is linear in (u′, B′). Poisson in u′ (length U/d₁′) makes the u′-sum
  negligible unless ‖a d₁′/d‖ ≲ p^ε d₁′/U. That puts a mod (d/d₁′) in a window of ≍ p^ε d/U residues. Likewise a mod (d/d₂)
  must lie in a window of ≍ p^ε d/V residues.
* The two moduli d/d₁′ and d/d₂ have gcd g := gcd(d₁, 4) ≤ 4. By generalised CRT (with a compatibility condition mod g, a
  bounded factor), that leaves ≍ (D/U)(D/V) = D²/(UV) frequencies a per conductor, up to p^ε.
* So dual/original ≍ D³/(UV)². The dual is shorter only for D < (UV)^{2/3} = p^{1/3} (balanced block). By (a), that range
  carries ≤ (UV)^{2/3}·p^{o(1)}/(UV) = p^{−1/6+o(1)} of the frequencies. Below U^{1−ε} the dual is empty except for the main term
  (Thm 3).

### 3.6 The ψ / exponential-sum route (Theorem 6)

Let Δ_H := max_{1≤h≤H} |S_h| with S_h = Σ_{𝔅} e(hF) as in (E3).

**Theorem 6.**
(a) (PROVED; uses Selberg's majorant.) For 1 ≤ H ≤ 4UV, N(U,V) ≤ UV/(H+1) + 1/16 + 2.5·Δ_H.

(b) (PROVED.) For H + 1 ≥ 2UV, Σ_{1≤|h|≤H} |S_h|² ≥ (H+1)UV/2. Hence Δ_H ≥ (UV)^{1/2}/2.

(c) (PROVED; immediate.)
* Suppose Δ_H ≤ (UV)^{1/2−η} for some H ≥ (UV)^{1/2+η}. Then (a) gives N ≪ (UV)^{1/2−η}; in the balanced block this is
  N ≪ p^{1/4−η/2}, a power saving.
* Square-root bounds Δ_H ≪ (UV)^{1/2} give only N ≪ (UV)^{1/2}. This is ≥ min(U, V), so it never beats Thm 1. In the balanced
  block it equals the trivial bound U.
* The "asymptotic" version of the route takes H ≥ 2UV, so that the majorant's main term UV/(H+1) is ≤ 1/2, i.e. comparable to
  M. By (b), that version provably outputs ≥ 1.25·(UV)^{1/2}.

(d) (EVIDENCE.) At p = 10¹² + 39, U = V = 1000, sharp sums (`scripts/z52d_hyperbola_expsum.c`,
`data/z52d/hyperbola/expsum_p1e12p39.tsv`):
* for 1 ≤ h ≤ 2000, |S_h|/U has rms 1.77, median 1.43 and max 5.77;
* for h = 7919k (k ≤ 2000, up to 1.58·10⁷ ≈ the full needed range 16UV), rms 1.42 and max 4.45.

So S_h is square-root size, not beyond. The best bound obtained from (a) over H ≤ 2000 is 13 448 (at H = 508), against the
trivial U = 1000.

(e) (B-process dual length. Assessment: a full-box geometric count. The Jacobian is PROVED; negligibility outside the image
and size inside are standard and cited, but the uniform 2D argument is not written out.)
* The 2D Poisson dual of the smoothed S_h is Σ_{(m,n)} I(m,n), with I(m,n) = ∫∫W·e(hF − mx − ny).
* By non-stationary phase (Blomer–Khan–Young, Duke 162 (2013), Lemma 8.1, checked in arXiv:1203.2573: I ≪_A (β−α)X[(QR/√Y)^{−A}
  + (RU)^{−A}]), I is negligible unless (m, n) lies within p^ε(1/min(U,V) + (hp/(UV))^{1/2}/min(U,V)) of
  Γ_h := h∇F(supp W). In the balanced block this distance is p^ε√h.
* The lemma is one-dimensional. In 2D it is applied in one variable after a stationary-phase reduction in the other
  (BKY Prop. 8.2); this step is standard and is not written out here.
* The exact Hessian determinant is (3p² + 4p(u+B) + 4uB)/(16u⁴B⁴) = 3p²/(16u⁴B⁴)·(1 + O((U+V)/p)). The map ∇F is injective
  on the box.
* For W ≈ the indicator of the full box (supp W = [1+η, 2−η]², η → 0), #(Γ_h ∩ ℤ²) ≈ h²·(3p²/16)·(7/(24U³))·(7/(24V³)) =
  κ₀h²ρ²·UV, with κ₀ = 147/9216 = 0.01595.
  * A general smooth W gives ∫∫_{supp W} h²|det| instead, which is smaller for smaller supports.
  * The lattice-point asymptotic needs the usual area ≫ perimeter·(neighbourhood width) regime.
* The geometric amplitude at interior points is 1/(h√det) ∈ [2.31, 36.95]/(hρ), multiplied by the weight W at the stationary
  point; it is not uniformly bounded below near the edge of supp W.
* So, for the full box, the dual is shorter than the original (UV terms) roughly when h < κ₀^{−1/2}/ρ = 7.92/ρ.
  * Resolving (2.3) needs H ≍ UV, so the fraction of needed frequencies with a shorter dual is ≍ 1/(ρUV) ≍ 1/C̄, where
    C̄ = p/(4UV) is the block's typical level.
  * In the balanced block (ρ = 1) the dual is shorter only for h ≲ 7.
* This is a length count, not an impossibility theorem. A longer dual can still have cancellation.

*Proof of (a).*
* Selberg's majorant S⁺ of 1_{[−δ,δ]} (mod 1) of degree H satisfies S⁺ ≥ 1_{[−δ,δ]}, Ŝ⁺(0) = 2δ + 1/(H+1), and
  |Ŝ⁺(h)| ≤ 1/(H+1) + min(2δ, 1/(π|h|)). (Montgomery, *Ten Lectures*, CBMS 84, Ch. 1; Vaaler, BAMS 12 (1985); statement checked
  as quoted in MathOverflow 453655.)
* By (2.3) with δ = 1/(32UV): N ≤ Σ_{𝔅} S⁺(F) = Σ_{|h|≤H} Ŝ⁺(h)S_h ≤ (2δ + 1/(H+1))(UV + 2HΔ_H).
* Here 2δ·UV = 1/16, 2δ·2H ≤ H/(8UV) ≤ 1/2, and 2H/(H+1) ≤ 2. ∎

*Proof of (b).*
* With the Fejér kernel K_H(θ) = (H+1)⁻¹|Σ_{j=0}^{H} e(jθ)|² ≥ 0 and K_H(0) = H + 1:
  Σ_{|h|≤H}(1 − |h|/(H+1))|S_h|² = Σ_{x,x′∈𝔅} K_H(F(x) − F(x′)) ≥ (H+1)UV.
* Subtract the h = 0 term (UV)² and use that the weights are ≤ 1. Then Σ_{1≤|h|≤H}|S_h|² ≥ (H+1)UV − (UV)² ≥ (H+1)UV/2.
* There are 2H terms, so Δ_H² ≥ (H+1)UV/(4H). ∎

*What (b) and (c) do not show.*
* For (UV)^{1/2+η} ≤ H < 2UV no lower bound on Δ_H is proved: a perfectly equidistributed phase could have S_h = 0 there.
  (d) shows that large |S_h| do occur in that segment at 10¹².
* Theorem 6 closes only the implementation that bounds the Fourier side Σ Ŝ⁺(h)S_h by 2H·Δ_H. A method that exploits
  cancellation *between* different h, or a different weighted estimate, is not excluded.

### 3.7 Divisor / Voronoi form and the members' routes

* **Z1034 (Voronoi).** In the divisor form, Σ_C #{x | 4Cp + 1 : x ≡ −1 (mod 4C)}, each additive modulus 4C belongs to exactly
  **one** integer n = 4Cp + 1.
  * A Voronoi formula for Σ_n τ(n)e(an/c)g(n) acts at a fixed modulus c on a long n-sum. Here that n-sum has length 1.
  * The alternative fixes the modulus 4p and sums over n ≡ 1 (mod 4p) (Selberg–Hooley/FKM, PARITY_AUDIT row B6). Then the class
    modulus (n − 1)/p varies with n.
  * Either way the one-step transform at fixed modulus has nothing to shorten. With Thm 5 this is the scoped no-go.
    Recommended: mark Z1034's first step as executed, with the outcome "one-step dualization is self-dual at fixed
    conductor". This is not a refutation of all cancellation.
* **Z1855 (pieces ⌈p/m⌉ = q).** These are the pair form (q = B, r = u = qm − p).
  * For m ≍ p^{3/4}, |d(p/m)/dm| = p/m² ≍ p^{−1/2}, so a piece {m : ⌈p/m⌉ = q} has length ≍ p/q² ≍ p^{1/2}: the pieces are
    long.
  * But the balanced block needs u = qm − p ∈ (U, 2U]. That cuts each piece q = B to a sub-interval of length U/q ≤ 1, which is
    the single candidate of Prop 2.
  * So in this block van der Corput on a piece acts on ≤ 1 term. Longer piece segments correspond to other blocks (small B,
    large u). Whether the van der Corput route works there is not decided here.
* **Z2958 / Z3149 (d-indexed trial form, k-reparametrisation).** This is (E5). In the balanced block it is the self-dual 𝓗-box.
* **Z0211 (modular hyperbola).** Same as (E5). The Weil error p^{1/2+o(1)} already exceeds the box main term ≍ p^{1/2}/8 before
  the height condition is imposed.
* **Z1480 (horizontal Eisenstein sums).** These are Thm 5 in spectral form: the level 4C and the argument 4Cp + 1 are in
  bijection, so a family sum over levels has one coefficient per level.
* **Z2997 (EMM).** Not affected by these theorems. It remains closed for the reasons given in its avenue row (degenerate
  quadric; counts are of power size).

### 3.8 Ledger for the balanced block (u, B ≍ p^{1/4}, C ≍ p^{1/2}, mean ≈ 0.146)

| form | original terms | dual / frequencies | conductor | terms per conductor | verdict |
|---|---|---|---|---|---|
| pair (E1) | UV ≈ p^{1/2} pairs | Σ 4uB ≈ 9p frequencies | ≥ 4UV/K for all but τ/K | ≤ K·p^{o(1)} | self-dual at fixed conductor (Thm 5) |
| trial (E2) | ≈ 0.19 p^{3/4} pairs (u, C) | Σ m ≈ p^{3/2} | ≍ p^{3/4} | ≤ τ | worse than (E1) |
| divisor / Voronoi | one n per modulus 4C | — | 4C ≍ p^{1/2} | 1 | nothing to sum (§3.7) |
| ψ-form (E3) + B-process | UV | ≈ κ₀h²UV per h (full box), h ≤ 16UV | — | — | shorter only for h ≲ 7 (Thm 6e, Assessment) |
| ψ-form + Erdős–Turán with max-bound | — | needs Δ_H ≤ (UV)^{1/2−η} | — | — | square-root gives the trivial bound (Thm 6) |
| hyperbola 𝓗 mod 4p (E5) | box area ≍ p^{3/2}, ≈ p^{1/2}/8 points | (4p)²/(XY) ≍ p^{1/2} | 4p | — | self-dual box; Weil error > main term |
| dispersion in (u, B) | graph of f | — | — | ≤ 1 per row (𝓛₁), ≤ 1 per column (𝓛₂) | empty (Prop 2) |
| low conductor d ≤ U^{1−ε} | — | zero frequency only | ≤ U^{1−ε} | ≍ UV/d | constant up to O(U^{−A}) (Thm 3) |

## 4. What survives

* **(R0) Cancellation across conductors or across frequencies.** This is not excluded by any theorem here, and no method for
  it is known.
* **(R1) Beyond-square-root cancellation on an initial frequency segment.** The statement is Δ_H ≤ (UV)^{1/2−η} for some
  H ≥ (UV)^{1/2+η}, where S_h = Σ_{u,B≍p^{1/4}} e(h(p+u+B)/(4uB)).
  * By Thm 6(a) this is *sufficient* for a power saving. It is not equivalent to the count.
  * No method gives beyond-square-root cancellation for an individual smooth 2D exponential sum. The data at 10¹² show
    |S_h| ≈ 1.4–1.8·(UV)^{1/2} (EVIDENCE against R1 at that scale).
  * Assessment: implausible.
* **(R2) Pair correlation of the remainder map.** Show that the partial map f (x ↦ (−p mod x) lifted to (U, 2U]) has
  ≪ U^{1−η} 2-cycles {u, B} satisfying the 4-condition 4 | (p+u+B)/(uB).
  * By Prop 2 this is *equivalent* to an upper bound N(U,U) ≪ U^{1−η}. (Without the 4-condition it is a different count; see
    the p = 17 example in (E4).)
  * It is a second-order statement about p mod x jointly with p mod f(x). The first-order statement, equidistribution of p/x
    mod 1 for x ≍ p^{1/4}, is a standard van der Corput problem and says nothing about 2-cycles. Open; no tool.
* **(R3) Counting (not cancellation).** An upper bound N(U,U) ≪ U^{1−η}, e.g. by the determinant method on the cubic surface
  4uBC − u − B = p, would be a "power saving on one block". It was not attempted here. It is an upper bound, so it is worth
  nothing for ES (rank_O's aside).
* **(R4) Why no single block can carry ES (EVIDENCE + Assessment).** P(N_block = 0) ≈ e^{−M/2} ≈ 0.93 (EVIDENCE §5: 92.8 %).
  Even the whole interior u, B, C ≥ 1000 is empty for 9.8 % of primes near 10¹².
  * So an existence argument that is to work in the computed range cannot rely on the interior alone. It must also use the
    boundary strips min(u, B, C) < T₀, which are single-integer divisor-class counts.
  * Asymptotically the interior's share of the log-area is 1/16 and its mean grows ∝ (log p)². Under swap-Poisson its emptiness
    is a finite-range phenomenon, so this does not prove that an eventual proof must use the strips.

## 5. The falsifier (EVIDENCE)

**Setup.** The windows are:
* 10⁵ consecutive primes from 10¹² + 39 to 1 000 002 761 677, with U = T₀ = 1000;
* 2·10⁴ consecutive primes from 10⁸ + 7, with U = T₀ = 100;
* 2·10⁴ consecutive primes from 10¹⁶ + 61 (U = 10⁴, balanced block only);
* 2·10⁴ consecutive primes from 10¹⁸ + 3 (U = 31622, balanced block only).

All primes are included; analyses involving F use p ≡ 1 (4), because F is defined there.

Per prime we compute:
* N_bal, the balanced block;
* T = Σ_{𝔅,adm} χ_{−4uB}(p)/φ(4uB), the Brauer character part (M_BM = M₀ − T);
* M_Q, the exact class-conditioned density for Q = 240240 = 2⁴·3·5·7·11·13;
* N_int, the interior region u, B, C ≥ T₀;
* the boundary strips S_u (u ≤ 16) and S_C (C ≤ 16);
* the full R(p), for the 10⁸ and 10¹² windows.

The program is `scripts/z52d_hyperbola_falsifier.c`.
* It agrees exactly with a sympy brute force on all quantities at 52 primes, 40 near 2·10⁴ and 12 near 10⁵, with different U
  and T₀.
* T and M_Q were checked independently at 5 primes.
* M₀ comes from `z52d_hyperbola_m0.c` (exact) and M₀_int from `z52d_hyperbola_m0int.c` (exact, at the window midpoint; the
  window's relative width is 3·10⁻⁶).
* Statistics: `scripts/z52d_hyperbola_analyze.py` → `data/z52d/hyperbola/falsifier_stats.json`; per-prime rows are in
  `data/z52d/hyperbola/out_*.tsv.gz`.

**Balanced block.**

| window | primes | mean N | M₀ | z(mean) | var/(2M₀) | hist N = 0/2/4/6 | swap-Poisson GOF p: rate M₀ (df 2) / fitted (df 1) |
|---|---|---|---|---|---|---|---|
| 10⁸ | 20 000 | 0.1416 | 0.14513 | −0.94 | 0.969 | 18629/1326/45/0 | 0.61 / 0.65 |
| 10¹² | 100 000 | 0.14986 | 0.14594 | +2.26 | 1.029 | 92784/6950/255/11 | 0.081 / 0.94 |
| 10¹⁶ | 20 000 | 0.1444 | 0.14603 | −0.43 | 0.983 | 18602/1354/42/2 | 0.63 / 0.39 |
| 10¹⁸ | 20 000 | 0.1381 | 0.14604 | −2.12 | 0.961 | 18676/1269/53/2 | 0.039 / 0.13 |

GOF bins are N/2 = 0, 1, ≥ 2; the sparse tail is pooled (review fix).

* N is always even (u ↔ B).
* Plain Poisson N ~ Poi(M) is rejected (χ² ≈ 10⁴ in every window).
* The four mean z-scores have χ²₄ = 10.7 (p ≈ 0.03). This is a mild window-to-window excess of the mean with no trend in p. The
  shape, with the rate fitted, is swap-Poisson in every window (p ≥ 0.13).
* No p-growing structure appears from 10⁸ to 10¹⁸.

**Class-aware predictors of the block error E = N_bal − M₀ (10¹² window; the 10⁸ window is given in brackets).**

| predictor | size | corr with E | reading |
|---|---|---|---|
| log F(p), RESIDUE_HARDNESS (★) factor | sd 0.109 | r = +0.001, t = 0.27 [10⁸: −0.021, t = −2.1] | none |
| −T, Brauer term | sd 5.2·10⁻⁴, max 0.019 | r = 0.005, t = 1.5 | negligible |
| M_Q − M₀, Q = 240240 ≫ U | sd 0.0117 | r = 0.024, t = 7.6 [10⁸: 0.136] | small, real |
| class means mod 3, 5, 7, 8, 16 | — | χ²-flat p = 0.91, 0.81, 0.10, 0.57, 0.90 | flat |

* The M_Q signal is a **high-conductor** effect, as Cor 4 predicts. Q exceeds U, so knowing p mod Q partially reveals
  p mod 4uB when gcd(4uB, Q) is large. It is larger at 10⁸, where Q ≫ U² and the block is tiny.
* M_Q improves the swap-Poisson log-likelihood by 26 nats at 10¹², but it explains only r² = 0.06 % of the variance.

**Interior versus boundary (10¹², p ≡ 1 (4), 49 984 primes; T₀ = 1000 = ⌊p^{1/4}⌋).**

| quantity | mean | var/mean | corr(·, log F) | log-linear c in log(Y+1) ~ c·log F | mod-7 class means (class 1 … 6, relative) | 840: class 1, Mordell squares |
|---|---|---|---|---|---|---|
| N_int (u, B, C ≥ 1000) | 4.657 (M₀_int 4.635) | 2.01 | −0.003 (t = −0.7) | −0.02 ± 0.03 | 0.997, 1.004, 0.999, 1.001, 1.001, 0.998 (χ² 0.55/5) | 0.976, 0.987 |
| boundary R − N_int | 117.06 | — | +0.43 (t = 106) | 1.00 ± 0.01 | 0.9403, 0.9425, 0.9655, 0.9796, 1.0709, 1.1013 (χ² 2546/5) | 0.827, 0.857 |
| S_u (u ≤ 16) | 28.13 | — | +0.45 (t = 111) | — | χ² 2514/5 | 0.617, 0.695 |
| S_C (C ≤ 16) | 28.42 | — | +0.32 (t = 76) | — | χ² 2419/5 | 0.834, 0.775 |
| R(p) | 121.72 | — | +0.43 (t = 105) | 0.96 ± 0.01 | 0.9425, 0.9448, 0.9668, 0.9804, 1.0682, 1.0973 | 0.833, 0.862 |

(The var/mean entry for N_int and the interior-emptiness figures below use all 10⁵ primes. The 840 columns give relative class
means.)

* RESIDUE_HARDNESS's mod-7 (★) factors at 10⁶ are 0.902 (class 1) and 1.174 (class 6). Rescaled by L₀/L = 14.16/27.63 to 10¹²
  they predict 0.950 and 1.089; R gives 0.943 and 1.097.
* At 10⁸ (T₀ = 100) the same picture holds: N_int has c = 0.09 ± 0.04 and the boundary has c = 0.98 ± 0.02. The small interior
  residue there is consistent with the O(q/T₀) edge effect.
* Interior emptiness: N_int = 0 for 9 798 of 10⁵ primes (9.80 %). Swap-Poisson e^{−M₀_int/2} predicts 9.85 %. At 10⁸ the values
  are 45.0 % and 45.2 %.
* The interior holds 3.8 % of R at 10¹².

**Reading (Assessment).** The falsifier does not refute C1's premise that the block error is small: it behaves as
swap-Poisson noise of size √M. It does sharpen what "class-aware" can mean.
* The class information that predicts hardness, F(p), is absent from the interior and from the balanced block. In theory this
  holds for the low-conductor part (Thm 3) and for the product model (Cor 4). In the data, c = −0.02 ± 0.03 in the interior
  against 1.00 ± 0.01 in the boundary.
* Empirically, F lives in the boundary strips, where there is no averaging variable.
* A class-filtered cancellation in the interior would therefore have to extract structure from the high-conductor part, which
  carries the T1 vanishing (Cor 3.2) and the actual fluctuations. There, the one-step implementations are closed (Thms 5–6),
  but cancellation across conductors or frequencies is not excluded.

## 6. Verdict for the cluster

**Narrowed.**

* **Closed (scoped theorems).** Each item below is closed as an *implementation*. None is an impossibility theorem for
  cancellation in general.
  * One-step dualization at fixed conductor: Poisson, Voronoi or Ramanujan in (u, B), (u, C) or the divisor form. At conductor
    ≥ q/K there are ≤ K·p^{o(1)} terms; the complete a-sum gives c_d(n), and summing over d | q gives back 1[q | n] (Thm 5,
    §3.7). The B-process
    count (Thm 6e, Assessment) shows the 2D dual is longer than the original except for h ≲ 7.9/ρ.
  * Dispersion by Cauchy–Schwarz in the function variable in the balanced block (Prop 2).
  * The majorant route with max_h |S_h| input: square-root input gives ≍ (UV)^{1/2} ≥ min(U, V), which never beats the
    elementary bound in any block, and for H ≥ 2UV a square-root floor is proved (Thm 6b, c). Beyond-square-root input on a
    short segment (R1) is not excluded.
  * A main term built from the low-conductor part or the class-conditioned product model. It is p-independent up to
    O(min^{−A}) and agrees at rough squares (Thm 3, Cor 3.2), and the product model is class-flat (Cor 4). The data agree.
* **Vacuous.** A01's p^{2/5−δ} block target, since every block is ≪ p^{1/3+o(1)} (Thm 1).
* **Survives.**
  * (R0) cancellation across conductors or across frequencies; no method known.
  * (R1) beyond-square-root bounds for S_h on h ≤ (UV)^{1/2+η}. This is sufficient, not equivalent, and the evidence is
    against it at 10¹².
  * (R2) the 2-cycle bound with the 4-condition, which is equivalent to the balanced-block count.
* **Untested side theorem.** (R3) a determinant-method upper bound. It is worth nothing for ES.

Members:
* Z1034, Z0211, Z2958 and Z3149: mark the proposed first step as executed. The outcome is that one-step dualization is
  self-dual at fixed conductor, and the hyperbola box is at the self-dual/Weil threshold. This is "covered by
  Z52D_HYPERBOLA", not refuted.
* Z1855: its pieces are long (≍ p^{1/2}), but within the balanced block each piece contributes ≤ 1 term. The route is
  undecided in unbalanced blocks.
* Z1480: the spectral restatement of Thm 5 (one coefficient per level).
* Z2997: unaffected, and already closed.

## 7. Proposed FRONTIER §7 text (do not edit FRONTIER here)

Replace §7.1 by:

> 1. **Cancellation on the height-tied hyperbola — rescoped (z52d, `Z52D_HYPERBOLA.md`).**
>    * The elementary benchmark is p^{1/3+o(1)}, not p^{2/5} (Thm 1; AGENT_REPORT_O178). Blocks satisfy
>      N(U,V) ≤ p^{o(1)}min(U, V, p/(UV) + 1), and the balanced block u, B ≍ p^{1/4} satisfies N ≤ p^{1/4}.
>    * PROVED: in the additive-character expansion of any block, the conductor ≤ min(U,V)^{1−ε} part equals a universal constant
>      up to O(min(U,V)^{−A}) at every prime and every rough odd square. Since (★) vanishes at squares, a uniform bound on the
>      high-conductor remainder valid for all rough n cannot prove positivity with a margin from the common leading term. Such
>      an argument must use primality at conductor > min(U,V)^{1−ε}.
>    * At conductor ≥ q/K each conductor carries ≤ K·p^{o(1)} pairs, and the a-sum is complete (it gives c_d(n)). So one-step
>      dualization at fixed conductor has nothing to act on.
>    * The Erdős–Turán/Vaaler route with max-bounds needs beyond-square-root cancellation of S_h = Σ e(h(p+u+B)/(4uB)) on
>      h ≤ (UV)^{1/2+η}. Square-root bounds give exactly the trivial bound.
>    * The balanced block is a count of the 2-cycles of the remainder map x ↦ (−p mod x) on (U, 2U] that satisfy the
>      4-condition. Dispersion in the function variable is empty.
>    * EVIDENCE (10⁵ primes at 10¹²): block errors are swap-Poisson, and |S_h| is square-root size. The interior
>      (u, B, C ≥ p^{1/4}) is class-blind (log-F coefficient −0.02 ± 0.03, against 1.00 ± 0.01 for the boundary strips) and is
>      empty for 9.8 % of primes.
>    * What remains open is cancellation across conductors or frequencies, or a 2-cycle bound. No method is known for either.
>      *Why it stays listed:* it is the exact form of B2 at its self-dual scale. It should no longer be called "the only lead
>      not ruled out"; it is a lead whose standard implementations are ruled out.

In FRONTIER §3 ("Tied modulus") and in PARITY_AUDIT Lemma 2.1′, replace "|E(p)| ≪ p^{2/5+o(1)}" by "≪ p^{1/3+o(1)}
(elementary; ET's p^{2/5} is for full Type II)". In §2.2, after the RESIDUE_HARDNESS bullet, add:

> In the product local model, interior blocks are class-flat (Z52D_HYPERBOLA Cor 4). Empirically, the factor lives in the
> boundary strips min(u, B, C) ≲ q.

## 8. Bottom line

The cluster's first lemma asked for a class-aware power saving by cancellation on one balanced block at fixed p. That block
sits at the self-dual scale of every standard transform:
* the dominant conductors of the additive-character dual carry p^{o(1)} pairs each, and the complete a-sum at each conductor
  only gives c_d(n);
* the Voronoi form has one integer per modulus;
* the modular-hyperbola box is at Weil's area-p^{3/2} threshold;
* the 2D B-process shortens only about seven frequencies;
* square-root (Weil-quality) bounds fed through Erdős–Turán reproduce exactly the trivial bound p^{1/4};
* dispersion in the function variable is empty.

The low-conductor part of the expansion is the same, up to a negligible error, at primes and at rough squares. So whatever
distinguishes primes must come from the high-conductor part. The class factor F(p) is absent from the interior both in the
product model and in the data; it lives in the boundary strips. A01's numerical target was vacuous, because the elementary
bound is p^{1/3}, not p^{2/5}.

Not excluded: cancellation across conductors or frequencies, for which no method is known, and an equivalent 2-cycle bound. At
10¹² the relevant sums are square-root size. §7.1 should be rescoped. ES remains open.

## 9. Reproduction

```
ulimit -v 8000000; mkdir -p /tmp/hyp && cd /tmp/hyp
gcc -O2 -march=native -o fals  $REPO/scripts/z52d_hyperbola_falsifier.c -lm
gcc -O2 -fopenmp -o m0    $REPO/scripts/z52d_hyperbola_m0.c
gcc -O2 -fopenmp -o m0int $REPO/scripts/z52d_hyperbola_m0int.c
gcc -O2 -fopenmp -o expsum $REPO/scripts/z52d_hyperbola_expsum.c -lm
# prime lists: consecutive primes after x (sympy nextprime)
uv run --with sympy python -c "from sympy import nextprime;p=10**12
for _ in range(100000): p=nextprime(p); print(p)" > p12.txt          # likewise 1e8, 1e16, 1e18 with 20000
split -n l/12 -d p12.txt c_ && for f in c_*; do timeout 7200 ./fals 1000 1000 1 < $f > o_$f & done; wait; cat o_c_* > out_1e12.tsv   # ~45 min on 12 cores
timeout 7200 ./fals 100 100 1 < p_1e8.txt > out_1e8.tsv
timeout 7200 ./fals 10000 10000 0 1 < p_1e16.txt > out_1e16.tsv; timeout 7200 ./fals 31622 31622 0 1 < p_1e18.txt > out_1e18.tsv
for U in 100 1000 10000 31622; do ./m0 $U; done; ./m0int 100184000 100; ./m0int 1000001380000 1000
OMP_NUM_THREADS=4 ./expsum 1000000000039 1000 2000 7919 2000 > expsum_p1e12p39.tsv
cd $REPO && uv run --with numpy --with scipy python scripts/z52d_hyperbola_analyze.py      # reads data/z52d/hyperbola/out_*.tsv.gz
uv run --with numpy --with sympy python scripts/z52d_hyperbola_lowcond.py [smooth]
```

## 10. Review log

**Hostile review 1** (deep-mode subagent, 2026-11-01). It independently re-verified:
* Lemma 3.1 by exact brute force, 575 tests covering every d ≤ 60;
* the falsifier program against direct enumeration, 144 small cases, and T/M_Q in 15 cases;
* all 160 000 primes' statistics, M₀ and M₀_int;
* the Jacobian and constants.

It found 2 CRITICAL, 6 MAJOR and 4 MINOR issues, all repaired:
* CRITICAL: the verdict over-claimed. Thms 5/6 and Prop 2 close specific *implementations*, not cancellation in general; R1 is
  sufficient, not equivalent; R2 must keep the 4-condition; finite-window interior emptiness does not force an eventual proof
  into the strips. → §0, §4, §6, §7 and §8 rescoped; (R0) added.
* CRITICAL: Thm 3 was over-read as exact equality. The low-conductor values differ by O(min^{−A}); the reviewer measured a spread
  of 1.3·10⁻¹⁰ at 45 digits. → Cor 3.2 restated with error terms, as a statement about bounds valid for all rough n; "conductor
  ≍ UV" weakened to "> min(U,V)^{1−ε}".
* MAJOR: Cor 4's proof mixed admissible-pair and all-pair sums. → Rewritten with an explicit global unit model (non-adm pairs
  have probability 0), the d₁ | q vanishing lemma, and gcd-weighted tail bounds (tail lemma in outline). Scoped to the product
  model.
* MAJOR: the B-process count used the full box but supp W in its definition, and asserted amplitudes without the weight. →
  Relabelled Assessment (full-box count); weight and asymptotic regime stated; not used as an impossibility argument.
* MAJOR: Z1855 derivative and piece length were reversed (pieces have length ≍ p^{1/2}). → Corrected; the balanced-block
  restriction cuts each piece to ≤ 1 term, and unbalanced blocks are left undecided.
* MAJOR: f partial, fixed points when 2U ≥ p. → Hypotheses integer U ≥ 1 and 2U < p, f(⊥) = ⊥, examples added.
* MAJOR: the §3.5 CRT needed coprime splits. → Restricted to coprime, populated splits; labelled a heuristic count.
* MAJOR: fitted-rate GOF used the wrong df and sparse bins. → Bins pooled (0, 1, ≥ 2), df 2 for fixed and 1 for fitted;
  p-values updated.
* MINOR: Vaaler best bound 15 745 → 13 448 (coefficient 2.5); 3(log 2)²/π² = 0.1460402; the sharp check's discrete-vs-integral
  prediction distinguished; the interior/boundary table's means recomputed on p ≡ 1 (4); the E5 rectangle corrected for
  unbalanced blocks.

The reviewer confirmed as correct: Lemma 0, Thm 1 and the p^{2/5} → p^{1/3} correction, Lemma 3.1, Thm 3 itself,
(2.2)/(2.3), Thm 5, and Thm 6(a)/(b).

**Hostile review 2** (deep-mode subagent, second pass on the repairs). It found 1 CRITICAL, 4 MAJOR and 3 MINOR issues, all
repaired:
* CRITICAL: Cor 4's tail outline lifted e | u + B, e | 4uB to e | u, e | B for prime powers. The counterexample is u = 12,
  B = 15, e = 9. → The tail lemma was re-proved using μ(d₂) (squarefree d₂ only) and a crude per-pair bound. The corollary
  improves to ≪ min(U,V)^{−1+ε}, uniformly in p, with no boundary bookkeeping.
* MAJOR: the boundary terms were unproved and p^ε was not uniform. → Eliminated by the new proof.
* MAJOR: Cor 3.2's "any bound is useless / any proof must use primality" over-reached. → Restricted to the positivity strategy
  "leading term minus a uniform remainder bound" with a margin; upper-bound uses noted.
* MAJOR: "max-bound implementation closed" conflicted with R1. → Now distinguished: square-root max input (any H) and
  max-bounds with H ≥ 2UV are closed; the short-segment beyond-square-root case (R1) stays open. Prop 2's reading is scoped to
  the Cauchy–Schwarz implementation.
* MAJOR: the pair-product model cannot see C-restrictions. → The scope paragraph was rewritten. Boundary confinement of F is
  now a synthesis (Cor 4 + RESIDUE_HARDNESS level/pair terms + EVIDENCE), not a consequence of Cor 4.
* MINOR: the §3.5 CRT moduli share gcd ≤ 4 (bounded compatibility factor), and excluded splits are "unanalysed", not
  "O(1) points". The complete a-sum gives c_d(n), and only the sum over d | q gives the indicator; the prose was fixed
  throughout. The Brauer-term numbers are attributed to the 10¹² window.

The reviewer confirmed as correct: the global unit model, the vanishing of E[c_{ℓ^k}] for k > j ≥ 1 (5 450 small cases
checked), the d₁/d₂ independence, Prop 2's hypotheses and examples, the Z1855 fix, the B-process relabelling, and all §5
numbers (best Vaaler bound 13 448.184 at H = 508).

