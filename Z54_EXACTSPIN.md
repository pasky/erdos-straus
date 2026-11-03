# Z54_EXACTSPIN — spins, Kummer and Rédei-type symbols over the free variable w in the exact class layer T_uw

Status: z54 depth lane EXACTSPIN (gap 2, algebraic angle). Internal; internally hostile-reviewed (review log §9);
cross-model review to follow. **ES is OPEN; nothing here proves or disproves ES, or (★), at any infinite set of primes.**
Labels: PROVED / CONDITIONAL / CERTIFIED / EVIDENCE / CONJECTURE / Assessment. Scripts `scripts/z54_exactspin_*`, data
`data/z54/exactspin/`. Builds on `Z53_GENUSX.md` (notation, Thm X, Lemmas 1, 2, 4.1–4.6) and `Z53_GENUSLVAL.md` (Thm U).

## 0. Checkpoint log
* cp1 (34903cb1): statement (§1), why not closed (§2), Lemmas 3.1–3.2, falsifier engine, first run (10⁹–10¹²).
* cp2 (d25729e9, 8c58bb1b): spin dictionary (§4), matching against the spin theorems (§5), falsifier to 10¹⁴ (§6), verdict.
* cp3: internal hostile review (`data/z54/exactspin/review_hostile.md`, 25 findings) applied (§9). The main changes are:
  * the global Kummer-field equality is withdrawn;
  * the character support of S₂, S_o is corrected;
  * the Type I / fixed-order statements are scoped;
  * the cube moduli are separated in Prop 4.6 and Prop 5.2;
  * the numerical reading is corrected;
  * the dictionary check is extended.

## 1. Setting and the precise statement attacked

Notation of `Z53_GENUSX` §1:
* p ≡ 1 (4) is prime, and γ < 1 − α₁.
* The Thm U family is 𝔉 = {(u, w)}: u ∈ 𝒰 (squarefree, u ≡ 1 (4), U₀ < u ≤ U₁, gcd(u, p) = 1), and w ∈ 𝒮_u ∩ (Y, X]
  (odd squarefree, gcd(w, up) = 1).
* The shell is 𝔖 = {(u, w) ∈ 𝔉 : w | p + u}. On 𝔖, w″ := (p + u)/(2w) is odd and prime to u.
* At a shell point put G_u := (ℤ/u)^× = A₂ × A_o (2-Sylow × odd part), and x := −w″ mod u ∈ G_u, with
  x = x₂x_o accordingly.

Then (GENUSX §1, level form) A_u(w) = 1[w″ ≡ 3 (4)]·1[x = 1], A_u^gen(w) = 1[w″ ≡ 3 (4)]·1[x ∈ G_u²]/|G_u²|, and
  R_𝔉 − G_𝔉 = 2 Σ_{𝔖} 1[w″ ≡ 3 (4)]·(1[x = 1] − 1[x ∈ G²]/|G²|) = 2 Σ_{𝔖} 1[w″ ≡ 3 (4)]·φ(u)⁻¹ Σ_{ψ mod u, ψ² ≠ 1} ψ(x).
With T_u = O(p^{−δ} log p) on Theorem X windows (GENUSX Thm X), T_uw = R_𝔉 − G_𝔉 − T_u. So T_uw and R_𝔉 − G_𝔉 differ
by o(1) there; below, "the exact class layer" means R_𝔉 − G_𝔉.

**Layers.** For k ≥ 3 define the exact-order-k layer and its two complementary groupings:
  Δ_k := 2 Σ_{𝔖} 1[w″≡3(4)] φ(u)⁻¹ Σ_{ψ mod u, ord ψ = k} ψ(x),
  S₂ := 2 Σ_{𝔖} 1[w″≡3(4)] (1[x₂ = 1] − 1[x ∈ G²]/|A₂²|)·1[x_o = 1]  = Σ_{4 | k} Δ_k,
  S_o := 2 Σ_{𝔖} 1[w″≡3(4)] (1[x ∈ G²]/|A₂²|)·(1[x_o = 1] − 1/|A_o|)  = Σ_{k ≥ 3, 4 ∤ k} Δ_k   (Lemma 3.1).
S₂ is the part carried by characters whose 2-component has order ≥ 4. Their odd component is arbitrary, so these are the
characters of order divisible by 4, not only quartic or octic ones. S_o is the part carried by characters whose
2-component is real (order ≤ 2) and whose odd component is non-trivial (orders 3, 5, 6, 7, 9, 10, …).

