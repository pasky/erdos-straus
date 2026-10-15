# NORMFORM_CUBIC — the degree-3 norm-form rung of the menu ladder (task O248, spark relay Z13)

Status: O248 work in progress (unreviewed). **ES is not solved here; no infinite case of ES for primes is claimed.**
Labels as in DISCOVERIES.md. Memos `BRAINSTORM/z20_*.md`; scripts `scripts/z20_*`.

## 0. Iteration log
(I1) Re-read SYNTHESIS_SPARKS7 §1 (Thms 1.1/1.2, degree 2) looking for the "top-part step that fails for degree 3".
Finding: the step does NOT fail. Every use of "Q has degree 2" in those proofs is an instance of "a homogeneous
irreducible polynomial cannot be written as a product of two homogeneous factors of positive degree", or of "a prime
of degree k cannot divide a product of forms of degree < k". Both are degree-free (unique factorisation in ℚ[x₁,…,x_r]).
The two places where the degree-2 proof used more (Q restricted to a rational line, Thm 1.2 (c1) B-quadratic; degree
count in (c2) μ = 2) have UFD replacements (§1 below). → Theorem 1.1′/1.2′: the collapse holds for every irreducible form
of every degree in any number of variables, and more generally whenever the *leading form* of n(x) is irreducible.

## 1. The collapse is degree-free

Setting. r ≥ 1 variables x = (x₁,…,x_r). P ∈ ℚ[x] non-constant of degree k ≥ 1, with top-degree homogeneous part P*
**irreducible over ℚ** (e.g. P a binary cubic form irreducible over ℚ, the ternary norm form N_{K/ℚ}(u + vθ + wθ²) of a
cubic field, or any norm form of a degree-k field in k variables — these factor only over a splitting field).
A polynomial Type II / Type I family for P is A, B, C, D ∈ ℚ[x] ∖ {0} with, identically,
  (II) 4ABCD = A + B + C·P,     (I) 4ABCD = P·(A + B) + C.
X* = top-degree part; α, β, γ, δ = degrees; s = α + β + γ + δ. ℚ[x] is a UFD and (UV)* = U*V*. Two facts used throughout:
 (F1) If P* = U·V with U, V forms, one of U, V is constant.  (F2) P* is prime, so P* ∤ any product of nonzero forms each
 of degree < k.  (F3) If U·V = P*^j·(const) with U, V forms, U = λ P*^i.

**Theorem 1.1′ (Type II, any degree; PROVED, elementary).** If a polynomial Type II family for P is valid (A, B, C, D > 0)
at one point, then A, B, C, D ∈ ℚ[P].
*Proof.* As in SYNTHESIS_SPARKS7 Thm 1.1, with k for 2. s ≤ max(α, β, γ + k).
(a) s ≤ α: β = γ = δ = 0, A(4BCD − 1) = B + CP; 4BCD = 1 would force CP = −B constant, impossible; A ∈ ℚ[P]. (β symmetric.)
(b) s > α, β. If γ + k ≠ s the right side has degree ≠ s (γ + k > s: the term C*P* survives; γ + k < s: everything has
degree < s); so γ + k = s, α + β + δ = k and 4A*B*D* = P*. By (F1) exactly one of A, B, D has degree k (top ∝ P*).
 (b1) D of degree k, A, B constants: C(4ABD − P) = A + B > 0 (validity), so C and 4ABD − P are constants: D ∈ ℚ[P].
 (b2) A of degree k, B, D constants: E := 4BDA − P has degree < k; C·E = A + B, so E ≠ 0 (A + B ≠ 0) and
 E·(4BDC − 1) = P + 4B²D. If deg E ≥ 1 then deg C ≥ 1 and E*·4BD·C* = P* contradicts (F1). So E is a nonzero constant and
 A = (P + E)/(4BD), C = (A + B)/E lie in ℚ[P]. (B of degree k: symmetric.) ∎
Note: positivity is used only through A + B ≠ 0 (as in the degree-2 Remark).

