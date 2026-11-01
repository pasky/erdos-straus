# Z53_GENUSLVAL — the full genus layer at one prime: an unconditional log² lower bound and L-value closed forms

Status: z53 depth lane GENUSLVAL. Internal result, internally reviewed only (§8). **ES is OPEN; nothing here proves or
disproves ES, or (★), at any infinite set of primes.** Labels: PROVED / CONDITIONAL / CERTIFIED / EVIDENCE / CONJECTURE /
Assessment. Scripts `scripts/z53_genuslval_*`, data `data/z53/genuslval/`. Builds on `SINGLE_P_COUNT.md` §2 (genus split),
`LOWERTAIL_DEEP_ASTRA.md` Thm 5.4 (conditional log² bound; its subfamily is reused), `BM_LVALUE.md` (hyperbola method).

## 0. Summary

* **Theorem U (PROVED, unconditional, effective; §2).** For every ε > 0 there is an effective p₀(ε) such that every prime
  p ≡ 1 (mod 4), p ≥ p₀(ε), satisfies
  **M_gen(p) ≥ (2/(3π⁴) − ε)·(log p)² ≈ 0.00684·(log p)².**
  This closes FRONTIER §7.4 as stated (polylog lower bound for M_gen, unconditionally). Inputs: Burgess's bound for
  primitive characters of *cube-free* conductor (all r), elementary hyperbola/Abel summation. No zero-free region, no Siegel,
  no GRH. Burgess with r ≤ 3 only gives 1/(3π⁴) ≈ 0.0034. (Conditional comparison: a fixed zero-free strip gives 2/π⁴ ≈ 0.0205,
  `LOWERTAIL_DEEP_ASTRA` Thm 5.4; observed min M_gen/log²p = 0.084 over the sampled p ≡ 1 (4) in [10³, 10⁷], EVIDENCE.)
* **How.** Thm 5.4's genus-exact subfamily (u, 2w), (2w, u) with sharp windows u ∈ (p^{α₀}, p^{α₁}], w ∈ (p^β, p^γ]. The
  window *difference* kills every constant term, so of the 2^{ω(u)+1} genus characters η mod 4u only η = 1 survives
  (Prop 2.4); η·χ_{−4up} is never principal **because p divides its conductor** (the only place primality enters; it is
  exactly what fails at odd squares, §2.8). Burgess needs w-windows longer than (conductor of η)^{1/4}·(conductor of
  ηχ_D)^{1/4} = (4up)^{1/4} — the two conductors multiply to 4up, not to 16u²p (§2.5) — and the average of L(1, χ_{−4up})
  over u is done by Burgess in u for the short part and per-u Burgess tails for the long part (Prop 2.5).
* **Proposition C (PROVED; §3): the u-slice closed form.** For squarefree u ≡ 1 (4), u ≤ p^{α} with α < (1 − τ)/(1 + τ)
  (τ the Burgess exponent, → 1/4; so any α < 3/5 for suitable r, ε), the u-slice of M_gen is
  S_u(p) = (2φ(u))⁻¹ Σ_{η = (·/d)χ₋₄^j, d|u, j∈{0,1}} ε_η·Σ_η + O(p^{−δ}) with
  Σ_1 = L(1, χ_{−4up})H_u(1)[log X_u + γ_E + L′/L(1, χ_{−4up}) + H_u′/H_u(1)] and
  Σ_η = **L(1, η)·L(1, ηχ_{−4up})·H_{u,η}(1)** (η ≠ 1), explicit signs ε_η = ±1 and explicit Euler products.
  ηχ_{−4up} is (up to Euler factors at 2d) the Kronecker character of conductor (4)(u/d)p: these are precisely the
  products L(1, χ_pψ)·L(1, ψ′) of the brief, ψ the genus character of u/d, ψ′ that of d. **EVIDENCE:** agrees with the
  exactly computed slice to |err| ≤ 1.2·10⁻³ (relative ≤ 0.5 %) for u ∈ {1, 5, 13, 21} at 8 primes 10⁵ … 10⁸ incl. four
  (★)-zero primes (§3.2).
* **(b) Which genus characters can make M_gen small (§4).** At a single p, M_gen − (principal-genus part) is a signed sum of
  the cross terms ε_η L(1, η)L(1, ηχ_{−4up})H; they carry no log-growth in the slice, and can be large and negative for
  individual u (EVIDENCE: at the (★)-zero prime 8 813 281, the net cross terms of the u = 13 slice remove 38 % of its
  principal-genus mass, driven by η = (·/13), (·/13)χ₋₄ with ε_η = −1). Theorem U shows that no configuration of the genus characters can make M_gen(p) = o(log²p) for
  p ≥ p₀ (unconditional, effective): it is excluded. The principal-genus part itself is never small on average over u.
* **Not a step toward (★) at one prime (B2/B3).** M_gen is the expected count; R(p) = M_gen + X with X the order-≥3 part.
  Theorem U improves the *main-term* side only: the target H⁻ relative to M_gen (X(p) ≥ −(1 − ε)M_gen(p)) now has an
  unconditionally log²-sized right-hand side, but X is untouched. **ES remains OPEN.**

## 1. Statements

Notation (FRONTIER §2.1, `SINGLE_P_COUNT` §2). p is a prime, p ≡ 1 (mod 4), χ_p = (·/p). 𝒫(p) = {(u, B) ∈ ℕ² : gcd(u, B) = 1,
u + B odd, 4uB − u − B ≤ p}; for a pair, q = 4uB, a = −(u + B), s(q) = |(ℤ/q)^× / ((ℤ/q)^×)²|, and
  M_gen(p) = Σ_{(u,B)∈𝒫(p)} (s(q)/φ(q))·1[p·a ∈ ((ℤ/q)^×)²]
(all terms ≥ 0; the contribution of the characters of order ≤ 2 to the orthogonality expansion of R(p); `SINGLE_P_COUNT`
Lemma 2.1). For a fundamental discriminant D, χ_D = (D/·) is the Kronecker character and L(1, χ_D) > 0.

**Theorem U.** Let r ≥ 3 be an integer and ε > 0 small. Put τ_r := (r + 1)/(4r) and
  c(α₀, α₁, β, γ) := (8/π⁴)(γ − β)(α₁ − α₀).
If 0 < α₀ < α₁ and β < γ satisfy
  (C1) γ < 1 − α₁,  (C2) β > τ_r(1 + α₁),  (C3) α₀ > τ_r²(1 + α₁),
