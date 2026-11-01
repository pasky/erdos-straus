# Z53_HYPSUMPROD — depth lane HYPSUMPROD (FRONTIER §7.1): sum-product / incidence / sieve tools on the tied hyperbola, block-shape map

ES is OPEN. Nothing here proves or disproves it, and nothing here is progress on the *existence* of a solution of 4/p.
Labels: PROVED / CONDITIONAL / CERTIFIED / EVIDENCE / CONJECTURE / Assessment. Internal results are internally reviewed only
(not refereed).

Brief: `z52bbriefs/z53_depth.md`, lane kickoff `z52bbriefs/z53_lanes.md` §HYPSUMPROD. Scripts `scripts/z53_hypsumprod_*`,
data `data/z53/hypsumprod/` (≈ 0.2 MB). Checkpoint 1 was commit 5ab7243d.

## 0. Summary

Fix n ≥ 2 (the case of interest is a prime p ≡ 1 (mod 24)). R(n) = #{(u, B, C) ∈ ℕ³ : 4uBC − u − B = n} is the (★) count;
E(p) = R(p) − M(p) with M(p) ≍ log²p. Since R ≥ 0, a pointwise bound |E(p)| ≪ p^θ (θ > 0) is the same as R(p) ≪ p^θ: the §7.1
benchmark question "beat the elementary p^{1/3+o(1)}" is a pure *counting* problem on the tied hyperbola.

1. **Theorem 1 (PROVED; the main new result). R(n) ≪ n^{1/3 − 1/225}(log n)² for all n ≥ 2**, uniformly in n. Hence
   |E(p)| ≪ p^{1/3−1/225}(log p)², the first power saving over the elementary benchmark p^{1/3+o(1)} (Z52D Thm 1). The
   extremal (cube) block u, B, C ≍ n^{1/3} has N ≪ n^{8/25+o(1)}.
   * Mechanism: near the cube, u and B are the roots of z² − sz + k with s = u + B = 4Ck − n and k = uB, so a (★) triple
     is exactly a point (C, k) of the thin strip 𝒜 = {(C, k) : 4Ck − n ∈ s-range} at which **f(C, k) = (4Ck − n)² − 4k is a
     perfect square**. Heath-Brown's square sieve converts "f is a square" into Jacobi-symbol sums Σ_𝒜 (f/qq′); these
     cancel because (i) the complete sums Σ_{k mod q}(f(c,k)/q) are ±1 except on one class of c (explicit discriminant
     16(4cn + 1)), and (ii) 𝒜 is equidistributed in residue classes mod qq′ by van der Corput's third-derivative test.
   * This *is* tie-aware cancellation: the tie x ≡ y ≡ −1 (mod 4C) of the hyperbola form is exactly the integrality of the
     roots, i.e. the square condition. It is the "non-trivial estimate for #{(x,y) : xy ≡ 1 (4p), x ≡ y ≡ −1 (mod 4C)} in a
     range" asked for in FRONTIER §7.1 — in the near-cube range, which is the range that carries the benchmark.
   * It is an **upper bound, uniform in n**: it holds verbatim at odd squares (where R = 0) and so can never give positivity.
     Worth nothing for ES existence; it moves only the error benchmark.
2. **Block-shape map (§4; PROVED floors + exponent bookkeeping).** Over the simplex of block shapes (u ≍ n^α, B ≍ n^β,
   C ≍ n^γ, α + β + γ = 1), the square-sieve route beats the trivial exponent min(α, β, γ) exactly in a small neighbourhood of
   the cube point (gain 1/75 at the cube; region ≈ |α − β| ≲ 0.02, 0.31 ≲ α ≲ 0.335 on the diagonal). Every other surveyed
   tool class has a PROVED floor at or above the trivial bound in every block:
   * λ-uniform modular-hyperbola box bounds (Weil/Kloosterman, Cilleruelo–Garaev, Bourgain–Garaev, KSWX, Shkredov) ≥ c·W
     (Prop B);
   * shift-uniform class-blind divisor counts ≥ (log 2 − o(1))·U, resp. V (Prop C);
   * the Erdős–Turán/ψ route with square-root max-input ≥ (UV)^{1/2} (Z52D Thm 6);
   * divisor-in-residue-class bounds (Lenstra, CHN, Bernstein) and Shiu: O(1) or O(log n) per fibre, removing only n^{o(1)}.
   The balanced block u, B ≍ p^{1/4} is **not** reached (the strip 𝒜 is sparse there; §4.3).
3. **Lower side (§5; PROVED).** Lemma A: a hyperbola point at height H yields a Type II solution iff x ≡ −1 (mod 4cd) for some
   factorisation H = c²d; so the tie modulus is always ≥ 4√H. Cor A′: a fixed congruence x ≡ −1 (mod q) certifies only
   heights H | q²/16 (≤ τ(q²) single integers 4Hn + 1). Weil/Selberg–Hooley give the tie-free count only for γ > 1/2, where the
   tie costs a factor ≍ W ≥ p^{1/2} against an error ≥ p^{1/2}.
4. **Z1855 pieces in unbalanced blocks reduce exactly to B-fibres** (Lemma D; PROVED): each piece count is a
   divisor-in-progression count of the single integer n + B.
5. **EVIDENCE/CERTIFIED computations.** For *every* integer n ≤ 5·10⁸ the near-cube count Q(n) (min(u,B,C) ≥ n^{1/3}/4) is
   ≤ 22 (trivial ≈ 800 at the top); the square-detection bijection matches brute force; the character sums Σ_𝒜(f/qq′) are
   square-root size (rms ≈ |𝒜|^{1/2}) at primes, test primes, odd squares and near-squares alike.

