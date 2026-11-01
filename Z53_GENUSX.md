# Z53_GENUSX — the order-≥3 remainder X on the Theorem U subfamily

Status: z53 depth lane GENUSX (wave z53b follow-up to `Z53_GENUSLVAL.md`). Internal, internally reviewed only.
**ES is OPEN; nothing here proves or disproves ES, or (★), at any infinite set of primes.** Labels: PROVED / CONDITIONAL /
CERTIFIED / EVIDENCE / CONJECTURE / Assessment. Scripts `scripts/z53_genusx_*`, data `data/z53/genusx/`.


## 0. Summary

* **Target.** On the Theorem U family 𝔉 (pairs (u, 2w), (2w, u); u ≡ 1 (4) squarefree in (p^{α₀}, p^{α₁}], w odd squarefree in
  (p^β, p^γ]) write R_𝔉 = M_𝔉 + X_𝔉 with M_𝔉 the genus (order ≤ 2) part and X_𝔉 the order-≥ 3 part. X_𝔉 splits exactly as
  T_u + T_w + T_uw (non-real characters mod 8u only / mod w only / both; Lemma 1). (H⁻_𝔉) X_𝔉 ≥ −(1 − ε)M_𝔉 would give ES
  for all large p; it is **not** claimed.
* **Theorem X (PROVED, unconditional, effective; §3).** If γ < 1 − α₁ and β > 2α₁ + 1/4 + ε (α₁ < 1/5), then T_u = O(p^{−δ}log p):
  the full residue class of B mod 8u — all characters of order ≥ 3 — contributes only its genus value to the density main
  term, and M^cls_𝔉 (exact class, density divisibility) ≥ (0.00194 − o(1))log²p. Input: Burgess for the Legendre symbol mod p
  (p in the conductor, class by class). This answers the brief's question (2) positively *at density level*.
* **Structure of the rest (PROVED; §1, §4).** In level form (w″ = (p + u)/(2w) is the (★) divisor 4uC − 1): R − G is "class of
  w″ inside its genus coset mod 4u over exact divisors", G − M is "genus layer of exact divisors vs density". The BM
  component on exact divisors is exactly −(w″/p) (Lemma 2: T1 = one Legendre symbol). Each divisor lies on at most one shell
  point, so no u-average acts (Cor 4.2); the shell has no bilinear structure (Lemma 4.3); the exact layers are sums over the free
  variable w of a function of (p mod w, ⌊p/w⌋) (Lemma 4.1); the genus layer is itself a (★)-shaped tied event for x² + pt
  (Lemma 4.4); interval information on χ_p of any strength cannot control the BM shell sum (Prop 4.6, scoped).
* **Falsifier (EVIDENCE; §5).** Exact engine at 10⁸–10¹² (900 random primes, 120 near-squares, 14 (★)-zero primes, 150
  squares): G/M̂ = 0.98–1.02 on average; T_w carries ≈ 10 % of var(R − M), T_uw ≈ 90 % at swap-Poisson level; at the (★)-zero
  primes the failure sits in T_uw at 6 of 9 informative primes. Not killed; localised.
* **Verdict: narrowed** (one strengthening lemma, Theorem X; the remainder is B2 over exact divisors with its density layers
  removed). **ES remains OPEN.**

## 1. Setting and the precise statement attacked

p prime, p ≡ 1 (mod 4); χ_p = (·/p); D = D_u = −4up. Fix exponents 0 < α₀ < α₁, β < γ, put U_i = p^{α_i}, Y = p^β,
X = p^γ, with γ < 1 − α₁ (so 8uw ≤ p). The **Thm U family** 𝔉 = 𝔉(p) is the set of (u, w) with
  u ∈ 𝒰 := {u squarefree, u ≡ 1 (4), U₀ < u ≤ U₁},  w ∈ 𝒮_u ∩ (Y, X],  𝒮_u := {w odd squarefree, gcd(w, up) = 1};
each (u, w) gives the two ordered pairs (u, 2w), (2w, u) ∈ 𝒫(p), q = 8uw, a = −(u + 2w) (`Z53_GENUSLVAL` Lemma 2.3).

By CRT (gcd(8u, w) = 1) the event 1[p ≡ a (mod q)] factors as A_u(w)·B_u(w) with
  A_u(w) := 1[p ≡ a (mod 8u)] = 1[w ≡ w₀ (mod 4)]·1[2w ≡ −p (mod u)]   (w₀ := −(p + u)/2 mod 4),
  B_u(w) := 1[p ≡ a (mod w)] = 1[w | p + u].
Their order-≤2 (genus) projections — the real-character parts of the orthogonality expansions mod 8u and mod w — are
  A_u^gen(w) := (s(8u)/φ(8u))·1[pa ∈ □ mod 8u] = (2φ(u))⁻¹ Σ_{η∈𝔈_u} ε_η η(w),
  B_u^gen(w) := (s(w)/φ(w))·1[pa ∈ □ mod w] = ρ_u(w) := 2^{ω(w)}·1[χ_D(ℓ) = 1 ∀ℓ | w]/φ(w)
(𝔈_u, ε_η as in `Z53_GENUSLVAL` Lemma 2.3). Define the four family sums (factor 2 = both orders)
  R_𝔉 := 2Σ_𝔉 A·B (exact),  M_𝔉 := 2Σ_𝔉 A^gen·B^gen (genus = M_gen restricted to 𝔉),
  G_𝔉 := 2Σ_𝔉 A^gen·B (exact divisibility, genus class),  M^cls_𝔉 := 2Σ_𝔉 A·B^gen (exact class, density divisibility).

**Lemma 1 (PROVED; exact decomposition).** X_𝔉 := R_𝔉 − M_𝔉 is exactly the contribution of the characters of order ≥ 3
mod q to the orthogonality expansion of R(p) restricted to 𝔉, and
  X_𝔉 = T_u + T_w + T_uw,  T_u := M^cls_𝔉 − M_𝔉,  T_w := G_𝔉 − M_𝔉,  T_uw := R_𝔉 − G_𝔉 − M^cls_𝔉 + M_𝔉,
