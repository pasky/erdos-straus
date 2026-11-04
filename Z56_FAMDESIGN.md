# Z56_FAMDESIGN — a (★) sub-family with a big provable genus main term

Status: z56 lane FAMDESIGN (brief `z52bbriefs/z56_lanes.md` §3, common rules `z53_depth.md`). Internal, internally
reviewed only (§8). **ES is OPEN; nothing here proves or disproves ES or (★) at any infinite set of primes.**
Labels: PROVED / CONDITIONAL / CERTIFIED / EVIDENCE / CONJECTURE / Assessment. Scripts `scripts/z56_famdesign_*`, data
`data/z56/famdesign/`.

## 0. Summary

* **Design answer (target (i)).** The provable genus share is not limited to Thm U's rectangle. Burgess sees the genus
  characters of a (★) pair (o, e) (o odd, e even) whenever the larger entry exceeds (smaller entry · p)^{1/4}: fix the
  smaller entry, sum over the larger one (Thm U's slices, plus *mirror slices* with e fixed). Tiling that region with
  Thm-U-type rectangles, for all arithmetic types (o ≡ 3 (4), e ≡ 0 (4), non-squarefree entries) and with the exact
  Euler-product average of L(1, χ_{−po}) over the outer variable, gives
  **Theorem V (PROVED; Burgess + Heath-Brown's quadratic large sieve):** for the family 𝔊* = {(o, e): max⁴ > min·p},
  M_𝔊*(p) ≥ (5/(4π²) − o(1))log²p ≈ 0.1267 log²p, hence **M_gen(p) ≥ (5/6 − o(1))·M₀(p)** at every large prime
  p ≡ 1 (4) (Thm U: 2/(3π⁴) ≈ 0.0068 = 4.5 % of M₀). With Burgess alone (and effective p₀): 29/(30π²) ≈ 0.0979 (64 % of
  M₀). On compact rectangles inside the region the main term is an asymptotic, (3/π²)·area·log²p. The excluded
  density-area sixth is the **Burgess corner** max(o, e) ≤ (min(o, e)·p)^{1/4} (both entries ≲ p^{1/3}, C ≳ p^{1/3}),
  where the slice cross terms are products of χ_p-twisted sums shorter than p^{1/4} (Assessment: the GRH gap).
  Also PROVED: Cor V1 (Thm U's own proof, tiled over its admissible trapezoid: 64/(45π⁴) ≈ 0.0146).
* **Zero sets (target (ii); CERTIFIED).** A new all-solution engine (validated against brute force, the census and CROSSF's
  scanner line by line) and a fast exhaustive decider: R_𝔊*(p) = 0 at exactly **38 primes p ≡ 1 (4) ≤ 10¹⁰**, the last
  **564 661 441**, and at none of the 57 806 primes in the windows and samples above 10¹⁰ (up to 10¹⁴); the Burgess-only family 𝔊*_{1/15}
  has 317 zeros ≤ 10¹⁰ (last 6 122 428 657). For comparison the Thm U standard-window family vanishes at 39 % → 8.5 % →
  4.8 % of primes at 10⁸ → 10¹² → 10¹³ (CROSSF, reproduced exactly). Every 𝔊*-zero above 10⁷ has R = 2 with its unique
  solution in the corner. Model scale of the last zero (Assessment): ~10^{8.3} for 𝔊* vs ~10^{118} for Thm U's family.
* **Remainder structure (target (iii)).** 𝔊* contains every solution with 64C³ ≤ p (PROVED), so two-thirds of its density
  consists of *complete* level sets Σ_C D⁻_{4C}(4Cp + 1) (multiplicative twisted divisor sums σ_χ(4Cp + 1), free modulus
  4C, no windows); the rest has Thm U's single-integer slice structure. Every family keeps the tied divisor event (B2).
  EVIDENCE: the (★)-zero primes lose their genus mass mainly in the corner (M_K at 28 % of its density vs 88 % for M_G).
* **Ranked table** §6. **Screens:** T1 pass (§3.8), 8/131 n/a, B2 fail (main term only), fixed-p pass.
  **Verdict: strengthened** on the main-term side; nothing about the order-≥3 remainder. **ES is OPEN.**

## 1. Setting, notation, statements attacked

p ≡ 1 (mod 4) prime, L := log p. A **(★) solution** is (o, e, C) ∈ ℕ³ with o odd, e even and
  p = 4oeC − o − e
(any positive solution of 4uBC − u − B = p has u + B odd, so this is the general solution with {u, B} = {o, e}). Each
solution gives the two ordered pairs (u, B) = (o, e), (e, o) of FRONTIER §2.1, so R(p) = 2·#{solutions}; gcd(o, e) = 1
automatically (it divides p and o, e < p). For a set 𝔊 of pairs (o, e):
  R_𝔊(p) := 2·#{solutions with (o, e) ∈ 𝔊},  hits_𝔊(p) := R_𝔊(p)/2,
  M_𝔊(p) := Σ_{(o,e) ∈ 𝔊} W(o, e),  W(o, e) := 2·(s(q)/φ(q))·1[p·a ∈ ((ℤ/q)^×)²],  q = 4oe, a = −(o + e),
i.e. M_𝔊 is the genus (order ≤ 2) part of R_𝔊 = M_gen of `SINGLE_P_COUNT` §2 restricted to 𝔊 (the factor 2 counts both
orders; all terms ≥ 0, so M_𝔊 ≤ M_gen for every 𝔊). Write e = 2^k e′ with e′ odd, k ≥ 1.

*The family and its region.* With P := min(o, e), Q := max(o, e) put
  **𝔊* := {(o, e) : Q⁴ > P·p}** ("the larger entry exceeds (smaller entry · p)^{1/4}"; exact integer inequality, o = 1
allowed), 𝔊*_λ := 𝔊* ∩ {P^{15} > p} for λ = 1/15 (and P > p^λ in general). In log-coordinates a := log o/L, b := log e/L
(pairs in 𝒫(p) have a + b < 1 + o(1)) its interior region is
  **G := {(a, b) ∈ (0, 1)² : a + b < 1, max(a, b) > (1 + min(a, b))/4}**,  G_λ := G ∩ {min(a, b) > λ};
the proofs integrate over (rectangles inside) G_λ, and every pair with (a, b) ∈ G_λ lies in 𝔊*_λ. The complement of G in
the triangle, the **Burgess corner**
K := {max(a, b) ≤ (1 + min(a, b))/4} (vertices (0,0), (1/4,0), (1/3,1/3), (0,1/4)), has area 1/12; area(G) = 5/12 of
the triangle's 1/2, and for 0 ≤ λ ≤ 1/15, area(G_λ) = 5/12 − 3λ/2 + 5λ²/4 (area(G_{1/15}) = 29/90). **Every solution
with 64C³ ≤ p lies in 𝔊*** (PROVED): if Q⁴ ≤ P·p ≤ Q·p then Q ≤ p^{1/3} and PQ ≤ Q² ≤ p^{2/3}, whereas a solution has
PQ = (p + P + Q)/(4C) > p/(4C) ≥ p^{2/3} when 4C ≤ p^{1/3}. So the corner is a large-C phenomenon (C > p^{1/3}/4).

*Arithmetic types.* **A**: all pairs. **S**: o squarefree, e′ squarefree. **U** (= `Z53_GENUSLVAL` Thm U's type):
o ≡ 1 (4) squarefree, k = 1, e′ squarefree. The Thm U family 𝔉 is U ∩ (rectangle); CROSSF's "standard window" is
U ∩ {p^{1/12} < o ≤ p^{1/3}/2, p^{1/3} < e/2 ≤ p^{2/3}/4}.

*Densities.* M₀(p) := Σ_{𝒫(p)} 1/φ(4uB) = (3/(2π²) + o(1))L² (`BM_CORRECTED_COUNT` Thm 2.2) is the expected count at a
random prime; per unit (a, b)-area (both orders) the pair density is 3/π² for type A. For S and U (Assessment; elementary
mean-value computation, not needed for any proof): a pair contributes 2·(2/φ(q)) = 2^{1−k}/(φ(o)φ(e′)) on average over
primes p ≡ 1 (4) if it is 2-adically compatible ((o ≡ 1 (4), k = 1) or (o ≡ 3 (4), k ≥ 2); Σ_{k≥2}2^{1−k} = 1) and 0
otherwise; Σ_{e′ odd squarefree, (e′,o)=1} 1/φ(e′) ~ (φ(o)/(2o))·log and Σ_{o odd squarefree} 1/o ~ (4/π²)·log give 2/π²
for S, and half of it, 1/π², for U (only o ≡ 1 (4)).

**Targets of the lane (brief).** (i) a family 𝔊 with an unconditional M_𝔊(p) ≥ (c − o(1))L² at every large prime
p ≡ 1 (4), c as large as possible; (ii) a small empirical zero set of R_𝔊; (iii) an exploitable remainder.

**Why this is not closed.** Thm U (FRONTIER §7.4, closed) proves one rectangle of type U, c = 2/(3π⁴) ≈ 0.00684,
≈ 4.5 % of M₀. Nothing in the closed list or FRONTIER §6 concerns the *size* of the provable genus share. This lane is
main-term engineering (B3): it does **not** touch the order-≥3 remainder (B2) and cannot by itself give R_𝔊 ≥ 1.

## 2. Results at a glance (ranked table: §6)

* **Corollary V1 (PROVED; from Thm U's proof by tiling).** U ∩ ℛ₁(1/15), ℛ₁(λ) := {a > λ, b > (1+a)/4, a + b < 1}:
  M ≥ (64/(45π⁴) − o(1))L² ≈ 0.0146 L².
  *Proof.* Thm U's proof (`Z53_GENUSLVAL` §2.4–2.7) bounds, for each rectangle (α₀, α₁] × (β, γ] satisfying its (C1)–(C3)
  with margins, the contribution of the U-type pairs with u ∈ (p^{α₀}, p^{α₁}], w = e/2 ∈ (p^β, p^γ] from below by
  ((8/π⁴)(α₁ − α₀)(γ − β) − o(1))L² (its last display bounds the subfamily sum, all of whose terms are ≥ 0). A closed
  rectangle inside the open set ℛ₁(1/15) satisfies (C1) γ < 1 − α₁ and (C2) β > (1 + α₁)/4 with margin, and (C3)
  α₀ > (1 + α₁)/16 once α₁ − α₀ is small, because a > 1/15 ⟺ a > (1 + a)/16. Tile ℛ₁(1/15) from inside by finitely many
  disjoint such rectangles, add the bounds (disjoint pair sets, nonnegative terms), and use
  area(ℛ₁(1/15)) = ∫_{1/15}^{3/5}(3/4 − 5a/4)da = 8/45. ∎ (Thm U optimised a single rectangle; its admissible set is the
  trapezoid.)
* **Theorem V (PROVED; §3).** For every η > 0 and every prime p ≡ 1 (4), p ≥ p₀(η, λ):
  M_{A∩G_λ}(p) ≥ ((3/π²)·area(G_λ) − η)L²; with λ = 1/15 using Burgess only (constant **29/(30π²) ≈ 0.0979**,
  p₀ effective), and for every fixed λ > 0 using also Heath-Brown's quadratic large sieve (constant → **5/(4π²) ≈ 0.1267**
  as λ → 0: for each η choose λ with (3/π²)(area(G) − area(G_λ)) < η/2).
  On every closed rectangle Q ⊂ G_λ the asymptotic M_{A∩Q}(p) = ((3/π²)area(Q) + o(1))L² holds (no p-dependent
  fluctuation in the main term on compact rectangles). **Corollary:** M_gen(p) ≥ (5/(4π²) − o(1))L² = (5/6 − o(1))·M₀(p)
  — 18.5 × Thm U's constant; the excluded *density-area* share 1/6 is exactly the Burgess corner K (no statement is made
  about the actual genus mass in K at a given p).

## 3. Proof of Theorem V

### 3.1 Inputs and conventions

Fix an integer r ≥ 3 and ε ∈ (0, 1/100); θ := (r + 1)/(4r²) + ε, κ := 1/r, τ := rθ (→ 1/4 as r → ∞, ε → 0). "≪" and
p^{o(1)} as in `Z53_GENUSLVAL` §2.1 (constants depend on r, ε and the fixed exponents only; τ(m), 2^{ω(m)} ≤ p^{o(1)} for
m ≤ p²). Characters below are real; "primitive of conductor f" includes f = 1 (the constant 1).
* **(Bu)** Burgess for primitive χ of cube-free conductor f > 1 (all r): |Σ_{M<n≤M+N}χ(n)| ≤ C N^{1−κ} f^{θ}, C = C(r, ε)
  effective (`Z53_GENUSLVAL` §2.1, with sources).
* **(Bu8) Lemma 3.1 (PROVED).** The same bound with C replaced by 4C holds for primitive χ of conductor f = 8f′, f′ odd
  squarefree. *Proof.* If f′ = 1, |Σ| ≤ 4 ≤ 4C N^{1−κ}f^θ. Else χ = χ₈′χ_{f′} (χ_{f′} primitive mod f′) and
  Σ_{M<n≤M+N}χ(n) = Σ_{c ∈ (ℤ/8)^×}χ₈′(c)·χ_{f′}(8)·Σ_{t ∈ I_c}χ_{f′}(t + s_c), with s_c ≡ c·8⁻¹ (mod f′) and I_c an
  interval of ≤ N/8 + 1 ≤ N integers (N ≥ 2; N = 1 is trivial); apply (Bu) to each of the four shifted sums. ∎
* **(HB)** Heath-Brown, *A mean value estimate for real character sums*, Acta Arith. 72 (1995) 235–275, **Theorem 1**
  (checked against the paper, p. 237): for positive integers M, N and complex a_n,
  Σ*_{m≤M} |Σ*_{n≤N} a_n (n/m)|² ≪_ε (MN)^{ε}(M + N) Σ*_{n≤N}|a_n|², where Σ* runs over positive odd squarefree integers
  and (n/m) is the Jacobi symbol. Used only in Theorem V(b). (Effectivity of its implied constant: not audited.)
* `Z53_GENUSLVAL` **Lemma 2.1** (L-series tails for χ = χ*·1[(·, e) = 1], χ* primitive with a Burgess bound, e squarefree)
  and **Lemma 2.2** (hyperbola with two such characters) are used verbatim; they only use the partial-sum bound, so they hold
  for conductors 8f′ by (Bu8) with C ↦ 4C.

### 3.2 Lemma 3.2 (genus weight of a general pair; PROVED)

Let o odd, e = 2^k e′ (k ≥ 1, e′ odd), gcd(o, e) = 1, p ∤ oe, 4oe − o − e ≤ p. Then (o, e), (e, o) ∈ 𝒫(p) are distinct,
have the same q, a, and
  W(o, e) = 2^{2−k}·(2^{ω(o)+ω(e′)}/(φ(o)φ(e′)))·1[(i)]·1[(ii)]·1[(iii)],
  (i) (−po/ℓ) = 1 for every prime ℓ | e′;  (ii) (−pe/ℓ) = 1 for every prime ℓ | o;  (iii) o + e ≡ −p (mod 8).
(iii) is equivalent to exactly one of: o ≡ 1 (4), k = 1, e′ ≡ e′₀ := (−p − o)/2 (mod 4); o ≡ 4 − p (8), k = 2;
o ≡ −p (8), k ≥ 3. For fixed e it says o ≡ c_e := −p − e (mod 8).
*Proof.* q = 2^{k+2}·o·e′ with k + 2 ≥ 3; (ℤ/q)^× ≅ (ℤ/2^{k+2})^× × ∏_{ℓ^v ‖ oe′}(ℤ/ℓ^v)^×, so s(q) = 4·2^{ω(o)+ω(e′)},
φ(q) = 2^{k+1}φ(o)φ(e′). pa is coprime to q (gcd(a, o) = gcd(e, o) = 1, likewise for e′; a odd; p ∤ q). A unit is a square
mod q iff it is ≡ 1 (8) and a quadratic residue mod every odd ℓ | q (Hensel). Mod ℓ | e′: pa ≡ −po; mod ℓ | o: pa ≡ −pe;
mod 8: −p(o + e) ≡ 1 ⟺ o + e ≡ −p (p² ≡ 1). Case analysis of o + 2^k e′ ≡ −p (8) with p ≡ 1 (4): k = 1 forces o ≡ 1 (4)
and then 2e′ ≡ −p − o (8); k = 2 gives o ≡ −p + 4; k ≥ 3 gives o ≡ −p. ∎

Discriminants. For odd o, p ∤ o, write o = o₁s² (o₁ squarefree) and let D_o be the discriminant of ℚ(√(−po₁))
(D_o = −po₁ if o₁ ≡ 3 (4), −4po₁ if o₁ ≡ 1 (4)). For e = 2^k e′, e′ = e′₁t², let E_e be the discriminant of
ℚ(√(−2^{k mod 2}pe′₁)) (−8pe′₁ for k odd; −pe′₁ or −4pe′₁ for k even). Then for every odd prime ℓ ∤ oe′p:
(−po/ℓ) = χ_{D_o}(ℓ) and (−pe/ℓ) = χ_{E_e}(ℓ); and for odd n: χ_{D_o}(n) = (−p/n)(o/n) when gcd(n, o) = 1,
χ_{E_e}(n) = (−2^k p/n)(e′/n) when gcd(n, e′) = 1 (Jacobi symbols; (s²/n) = 1).

### 3.3 Lemma 3.3 (slice expansions; PROVED)

Put ρ(m; χ) := 2^{ω(m)}·1[χ(ℓ) = 1 ∀ℓ | m]/φ(m). Fix K := ⌊ε log₂ p⌋.
(a) *Region-1 slice (o fixed).* Let o odd, p ∤ o, 1 ≤ Y < X with 8oX ≤ p. Then
  𝒮₁(o; Y, X) := Σ_{Y<e≤X, e even, gcd(e,o)=1, v₂(e)≤K} W(o, e)
   = (1/φ(o))·Σ_{k∈𝒦_o, k≤K} 2^{2−k}c_k Σ_{d | rad o} Σ_{j∈J_k} ε_{k,d,j}·S_{η_{d,j}}(o; Y/2^k, X/2^k),
  S_η(o; y, x) := Σ_{y<m≤x, gcd(m, 2op)=1} η(m)ρ(m; χ_{D_o}),  η_{d,j} := (·/d)χ₋₄^j,
with 𝒦_o = {1} (o ≡ 1 (4)), {2} (o ≡ 4 − p (8)), {3, 4, …} (o ≡ −p (8)); J_1 = {0, 1}, c_1 = ½; J_k = {0}, c_k = 1
(k ≥ 2); ε_{k,d,j} := (−2^k p/d)χ₋₄(e′₀)^j ∈ {±1}, ε_{k,1,0} = 1. The coefficient of the principal η = 1 is
T_o := Σ_{k∈𝒦_o, k≤K}2^{2−k}c_k ∈ {1, 1 − 2^{2−K}} (p large, so that K ≥ 3).
(b) *Region-2 slice (e fixed).* Let e = 2^k e′, p ∤ e′, 1 ≤ Y < X with 8eX ≤ p. Then
  𝒮₂(e; Y, X) := Σ_{Y<o≤X, o odd, gcd(o,e′)=1} W(o, e) = (2^{−k}/φ(e′))·Σ_{d′ | rad e′} Σ_{ψ} (−p/d′)ψ(c_e)·S′_{(·/d′)ψ}(e; Y, X),
  S′_η(e; y, x) := Σ_{y<m≤x, gcd(m, 2e′p)=1} η(m)ρ(m; χ_{E_e}),
ψ running over the four real characters 1, χ₋₄, χ₈, χ₋₈ (primitive, conductors 1, 4, 8, 8).
*Proof.* Lemma 3.2 with 1[(ii)] = 2^{−ω(o)}Σ_{d|rad o}(−pe/d) = 2^{−ω(o)}Σ_d (−2^kp/d)(e′/d) and
2^{ω(e′)}1[(i)] = 2^{ω(e′)}1[χ_{D_o}(ℓ) = 1 ∀ℓ | e′] in (a) (and 1[e′ ≡ e′₀ (4)] = ½Σ_j χ₋₄(e′₀)^jχ₋₄(e′)^j for k = 1);
in (b) 1[(i)] = 2^{−ω(e′)}Σ_{d′|rad e′}(−p/d′)(o/d′), 2^{ω(o)}1[(ii)] = 2^{ω(o)}1[χ_{E_e}(ℓ) = 1 ∀ℓ | o] and
1[o ≡ c_e (8)] = ¼Σ_ψ ψ(c_e)ψ(o) for odd o. 8oX ≤ p gives 4oe − o − e ≤ p. The weight 2^{2−k}/(φ(o)φ(e′)) collects the
prefactors (in (b): 2^{2−k}·¼ = 2^{−k}). ∎

### 3.4 Proposition 3.4 (one slice: only η = 1 survives; PROVED)

There is δ = δ(r, ε) > 0 such that, uniformly:
(a) for o odd, p ∤ o, o ≤ p, every η ∈ 𝔈_o := {η_{d,j} : d | rad o, j ∈ {0, 1}} and every p^{−ε}Y₀ ≤ y < x ≤ p with
Y₀ := (16op)^{τ}p^{6ε}:
  S_η(o; y, x) = 1[η = 1]·H_o(1)L(1, χ_{D_o})·log(x/y) + O(p^{−δ});
(b) for e = 2^k e′ ≤ p, every η ∈ 𝔈′_e := {(·/d′)ψ : d′ | rad e′, ψ ∈ {1, χ₋₄, χ₈, χ₋₈}} and Y′₀ := (64e′p)^τ p^{6ε} ≤ y < x ≤ p:
  S′_η(e; y, x) = 1[η = 1]·H′_e(1)L(1, χ_{E_e})·log(x/y) + O(p^{−δ}).
Here H_o(1) := ∏_ℓ h_ℓ, with h_ℓ = (1 − 1/ℓ)(1 − χ_{D_o}(ℓ)/ℓ) for ℓ | 2op and h_ℓ = 1 + χ_{D_o}(ℓ)/ℓ² otherwise (H′_e
likewise with E_e and ℓ | 2e′p).
*Proof.* This is `Z53_GENUSLVAL` Prop 2.4 (and the non-squarefree bookkeeping of its Prop C) with the following data.
(1) *Factorisation.* For χ := χ_{D_o}, g(m) := 1[(m, 2op) = 1](m/φ(m))Σ_{b | m, μ²(b)=1}χ(b) = m·ρ(m; χ) for (m, 2op) = 1, and
g = 1 ∗ χ ∗ h with h multiplicative: at ℓ | 2op, h(ℓ) = −(1 + χ(ℓ)), h(ℓ²) = χ(ℓ), h(ℓ^j) = 0 (j ≥ 3); at ℓ ∤ 2op (χ(ℓ) = ±1)
the local series [1 + (1 + χ(ℓ))(ℓ/(ℓ−1))Y/(1 − Y)](1 − Y)(1 − χ(ℓ)Y) gives h(ℓ) = (1 + χ(ℓ))/(ℓ − 1),
h(ℓ²) = χ(ℓ)(1 − (1 + χ(ℓ))ℓ/(ℓ − 1)) (= −(ℓ+1)/(ℓ−1) or −1), h(ℓ^j) = 0 (j ≥ 3). So |h(ℓ^j)| ≤ 2 (ℓ ≥ 3), h(ℓ) ≤ 2/(ℓ−1)
at good primes, and Σ_c|h(c)|c^{θ′−1} ≤ 2^{O(ω(2op))}·∏_{ℓ≥3}(1 + 2ℓ^{θ′−1}/(ℓ−1) + 2ℓ^{2θ′−2}) = p^{o(1)} for θ′ = 1/4.
The values h_ℓ above are Σ_j h(ℓ^j)ℓ^{−j}; e.g. at good ℓ with χ(ℓ) = 1: 1 + 2/(ℓ(ℓ−1)) − (ℓ+1)/(ℓ²(ℓ−1)) = 1 + 1/ℓ².
Then S_η(o; y, x) = Σ_{c≥1}(η(c)h(c)/c)[Φ_η(x/c) − Φ_η(y/c)], Φ_η(t) := Σ_{ab≤t}η(a)(ηχ)(b)/(ab), exactly as in Prop 2.4(1).
(2) *Characters and conductors.* η_{d,j} is primitive of conductor f_F = 4^j d (d odd squarefree; f_F = 1 iff η = 1).
For odd n, quadratic reciprocity gives χ(n) = χ₋₄(n)^{1+[o₁≡3 (4)]}(n/o₁)(n/p), so with g := gcd(d, o₁),
  ηχ(n) = χ₋₄(n)^{ι}·(n/(d o₁/g²))·(n/p)·1[gcd(n, g) = 1]  (n odd; ι ∈ {0, 1}),
so the Dirichlet character ηχ (a product of two characters) is χ*_G·1[gcd(·, e_G) = 1] with χ*_G primitive of conductor
f_G = 4^{ι}(do₁/g²)p and some squarefree e_G | 2g (its values on odd n determine χ*_G; at n = 2 only the indicator can
change). **p | f_G, so ηχ is non-principal for every η ∈ 𝔈_o** (the decisive
square-sensitive step, §3.8). Writing d = g·d₂ with d₂ | s (the primes of d not dividing o₁ divide s): f_F·f_G ≤ 16·d·(do₁/g²)·p =
16·(d²o₁/g²)·p = 16·d₂²o₁·p ≤ 16·o·p, i.e. **f_F·f_G ≤ 16·o·p**. All conductors are 4^{≤1}·(odd squarefree): cube-free, so (Bu) applies.
(b) is identical with χ := χ_{E_e}, m odd coprime to e′p, η = (·/d′)ψ of conductor f_F = d′·f_ψ ≤ 8d′, and for odd n
χ_{E_e}(n) = ψ₁(n)(n/e′₁)(n/p) with ψ₁ a character mod 8, so ηχ = χ*_G·1[gcd(·, e_G) = 1] (e_G | 2g′ squarefree) with
χ*_G = ψ₂·(·/(d′e′₁/g′²))·(·/p), g′ = gcd(d′, e′₁), ψ₂ mod 8; f_G ≤ 8(d′e′₁/g′²)p, and with d′ = g′d′₂, d′₂ | t:
f_F f_G ≤ 64·d′₂²e′₁·p ≤ 64e′p; p | f_G. Conductors 8·(odd squarefree) occur: use (Bu8).
(3) *η ≠ 1.* As Prop 2.4(3): K_F K_G ≤ p^{o(1)}(f_F f_G)^θ ≤ p^{o(1)}(16op)^θ; for c ≤ C₀ := p^{ε}, (y/c)^κ ≥
(Y₀p^{−2ε})^κ = (16op)^{θ}p^{4κε} ≥ K_FK_G p^{κε}·p^{κε} for large p, so Lemma 2.2(a) gives |Φ_η(x/c) − Φ_η(y/c)| ≤
2(2r + 3)p^{−κε/2}; the c > C₀ part is ≤ 2(1 + log p)²C₀^{−1/4}Σ_c|h(c)|c^{−3/4} = p^{−ε/4+o(1)}. (4) *η = 1.* Lemma 2.2(b)
with G = χ and z = p^{ε}: Φ_1(x/c) − Φ_1(y/c) = L(1, χ)log(x/y) + O(p^{−κε/2}) (the constants γ_E L + L′ cancel in the
difference); summing with weights h(c)/c, H_o(1) = Σ_c h(c)/c. ∎

### 3.5 Lemma 3.5 (the main term as one Dirichlet series; PROVED)

With β(n) := ∏_{ℓ | n}(1 + 1/ℓ) and, for a real character χ and an integer S,
  𝓛(χ; S) := L^{(S)}(1, χ)·Σ_{(d, S)=1} μ²(d)χ(d)/d²  (= "Σ_{(n,S)=1} χ(n)β(n)/n", the Euler product of the formal series)
(L^{(S)}: Euler factors at ℓ | S removed), one has
  (1/φ(o))·H_o(1)L(1, χ_{D_o}) = ½(1 − 1/p)·(1/o)·𝓛(χ_{D_o}; 2op),
  (2^{−k}/φ(e′))·H′_e(1)L(1, χ_{E_e}) = ½(1 − 1/p)·(1/e)·𝓛(χ_{E_e}; 2pe′),
and 𝓛 > 0. *Proof.* L(1, χ)H_o(1) = ∏_{ℓ|2op}(1 − 1/ℓ)·L^{(2op)}(1, χ)·∏_{ℓ∤2op}(1 + χ(ℓ)ℓ^{−2}) (the factors (1 − χ(ℓ)/ℓ) at
ℓ | 2op cancel L's Euler factors; the last product converges absolutely), ∏_{ℓ∤2op}(1 + χ(ℓ)ℓ^{−2}) = Σ_{(d,2op)=1}μ²(d)χ(d)/d²,
and ∏_{ℓ|2op}(1 − 1/ℓ) = ½(1 − 1/p)φ(o)/o. Locally (1 + χℓ^{−2})(1 − χ/ℓ)^{−1} = Σ_m χ^mβ(ℓ^m)ℓ^{−m}, whence the name.
Positivity: L(1, χ) > 0 and every factor is > 0. Same for e (∏_{ℓ|2pe′}(1 − 1/ℓ) = ½(1 − 1/p)φ(e′)/e′). ∎

### 3.6 Proposition 3.6 (averages over the outer variable; PROVED)

Let 0 < α₀ < α₁ < 1, O_i := p^{α_i}, and suppose **(C3)** α₀ > τ²(1 + α₁) + 4ε (Burgess version) or **(C3-HB)** α₀ ≥ λ
for a fixed λ > 0 (HB version). Then
  (a) Σ_{O₀<o≤O₁, o odd} 𝓛(χ_{D_o}; 2op)/o = (6/π²)·log(O₁/O₀) + O(1);
  (b) Σ_{O₀<e≤O₁, e even, v₂(e)≤K} 𝓛(χ_{E_e}; 2pe′)/e = (1 − 2^{−K})(6/π²)·log(O₁/O₀) + O(1),
the latter under the same hypothesis with α₀ replaced by α₀ − ε.
*Proof of (a).* (1) *Truncation.* For odd o ≤ O₁ put χ := χ_{D_o} (conductor ≤ 4op ≤ 4p^{1+α₁}), N := p^{ν},
ν := τ(1 + α₁) + 3ε. Splitting the d-sum at p^{ε} and using Lemma 2.1 (χ·1[(·, 2o) = 1]; τ(rad 2o) = p^{o(1)}) for the
tails Σ_{m>N/d}, and |Σ_{m≤t}χ(m)/m| ≤ 1 + log t, |L^{(2op)}(1, χ)| ≤ p^{o(1)}(1 + log p):
  𝓛(χ; 2op) = Σ_{d≤p^ε}Σ_{m≤N/d} μ²(d)χ(dm)/(d²m)·1[(dm, 2op) = 1] + O(p^{−κε+o(1)} + p^{−ε+o(1)}),
since K_χ(N/d)^{−κ} ≤ p^{θ(1+α₁)+o(1)}(Np^{−ε})^{−κ} = p^{−2κε+o(1)}. For odd n = dm with gcd(n, o) = 1,
χ(n) = (−p/n)(o/n), and (o/n) = 0 when gcd(n, o) > 1, so the truncated sum is
Σ_{d≤p^ε, m≤N/d, dm odd} (μ²(d)/(d²m))(−p/dm)(o/dm). (2) *Average.* Summing over o with weight 1/o, the inner sum is
V(n) := Σ_{O₀<o≤O₁, o odd}(o/n)/o, n = dm odd. If n = s² is a square, (−p/n) = 1[p ∤ s] and
V(s²) = Σ_{o odd, (o,s)=1}1/o = (φ(s)/(2s))log(O₁/O₀) + O(τ(s)). The squares n = dm = s² (d | s squarefree, m = s²/d)
contribute ½log(O₁/O₀)·Σ_{s odd, p∤s}(φ(s)/s)s^{−2}Σ_{d|s, μ²(d)=1}1/d (truncations cost O(N^{−1/2} + p^{−ε})·L), and
Σ_{d|s}μ²(d)/d = β(s²) = ∏_{ℓ|s}(1 + 1/ℓ), so the s-sum is Σ_{s odd}∏_{ℓ|s}(1 − ℓ^{−2})/s² · (1 + O(p^{−2})) =
∏_{ℓ odd}(1 + ℓ^{−2}) + O(p^{−2}) = (ζ(2)/ζ(4))·(4/5) = 12/π². Total ½·(12/π²)log(O₁/O₀) + O(1). (3) *Non-squares, Burgess.*
n = n₁m′² with n₁ > 1 squarefree: (o/n)1[o odd] = ψ(o) with ψ := (·/n₁)·1[(·, 2m′) = 1], (·/n₁) primitive of conductor
n₁ (cube-free). By (Bu) and Möbius over the divisors of 2m′, |Σ_{o≤t}ψ(o)| ≤ τ(2m′)C t^{1−κ}n₁^{θ}; partial summation over
(O₀, O₁] gives |V(n)| ≤ (2 + r)τ(2m′)C n^{θ}O₀^{−κ}. With weights Σ_{dm=n}μ²(d)/(d²m) = β(n)/n ≤ 2^{ω(n)}/n:
Σ_{n≤N non-square}(β(n)/n)|V(n)| ≤ p^{o(1)}N^{θ}O₀^{−κ} = p^{θν−κα₀+o(1)}, and θν < κα₀ ⟸ α₀ > τν = τ²(1+α₁) + 3τε. (3-HB)
Write o = o₂t², o₂ squarefree: V(n) = Σ_{t odd, (t, n) = 1}t^{−2}Σ_{o₂}(o₂/n₁)1[(o₂, 2m′) = 1]/o₂ over o₂ ∈ (O₀/t², O₁/t²].
Terms with t > p^{λ/4} contribute ≤ p^{−λ/4}(1 + L) in total (per n). For t ≤ p^{λ/4} the o₂-range starts above p^{λ/2}. If
n₁ ≤ p^{ε₁} (ε₁ := λ/8): Pólya–Vinogradov/periodicity with μ²(o₂) = Σ_{f²|o₂}μ(f) gives |Σ_{o₂≤t′}μ²(o₂)ψ(o₂)| ≪ τ(2m′)n₁t′^{1/2},
so the inner sum is ≪ τ(2m′)p^{ε₁}·p^{−λ/4}. If n₁ > p^{ε₁}: in dyadic blocks n₁ ~ N₁, o₂ ~ O′ (O′ ≥ p^{λ/2}),
Cauchy–Schwarz and (HB) with a_{o₂} = 1[(o₂, 2m′) = 1]/o₂ give Σ_{n₁~N₁}n₁^{−1}|Σ_{o₂~O′}a_{o₂}(o₂/n₁)| ≪_{ε′}
N₁^{−1/2}((N₁O′)^{ε′}(N₁ + O′)/O′)^{1/2} ≤ p^{2ε′}(p^{−λ/4} + p^{−ε₁/2}). Summing O(L²) dyadic blocks, over m′ with weight
m′^{−2}·2^{ω(m′)}, and over t: the non-square part is ≪ p^{3ε′ − λ/16}L^{O(1)} = o(1) for ε′ < λ/100. (In the HB version the
truncation N = p^{ν} with ν = τ(1 + α₁) + 3ε is unchanged; only the bound for V(n) changes.)
*Proof of (b).* For each k ≤ K, e = 2^k e′ with e′ odd in (O₀2^{−k}, O₁2^{−k}] (lower end ≥ p^{α₀−ε}), weight 1/e = 2^{−k}/e′,
and for odd n coprime to e′: χ_{E_e}(n) = (−2^kp/n)(e′/n) (§3.2); |E_e| ≤ 8pe′. Steps (1)–(3) apply verbatim with e′ in
place of o (squares n = s²: (−2^kp/s²) = 1[p ∤ s]), giving 2^{−k}(6/π²)log(O₁/O₀) + O(2^{−k}) per k, the O(2^{−k}) uniform in k ≤ K (all bounds of steps (1)–(3) are
uniform in the shift e′ ↦ 2^k e′ since 2^k ≤ p^{ε}); summing over k ≤ K gives the error O(1). ∎

### 3.7 Proof of Theorem V

*Rectangles.* Call a closed rectangle Q = [α₀, α₁] × [β₀, β₁] (a = log o/L, b = log e/L) **type 1** if (C1) α₁ + β₁ < 1,
(C2) β₀ > τ(1 + α₁) + 8ε, and (C3) or (C3-HB) holds for (α₀, α₁); **type 2** if (C1), (C2′) α₀ > τ(1 + β₁) + 8ε, and
(C3)/(C3-HB) holds for (β₀ − ε, β₁). Let 𝒬 be the A-pairs with (a, b) ∈ Q (v₂(e) ≤ K in type 2 and in the o ≡ −p (8) part of
type 1).
*Type 1.* By Lemma 3.3(a) and Prop 3.4(a) (each window (p^{β₀}2^{−k}, p^{β₁}2^{−k}] starts above (16op)^{τ}p^{6ε} by (C2),
since 2^k ≤ p^{ε}; 8oX ≤ p by (C1)), and Lemma 3.5:
  M_𝒬 = Σ_{o} T_o·½(1 − 1/p)(1/o)𝓛(χ_{D_o}; 2op)·(β₁ − β₀)L + O(p^{−δ}Σ_{o≤p}2^{ω(o)+1}/φ(o)).
The error is p^{−δ+o(1)}. Since 𝓛 > 0 and 1 − 2^{2−K} ≤ T_o ≤ 1, Prop 3.6(a) gives
  M_𝒬 = (3/π²)(α₁ − α₀)(β₁ − β₀)L² + O(L) + O(2^{−K}L²) = ((3/π²)·area(Q) + o(1))L².
*Type 2.* By Lemma 3.3(b), Prop 3.4(b) (window o > p^{α₀} ≥ (64e′p)^{τ}p^{6ε} by (C2′)) and Lemma 3.5,
M_𝒬 = Σ_e ½(1 − 1/p)(1/e)𝓛(χ_{E_e}; 2pe′)(α₁ − α₀)L + p^{−δ+o(1)}, and Prop 3.6(b) gives the same asymptotic.
(The pairs with v₂(e) > K omitted in either type have total weight ≪ 2^{−K}Σ_{o≤p}(2^{ω(o)}/φ(o))Σ_{m≤p}2^{ω(m)}/φ(m) ≪
2^{−K}L⁴ = o(L²); so the asymptotic also holds for all A-pairs in Q.)
*Tiling.* G_λ ∩ ℛ₁ with ℛ₁ := {b > (1 + a)/4} and G_λ \ ℛ₁ = {a > (1 + b)/4, b < (1 + a)/4, b > λ, a + b < 1} (up to the null
line b = (1 + a)/4) are open sets; with r large and ε small (both fixed before p → ∞), every sufficiently thin closed
rectangle inside the first is of type 1 and inside the second of type 2: (C1), (C2), (C2′) hold with margin because the closed
rectangle lies in the open region and τ → 1/4; for (C3) with λ = 1/15, a > 1/15 ⟺ a > (1 + a)/16, so α₀ > (1 + α₁)/16 holds
with margin once α₁ − α₀ is small (resp. (C3-HB) with α₀ ≥ λ). Choose finitely many disjoint such rectangles of total area
≥ area(G_λ) − π²η/6, so that their main terms sum to ≥ ((3/π²)area(G_λ) − η/2)L²; the finitely many o(1)'s are ≤ η/2
for p ≥ p₀. Distinct rectangles give disjoint pair sets and all W ≥ 0, so
  M_gen(p) ≥ M_{A∩G_λ}(p) ≥ Σ_Q M_𝒬 ≥ ((3/π²)area(G_λ) − η)L²  for p ≥ p₀(η, λ). ∎
With λ = 1/15 only (Bu), (Bu8) and elementary steps enter, and every constant is effective. Letting λ → 0 (HB):
M_gen(p) ≥ (5/(4π²) − o(1))L² = (5/6 − o(1))M₀(p).

*Remark (the n = 1 version).* Keeping only the term n = 1 in Prop 3.6 and bounding the Euler factor ∏(1 + χℓ^{−2}) ≥ ∏(1 − ℓ^{−2})
gives the weaker but shorter bound (2/π²)·area (same structure as Thm U's (8/π⁴)·area for type U). The difference
3/π² vs 2/π² is the contribution of the square terms n = s² > 1 and of the split-prime Euler factors.

### 3.7′ Numerical check of the slice constants (EVIDENCE)

`scripts/z56_famdesign_slicecheck.{c,py}` → `slicecheck.txt`: exact slice sums 𝒮₁(o; Y, X) (all k) and 𝒮₂(e; Y, X) by direct
summation of Lemma 3.2's weights, against the predicted main terms ½(1 − 1/p)(1/o)𝓛(χ_{D_o}; 2op)log(X/Y) and
½(1 − 1/p)(1/e)𝓛(χ_{E_e}; 2pe′)log(X/Y) (PARI `lfun`, Euler products to 10⁶), with Y = 4(16op)^{1/4} resp. 4(64e′p)^{1/4},
X = p/(8o) resp. p/(8e), at p = 100 000 049 and 1 000 000 009, for o ∈ {1, 3, 5, 7, 9, 11, 15, 21, 25, 27, 45, 105} (both classes
mod 4, non-squarefree o) and e ∈ {2, 4, 6, 8, 10, 12, 16, 18, 24, 50, 90} (k = 1…4, non-squarefree e′): all 46 ratios lie in
[0.909, 1.045], 42 of them within 3 %. This checks the bookkeeping (2-adic weights 2^{2−k}, the ½ and the Euler factors).

### 3.8 T1 audit (where the proof fails at odd squares; PROVED)

M_gen(m²) = 0 (`SINGLE_P_COUNT` Prop 2.2(b)), so the proof must break at n = m². The decisive step is Prop 3.4(2):
"p | f_G, so ηχ is non-principal". At n = m² (gcd(m, 2o) = 1) the field is ℚ(√(−o₁)), χ_{D_o} = χ_{−o₁ or −4o₁}·1[(·, m)=1],
and χ(n) = χ₋₄(n)^{1+[o₁≡3 (4)]}(n/o₁) on odd n coprime to m (no factor (n/p)). Hence η_{o₁,j}χ is principal (on integers
coprime to 2om) for j ≡ 1 + [o₁ ≡ 3 (4)] (mod 2), and this j is always available: o ≡ 1 (4) ⟹ o₁ ≡ 1 (4), j = 1 ∈ J₁;
o ≡ 3 (4) ⟹ o₁ ≡ 3 (4), j = 0 ∈ J_k (k ≥ 2). So a second pole appears in Prop 3.4(3); since every weight W vanishes at
n = m² (M_gen(m²) = 0), it cancels the η = 1 pole exactly (cf. the explicit sign computation in `Z53_GENUSLVAL` §2.8 for
type U). Mirror statement for region 2 (η = (·/e′₁)ψ with suitable ψ). (Here "principal" means the imprimitive
extension of the trivial character; Prop 3.6 is not where T1 enters, but its constant would change at a general odd
square through local factors at the primes of m — irrelevant for the audit.)

## 4. Scans: zero sets and means of the actual counts (target (ii))

### 4.1 Engines and validation (CERTIFIED)

* `scripts/z56_famdesign_scan.c` enumerates **all** (★) solutions (o, e, C) of each odd n (three exhaustive loops by
  which of P = min(o, e), Q = max(o, e), C is smallest; cost ≈ 3n^{2/3}) and counts hits_𝔊 = R_𝔊/2 for the columns
  all | F0 | F1 | F2U | F2S | F3U | F3S | F4 | F4L | K | H3 | HC (definitions in §6). Membership tests are exact integer
  inequalities (Q⁴ > P·n, P^{15} > n, 64C³ ≤ n in 128-bit arithmetic); the HC cutoff ⌊log²n⌋ is computed in long double
  with an abort if |log²n − round(log²n)| < 10⁻⁹ (never triggered); squarefreeness by trial division to n^{1/3} plus a
  perfect-square test of the cofactor. (First runs used long-double logarithms for the membership tests; every scan, sample, control and decision
  run of this memo was repeated with the exact integer tests and the outputs are byte-identical. The HC tie guard, first
  set at 10⁻⁹, fired once, at p = 5 498 061 937 where log²p = 502.99999999953; long double resolves ≈ 10⁻¹⁵ there, so it
  was set to 10⁻¹² and the chunk rerun, identical.) Validation: (a) total count = brute force R(n) for every odd n ≤ 3000
  (`scripts/z56_famdesign_brute.py`, 1 498 values, 0 mismatches); (b) the (★) zeros among primes p ≡ 1 (4) ≤ 10⁷ are
  exactly the 14 census primes 409 … 8 813 281 (FRONTIER §2.1); (c) column F0 equals CROSSF's independent C-form scanner
  line by line on [10⁸, 1.02·10⁸], [10⁹, 10⁹ + 2·10⁶], [10¹⁰, 10¹⁰ + 2·10⁶] (54 198 + 48 139 + 43 439 primes, 0 mismatches).
* `scripts/z56_famdesign_decide.c`: exhaustive *decision* of hits ≥ 1 for HC, H3, F4, F4L over all primes in a range
  (segmented sieve; level scan C = 1, 2, … using that every solution with 64C³ ≤ p lies in G (§1); exact full count as
  fallback). It reproduces the full-scan zero lists exactly on [10³, 10⁸] (607 + 225 primes, identical lines).
* `scripts/z56_famdesign_mgen.c`: exact M_gen(p) split into G and K (Lemma 3.2 weights; reproduces `Z53_GENUSLVAL`'s
  M_gen(409, 577, 5569, 9601) = 3.9991, 5.3524, 6.2407, 7.9262).

### 4.2 Zero counts (CERTIFIED) and means (EVIDENCE)

Primes p ≡ 1 (4); entries = number (fraction) of primes with hits_𝔊(p) = 0. Exhaustive ranges up to the 10¹² window;
the 10¹³ / 10¹⁴ rows are samples (next prime ≡ 1 (4) after 10^k + j·step, as in CROSSF). `data/z56/famdesign/stats.txt`.

| family | ≤ 10⁷ (332 180) | (10⁷, 10⁸] (2 548 324) | [10⁸, +2·10⁶] (54 198) | [10⁹, +2·10⁶] (48 139) | [10¹⁰, +2·10⁶] (43 439) | [10¹¹, +6·10⁵] (11 876) | [10¹², +1.1·10⁵] (1 991) | 10¹³ (400) | 10¹⁴ (100) |
|---|---|---|---|---|---|---|---|---|---|
| F0 (Thm U std window) | 196 739 (59.2 %) | 1 112 729 (43.7 %) | 21 233 (39.2 %) | 16 757 (34.8 %) | 10 333 (23.8 %) | 1 856 (15.6 %) | 169 (8.5 %) | 19 (4.8 %) | 6 (6 %) |
| F1 (U ∩ ℛ₁(1/15)) | 76 670 (23.1 %) | 294 831 (11.6 %) | 4 843 (8.9 %) | 2 074 (4.3 %) | 783 (1.8 %) | 151 (1.3 %) | 11 (0.55 %) | 0 | 0 |
| F2U (U ∩ G_{1/15}) | 22 555 (6.8 %) | 47 857 (1.9 %) | 632 (1.2 %) | 178 (0.37 %) | 30 (0.07 %) | 2 | 1 | 0 | 0 |
| F2S (S ∩ G_{1/15}) | 1 019 (0.31 %) | 758 (0.03 %) | 6 | 1 | 0 | 0 | 0 | 0 | 0 |
| F3U (U ∩ G) | 1 603 (0.48 %) | 2 704 (0.11 %) | 37 | 11 | 1 | 0 | 0 | 0 | 0 |
| F3S (S ∩ G) | 111 | 39 | 1 | 0 | 0 | 0 | 0 | 0 | 0 |
| **F4L (A ∩ G_{1/15})** | 255 | 47 | 0 | 0 | 0 | 0 | 0 | 0 | 0 |
| **F4 = 𝔊* (A ∩ G)** | 34 | 3 | 0 | 0 | 0 | 0 | 0 | 0 | 0 |
| H3 (A, 64C³ ≤ p) | 456 | 184 | 1 | 0 | 0 | 0 | 0 | 0 | 0 |
| HC (A, C ≤ log²p) | 51 | 28 | 0 | 0 | 0 | 0 | 0 | 0 | 0 |
| K (Burgess corner) | 6 449 (1.9 %) | 17 253 (0.68 %) | 238 | 54 | 20 | 2 | 0 | 0 | 0 |
| all (R) | 14 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 |

Means R_𝔊/L² (= 2·hits/L², EVIDENCE) against the asymptotic density (3/π², 2/π², 1/π² per unit area for A, S, U; areas
§1; Assessment for S and U, Theorem V for A):

| family | ≤ 10⁷ | 10⁸ | 10¹⁰ | 10¹² | 10¹⁴ | density × area |
|---|---|---|---|---|---|---|
| F0 | 0.005 | 0.006 | 0.006 | 0.006 | 0.006 | (1/π²)(1/12) = 0.0084 |
| F1 | 0.014 | 0.015 | 0.017 | 0.016 | 0.016 | (1/π²)(8/45) = 0.0180 |
| F2S | 0.064 | 0.061 | 0.062 | 0.062 | 0.059 | (2/π²)(29/90) = 0.0653 |
| F3S | 0.099 | 0.096 | 0.094 | 0.093 | 0.090 | (2/π²)(5/12) = 0.0844 |
| F4L | 0.087 | 0.087 | 0.090 | 0.091 | 0.088 | (3/π²)(29/90) = 0.0979 |
| F4 | 0.134 | 0.132 | 0.131 | 0.130 | 0.126 | (3/π²)(5/12) = 0.1267 |
| H3 | 0.080 | 0.080 | 0.081 | 0.082 | 0.081 | (3/π²)(5/18) = 0.0844 |
| HC | 0.105 | 0.093 | 0.081 | 0.072 | 0.064 | → 0 (area → 0; ≍ log L/L) |
| K | 0.033 | 0.031 | 0.030 | 0.029 | 0.028 | (3/π²)(1/12) = 0.0253 |
| all | 0.166 | 0.163 | 0.161 | 0.159 | 0.155 | 3/(2π²) = 0.1520 |

Variance/mean of hits (EVIDENCE): F0 0.92–1.08 (CROSSF's near-Poisson), but 1.6–2.3 for F2S, 1.8–2.7 for F4L, 1.8–3.4
for F3S/H3 and 2.4 → 4.9 (10⁷ → 10¹⁴) for F4 and the full count: the large families are strongly overdispersed (solutions cluster on
integers with many divisors), so P(hits = 0) ≫ e^{−mean} (§4.4).

### 4.3 The top family's zero set (CERTIFIED)

* **F4 = A ∩ G: exactly 37 zeros among primes p ≡ 1 (4) ≤ 10⁸** (`zeros_le1e8.txt`): the 14 (★)-zero primes, 20 primes
  ≤ 4.7·10⁶ whose (★) solutions all lie in the corner, and 11 814 001, 20 445 289, **85 664 329**, each with R = 2 and its
  unique solution in K: (o, e, C) = (9, 38, 8636), (65, 6, 13106), (29, 18, 41027). **Exhaustively over all primes p ≡ 1 (4) ≤ 10¹⁰**
  (227 523 275 primes = π(10¹⁰; 4, 1); `decide_1e7_1e10.txt`): **38 zeros**, the only one above 10⁸ being
  **564 661 441** (≡ 1 mod 840), again with R = 2 and its unique solution (9, 206, 76141) in K.
* Up to 10¹⁰ (exhaustive): F4L 317 zeros (302 ≤ 10⁸), last 6 122 428 657; H3 873 zeros (640 ≤ 10⁸), last
  9 466 909 909; HC 163 zeros (79 ≤ 10⁸), last 9 466 909 909. The full count R has no zero in (8 813 281, 10¹⁰]
  (re-confirming FRONTIER §2.1's census by an independent engine).
* Controls: all 10 odd squares 10001², …, 1000001² have hits = 0 in **every** family (T1; CROSSO Cor 1.2); the
  19 FRONTIER §4 item-14 test primes behave as recorded there (the 14 (★)-zeros are zeros of every family; 193, 2521,
  66529, 3361, 5101441 have R = 4, 2, 8, 2, 10); 493 prime near-squares p = m² + k (1 ≤ k ≤ 16) near 10⁸, 10⁹, 10¹⁰
  (`controls.txt`) have no zero in F2S, F3S, F4L, F4, with means 10–16 % below the generic window means at the same
  scale (the known near-square depletion, FRONTIER §4 item 15).

### 4.4 Model scale of the last zero (Assessment; model only)

A binned Poisson-ML fit of P(hits_𝔊 = 0) = exp(b − c_eff L²) on all primes in [10⁵, 10⁸]
(`scripts/z56_famdesign_zerofit.py`, `zerofit.txt`), extrapolated with E(x) = ∫_{log x}^∞ e^{s+b−c_eff s²}/(2s) ds:

| family | zeros in [10⁵, 10⁸] | c_eff | E(> 10⁸) | E(x*) = 1 at x* ≈ |
|---|---|---|---|---|
| F0 | 1 305 402 | 0.0036 | 2·10²⁹ | 10¹¹⁸ (CROSSF's Poisson model: 10¹²⁴) |
| F1 | 368 856 | 0.0080 | 9·10¹² | 10⁵² |
| F2S | 1 551 | 0.025 | 2·10³ | 10¹⁵ |
| F3S | 115 | 0.030 | 49 | 10^{11.4} |
| F4L | 204 | 0.036 | 27 | 10^{10.2} |
| **F4** | 22 | 0.039 | 1.5 | **10^{8.3}** |
| H3 | 516 | 0.029 | 260 | 10^{12.6} |
| all | 8 | 0.041 | 0.36 | < 10⁸ |

c_eff is well below the mean coefficient (e.g. 0.039 vs 0.065 for F4) because of the overdispersion. The fit is crude
(two parameters, F4 has only 22 zeros in the fit range) and says nothing certain beyond the data; it only shows that for
the large families "R_𝔊 ≥ 1 for p ≥ p₀" is a statement whose expected exceptions end at *computable* sizes, unlike the
Thm U family (CROSSF §4).

### 4.5 Is the G-part of the main term rigid? (EVIDENCE)

Theorem V says M_{A∩Q}(p) = (3/π²)area(Q)L²(1 + o(1)) on each fixed compact rectangle Q inside G: no class-number
fluctuation survives there (globally on G only the lower bound is proved).
`scripts/z56_famdesign_mgen_run.py` (exact M_gen split, seeded random primes; `mgen_split.tsv`) gives, as
mean ± sd [min, max] of M_G/M₀,G and M_K/M₀,K (M₀,· = density part 2/φ(4oe) of the same region):

| set | M_G/M₀,G | M_K/M₀,K | M_G/L² |
|---|---|---|---|
| 14 (★)-zero primes | 0.877 ± 0.080 [0.743, 1.071] | **0.279 ± 0.259** [0.000, 0.861] | 0.101 ± 0.007 |
| 40 random p ∈ [10⁶, 2·10⁶] | 1.022 ± 0.122 [0.886, 1.388] | 1.081 ± 0.204 [0.470, 1.516] | 0.121 ± 0.014 |
| 40 random p ∈ [10⁷, 2·10⁷] | 0.974 ± 0.074 [0.841, 1.154] | 0.999 ± 0.217 [0.316, 1.332] | 0.116 ± 0.009 |
| 20 random p ∈ [10⁸, 2·10⁸] | 1.010 ± 0.122 [0.853, 1.302] | 1.120 ± 0.104 [0.917, 1.273] | 0.122 ± 0.015 |
| 3 random p ∈ [10⁹, 2·10⁹] | 1.069 ± 0.108 | 1.100 ± 0.124 | 0.129 ± 0.013 |

Reading: at attainable sizes the G-part still fluctuates by ≈ 10 % (the proved error terms are p^{−δ} with tiny δ and
the windows near ∂G are not yet asymptotic), but the (★)-zero primes are distinguished mainly by a **depleted corner**
(M_K at 28 % of its density, vs ≈ 88 % for M_G): the genus deficit of the hardest primes sits where Theorem V says it
can (the Burgess corner). Exact counts vs genus parts at the same primes (`mcorr.txt`): R_G/M_G has mean 1.05–1.26 and
sd 0.27–0.38 at 10⁶–10⁸; corr(R_G, M_G) = 0.39, 0.41, 0.66 at 10⁶, 10⁷, 10⁸.

## 5. Remainder structure (target (iii))

Notation as in `Z53_GENUSX` Lemma 1: X_𝔊 := R_𝔊 − M_𝔊 is the order-≥3 part. Facts (PROVED, elementary) and readings
(Assessment):

1. **Slice form (all families; PROVED identities).** In region-1 slices (o fixed) the exact count is
   #{e ∈ window : e | p + o, (p + o)/e ≡ −1 (mod 4o)} — divisors of the single integer p + o in one class mod 4o; in
   region-2 slices (e fixed) it is #{o ∈ window : o | p + e, (p + e)/o ≡ −1 (mod 4e)}; at fixed C it is
   #{d | 4Cp + 1 : d ≡ −1 (mod 4C), cofactor conditions} (cf. `Z55_CROSSF` Lemma 1.3, which is form-independent). So
   every family has the tied single-integer structure (B2); no family design removes it.
2. **𝔊* contains every complete C-layer with 64C³ ≤ p (PROVED, §1).** Hence
   R_{𝔊*}(p) ≥ R_{H3}(p) = Σ_{C ≤ (p/64)^{1/3}} D⁻_{4C}(4Cp + 1), D⁻_t(N) := #{d | N : d ≡ −1 (mod t)}, and on H3 the exact
   count at each level is **window-free**: D⁻_{4C}(N) = φ(4C)⁻¹Σ_{χ mod 4C}χ(−1)σ_χ(N), σ_χ(N) = Σ_{d|N}χ(d) multiplicative
   in N (the level-t theta-quotient normal form of FRONTIER §2.3 applies level by level). The order-≥3 remainder of H3 in
   level coordinates is Σ_C φ(4C)⁻¹Σ_{χ mod 4C, ord χ ≥ 3}χ(−1)σ_χ(4Cp + 1): a sum over the free variable C of complete
   multiplicative twisted divisor functions of the linear sequence 4Cp + 1, with modulus 4C *not attached to p*.
   H3 carries ≈ 62 % of R_{𝔊*} (EVIDENCE: means 0.081 vs 0.130); its *density-area* share is (5/18)/(5/12) = 2/3
   (Assessment for the actual counts: the remainder is uncontrolled). The Thm U family has
   no complete layer (both u and w are windowed, and u is restricted mod 4 and squarefree).
   (Caveat: the genus split in level coordinates — characters of order ≤ 2 mod 4C — is a different decomposition of the
   same count from the pair-coordinate M_gen of Theorem V. In pair coordinates H3 is the pair set
   {(o, e) : 64·((p + o + e)/(4oe))³ ≤ p} (for solutions (p + o + e)/(4oe) = C); it contains the pairs with
   (a, b) in the open strip {2/3 < a + b < 1} for large p, and tiling that strip (it lies in G) gives
   M_{H3}(p) ≥ ((3/π²)·(5/18) − o(1))L² = (5/(6π²) − o(1))L² with HB, and (3/π²)(7/30) = 7/(10π²) with Burgess only.)
3. **The remaining third of 𝔊*** (C ∈ (p^{1/3}/4, p^{3/4}), windowed slices) has the Thm-U-type structure of item 1.
4. **Where the deficits sit (EVIDENCE, §4.5).** At the (★)-zero primes the genus layer is depleted mostly in the corner K,
   which 𝔊* excludes; within 𝔊* the remainder has sd ≈ 0.3·M_G at 10⁶–10⁸ and the counts are overdispersed
   (var/mean 2.5–4.9), i.e. solutions cluster on the integers p + o, p + e, 4Cp + 1 with many divisors.
5. **Assessment for FAMATTACK.** The most exploitable piece is H3: complete levels, multiplicative σ_χ, free modulus 4C,
   main term ≥ (5/(6π²) − o(1))L² unconditionally (Theorem V's proof on the strip {2/3 < a + b < 1}; 7/(10π²) with Burgess only),
   but its zero set is larger than 𝔊*'s (873 zeros ≤ 10¹⁰, the last at 9 466 909 909; model scale 10^{12.6}). Positivity of H3 is still B2: it needs a
   lower bound for Σ_C D⁻_{4C}(4Cp + 1) at one p, i.e. control of the order-≥3 characters mod 4C on the prime factors of
   4Cp + 1 jointly in C — the HC-type problem with a log²p (not log p) main term.

## 6. Ranked table of families

c_prov = proved constant in M_𝔊(p) ≥ (c_prov − o(1))L² (both orders; L = log p); c_dens = asymptotic density × area
(Theorem V for A; Assessment for S, U); "R/L²" = observed mean at 10¹²; zeros = CERTIFIED counts (§4.2–4.3); x* = fitted
model scale of the last zero (§4.4, Assessment).

| rank | family | definition | c_prov (label; inputs) | c_dens | R/L² @10¹² | zeros ≤ 10⁸ (last) | beyond 10⁸ | x* | remainder structure |
|---|---|---|---|---|---|---|---|---|---|
| 1 | **𝔊* = F4** | all pairs, max(o,e) > (min·p)^{1/4} | **5/(4π²) ≈ 0.1267** (PROVED; Burgess + HB) | 0.1267 | 0.130 | 37 (85 664 329) | 1 in (10⁸, 10¹⁰]: 564 661 441 | 10^{8.3} | ⅔ complete C-layers (H3) + ⅓ windowed slices |
| 2 | F4L | 𝔊* ∩ {min(o,e) > p^{1/15}} | **29/(30π²) ≈ 0.0979** (PROVED; Burgess only, effective) | 0.0979 | 0.091 | 302 (85 664 329) | 15 in (10⁸, 10¹⁰], last 6 122 428 657 | 10^{10.2} | as 𝔊*, small-min slices removed |
| 3 | H3 | all solutions with 64C³ ≤ p | 5/(6π²) ≈ 0.0844 (PROVED, HB); 7/(10π²) ≈ 0.0709 (Burgess) | 0.0844 | 0.082 | 640 (99 122 929) | 233 in (10⁸, 10¹⁰], last 9 466 909 909 | 10^{12.6} | complete levels: Σ_C D⁻_{4C}(4Cp+1), σ_χ multiplicative, free modulus 4C |
| 4 | F3S | S ∩ G | 20/(3π⁴) ≈ 0.068 (n = 1 version; Assessment: same proof) | 0.0844 | 0.093 | 150 (97 661 089) | 1 at 100 038 481 | 10^{11.4} | as 𝔊*, squarefree |
| 5 | HC | all solutions with C ≤ log²p | none at L² scale (area → 0) | → 0 | 0.072 ↓ | 79 (93 412 201) | 84 in (10⁸, 10¹⁰], last 9 466 909 909 | 10^{12.5} | complete levels C ≤ L² (HC-type) |
| 6 | F2S | S ∩ G_{1/15} | 232/(45π⁴) ≈ 0.0529 (n = 1; Assessment) | 0.0653 | 0.062 | 1 777 (99 989 117) | 6 at 10⁸, 1 at 10⁹ | 10¹⁵ | |
| 7 | F3U | U ∩ G | 10/(3π⁴) ≈ 0.0342 (n = 1; Assessment) | 0.0422 | 0.053 | 4 307 | 37, 11, 1 at 10⁸, 10⁹, 10¹⁰ | — | |
| 8 | F2U | U ∩ G_{1/15} | 116/(45π⁴) ≈ 0.0265 (n = 1; Assessment) | 0.0326 | 0.029 | 70 412 | 2 at 10¹¹, 1 at 10¹² | — | |
| 9 | F1 | U ∩ ℛ₁(1/15) (Thm U tiled) | 64/(45π⁴) ≈ 0.0146 (PROVED, Cor V1) | 0.0180 | 0.016 | 371 501 | 11 at 10¹² | 10⁵² | Thm U type |
| 10 | F0 | Thm U standard window | 2/(3π⁴) ≈ 0.0068 (PROVED, `Z53_GENUSLVAL`) | 0.0084 | 0.006 | 1 309 468 | 8.5 % at 10¹², 4.8 % at 10¹³ | 10¹¹⁸ | Thm U type (CROSSF) |
| — | full (★) | all solutions | M_gen ≥ (5/(4π²) − o(1))L² (Cor. of Thm V) | 0.152 | 0.159 | 14 (8 813 281; none in (8.8·10⁶, 10¹⁰]) | — | — | includes the corner |
| — | K | Burgess corner | none (Assessment: Burgess wall) | 0.0253 | 0.029 | 23 702 | 2 at 10¹¹ | 10^{33.7} | the L(1, χ_pψ) layer |

Recommendation (Assessment): for an attack on positivity use **𝔊*** (largest proved constant, earliest end of
zeros) or **H3** (complete levels, cleanest remainder); the Thm U rectangle should be retired as a target.

## 7. Screens, verdict, proposed FRONTIER text, bottom line

**FRONTIER §4 hard screens for Theorem V / 𝔊* as an ES ingredient.**
1. *T1 (squares):* passes — §3.8 names the false step at n = m² (non-principality of ηχ_{D_o} because p | its conductor);
   CERTIFIED: hits = 0 at every tested odd square in every family.
2. *8/131:* not applicable — Theorem V concerns the numerator-4 genus main term and asserts no solutions; used as an ES
   method it inherits screen 3's failure.
3. *Tied modulus (B2):* **fails** — main term only (B3); the order-≥3 remainder X_𝔊* is untouched, so R_𝔊* ≥ 1 does not
   follow.
4. *Fixed p (B6):* passes — every average is over a free variable at fixed p (e or o inside a slice, o or e across slices,
   Burgess character by character, HB over the moduli n₁ of the L-series coefficients); nothing is averaged over p.

**Verdict: strengthened (main-term side).** New and PROVED: (1) Theorem V — the unconditional genus main term of the
non-corner (★) family is (5/(4π²) − o(1))L², i.e. **at least 5/6 of M₀** (Thm U: 4.5 %); with Burgess only, 29/45 of M₀,
effectively; on rectangles inside G it is an asymptotic with no p-dependent fluctuation. (2) The exact obstruction to more:
the excluded sixth is the Burgess corner max(o, e) ≤ (min(o, e)·p)^{1/4}, where the slice cross terms are products of
χ_p-twisted sums shorter than p^{1/4} (Assessment: the GRH/zero-free-strip gap of `Z53_GENUSLVAL` §4; under GRH the whole
triangle would be admissible). (3) CERTIFIED: the top family's count vanishes at exactly 38 primes p ≡ 1 (4) ≤ 10¹⁰, the last
being 564 661 441; the model scale of its last zero is ~10^{8}–10^{10} (Assessment), versus ~10¹²⁰ for the Thm U family.
What it buys: problem CROSS can now be posed on a family whose main term is 18 × larger and whose positivity has
checkable content. What it does not buy: anything about the order-≥3 remainder (B2). **ES remains OPEN.**

**Proposed FRONTIER §7 text** (do not edit FRONTIER here):
> 4′. **Genus main term: 5/6 of M₀ unconditionally (z56, `Z56_FAMDESIGN.md` Thm V; PROVED, internal review).** For every
> prime p ≡ 1 (4), p ≥ p₀: M_gen restricted to the pairs with max(o, e) > (min(o, e)·p)^{1/4} (the family 𝔊*) is
> ≥ (5/(4π²) − o(1))log²p (Burgess + Heath-Brown's quadratic large sieve; 29/(30π²) with Burgess only, effective), so
> M_gen(p) ≥ (5/6 − o(1))M₀(p) (Thm U: 4.5 %). Proof: Thm U's slices tiled over the region, plus mirror slices (e fixed),
> all arithmetic types, and the exact Euler-product average. The excluded "Burgess corner" (both entries ≲ p^{1/3},
> C ≳ p^{1/3}) is where the L(1, χ_pψ) cross terms cannot be averaged unconditionally. CERTIFIED: R_𝔊*(p) = 0 at exactly
> 38 primes p ≡ 1 (4) ≤ 10¹⁰ (last 564 661 441; no zero in the sampled windows up to 10¹⁴). Open: the remainder X_𝔊* (B2); 𝔊* and its complete-level part
> H3 = {64C³ ≤ p} are the recommended targets for problem CROSS.

**Bottom line.** The Thm U rectangle captured 4.5 % of the expected (★) count; the whole region where Burgess can see the
genus characters captures 5/6 of it (Theorem V, PROVED, as a lower bound for M_gen; 64 % with Burgess alone), and the
excluded density-area sixth is exactly the large-C corner where the class-number cross terms live — which is also where the (★)-zero primes lose most of their genus
mass. The family 𝔊* has a main term ≈ 0.127·log²p, an empirical zero set of 38 primes up to 10¹⁰ (the last 564 661 441; none in windows and samples up to
10¹⁴), and two-thirds of it consists of complete level sets Σ_C D⁻_{4C}(4Cp + 1). The order-≥3 remainder (B2) is
untouched; **ES remains OPEN.**

## 8. Review log

(to come)