**Verdict: strengthened** (a genuine new lemma: the §7.1 benchmark p^{1/3} is beaten by a power, via tie-detecting character
sums) — and simultaneously **narrowed** (every λ-uniform, class-blind or fibre-local tool is floored at the trivial bound; the
square sieve is upper-bound-only and does not reach the balanced block). ES positivity is untouched.

## 1. Setting, notation, statements attacked

For n ≥ 2 a (★) triple is (u, B, C) ∈ ℕ³ with 4uBC − u − B = n. Block: 𝔅(U,V) = (U, 2U] × (V, 2V],
N(U,V) = N(U,V; n) = #{(u,B) ∈ 𝔅 : 4uB | n + u + B} (Z52D_HYPERBOLA §0). Put W := n/(4UV); a block solution has
C = (n+u+B)/(4uB) ∈ [n/(16UV), (n+2U+2V)/(4UV)], so C ≍ W. Exponents U = n^α, V = n^β, W ≍ n^γ, γ = 1 − α − β, over the
simplex Δ = {α, β ≥ 0, α + β ≤ 1}. Trivial exponent t(α,β) := min(α, β, γ) (Z52D Thm 1: N ≤ n^{o(1)}min(U, V, n/(UV) + 1),
valid for every n, not only primes); max t = 1/3 at the cube point.

Three fibrations of the same set (PROVED, elementary; Z52D §2):
* u-fibre: (4uC − 1)·B = n + u — a divisor d = 4uC − 1 ≡ −1 (mod 4u) of the single integer n + u;
* B-fibre: symmetric (n + B, modulus 4B);
* C-fibre: (4Cu − 1)(4CB − 1) = 4Cn + 1 — a point (x, y) of 𝓗 = {xy ≡ 1 (mod 4n)} at **height** C = (xy − 1)/(4n) with
  the **tie** x ≡ −1 (mod 4C) (which forces y ≡ −1 (mod 4C)).

**(S1) Upper side.** For each (α, β) ∈ Δ, which known tool proves N(U,V; n) ≪ n^{θ+o(1)} with θ < t(α,β) (tie included), and
does anything improve R(p) ≪ p^{1/3+o(1)}? → Theorem 1 (yes, near the cube) and §4 (map; floors elsewhere).
**(S2) Lower side.** Where do lower-bound tools apply to tie-free counts, which tie relaxations can they carry, how does the tie
break them? → §5.
**(S3) Integer-uniform falsifier.** Does some integer n attain the trivial bound near the cube (which would cap every
n-uniform method at 1/3)? → No: Theorem 1 is itself n-uniform; EVIDENCE §7.1.

## 2. Why this is not already closed

Z52D_HYPERBOLA closed, at the **balanced block**, one-step fixed-conductor dualization, the Erdős–Turán/Fejér route with
max|S_h| input, dispersion in the function variable and low-conductor main terms, and listed as open "(R3) counting, not
cancellation … determinant method … not attempted". It did not consider the cube block (which is where the p^{1/3} benchmark
lives), Heath-Brown's square sieve, divisor-in-class bounds, λ-uniform concentration bounds, or the lower side. None of the
closed items of the brief (hyperbola one-step dualization at fixed conductor; ET/Fejér with square-root input; Cauchy–Schwarz
in the function variable; low-conductor universality) covers a square-sieve argument: the sieve does not dualize at fixed
conductor, does not use max_h|S_h|, and uses no main term (it is an upper bound; low-conductor universality is irrelevant to
upper bounds, as Z52D Cor 3.2 itself notes).

## 3. Theorem 1 (power saving at the cube) — statement and full proof

**Theorem 1 (PROVED).** Let n ≥ 2, T := n^{1/3}, and 0 < η ≤ 1/20 fixed. Let
𝒮_η(n) := #{(u, B, C) ∈ ℕ³ : 4uBC − u − B = n, min(u, B, C) ≥ T^{1−η}}. Then
  (a) 𝒮_η(n) ≪_η T^{24/25 + 2η}(log T)²;
  (b) with η = 1/75: **R(n) ≪ n^{1/3 − 1/225}(log n)²** (the log² uses Shiu's theorem; without it, n^{1/3−1/225+o(1)} by the
      divisor bound).
  (c) For the cube block (U = V ≍ (n/4)^{1/3}, so C ≍ U as well) the same argument gives N(U,U) ≪ n^{8/25}(log n)².

Implied constants are absolute (given η). No primality is used; the statement holds for odd squares too (where R = 0).

### 3.1 Ranges (PROVED)
Let (u,B,C) be counted by 𝒮_η and M := max(u,B,C). Then 4uBC ≥ 4T^{2−2η}M and 4uBC = n + u + B ≤ n + 2M, so
M(4T^{2−2η} − 2) ≤ n, hence M ≤ T^{1+2η}/2 once T^{2−2η} ≥ 1. So
  C ∈ 𝒞 := [T^{1−η}, T^{1+2η}/2] ∩ ℤ,  s := u + B ∈ (S₁, S₂] := (2T^{1−η} − 1, T^{1+2η}].