where T_u (resp. T_w) is the part with a non-real character mod 8u and a real one mod w (resp. real mod 8u, non-real mod w),
and T_uw the part with non-real characters on both sides.
*Proof.* χ mod q = χ₁χ₂ (χ₁ mod 8u, χ₂ mod w); χ is real iff both are. A − A^gen = φ(8u)⁻¹Σ_{χ₁ non-real}χ₁(p)χ̄₁(a),
B − B^gen likewise; expand AB = A^gB^g + (A − A^g)B^g + A^g(B − B^g) + (A − A^g)(B − B^g). ∎

**Divisor (level) form (PROVED, elementary).** For w | p + u put w′ := (p + u)/w and w″ := w′/2 (p + u ≡ 2 (mod 4) and w odd,
so w″ is odd). Then on exact divisors
  A_u(w) = 1[w″ ≡ −1 (mod 4u)],   A_u^gen(w) = (2^{ω(u)}/φ(u))·1[w″ ∈ −(ℤ/4u)^{×2}]  (i.e. w″ ≡ 3 (4) and (−w″/ℓ) = 1 ∀ℓ | u).
(p + u = 2ww″ gives p ≡ 2ww″ (mod u), so 2w ≡ −p (mod u) ⟺ w″ ≡ −1 (mod u) (w is a unit mod u); w₀ ≡ −ww″ (mod 4), so
w ≡ w₀ (mod 4) ⟺ w″ ≡ 3 (mod 4); and for ℓ | u, (−2pw/ℓ) = (−4w²w″/ℓ) = (−w″/ℓ).) So w″ = 4uC − 1 is the (★) level divisor
of p + u, and
  R_𝔉 = 2#{(u, w) ∈ 𝔉 : w | p+u, w″ ≡ −1 (4u)},  G_𝔉 = 2Σ_{u∈𝒰}(2^{ω(u)}/φ(u))#{w ∈ 𝒮_u∩(Y,X] : w | p+u, w″ ∈ −□ (4u)}:
**R − G is "class of the level divisor inside its genus coset mod 4u", G − M is "genus layer of exact divisors vs. density".**

**Lemma 2 (PROVED; the BM component on exact divisors is one Legendre symbol).** For w | p + u (u ∈ 𝒰, w ∈ 𝒮_u):
  ε_{1,0}η_{1,0}(w) = 1,  ε_{1,1}η_{1,1}(w) = −χ₋₄(w″),  ε_{u,0}η_{u,0}(w) = χ₋₄(w″)(w″/p),  ε_{u,1}η_{u,1}(w) = −(w″/p),
so the d ∈ {1, u} part of Σ_η ε_ηη(w) is (1 − χ₋₄(w″))(1 − (w″/p)) ≥ 0. *Proof.* ε_{d,j}η_{d,j}(w) = (−2p/d)(w/d)χ₋₄(w₀w)^j;
(pw/u) = (2w″/u) (p ≡ 2ww″ mod u); (w″/u) = (u/w″) (Jacobi reciprocity, u ≡ 1 (4)) = ((2ww″ − p)/w″) = (−p/w″) = χ₋₄(w″)(w″/p);
χ₋₄(w₀w) = χ₋₄(−ww″·w) = −χ₋₄(w″); (−2/u)(2/u) = (−1/u) = 1. ∎
*Reading.* At an odd square n = m² (gcd(w″, m) = 1) the BM component is −1 and cancels η = 1 pointwise (this is
`Z53_GENUSLVAL` §2.8 at the exact level); at a prime it is the Legendre symbol of the level divisor w″ mod p — the BM layer
of FRONTIER §2.2 / B5 ("every hit has (w″/p) = −1").

**The statement attacked (CONJECTURE-strength target, not claimed).** (H⁻_𝔉) X_𝔉(p) ≥ −(1 − ε)M_𝔉(p) for all p > p₀.
With Theorem U (M_𝔉 ≥ (c − o(1))log²p) this would give R(p) ≥ R_𝔉(p) > 0, i.e. (★), hence ES(p), for all large p — so it is
ES-(★)-strength on a subfamily. The lane's sub-statements, in order:
  (X-u) T_u = o(log²p) [the order-≥3 characters mod 8u at density level];
  (X-w) T_w = o(log²p) [genus layer of exact divisors];
  (X-uw) T_uw ≥ −(1 − ε)M_𝔉 [class inside genus coset over exact divisors: the B2 core].

## 2. Why this is not already closed

* Thm U (`Z53_GENUSLVAL`) controls only M_𝔉; its review (`data/z53/xreview/REVIEW_GENUSLVAL.md`) marks "any estimate for X(p)"
  not bankable. Prop 2.4 there treats real η only.
* Low-conductor universality (closed) concerns smooth blocks and remainders uniform over rough n; (X-u) is a *density*
  statement with p in the conductor, square-sensitive only through M_𝔉, and (X-w) is T1-sensitive by Lemma 2 (G(m²) = 0 while
  its η = 1 part is ≍ log²) — neither is a remainder bound uniform over n.
* The signed bounded-order inverse lemma (closed) and the bounded-order minorant (`SINGLE_P_COUNT` Lemma 5.2) concern
  positivity from finitely many characters; (X-u) is a full-character (all ψ mod u) density statement, not a minorant.

## 3. Theorem X: the order-≥3 characters mod 8u carry no density main term (PROVED)