**Theorem 1.2′ (Type I, any degree, any level; PROVED, elementary).** Let a polynomial Type I family for P be valid at all
points of a lattice coset L ⊂ ℤ^r lying in an open cone Γ ⊂ ℝ^r (outside a bounded set). Then A, B, C, D ∈ ℚ[P].
*Proof.* Positivity: the zero sets of A*, B*, C*, D*, P* on the sphere are proper algebraic subsets, so Γ ∩ S^{r−1} contains a
non-empty open set U avoiding them; along points of L tending to infinity in a direction θ ∈ U every coordinate is
~ |x|^{deg}·X*(θ) and is positive, as is P(x) = n, so A*, B*, C*, D*, P* > 0 on U. Hence no top-degree cancellation occurs in
A + B or in P(A + B) + C. Put μ = max(α, β): deg(A + B) = μ, s = max(μ + k, γ).
(a) γ > μ + k: s = γ forces α = β = δ = 0, then C(4ABD − 1) = P(A + B) has degree k < γ, or 4ABD = 1 and P(A + B) = 0: impossible.
(b) γ = μ + k: s = γ forces α = β = δ = 0, γ = k; 4ABD ≠ 1 and C = P(A + B)/(4ABD − 1) ∈ ℚ[P].
(c) γ < μ + k = s.
 (c1) α > β (wlog). Then β + γ + δ = k and 4B*C*D* = P*; by (F1) one of B, C, D has degree k, the others are constants.
  • B of degree k (so α > k): E := 4BCD − P, deg E < k, and A·E = PB + C ≠ 0 (degree 2k), so E ≠ 0. Substituting
    B = (P + E)/(4CD): E·(4CD·A − P) = P² + 4C²D. If deg E ≥ 1, E* divides (P² + 4C²D)* = P*², so E* = λP*^i (F3) with
    0 < deg E* < k: impossible. So E is constant and B, A = (PB + C)/E ∈ ℚ[P].
  • C of degree k: C = P/(4BD) + E, deg E < k, and the identity A(4BCD − P) = PB + C becomes E·(4BD·A − 1) = κP with
    κ = B + 1/(4BD) > 0. E ≠ 0; α ≥ 1, so E*·4BD·A* = κP*: by (F1) E is constant and A ∈ ℚ[P].
  • D of degree k: D = P/(4BC) + E, deg E < k, and 4BC·A·E = PB + C (≠ 0): by (F1) E is constant, A, D ∈ ℚ[P].
 (c2) α = β = μ; then (A + B)* = A* + B* ≠ 0 (positivity), 2μ + γ + δ = μ + k, so μ + γ + δ = k, and
 4A*B*C*D* = P*(A* + B*).
  • μ = 0: C(4ABD − 1) = P(A + B). (γ, δ) = (k, 0): C ∈ ℚ[P]; (0, k): D ∈ ℚ[P]; 0 < γ < k: 4AB·C*D* = P*(A + B) contradicts (F1).
  • 0 < μ < k: P* divides 4A*B*C*D*, all factors of degree < k: contradicts (F2).
  • μ = k, γ = δ = 0: P* | A*B*, so wlog A* = κP* (F2); then B*(4CDκ − 1) = κP*, so B* = κ'P*. Write A = κP + E_A, B = κ'P + E_B
    with deg E_A, deg E_B < k. Coefficient of P²: 4CDκκ' = κ + κ'. The rest: P·G = C − 4CD·E_A·E_B with
    G := (4CDκ − 1)E_B + (4CDκ' − 1)E_A, deg G < k. If G ≠ 0 the left side has degree k + deg G ≥ k ≥ 1, so the right side is
    non-constant, deg E_A + deg E_B = k + deg G, and P*·G* = −4CD·E_A*·E_B* with deg E_A*, deg E_B* < k: contradicts (F2).
    So G = 0, E_A·E_B = 1/(4D) is a nonzero constant, E_A, E_B are constants, A, B ∈ ℚ[P]. ∎

**Corollary 1.3′ (PROVED).** For every binary cubic form irreducible over ℚ, every ternary cubic norm form, and every norm
form N_{K/ℚ}(x₁ω₁ + … + x_kω_k) of any number field K of degree k ≥ 2 (more generally: every P with irreducible leading form):
every polynomial Type II family valid at one point, and every polynomial Type I family valid on a lattice coset inside an
open cone, is an ET identity in n = P(x) (all ET coordinates lie in ℚ[n]). The cubic norm-form rung — and every
higher-degree norm-form rung — collapses to rung 0 for polynomial ET families. The algebraic structure of K (units, the
splitting n = α·α′·α″) cannot enter a polynomial family with rational coefficients: whatever it does, the family's
coordinates end up in ℚ[n].
*Proof.* Norm forms are irreducible over ℚ (the k linear factors x·ω^{(i)} are permuted transitively by Galois, and no proper
sub-product is rational because the ω^{(i)} are distinct conjugates; for a binary cubic, irreducible over ℚ is the hypothesis).
Apply Theorems 1.1′/1.2′ with P = P*. ∎

**Remark 1.4 (what the degree-2 proof used that is not needed).** SYNTHESIS_SPARKS7 Thm 1.2 (c1) used "Q restricted to the
rational line E = 0 has degree exactly 2"; (F3) replaces it: E | P² + const forces E* | P*². Its (c2) μ = 2 case used a
degree count; (F2) replaces it. Hence the comment "the top-part step fails for degree 3" (SYNTHESIS_SPARKS7 Cor 1.3) is
wrong: the step was "P* prime", which holds in every degree.

## 2. Unit orbits and cusps: what Thm 1.2′ does not cover, and the finiteness lemma

Every cubic field has unit rank ≥ 1, so each n = N(x) ≠ 0 has infinitely many representations (unit orbits), accumulating
at the "cusps" (directions where N* = 0). POINTWISE_BINARYFORM §4.3 left open, for indefinite binary quadratics, whether a
family can be valid on a cusp; the cubic norm forms are cusp-rich in the same way. The tempting mechanism: a polynomial
Type I family valid on L ∩ (a cusp neighbourhood that is forward-invariant under a unit ε ≡ 1 mod M) would prove ES for
every prime of the class represented by N, since every unit orbit enters every such neighbourhood. This is killed by the
plain finiteness of the ES solution set at fixed n:

**Lemma 2.1 (orbit finiteness; PROVED, uses Skolem–Mahler–Lech).** Let K be a number field of degree k with ℚ-basis
ω₁,…,ω_k, N(x) = N_{K/ℚ}(Σx_iω_i), and identify ℚ^k ≅ K. Let ε ∈ O_K^× have infinite order and let T_ε be the identity
component of the Zariski closure of ⟨ε⟩ in R_{K/ℚ}𝔾_m (acting on 𝔸^k by multiplication). Let F ∈ ℚ[x]^m be any
polynomial map (ET coordinates (A, B, C, D), or (x, y, z)) and x₀ ∈ ℤ^k with N(x₀) = n ≠ 0. If F(ε^j x₀) is an ES solution
for 4/n (Type I/II/any) for infinitely many j ∈ ℤ, then for each coordinate F_i there are q ≥ 1, r with F_i constant on T_ε·ε^r x₀ (contained in the Zariski
closure of {ε^{qi + r}x₀ : i ∈ ℤ}).
If K is a cubic field (or real quadratic), T_ε·y = {N = n} (geometrically), so F is constant on the hypersurface N = n,
i.e. (N − n) | (F_i − F_i(x₀)) for every coordinate.
*Proof.* 4/n has finitely many solutions (x ≤ y ≤ z: x ≤ 3n/4, then y ≤ 2xn/(4x − n), z determined), and the ET
coordinates (or x, y, z) are determined by the solution, so each coordinate F_i takes finitely many values on the infinite
set J of valid j; fix a value c taken on an infinite J_c ⊂ J. e(j) := F_i(ε^j x₀) − c is an exponential polynomial
Σ_χ c_χ χ(ε)^j (expand F_i in the conjugate coordinates σ_1(x), …, σ_k(x); multiplication by ε scales σ_s by σ_s(ε)) with
infinitely many zeros, so by Skolem–Mahler–Lech its zero set contains an infinite progression {qi + r : i ≥ 0}; i ↦ e(qi + r)
is again an exponential polynomial and vanishes for all i ≥ 0, hence (Vandermonde) for all i ∈ ℤ. So F_i − c vanishes on
{ε^{qi}·ε^r x₀ : i ∈ ℤ}, whose Zariski closure contains T_{ε^q}·ε^r x₀ = T_ε·ε^r x₀ (finite index does not change the
identity component). (q, r, c depend on i; the statement is per coordinate.)
Cubic K: T_ε ⊂ T := R¹_{K/ℚ}𝔾_m (N(ε) = ±1; replace ε by ε²). T has character module X ⊗ ℚ = (permutation module on the 3
embeddings)/(trivial), which is ℚ-irreducible because Gal acts transitively on 3 points (C₃ or S₃); so T has no proper
non-trivial ℚ-subtori and T_ε = T (positive-dimensional since ⟨ε⟩ is infinite). T(ℂ) ≅ {t₁t₂t₃ = 1} acts simply
transitively on {N = n}(ℂ) = {l₁l₂l₃ = n/c}, which is irreducible. Real quadratic: T is 1-dimensional. ∎
*(Several units.)* Infinitely many valid points in one orbit of a rank-2 unit group: Laurent's theorem (zero sets of
exponential polynomials on ℤ^d are finite unions of cosets of subgroups; Astérisque 147–148, 1987) gives an infinite coset,
hence an infinite-order unit, and the lemma applies. (Not needed below.)