### 3.2 Square detection (Lemma 1.1; PROVED)
Define 𝒜 := {(C, k) ∈ ℤ² : C ∈ 𝒞, 4Ck − n ∈ (S₁, S₂]} and f(C, k) := (4Ck − n)² − 4k.
(i) If (u,B,C) is counted by 𝒮_η, then (C, k) := (C, uB) ∈ 𝒜 and f(C, k) = (u − B)².
(ii) If (C, k) ∈ 𝒜 and f(C, k) = r² with r ∈ ℤ_{≥0}, then u, B := (s ∓ r)/2 with s = 4Ck − n are positive integers with
4uBC − u − B = n, u + B = s, uB = k.
(iii) Hence 𝒮_η(n) ≤ 2·#{(C,k) ∈ 𝒜 : f(C,k) is a nonzero perfect square} + τ(n).
*Proof.* (i) s = u + B and 4Ck − s = 4uBC − u − B = n, so 4Ck − n = s ∈ (S₁, S₂]; f = s² − 4uB = (u − B)².
(ii) k ≥ 1 because 4Ck = n + s > 0. From s² − r² = 4k: s ≡ r (mod 2) and (s − r)(s + r) = 4k > 0 with s > 0, so s − r > 0
and even, i.e. u = (s − r)/2 ≥ 1; B = (s + r)/2 ≥ u. Then u + B = s, uB = (s² − r²)/4 = k and 4uBC − u − B = 4Ck − s = n.
(iii) By (i) each counted triple with u ≠ B maps to a point with f a nonzero square, and (u,B,C), (B,u,C) are the only
preimages of a point (by (ii), {u,B} is determined by (s, k)). Triples with u = B satisfy u(4uC − 2) = n, so u | n, and C is
then determined: at most τ(n) of them. ∎

### 3.3 The square sieve (Lemma 1.2; Heath-Brown, Math. Ann. 266 (1984), Thm 1 — self-contained proof)
Let 𝒫 be a set of P₀ ≥ 1 odd primes and w : ℤ∖{0} → [0, ∞) finitely supported, with w(a) = 0 for a perfect square
a > 2^{P₀}. Then
  Σ_{m ≥ 1} w(m²) ≤ (4/P₀) Σ_a w(a) + (4/P₀²) Σ_{q ≠ q′ ∈ 𝒫} |Σ_a w(a)(a/qq′)|,
with (·/qq′) the Jacobi symbol (Legendre symbols of residues for a < 0).
*Proof.* For a = m² with 1 ≤ m ≤ 2^{P₀/2}: ω(m) ≤ log₂ m ≤ P₀/2, so Σ_{q∈𝒫}(a/q) = #{q ∈ 𝒫 : q ∤ m} ≥ P₀/2. Hence
Σ_m w(m²) ≤ (4/P₀²)Σ_a w(a)(Σ_q (a/q))² (all added terms are ≥ 0). Expand the square: diagonal terms (a/q)² ≤ 1 give ≤ P₀Σ w;
off-diagonal give Σ_{q≠q′}Σ_a w(a)(a/q)(a/q′). ∎
Apply with w(a) := #{(C,k) ∈ 𝒜 : f(C,k) = a} (a ≠ 0). Squares f ≤ S₂² ≤ T^{2+4η} ≤ 2^{P₀} once P₀ ≥ 3 log₂ T. Since
(0/qq′) = 0,
  #{(C,k) ∈ 𝒜 : f nonzero square} ≤ (4/P₀)|𝒜| + 4 max_{q≠q′∈𝒫} |S_{qq′}|,  S_Q := Σ_{(C,k)∈𝒜} (f(C,k)/Q).   (3.1)

### 3.4 Complete sums (Lemma 1.3; PROVED)
Let q be an odd prime, c ∈ ℤ, K_q(c) := Σ_{k mod q} (f(c,k)/q). Then K_q(c) = 0 if q | c; K_q(c) = q − 1 if q ∤ c and
q | 4cn + 1; K_q(c) = −1 otherwise. For Q = qq′ (q ≠ q′), K(c) := Σ_{k mod Q}(f(c,k)/Q) = K_q(c)K_{q′}(c) (CRT).
*Proof.* f(c, k) = 16c²k² − (8cn + 4)k + n². If q | c, f ≡ n² − 4k is a non-constant linear polynomial in k (q odd), so the
sum of (·/q) over k is 0. Otherwise f is quadratic with leading coefficient 16c² (a nonzero square mod q) and discriminant
(8cn + 4)² − 64c²n² = 16(4cn + 1); the classical evaluation Σ_x ((ax² + bx + c)/q) = −(a/q) if q ∤ b² − 4ac and (q−1)(a/q)
otherwise gives the claim. ∎
Let D_q := {c : q | 4cn + 1} (one class mod q, empty if q | n). So |K(c)| ≤ (1 + q·1_{D_q}(c))(1 + q′·1_{D_{q′}}(c)).

### 3.5 Main term / discrepancy split (PROVED)
For C ∈ 𝒞 put J_C := ((n + S₁)/(4C), (n + S₂)/(4C)], so 𝒜 = {(C,k) : C ∈ 𝒞, k ∈ J_C ∩ ℤ}, |J_C| = (S₂ − S₁)/(4C).
For residues c₀, k₀ mod Q, with ψ(x) = x − ⌊x⌋ − 1/2,
  #{k ∈ J_C ∩ ℤ : k ≡ k₀ (Q)} = #{j ∈ ℤ ∩ (α_C, β_C]} = |J_C|/Q − ψ(β_C) + ψ(α_C),
  α_C := ((n + S₁)/(4C) − k₀)/Q,  β_C := ((n + S₂)/(4C) − k₀)/Q.
Since f(C,k) mod Q depends only on (C mod Q, k mod Q),
  S_Q = Σ_{c₀ mod Q} M(c₀)K(c₀) + Σ_{c₀, k₀ mod Q} (f(c₀,k₀)/Q)·E(c₀,k₀),
  M(c₀) := Q⁻¹ Σ_{C∈𝒞, C≡c₀} |J_C|,  E(c₀,k₀) := Σ_{C∈𝒞, C≡c₀ (Q)} [ψ(α_C) − ψ(β_C)].   (3.2)

