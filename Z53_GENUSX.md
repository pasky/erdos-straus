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

## 3. First lemma: (X-u) holds — the class of 2w mod 8u is free at density level (PROVED; full proof §4 TODO)

**Theorem X (statement).** Let (C1) γ < 1 − α₁, (C2*) β > 2α₁ + 1/4 + 6ε. Then T_u = O(p^{−δ}) with δ = δ(ε, r) > 0
(effective), i.e. M^cls_𝔉 = M_𝔉 + O(p^{−δ}). If moreover (C3) α₀ > (1 + α₁)/16 + 4ε (Thm U's condition at τ → 1/4) then
M^cls_𝔉(p) ≥ (c_X − o(1))(log p)², c_X := (8/π⁴)·max_{α₁}(3/4 − 3α₁)(15α₁ − 1)/16 = (8/π⁴)(5445/230400) ≈ 0.00194
(α₁ = 19/120). Input: Burgess for the Legendre symbol mod p only; no averaging over characters (all ψ mod u at once).
*Idea.* M^cls_𝔉 = 2Σ_u Σ_{w ≡ r_u (4u)} ρ_u(w): for each single class r mod 4u, Σ_{w∈(Y,X], w≡r} g(w)/w = (main term
independent of r) + O(p^{−δ}/u), via g = 1 ∗ χ_D ∗ h and the hyperbola split at b = B₀ := u·p^{1/4+2ε}: for b > B₀ the
progression b ≡ s (4u) turns χ_D(b) into a shifted Legendre symbol ((s + 4uk)/p) (Burgess in k); for b ≤ B₀ the a-sum in a
progression mod 4u has a class-independent main term and error ≪ cb/Y. Averaging over the genus coset then gives the claim.

## 4. Falsifier F (computation that could kill the route fast; TODO results)

Exact engine over 𝔉 at a single p (segmented factorisation of p + u, divisor enumeration): R_𝔉, G_𝔉 and its η-type
components (η = 1 [= E₁], BM [= −Σ(w″/p)/φ(u)], χ₋₄, rest), and M_𝔉 via the window closed form
Σ_u φ(u)⁻¹H_u(1)L(1, χ_{−4up})log(X/Y) (validated against direct summation at small p). Primes: the 14 (★)-zero primes,
FRONTIER §4 item-14 primes (193, 2521, 66529, 3361, 5101441), random p ≡ 1 (24) at 10⁸–10¹², near-squares m² + k; controls:
odd squares (R = G = M = 0 must hold exactly), composite non-squares. Kill criteria: (a) if G − M is of the same size as
R − M at large p, (X-w) is as hard as the whole problem (the genus layer of exact divisors is itself B2); (b) if
P(R_𝔉 = 0) decays slower than e^{−M} the family cannot carry a lower bound at attainable sizes.

## 5–8. TODO: proofs, results, screens, verdict, FRONTIER text, review log.