**Corollary 2.2 (orbit-tail families collapse; PROVED).** For a cubic (or real quadratic) norm form N: if a polynomial family
F (any of Type I, Type II, (x, y, z)) is, for infinitely many primes p, valid at infinitely many points of one unit orbit of
a representation of p, then every coordinate of F lies in ℚ[N] (an ET identity in n). In particular a family valid on
L ∩ U for a cusp neighbourhood U with εU ⊂ U, ε ≡ 1 (mod M), collapses.
*Proof.* By Lemma 2.1, F_i ≡ c_i(p) on {N = p} for infinitely many p. Then dF_i ∧ dN vanishes on a Zariski-dense set (the
union of these hypersurfaces: on N = p, F_i − c_i(p) = (N − p)G, so dF_i = G·dN there), hence identically, so F_i and N are
algebraically dependent (Jacobian criterion, char 0). N is non-composite: N − t = c·l₁l₂l₃ − t is irreducible over
\overline{ℚ(t)} (it is linear in l₁ with coprime coefficients c·l₂l₃ and −t), so ℚ(N) is algebraically closed in ℚ(x)
(standard, e.g. Schinzel, *Polynomials with special regard to reducibility*, §3.3), and F_i ∈ ℚ(N). Finally ℚ(N) ∩ ℚ[x] =
ℚ[N]: if F_i = f(N)/g(N) in lowest terms with g non-constant, at a root τ of g the hypersurface N = τ is non-empty and
g(N)F_i = f(N) gives f(τ) = 0, contradiction. ∎