**External input (Bu₁): Burgess, prime modulus.** For every r ≥ 1 and ε > 0 there is an effective C = C(r, ε) such that for
every prime p, every non-principal χ mod p and all M ≥ 0, N ≥ 1: |Σ_{M<n≤M+N} χ(n)| ≤ C N^{1−1/r} p^{(r+1)/(4r²)+ε}.
(Burgess, Proc. LMS (3) 12 (1962) 179–192 and 13 (1963) 524–536; Iwaniec–Kowalski Thm 12.6; the cube-free version quoted
in `Z53_GENUSLVAL` §2.1 from arXiv:2511.17778 contains it.) Put τ_r := (r + 1)/(4r) + rε (so N ≥ p^{τ_r + ε} gives a saving
N^{−ε/r}·… below; τ_r → 1/4).

**Theorem X.** Fix r ≥ 1, ε ∈ (0, 1/100) and exponents with
  (C1) γ < 1 − α₁,  (C2*) β > 2α₁ + τ_r + 4ε,  (C4) α₁ < 1/5.
There is δ = δ(r, ε, α₁, β) > 0 such that, uniformly in u ∈ 𝒰 and in the unit class s mod 4u,
  Σ_{w ∈ 𝒮_u ∩ (Y, X], w ≡ s (4u)} ρ_u(w) = 𝔐_u + O(p^{−δ}/u),   𝔐_u independent of s.        (X.1)