*Main term.* |J_C| is decreasing in C, so for any modulus m and class, Σ_{C∈𝒞, C≡c (m)}|J_C| ≤ m⁻¹Σ_J + J_max, where
Σ_J := Σ_{C∈𝒞}|J_C| ≤ (S₂/4)(3η log T + 1) and J_max := max|J_C| ≤ T^{3η}/4. Using the bound on |K(c)| and expanding,
  |Σ_{c₀} M(c₀)K(c₀)| ≤ Q⁻¹[Σ_J + q(Σ_J/q + J_max) + q′(Σ_J/q′ + J_max) + Q(Σ_J/Q + J_max)] ≤ 4Σ_J/Q + 3J_max
  ≪ T^{1+2η}(log T)/Q + T^{3η}.   (3.3)
Also |𝒜| ≤ Σ_C (|J_C| + 1) ≤ Σ_J + |𝒞| ≪ T^{1+2η} log T.   (3.4)

### 3.6 Discrepancy in residue classes (Lemma 1.4; PROVED relative to two classical estimates)
Inputs (standard): **(V)** Vaaler's lemma (Graham–Kolesnik, *Van der Corput's method of exponential sums*, Thm A.6; Vaaler,
BAMS 12 (1985)): for real g on a set I of N integers and H ≥ 1, |Σ_{j∈I}ψ(g(j))| ≤ N/(2H+2) + Σ_{h=1}^{H}(1/(πh) + 1/(H+1))
|Σ_{j∈I}e(hg(j))| (as re-derived from Vaaler's Thm A.6 in Ma–Sun, arXiv:2109.02924, Lemma 2.1).
**(3D)** van der Corput's third-derivative test (Titchmarsh, *Theory of the Riemann zeta-function*, 2nd ed., Thm 5.11;
Graham–Kolesnik Thm 2.6): if φ ∈ C³ on an interval I of length N ≥ 1 and λ ≤ |φ‴| ≤ αλ there, then
Σ_{j∈I}e(φ(j)) ≪ α^{1/2}Nλ^{1/6} + N^{1/2}λ^{−1/6}. (The source statements were not re-read in this lane; both are textbook.)

**Lemma 1.4.** Let Q ≤ T^{1/2}. Then Σ_{c₀,k₀ mod Q} |E(c₀,k₀)| ≪ (T^{6/7+2η}Q^{9/7} + T^{2/3+7η/3}Q^{7/6})(log T)².
*Proof.* Split 𝒞 into O(log T) dyadic pieces (W, 2W] ∩ 𝒞 (T^{1−η}/2 ≤ W ≤ T^{1+2η}/2). Fix a piece, a class (c₀, k₀) and one
endpoint (S = S₁ or S₂). Writing C = c₀ + Qj, j runs over an interval I of N ≤ W/Q + 1 ≤ 2W/Q integers (Q ≤ W), and
ψ(α_C) = ψ(g(j)) with g(j) = A/(c₀ + Qj) − k₀/Q, A = (n + S)/(4Q). Then hg‴(j) = −6hAQ³/C⁴ = −(3/2)h(n+S)Q²/C⁴, so on the
piece λ_h ≤ |hg‴| ≤ 16λ_h with λ_h := (3/32)h(n+S)Q²/W⁴ ≍ hnQ²/W⁴ (n ≤ n + S ≤ 2n). By (V) and (3D) with H ≥ 1,
  |Σ_{j∈I}ψ(g(j))| ≪ W/(QH) + Σ_{h≤H} h⁻¹[(W/Q)λ_h^{1/6} + (W/Q)^{1/2}λ_h^{−1/6}].
With n ≍ T³ and W ≤ T^{1+2η}: (W/Q)λ_h^{1/6} ≪ h^{1/6}T^{1/2}W^{1/3}Q^{−2/3} ≤ h^{1/6}T^{5/6+2η/3}Q^{−2/3}, and
(W/Q)^{1/2}λ_h^{−1/6} ≪ h^{−1/6}W^{7/6}T^{−1/2}Q^{−5/6} ≤ T^{2/3+7η/3}Q^{−5/6}. Summing over h ≤ H:
  ≪ T^{1+2η}/(QH) + H^{1/6}T^{5/6+2η/3}Q^{−2/3} + T^{2/3+7η/3}Q^{−5/6}log H.
Choose H := ⌈T^{1/7}Q^{−2/7}⌉ (≥ 1 as Q ≤ T^{1/2}): the first two terms are ≪ T^{6/7+2η}Q^{−5/7}. Multiply by the Q² classes,
the 2 endpoints and the O(log T) pieces. ∎

### 3.7 Assembly
Take 𝒫 := the primes in (P, 2P] with P := T^{1/25}, so P₀ ≫ P/log P (≥ 3 log₂ T for large T) and Q = qq′ ≤ 4P² ≤ T^{1/2}.
By (3.2)–(3.4) and Lemma 1.4,
  max_Q |S_Q| ≪ T^{1+2η}log T/P² + T^{3η} + (T^{6/7+2η}P^{18/7} + T^{2/3+7η/3}P^{7/3})(log T)²,
and by (3.1) and Lemma 1.1(iii),
  𝒮_η(n) ≪ (log P/P)·T^{1+2η}log T + T^{6/7+2η}P^{18/7}(log T)² + T^{2/3+7η/3}P^{7/3}(log T)² + τ(n).
With P = T^{1/25}: the first two terms are ≪ T^{24/25+2η}(log T)²; the third is T^{2/3+7/75+7η/3}(log T)² ≤ T^{0.88} for
η ≤ 1/20. This is (a).