**What is left (exact).** A non-collapsing polynomial family for a cubic norm form can be valid, for each prime, only at
finitely many points of each unit orbit, and (Thm 1.2′) on no lattice coset of an open cone with N* > 0. Unit fundamental
domains can be taken to be finite unions of (Shintani) open cones, so "evaluate at the reduced representative" is covered
by Thm 1.2′ on each cone. The residual validity sets are *power-cusp shells*: regions {|l₁| ≍ |x|, |l₂ l₃| ≍ |x|^κ} with
0 < κ < 2 (the depth along the orbit growing like a fixed multiple of log p), and thin sets near the zero directions Z_F of
the top forms. §3 studies the shells.

## 3. Type I without cones: the unit-group criterion

Iteration (I2). §2 showed the cone hypothesis of Thm 1.2′ is where cusps/shells could hide. Trying to construct a shell
family (weighted degrees with irrational weights on the conjugate coordinates l₁, l₂, l₃, where P's weighted leading part
c·l₁l₂l₃ is *reducible* over ℚ̄, so (F1) is unavailable) led instead to a purely algebraic proof that needs no positivity
region at all: the Type I equation factors as C·(4ABD − 1) = P·(A + B), and P either divides 4ABD − 1 — then A, B, D are
*units modulo P* — or not. For a prime form P the ring ℚ[x]/(P) is a graded domain, whose only units are constants.