(each with a margin depending on ε), then M_gen(p) ≥ (c(α₀, α₁, β, γ) − o(1))(log p)² as p → ∞ through primes p ≡ 1 (4),
with an effective o(1). Optimising (r → ∞, α₁ = 1/3, α₀ ↓ 1/12, β ↓ 1/3, γ ↑ 2/3) gives
  **M_gen(p) ≥ (2/(3π⁴) − ε)(log p)²  for p ≥ p₀(ε) (effective).**
With r = 3 (τ = 1/3): α₁ = 5/16, constant (8/π⁴)/24 = 1/(3π⁴) ≈ 0.00342.

(Optimisation: with the margins removed, (γ − β)(α₁ − α₀) = (1 − τ − α₁(1 + τ))·(α₁(1 − τ²) − τ²); at τ = 1/4 this is
(3 − 5α₁)(15α₁ − 1)/64, maximal at α₁ = 1/3 with value 1/12; at τ = 1/3 it is (2 − 4α₁)(8α₁ − 1)/27, maximal at α₁ = 5/16
with value 1/24.)

## 2. Proof of Theorem U (PROVED)

### 2.1 External inputs (checked against the sources)

* **(Bu) Burgess, cube-free conductor.** For every integer r ≥ 1 and ε > 0 there is an effective C = C(r, ε) such that for
  every primitive Dirichlet character χ of cube-free conductor f > 1 and all real M ≥ 0, N ≥ 1,
  |Σ_{M<n≤M+N} χ(n)| ≤ C·N^{1−1/r}·f^{θ}, θ = θ_{r,ε} := (r + 1)/(4r²) + ε.
  Source: D. A. Burgess, *On character sums and L-series II*, Proc. LMS (3) 13 (1963) 524–536; Iwaniec–Kowalski,
  *Analytic Number Theory*, Thm 12.6; restated verbatim in the abstract of Hasanalizade–Lin–Martin–Luna Martínez–Treviño,
  arXiv:2511.17778 ("for χ_q a primitive Dirichlet character modulo q with q cubefree, Σ_{M<n≤M+N}χ_q(n) =
  O(N^{1−1/r}q^{(r+1)/(4r²)+ε}) for all integers r ≥ 1"), which also gives explicit constants (effectivity). Every conductor
  below is 4^a·(odd squarefree), a ≤ 1, hence cube-free.
* Everything else is elementary (Abel summation, Dirichlet's hyperbola method, multiplicativity).

Notation. Fix r ≥ 3 and ε ∈ (0, 1/100); κ := 1/r; τ := rθ = (r + 1)/(4r) + rε. "≪" constants depend only on r, ε and the
fixed exponents α₀, α₁, β, γ, ν; p^{o(1)} absorbs divisor-type factors such as τ(m), 2^{ω(m)} for m ≤ p².

### 2.2 Lemma 2.1 (tails of L(1, ·))

Let χ(n) = χ*(n)·1[gcd(n, e) = 1] with χ* primitive of cube-free conductor f > 1 and e ≥ 1 squarefree. Then for t ≥ 1,
  |Σ_{n>t} χ(n)/n| ≤ K t^{−κ},  |Σ_{n>t} χ(n) log n/n| ≤ (r + 1)K t^{−κ}(1 + log t),  K := (1 + r)·τ(e)·C·f^{θ}.
*Proof.* S(v) := Σ_{n≤v} χ(n) = Σ_{g|e} μ(g)χ*(g)Σ_{m≤v/g} χ*(m), so |S(v)| ≤ τ(e)C v^{1−κ}f^θ by (Bu) (for v/g < 1 the inner sum
is empty). Abel summation: Σ_{n>t}χ(n)/n = −S(t)/t + ∫_t^∞ S(v)v^{−2}dv, giving ≤ τ(e)Cf^θ(t^{−κ} + r t^{−κ}). For the second
sum, d(log v/v) = (1 − log v)v^{−2}dv and ∫_t^∞ v^{−1−κ}(1 + log v)dv = r t^{−κ}(1 + log t + r). ∎

### 2.3 Lemma 2.2 (hyperbola with two characters)

For functions F, G on ℕ and y ≥ 1 let Φ(y) := Σ_{ab≤y} F(a)G(b)/(ab).
(a) If F and G are as in Lemma 2.1 with constants K_F, K_G ≥ 1, then for y with y^κ ≥ K_F K_G:
  |Φ(y) − L(1, F)L(1, G)| ≤ (2r + 3)·(K_F K_G y^{−κ})^{1/2}.
(b) If F ≡ 1 and G is as in Lemma 2.1 with constant K_G, then for 1 ≤ z ≤ y:
  |Φ(y) − L(1, G)(log y + γ_E) − L′(1, G)| ≤ 5r²K_G (z/y)^κ(1 + log y) + 2/z.
*Proof.* Hyperbola identity, for 1 ≤ z ≤ y, with 𝔉(t) = Σ_{a≤t}F(a)/a, 𝔊(t) = Σ_{b≤t}G(b)/b:
  Φ(y) = Σ_{a≤z}(F(a)/a)𝔊(y/a) + Σ_{b≤y/z}(G(b)/b)𝔉(y/b) − 𝔉(z)𝔊(y/z).
(a) Write 𝔉(t) = L_F − r_F(t), 𝔊 = L_G − r_G(t), |r_F(t)| ≤ K_F t^{−κ}, |r_G(t)| ≤ K_G t^{−κ}. Expanding (all L_F L_G terms
combine to one), Φ(y) − L_F L_G = −Σ_{a≤z}(F(a)/a)r_G(y/a) − Σ_{b≤y/z}(G(b)/b)r_F(y/b) − r_F(z)r_G(y/z). Using
Σ_{a≤z}a^{κ−1} ≤ 1 + z^κ/κ, the three terms are ≤ K_G y^{−κ}(1 + r z^κ), K_F y^{−κ}(1 + r(y/z)^κ), K_F K_G y^{−κ}. Choose
z := y^{1/2}(K_F/K_G)^{r/2}; the hypothesis y^κ ≥ K_F K_G (and K_F, K_G ≥ 1) gives 1 ≤ z ≤ y. Then
r K_G (z/y)^κ = r K_F z^{−κ} = r(K_F K_G y^{−κ})^{1/2}, K_F K_G y^{−κ} ≤ (K_F K_G y^{−κ})^{1/2} and
(K_F + K_G)y^{−κ} ≤ 2K_FK_G y^{−κ} ≤ 2(K_FK_Gy^{−κ})^{1/2}; total ≤ (2r + 3)(…)^{1/2}.
(b) Now 𝔉(t) = log t + γ_E + r₁(t), |r₁(t)| ≤ 1/t (t ≥ 1). Substituting and collecting exactly as in `BM_LVALUE` Lemma 2.4:
Φ(y) = L_G(log y + γ_E) + L′(1, G) + [−Σ_{a≤z}(1/a)r_G(y/a) − log(y/z)·r_G(y/z) − r′_G(y/z) + Σ_{b≤y/z}(G(b)/b)r₁(y/b)
+ r₁(z)r_G(y/z)], where L′(1, G) = −Σ_b G(b)log b/b and r′_G(t) := Σ_{b>t}G(b)log b/b. (Check: the coefficient of
log z cancels between Σ_{a≤z}(1/a)L_G and −𝔉(z)L_G; the b-sum gives (log y + γ_E)(L_G − r_G(y/z)) − Σ_{b≤y/z}G(b)log b/b.)
Bounds: K_G y^{−κ}(1 + r z^κ); K_G(z/y)^κ log y; (r + 1)K_G(z/y)^κ(1 + log y); Σ_{b≤y/z}(1/b)(b/y) ≤ 1/z; K_G(z/y)^κ/z. ∎

### 2.4 Lemma 2.3 (the genus-exact subfamily; = Thm 5.4 (19)–(20), rechecked)

Let u ≡ 1 (mod 4) be squarefree, w odd, gcd(w, u) = 1, p ∤ uw, 8uw ≤ p, D = D_u := −4up (a fundamental discriminant:
−up ≡ 3 (4) and up is squarefree). Then (u, 2w), (2w, u) ∈ 𝒫(p) are distinct, each has
  s(q)/φ(q) = 2^{ω(u)+ω(w)}/(φ(u)φ(w))  (q = 8uw),
and each is genus-matched (p·a ∈ □ mod q) iff
  (i) χ_D(ℓ) = 1 for every prime ℓ | w;  (ii) (−2pw/ℓ) = 1 for every prime ℓ | u;  (iii) w ≡ w₀ := −(p + u)/2 (mod 4).
Consequently, for w also squarefree, the genus weight of the two pairs equals
  (2^{ω(u)}/φ(u))·(2^{ω(w)}1[(i)]/φ(w))·2·2^{−ω(u)−1} Σ_{η∈𝔈_u} ε_η η(w),
with 𝔈_u := {η_{d,j} := (·/d)·χ₋₄^j : d | u, j ∈ {0, 1}} (Jacobi symbol (·/d)), ε_{d,j} := (−2p/d)·χ₋₄(w₀)^j ∈ {±1}, ε_{1,0} = 1.
*Proof.* 4·u·2w − u − 2w < 8uw ≤ p; gcd(u, 2w) = 1; u + 2w odd. q = 8uw with 8 ‖ q, so (ℤ/q)^× ≅ (ℤ/8)^× × ∏_{ℓ|uw}(ℤ/ℓ)^×
(uw squarefree odd for the weight; for the matching conditions only the primes matter), s(q) = 4·2^{ω(uw)}, φ(q) = 4φ(u)φ(w).
A unit is a square mod q iff it is ≡ 1 mod 8 and a quadratic residue mod each odd ℓ | q. With a = −(u + 2w): a ≡ −u (mod ℓ | w)
gives (i) ((−up/ℓ) = (D/ℓ)); a ≡ −2w (mod ℓ | u) gives (ii); p·a ≡ 1 (mod 8) ⟺ a ≡ p ⟺ 2w ≡ −(p + u) (mod 8) ⟺ (iii)
(p + u ≡ 2 mod 4). The pair (2w, u) has the same q and a. For w coprime to u, (ii)–(iii) have indicator
∏_{ℓ|u}½(1 + (−2p/ℓ)(w/ℓ))·½(1 + χ₋₄(w₀)χ₋₄(w)); expand. ∎ (Lemma 2.3 is checked by the direct square-class test with 0
mismatches on all runs of `scripts/z53_genuslval_family.c`, §5.)

### 2.5 Proposition 2.4 (windowed sums: only η = 1 survives)

Let 0 < α₁ < 1, 𝒰 := {u squarefree, u ≡ 1 (4), U₀ < u ≤ U₁}, U_i = p^{α_i}, and put Y = p^β, X = p^γ with
  γ < 1 − α₁ (so 8uw ≤ p for large p),  β > τ(1 + α₁) + 4ε.
For u ∈ 𝒰 and η ∈ 𝔈_u let
  S_η(u) := Σ_{Y<w≤X, w ∈ 𝒮_u} η(w)·2^{ω(w)}1[χ_D(ℓ) = 1 ∀ℓ | w]/φ(w),  𝒮_u := {w odd squarefree, gcd(w, up) = 1}.
Then, uniformly in u ∈ 𝒰 and η ∈ 𝔈_u, with some δ = δ(r, ε, β, α₁) > 0,
  **S_η(u) = 1[η = 1]·H_u(1)·L(1, χ_D)·(γ − β) log p + O(p^{−δ}),  H_u(1) = (6/π²)∏_{ℓ|2up} ℓ/(ℓ + 1).**
*Proof.* (1) *Factorisation.* For w ∈ 𝒮_u, Σ_{b|w}χ_D(b) = ∏_{ℓ|w}(1 + χ_D(ℓ)) = 2^{ω(w)}1[(i)] (no ℓ | w divides D). Let
g(w) := 1_{𝒮_u}(w)(w/φ(w))Σ_{b|w}χ_D(b). Then g = 1 ∗ χ_D ∗ h with h multiplicative: h(ℓ) = −1, h(ℓ^k) = 0 (k ≥ 2) for ℓ | 2up;
for ℓ ∤ 2up, comparing local series (1 + c_ℓY)·(1 − Y)(1 − χ_D(ℓ)Y), c_ℓ = (1 + χ_D(ℓ))ℓ/(ℓ − 1):
χ_D(ℓ) = 1: h(ℓ) = 2/(ℓ − 1), h(ℓ²) = −(3ℓ + 1)/(ℓ − 1), h(ℓ³) = 2ℓ/(ℓ − 1); χ_D(ℓ) = −1: h(ℓ²) = −1, others 0.
Hence for 0 ≤ θ′ < 1/2, Σ_c |h(c)|c^{θ′−1} ≤ 2^{ω(2up)}·Π_{θ′} with Π_{θ′} := ∏_{ℓ≥3}(1 + 2ℓ^{θ′−1}/(ℓ−1) + 5ℓ^{2θ′−2}
+ 3ℓ^{3θ′−3}) < ∞, so it is p^{o(1)}. At s = 1 every unramified factor is 1 − ℓ^{−2} (split: (ℓ+1)(ℓ−1)/ℓ²; inert:
(1 − 1/ℓ)(1 + 1/ℓ)), so H_u(1) := Σ_c h(c)/c = ∏_{ℓ|2up}(1 − 1/ℓ)∏_{ℓ∤2up}(1 − ℓ^{−2}) = (6/π²)∏_{ℓ|2up}ℓ/(ℓ + 1).
Since η is completely multiplicative, η(w)g(w)/w = Σ_{abc=w}(η(a)/a)(ηχ_D(b)/b)(η(c)h(c)/c), so
  S_η(u) = Σ_{c≥1}(η(c)h(c)/c)·[Φ_η(X/c) − Φ_η(Y/c)],  Φ_η(y) := Σ_{ab≤y} η(a)(ηχ_D)(b)/(ab)  (Φ_η(y) = 0 for y < 1).
(2) *The characters.* η = η_{d,j}: (·/d) is the primitive character of conductor d (d odd squarefree; trivial if d = 1),
and χ₋₄(·/d) is primitive of conductor 4d. For odd n, χ_D(n) = (−up/n) = χ₋₄(n)(n/u)(n/p) (Jacobi; reciprocity for
u ≡ p ≡ 1 (4)), and χ_D(n) = 0 for even n. So
  η_{d,j}χ_D(n) = χ₋₄(n)^{j+1}·(n/(u/d))·(n/p)·1[gcd(n, 2d) = 1],
i.e. ηχ_D = χ*·1[gcd(·, 2d) = 1] with χ* primitive of conductor f_G = 4^{1−j}(u/d)p (cube-free, > 1). **ηχ_D is non-principal
for every η ∈ 𝔈_u because p | f_G.** η itself is principal (≡ 1) iff (d, j) = (1, 0); otherwise it is primitive of conductor
f_F = 4^j d. Crucially **f_F·f_G = 4up** for every (d, j).
(3) *η ≠ 1.* Lemma 2.1 gives K_F = (1 + r)Cf_F^θ, K_G = (1 + r)τ(2d)Cf_G^θ, so K_FK_G ≤ (1 + r)²C²τ(2d)(4up)^θ ≤
p^{θ(1+α₁)+o(1)}. For c ≤ C₀ := p^{ε}, both X/c and Y/c are ≥ p^{β−ε}, and (p^{β−ε})^κ ≥ K_FK_G p^{κε} because
(β − ε)κ > θ(1 + α₁) + κε ⟸ β > rθ(1 + α₁) + 2ε = τ(1 + α₁) + 2ε. Lemma 2.2(a) gives |Φ_η(X/c) − Φ_η(Y/c)| ≤
2(2r + 3)p^{−κε/2}. For c > C₀ use |Φ_η(y)| ≤ Σ_{n≤y}τ(n)/n ≤ (1 + log y)², so the c > C₀ part is
≤ 2(1 + log X)²·C₀^{−θ′}Σ_c|h(c)|c^{θ′−1} ≤ p^{−εθ′+o(1)} (fix θ′ = 1/4). The c ≤ C₀ part is ≤ 2(2r + 3)p^{−κε/2}Σ_c|h(c)|/c =
p^{−κε/2+o(1)}. So S_η(u) = O(p^{−δ}).
(4) *η = 1.* Lemma 2.2(b) with G = χ_D (K_G ≤ (1 + r)C(4up)^θ), y ∈ {X/c, Y/c} ≥ p^{β−ε} (c ≤ C₀) and z := p^{ε}:
(z/y)^κK_G ≤ p^{κ(2ε − β) + θ(1+α₁) + o(1)} ≤ p^{−κε+o(1)}. Thus Φ_1(X/c) − Φ_1(Y/c) = L(1, χ_D)log(X/Y) + O(p^{−κε/2}) (the constants
L(1, χ_D)γ_E + L′(1, χ_D) cancel in the difference — this is the point of the window). Summing over c ≤ C₀ with weight h(c)/c,
using Σ_{c≤C₀}h(c)/c = H_u(1) + O(C₀^{−1/4}p^{o(1)}), L(1, χ_D) ≤ 1 + log(4up), and the c > C₀ bound of (3), gives
S_1(u) = H_u(1)L(1, χ_D)(γ − β)log p + O(p^{−δ}). ∎

### 2.6 Proposition 2.5 (the average of L(1, χ_{−4up}) over u)

Let 0 < α₀ < α₁ < 1 with **α₀ > τ²(1 + α₁) + 3ε** (C3). Then
  Σ_{u∈𝒰} L(1, χ_{−4up})/u ≥ (2/π²)(α₁ − α₀)log p − O(1).
*Proof.* Put ν := τ(1 + α₁) + ε, N := p^ν. For u ∈ 𝒰, χ_{−4up}(n) = 0 for even n and = χ₋₄p(n)(u/n) for odd n
(χ₋₄p(n) := χ₋₄(n)(n/p) = χ_{−4p}(n); (n/u) = (u/n) by reciprocity, u ≡ 1 (4)). So
  L(1, χ_{−4up}) = Σ_{n≤N, n odd} χ_{−4p}(n)(u/n)/n + ρ_u,  |ρ_u| ≤ (1 + r)C(4up)^θ N^{−κ}  (Lemma 2.1, conductor 4up).
*Tail.* Σ_{u∈𝒰}|ρ_u|/u ≤ (log p + 1)(1 + r)C·4^θ p^{θ(1+α₁) − κν} = p^{−κε + o(1)} (since κν = θ(1 + α₁) + κε).
*Head.* Interchange: Σ_{n≤N odd}(χ_{−4p}(n)/n)·V(n), V(n) := Σ_{u∈𝒰}(u/n)/u.
– n = m² (m odd): (u/m²) = 1[gcd(u, m) = 1] ≥ 0 and χ_{−4p}(m²) ∈ {0, 1}: every such term is ≥ 0; keep only n = 1:
V(1) = Σ_{u∈𝒰}1/u = (2/π²)(α₁ − α₀)log p + O(1) (squarefree u ≡ 1 (4) have counting function (2/π²)x + O(√x)).
– n not a square: n = n₁m² with n₁ > 1 squarefree, and 1[u ≡ 1 (4)](u/n) = ½(ψ₁(u) + ψ₂(u)) with ψ₁ = (·/n₁)·1[gcd(·, 2m) = 1],
ψ₂ = χ₋₄(·/n₁)·1[gcd(·, m) = 1] — completely multiplicative, with primitive parts of cube-free conductors n₁, 4n₁ > 1.
By μ²(u) = Σ_{e²|u}μ(e) and Lemma 2.1's partial-sum bound, for V′ ≥ 1:
|Σ_{u≤V′}μ²(u)ψ_i(u)| ≤ Σ_{e≤√V′}|Σ_{v≤V′/e²}ψ_i(v)| ≤ τ(2m)C(4n₁)^θ V′^{1−κ}Σ_e e^{2κ−2} ≤ ζ(2 − 2κ)τ(2m)C(4n)^θ V′^{1−κ}
(r ≥ 3 ⇒ 2 − 2κ > 1). Partial summation over (U₀, U₁] gives |V(n)| ≤ (2 + r)ζ(2 − 2κ)τ(2m)C(4n)^θ U₀^{−κ}. Hence
Σ_{n≤N non-square}|V(n)|/n ≤ p^{o(1)}U₀^{−κ}Σ_{n≤N}n^{θ−1} ≤ p^{o(1)}N^θ U₀^{−κ} = p^{θν − κα₀ + o(1)}, and θν − κα₀ < 0
⟸ α₀ > rθν = τν = τ²(1 + α₁) + τε. ∎

### 2.7 Proof of Theorem U

Take u ∈ 𝒰, w ∈ 𝒮_u ∩ (Y, X] in Lemma 2.3 (conditions γ < 1 − α₁ ⇒ 8uw ≤ p; distinct (u, w) give distinct pairs since
the odd coordinate is u). All terms of M_gen are ≥ 0, so
  M_gen(p) ≥ Σ_{u∈𝒰}Σ_w (genus weight of (u, 2w) and (2w, u)) = Σ_{u∈𝒰}(1/φ(u))Σ_{η∈𝔈_u}ε_η S_η(u)
(the factor 2·2^{ω(u)}·2^{−ω(u)−1} = 1). By Prop 2.4 (|𝔈_u| = 2^{ω(u)+1}, Σ_{u≤U₁}2^{ω(u)+1}/φ(u) ≪ log²p),
  M_gen(p) ≥ (γ − β)log p·Σ_{u∈𝒰}H_u(1)L(1, χ_{−4up})/φ(u) − O(p^{−δ}log²p).
Now H_u(1)/φ(u) = (6/π²)(2/3)(p/(p + 1))∏_{ℓ|u}(ℓ/(ℓ + 1))/φ(u) = (4/π²)(p/(p+1))·u⁻¹∏_{ℓ|u}(1 − ℓ^{−2})^{−1} ≥ (4/π²)(p/(p+1))/u
(u squarefree), and L(1, χ_{−4up}) > 0. By Prop 2.5,
  M_gen(p) ≥ (γ − β)(4/π²)(2/π²)(α₁ − α₀)(log p)² − O(log p) = (c(α₀, α₁, β, γ) − o(1))(log p)².
Conditions used: (C1) γ < 1 − α₁; (C2) β > τ(1 + α₁) + 4ε; (C3) α₀ > τ²(1 + α₁) + 3ε; with τ = (r+1)/(4r) + rε. Letting
r → ∞, ε → 0 (all choices fixed before p → ∞) gives τ → 1/4 and the stated optimum. Every constant is effective (Burgess's
C(r, ε) is effective, arXiv:2511.17778 makes it explicit; nothing ineffective such as Siegel's theorem is used: L(1, χ) > 0 is
only used through sign). ∎

*Remarks.* (1) The constant is not optimised: we drop the n = m² > 1 terms of Prop 2.5, the factor ∏_{ℓ|u}(1 − ℓ^{−2})^{−1},
u ≡ 3 (4) and B ≡ 0 (4). Replacing Prop 2.5 by Heath-Brown's quadratic large sieve would allow α₀ → 0 and give
(8/π⁴)·max_{α₁}(3/4 − 5α₁/4)α₁ = 9/(10π⁴) ≈ 0.0092 (Assessment; not written out). A large-sieve average over u in Prop 2.4 would be
needed to approach the strip constant 2/π⁴. (2) The proof never evaluates an L-function at a single small modulus: Prop 2.4
averages over the free variable w at fixed u, Prop 2.5 averages over the free variable u; p is fixed throughout (B6 screen).

### 2.8 T1 audit: the step that fails at odd squares (PROVED)

M_gen(m²) = 0 (`SINGLE_P_COUNT` Prop 2.2(b)), so the argument must break at n = m². Primality of p is used in exactly one
place: Prop 2.4(2), "ηχ_D is non-principal since p | f_G". For n = m² (gcd(m, 2u) = 1), D = −4um² has χ_D = χ_{−4u}·1[gcd(·, m) = 1]
and for η = η_{u,1} = χ₋₄(·/u) the product ηχ_D is principal (on integers coprime to 2um). Then Φ_η acquires a log term and S_η has
main term ε_η·L(1, χ_{−4u})·H′·log(X/Y) of the same size as the η = 1 term; and its sign is forced: ε_{u,1} = (−2m²/u)χ₋₄(w₀) =
(−2/u)χ₋₄(−(m² + u)/2) = −1 for u ≡ 1 and u ≡ 5 (mod 8) alike (m² ≡ 1 mod 8). So the two poles cancel, exactly as in
`LOWERTAIL_DEEP_ASTRA` §5.4 "T1 audit". (Prop 2.5 is true at squares as well; it is not where T1 enters.) For non-square
n ≡ 1 (4), ηχ_D is non-principal (its conductor contains the odd squarefree kernel of n or u/d), and the same argument
should give M_gen(n) ≫ (local factor at the primes of n)·log²n (Assessment; not written out, not needed).

## 3. Closed forms of the genus layer (the brief's L(1, χ_pψ)·L(1, ψ′) products)

### 3.1 Proposition C (u-slice closed form; PROVED)

For squarefree u ≡ 1 (4) let S_u(p) := Σ_{B even, (u,B)∈𝒫(p)} (s(q)/φ(q))1[p·a ∈ □] (one order; M_gen = 2Σ_{u odd}S_u).
On this slice B = 2w with w odd (p + u ≡ 2 (4) forces 2 ‖ B), X_u := ⌊(p + u)/(2(4u − 1))⌋, and Lemma 2.3 (whose proof never
used w squarefree; for general w, s(q)/φ(q) = 2^{ω(u)+ω(w)}/(φ(u)φ(w)) still) gives exactly
  S_u(p) = (2φ(u))⁻¹ Σ_{η∈𝔈_u} ε_η Σ_η(X_u),  Σ_η(X) := Σ_{w≤X, w odd, gcd(w,u)=1} η(w)·2^{ω(w)}1[χ_D(ℓ) = 1 ∀ℓ|w]/φ(w).
**Claim.** If u ≤ p^{α} with 1 − α > τ(1 + α) + 5ε (τ = (r + 1)/(4r) + rε; as r → ∞, ε → 0 this allows every α < 3/5),
then with D = −4up and δ = δ(r, ε, α) > 0:
  Σ_1(X_u) = L(1, χ_D)H_u(1)·[log X_u + γ_E + L′/L(1, χ_D) + H_u′/H_u(1)] + O(p^{−δ}),
  Σ_η(X_u) = L(1, η)·L(1, ηχ_D)·H_{u,η}(1) + O(p^{−δ})  (η ≠ 1),
where now H_{u,η}(s) = ∏_ℓ h_ℓ(η(ℓ)ℓ^{−s}) with h_ℓ(Y) = 1 − Y (ℓ | 2up), 1 + 2Y/(ℓ − 1) − (ℓ + 1)Y²/(ℓ − 1) (χ_D(ℓ) = 1),
1 − Y² (χ_D(ℓ) = −1); H_u := H_{u,1}. Here L(1, η) = L(1, χ_{d*}) (j = 0) or L(1, χ_{−4d*}) (j = 1), d* = (−1)^{(d−1)/2}d, and
L(1, ηχ_D) = L(1, χ_{D′})∏_{ℓ|2d}(1 − χ_{D′}(ℓ)/ℓ) with D′ = −4(ep)* (j = 0) or (ep)* (j = 1), e = u/d.
*Proof.* Same as Prop 2.4 with the window (Y, X] replaced by [1, X_u] and h by the non-squarefree local factors above
(g's local series at a split ℓ is 1 + (2ℓ/(ℓ−1))Y/(1 − Y), BM_LVALUE Lemma 2.2; at inert ℓ it is 1; all |h(ℓ^k)| ≤ 2, k ≤ 2).
Σ_η(X) = Σ_c(η(c)h(c)/c)Φ_η(X/c). For c ≤ X/y₀ with y₀ := (4up)^τ p^{3ε} Lemma 2.2 gives Φ_η(X/c) = (main) + O(p^{−κε/2}),
the main being L(1, η)L(1, ηχ_D) (η ≠ 1) or L(1, χ_D)(log(X/c) + γ_E) + L′(1, χ_D) (η = 1); the c > X/y₀ part and the tails of the
c-sums of the main terms are ≤ (X/y₀)^{−1/4}p^{o(1)}(1 + log p)³ (Σ_c|h(c)|c^{−3/4}(1 + log c) = p^{o(1)}). X_u/y₀ ≥ p^{ε}
iff (roughly) 1 − α > τ(1 + α), α < (1 − τ)/(1 + τ) → 3/5. Finally Σ_c h(c)(log X − log c)/c = H_u(1)log X + H_u′(1). ∎
(The identity of the twisted characters is the computation of Prop 2.4(2). For u ≡ 3 (4) the slice has B = 2^k w with
k = 2 if p + u ≡ 4 (8) and k ≥ 3 if p + u ≡ 0 (8), weight 2^{1−k}, and characters (·/d) only — same proof; not tabulated.)

**Reading.** The principal-genus term (η = 1) is the class-number term of K_u = ℚ(√−up): L(1, χ_{−4up}) = πh(−4up)/√(4up),
times a log. Each other genus character η = η_{d,j} of the slice contributes the product **L(1, ψ′)·L(1, χ_pψ)** with
ψ′ = η of conductor (4)d and χ_pψ of conductor (4)(u/d)p — no log, explicit sign ε_η = (−2p/d)χ₋₄(w₀)^j, explicit Euler
factor. For d = u, j = 1 the second factor is L(1, χ_p)(1 − χ_p(2)/2) up to Euler factors: this is the slice's share of the
BM term T(p) ≈ (σ/4)E L(1, χ_p)² of `BM_LVALUE` (which arises after summing χ_p(u)L(1, χ_{−4u})/u over u). So the whole
genus layer is "BM plus all other (d, j)", each an L(1)·L(1) product — the class-in-coset layer of FRONTIER §7.3 written out.

*Global form (Assessment, not fully written).* Splitting 𝒫(p) by the hyperbola at u ≍ p^{3/5−ε} (resp. B ≍ p^{2/5+ε}) and
using the mirror slices (B fixed, u summed; conductors ≤ 8Bp, characters mod 8w) gives M_gen(p) as a sum of ≍ p^{3/5}
such slice closed forms with total error O(p^{−δ}·p^{o(1)}): the cross constants of the u-slices cancel against the overlap
slices (window effect), so the u-side contributes only principal-genus log terms and the B-side carries all L(1)·L(1) cross
products. The B-side mirror lemma (2-adic bookkeeping with k = v₂(B)) was not written out; we do not label this PROVED.

### 3.2 Numerical verification (EVIDENCE; `scripts/z53_genuslval_slice.{c,py}` → `data/z53/genuslval/slice_checks.txt`)

Exact slice by direct summation (square-class test) vs. the η-expansion (identical to 10⁻¹², confirming the projector) vs.
the closed form (L-values by PARI `lfun`, Euler products to ℓ ≤ 2·10⁶):

| p | p mod 8 | u = 1: S_u / closed / err | u = 5 | u = 13 | u = 21 |
|---|---|---|---|---|---|
| 9601 (★)-zero | 1 | 0.91179 / 0.91325 / −1.5e−3 | 0.2414 / 0.2652 / −2.4e−2 | 0.20655 / 0.20614 / +4e−4 | 0.0556 / 0.0662 / −1.1e−2 |
| 102001 (★)-zero | 1 | 1.45923 / 1.45900 / +2.4e−4 | 0.30407 / 0.30468 / −6e−4 | 0.06202 / 0.06614 / −4.1e−3 | 0.04046 / 0.04078 / −3e−4 |
| 1134241 (★)-zero | 1 | 2.63832 / 2.63752 / +8e−4 | 0.39243 / 0.39259 / −1.6e−4 | 0.07941 / 0.08039 / −1e−3 | 0.44444 / 0.44402 / +4e−4 |
| 8813281 (★)-zero | 1 | 2.028549 / 2.028559 / −1.0e−5 | 0.89082 / 0.89198 / −1.2e−3 | 0.11536 / 0.11590 / −5e−4 | 0.08497 / 0.08509 / −1.2e−4 |
| 99999989 | 5 | 8.25576 / 8.25615 / −4e−4 | 0.384032 / 0.384010 / +2e−5 | 0.42554 / 0.42568 / −1.3e−4 | 0.20220 / 0.20212 / +9e−5 |

(At p = 409, X_5 = 10: the asymptotic is not yet operative, err −0.11 — recorded in the data file.) Each η-component is
matched individually (e.g. 8813281, u = 21: eight components, max |err| 9.8·10⁻³ on values 0.48–4.46). The error falls
with X_u as predicted.

## 4. (b) Which genus characters can make M_gen small

**Exact decomposition (PROVED, Lemma 2.3 + Prop C).** In each slice, S_u = (2φ(u))⁻¹[Σ_1 + Σ_{η≠1}ε_ηΣ_η], with Σ_1 ≈
L(1, χ_{−4up})H_u(1)·log X_u > 0 and the 2^{ω(u)+1} − 1 cross terms ε_η L(1, η)L(1, ηχ_D)H_{u,η}(1) of either sign.
* **What can make a slice small:** (α) L(1, χ_{−4up}) small (a Siegel-type small class number h(−4up)), or (β) cross terms
  with ε_η = −1 and large L(1, ηχ_D) = L(1, χ_pψ) (i.e. χ_p ψ(ℓ) = +1 at the small primes ℓ). Both occur for individual u at
  attainable p (EVIDENCE: at p = 8 813 281, u = 13: Σ_1 = 4.46 but ε = −1 on (·/13) and χ₋₄(·/13) with Σ = 0.57, 1.81, so the
  slice is (4.46 + 0.69 − 0.57 − 1.81)/24 = 0.115, i.e. the net cross term −1.69 removes 38 % of the principal mass
  Σ_1 = 4.46; at 102001, u = 13 the slice is 0.062).
* **What cannot happen (PROVED, Theorem U):** neither (α) nor (β) can make M_gen(p) itself o(log²p) for p ≥ p₀ — the windowed
  subfamily has no cross terms at all (they are constants, cancelled by the window), and (α) is excluded on average over u by
  Prop 2.5 (Burgess in u), which does not care about one exceptional character. So at a single large p **no genus character
  configuration can make M_gen small**; this is unconditional and effective. Quantitatively M_gen(p)/M₀(p) ≥ (2/(3π⁴))/(3/(2π²))
  − o(1) = 4/(9π²) − o(1) ≈ 0.045 (M₀ = (3/(2π²) + o(1))log²p, `BM_CORRECTED` Thm 2.2).
* **EVIDENCE for the attained range:** min M_gen/M₀ over the sampled primes p ≡ 1 (4), 10³ ≤ p ≤ 10⁷ (all primes ≤ 10⁶, the window
  [9.8·10⁶, 10⁷] and the stratified sample of `BM_LVALUE`) is 0.57 (p = 8089); for p > 10⁵ it is 0.616 (p = 176089); at the 14
  (★)-zero primes 0.57–0.92. min M_gen/log²p is 0.084 (p = 8089), 0.092 (p > 10⁵), 0.103 on [9.8·10⁶, 10⁷]: 12–15× above c_U.
  (Computed from `data/z52c/bmL/*.tsv.gz`, column Mgen.)
* **Assessment (not proved).** Heuristically (`SINGLE_P_COUNT` §4.1 and the slice formula), M_gen − M₀ ≈ (log p)·Σ_{ψ}c_ψ
  L(1, χ_pψ) + O(L(1, χ_p)²): its χ_p-dependence is an infinite weighted family of twisted L-values L(1, χ_pψ), ψ running over the
  genus characters of the cofactor, not finitely many. Under GRH each is ≪ log log p, which suggests M_gen ~ M₀; the observed
  M_gen/M₀ ∈ [0.57, 1.46] reflects L(1, χ_pψ) of size up to ≈ 5 at 10⁷ (hard primes are QR-rich, `BM_LVALUE` §3.3).
* **Which characters do it at the (★)-zero primes (EVIDENCE; `scripts/z53_genuslval_decomp{.c,_stats.py}` →
  `data/z53/genuslval/decomp_stats.txt`, `decomp_raw.tsv`).** Exact decomposition (Lemma 2.3, no asymptotics) of the part of
  M_gen coming from all squarefree u ≡ 1 (4) slices, by genus character type: P (η = 1, principal genus), C4 (η = χ₋₄; product
  L(1, χ₋₄)L(1, χ_{up}) up to Euler factors), CBM (η = χ₋₄(·/u), u > 1; ηχ_D = χ_p, the BM-like product L(1, χ_{−4u})L(1, χ_p)),
  CU0 (η = (·/u)), CMIX (1 < d < u). Each of the 14 (★)-zero primes against 60 random primes p′ ≡ 1 (8) in [0.9p, 1.1p]
  (seed 53); mean percentile of the failures: **P 26, C4 6, CBM 20, CU0 35, CMIX 68, total 7**. At 11 of 14 failures C4 is at
  percentile ≤ 4, and at 9 of 14 (all six failures ≥ 712321 among them) CBM is at ≤ 3; 577 and 329617 go the other way (CBM
  at percentile 100 / 83). Typical sizes at 10⁶–10⁷ (per log²p): P ≈ 0.040–0.045 for controls vs 0.035–0.039 at failures; C4 ≈ −0.001
  vs −0.0028 … −0.0043; CBM ≈ 0 vs −0.0016 … −0.0040. **Reading:** at the hard primes the genus deficit is carried mainly by two specific cross characters, χ₋₄ and the
  BM-like χ₋₄(·/u), whose second L-factor L(1, χ_pψ) is large (QR-richness of p) and whose sign ε_η is −1 on the dominant
  small-u slices; the principal class-number term is only moderately low. This identifies "which genus characters" at
  attained sizes; by Theorem U their combined effect is bounded away from killing M_gen as p → ∞.
* **What Siegel / Stephens / Burgess / GRH give (brief (a)).** Siegel (ineffective): each slice's principal term is
  ≫_ε p^{−ε}·log p — useless for log². Landau–Page/Tatuzawa: at most one exceptional u — superseded by the averaging of
  Prop 2.5, which needs no such input. Stephens (|L(1, χ)| ≤ (c_S + o(1))log q): bounds every cross term by O(log²p), so the
  *unwindowed* slice sums are only bounded by O(log³p) in total — insufficient; the window trick is what removes the cross
  terms. Burgess (cube-free): Theorem U, 2/(3π⁴). GRH (or a fixed strip): β, α₀ → 0, constant 2/π⁴ (Thm 5.4).

## 5. Falsifier F1 and controls (EVIDENCE / CERTIFIED identities)

`scripts/z53_genuslval_family.c` (engine) + `scripts/z53_genuslval_f1.py` (driver; A_u from PARI class numbers).
* **Lemma 2.3 check (CERTIFIED on the listed ranges):** direct square-class test ≡ conditions (i)–(iii) on every family pair:
  0 mismatches at p = 409, 577, 5569, 9601 (u ≤ 40, w ≤ p/320), 102001, 1000033, 8813281, 100000049 (windows below).
  M_gen recomputed independently at 409, 577, 5569, 9601: 3.9991, 5.3524, 6.2407, 7.9262 (= `BM_LVALUE` §1.4 table).
  T1 controls: n = 9, 961: family = M_gen = 0.
* **Windowed family vs predicted main term** (u ∈ (5, 60], w ∈ (200, p/480]):

| p | family F | Σ_u A_u log(X/Y)/φ(u) | ratio | max slice rel. err (η = 1) |
|---|---|---|---|---|
| 1000033 | 0.4420 | 0.4547 | 0.972 | 5.7 % |
| 8813281 (★)-zero | 0.8145 | 0.8120 | 1.003 | 4.6 % |
| 100000049 | 0.9537 | 0.9850 | 0.968 | 2.2 % |

  and with u ∈ (10, 200], w ∈ (2000, p/1600] at 8813281: 0.3195 vs 0.3075 (1.039). At p = 102001 the window is (200, 212]:
  degenerate, as expected. The cross terms (η ≠ 1) cancel in the windows to within these few per cent at p ≤ 10⁸; the proved
  power saving is far below visibility at these sizes (Assessment: the family's proved share, (8/π⁴)·(γ−β)(α₁−α₀) ≈ 0.007 of
  log²p, is ≈ 5 % of M_gen).
* **Near-squares / composite controls.** The theorem is uniform over primes p ≡ 1 (4); nothing depends on p − m². For
  composite non-square n the proof is expected to go through (§2.8); for odd squares it provably fails at the identified step.

## 6. The four FRONTIER §4 hard screens (for Theorem U as an ES ingredient)

1. **T1 (squares):** passes — the step false at m² is identified (§2.8: a second pole from η = χ₋₄(·/u) with forced sign −1).
2. **8/131 (numerator):** not applicable as a solution statement — Theorem U concerns the numerator-4 genus main term
   M_gen, and asserts nothing about solutions. Used as an ES method it inherits screen 4's failure.
3. **Tied modulus (B2):** fails — main term only (B3). The class of the divisor inside the coset (characters of order ≥ 3,
   X(p)) is untouched; R(p) ≥ 1 does not follow.
4. **Fixed p (B6):** passes — every average is over a free variable (w in Prop 2.4, u in Prop 2.5) at fixed p; Burgess is
   applied character by character; no average over p, discriminant or level attached to p.

## 7. Verdict, proposed FRONTIER text, bottom line

**Verdict: strengthened** (for §7.4) — a genuine new unconditional lemma: M_gen(p) ≥ (2/(3π⁴) − o(1))log²p, effective. It
buys: the one-sided target "X(p) ≥ −(1 − ε)M_gen(p)" (H⁻ relative to the genus series) now has an unconditionally
log²-sized main term, so §7.4's "(L)" half of `SINGLE_P_COUNT`'s (L)/(U) split is closed; (U) is untouched. For §7.3:
**narrowed/clarified** — the genus part of the class-in-coset layer is written out as explicit L(1, ψ′)L(1, χ_pψ) products per
slice (Prop C, PROVED for u ≤ p^{3/5−ε}), and it is shown that these cross terms cannot make the genus layer small; what
remains in §7.3 is entirely the order-≥3 layer X(p) (B2).

*Proposed FRONTIER §7 text* (replace item 4; append to item 3):
> 4. **A polylog lower bound for M_gen(p) — CLOSED (z53, `Z53_GENUSLVAL.md` Thm U, PROVED, internal review).**
> M_gen(p) ≥ (2/(3π⁴) − o(1))(log p)² ≈ 0.0068 log²p for all primes p ≡ 1 (4), unconditionally and effectively (Burgess for
> cube-free conductors on `LOWERTAIL_DEEP_ASTRA` Thm 5.4's subfamily with sharp windows; the strip version gives 2/π⁴).
> The only primality step (ηχ_{−4up} non-principal) is the one that fails at odd squares. Open: the transfer to R(p), i.e.
> X(p) ≥ −(1 − ε)M_gen(p) (= H⁻ relative to the genus series, ES-(★) strength); a sharp constant (observed min 0.084).
>
> 3. (append) *(z53, `Z53_GENUSLVAL.md` Prop C.)* In each slice u ≤ p^{3/5−ε} the genus layer is an explicit signed sum
> Σ_η ε_η L(1, η)L(1, ηχ_{−4up})H_η plus the principal class-number term L(1, χ_{−4up})·log (PROVED; numerically exact to
> ≤ 0.5 % at 10⁵–10⁸ incl. (★)-zero primes). Cross terms can remove ~40 % of a slice (EVIDENCE) but cannot make
> M_gen = o(log²p) (Thm U). The non-genus (order ≥ 3) part is all that remains of this item.

**Bottom line.** The genus layer of (★) at a single prime is now under unconditional control: it is ≥ 0.0068·log²p for every
large p ≡ 1 (4) (effective, Burgess only), and slice by slice it is an explicit sum of class-number terms and products
L(1, ψ′)L(1, χ_pψ) with explicit signs and Euler factors, verified numerically to 10⁸. This closes FRONTIER §7.4 as posed
and shows that no configuration of quadratic characters can starve the expected count. It does not touch the order-≥3
characters, which carry the entire remaining difficulty (B2/B3): R(p) = M_gen(p) + X(p) and nothing here bounds X(p).
**ES remains OPEN.**

## 8. Review log

(pending)