(b) Triples with u < T^{1−η}: for fixed u, B is a divisor of n + u and determines C, so their number is
≤ Σ_{n<m≤n+T^{1−η}} τ(m) ≪ T^{1−η}log n by Shiu (Brun–Titchmarsh for multiplicative functions, J. reine angew. Math. 313
(1980), Thm 1, with k = 1, y = T^{1−η} > x^{1/4}). Likewise B < T^{1−η}. Triples with C < T^{1−η}: for fixed C, (u,B) is
determined by the divisor 4Cu − 1 of 4Cn + 1, so their number is ≤ Σ_{C<T^{1−η}} τ(4Cn + 1) ≪ T^{1−η}log n by Shiu with
k = 4n, a = 1, y = 4nT^{1−η} (k < y^{1−β}), using exp(Σ_{ℓ≤x, ℓ∤k}2/ℓ) ≪ (log x)²(φ(k)/k)². All remaining triples are
counted by 𝒮_η. With η = 1/75 both parts are ≪ T^{74/75}(log n)² = n^{1/3−1/225}(log n)².
(c) Same proof with 𝒞 = the block's C-range, (S₁, S₂] = (2U, 4U] and η = 0 in all size bounds. ∎

*Remarks.* (1) The constants 1/25, 1/225 are not optimised. Exponent bookkeeping of the same argument block by block
(`scripts/z53_hypsumprod_sqmap.py`, a computation of exponents with log factors ignored, not a written proof; it also uses
the second-derivative and Kusmin–Landau tests where better) gives max over Δ of min(t, θ_sq) ≈ 0.3272, i.e. R(n) ≪ n^{0.3272}
(δ ≈ 1/160). Better exponent pairs or a Fourier treatment of the classes would improve further; not pursued.
(2) The data show the character sums are square-root size (§7.2), far better than Lemma 1.4; with square-root sums the
square sieve would give ≈ n^{1/4}-type bounds at the cube. Not claimed.
(3) Why primality is irrelevant: every step is uniform in n. Consequently the theorem can never feed a positivity argument
(T1: R(m²) = 0 satisfies every upper bound).

## 4. The block-shape map (upper side)

### 4.1 Floors for tie-blind and class-blind tools (PROVED)
**Proposition B (λ-uniform floor).** m = 4p, I, J intervals of lengths L_I, L_J, H_λ := #{(x,y) ∈ I × J : xy ≡ λ (mod m)}.
Then max_{λ ∈ (ℤ/m)^×} H_λ ≥ φ(m)⁻¹·#{x ∈ I : (x,m) = 1}·#{y ∈ J : (y,m) = 1}
≥ (L_I(p−1)/(2p) − 2)₊(L_J(p−1)/(2p) − 2)₊/(2(p − 1)) (p odd prime, I, J with L_I, L_J integers).
*Proof.* Σ_λ H_λ counts the pairs (x, y) with both coordinates units mod 4p; average over the φ(4p) = 2(p − 1) unit classes.
An interval of L integers has ≥ (L − 1)/2 odd integers and ≤ L/(2p) + 1 odd multiples of p, so #{x ∈ I : (x, 4p) = 1}
≥ L(p−1)/(2p) − 3/2. ∎
*Application.* The (x, y) = (4Cu − 1, 4CB − 1) image of 𝔅(U,V) lies in a box with L_I ≍ WU, L_J ≍ WV, L_I L_J ≍ Wp, so the
floor is ≍ W ≥ min(U,V,W). Any bound for N obtained as a λ-uniform bound for H_1(box) — Weil/Kloosterman box counts;
Cilleruelo–Garaev (GAFA 21 (2011) 892–904, Thm 1: #{xy ≡ λ (p), (x,y) ∈ [K+1,K+M]×[L+1,L+M]} < M^{4/3+o(1)}p^{−1/3} + M^{o(1)},
uniform in λ, K, L; prime modulus, verified from arXiv:1007.1526); Bourgain–Garaev, KSWX, Shkredov-type bilinear inputs as
used for box counts — is never below the trivial bound by a power, in any block.

**Proposition C (shift-uniform class-blind floor).** For X ≥ V: X⁻¹Σ_{n₀=1}^{X} #{(u,B) ∈ 𝔅(U,V) : B | n₀ + u}
≥ U(Σ_{V<B≤2V}1/B) − UV/X ≥ U(log 2 − 1/V) − UV/X.
*Proof.* For fixed (u,B), #{n₀ ≤ X : B | n₀ + u} ≥ X/B − 1; sum over the UV pairs and use Σ_{V<B≤2V}1/B ≥ log 2 − 1/V. ∎
So a bound for 𝓛₂ = {(u,B) : B | n + u} (the class-blind u-fibre relation, i.e. dropping the class −1 (mod 4u) of the
co-divisor) valid for every shift n ≤ X is ≥ (log 2 − o(1))U; symmetrically ≥ (log 2 − o(1))V for 𝓛₁. Neither beats
min(U, V) by a power. (The joint relation 𝓛₁ ∩ 𝓛₂ = {uB | n + u + B} is the tie up to the 2-adic condition; that is what
the square sieve exploits.)

### 4.2 The map
Exponents base n; "beats trivial" means θ < t(α,β) = min(α, β, γ).