Consequently **T_u = M^cls_𝔉 − M_𝔉 = O(p^{−δ} log p)**: on 𝔉 the full residue class of B = 2w mod 8u — all characters mod 8u,
of every order — contributes exactly the genus value to the density main term. If in addition (C3) α₀ > τ²(1 + α₁) + 3ε
(Thm U's condition, τ the cube-free Burgess exponent), then M^cls_𝔉(p) ≥ M_𝔉(p) − o(1) ≥ (c − o(1))(log p)² with
c = (8/π⁴)(γ − β)(α₁ − α₀); optimising (r → ∞, ε → 0; γ ↑ 1 − α₁, β ↓ 2α₁ + 1/4, α₀ ↓ (1 + α₁)/16):
  (γ − β)(α₁ − α₀) → (3/4 − 3α₁)(15α₁ − 1)/16, maximal at α₁ = 19/120 with value 5445/230400, so
  **M^cls_𝔉(p) ≥ (c_X − ε′)(log p)²,  c_X = (8/π⁴)·5445/230400 ≈ 0.001941**, for p ≥ p₀(ε′), effectively.

*Proof.* Notation as in `Z53_GENUSLVAL` Prop 2.4(1): ρ_u(w) = g(w)/w, g = 1 ∗ χ_D ∗ h with h multiplicative, h(ℓ) = −1
(ℓ | 2up), and for ℓ ∤ 2up h(ℓ) = 2/(ℓ − 1), h(ℓ²) = −(3ℓ + 1)/(ℓ − 1), h(ℓ³) = 2ℓ/(ℓ − 1) (χ_D(ℓ) = 1), h(ℓ²) = −1
(χ_D(ℓ) = −1), else 0; hence for 0 ≤ θ′ < 1/2, Σ_c |h(c)| c^{θ′−1} ≤ p^{o(1)} (the factor 2^{ω(2up)} and a convergent
Euler product). Fix θ′ := 1/2 − ε. Write q := 4u, s a unit mod q. Since w = abc ≡ s forces gcd(abc, q) = 1,
  Σ_{w ≡ s} ρ_u(w) = Σ_{c: (c,q)=1} (h(c)/c)·[Φ_{s c̄}(X/c) − Φ_{s c̄}(Y/c)],  Φ_t(y) := Σ_{ab ≤ y, ab ≡ t (q)} χ_D(b)/(ab).

(i) *Large c.* For T₁ ≥ 1, Σ_{T₁<n≤T₂, n≡t (q)} τ(n)/n ≤ p^{o(1)}(3/T₁ + q⁻¹ log(T₂/T₁)) for T₂ ≤ p (τ(n) ≤ p^{o(1)}).
For C₀ := p^ε < c ≤ Y/q the bracket is ≤ p^{o(1)}/u, and Σ_{c > C₀}|h(c)|/c ≤ C₀^{−θ′}p^{o(1)}: contribution ≤ p^{−εθ′+o(1)}/u.
For c > Y/q the bracket is ≤ (1 + log X)² and Σ_{c > Y/q}|h(c)|/c ≤ (Y/q)^{−θ′}p^{o(1)} = p^{−θ′(β − α₁) + o(1)}; by (C2*),
β − α₁ > α₁ + 1/4 + 4ε, and (1/2 − ε)(α₁ + 1/4 + 4ε) ≥ α₁ + ε/2 because α₁ < 1/5 (C4) and ε < 1/100 (at α₁ = 1/5,
ε = 1/100: 0.2401 ≥ 0.205), so θ′(β − α₁) ≥ α₁ + ε/2: contribution ≤ p^{−ε/2+o(1)}/u.

(ii) *Small c (c ≤ C₀): hyperbola split at B₀ := q·p^{τ_r+ε}.* For every y ≥ 1 (exact identity, splitting by b ≤ B₀ or b > B₀):
  Φ_t(y) = Σ_{b ≤ B₀} (χ_D(b)/b)·α_{t b̄}(y/b) + Σ_{a ≤ y/B₀} (1/a)·[β_{t ā}(y/a) − β_{t ā}(B₀)],
α_v(T) := Σ_{a ≤ T, a ≡ v (q)} 1/a, β_v(T) := Σ_{b ≤ T, b ≡ v (q)} χ_D(b)/b (χ_D(b) ≠ 0 forces gcd(b, q) = 1, and then
gcd(a, q) = 1 is forced by ab ≡ t).
– *Second part.* For a unit v mod q and b ≡ v (q), b odd and prime to u, χ_D(b) = χ₋₄(b)(b/u)(b/p) = χ₋₄(v)(v/u)·(b/p)
(Jacobi reciprocity with u ≡ p ≡ 1 (4), as in `Z53_GENUSLVAL` Prop 2.4(2)). With b = v₀ + qk (1 ≤ v₀ ≤ q),
(b/p) = (q/p)·((k + v₀q̄)/p) (q̄ the inverse mod p), a shifted Legendre symbol in k. By (Bu₁) its sums over any k-range of
length K are ≤ C K^{1−1/r}p^{(r+1)/(4r²)+ε}; Abel summation against the decreasing weight 1/(v₀ + qk) from k₀ ≥ B₀/q − 1 gives
  |β_v(T) − β_v(B₀)| ≤ (r + 2)C·p^{(r+1)/(4r²)+ε}·k₀^{−1/r}/q ≤ 2(r + 2)C·p^{−ε/r}/q   (k₀^{1/r} ≥ ½p^{(r+1)/(4r²)+ε+ε/r}),
(boundary term ≤ CP k₁^{−1/r}/q, and Σ_k k^{1−1/r}(f(k) − f(k+1)) ≤ q⁻¹Σ_{k>k₀}k^{−1−1/r} ≤ (r + 1)k₀^{−1/r}/q), so the second part is ≤ 2(1 + log p)(r + 2)C p^{−ε/r}/q for each y — an error O(p^{−ε/r+o(1)}/u), for both y = X/c, Y/c.
– *First part (window difference).* For T₁ ≥ 1, |Σ_{T₁<a≤T₂, a≡v (q)} 1/a − q⁻¹ log(T₂/T₁)| ≤ 3/T₁. With T₁ = Y/(cb) ≥
Y/(C₀B₀) ≥ 1 and T₂/T₁ = X/Y:
  Σ_{b≤B₀}(χ_D(b)/b)[α_{tb̄}(X/(cb)) − α_{tb̄}(Y/(cb))] = q⁻¹ log(X/Y)·Λ(B₀) + O(3cB₀/Y),  Λ(B₀) := Σ_{b ≤ B₀} χ_D(b)/b,
and 3cB₀/Y ≤ 12·u·p^{2ε+τ_r−β} ≤ p^{−ε}/u by (C2*) (u ≤ p^{α₁}). **The main term does not depend on t.**
Summing over c ≤ C₀: 𝔐_u := q⁻¹log(X/Y)Λ(B₀)Σ_{c ≤ C₀, (c,q)=1} h(c)/c, with total error p^{o(1)}·O(p^{−ε/r+o(1)}/u)
(Σ_c|h(c)|/c ≤ p^{o(1)}). Together with (i) this proves (X.1) with any δ < min(ε/r, εθ′, ε/2) for p large.

(iii) *T_u.* On 𝒮_u, A_u(w) = 1[w ≡ s_u (q)] for the single unit class s_u (w ≡ w₀ (4), w ≡ −p·2̄ (u)), and
A_u^gen(w) = |𝒞|⁻¹Σ_{s∈𝒞}1[w ≡ s (q)] with 𝒞 = s_u·(ℤ/q)^{×2} (|𝒞| = φ(u)/2^{ω(u)}; indeed (ii)–(iii) of
`Z53_GENUSLVAL` Lemma 2.3 say w ≡ w₀ (4) and (w/ℓ) = (−2p/ℓ) = (s_u/ℓ) for ℓ | u). By (X.1),
Σ_w (A_u − A_u^gen)(w)ρ_u(w) = [𝔐_u + O(p^{−δ}/u)] − |𝒞|⁻¹Σ_{s∈𝒞}[𝔐_u + O(p^{−δ}/u)] = O(p^{−δ}/u), and
|T_u| ≤ 2Σ_{u ≤ U₁} O(p^{−δ}/u) = O(p^{−δ}log p). (C2*) implies Thm U's (C2) (τ(1 + α₁) ≤ τ + 2α₁), so with (C3)
Thm U applies to the same window and gives the lower bound; the optimisation is elementary. ∎

*Remarks.* (1) Only the Legendre symbol mod p is ever summed (p in the conductor, exactly as in Thm U); no average over
characters mod u is taken, so the 2φ(u) characters per u cost nothing. (2) Theorem X re-proves the "window kills the
constants" mechanism class by class: (X.1) is equidistribution of the divisibility density ρ_u in *every* residue class mod
4u, at relative precision p^{−δ}, for moduli up to p^{α₁}, α₁ < (β − 1/4)/2. (3) T1: at n = m², M^cls_𝔉(m²) = 0 exactly
(A ≤ |𝒞|·A^gen pointwise and M_𝔉(m²) = 0 termwise) — nothing to audit beyond Thm U §2.8.
(4) **Reading.** The order-≥3 remainder on the family is X_𝔉 = T_w + T_uw + O(p^{−δ}log p), and
R_𝔉 − G_𝔉 = T_u + T_uw = T_uw + o(1): every non-real character mod 8u enters X only *over exact divisors* of p + u.

## 4. The exact layers T_w, T_uw: structure theorems and scoped no-gos (PROVED)

Standing assumptions: (C1) and Y ≥ U₁ (true for every window above: β > α₁). The **shell** is 𝔖 := {(u, w) ∈ 𝔉 : w | p + u}
(support of B); for (u, w) ∈ 𝔖 write w′ = (p + u)/w = 2w″.

**Lemma 4.1 (residual-map form).** The projections (u, w) ↦ w and (u, w) ↦ w″ are injective on 𝔖. For w ∈ (Y, X] let r_w
be the least non-negative residue of −p mod w. Then (u, w) ∈ 𝔖 ⟺ u = r_w ∈ 𝒰 and w ∈ 𝒮_{r_w}; on 𝔖, w′ = ⌈p/w⌉; hence
  R_𝔉 = 2#{w ∈ (Y, X] : r_w ∈ 𝒰, w ∈ 𝒮_{r_w}, ⌈p/w⌉ ≡ −2 (mod 8r_w)},
  G_𝔉 = Σ_{w ∈ (Y,X]: r_w ∈ 𝒰, w ∈ 𝒮_{r_w}} (2·2^{ω(r_w)}/φ(r_w))·1[⌈p/w⌉/2 ∈ −(ℤ/4r_w)^{×2}].
*Proof.* w | p + u₁, p + u₂ ⇒ w | u₁ − u₂, |u₁ − u₂| < U₁ ≤ Y < w ⇒ u₁ = u₂; as 0 < u ≤ U₁ < w and u ≡ −p (w), u = r_w and
w′ = (p + r_w)/w = ⌈p/w⌉. For w″: w″ | (p + u_i)/2 ⇒ w″ | (u₁ − u₂)/2, while w″ = (p + u)/(2w) > p/(2X) ≥ 4U₁. The class
condition w″ ≡ −1 (4u) is w′ ≡ −2 (8u); the genus condition is the level form of §1. ∎
*Reading.* The exact layers are sums over the **free** variable w (not attached to p) of a function of the pair
(p mod w, ⌊p/w⌋) — exactly the "x ↦ −p mod x" structure of FRONTIER §7.1. The Diophantine content is that p/w lies within
U₁/w of an integer from below *and* that integer (+2) is divisible by 8·(its distance).

**Corollary 4.2 (no u-average reaches the exact layers).** For every fixed w (resp. w″) at most one u ∈ 𝒰 has B_u(w) = 1.
Thm U and Theorem X average over u (with p in the conductor of a quadratic character of u) and over w at fixed u (against
the *density* ρ_u). In B − B^gen the u-average of 1[w | p + u] at fixed w has ≤ 1 term, so neither mechanism acts on T_w or
T_uw. The variable w is free, but its summand depends on p through p mod w (Lemma 4.1).

**Lemma 4.3 (the shell carries no bilinear structure).** For any complex b_{w″},
Σ_w |Σ_{w″} b_{w″}1[(·, w, w″) ∈ 𝔖]|² = Σ_{𝔖}|b_{w″}|² (each w has at most one partner w″, Lemma 4.1). Hence Cauchy–Schwarz,
Type II bilinear and one-variable large-sieve arguments over the shell have *no off-diagonal terms* and return exactly the
trivial bound. (Shell version of the closed "Cauchy–Schwarz in the function variable"; FRONTIER §7.1, z52d.)

**Lemma 4.4 (the genus layer is itself a (★)-shaped tied event; PROVED identity).** For (u, w) ∈ 𝔖, gcd(w″, u) = 1 and
2^{ω(u)}1[−w″ ∈ □ (mod u)] = #{x mod u : x² ≡ −w″ (u)}; therefore
  G_𝔉 = Σ_{(u,w) ∈ 𝔖, w″ ≡ 3 (4)} (2/φ(u))·#{(x, t) : 0 ≤ x < u, t ≥ 1, **x² + pt = w″·(2wt − 1)**}.
*Proof.* x² ≡ −w″ (u) ⟺ x² + w″ = ut (t ≥ 1) and with u = 2ww″ − p this is x² + pt = w″(2wt − 1). ∎
*Reading.* "The level divisor w″ lies in the genus of −1 mod 4u" ⟺ "for some x < u, the integer x² + pt has the divisor w″
with cofactor ≡ −1 (mod 2t)": a tied-modulus divisor event of the (★) shape, one quadratic level down (cf.
`SINGLE_P_COUNT` Prop 2.2(c): M_gen > 0 ⟺ (★) at n·y²). So (X-w) is not softer *in kind* than B2.

