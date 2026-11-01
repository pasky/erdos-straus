# Z53_GENUSX — the order-≥3 remainder X on the Theorem U subfamily

Status: z53 depth lane GENUSX (wave z53b follow-up to `Z53_GENUSLVAL.md`). Internal, internally reviewed only.
**ES is OPEN; nothing here proves or disproves ES, or (★), at any infinite set of primes.** Labels: PROVED / CONDITIONAL /
CERTIFIED / EVIDENCE / CONJECTURE / Assessment. Scripts `scripts/z53_genusx_*`, data `data/z53/genusx/`.

*(Checkpoint 1 skeleton — statements, decomposition, first lemma, falsifier plan. Sections marked TODO are filled later.)*

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
(2w ≡ −p (mod u) ⟺ 2w·2w″ ≡ −2p·2w″... directly: p + u = 2ww″ gives p ≡ 2ww″ (mod u), so 2w ≡ −p ⟺ w″ ≡ −1 (mod u); the mod-4
condition w ≡ −ww″ (mod 4) ⟺ w″ ≡ 3 (mod 4); and (−2pw/ℓ) = (−4w²w″/ℓ) = (−w″/ℓ).) So w″ = 4uC − 1 is the (★) level divisor
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

## 4. Falsifier F (computation that could kill the route fast; TODO results)

Exact engine over 𝔉 at a single p (segmented factorisation of p + u, divisor enumeration): R_𝔉, G_𝔉 and its η-type
components (η = 1 [= E₁], BM [= −Σ(w″/p)/φ(u)], χ₋₄, rest), and M_𝔉 via the window closed form
Σ_u φ(u)⁻¹H_u(1)L(1, χ_{−4up})log(X/Y) (validated against direct summation at small p). Primes: the 14 (★)-zero primes,
FRONTIER §4 item-14 primes (193, 2521, 66529, 3361, 5101441), random p ≡ 1 (24) at 10⁸–10¹², near-squares m² + k; controls:
odd squares (R = G = M = 0 must hold exactly), composite non-squares. Kill criteria: (a) if G − M is of the same size as
R − M at large p, (X-w) is as hard as the whole problem (the genus layer of exact divisors is itself B2); (b) if
P(R_𝔉 = 0) decays slower than e^{−M} the family cannot carry a lower bound at attainable sizes.

## 5–8. TODO: proofs, results, screens, verdict, FRONTIER text, review log.