| tool class | where it applies | best bound (exponent) | vs trivial | status |
|---|---|---|---|---|
| elementary fibre bound (Z52D Thm 1) | all Δ | t + o(1) | = | PROVED |
| Shiu (τ in short intervals / APs mod 4n) | min(α,β,γ) ≥ δ₀ | t, with n^{o(1)} → log n | = (log only) | PROVED rel. Shiu |
| Lenstra / CHN / Bernstein (divisors of one integer in a class) | u-fibre α > 1/4; B-fibre β > 1/4; C-fibre γ > 1/3 (s = 4C ≥ (4Cn)^{1/4+ε}) | ≤ c(ε) per fibre ⇒ ≤ c·(#fibres) | = (n^{o(1)} only) | PROVED rel. Lenstra (3.1), CHN |
| λ-uniform 𝓗 box/concentration bounds | all Δ | ≥ γ (Prop B floor) | never below | PROVED floor |
| shift-uniform class-blind fibre counts | all Δ | ≥ α resp. β (Prop C floor) | never below | PROVED floor |
| ψ / Erdős–Turán with max|S_h|, square-root input | all Δ | ≥ (α+β)/2 (Z52D Thm 6c) | never below | PROVED (Z52D) |
| determinant method / affine dimension growth | cubic surface 4xyz − x − y = n | general bounds ≥ B^{1} (lines/dimension growth; Vermeulen arXiv:2311.05433 Thm 1.2 excludes degree 3) | not below | Assessment (lit.) |
| **square sieve + third-derivative test (Thm 1)** | neighbourhood of the cube (table below) | θ_sq | **below**, gain ≤ 1/75 | **PROVED** (cube: Thm 1(a,c)); off-cube values: exponent bookkeeping |

Square-sieve exponent θ_sq (`scripts/z53_hypsumprod_sqmap.py`; computation of exponents; grid step ≤ 0.002 near the cube):

| (α, β, γ) | trivial t | θ_sq | gain t − θ_sq |
|---|---|---|---|
| (1/3, 1/3, 1/3) cube | 0.3333 | 0.3203 | +0.0130 (= 1/75, Thm 1(c)) |
| (0.33, 0.33, 0.34) | 0.330 | 0.3185 | +0.0115 |
| (0.32, 0.32, 0.36) | 0.320 | 0.3140 | +0.0060 |
| (0.31, 0.31, 0.38) | 0.310 | 0.3090 | +0.0010 |
| (0.30, 0.30, 0.40) | 0.300 | 0.3146 | −0.0146 (no gain) |
| (0.33, 0.34, 0.33) | 0.330 | 0.3245 | +0.0055 |
| (0.34, 0.34, 0.32) | 0.320 | 0.3235 | −0.0035 (no gain) |
| (0.25, 0.25, 0.50) balanced | 0.250 | 0.3337 | −0.084 (no gain) |

Global: max over Δ of min(t, θ_sq) ≈ 0.3272 (attained near (0.328, 0.344, 0.328)); the written proof (uniform near-cube
treatment) gives 74/225 ≈ 0.3289.

### 4.3 Why the square sieve does not reach the balanced block (Assessment, with the exponent computation)
The sieve needs 𝒜 (the strip 4Ck − n ∈ s-range) to be equidistributed mod qq′ with a discrepancy below the target. 𝒜 is
parametrised by C ∈ (W, 2W] with |J_C| ≍ V/W points per C. In the balanced block V/W ≍ p^{−1/4}: only a p^{−1/4} fraction of
the C carry a point, and the discrepancy is a ψ-sum over all ≍ p^{1/2} values of C, whose van der Corput bounds are ≫ p^{1/4}
= the trivial bound (θ_sq ≈ 0.334 > 0.25). Re-parametrising 𝒜 by s (for each s ≍ U, C | (n + s)/4) turns it into
divisors of single integers — B2 again. So the square sieve is effective exactly where 𝒜 is dense along C, i.e. V ≍ W,
and the U ≍ V requirement comes from |𝒜| ≍ max(U,V): a neighbourhood of the cube.

### 4.4 Z1855 pieces in unbalanced blocks (Lemma D; PROVED)
Fix B. Z1855's piece for q = B is {m : u := Bm − n ∈ (U, 2U], 4u | m + 1}. Its elements are in bijection (via C = (m + 1)/(4u))
with the (★) triples (u, B, C) having this B and u ∈ (U, 2U]; every such u satisfies u | n + B and u ≡ −n (mod B).
*Proof.* Given m with 4u | m + 1, C := (m+1)/(4u) gives (4uC − 1)B = mB = n + u. Conversely a triple gives m := 4uC − 1 with
Bm − n = u. And m ≡ −1 (mod u), Bm = n + u force u | n + B; u ≡ −n (mod B) is u = Bm − n. ∎
So any piece-wise method (van der Corput on the piece of length U/B) acts on a divisor-in-progression count of the single
integer n + B, which has ≤ τ(n + B) candidates. A piece-wise exponential-sum detection would have to certify that most
pieces are *empty*, i.e. beat the single-integer divisor structure; no such method is known (Assessment). Z1855 in
unbalanced blocks: **closed as a reduction** (no information beyond the B-fibre).

## 5. Lower side: where lower-bound tools apply and how the tie breaks them

**Lemma A (tie floor for Type II; PROVED).** Let n ≥ 1, (x, y) ∈ ℕ² with xy ≡ 1 (mod 4n), H := (xy − 1)/(4n). The Type II
quadruples (a,b,c,d) ∈ ℕ⁴ with 4abcd − a − b = cn and (4acd − 1, 4bcd − 1) = (x, y) correspond bijectively to factorisations
H = c²d with x ≡ −1 (mod 4cd).
*Proof.* (⇒) (4acd − 1)(4bcd − 1) = 4cd(4abcd − a − b) + 1 = 4c²dn + 1, so H = c²d and x ≡ −1 (mod 4cd). (⇐) Given
H = c²d with 4cd | x + 1: xy = 4c²dn + 1 ≡ 1 (mod 4cd) forces y ≡ −1 (mod 4cd); a := (x+1)/(4cd), b := (y+1)/(4cd) satisfy
16abc²d² − 4cd(a+b) + 1 = 4c²dn + 1, i.e. 4abcd − a − b = cn. The maps are mutually inverse. ∎
(★) is c = 1, d = H (full tie mod 4H); the weakest admissible tie has modulus 4cd = 4√(Hd) ≥ 4√H.

**Corollary A′ (fixed congruences certify only finitely many heights; PROVED).** Fix q ≥ 1 and H ≥ 1. The implication
"x ≡ −1 (mod q) ⇒ x ≡ −1 (mod 4cd) for some H = c²d" holds for all integers x iff some factorisation H = c²d has 4cd | q;
then 16H | q², so H | q²/16.
*Proof.* If 4cd | q the implication is trivial and 16c²d² | q² gives 16Hd | q². Conversely, if 4c_id_i ∤ q for all
factorisations, write x = −1 + qt: x ≡ −1 (mod 4c_id_i) ⇔ e_i | t with e_i = 4c_id_i/gcd(q, 4c_id_i) > 1; x = q − 1 (t = 1)
violates all of them. ∎

**Where the tie breaks the lower-bound tools (PROVED arithmetic + Assessment reading).**
* Weil/Kloosterman: #{(x,y) ∈ box : xy ≡ 1 (4p)} = main + O(p^{1/2+o(1)}), nontrivial only for box area ≫ p^{3/2+ε}. The block
  box has area ≍ Wp, so this needs γ > 1/2 (blocks with UV < p^{1/2}). There the tie-free count is ≍ W (proved), while the tied
  count has mean O(1): the tie costs a factor ≍ W ≥ p^{1/2}, against an error ≥ p^{1/2}. Selberg–Hooley/FKM for τ(4Cp + 1) in
  C ≤ W needs W ≥ p^{1/2+ε} too (PARITY_AUDIT row B6): same region, same verdict.
* Every-λ solvability (xy ≡ λ with x, y ≪ p^{3/4}; almost-all-λ versions at p^{1/2+ε}) is trivial at λ = 1 ((1,1) is a point)
  and carries no height control.
* Adding fixed congruences to any of these: by Cor A′ the certified points sit at ≤ τ(q²) fixed heights H | q²/16, each a
  factorisation question for one integer 4Hp + 1 where no box tool acts. A lower-bound tool must therefore carry a tie of
  modulus ≥ 4√H moving with the point — which is B2.
* The square sieve of §3 is upper-bound-only; there is no known lower-bound analogue of square detection that survives T1
  (squares in a thin set cannot be forced from character sums that are uniform in n).

## 6. Status of the integer-uniform question (S3)
Theorem 1 is n-uniform, so no integer attains the trivial cap near the cube: every integer n has 𝒮_η(n) ≪ T^{24/25+2η}.
The EVIDENCE of §7.1 is consistent (max Q(n) ≤ 22 for all n ≤ 5·10⁸).

## 7. Computations

### 7.1 Integer-uniform falsifier (CERTIFIED for the stated range; `scripts/z53_hypsumprod_rmax.c`)
R(n) and Q(n) := #{(★) triples with 64·min(u,B,C)³ ≥ n} (i.e. min ≥ n^{1/3}/4) for **every** n ≤ 5·10⁸ (exhaustive
enumeration of all triples with 4uBC − u − B ≤ X). Output `data/z53/hypsumprod/rmax_5e8.txt` (records and dyadic maxima).
* max Q(n) over all n ≤ 5·10⁸: **22** (n = 199 582 860); over primes n ≡ 1 (4): 16 (n = 9 405 457). Dyadic maxima of Q grow
  6 → 22 from n ≈ 10³ to 3·10⁸ (log-like), against trivial ≈ n^{1/3}/… ≈ 800.