**Lemma 4.5 (= Lemma 2, T1 on the exact layer).** On 𝔖 the BM component of the genus expansion is −(w″/p) =
−(2u/p)(w/p); at odd squares it is −1 and cancels the η = 1 component E₁ pointwise; at primes the BM part of T_w is the shell
sum −Σ_{𝔖} (w″/p)/φ(u). Any proof of (X-w) must therefore prove cancellation of the Legendre symbol (·/p) along the
w″-projection of the shell (at squares this sum equals −E₁ ≍ log²).

**Proposition 4.6 (interval information on χ_p cannot do it; scoped no-go).** Let N ≥ √p and 𝒲 := {w″ : (u, w) ∈ 𝔖,
N < w″ ≤ 2N} (w″ ≥ √p means w ≤ (p + U₁)/(2√p), so the box meets 𝔖 only if β < 1/2: true for Thm U's optimal and the standard windows,
false for Theorem X's windows, β > 1/2). Then
(a) |𝒲 ∩ I| ≤ p|I|/(2N²) + 2 for every interval I ⊂ (N, 2N];
(b) there is f : ℤ ∩ (N, 2N] → {±1} with f ≡ −1 on 𝒲 and |Σ_{n∈I} f(n)| ≤ 5 for **every** interval I.
So every hypothesis on χ_p that only constrains its sums over intervals (or smoothly weighted sums: partial summation), of
any strength down to O(1), is satisfied by f, while f makes the BM shell sum equal to its square value −Σ_{𝔖∩box}1/φ(u).
*Proof.* (a) w″ ∈ (N₁, N₁ + L] and 2ww″ ∈ (p, p + U₁] give w ∈ (p/(2(N₁ + L)), (p + U₁)/(2N₁)], of length ≤ pL/(2N²) +
U₁/(2N) ≤ pL/(2N²) + 1/8 (N > p/(2X) ≥ 4U₁); injectivity (Lemma 4.1) bounds |𝒲 ∩ I| by the number of integers there.
(b) Greedy: f(n) := −1 on 𝒲; off 𝒲, f(n) := −1 if S(n − 1) ≥ 0 and +1 if S(n − 1) < 0, S(n) := Σ_{N<k≤n} f(k), S(N) = 0.
Then S ≤ 0 throughout. If S(n) < 0, let a < n be the last index with S(a) = 0; on (a + 1, n] every k ∉ 𝒲 has f(k) = +1, so
S(n) ≥ −1 + |(a+1, n] \ 𝒲| − |(a+1, n] ∩ 𝒲| ≥ −1 + L − 2(pL/(2N²) + 2) ≥ −5 (L := n − a − 1, p/N² ≤ 1). So S ∈ [−5, 0] and
interval sums S(b) − S(a) lie in [−5, 5]. ∎
*Scope.* f is not multiplicative and has no prescribed sums on progressions mod q > 2; arguments using the complete
multiplicativity of χ_p jointly with the shell's arithmetic (as Thm U/Theorem X do for the *density*) are not covered.
That is the escape hatch, and §5 shows what it has to beat.

**Remark 4.7 (cubic/quartic characters, cubic large sieve; Assessment).** For χ₂ mod w of order k ∈ {3, 4, 6}, k-th power
reciprocity in ℚ(ζ_k) rewrites χ₂(−p·ū) as a Hecke character with p (split, p ≡ 1 (24)) in its conductor, evaluated at
the prime ideals above w — "p in the conductor" exactly as in Thm U. So each *bounded-order density layer* on the w-side
(B^{(k)} := projection of B onto χ₂ with χ₂^k = 1) is of Thm U type and should be o(1) on windows by Hecke-L/Burgess bounds
over ℚ(ζ_k) (not written out). This does not touch T_w or T_uw: B − B^gen is the sum over *all* χ₂ mod w (orders up to λ(w)),
and by Lemma 4.1 its support is the shell, where no average acts. Heath-Brown's cubic large sieve [HB00, Thm 2; restated as
(1.11) in Dunn–Radziwiłł, arXiv:2109.07463: Σ_{N(a)≤A, a≡1(3)} μ²(a)|Σ_{N(b)≤B, b≡1(3)} β_b (b/a)₃|² ≪_ε (AB)^ε(A + B +
(AB)^{2/3})Σ|β_b|²] is a mean square over moduli: on the shell (moduli a ↔ w, points b ↔ u², A ≍ X, B ≍ U₁⁴, with χ₂(p)
carried as a coefficient) Cauchy–Schwarz against it can only return (number of (w, χ₂) pairs)^{1/2}·(A + B)^{1/2}-type bounds,
i.e. the square-root barrier (B6), since the shell sum of interest has size ≍ log²p while the coefficient vectors have ℓ²
mass ≍ #shell. The u-side ladder of §5 (EVIDENCE) shows the same thing numerically: each bounded order explains a growing but
partial share; no bounded order carries the remainder.