**Statement attacked (the brief's question, made precise).**
(Q1) *Identification.* Can Δ_k, S₂, S_o (or a sub-piece) be written as Σ over the free variable w (or w″, or u) of a
spin / Kummer / Rédei-type symbol attached to a field depending only on p (or on p and u ≤ p^{α₁})?
(Q2) *Cancellation.* If so, does a FIMR / Koymans–Milovic-type theorem (cancellation of such a symbol over a free variable,
p fixed) apply? That is, can one prove, for some window family with M_𝔉 ≫ log²p,
  (Sp-k) Δ_k = o(log²p) for fixed k;  (Sp-2) S₂ = o(log²p);  (Sp-o) S_o = o(log²p)?
Since R_𝔉 − G_𝔉 = S₂ + S_o (Lemma 3.1), the bounds (Sp-2), (Sp-o) and (X-w) [T_w = o(log²p)] on a Theorem X window with Thm
U's (C3) would give R_𝔉 ≥ (c − o(1))log²p, hence (★) and ES(p) for all large p. So (Sp-2) + (Sp-o) is ES-(★) strength
(CONJECTURE-strength target, not claimed). (Sp-k) for fixed k is much weaker (Lemma 3.3).

## 2. Why this is not already closed, and what is already in the repository

*Precedents (credited):*
* the A₂ × A_odd decomposition of the class condition and the reading of its odd part via cubic (Eisenstein) reciprocity as a
  "spin" (`BRAINSTORM/bsB_redei_oddpart.md` items 1–4);
* the blindness of bounded-order character data to the class within a coset (`SINGLE_P_COUNT.md` Lemma 5.2);
* the shell injectivity / fibre structure (`Z53_GENUSX.md` Lemma 4.1);
* the measured u-side order ladder G^{(K)} (`Z53_GENUSX.md` §5).

*Not closed:*
* GENUSX treats the exact layers only through order-agnostic structure. Its Remark 4.7 concerns density-level
  bounded-order w-side layers. No identification of the exact u-side layers with Kummer/Rédei-type symbols over the free
  variable, and no matching against the spin theorems, exists.
* CLASS_FORCING Thm 2.1 and GENUSREDEI JRT, Cor F are *forcing* statements: what holds at every prime with a given Frobenius
  datum. They say nothing about cancellation of a symbol *summed over a free variable at fixed p*.
* GENUSREDEI §7.4 and `bsB_redei_oddpart.md` dismissed spins as "averages over the prime (B6)". In Lemma 4.1 form the free
  variable is w, not p, so that dismissal is not the operative obstruction here (§7, screen 4).
* FRONTIER §4 item 9 is likewise a forcing statement.

*New here:*
* the centred split S₂ + S_o with its character support and T1 localisation (Lemma 3.1);
* the explicit cubic and quartic dictionaries with all supplementary factors (§4);
* the norm-fibre cancellation lemma as applied here (Lemma 4.3);
* the twisted shrinking-disc reformulation (Prop 4.6) and its Fourier majorant limitation (Prop 5.2);
* the hypothesis matching (§5) and the falsifier (§6).

## 3. First lemmas (PROVED)

**Lemma 3.1 (2-adic / odd split; character support; T1 localisation).**
(a) R_𝔉 − G_𝔉 = S₂ + S_o identically.
(b) Per shell point, S₂ carries exactly the characters ψ = ψ₂ψ_o with ψ₂² ≠ 1, i.e. 4 | ord ψ. S_o carries exactly those
with ψ₂² = 1 and ψ_o ≠ 1, i.e. ord ψ ≥ 3 and 4 ∤ ord ψ. Hence S₂ = Σ_{4|k}Δ_k and S_o = Σ_{k≥3, 4∤k}Δ_k.
(c) Both summands vanish at every shell point with x ∉ G_u². Consequently, at an odd square n = m² with the same family
conventions (in particular gcd(u, m) = 1), S₂ = S_o = 0 *pointwise*.
*Proof.* (a) G² = A₂² × A_o (A_o has odd order), |G²| = |A₂²||A_o|; 1[x = 1] = 1[x₂ = 1]1[x_o = 1]; x₂ = 1 ⇒ x ∈ G². So
1[x=1] − 1[x∈G²]/|G²| = (1[x₂=1] − 1[x∈G²]/|A₂²|)1[x_o=1] + (1[x∈G²]/|A₂²|)(1[x_o=1] − 1/|A_o|).
(b) With |A₂|⁻¹Σ_{ψ₂}ψ₂(x) = 1[x₂ = 1], |A₂|⁻¹Σ_{ψ₂²=1}ψ₂(x) = 1[x ∈ G²]/|A₂²| and |A_o|⁻¹Σ_{ψ_o}ψ_o(x) = 1[x_o = 1]:
the S₂ factor is φ(u)⁻¹Σ_{ψ₂²≠1}Σ_{ψ_o}ψ₂ψ_o(x), and the S_o factor is φ(u)⁻¹Σ_{ψ₂²=1}Σ_{ψ_o≠1}ψ₂ψ_o(x).
(c) Both terms of (a) contain 1[x ∈ G²] or 1[x₂ = 1] (which implies x ∈ G²). At n = m²: gcd(w″, u) | gcd(n, u) = 1 and,
for ℓ | u, 2ww″ ≡ m² (mod ℓ). By Jacobi reciprocity (u ≡ 1 (4)),
(−w″/u) = (w″/u) = (u/w″) = ((2ww″ − m²)/w″) = (−1/w″) = −1 when w″ ≡ 3 (4) (gcd(w″, m) = 1 because gcd(w″, u) = 1).
So some ℓ | u has (−w″/ℓ) = −1, i.e. x ∉ G². This is Thm U §2.8 / GENUSX Lemma 2 at squares. ∎

**Lemma 3.2 (order-k layers at squares).** For every k ≥ 3 and x ∈ G_u,
  Σ_{ord ψ = k} ψ(x) = Σ_{d | k} μ(k/d)·|G/G^d|·1[x ∈ G^d],  |G/G^d| = ∏_{ℓ|u} gcd(d, ℓ − 1).
If 4 | k this vanishes for every x ∉ G² (hence Δ_k(m²) = 0 pointwise at odd squares). If 4 ∤ k it need not (§6: Δ₃, Δ₅,
Δ₆, Δ₇ ≠ 0 at squares).
*Proof.* Σ_{ψ^d = 1} ψ(x) = |G/G^d|·1[x ∈ G^d] (characters of G/G^d); then apply Möbius inversion over the order. If 4 | k
and μ(k/d) ≠ 0, then k/d is squarefree, so 2 | d, and x ∉ G² ⇒ x ∉ G^d. ∎
*Reading.* At odd-square inputs, S_o = 0 although its individual summands Δ_k (4 ∤ k) are not. The vanishing of S₂ and
S_o at squares is inherited from the empty genus; it is not produced by any cancellation among higher characters. So the
targets (Sp-2), (Sp-o) are T1-consistent without spin input. This says nothing about which step a successful proof would
use (§7, screen 1).

**Lemma 3.3 (fixed orders: non-reconstruction; variance ratio).** Fix K ≥ 2, and let P_K(x) := 1[x ∈ G^K]/|G^K| be the
projection of 1[x = 1] onto the characters ψ of G = G_u with ψ^K = 1.
(a) P_K = 1[· = 1] on G_u iff λ(u) | K iff ℓ − 1 | K for every prime ℓ | u. The set 𝒰_K of squarefree u with this property
is finite (u divides ∏_{ℓ prime, ℓ−1 | K} ℓ). For p ≥ p₀(K, α₀), 𝒰 ∩ 𝒰_K = ∅ (since U₀ = p^{α₀} → ∞).
(b) If x is uniform on G, put h := |G/G^K| and g := φ(u) > 1. Then
Var P_K(x) / Var 1[x = 1] = (h − 1)/(g − 1) ≤ h/g ≤ K^{ω(u)}/φ(u).
*Proof.* (a) G^K = {1} iff the exponent λ(u) = lcm(ℓ − 1) divides K; P_K = 1[· = 1] forces |G^K| = 1 (evaluate at x = 1).
(b) E P_K² = h/g², E P_K = 1/g, Var 1[x=1] = (1/g)(1 − 1/g). Also (h − 1)/(g − 1) ≤ h/g since h ≤ g, and
h = ∏_ℓ gcd(K, ℓ − 1) ≤ K^{ω(u)}. ∎
*Reading (scoped).* The characters of order dividing a fixed K do not reconstruct the class indicator outside the finite
set 𝒰_K, which the Thm U family leaves for large p. In the uniform model they carry a per-point variance fraction
≤ K^{ω(u)}/φ(u) = u^{−1+o(1)} uniformly on 𝒰. Consequently finitely many estimates (Sp-k) *alone* leave an uncontrolled
remainder Σ_{ord ψ ∤ K} in this character expansion. This is a statement about this expansion. It does not exclude that
finitely many fixed-order bounds, combined with other arithmetic input, contribute to a bound on the remainder. Compare
SINGLE_P_COUNT Lemma 5.2.

## 4. The spin dictionary (answer to Q1)

Throughout this section u = ℓ is prime. This is the *prime-u sub-piece* of each layer: a sub-sum of Δ_k, S₂, S_o with the
same normalisation. Fix (ℓ, w) ∈ 𝔖 and x = −w″ mod ℓ. Note x ≡ −p·(2w)⁻¹ (mod ℓ), because 2ww″ = p + ℓ.

**Lemma 4.1 (Kummer form, every order k; PROVED).** Let k | ℓ − 1 and 𝔩 a prime of ℚ(ζ_k) above ℓ (of degree 1). The
characters of (ℤ/ℓ)^× of exact order k are x ↦ (x/𝔩)_k^j, j ∈ (ℤ/k)^×, so
  Σ_{ord ψ = k} ψ(x) = Σ_{j∈(ℤ/k)^×} (x/𝔩)_k^j = c_k(e)  when (x/𝔩)_k = ζ_k^e  (c_k the Ramanujan sum),
and
  (x/𝔩)_k = (−w″/𝔩)_k = (−p/(2w) / 𝔩)_k = (−1/𝔩)_k·(p/𝔩)_k·(2w/𝔩)_k⁻¹.
The power-residue symbol (a/𝔩)_k is the Frobenius at 𝔩 acting on a^{1/k}. So the order-k class at prime u is the common
value at 𝔩 of the Kummer symbols of the two (generally different) Kummer extensions ℚ(ζ_k, (−w″)^{1/k}) and
ℚ(ζ_k, (−p/(2w))^{1/k}). The second is ramified at p, the first is not; only their Frobenius at 𝔩 agrees. In the product
form, the p-factor (p/𝔩)_k is the Frobenius of 𝔩 in the Kummer field ℚ(ζ_k, p^{1/k}), which depends only on p. The
w-factor is the Frobenius of 𝔩 in ℚ(ζ_k, (2w)^{1/k}), which depends on the free variable. Replacing 𝔩 by a conjugate
conjugates the symbol; the sum over j is conjugation-invariant.
*Proof.* O/𝔩 = F_ℓ, and (·/𝔩)_k: F_ℓ^× → μ_k is a surjective homomorphism, so its powers with j prime to k are exactly the
characters of order k. The symbol is multiplicative in the numerator; −w″ ≡ −p(2w)⁻¹ (mod 𝔩). ∎

**Lemma 4.2 (cubic dictionary; the p-part and the angle; PROVED).** Let ℓ ≡ 1 (3), π ∈ ℤ[ω] the primary generator
(π ≡ 2 mod 3) of a fixed prime above ℓ, and θ := π/π̄. Write w = 3^v w₁ (v ∈ {0, 1}; w is squarefree). Then
  (a) (x/π)₃ = (π/p)₃ · (π/2w₁)₃⁻¹ · (3/π)₃^{−v};  and if 3 ∤ w″, (x/π)₃ = (π/w″)₃.
  (b) For every rational prime q ∤ 3ℓ, (π/q)₃ := ∏_{𝔮|q}(π/𝔮)₃ = Ξ_q(θ mod q). Here Ξ_q is a non-trivial cubic character
      of the norm-one group T_q := ker(N: (ℤ[ω]/q)^× → F_q^×):
      * Ξ_q(t) = (t/𝔮)₃ if q = 𝔮𝔮̄ splits (on T_q this does not depend on the choice of 𝔮 | q);
      * Ξ_q(t) = t^{−(q+1)/3} if q is inert (q ≡ 2 mod 3, including q = 2).
      Moreover the symbol (·/q)₃ restricted to T_q equals Ξ_q⁻¹; in particular it is non-trivial on T_q.
  (c) Hence (x/π)₃ = Ξ_p(θ)·Ξ_{2w₁}(θ)⁻¹·(3/π)₃^{−v}, where Ξ_m := ∏_{q|m}Ξ_q. The ramified factor (3/π)₃ depends only on
      π mod 9 (CERTIFIED on the points below).
In this cubic case:
* the dependence on p is the factor (π/p)₃ = (p/π)₃, the Frobenius of π in ℚ(ω, p^{1/3}), a field depending only on p,
  evaluated at the chosen prime above u;
* the coupling to the free variable is the anticyclotomic character Ξ_{2w₁} of the *angle* θ of π modulo 2w₁;
* the shell condition fixes the norm N π = ℓ ≡ −p (mod w) and does not involve θ.
*Proof.* (a) x ≡ −p(2w)⁻¹ (mod π) and (−1/π)₃ = 1. The law of cubic reciprocity (for primary primes π₁, π₂ with
N π₁ ≠ N π₂, both norms ≠ 3: (π₁/π₂)₃ = (π₂/π₁)₃; e.g. Ireland–Rosen, *A Classical Introduction to Modern Number Theory*,
Ch. 9 — chapter reference not re-verified in this lane) is applied to the primary prime factors of a rational n with
gcd(n, 3ℓ) = 1. Here q ≡ 2 (3) is itself a primary prime, and q ≡ 1 (3) is ρρ̄ with ρ, ρ̄ primary. This gives
(n/π)₃ = (π/n)₃; take n = p and n = 2w₁. The ramified prime 3 is excluded from reciprocity, so (3/π)₃ is kept as a
separate factor. For 3 ∤ w″, apply the same reciprocity to n = w″.
(b) *Split q.* Complex conjugation σ maps 𝔮 to 𝔮̄ and acts on μ₃ by inversion, so (π/𝔮̄)₃ = σ((π̄/𝔮)₃) = (π̄/𝔮)₃⁻¹ and
(π/q)₃ = ((π/π̄)/𝔮)₃ = Ξ_q(θ). Ξ_q is non-trivial on T_q, because reduction mod 𝔮 is an isomorphism T_q ≅ F_q^×.
For t ∈ T_q, (t/𝔮̄)₃ = (t̄/𝔮)₃⁻¹ = (t⁻¹/𝔮)₃⁻¹ = (t/𝔮)₃.
*Inert q.* ℤ[ω]/q = F_{q²} and Frobenius is conjugation, so π^q ≡ π̄ and
(π/q)₃ ≡ π^{(q²−1)/3} = (π^{q−1})^{(q+1)/3} ≡ θ^{−(q+1)/3}. T_q is cyclic of order q + 1 ≡ 0 (3), so t ↦ t^{−(q+1)/3} is
onto μ₃.
*The last claim.* For any unit α mod q, (ᾱ/q)₃ = σ((α/q)₃) = (α/q)₃⁻¹ (q is rational), so
((α/ᾱ)/q)₃ = (α/q)₃² = (α/q)₃⁻¹ = Ξ_q(α/ᾱ)⁻¹. Every t ∈ T_q has the form α/ᾱ (Hilbert 90 for F_{q²}/F_q; in the split
case T_q = {(t, t⁻¹)}).
(c) Combine. ∎

**Lemma 4.3 (complete-sum cancellation over a norm fibre; PROVED).** Let m > 1 with gcd(m, 3) = 1 and m not a perfect cube,
c ∈ (ℤ/m)^×, and F_c := {α ∈ (ℤ[ω]/m)^× : N α ≡ c (mod m)}. Then Σ_{α∈F_c} (α/m)₃ = 0. If m is a cube, (α/m)₃ ≡ 1.
The analogue holds for (·/m)₄ in ℤ[i] whenever m is odd and some prime q has v_q(m) odd.
*Proof.* By CRT, F_c = ∏_{q^e ∥ m} F_{c,q^e} and (α/m)₃ = ∏ (α/q)₃^e, so it suffices that one factor vanishes.
* q is unramified in ℤ[ω], so the norm map (ℤ[ω]/q^e)^× → (ℤ/q^e)^× is onto: split, (a, b) ↦ ab; inert, the unramified
  local norm is onto the units.
* Its kernel T_{q^e} reduces onto T_q with fibres of equal size. Lifting uses N(1 + q^j z) ≡ 1 + q^j Tr(z) (mod q^{j+1}),
  and the trace is surjective. Hence F_{c,q^e} = α₀T_{q^e}.
* Therefore Σ_{F_{c,q^e}}(α/q)₃^e = (α₀/q)₃^e·|ker|·Σ_{t∈T_q}(t/q)₃^e. This is 0 when 3 ∤ e, because (·/q)₃ = Ξ_q⁻¹ is a
  non-trivial cubic character of T_q (Lemma 4.2(b)). Such a q exists unless m is a cube.
* For ℤ[i]: (t/q)₄ on T_q is the quadratic character of the cyclic group T_q (split: (t/𝔮)₄(t̄/𝔮)₄⁻¹ = (t/𝔮)₄²; inert
  q ≡ 3 (4): t^{(q²−1)/4} = t^{−(q+1)/2}). So the factor at q vanishes when e is odd. ∎
*Reading.* This identity would be the input of a direct complete-fibre (Type I-shaped) averaging: sum the symbol over the
argument at a fixed modulus. At density level, the order-3 class is therefore free. Lemma 4.5 records that, in the original
coordinates, the exact shell does not contain such fibres.

**Lemma 4.4 (quartic dictionary; PROVED).** Let ℓ ≡ 1 (4), π = a + bi ∈ ℤ[i] the primary generator (b even,
a + b ≡ 1 mod 4) of a fixed prime above ℓ, θ = π/π̄, and p = ρρ̄ with ρ primary. Then
  (a) (x/π)₄ = ε(π, w)·(π/p)₄·(π/w)₄⁻¹ with ε(π, w) = (−1/π)₄(2/π)₄⁻¹·[(−1/π)₄⁻¹ if w ≡ 3 (4)], where (−1/π)₄ = (−1)^{(ℓ−1)/4}.
      For every odd prime q ∤ ℓ, (π/q)₄ = Ξ_q(θ) is anticyclotomic: (π/q)₄ = ((π/π̄)/κ)₄ for split q = κκ̄, and
      (π/q)₄ ≡ (π̄/π)^{(q+1)/4} for inert q ≡ 3 (4); Ξ_q has order 4 on T_q.
  (b) (π/p)₄ = (ℓ/ρ)₄⁻¹·(π/ρ)₂. So the p-part is a quartic Dirichlet character mod p evaluated at u = ℓ, times the sign
      (π/ρ)₂ ∈ {±1}, a quadratic residue symbol in ℤ[i]: the Frobenius of (ρ) in ℚ(i, √π), a field depending only on u.
  (c) For a split prime q = κκ̄ dividing w (so ℓ ≡ −p mod q), (π/q)₄ = (π/κ)₂·(−p/κ)₄⁻¹: a quadratic Artin symbol of κ in
      ℚ(i, √π) times a quartic symbol of the fixed p at κ. Inert q | w contribute the angle factor of (a), which is not
      trivial in general (e.g. (−1+2i / 3)₄ = −i).
We call the signs in (b), (c) *Rédei-type bits*: they are quadratic Artin symbols in a field generated by a square root of
π_u. They are not identified here with a classical Rédei triple symbol or with a published spin.
*Proof.* (a) As 4.2(a), with the law of biquadratic reciprocity for primary primes α, β of coprime odd norms:
(α/β)₄ = (β/α)₄(−1)^{((Nα−1)/4)((Nβ−1)/4)} (e.g. Ireland–Rosen Ch. 9; reference not re-verified). For p ≡ 1 (4), the two
signs for ρ, ρ̄ cancel, so (p/π)₄ = (π/p)₄. An odd rational n ≡ 1 (4) is primary with (n² − 1)/4 even, so
(n/π)₄ = (π/n)₄; for n ≡ 3 (4) use −n. The anticyclotomic forms are proved as in 4.2(b).
(b) (π/ρ̄)₄ = (π̄/ρ)₄⁻¹ (conjugation), (π/ρ)₄(π̄/ρ)₄ = (ℓ/ρ)₄, and (π/ρ)₄² = (π/ρ)₂, so
(π/p)₄ = (π/ρ)₄(π̄/ρ)₄⁻¹ = (π/ρ)₄²(ℓ/ρ)₄⁻¹.
(c) The same computation with κ in place of ρ, and ℓ ≡ −p (mod κ). ∎

*CERTIFIED (finite checks; `scripts/z54_exactspin_cubic_check.py`, `data/z54/exactspin/dict_check.txt`).* Scope: the
engine dump of all shell points with w″ ≡ 3 (4) and u prime, at 24 primes p ≡ 1 (4) in [10⁹, 2·10¹²]; both classes of p
mod 3 occur, and p ≡ 1, 5 (8) occur. The checker uses the primary generator of *one* prime above ℓ (the conjugate gives the
conjugate symbol). Its residue symbols are computed from the definitions, with no reciprocity used:
* split q: both residue fields;
* inert q: F_{q²} exponentiation;
* (x/π)_k: x^{(ℓ−1)/k} mod ℓ with ω ≡ −a/b, resp. i ≡ −a/b, mod π.

Checked, all with 0 failures:
* 4.2(a) on 3 817 cubic points, including the factor (3/π)₃ when 3 | w; the factor (3/π)₃ is a function of π mod 9 on
  all of them;
* the w″ form of 4.2(a) on the 1 941 points with 3 ∤ w″;
* the anticyclotomic forms 4.2(b) for every prime of 2pw₁;
* 4.4(a) on 7 822 quartic points, with ε given by the explicit formula;
* 4.4(b) on all quartic points;
* 4.4(c) on 8 093 split prime factors of w;
* the quartic anticyclotomic forms on every prime factor of w.

Not covered by the check: non-squarefree moduli, and the statement "(·/q)_k = Ξ_q^{∓1} on all of T_q". The referee
verified these separately by exhaustive enumeration for small q, q^e ≤ 125 (`review_hostile.md` item 25; not stored as a
certificate).

**Lemma 4.5 (fibre sizes on the (★) support; PROVED).**
(a) For any odd n ≥ 3 and any (★) triple written in trial form d := 4uC − 1 | n + u (FRONTIER §2.1), d ≥ 4u − 1, i.e.
u ≤ (d + 1)/4 < d. Hence, for a fixed value of the level divisor d, at most one u occurs: the least positive residue of
−n mod d. The elements π of ℤ[ω] (resp. ℤ[i]) of norm u number ≤ 6τ(u) (resp. 4τ(u)).
(b) On the Thm U shell 𝔖 the same holds with w or w″ as the fixed modulus, for all shell points, not only hits
(w > Y ≥ U₁, w″ > 4U₁; GENUSX Lemma 4.1).
(c) For fixed u (fixed π), the moduli w, w″ range over divisors of the single integer p + u.
*Proof.* (a) d ≡ −1 (mod 4u) and d > 0 give d ≥ 4u − 1. Then d | n + u with 1 ≤ u < d fixes u ≡ −n (mod d). The bound
#{π : N π = u} ≤ 6τ(u) holds for ℤ[ω] (4τ(u) for ℤ[i]). (b), (c): GENUSX Lemma 4.1. ∎
*Reading (Assessment, scoped).* In the original coordinates, a direct application of Lemma 4.3 needs the argument π to run
over a whole norm fibre, or over a box long compared with the modulus. On the (★) support each fixed-modulus fibre has
≤ 6τ(u) points, and each fixed-argument fibre is a divisor set of one integer. This excludes the *direct* complete-fibre
averaging. It does not exclude transformed sums, completions, factorisations or other Type I-type decompositions, which
are not classified here (as in GENUSX Cor 4.2, Lemma 4.3).

**Proposition 4.6 (the cubic layer as twisted equidistribution of 2-dimensional roots in shrinking discs; PROVED
identity).** Let Δ₃^{pr} be the prime-u part of Δ₃ restricted to shell points with 3 ∤ w″.
* For c > 1 with gcd(c, 3p) = 1 put 𝔑(c) := {α ∈ ℤ[ω]/c : N α ≡ −p (mod c)}. These are the 2-dimensional "roots" of the
  norm form, and |𝔑(c)| = c·∏_{q|c}(1 − χ₋₃(q)/q) = c^{1+o(1)} (no uniform two-sided constant: products of split primes
  make the ratio small, products of inert primes make it large).
* For α ∈ 𝔑(c) let Φ_c(α) := 1 if the coset α + cℤ[ω] contains a primary prime π satisfying all of the following, and
  Φ_c(α) := 0 otherwise:
  * ℓ := N π ∈ 𝒰 is prime, ℓ ≡ 1 (3), ℓ ≡ −p (mod 2c);
  * w := (p + ℓ)/(2c) ∈ (Y, X] ∩ 𝒮_ℓ;
  * c ≡ 3 (4) and c > 4U₁.
  Such π is unique: two elements of a coset differ by a non-zero cβ, |cβ| ≥ c > 2√U₁ ≥ |π − π′|.
* Put ν(α) := 2/(N π − 1) where Φ_c(α) = 1.

Then
  Δ₃^{pr} = Σ_c Σ_{α∈𝔑(c)} Φ_c(α)ν(α)·Re (α/c)₃,
and Σ_{α∈𝔑(c)} (α/c)₃ = 0 for every such c that is not a perfect cube; for cubes, (α/c)₃ ≡ 1.

So on non-cube c, Δ₃^{pr} is a weighted covariance, fibre by fibre, between the cubic symbol (constant on cosets, mean 0 on
each fibre by Lemma 4.3) and the weight Φ_cν. In torus coordinates α/c ∈ ℂ/ℤ[ω], this is the equidistribution of the roots
of N α ≡ −p (mod c), *twisted by the cubic symbol*, in a disc of radius √U₁/c around 0. It is a Hooley /
Duke–Friedlander–Iwaniec-type question for the fixed polynomial N(α) + p, compatible with B6 (p fixed, the modulus c free),
but at a shrinking scale: the expected number of roots of one fibre in the disc is ≍ |𝔑(c)|·U₁/c² = c^{o(1)}U₁/c, which is
< 1 on the shell. The cube moduli c ≤ (p + U₁)/(2Y) number at most ((p + U₁)/(2Y))^{1/3}.
*Proof.* Lemma 4.2(a) with 3 ∤ w″ gives (x/π)₃ = (π/c)₃ with c = w″, constant on π + cℤ[ω]. The two primary primes π, π̄
above ℓ lie in different cosets, satisfy the same conditions, and give the same Re. The shell point's Δ₃ term is
2·(ℓ − 1)⁻¹·2Re(x/π)₃ = Σ_{π,π̄} ν·Re(·). The vanishing is Lemma 4.3 with m = c. ∎
*The full class event.* With the small representative π of a coset fixed, α ↦ Φ_c(α)·1[N π | c + 1] is a well-defined
function on 𝔑(c). What is missing is a description of it by finitely many fixed-order residue characters. The symbols
(α/c)_k are functions of α mod c alone, whereas 1[N π | c + 1] depends on the representative chosen by the disc
(N(π + cβ) ≡ N π only mod c). At prime ℓ, Lemma 4.1 writes the class indicator via the order-(ℓ − 1) symbol, i.e. via
ℚ(ζ_{ℓ−1}), of degree φ(ℓ − 1). This displayed construction has unbounded degree; no bounded-degree identification of the
full layer is established, and none is excluded.

## 5. Matching against the spin theorems (Q2)

Sources (from the papers' theorem statements, `data/z54/exactspin/lit_spins.md`; research subagent):
* **FIMR** (Friedlander–Iwaniec–Mazur–Rubin, *Invent. Math.* 193 (2013) 697–749, arXiv:1110.6331), Thm 1.1.
  * Hypotheses: K/ℚ cyclic of degree n ≥ 3, totally real, totally positive units are squares.
  * The spin is the *quadratic* symbol spin(σ, 𝔞) = (α/𝔞^σ), 𝔞 = (α), α ≫ 0, with σ a generator of Gal(K/ℚ).
  * The sum runs over principal prime ideals N𝔭 ≤ x of the fixed field: Σ spin(σ, 𝔭) ≪ x^{1−ν+ε},
    ν = δ/(2n(12n + 1)), under Conjecture C_n (short character sums, δ ≤ 2/n); unconditional for n = 3 (δ = 1/48).
  * Type I: Prop 6.1. Type II: Prop 7.1, via spin(𝔞𝔟) = spin(𝔞)spin(𝔟)·(cross symbols). Combination: Prop 5.2.
* **Koymans–Milovic.**
  * Compositio 2019 (arXiv:1611.10337): a generalised averaged spin in the fixed dihedral field ℚ(ζ₈, √(1+i)),
    conditional on a short-sum conjecture.
  * *Duke* 170 (2021) (arXiv:1809.09597): joint spins over prime ideals of a fixed Galois K, with S ∌ σ⁻¹ for σ ∈ S,
    under C_{|S|n}.
  * IMRN 2019 (arXiv:1705.05505): a sum over rational primes p ≤ X of the 16-rank sign, X^{1−1/3200}.
* **Large sieves for higher symbols.**
  * Heath-Brown's cubic large sieve, as restated in Blomer–Goldmakher–Louvel, arXiv:1112.1650, (1.2):
    Σ_{Nm≤M}|Σ_{Nn≤N} a_n (n/m)₃|² ≪ (M + N + (MN)^{2/3})(MN)^ε Σ|a_n|² (squarefree, primary).
  * Gao–Zhao, arXiv:1101.3646, Thm 1.1 (quartic, (MN)^{3/4} in place of (MN)^{2/3}).
  * BGL Thm 1.3, for n-th order Hecke characters.
  * These are mean squares over all moduli with coefficients independent of the modulus.
* **Koymans–Pagano** (JEMS 2022, under GRH): averages over a family of cyclic fields; B6 makes this inapplicable at
  fixed p.

| requirement | FIMR / KM | here | status |
|---|---|---|---|
| kind of symbol | quadratic symbol (α/𝔞^σ) of an ideal against a Galois conjugate | k-th power symbol (π_u/w)_k of the prime above the residual u = r_w against the free modulus (Lemmas 4.2, 4.4) | different: no identification with (generalised) spins supplied |
| base field / automorphism | totally real cyclic, n ≥ 3, σ ≠ σ⁻¹ (KM: inverse-free S) | ℚ(ζ₃), ℚ(i): imaginary quadratic, the only non-trivial automorphism satisfies σ = σ⁻¹ | ✗ (the hypotheses are not met) |
| field fixed, constants uniform | constants depend on K | the p-part needs the conductor-p twist (ℚ(ζ_k, p^{1/k})); uniformity in p not provided | ✗ |
| bounded order | one fixed n | fixed k per layer; the full class needs every order (Lemma 3.3) | ✗ for the layer |
| summation set | all prime ideals of K (boxes for Type I) | the shell, with small fibres (Lemma 4.5) | ✗ for the direct approach |
| Type II structure | twisted multiplicativity | CRT determines r_{w₁w₂} from (r_{w₁}, r_{w₂}), but no twisted-multiplicative factorisation of (π_{r_w}/w)_k suitable for Type II was found | ✗ (Assessment) |

**Corollary 5.1 (scoped consequences).**
(i) *PROVED.* On the exact shell, every fixed-modulus fibre has ≤ 6τ(u) points and every fixed-argument fibre is one
integer's divisor set (Lemma 4.5). Characters of order dividing a fixed K do not reconstruct the class event outside the
finite menu 𝒰_K (Lemma 3.3).
(ii) *Assessment.* The cited spin theorems do not apply as stated: wrong kind of symbol and base field (table), no
uniformity in p or in the order, and no identified Type I/II structure in the summation set. Finitely many fixed-order
estimates (Sp-k) would alone leave the high-order remainder of Lemma 3.3 uncontrolled.
(iii) *Formal exponent heuristic only.* FIMR's exponent satisfies ν ≤ 1/(n²(12n + 1)) when δ ≤ 2/n. Ignoring ε and the
field-dependent constants, a bound of shape x^{1−ν} with this ν would be non-trivial only while ν log x → ∞, i.e. for
n ≲ (log x)^{1/3}. No theorem with growing fields exists to which this applies; this only indicates the order of the gap.

**Proposition 5.2 (a limitation of the smooth Fourier majorant for the cubic layer; PROVED, scoped).**
*Setting.* Use the coordinates of Prop 4.6.
* Take a dyadic block c ∈ (C, 2C], gcd(c, 6p) = 1, with the perfect cubes excluded throughout. (Each cube carries a
  non-vanishing zero mode; their total is O(r²C^{4/3+o(1)}), relative size C^{−2/3+o(1)}.)
* Fix f₀ ∈ C_c^∞ supported in the unit disc, and put f_r(z) := f₀(z/r) on the torus 𝕋 := ℂ/ℤ[ω], with r := C^{θ−1}.
* Then |f̂_r(m)| ≪_B r²(1 + r|m|)^{−B} uniformly. Put
  N_f(C) := Σ_c Σ_{α∈𝔑(c)} f_r(α/c) and D_f(C) := Σ_c Σ_{α∈𝔑(c)} f_r(α/c)(α/c)₃.
* N_f(C) has expected size C^{2+o(1)}r².
* On the Thm U shell the relevant θ satisfies θ ≤ 1/2. Indeed c = w″ > 4U₁ (GENUSX Lemma 4.1), so a block containing shell
  points has U₁ < C/2 and disc radius √U₁/c < C^{−1/2}.

*Hypothesis.* Suppose a twisted Weyl bound with absolute values in c and some A ≥ 0:
  (W) Σ_{C<c≤2C} |Σ_{α∈𝔑(c)} (α/c)₃ e(⟨m, α/c⟩)| ≪ C^{2−δ}|m|^A  for all 0 ≠ m in the dual lattice.

*Conclusion.* Expand f_r in Fourier series. The m = 0 term vanishes on non-cube c by Lemma 4.3. Using the triangle
inequality in m,
  |D_f(C)| ≪ C^{2−δ}·r²Σ_{m≠0}(1 + r|m|)^{−B}|m|^A ≪ C^{2−δ}r^{−A},  so |D_f(C)|/(C²r²) ≪ C^{(1−θ)(2+A)−δ},
using Σ_{m≠0}(1 + r|m|)^{−B}|m|^A ≍ r^{−2−A} for B > A + 2 (dyadic shells).

*Reading.* This *upper bound* is o(1) when δ > (1 − θ)(2 + A); for θ ≤ 1/2 that means δ > 1 + A/2 ≥ 1. For comparison:
per-modulus square-root cancellation of the complete inner sums gives δ = 1/2. Square-root cancellation of a hypothetical
signed global double sum would correspond to δ = 1 (a different type of input). So this particular estimate — smooth
unweighted completion plus the triangle inequality in m and in c — cannot reach the cubic layer at the scale of the shell
with any (W) of square-root strength. It is the two-dimensional, cubic-twisted analogue of the closed Erdős–Turán/Fejér
item of FRONTIER §7.1. This is a limitation of the majorant, not a necessary condition for cancellation. Not covered:
* signed combinations over m, other smoothings, non-Fourier methods;
* the non-smooth prime/primary/window weights Φ_cν of Prop 4.6.
The transfer from the smooth disc to Φ_cν is open. Any such route would reach only the fixed order k = 3.

**Escape hatches left open (Assessment).**
1. *Hermitian form.* With H := [[2w, π], [π̄, w″]], det H = 2ww″ − N π = p. Shell points with u a norm are therefore integral
   binary hermitian forms over ℤ[ω] (resp. ℤ[i]) of determinant p in a thin region. The order-k twist (π/w″)_k =
   (H₁₂/H₂₂)_k (when defined) is invariant under H ↦ gHg*, g = [[1, t], [0, 1]] (H₂₂ fixed, H₁₂ ↦ H₁₂ + tH₂₂). Whether
   this connects to Kubota's metaplectic covers of SL₂ over ℤ[ω], ℤ[i], and to their spectral theory, is speculative and
   not developed. Any result would again be per fixed order.
2. *Quartic layer as a product over the prime factors of w.* By Lemma 4.4, at prime u the quartic symbol is
   ε·(ℓ/ρ)₄⁻¹(π_u/ρ)₂·∏_{q|w}(π_u/q)₄⁻¹. Each split q = κκ̄ contributes (π_u/κ)₂(−p/κ)₄⁻¹; each inert q contributes the
   angle factor Ξ_q(θ)⁻¹. At fixed u this is a twisted divisor sum of p + u (B2). Across u, the field ℚ(i, √π_u) moves. A
   fixed-p joint-spin theorem over a family of fields indexed by u ≤ p^{α₁} is not available.
3. *Dual windows.* If the class modulus u is the long variable (u ≫ w), Lemma 4.3 can be used in the variable π with w fixed,
   and bounded-order layers become density-level. Controlling them would need a Burgess-type bound for Hecke characters of
   conductor ≍ pw over boxes in ℤ[ω] (rows of length ≥ (pw)^{1/4+ε}). No such theorem with this conductor uniformity was
   located (lit_spins.md §5). In that regime the exact condition is u | p + 2w, divisors of one integer, so exactness
   migrates to the summed modulus.

## 6. Falsifier F: are the spin layers biased? (EVIDENCE; identities CERTIFIED on these runs)

**Design.** A spin *law* would be a bias of the class of w″ inside its genus coset forced by higher reciprocity. It would
show up as a non-zero sample mean of the layers in units of their random-model standard deviation. A cancellation
statement (Sp-k) would then be false or would need a main term. The statistic is one aggregate per prime, averaged over
sampled primes. It cannot detect a p-dependent bias that changes sign across p, and it does not test pointwise
independence.

*Engine.* `scripts/z54_exactspin_engine.c` (compile `gcc -O2 -o /tmp/z54_exactspin_eng scripts/z54_exactspin_engine.c
-lm`) uses GENUSX's shell enumeration. Per shell point with w″ ≡ 3 (4) it computes:
* R, G, S₂, S_o (Lemma 3.1);
* Δ_k for the listed orders k ∈ 𝒦 := {3, …, 13, 16, 20, 24} (Lemma 3.2);
* model variances:
  * S₂, S_o with x uniform in its actual G²-coset (genus-conditioned): V₂ = Σ 4·|A_o|⁻¹|A₂²|⁻¹(1 − |A₂²|⁻¹) and
    V_o = Σ 4·|A₂²|⁻²|A_o|⁻¹(1 − |A_o|⁻¹) over genus points;
  * Δ_k with x uniform on G: V_k = Σ 4N_k(u)/φ(u)², N_k = #{ord ψ = k}.

z := layer/√V; rows with V = 0 (then the layer is 0) are excluded, with the same convention in both summary scripts.

*Window.* The GENUSX standard window (U₀, U₁, Y, X) = (p^{1/12}, p^{1/3}/2, p^{1/3}, p^{2/3}/4). It is a proxy window,
outside Thm X's hypotheses (as in GENUSX §5).

*Samples.* `uv run --with sympy python scripts/z54_exactspin_samples.py`, seed 5400:
* random primes p ≡ 1 (24) in [10^k, 2·10^k];
* near-squares p = m² + k₀, k₀ ∈ {4, 16, 36, 64, 100};
* odd squares m².

*Commands* (from `data/z54/exactspin/`):
* `ENG=/tmp/z54_exactspin_eng python3 ../../../scripts/z54_exactspin_run.py layers.tsv TAG @samples/TAG.txt`, for TAG in
  rand_1e9 … rand_1e14, nearsq_1e10/12/14, squares_1e10/12/14;
* then `uv run --with numpy python scripts/z54_exactspin_stats.py layers.tsv` (→ `stats.txt`) and
  `scripts/z54_exactspin_table.py` (→ `table.md`);
* hard primes → `layers_hard.tsv`.

**Identity checks (CERTIFIED on these runs).**
* R − G = S₂ + S_o to the 10⁻⁶ printing precision on all 9 800 integers.
* The split x = 1 ⟺ (x₂ = 1 and x_o = 1) holds on every shell point (0 mismatches).
* At the 600 odd squares R = G = S₂ = S_o = 0, and Δ_k = 0 for every listed k with 4 | k (Lemmas 3.1, 3.2).
* At the same squares Δ₃, Δ₅, Δ₆, Δ₇ are non-zero: mean |Δ₃| = 0.240, 0.262, 0.214 at 10¹⁰, 10¹², 10¹⁴.
* Δ₆ = −Δ₃ holds exactly there, since at shell points outside G² (in particular at odd-square inputs) the d = 6 and d = 2
  terms of Lemma 3.2 vanish.

**Main table** (`table.md`):

| sample | N | mean G/log²p | mean R / mean G | P(R=0) | var S₂ / var(R−G) | var S_o / var(R−G) | z(S₂) mean, sd | z(S_o) mean, sd | z(R−G) mean, sd | max_{k∈𝒦} |mean z(Δ_k)|/se | sd z(Δ_k), k ∈ 𝒦 | Σ_{k∈𝒦} marginal variance share (model / emp.) |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
| rand 10⁹ | 2000 | 0.0051 | 1.024 | 0.301 | 0.53 | 0.51 | +0.016, 0.99 | +0.016, 0.98 | +0.024, 0.97 | 1.5 | 0.96–1.04 | 0.43 / 0.46 |
| rand 10¹⁰ | 2000 | 0.0057 | 1.006 | 0.210 | 0.52 | 0.52 | −0.007, 1.02 | +0.020, 1.01 | +0.009, 1.00 | 1.2 | 0.97–1.03 | 0.37 / 0.38 |
| rand 10¹¹ | 2000 | 0.0060 | 1.025 | 0.139 | 0.50 | 0.49 | +0.015, 1.01 | +0.034, 0.99 | +0.038, 1.01 | 1.8 | 0.94–1.04 | 0.33 / 0.32 |
| rand 10¹² | 1500 | 0.0065 | 1.030 | 0.070 | 0.49 | 0.47 | +0.052, 1.04 | +0.019, 1.01 | +0.051, 1.04 | 2.9 | 0.96–1.02 | 0.29 / 0.26 |
| rand 10¹³ | 800 | 0.0067 | 1.032 | 0.052 | 0.53 | 0.45 | +0.059, 1.08 | +0.029, 0.98 | +0.060, 1.05 | 1.9 | 0.92–1.05 | 0.26 / 0.24 |
| rand 10¹⁴ | 300 | 0.0070 | 1.026 | 0.030 | 0.51 | 0.48 | +0.012, 1.00 | +0.051, 0.95 | +0.045, 0.97 | 1.4 | 0.95–1.11 | 0.21 / 0.23 |
| near-sq 10¹⁰ | 200 | 0.0049 | 0.991 | 0.315 | 0.55 | 0.40 | +0.081, 1.04 | −0.125, 0.92 | −0.034, 1.00 | 2.5 | 0.92–1.07 | 0.35 / 0.34 |
| near-sq 10¹² | 200 | 0.0059 | 1.029 | 0.075 | 0.50 | 0.52 | +0.011, 1.01 | +0.047, 1.04 | +0.040, 1.01 | 1.8 | 0.93–1.12 | 0.27 / 0.26 |
| near-sq 10¹⁴ | 200 | 0.0063 | 0.963 | 0.055 | 0.50 | 0.56 | −0.041, 0.96 | −0.055, 0.98 | −0.070, 0.94 | 1.0 | 0.93–1.06 | 0.19 / 0.20 |

How to read the last two columns:
* "Σ marginal variance share" is Σ_{k∈𝒦} var(Δ_k)/var(R − G). It omits cross-covariances and the unlisted orders 14, 15,
  17, …. The model value is the mean over primes of Σ_{k∈𝒦}V_k/V_unif, with x uniform on G.
* For the selected sum Σ_{k∈𝒦}Δ_k itself, the empirical variance share is 0.473 at 10⁹ and 0.237 at 10¹⁴ (review recomputation).

**Reading (EVIDENCE, sample-average level).**
(a) *No significant sample-average bias.* Across all layers (S₂, S_o, R − G, and Δ_k for k ∈ 𝒦) and all nine non-square
samples:
* the z-sd lies in 0.92–1.12;
* the largest |mean z| is 0.178 (Δ₆, near-squares 10¹⁰), then 0.129 (Δ₁₆, near-squares 10¹²) and 0.125 (S_o,
  near-squares 10¹⁰);
* for random primes the largest is 0.085 (Δ₂₄, 10¹⁴);
* the largest |mean z|/se among the Δ_k is 2.9 (k = 24, 10¹²).

Among the 126 dependent (k, sample) tests, this is compatible with no bias; the multiple-comparison reading is informal.
This is consistent with — not a proof of — equidistribution of the class within the genus coset at every tested order. It
does not establish independence or pointwise cancellation at a fixed p.
(b) *Even split.* var S₂ ≈ var S_o ≈ ½ var(R − G), with |cov| ≤ 0.06·var(R − G). The listed orders carry a decreasing
marginal-variance share: 0.46 → 0.23 from 10⁹ to 10¹⁴, model 0.43 → 0.21. This is the direction predicted by Lemma 3.3(b);
it is not a direct check of Lemma 3.3, which concerns one fixed K.
(c) *A small offset.* Pooled over the 8 600 random primes, mean z(R − G) = +0.0325 ± 0.0108 (3.0 se), and mean R / mean
G = 1.006–1.032. Its source is not resolved here. A candidate (not tested) is the finite-size density offset
T_u = M^cls_𝔉 − M_𝔉, which GENUSX measured directly at 10¹⁰ as M^cls/M ≈ 1.01 in this window.
(d) *(★)-zero primes* (`layers_hard.tsv`; R = 0, so R − G = −G = S₂ + S_o). The deficit splits differently from prime to
prime: (S₂, S_o) = (−1.50, +0.33) at 712321, (0, −1.16) at 5212561, (−0.75, −1.15) at 8813281, (−1.00, −0.33) at 329617.
At these primes the failures are not confined to one of the two layers.

## 7. The four FRONTIER §4 hard screens (Assessment, except where labelled)

1. **T1 (odd squares): consistent.**
   * S₂ and S_o vanish pointwise at odd squares (Lemma 3.1, PROVED; CERTIFIED on 600 squares). They vanish because the
     genus is empty there; the exact odd-order layers Δ_k (4 ∤ k) do *not* vanish at squares (Lemma 3.2; CERTIFIED).
   * So the bounds (Sp-2), (Sp-o) are T1-consistent targets. The square-sensitive input of the conditional chain in §1 is
     Thm U's lower bound for the genus main term.
   * Nothing here decides whether some proof could instead draw primality from the higher layers. At n = m² the p-part of
     the dictionary changes, e.g. (p/π_u)₄ becomes (m²/π_u)₄ = (m/π_u)₄², whose order is at most 2; the dictionary is not
     claimed to be square-blind.
2. **8/131: not applicable** (structure and identity statements about the (★) family, not a solution mechanism).
3. **Tied modulus (B2): fails — this is where the lane ends.**
   * In the cubic and quartic dictionaries, the tie appears in the coupling factor (π_{r_w}/2w₁)_k. This is the angle of
     the prime above the residual r_w = −p mod w, read modulo the free variable.
   * Every fixed-modulus fibre of the shell has ≤ 6τ(u) points, and every fixed-argument fibre is one integer's divisor set
     (Lemma 4.5).
   * Fixed orders do not reconstruct the class (Lemma 3.3).
4. **Fixed p (B6): passes.** Every statement is at fixed p; the free variables are w, w″, u, π and the root α mod c. FIMR
   and Koymans–Milovic sum over prime ideals of a fixed field, which would be a fixed-p operation here. The mismatch is in
   their other hypotheses (§5 table), not in B6.

## 8. Verdict, proposed FRONTIER §7 text, bottom line

**Verdict: narrowed.** No bound on T_uw is obtained; the spin route is mapped, and specified sub-routes are closed as scoped
statements.
* *Q1, per fixed order (PROVED; finite CERTIFIED checks).* At prime u = ℓ, the order-k part of the class of the level divisor
  is c_k of the power-residue symbol (−w″/𝔩)_k = (−1/𝔩)_k(p/𝔩)_k(2w/𝔩)_k⁻¹ (Lemma 4.1). Its p-factor is the Frobenius in
  the Kummer field ℚ(ζ_k, p^{1/k}), a field depending only on p.
  * For k = 3 (Lemma 4.2, including the ramified factor (3/π)₃^{−v}): (x/π)₃ = Ξ_p(θ)Ξ_{2w₁}(θ)⁻¹(3/π)₃^{−v}. This is an
    anticyclotomic character of the angle θ = π_u/π̄_u modulo p·2w₁ — with π_u the primary generator of a fixed prime above
    u; the conjugate prime gives the conjugate value.
  * For k = 4 (Lemma 4.4): (x/π)₄ = ε(π, w)(π/p)₄(π/w)₄⁻¹, with (π/p)₄ = (u/ρ)₄⁻¹(π_u/ρ)₂. A split prime κ | w contributes
    (π_u/κ)₂(−p/κ)₄⁻¹, and an inert prime contributes an angle factor.
* *Q1, full layer.* No bounded-degree identification is established. The displayed construction at prime u uses
  ℚ(ζ_{u−1}).
* *Decomposition (PROVED).* R_𝔉 − G_𝔉 = S₂ + S_o with S₂ = Σ_{4|k}Δ_k and S_o = Σ_{4∤k}Δ_k. Both vanish pointwise off the
  genus, hence at odd squares, while individual Δ_k with 4 ∤ k do not (Lemmas 3.1, 3.2).
* *Scoped limitations.*
  * Fibre sizes on the (★) support (Lemma 4.5, PROVED) exclude the direct complete-fibre averaging of Lemma 4.3. Other Type
    I decompositions are not classified (Assessment).
  * Fixed-order character data do not reconstruct the class outside a finite menu of u (Lemma 3.3, PROVED).
  * The cubic layer is a twisted shrinking-disc equidistribution problem for the roots of N(α) ≡ −p (mod c) (Prop 4.6,
    PROVED identity). The smooth Fourier majorant with triangle inequalities needs δ > (1 − θ)(2 + A) ≥ 1 in (W)
    (Prop 5.2, PROVED, scoped; cube moduli separated).
  * The FIMR / Koymans–Milovic hypotheses are not met (symbol type, base field, uniformity, summation set; §5 table,
    Assessment).
* *EVIDENCE (10⁹–10¹⁴: 8 600 random primes, 600 near-squares, 600 squares).*
  * No significant sample-average bias in any layer: largest |mean z| = 0.178 among near-squares and 0.085 among random
    primes; z-sd 0.92–1.12.
  * S₂ and S_o each carry ≈ ½ of var(R − G).
  * A small positive offset of R − G (+0.03σ, pooled) is unexplained.
* *What survives (Assessment).*
  * A fixed-p theory of symbols over a *moving* family of fields indexed by u ≤ p^{α₁}; no such theorem is known.
  * Signed or non-Fourier methods for the twisted 2-dimensional root problem, e.g. a hermitian-form/metaplectic approach
    (§5 hatch 1), which would still be per fixed order.
  * Type II structure in the residual map w ↦ r_w. EXACTSUM's exponential-sum angle attacks the same map analytically.

*Proposed FRONTIER §7 text* (append to item 3, after the GENUSX entry):
> *(z54, `Z54_EXACTSPIN.md`, internal hostile review applied; cross-model review pending.)* Higher-order symbols on the
> exact class layer.
> * R_𝔉 − G_𝔉 = S₂ + S_o, with S₂ = Σ_{4|k}Δ_k (characters of order divisible by 4) and S_o = Σ_{k≥3, 4∤k}Δ_k (PROVED).
>   Both vanish pointwise at odd squares, but only via the empty genus; the individual Δ_k with 4 ∤ k do not.
> * Dictionary at prime u (PROVED; finite CERTIFIED checks on 3 817 cubic / 7 822 quartic shell points).
>   * The order-k class is c_k((−w″/𝔩)_k) with (−w″/𝔩)_k = (−1/𝔩)_k(p/𝔩)_k(2w/𝔩)_k⁻¹. The p-factor is the Frobenius of 𝔩 in
>     ℚ(ζ_k, p^{1/k}).
>   * For k = 3, (x/π)₃ = Ξ_p(θ)Ξ_{2w₁}(θ)⁻¹(3/π)₃^{−v}: an anticyclotomic character of the angle θ = π_u/π̄_u, with a
>     ramified factor at 3.
>   * For k = 4, (x/π)₄ = ε(π, w)(π/p)₄(π/w)₄⁻¹, with (π/p)₄ = (u/ρ)₄⁻¹(π_u/ρ)₂ and split-prime factors (π_u/κ)₂(−p/κ)₄⁻¹.
>   * No bounded-degree identification of the full layer is established.
> * Scoped limitations (PROVED as stated).
>   * Complete sums over norm fibres vanish, but on the (★) support each fixed-modulus fibre has ≤ 6τ(u) points (the level
>     divisor exceeds u); this excludes the direct complete-fibre average only.
>   * Fixed orders do not reconstruct the class outside a finite menu of u.
>   * The cubic layer is a twisted equidistribution problem for roots of N(α) ≡ −p (mod c) in discs of radius ≤ c^{−1/2};
>     the smooth Fourier majorant would need better-than-square-root input there.
> * FIMR / Koymans–Milovic do not apply as stated: quadratic spins in totally real cyclic fields of degree ≥ 3, versus
>   k-th power symbols over ℚ(ζ₃), ℚ(i), with no uniformity in p or the order (Assessment). B6 is not the obstruction.
> * EVIDENCE (10⁹–10¹⁴): no significant sample-average bias at any listed order ≤ 24 (|mean z| ≤ 0.18, sd ≈ 1). S₂ and S_o
>   each carry ≈ ½ of var(R − G).

**Bottom line.** At every fixed order, the class of the level divisor inside its genus coset has an explicit Kummer
description at prime u. Its p-factor is a Frobenius in ℚ(ζ_k, p^{1/k}), a field depending only on p. In the cubic and
quartic cases the coupling to the free variable is an anticyclotomic character of the angle of the prime above u, read
modulo w; this coupling carries the tie. Numerically no sample-average bias appears in any layer up to 10¹⁴. But this
does not produce a bound:
* the cited spin theorems do not apply as stated (different symbol, base field, uniformity and summation set);
* the direct complete-fibre averaging is unavailable on the (★) support, because there the level divisor always exceeds
  the class modulus;
* fixed orders do not reconstruct the class outside a finite menu of u;
* the smooth Fourier majorant for the cubic layer would need better-than-square-root input.
Each of these is a scoped statement, not a theorem about all methods. The obstruction remains the tied modulus, now visible
as the residual map w ↦ π_{r_w}. **ES remains OPEN.**

## 9. Review log

**Internal hostile review** (deep-mode subagent; `data/z54/exactspin/review_hostile.md`; verdict "major revision required";
no edits by the reviewer). The reviewer:
* reproduced `stats.txt` and `table.md` byte for byte, and four engine rows;
* reproduced the dictionary checks at three primes;
* additionally verified the explicit quartic ε, 4.4(b), 4.4(c), the w″ form of 4.2(a), and the norm-fibre lemma by
  exhaustive enumeration for q^e ≤ 125;
* confirmed that the core algebra (Lemmas 3.1–3.3, 4.2–4.5) survives.

Fixes applied (finding numbers in brackets):
* [1] Lemma 4.1: the false equality of Kummer fields is withdrawn; only the Frobenius at 𝔩 agrees.
* [2] The character support of S₂ / S_o is corrected (Lemma 3.1(b): S₂ = Σ_{4|k}Δ_k, S_o = Σ_{4∤k}Δ_k).
* [3] The Type I statements are scoped: Lemma 4.5 is PROVED for fibre sizes only; the method reading is Assessment;
  "no Type I sum in any variable" is removed.
* [4] Cube moduli are excluded from Prop 5.2 and separated in Prop 4.6 (zero mode, count bound with (p + U₁)/(2Y)).
* [5] Prop 5.2 is restated as a limitation of a specified smooth majorant (f_r = f₀(·/r), A ≥ 0); the prime/window
  transfer is stated as open.
* [6] The justification θ ≤ 1/2 now uses w″ > 4U₁; for general hits, u ≤ (d + 1)/4.
* [7] Prop 4.6 now has the exact |𝔑(c)|, gcd(c, 3p) = 1, a weighted covariance on non-cube fibres, and the corrected cube
  bound.
* [8] "The full class event is not a function on 𝔑(c)" is replaced by the correct narrower statement.
* [9] The readings of Lemma 3.3 and Cor 5.1 are narrowed to the character expansion. "Q1: no for the layer" becomes "no
  bounded-degree identification established".
* [10] The hypothesis table gains rows for symbol type, base field / automorphism and uniformity. The λ(u) normal-order
  claim is deleted. The (log x)^{1/3} computation is labelled a formal heuristic. Large sieves are distinguished from spin
  theorems.
* [11] The CRT statement is corrected.
* [12] The T1 screen no longer claims that spins cannot carry primality, or that nothing degenerates at squares.
* [13] The numerical claims are corrected: the largest |mean z| is 0.178, the statistics are sample-average only, and
  fixed-p independence is not claimed.
* [14] "Orders ≤ 24 share" is relabelled as the listed-order sum of marginal variances, with the selected-sum values
  quoted.
* [15] Both summary scripts now exclude zero-variance rows consistently.
* [16] The checker was extended (w″ form, explicit ε, 4.4(b), 4.4(c), quartic anticyclotomic forms; all 24 primes rerun);
  the CERTIFIED scope is enumerated.
* [17] The Ireland–Rosen pinpoint numbers are removed; the GRH qualification for Koymans–Pagano is added.
* [18] General-k (Kummer) and k = 3, 4 (anticyclotomic) statements are separated; the supplementary factors and the
  primary-prime choice are kept.
* [19] The hatches are corrected (w versus w″, inert factors with the example (−1+2i/3)₄ = −i, metaplectic link labelled
  speculative, "provable in principle" removed).
* [20] The square convention gcd(u, m) = 1 and the inequality (h − 1)/(g − 1) ≤ h/g are added.
* [21] The trace-lifting sentence is added to Lemma 4.3.
* [22] Precedents are credited (§2).
* [23] Stale checkpoint counts, a dangling lemma reference, and the "non-squares" wording are fixed.

A cross-model review is to follow.