* max R(n) ≤ 5·10⁸: 439 (n = 480 134 654); mean R over the top dyadic range ≈ 51 (all n), 63 (primes ≡ 1 (4)).

### 7.2 Square-sieve sanity checks (EVIDENCE; `scripts/z53_hypsumprod_sqsieve.c`)
For given n, C-range (W, 2W] and s-range (S₁, S₂]: (i) #{(C,k) ∈ 𝒜 : f nonzero square} vs a brute-force count of (★) triples
with C ∈ (W, 2W], u + B ∈ (S₁, S₂], u < B — **MATCH** in all 8 brute-force cases (n = 10⁹+7, 10⁹+9, 999 999 999,
199 582 860 (8 solutions), 9 405 457, 8 813 281 (test prime), 8 812 969, 8 814 961 = 2969²). (ii) S_Q over 91 prime pairs
q < q′ from {101,…,1013}: rms|S_Q| ≈ |𝒜|^{1/2} throughout. Controls at n ≈ 10¹⁵ (W = 40 000, s ∈ (5·10⁴, 4·10⁵]):

| n | type | |𝒜| | squares | max|S_Q| | rms|S_Q| |
|---|---|---|---|---|---|
| 1 000 000 025 191 729 = 31 622 777² | odd square (T1) | 60 774 | 0 | 614 | 257 |
| 1 000 000 025 191 733 = m² + 4 | near-square | 60 773 | 0 | 597 | 259 |
| 1 000 000 000 000 037 | prime | 60 676 | 0 | 636 | 273 |
| 1 000 000 000 000 091 (W = 50 000) | prime | 60 635 | — | 612 | 232 |

The sums behave identically at the square, the near-square and primes: the mechanism is T1-blind, as an upper bound must be.
(`data/z53/hypsumprod/sqsieve_checks.txt`, `sqsieve_controls.txt`.)

### 7.3 Exponent map (computation; `scripts/z53_hypsumprod_sqmap.py`)
Grid over Δ (step 1/60; fine grid step 0.002 on [0.30, 0.38]²), optimising P = n^ρ and H = n^{e_H}. Outputs
`data/z53/hypsumprod/sqmap_grid60.json`, `sqmap_fine_cube.json`. Gains exist only near the cube (§4.2 table).