## 5. Falsifier F: sizes of the three layers at 10⁸–10¹² (EVIDENCE; CERTIFIED identities)

**Engine.** `scripts/z53_genusx_engine.c` (compile `gcc -O2 -o /tmp/z53gx2 scripts/z53_genusx_engine.c -lm`): segmented
factorisation of p + u, u ∈ (U₀, U₁]; enumerates the shell 𝔖 and computes R_𝔉, G_𝔉, the η-type components of G
(E₁: η = 1; C4: χ₋₄; CU0: (·/u); CBM: χ₋₄(·/u); REST: 1 < d < u), the u-side order ladder G^{(K)} (projection of the exact class
A onto the characters χ mod 8u with χ^K = 1: weight ∏_{ℓ|u}gcd(K, ℓ−1)/φ(u), condition w″ ≡ 3 (4), −w″ ∈ (ℤ/u)^{×K};
K = 2 is G, K → ∞ is R), and in mode D the density sums M_𝔉 and M^cls_𝔉 by direct summation over w. Driver
`scripts/z53_genusx_run.py` adds M̂ := Σ_u H_u(1)L(1, χ_{−4up})log(X/Y)/φ(u) (Thm U window closed form; class numbers by PARI
`quadclassunit`); `scripts/z53_genusx_stats.py`, `scripts/z53_genusx_ladder.py` summarise. Standard window:
U₀ = ⌊p^{1/12}⌋, U₁ = ⌊p^{1/3}/2⌋, Y = ⌊p^{1/3}⌋, X = ⌊p^{2/3}/4⌋ (8U₁X ≤ p). Commands:
`uv run --with cypari2 python scripts/z53_genusx_run.py data/z53/genusx/random.tsv R1e12 @data/z53/genusx/primes_1e12.txt`
(likewise R1e8…R1e11 → `random_small.tsv`/`random.tsv`, NS1e10/NS1e12 → `nearsq.tsv`, STARZERO/ITEM14 → `hard.tsv`,
SQUARE/COMPOSITE → `controls.tsv`; `DIRECT=1` → `validate_direct*.tsv`); then
`uv run --with numpy python scripts/z53_genusx_stats.py data/z53/genusx/{random_small,random,nearsq}.tsv` (→ `stats.txt`) and
`ENG=/tmp/z53gx2 uv run --with numpy python scripts/z53_genusx_ladder.py data/z53/genusx/ladder_large.tsv data/z53/genusx/random.tsv`.
Samples: random primes p ≡ 1 (24) in [10^k, 2·10^k] (seed 5300): 200 each at k = 8, 9, 10, 150 each at k = 11, 12;
60 near-squares p = m² + k (k ∈ {4, 16, 36, 64, 100}, p ≡ 1 (4)) near 10¹⁰ and 10¹².

**Identity checks (CERTIFIED on all runs).** (1) Lemma 2's four closed forms and the full expansion Σ_{d|u,j}ε_{d,j}η_{d,j}(w)
= 2^{ω(u)+1}·1[genus] (ω(u) ≤ 8) on every shell point of every run: 0 mismatches (≈ 1.4·10⁶ shell points in the saved TSVs, incl. 1.3·10⁵ at squares). (2) Class ⊂ genus on
every hit. (3) R_𝔉 equals a brute-force count over all (u, w) at p = 100000049 (`scripts/z53_genusx_bruteR.py`: 2 = 2).
(4) **T1 controls:** 150 odd squares (m² for odd m ∈ [10001, 10199] and [1000001, 1000099]) give R = G = 0 exactly, with
E₁ = −CBM, C4 = −CU0, REST = 0 (Lemma 2 at squares; 1.3·10⁵ shell points); M = M^cls = 0 checked by direct summation at
10001² (mode D). 50 composite non-squares near 10¹⁰ all give G > 0 (no T1).