**Theorem 3.1 (Type I collapse at one valid point; PROVED, elementary).** Let P ∈ ℚ[x₁,…,x_r] be prime with
(ℚ[x]/(P))^× = ℚ^× (e.g. any homogeneous prime form: an irreducible binary form of any degree, a norm form, an irreducible
indefinite binary quadratic). Let A, B, C, D ∈ ℚ[x] ∖ {0} satisfy 4ABCD = P(A + B) + C identically. Then either all of
A, B, C, D lie in ℚ[P], or (up to swapping A and B) the family is degenerate: A + B = 0, or B = b, D = −1/(4b²), C = −bP
with A arbitrary. Degenerate families are valid nowhere (B = −A, resp. D < 0). Hence **every polynomial Type I family for P
that is valid at one point lies in ℚ[P]**.
*Proof.* ℚ(P) ∩ ℚ[x] = ℚ[P] (if F = f(P)/g(P) in lowest terms with g non-constant, P = τ is non-empty for a root τ of g and
f(τ) = 0, contradiction). Assume A + B ≠ 0 and wlog α ≥ β. The identity is C·(4ABD − 1) = P·(A + B).
(e0) P ∤ 4ABD − 1. P is prime, so 4ABD − 1 | A + B ≠ 0. If A, B, D are all constant, C = P(A + B)/(4ABD − 1) ∈ ℚ[P].
Otherwise deg(4ABD − 1) = α + β + δ ≤ deg(A + B) ≤ α, so B = b, D = d are constants and, if α ≥ 1, A + b = λ(4bdA − 1) with
λ ∈ ℚ: either 4λbd ≠ 1 and A is constant, or 4λbd = 1, λ = −b, i.e. d = −1/(4b²), and then C = P(A + b)/(4bdA − 1) = −bP:
the degenerate family. (Check: 4A·b·(−bP)·(−1/(4b²)) = AP = P(A + b) − bP.)
(e1) P | 4ABD − 1. Then A, B, D are units mod P, hence A ≡ a, B ≡ b, D ≡ d (mod P) with 4abd = 1, and C·H = A + B with
H := (4ABD − 1)/P ≠ 0 (if 4ABD = 1 then A + B = 0). So deg H = α + β + δ − deg P ≤ deg(A + B) ≤ α, i.e. β + δ ≤ deg P. A
non-constant B ≡ b has β ≥ deg P (B − b = P·B₁), likewise D; so (β, δ) ∈ {(0, 0), (deg P, 0), (0, deg P)}, and in the last two
cases B = b + κP resp. D = d + κP with κ ∈ ℚ. Write A = a + P·A₁ (A₁ ≠ 0 unless everything is constant). Using 4abd = 1:
 (i) B = b, D = d: H = A₁/a, so A₁ | A + B = (a + b) + P·A₁, i.e. A₁ | a + b. If a + b ≠ 0, A₁ is constant and A ∈ ℚ[P].
 If a + b = 0 then d = −1/(4a²) = −1/(4b²) and C = (A + B)/H = aP = −bP: the degenerate family.
 (ii) B = b + κP, D = d: H = 4d(aκ + B·A₁). If α ≤ deg P, A₁ is constant. Otherwise deg H = α = deg(A + B), so A + B = G·H
 with G ∈ ℚ, which rearranges to A₁·(4dG·B − P) = a + B − 4dGaκ; the bracket 4dGb + (4dGκ − 1)P is non-zero (b, d ≠ 0), and
 both sides' other factors lie in ℚ[P], so A₁ ∈ ℚ(P) ∩ ℚ[x] = ℚ[P].
 (iii) B = b, D = d + κP: H = 4b(aκ + A₁·D); as in (ii), A₁·(4bG·D − P) = a + b − 4bGaκ, so A₁ ∈ ℚ[P].
In all non-degenerate cases A, B, D ∈ ℚ[P], and C = P(A + B)/(4ABD − 1) ∈ ℚ(P) ∩ ℚ[x] = ℚ[P]. Validity: degenerate families
have B = −A or D < 0. ∎
(The five rearrangements in (i)–(iii) are checked by sympy in scripts/z20_collapse_check.py, section "Thm 3.1".)

**Corollary 3.2 (PROVED).** For every norm form N of every number field of degree ≥ 2 (and every irreducible binary form):
every polynomial ET family, Type I or Type II, that is valid at a single point is an ET identity in n = N(x). No cone, no
positivity region, no direction condition. In particular:
 (a) the cubic norm-form rung collapses completely (binary cubic forms, ternary cubic norm forms, any signature);
 (b) POINTWISE_BINARYFORM §4.3 (indefinite binary quadratics: can a family be valid on a cusp?) is settled negatively for
 polynomial ET families (Type I by Thm 3.1, Type II by SYNTHESIS_SPARKS7 Thm 1.1), and so are §2's power-cusp shells;
 (c) Thm 1.2′ (cones) is subsumed for homogeneous prime P; Lemma 2.1 remains the tool for families given only by
 (x, y, z) ∈ ℚ[x]³ (whose ET coordinates need not be polynomial).

**Remark 3.3 (the dictionary: Type I families ↔ units of ℚ[x]/(P)).** The proof shows what a non-collapsing Type I family
needs: a factorisation 4ABD ≡ 1 in the unit group of the "zero-fibre algebra" ℚ[x]/(P) with non-constant A, B or D, or
divisibility 4ABD − 1 | A + B. For a one-parameter menu n = φ(u) this algebra is MENU_STERILITY's A = ℚ[u]/(φ), an étale
algebra with a huge unit group — exactly the algebra in which Theorem A (witness reciprocity) runs; e.g. MENU_STERILITY
Thm B (n = 48X⁴ + 1) lives on units of ℚ[X]/(48X⁴ + 1). For norm forms in k variables the zero fibre {N = 0} is a cone over
a geometrically reducible but ℚ-irreducible variety, and its coordinate ring has no units: nothing to factor with. Where
units do exist — n = uv + 1 (u is a unit mod P), n = 4abd − a − b — the parameters encode a divisor of n ± const (B2).
So, for polynomial ET families, *the menu ladder's positive-density rungs are sorted by (ℚ[x]/(P))^×*. (Assessment for the
last sentence; the theorem is the precise statement.)