## 8. FRONTIER §4 hard screens (for Theorem 1)
1. **T1 (odd squares).** Not applicable as a positivity screen: Theorem 1 is an upper bound and holds at m² (where R = 0).
   It is n-uniform, so it *cannot* be a step of a positivity argument — stated explicitly.
2. **8/131.** The argument uses only the shape "u, B roots of z² − sz + k with a linear relation between level·k and s"; it
   transfers to numerator-m analogues (upper bounds), so it is numerator-uniform. Harmless for an upper bound; it says
   nothing about 8/131.
3. **Tied modulus.** Passed in the upper-bound sense: the tie is used (it *is* the square condition), and the moving modulus
   4C is absorbed into the strip parametrisation (C, k) with auxiliary *fixed* moduli qq′. This is the first tie-aware
   cancellation estimate in the campaign; it controls a power-size count, not a (log p)² main term (B3 still applies to any
   positivity use).
4. **Fixed p.** Passed: pointwise in n; the only averaging is over C along the strip and over auxiliary primes q, q′.

## 9. Verdict
**Strengthened** (genuine new step): R(n) ≪ n^{1/3−1/225}(log n)² for all n (Theorem 1, PROVED, relative to Vaaler's lemma,
van der Corput's third-derivative test, the classical quadratic character-sum evaluation and Shiu), hence |E(p)| ≪
p^{1/3−1/225+o(1)}; the cube block, which carries the benchmark, has N ≪ n^{8/25+o(1)}. What it buys: the FRONTIER benchmark
p^{1/3} for E(p) moves; §7.1's "any non-trivial estimate for the tied count in a range" is achieved in the near-cube range by
cancellation in tie-detecting character sums; the integer-uniform question (S3) is settled (no integer attains the trivial
cap). What it does not buy: anything about positivity (upper bound, n-uniform, T1-blind), anything in the balanced block,
anything near log²p.
**Narrowed** (scoped theorems): λ-uniform hyperbola tools (Prop B), shift-uniform class-blind fibre counts (Prop C), Lenstra-
type fibre bounds and Shiu (≤ n^{o(1)} gain), Z1855 piece methods in unbalanced blocks (Lemma D: reduce to B-fibres), and every
fixed-congruence lower-bound count (Lemma A / Cor A′: only finitely many heights) cannot beat the trivial bound or certify ES.

## 10. Proposed FRONTIER §7 text (do NOT edit FRONTIER here)
Append to §7.1:
> *(z53, `Z53_HYPSUMPROD.md`; internal.)* **The p^{1/3} benchmark is beaten.** R(n) ≪ n^{1/3−1/225}(log n)² for every n
> (PROVED rel. Vaaler, the third-derivative test and Shiu): near the cube u, B, C ≍ n^{1/3} a (★) triple is a point (C, k) of
> the strip 4Ck − n ∈ (s-range) at which (4Ck − n)² − 4k is a square (u, B are the roots of z² − sz + k); Heath-Brown's
> square sieve plus equidistribution of the strip mod qq′ gives the saving. This is tie-aware cancellation, but an upper bound
> uniform in n (valid at squares), so it does nothing for positivity. Block map: the gain exists only near the cube
> (≤ 1/75); λ-uniform hyperbola concentration bounds are floored at ≍ W, shift-uniform class-blind counts at ≍ U, Lenstra-type
> and Shiu bounds remove only n^{o(1)}; the balanced block is not reached (sparse strip). Lower side: a hyperbola point gives a
> Type II solution iff x ≡ −1 mod 4cd for some c²d = height (tie modulus ≥ 4√H), so fixed congruences certify only heights
> H | q²/16.

In §3 ("Tied modulus") and §2.2 replace "|E(p)| ≪ p^{1/3+o(1)} (best known)" by "|E(p)| ≪ p^{1/3−1/225+o(1)} (z53; square sieve;
elementary p^{1/3+o(1)})". In §6 add: "λ-uniform hyperbola concentration / class-blind fibre counts → floored at the trivial
block bound → `Z53_HYPSUMPROD` Props B, C".

## 11. Bottom line
The §7.1 lead "cancellation on the height-tied hyperbola" now has its first theorem: at the cube, where the elementary p^{1/3}
lives, the tie can be detected as a perfect-square condition and Heath-Brown's square sieve, with van der Corput
equidistribution of the strip modulo auxiliary primes, beats the divisor bound by a power, giving R(n) ≪ n^{1/3−1/225} for every
n. The price is the usual one for upper bounds: the argument is uniform in n, valid at odd squares, and therefore silent on
existence; it also stops near the cube (the strip is too sparse in the balanced block). Every other tool class surveyed has a
proved floor at the trivial bound. ES remains open.

## 12. Reproduction
```
cd $REPO; mkdir -p /tmp/z53 && cd /tmp/z53
gcc -O2 -o rmax $REPO/scripts/z53_hypsumprod_rmax.c
ulimit -v 7000000; timeout 1500 ./rmax 500000000 > rmax_5e8.txt                    # ~6 min, ~3.5 GB
gcc -O2 -o sqs $REPO/scripts/z53_hypsumprod_sqsieve.c -lm
ulimit -v 4000000; ./sqs 1000000007 300 500 4000 1; ./sqs 199582860 150 200 2400 1      # bijection + character sums
./sqs 1000000025191729 40000 50000 400000 0; ./sqs 1000000000000037 40000 50000 400000 0  # controls (~1 min each)
uv run python $REPO/scripts/z53_hypsumprod_sqmap.py 0.0166666667 sqmap60.json           # exponent map (~5 min)
```

## 13. Review log
(TODO: hostile deep review of Theorem 1.)