**Validation of M̂ and of Theorem X at finite size** (`validate_direct.tsv`; exact M_𝔉 and M^cls_𝔉 by direct summation):

| p | R | G | M̂ | M (direct) | M^cls (direct) |
|---|---|---|---|---|---|
| 5212561 (★)-zero | 0 | 1.158 | 1.229 | 1.293 | 1.132 |
| 8813281 (★)-zero | 0 | 1.904 | 1.539 | 1.633 | 1.601 |
| 10000169 | 0 | 0.330 | 1.181 | 1.174 | 1.164 |
| 99999989 | 0 | 1.293 | 1.681 | 1.659 | 1.628 |
| 100000049 | 2 | 3.449 | 1.726 | 1.718 | 1.611 |
| 1000000021 | 2 | 2.376 | 2.246 | 2.268 | 2.313 |

M̂ is within 6 % of M (1 % at 10⁹); M^cls/M ∈ [0.875, 1.02] — consistent with Theorem X (T_u = o(1)) at these sizes.
(1000000081 in the same file is composite; ignore.) At 10¹⁰ (`validate_direct_1e10.tsv`, three primes): M̂/M = 0.997,
0.999, 0.995 and M^cls/M = 1.011, 1.009, 1.009.

**Main table** (`stats.txt`; per scale: mean over primes; shares of var(R − M̂) = var(T_w) + var(R − G) + 2cov):

| sample | N | mean M̂/log²p | mean R/M̂ | mean G/M̂ | sd(R−M̂)/M̂ | sd(G−M̂)/M̂ | share T_w = G−M̂ | share R−G | var(R−G)/(2·mean G) | P(R=0) | mean e^{−M̂/2} |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 10⁸ | 200 | 0.0064 | 0.93 | 0.99 | 0.94 | 0.50 | 0.28 | 0.77 | 0.77 | 0.350 | 0.325 |
| 10⁹ | 200 | 0.0051 | 1.08 | 0.98 | 0.97 | 0.29 | 0.09 | 0.93 | 1.00 | 0.275 | 0.320 |
| 10¹⁰ | 200 | 0.0057 | 0.93 | 1.02 | 0.86 | 0.28 | 0.10 | 0.90 | 1.02 | 0.275 | 0.212 |
| 10¹¹ | 150 | 0.0061 | 1.01 | 1.01 | 0.69 | 0.22 | 0.10 | 0.93 | 0.88 | 0.153 | 0.133 |
| 10¹² | 150 | 0.0065 | 0.91 | 1.00 | 0.60 | 0.19 | 0.10 | 0.88 | 0.81 | 0.120 | 0.079 |
| near-sq 10¹⁰ | 60 | 0.0055 | 1.02 | 0.94 | 0.70 | 0.22 | 0.10 | 0.93 | 0.68 | 0.167 | 0.233 |
| near-sq 10¹² | 60 | 0.0064 | 0.93 | 0.93 | 0.59 | 0.17 | 0.08 | 0.96 | 0.87 | 0.100 | 0.086 |

Components of G (mean/M̂ at 10¹²): E₁ 1.014, C4 0.000, CU0 −0.005, CBM −0.001, REST −0.009; corr(E₁ − M̂, G − M̂) = 0.85
(0.71–0.85 at all scales): the T_w fluctuation is mostly the plain divisor count E₁ = Σ_u φ(u)⁻¹#{w | p + u in window}.
Near-squares: C4 mean −0.056·M̂ (10¹²), −0.070·M̂ (10¹⁰) against ≈ 0 for random primes — the χ₋₄ component of the exact genus
layer is depressed near squares (the T1 deformation of B5), G/M̂ ≈ 0.93.

**u-side order ladder** (`ladder_*`; share of var(R − M̂) explained by G^{(K)} − M̂, K = 2, 4, 6, 12, 120):
10⁹: 0.09, 0.14, 0.20, 0.31, 0.53; 10¹⁰: 0.10, 0.16, 0.15, 0.27, 0.38; 10¹¹: 0.10, 0.13, 0.20, 0.24, 0.39;
10¹²: 0.10, 0.13, 0.16, 0.22, 0.35 (`ladder_small_summary.txt`, `ladder_large_summary.txt`); mean G^{(K)}/M̂ ∈ [0.948, 1.060]
for the random primes at 10⁹–10¹² (near-squares 0.90–0.98). The explained share grows steadily with
the size of the K-th-power quotient; no bounded order carries the remainder (K = 120 already equals R on every u whose prime
factors all have ℓ − 1 | 120).

**The (★)-zero primes** (`hard.tsv`; M̂ > 0.5): G/M̂ = 0, 0 (83449, 102001: one shell point each), 1.53 (329617), 1.35
(712321), 0.84 (1134241), 1.42 (1724209), 0.10 (1726201), 0.94 (5212561), 1.24 (8813281); R = 0 at all of them by
definition. At 6 of the 9 the exact genus layer is normal or high: there the failure is entirely the class-within-genus
layer (T_uw = −G); at 83449, 102001, 1726201 the window is nearly empty already at genus level.

**Reading (EVIDENCE).** (a) The route is not killed by F: the genus layer of exact divisors tracks M (mean G/M̂ = 0.98–1.02
at every scale ≥ 10⁹) and T_w carries a stable ≈ 10 % of var(R − M) at 10⁹–10¹²; ≈ 90 % sits in R − G = T_uw + o(1), whose
variance is ≈ 0.8–1.0 × the swap-Poisson value 2·G — the class of the level divisor inside its genus coset behaves like a
uniform choice. (b) T_w at attainable sizes is dominated by the smallest u in the window (weights 1/φ(u), u ≥ p^{1/12} ≈ 10
at 10¹²; Assessment from the E₁ correlation). (c) P(R_𝔉 = 0) is 1.0–1.5 × e^{−M̂/2} (fatter at 10¹², 0.120 vs 0.079): the
same mild zero excess as for the full count (FRONTIER §2.4).

