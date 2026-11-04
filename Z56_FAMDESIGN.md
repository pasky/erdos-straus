# Z56_FAMDESIGN — a (★) sub-family with a big provable genus main term

Status: z56 lane FAMDESIGN (brief `z52bbriefs/z56_lanes.md` §3, common rules `z53_depth.md`). Internal, internally
reviewed only (§8). **ES is OPEN; nothing here proves or disproves ES or (★) at any infinite set of primes.**
Labels: PROVED / CONDITIONAL / CERTIFIED / EVIDENCE / CONJECTURE / Assessment. Scripts `scripts/z56_famdesign_*`, data
`data/z56/famdesign/`.

## 0. Summary

DRAFT — filled in at the end.

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

*Log-coordinates.* a := log o/L, b := log e/L; pairs in 𝒫(p) have a + b < 1 + o(1). Put
  **G := {(a, b) ∈ (0, 1)² : a + b < 1, max(a, b) > (1 + min(a, b))/4}**,  G_λ := G ∩ {min(a, b) > λ},
i.e. "the larger entry exceeds (smaller entry · p)^{1/4}". Its complement in the triangle, the **Burgess corner**
K := {max(a, b) ≤ (1 + min(a, b))/4} (vertices (0,0), (1/4,0), (1/3,1/3), (0,1/4)), has area 1/12; area(G) = 5/12 of
the triangle's 1/2, and for 0 ≤ λ ≤ 1/15, area(G_λ) = 5/12 − 3λ/2 + 5λ²/4 (area(G_{1/15}) = 29/90). Every solution
with 64C³ ≤ p lies in G (if max ≤ (min·p)^{1/4} then max ≤ p^{1/3}, so oe ≤ p^{2/3} < p/(4C)); the corner is a
large-C phenomenon (C ≳ p^{1/3}/4).

*Arithmetic types.* **A**: all pairs. **S**: o squarefree, e′ squarefree. **U** (= `Z53_GENUSLVAL` Thm U's type):
o ≡ 1 (4) squarefree, k = 1, e′ squarefree. The Thm U family 𝔉 is U ∩ (rectangle); CROSSF's "standard window" is
U ∩ {p^{1/12} < o ≤ p^{1/3}/2, p^{1/3} < e/2 ≤ p^{2/3}/4}.

*Densities.* M₀(p) := Σ_{𝒫(p)} 1/φ(4uB) = (3/(2π²) + o(1))L² (`BM_CORRECTED_COUNT` Thm 2.2) is the expected count at a
random prime; per unit (a, b)-area (both orders) the pair density is 3/π² for type A. Assessment (elementary mean-value
computation, §2): 2/π² for S and 1/π² for U.

**Targets of the lane (brief).** (i) a family 𝔊 with an unconditional M_𝔊(p) ≥ (c − o(1))L² at every large prime
p ≡ 1 (4), c as large as possible; (ii) a small empirical zero set of R_𝔊; (iii) an exploitable remainder.

**Why this is not closed.** Thm U (FRONTIER §7.4, closed) proves one rectangle of type U, c = 2/(3π⁴) ≈ 0.00684,
≈ 4.5 % of M₀. Nothing in the closed list or FRONTIER §6 concerns the *size* of the provable genus share. This lane is
main-term engineering (B3): it does **not** touch the order-≥3 remainder (B2) and cannot by itself give R_𝔊 ≥ 1.

## 2. Results at a glance (ranked table: §6)

* **Corollary V1 (PROVED; from Thm U's proof by tiling).** U ∩ ℛ₁(1/15), ℛ₁(λ) := {a > λ, b > (1+a)/4, a + b < 1}:
  M ≥ (64/(45π⁴) − o(1))L² ≈ 0.0146 L².
* **Theorem V (PROVED; §3).** For every η > 0 and every prime p ≡ 1 (4), p ≥ p₀(η, λ):
  M_{A∩G_λ}(p) ≥ ((3/π²)·area(G_λ) − η)L²; with λ = 1/15 using Burgess only (constant **29/(30π²) ≈ 0.0979**,
  p₀ effective), and for every fixed λ > 0 using also Heath-Brown's quadratic large sieve (constant → **5/(4π²) ≈ 0.1267**).
  On every closed rectangle Q ⊂ G_λ the asymptotic M_{A∩Q}(p) = ((3/π²)area(Q) + o(1))L² holds (no p-dependent
  fluctuation in the main term). **Corollary:** M_gen(p) ≥ (5/(4π²) − o(1))L² = (5/6 − o(1))·M₀(p) — 18.5 × Thm U's
  constant; the uncaptured sixth is exactly the Burgess corner K.

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
T_o := Σ_{k∈𝒦_o, k≤K}2^{2−k}c_k ∈ {1, 1 − 2^{2−K}}.
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
square-sensitive step, §3.8). Writing d = g·d₂ with d₂ | s (the primes of d not dividing o₁ divide s): do₁/g² = d₂²o₁ ≤ o,
hence **f_F·f_G ≤ 16·o·p**. All conductors are 4^{≤1}·(odd squarefree): cube-free, so (Bu) applies.
(b) is identical with χ := χ_{E_e}, m odd coprime to e′p, η = (·/d′)ψ of conductor f_F = d′·f_ψ ≤ 8d′, and for odd n
χ_{E_e}(n) = ψ₁(n)(n/e′₁)(n/p) with ψ₁ a character mod 8, so ηχ = χ*_G·1[gcd(n, 2g′) = 1] with
χ*_G = ψ₂·(·/(d′e′₁/g′²))·(·/p), g′ = gcd(d′, e′₁), conductor ≤ 8e′p·(…) and f_F f_G ≤ 64e′p; p | f_G. Conductors
8·(odd squarefree) occur: use (Bu8).
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
  (b) Σ_{O₀<e≤O₁, e even, v₂(e)≤K} 𝓛(χ_{E_e}; 2pe′)/e = (1 − 2^{−K})(6/π²)·log(O₁/O₀) + O(K),
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
place of o (squares n = s²: (−2^kp/s²) = 1[p ∤ s]), giving 2^{−k}(6/π²)log(O₁/O₀) + O(2^{−k}) per k; sum over k ≤ K. ∎

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

### 3.8 T1 audit (where the proof fails at odd squares; PROVED)

M_gen(m²) = 0 (`SINGLE_P_COUNT` Prop 2.2(b)), so the proof must break at n = m². The decisive step is Prop 3.4(2):
"p | f_G, so ηχ is non-principal". At n = m² (gcd(m, 2o) = 1) the field is ℚ(√(−o₁)), χ_{D_o} = χ_{−o₁ or −4o₁}·1[(·, m)=1],
and for d = o₁ and the j with χ₋₄^j(·/o₁)χ_{D_o} principal (on integers coprime to 2om) the character ηχ is principal:
a second pole appears with sign ε_{k,o₁,j}; as in `Z53_GENUSLVAL` §2.8 it equals −1 and cancels the η = 1 pole identically.
Mirror statement for region 2 (η = (·/e′₁)ψ). Prop 3.6 is true at squares as well (it is not where T1 enters).

## 4. Scans (CERTIFIED counts, EVIDENCE statistics)

(to come)

## 5. Remainder structure (iii)

(to come)

## 6. Ranked table of families

(to come)

## 7. Screens, verdict, proposed FRONTIER text, bottom line

(to come)

## 8. Review log

(to come)