## 6. The four FRONTIER §4 hard screens

For Theorem X (as an ES ingredient) and for the localisation X_𝔉 = T_w + T_uw + o(1):
1. **T1 (squares): passes / consistent.** Theorem X is a statement about M^cls, which vanishes identically at odd squares
   (§3 Remark 3); the square-sensitive step remains Thm U's (§2.8 there). At the exact level T1 is located precisely: the BM
   component −(w″/p) (Lemma 2/4.5) is −1 at squares and cancels E₁ pointwise; CERTIFIED on 150 squares.
2. **8/131: not applicable** as a solution statement (density and structure statements only).
3. **Tied modulus (B2): fails — as it must; this is where the lane ends.** T_uw is the class of the level divisor w″ inside
   its genus coset mod 4u over the exact divisors of p + u (B2 verbatim), and T_w is itself a (★)-shaped tied event for
   x² + pt (Lemma 4.4). Neither is bounded.
4. **Fixed p (B6): passes** for Theorem X (averages only over w at fixed u and over the residue classes; p fixed). The
   no-go statements (Cor 4.2, Lemma 4.3, Prop 4.6) are fixed-p statements.

## 7. Verdict, proposed FRONTIER §7 text, bottom line

**Verdict: narrowed** (with one strengthening lemma).
* *Strengthened:* **Theorem X (PROVED, unconditional, effective):** on the Thm U family with α₁ < (β − 1/4)/2, every
  character mod 8u (all orders, all classes) contributes exactly its genus value to the density main term: T_u = O(p^{−δ}log p)
  and M^cls_𝔉 ≥ (0.00194 − o(1))log²p. This is the "p divides the conductor" trick acting on order-≥3 characters — it works,
  class by class, because the twist χ_{−4up} turns each progression b ≡ v (4u) into a shifted Legendre symbol mod p.
  What it buys: the order-≥3 remainder on the family is X_𝔉 = T_w + T_uw + O(p^{−δ}log p); every non-real character mod 8u
  reaches X only through exact divisors of p + u.
* *Narrowed (PROVED, scoped):* on the remaining layers no average over u acts (Cor 4.2: each w, w″ lies on ≤ 1 shell point);
  the shell has no bilinear structure (Lemma 4.3); the exact layers are sums over the free variable w of a function of
  (p mod w, ⌊p/w⌋) (Lemma 4.1); the genus layer of exact divisors is a (★)-shaped tied event for x² + pt (Lemma 4.4); its T1
  content is one Legendre symbol (w″/p) on the shell, and interval information on χ_p of any strength cannot control it
  (Prop 4.6; multiplicativity + shell arithmetic not covered).
* *EVIDENCE:* T_w ≈ 10 % of var(R − M), T_uw ≈ 90 % at Poisson level, 10⁹–10¹²; at the (★)-zero primes the failure is in
  T_uw at 6 of 9 informative primes.
* What is still missing for (H⁻_𝔉): a fixed-p lower bound for the class-within-genus layer over exact divisors (B2), plus
  (X-w), which needs cancellation of real characters (·/p), (·/d), d | u, along the shell — the 2-cycle-type structure of
  FRONTIER §7.1.

*Proposed FRONTIER §7 text* (append to item 3, "Beyond the BM layer"; and to item 4):
> 3. *(z53b, `Z53_GENUSX.md`, internal review.)* On the Thm U family (u ≡ 1 (4) squarefree in (p^{α₀}, p^{α₁}], B = 2w,
> w ∈ (p^β, p^γ], α₁ < (β − 1/4)/2) the *full* residue class of B mod 8u — all characters of order ≥ 3 — is free at density
> level: T_u = O(p^{−δ}), M^cls ≥ (0.0019 − o(1))log²p (Theorem X, PROVED, Burgess mod p only). So the order-≥3 remainder
> enters only over exact divisors: X_𝔉 = T_w (genus layer of exact divisors) + T_uw (class of the level divisor inside its genus
> coset) + o(1). Scoped no-gos (PROVED): no u-average acts on these (each divisor lies on ≤ 1 shell point), the shell has no
> bilinear structure, the genus layer of exact divisors is itself a (★)-shaped tied event for x² + pt, and its T1 content is
> the single Legendre symbol (w″/p) of the level divisor, which interval information on χ_p cannot control. EVIDENCE
> (10⁸–10¹²): T_uw carries ≈ 90 % of var(R − M) at swap-Poisson level, T_w ≈ 10 %.
>
> 4. (append) The transfer X(p) ≥ −(1 − ε)M_gen(p) is open; on the Thm U family its order-≥3-mod-8u density part is closed
> (Theorem X) and what remains is B2 over exact divisors (`Z53_GENUSX.md`).

**Bottom line.** The "p in the conductor" mechanism of Theorem U does act on order-≥3 characters — but only at the density
level: on the Thm U family every character mod 8u, of every order, is equidistributed against the divisibility density
(Theorem X, unconditional, Burgess mod p). Everything that remains of X on the family lives over *exact* divisors of p + u,
where each divisor occurs for at most one shift u, no bilinear structure exists, and even the genus layer is again a
tied-modulus event (for x² + pt) whose square-sensitive part is the Legendre symbol of the level divisor. Numerically the
genus layer of exact divisors is well behaved (≈ 10 % of the variance) and the class-within-genus layer is Poisson-like
(≈ 90 %). The order-≥3 remainder on the subfamily is therefore exactly B2 over exact divisors, now with its density
layers removed. **ES remains OPEN.**

## 8. Review log

TODO (internal hostile review; cross-model review to follow).
