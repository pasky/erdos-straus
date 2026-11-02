# Z54_EXACTSPIN — spins, Kummer and Rédei symbols over the free variable w in the exact class layer T_uw

Status: z54 depth lane EXACTSPIN (gap 2, algebraic angle). Internal; internally reviewed only (review log §9).
**ES is OPEN; nothing here proves or disproves ES, or (★), at any infinite set of primes.** Labels: PROVED / CONDITIONAL /
CERTIFIED / EVIDENCE / CONJECTURE / Assessment. Scripts `scripts/z54_exactspin_*`, data `data/z54/exactspin/`.
Builds on `Z53_GENUSX.md` (notation, Thm X, Lemmas 1, 2, 4.1–4.6) and `Z53_GENUSLVAL.md` (Thm U).

## 0. Checkpoint log
* cp1: precise statement (§1), why not closed (§2), first lemmas (§3: spin split S₂ + S_odd, T1 localisation, order-k
  layers), first falsifier (§6: 9 500 primes 10⁹–10¹², controls).

## 1. Setting and the precise statement attacked

Notation of `Z53_GENUSX` §1: p ≡ 1 (4) prime; Thm U family 𝔉 = {(u, w)}: u ∈ 𝒰 (squarefree, u ≡ 1 (4), U₀ < u ≤ U₁),
w ∈ 𝒮_u ∩ (Y, X] (odd squarefree, gcd(w, up) = 1), γ < 1 − α₁. Shell 𝔖 = {(u, w) ∈ 𝔉 : w | p + u}; on 𝔖,
w″ := (p + u)/(2w) is odd and prime to u. Put, at a shell point,
  G_u := (ℤ/u)^× = A₂ × A_o (2-Sylow × odd part),  x := −w″ mod u ∈ G_u.
Then (GENUSX §1, level form) A_u(w) = 1[w″ ≡ 3 (4)]·1[x = 1], A_u^gen(w) = 1[w″ ≡ 3 (4)]·1[x ∈ G_u²]/|G_u²|, and
  R_𝔉 − G_𝔉 = 2 Σ_{𝔖} 1[w″ ≡ 3 (4)]·(1[x = 1] − 1[x ∈ G²]/|G²|) = 2 Σ_{𝔖} 1[w″ ≡ 3 (4)]·φ(u)⁻¹ Σ_{ψ mod u, ψ² ≠ 1} ψ(x).
With T_u = O(p^{−δ} log p) on Theorem X windows (GENUSX Thm X), T_uw = R_𝔉 − G_𝔉 − T_u, so T_uw and R_𝔉 − G_𝔉 differ
by o(1) there; below "the exact class layer" means R_𝔉 − G_𝔉.

**Spin layers.** For k ≥ 3 the *exact-order-k layer* and the *2-adic / odd spin layers* are
  Δ_k := 2 Σ_{𝔖} 1[w″≡3(4)] φ(u)⁻¹ Σ_{ψ mod u, ord ψ = k} ψ(x),
  S₂ := 2 Σ_{𝔖} 1[w″≡3(4)] (1[x₂ = 1] − 1[x ∈ G²]/|A₂²|)·1[x_o = 1],
  S_o := 2 Σ_{𝔖} 1[w″≡3(4)] (1[x ∈ G²]/|A₂²|)·(1[x_o = 1] − 1/|A_o|),
(x = x₂x_o the A₂ × A_o decomposition). S₂ is governed by the characters of 2-power order ≥ 4 (quartic, octic, … —
Rédei/governing-field data), S_o by the odd-order characters (cubic, quintic, … — Eisenstein/Kummer data).

**Statement attacked (the brief's question, made precise).**
(Q1) *Identification.* Can Δ_k, S₂, S_o (or a sub-piece) be written as Σ over the free variable w (or w″, or u) of a
spin / Kummer / Rédei symbol attached to a field depending only on p (or on p and u ≤ p^{α₁})?
(Q2) *Cancellation.* If so, does a FIMR / Koymans–Milovic-type theorem (cancellation of such a symbol over a free variable,
p fixed) apply, i.e. can one prove for some window family with M_𝔉 ≫ log²p
  (Sp-k) Δ_k = o(log²p) for fixed k;  (Sp-2) S₂ = o(log²p);  (Sp-o) S_o = o(log²p)?
Since R_𝔉 − G_𝔉 = S₂ + S_o (Lemma 3.1), (Sp-2) + (Sp-o) + (X-w) [T_w = o(log²p)] on a Theorem X window with Thm U's (C3)
would give R_𝔉 ≥ (c − o(1))log²p, hence (★) and ES(p) for all large p. So (Sp-2) + (Sp-o) is ES-(★) strength
(CONJECTURE-strength target, not claimed). (Sp-k) for fixed k is much weaker (Lemma 3.4).

## 2. Why this is not already closed
* GENUSX treats the exact layers only through order-agnostic structure (Lemma 4.1 injectivity, Lemma 4.3 diagonal
  Cauchy–Schwarz, Prop 4.6 interval data on χ_p for the BM *genus* component); its Remark 4.7 concerns *density-level*
  bounded-order w-side layers. The u-side order filtration of R − G over exact divisors was only measured (ladder G^{(K)}).
* CLASS_FORCING Thm 2.1 / GENUSREDEI JRT, Cor F are *forcing* statements (what holds at every prime with a given Frobenius
  datum); they say nothing about cancellation of a symbol *summed over a free variable at fixed p*. GENUSREDEI §7.4 and
  `BRAINSTORM/bsB_redei_oddpart.md` dismissed spins as "averages over the prime (B6)"; but in Lemma 4.1 form the free
  variable is w, not p, so that dismissal does not apply as stated. FIMR/Koymans–Milovic were never matched against the
  exact layer.
* FRONTIER §4 item 9 ("reciprocity forces parity, never class") is a forcing statement; equidistribution (cancellation)
  of higher symbols over a free variable is not excluded by it.

## 3. First lemmas (PROVED)

**Lemma 3.1 (2-adic / odd split; T1 localisation).** R_𝔉 − G_𝔉 = S₂ + S_o identically, and both summands vanish at
every shell point with x ∉ G_u². In particular at an odd square n = m² (where G_𝔉(m²) = 0, so no shell point with
w″ ≡ 3 (4) has x ∈ G²; GENUSX §5 CERTIFIED and Thm U §2.8) S₂ = S_o = 0 *pointwise*.
*Proof.* G² = A₂² × A_o (A_o has odd order, so A_o² = A_o), |G²| = |A₂²||A_o|; 1[x = 1] = 1[x₂ = 1]1[x_o = 1];
x₂ = 1 ⇒ x ∈ G². So 1[x=1] − 1[x∈G²]/|G²| = (1[x₂=1] − 1[x∈G²]/|A₂²|)1[x_o=1] + (1[x∈G²]/|A₂²|)(1[x_o=1] − 1/|A_o|), and
both terms vanish if x ∉ G². At n = m² the genus layer G is a sum of non-negative terms with value 0. ∎

**Lemma 3.2 (order-k layers and squares).** For every k ≥ 3 and x ∈ G_u,
  Σ_{ord ψ = k} ψ(x) = Σ_{d | k} μ(k/d)·|G/G^d|·1[x ∈ G^d],  |G/G^d| = ∏_{ℓ|u} gcd(d, ℓ − 1).
If 4 | k this vanishes for every x ∉ G² (hence Δ_k(m²) = 0 pointwise at odd squares); if 4 ∤ k it need not.
*Proof.* Σ_{ψ^d = 1} ψ(x) = |G/G^d|·1[x ∈ G^d] (characters of G/G^d), then Möbius inversion over the order. If 4 | k
and μ(k/d) ≠ 0 then k/d is squarefree, so 2 | d and x ∉ G² ⇒ x ∉ G^d. For 4 ∤ k see §6 (Δ₃, Δ₅, Δ₆ ≠ 0 at squares). ∎
*Reading.* Odd-order spin layers (and k ≡ 2 (4)) are T1-blind: a cancellation theorem for them holds or fails
regardless of whether n is a square; the square-sensitive step must stay in the 2-adic genus (Thm U's step).

**Lemma 3.3 (bounded orders are a finite menu; variance share).** Fix K ≥ 2 and let P_K(x) := 1[x ∈ G^K]/|G^K| be the
projection of 1[x = 1] onto the characters ψ of G = G_u with ψ^K = 1.
(a) P_K = 1[· = 1] on G_u iff λ(u) | K iff ℓ − 1 | K for every prime ℓ | u. The set 𝒰_K of squarefree u with this property
is finite (u divides ∏_{ℓ prime, ℓ−1 | K} ℓ). For p ≥ p₀(K, α₀), 𝒰 ∩ 𝒰_K = ∅ (since U₀ = p^{α₀} → ∞).
(b) If x is uniform on G, Var P_K(x) / Var 1[x = 1] = (|G/G^K| − 1)/(φ(u) − 1) ≤ K^{ω(u)}/φ(u).
*Proof.* (a) G^K = {1} iff the exponent λ(u) = lcm(ℓ − 1) divides K; P_K = 1[· = 1] forces |G^K| = 1 (evaluate at x = 1).
(b) E P_K² = 1/(φ|G^K|), E P_K = 1/φ, Var 1[x=1] = (1/φ)(1 − 1/φ), and 1/|G^K| = |G/G^K|/φ;
|G/G^K| = ∏_ℓ gcd(K, ℓ − 1) ≤ K^{ω(u)}. ∎
*Reading.* Any argument that controls only the characters of order dividing a fixed K (each FIMR / Koymans–Milovic /
cubic-large-sieve input is of this kind: one fixed field ℚ(ζ_k)) determines the class event only on the finite menu
𝒰_K — which the Thm U family leaves for large p — and in the uniform-class model carries a share ≤ K^{ω(u)}/φ(u) of the
per-point variance, → 0 uniformly on 𝒰 as U₀ → ∞. EVIDENCE (§6): orders k ≤ 24 carry 46 % → 23 % of var(R − G)
from 10⁹ to 10¹⁴, decreasing, in agreement with the model.

## 4. The spin dictionary (answer to Q1; PROVED, with a CERTIFIED check)

Throughout this section u = ℓ is prime (the *prime-u sub-piece* of each layer; it is a sub-sum of Δ_k, S₂, S_o with the
same normalisation) and (ℓ, w) ∈ 𝔖, x = −w″ mod ℓ. Note x ≡ −p·(2w)⁻¹ (mod ℓ), because 2ww″ = p + ℓ.

**Lemma 4.1 (Kummer form).** Let k | ℓ − 1 and 𝔩 a prime of ℚ(ζ_k) above ℓ (of degree 1). The characters of
(ℤ/ℓ)^× of exact order k are x ↦ (x/𝔩)_k^j, j ∈ (ℤ/k)^×, so
  Σ_{ord ψ = k} ψ(x) = Σ_{j∈(ℤ/k)^×} (x/𝔩)_k^j = c_k(e)  when (x/𝔩)_k = ζ_k^e  (c_k the Ramanujan sum),
and (x/𝔩)_k = (−p/2w / 𝔩)_k = (−w″/𝔩)_k is the Kummer symbol of 𝔩 in ℚ(ζ_k, (−p/(2w))^{1/k}) = ℚ(ζ_k, (−w″)^{1/k}) (same
Frobenius at 𝔩): **the order-k class of the level divisor at prime u is the splitting of the residual prime u = r_w in a
Kummer field generated by a k-th root of −p/(2w), a field depending on p and on the free variable w.**
*Proof.* O/𝔩 = F_ℓ; (·/𝔩)_k: F_ℓ^× → μ_k is a surjective homomorphism, so its powers with j prime to k are exactly the
characters of order k. The Kummer interpretation is the definition of the power-residue symbol (Frobenius at 𝔩 acting on
a k-th root of a, 𝔩 ∤ ka). The two radicands are congruent mod 𝔩. ∎

**Lemma 4.2 (cubic dictionary; the p-part and the angle).** Let ℓ ≡ 1 (3), π ∈ ℤ[ω] a primary prime (π ≡ 2 mod 3) with
N π = ℓ, θ := π/π̄. Write w = 3^v w₁ (v ∈ {0,1}; w is squarefree). Then
  (a) (x/π)₃ = (π/p)₃ · (π/2w₁)₃⁻¹ · (3/π)₃^{−v},  and, if 3 ∤ w″, (x/π)₃ = (π/w″)₃;
  (b) for every rational prime q ∤ 3ℓ, (π/q)₃ := ∏_{𝔮|q}(π/𝔮)₃ = Ξ_q(θ mod q), where Ξ_q is a non-trivial cubic character of
      the norm-one group T_q := ker(N: (ℤ[ω]/q)^× → F_q^×): Ξ_q(t) = (t/𝔮)₃² if q = 𝔮𝔮̄ splits, Ξ_q(t) = t^{−(q+1)/3} if q is
      inert (q ≡ 2 mod 3, including q = 2);
  (c) hence (x/π)₃ = Ξ_p(θ)·Ξ_{2w₁}(θ)⁻¹·(3/π)₃^{−v} (Ξ_m := ∏_{q|m}Ξ_q), and (3/π)₃ depends only on π mod 9.
So the only dependence on p is the factor (π/p)₃ = (p/π)₃ = **Frobenius of π in the Kummer field ℚ(ω, p^{1/3}), a field
depending only on p, evaluated at the prime above u** (a function of (p, u)); the coupling to the free variable is the
anticyclotomic character Ξ_{2w₁} of the *angle* θ of π modulo 2w₁. The shell condition fixes the norm
N π = ℓ ≡ −p (mod w) and says nothing about θ.
*Proof.* (a) x ≡ −p(2w)⁻¹ (mod π) and (−1/π)₃ = 1. Cubic reciprocity (Ireland–Rosen, *A Classical Introduction to Modern
Number Theory*, Ch. 9 §3, Thm 1: (π₁/π₂)₃ = (π₂/π₁)₃ for primary π₁, π₂ with N π₁ ≠ N π₂, both ≠ 3), applied to the
primary prime factors of a rational n with gcd(n, 3ℓ) = 1 (q ≡ 2 (3) is itself a primary prime; q ≡ 1 (3) is ρρ̄ with ρ, ρ̄
primary), gives (n/π)₃ = (π/n)₃; take n = p and n = 2w₁. The prime 3 is ramified and excluded from reciprocity; the factor
(3/π)₃ is kept as is (it is determined by π mod 9 by the supplementary law; checked numerically below). For 3 ∤ w″ apply
the same reciprocity to n = w″ directly: (x/π)₃ = (w″/π)₃ = (π/w″)₃.
(b) Split q: complex conjugation σ maps 𝔮 to 𝔮̄ and acts on μ₃ by inversion, so (π/𝔮̄)₃ = σ((π̄/𝔮)₃) = (π̄/𝔮)₃⁻¹ and
(π/q)₃ = ((π/π̄)/𝔮)₃; on T_q (where t̄ ≡ t⁻¹) this is t ↦ (t/𝔮)₃(t⁻¹/𝔮)₃⁻¹ = (t/𝔮)₃², non-trivial since T_q ≅ F_q^× via
reduction mod 𝔮. Inert q: ℤ[ω]/q = F_{q²}, Frobenius = conjugation, so π^q ≡ π̄ and (π/q)₃ ≡ π^{(q²−1)/3} =
(π^{q−1})^{(q+1)/3} ≡ θ^{−(q+1)/3}; T_q is cyclic of order q + 1 ≡ 0 (3), so t ↦ t^{(q+1)/3} is onto μ₃. (c) Combine. ∎

**Lemma 4.3 (complete-sum cancellation: the Type I input).** Let m > 1 be squarefree, gcd(m, 3) = 1, c ∈ (ℤ/m)^×, and
F_c := {α ∈ (ℤ[ω]/m)^× : N α ≡ c (mod m)}. Then Σ_{α∈F_c} (α/m)₃ = 0; equivalently, over the norm fibre the angle
character Ξ_m is equidistributed in μ₃. (Same statement for (·/m)₄ in ℤ[i], m odd squarefree.)
*Proof.* By CRT it suffices that each prime factor q gives a vanishing factor. The norm map is onto F_q^× (split:
(a, b) ↦ ab; inert: F_{q²}^× → F_q^×), so F_{c,q} = α₀T_q and Σ_{t∈T_q}(α₀t/q)₃ = (α₀/q)₃Σ_{t∈T_q}Ξ_q(t) = 0 by (b).
For ℤ[i]: (t/q)₄ on T_q is the quadratic character of the cyclic group T_q (split: (t/𝔮)₄² ; inert: t^{−(q+1)/2}), non-
trivial. ∎
*Reading.* This is the identity a FIMR-type Type I estimate would exploit (sum the symbol over the argument at fixed
modulus): at *density* level the order-k class is free. Lemma 4.5 shows the exact shell never offers such a sum.

**Lemma 4.4 (quartic dictionary, 2-adic layer; the Rédei bits).** Let ℓ ≡ 1 (4), π = a + bi ∈ ℤ[i] primary (b even,
a + b ≡ 1 mod 4), N π = ℓ, θ = π/π̄, p = ρρ̄ (ρ primary). Then
  (a) (x/π)₄ = ε(π, w)·(π/p)₄·(π/w)₄⁻¹ with ε(π, w) = (−1/π)₄(2/π)₄⁻¹·[(−1/π)₄⁻¹ if w ≡ 3 (4)], a unit depending only on
      π mod 16 and w mod 4; (π/q)₄ = Ξ_q(θ) (anticyclotomic, as in 4.2(b)) for every odd prime q ∤ ℓ;
  (b) (π/p)₄ = (ℓ/ρ)₄⁻¹·(π/ρ)₂: the p-part is a quartic Dirichlet character mod p of u = ℓ ("p in the conductor", in the
      variable u) times the **Rédei bit** (π/ρ)₂ ∈ {±1} — the Frobenius of (ρ) in ℚ(i, √π), a field depending only on u;
  (c) for a split prime q = κκ̄ dividing w (so ℓ ≡ −p mod q), (π/q)₄ = (π/κ)₂·(−p/κ)₄⁻¹: again a Rédei bit (Frobenius of κ
      in ℚ(i, √π)) times a quartic symbol of the fixed p at κ.
*Proof.* (a) As 4.2(a), with quartic reciprocity ((α/β)₄ = (β/α)₄(−1)^{((Nα−1)/4)((Nβ−1)/4)} for primary α, β of coprime
odd norms; Ireland–Rosen Ch. 9 §9, Thm 2): for p ≡ 1 (4) the two signs for ρ, ρ̄ cancel, so (p/π)₄ = (π/p)₄; an odd rational
n ≡ 1 (4) is primary with (n² − 1)/4 even, so (n/π)₄ = (π/n)₄, and n ≡ 3 (4) uses −n. The anticyclotomic form is proved as
in 4.2(b) ((π/q)₄ ≡ (π̄/π)^{(q+1)/4} for inert q ≡ 3 (4)). (b) (π/ρ̄)₄ = (π̄/ρ)₄⁻¹ (conjugation), (π/ρ)₄(π̄/ρ)₄ = (ℓ/ρ)₄, and
(π/ρ)₄² = (π/ρ)₂, so (π/p)₄ = (π/ρ)₄(π̄/ρ)₄⁻¹ = (π/ρ)₄²(ℓ/ρ)₄⁻¹. (c) Same computation with κ in place of ρ and
ℓ ≡ −p (mod κ). ∎
*CERTIFIED check* (`scripts/z54_exactspin_cubic_check.py`, `data/z54/exactspin/dict_check.txt`): on all shell points with
prime u of 24 primes p ≡ 1 (4) in [10⁹, 2·10¹²] (both classes of p mod 3 and mod 8): 3 817 cubic points, 0 mismatches in
4.2(a) (computed from the definitions: residue symbols mod the primes of p·2w₁, and (x/π)₃ = x^{(ℓ−1)/3} with
ω ≡ −a/b mod π), 0 mismatches of the anticyclotomic forms 4.2(b), (3/π)₃ a function of π mod 9 on all points;
7 822 quartic points, ε(π, w) a function of (π mod 16, w mod 4) on every point.

**Lemma 4.5 (fibre degeneracy on the (★) support).** (a) For any odd n ≥ 3 and any (★) triple written in trial form
d := 4uC − 1 | n + u (FRONTIER §2.1), d ≥ 4u − 1 > u. Hence for a fixed value of the level divisor d, at most one u
(the least positive residue of −n mod d) occurs, and the elements π of ℤ[ω] (resp. ℤ[i]) of norm u number ≤ 6τ(u)
(resp. 4τ(u)). (b) On the Thm U shell 𝔖 the same holds with w or w″ as the fixed modulus (w > Y ≥ U₁, w″ > 4U₁;
GENUSX Lemma 4.1), for all shell points, not only hits. (c) For fixed u (fixed π), the moduli w, w″ range over divisors of
the single integer p + u.
*Proof.* (a) d ≡ −1 (mod 4u), d > 0 ⇒ d ≥ 4u − 1; d | n + u with 1 ≤ u < d fixes u ≡ −n (mod d); r₂-type bound
#{π : N π = u} ≤ 6τ(u) for ℤ[ω] (4τ(u) for ℤ[i]). (b), (c): GENUSX Lemma 4.1. ∎
*Reading.* Lemma 4.3 needs the argument π to run over a whole norm fibre (or a box/progression long compared with the
modulus); on the (★) support every fixed-modulus fibre is the representation set of one integer, and every fixed-argument
fibre is a divisor set of one integer. So the exact layer contains no Type I sum in any of the variables w, w″, u, π.

**Proposition 4.6 (the order-k layer as twisted shrinking-disc equidistribution of 2-dimensional roots; PROVED
identity).** Let Δ₃^{pr} be the prime-u part of Δ₃ restricted to shell points with 3 ∤ w″. For an odd c ∤ 3 put
𝔑(c) := {α ∈ ℤ[ω]/c : N α ≡ −p (mod c)} (2-dimensional "roots" of the norm form; |𝔑(c)| ≍ c). For α ∈ 𝔑(c) let
Φ_c(α) := 1 if the coset α + cℤ[ω] contains a primary prime π with ℓ := N π ∈ 𝒰 prime, ℓ ≡ 1 (3), ℓ ≡ −p (mod 2c),
w := (p + ℓ)/(2c) ∈ (Y, X] ∩ 𝒮_ℓ, and c ≡ 3 (4) — then that π is unique (|π|² ≤ U₁ < c²/4) — and Φ_c(α) := 0 otherwise; put
ν(α) := 2/(N π − 1) on Φ_c = 1. Then
  Δ₃^{pr} = Σ_c Σ_{α∈𝔑(c)} Φ_c(α)ν(α)·Re (α/c)₃,  and  Σ_{α∈𝔑(c)} (α/c)₃ = 0 for every c > 1.
So Δ₃^{pr} is the covariance, fibre by fibre, between the cubic symbol (constant on cosets, mean 0 on each fibre by
Lemma 4.3) and the indicator that the coset meets the disc |α| ≤ √U₁ in a window prime: in torus coordinates α/c ∈ ℂ/ℤ[ω]
this is equidistribution of the roots of N α ≡ −p (mod c), *twisted by the cubic symbol*, in a disc of radius √U₁/c
around 0 — a Hooley/Duke–Friedlander–Iwaniec-type statement for the fixed polynomial N(α) + p (B6-compatible: p fixed,
the modulus c free), at a shrinking scale where each fibre meets the disc O(1) times on average (|𝔑(c)|·U₁/c² ≍ U₁/c < 1).
*Proof.* Lemma 4.2(a) with 3 ∤ w″ gives (x/π)₃ = (π/c)₃ with c = w″, constant on π + cℤ[ω]; the two primary primes above
ℓ (π and π̄) give the same Re; the shell point's Δ₃ term is 2·(ℓ − 1)⁻¹·2Re(x/π)₃ = Σ_{π,π̄} ν Re(·). Uniqueness: two
elements of a coset differ by cβ, |cβ| ≥ c > 2√U₁. Vanishing: Lemma 4.3 with m = c. ∎
*The full class event is not of this form.* In the same coordinates the exact event is 1[N π | c + 1] for the *small
representative* π of the coset: it changes along the coset (N(π + cβ) ≡ N π mod c only), so it is not a function on
𝔑(c); by Lemma 4.1 at prime ℓ it is the order-(ℓ − 1) Kummer symbol, living in ℚ(ζ_{ℓ−1}), a field of degree
φ(ℓ − 1) → ∞ that depends on u.

## 5. Matching against the spin theorems (Q2): hypotheses, Type I/II, uniformity, exponent deficit

Sources verified from the papers (abstract/theorem statements; `data/z54/exactspin/lit_spins.md`, research subagent):
* **FIMR** (Friedlander–Iwaniec–Mazur–Rubin, *Invent. Math.* 193 (2013) 697–749, arXiv:1110.6331), Thm 1.1: K/ℚ cyclic of
  degree n ≥ 3, totally real, totally positive units are squares; spin(σ, 𝔞) = (α/𝔞^σ) for 𝔞 = (α), α ≫ 0; the sum is over
  principal prime ideals N𝔭 ≤ x of the *fixed* field: Σ spin(σ, 𝔭) ≪ x^{1−ν+ε}, ν = δ/(2n(12n + 1)), under Conjecture C_n
  (short character sums, δ ≤ 2/n); unconditional for n = 3 (δ = 1/48). Type I: Prop 6.1 (ideals 𝔞 ≡ 0 mod 𝔪 in a box);
  Type II: Prop 7.1 (bilinear, via spin(𝔞𝔟) = spin(𝔞)spin(𝔟)·(cross symbols)); combination Prop 5.2.
* **Koymans–Milovic**: Compositio 2019 (arXiv:1611.10337; fixed dihedral field ℚ(ζ₈, √(1+i)), conditional on a short-sum
  conjecture); *Duke* 170 (2021) (arXiv:1809.09597; joint spins over prime ideals of a fixed Galois K, S ∌ σ⁻¹ for σ ∈ S,
  under C_{|S|n}); IMRN 2019 (arXiv:1705.05505; sum over rational primes p ≤ X of the 16-rank sign, X^{1−1/3200}).
* **Large sieves for higher symbols**: Heath-Brown's cubic large sieve (as restated in Blomer–Goldmakher–Louvel,
  arXiv:1112.1650, (1.2)): Σ_{Nm≤M}|Σ_{Nn≤N} a_n (n/m)₃|² ≪ (M + N + (MN)^{2/3})(MN)^ε Σ|a_n|² (squarefree, primary);
  Gao–Zhao (arXiv:1101.3646) Thm 1.1, quartic, (MN)^{3/4} in place of (MN)^{2/3}; BGL Thm 1.3 for n-th order Hecke characters.
* **Koymans–Pagano** (JEMS 2022): averages over a family of cyclic fields (B6: not applicable at fixed p).

| requirement | FIMR / KM | exact layer (this memo) | status |
|---|---|---|---|
| fixed field of bounded degree | yes (K, or ℚ(ζ_k)) | order k: ℚ(ζ_k) fixed ✓; full class at prime u: ℚ(ζ_{u−1}), degree φ(u−1) → ∞ (Prop 4.6 end, Lemma 4.1) | ✗ for the layer, ✓ per order |
| p-dependence through a fixed-field Frobenius | — | (π_u/p)_k = Frob in ℚ(ζ_k, p^{1/k}) (Lemmas 4.2, 4.4) | ✓ (identified) |
| free variable runs over all ideals / a box | prime ideals of K | the shell: one π per modulus, divisor sets per argument (Lemma 4.5) | ✗ |
| Type I (fixed modulus, argument in a box/progression) | Prop 6.1 | complete sums vanish (Lemma 4.3), but every fixed-modulus fibre has ≤ 6τ(u) points | ✗ |
| Type II (twisted multiplicativity in the free variable) | Prop 7.1 | modulus u = r_w is the residual −p mod w; r_{w₁w₂} is the CRT lift, not a function of the factors' data | ✗ (Assessment) |
| uniformity in the order k | none (ν ≍ n⁻³) | needed up to λ(u) ≥ U₀^{1−o(1)} on most u (Lemma 3.3) | ✗ |

**Corollary 5.1 (what spin technology can and cannot reach here; PROVED part / Assessment part).** *PROVED:* (i) on the
exact shell no Type I sum exists in any of w, w″, u, π (Lemma 4.5); (ii) any input that controls only characters of order
dividing a fixed K determines the class event only on the finite menu 𝒰_K (Lemma 3.3), so (Sp-2) + (Sp-o) cannot follow
from finitely many fixed-order statements (Sp-k). *Assessment:* (iii) the published spin exponents decay like n⁻³ in the
degree n = φ(k) (FIMR's ν ≤ 1/(n²(12n+1)) when δ ≤ 2/n), so even with the missing Type I/II structure they would be
non-trivial only for φ(k) ≲ (log x)^{1/3}, while the class event at prime u needs order u − 1.

**Proposition 5.2 (exponent deficit of the twisted-root Fourier route; PROVED, scoped).** In the coordinates of Prop 4.6
take a dyadic block c ∈ (C, 2C], gcd(c, 6) = 1, and a smooth bump f on the torus 𝕋 := ℂ/ℤ[ω] supported in the disc of
radius r := C^{θ−1}, θ ∈ (0, 1/2) (on the (★) support θ ≤ 1/2 is forced: u < c/4 by Lemma 4.5(a), so the disc of radius
√U₁/c has U₁ < C). Put N_f(C) := Σ_c Σ_{α∈𝔑(c)} f(α/c) and D_f(C) := Σ_c Σ_{α∈𝔑(c)} f(α/c)(α/c)₃. For squarefree c,
|𝔑(c)| = ∏_{q|c}(q − χ₋₃(q)) (q − 1 points on a split fibre, q + 1 on an inert one), so the expected size of N_f(C) is
≍ C²r² (up to C^{o(1)} factors). Suppose a twisted Weyl bound with absolute values in c:
  (W) Σ_{C<c≤2C} |Σ_{α∈𝔑(c)} (α/c)₃ e(⟨m, α/c⟩)| ≪ C^{2−δ}|m|^A  for all 0 ≠ m in the dual lattice.
Then, expanding f in Fourier series on 𝕋 and using the triangle inequality in m (f̂(0)·(m = 0 term) vanishes exactly
by Lemma 4.3; |f̂(m)| ≪_B r²(1 + r|m|)^{−B}):
  |D_f(C)| ≪ C^{2−δ}·r²Σ_{m≠0}(1 + r|m|)^{−B}|m|^A ≪ C^{2−δ}r^{−A},  so |D_f(C)|/(C²r²) ≪ C^{(1−θ)(2+A)−δ}.
This is o(1) only if δ > (1 − θ)(2 + A) > 1 + A/2 ≥ 1, i.e. (W) must beat square-root cancellation (the double sum has
≍ C² unimodular terms: square-root cancellation in the whole double sum is δ = 1, per-modulus square-root cancellation of
the complete inner sums is δ = 1/2). So the Fourier/Weyl route to (Sp-3) on the (★) support fails for *every* (W) with at most
square-root cancellation — the two-dimensional, cubic-twisted analogue of the closed Erdős–Turán/Fejér item of FRONTIER §7.1
(square-root input reproduces the trivial bound), here forced by the shrinking scale r = C^{θ−1}. It would in any case reach
only the fixed order k = 3 (Cor 5.1(ii)). *Proof.* Σ_{m≠0}(1 + r|m|)^{−B}|m|^A ≍ r^{−2−A} for B > A + 2 (lattice-point count
in dyadic shells). *Scope:* triangle inequality over m and over c-blocks; signed combinations over m, other smoothings, and
non-Fourier methods are not covered; the prime/window factors of Φ_c (Prop 4.6) are not smooth and are not treated.

**Escape hatches left open (Assessment).**
1. *Hermitian / metaplectic form.* With H := [[2w, π], [π̄, w″]], det H = 2ww″ − N π = p: shell points with u a norm are
   integral binary hermitian forms over ℤ[ω] (ℤ[i]) of determinant p in a thin region; the order-k twist (π/w″)_k =
   (H₁₂/H₂₂)_k is invariant under H ↦ gHg*, g = [[1, t], [0, 1]] (H₂₂ fixed, H₁₂ ↦ H₁₂ + t H₂₂). This is Kubota-symbol
   structure (cubic/quartic metaplectic covers of SL₂ over ℤ[ω], ℤ[i]); spectral methods there (Patterson, Heath-Brown–
   Patterson) average over large regions. Not developed; any result would again be per fixed order (Cor 5.1(ii)).
2. *Joint spins of the prime factors of w″.* By Lemma 4.4(c) the quartic layer at prime u is a product, over the split
   prime factors κ of w, of Rédei bits (π_u/κ)₂ times quartic symbols (−p/κ)₄ — a multiplicative function of w twisted by a
   field ℚ(i, √π_u) that depends only on u. At fixed u this is a twisted divisor sum of p + u (B2); across u the field moves.
   A joint-spin theorem with the field varying in a family indexed by u ≤ p^{α₁} (Koymans–Pagano style, but at fixed p)
   is not available.
3. *Dual windows.* If the class modulus u is the long variable (u ≫ w), Lemma 4.3 applies in the variable π with w fixed,
   and bounded-order layers become density-level (provable in principle with a Burgess bound for Hecke characters of
   conductor ≍ pw over ℤ[ω] — not verified in the literature check: lit_spins.md §5). But then the exact condition is
   u | p + 2w, divisors of one integer again: exactness migrates to the summed modulus.

## 6. Falsifier F: are the spin layers biased at fixed p? (EVIDENCE; identities CERTIFIED)

**Design.** If a spin *law* existed (a pointwise or statistical bias of the class of w″ inside its genus coset forced by
higher reciprocity), the layers S₂, S_o, Δ_k would have non-zero mean in units of their random-model standard deviation,
and a cancellation theorem (Sp-k) would be false or need a main term. Engine `scripts/z54_exactspin_engine.c` (compile
`gcc -O2 -o /tmp/z54_exactspin_eng scripts/z54_exactspin_engine.c -lm`): GENUSX's shell enumeration; per shell point with
w″ ≡ 3 (4) it computes R, G, S₂, S_o (Lemma 3.1) and Δ_k for k ∈ {3, …, 13, 16, 20, 24} (Lemma 3.2), plus model variances:
S₂, S_o with x uniform in its actual G²-coset (genus-conditioned; V₂ = Σ 4·|A_o|⁻¹|A₂²|⁻¹(1 − |A₂²|⁻¹),
V_o = Σ 4·|A₂²|⁻²|A_o|⁻¹(1 − |A_o|⁻¹) over genus points), Δ_k with x uniform on G (V_k = Σ 4N_k(u)/φ(u)², N_k = #{ord ψ = k}).
z := layer/√V. Window: GENUSX standard (U₀, U₁, Y, X) = (p^{1/12}, p^{1/3}/2, p^{1/3}, p^{2/3}/4) — a proxy window, outside
Thm X's hypotheses (as in GENUSX §5). Commands (from `data/z54/exactspin/`):
`ENG=/tmp/z54_exactspin_eng python3 ../../../scripts/z54_exactspin_run.py layers.tsv TAG @samples/TAG.txt` for TAG in
rand_1e9 … rand_1e14, nearsq_1e10/12/14, squares_1e10/12/14 (samples: `uv run --with sympy python
scripts/z54_exactspin_samples.py`, seed 5400: random primes p ≡ 1 (24) in [10^k, 2·10^k]; near-squares p = m² + k₀,
k₀ ∈ {4, 16, 36, 64, 100}; odd squares m²), then `uv run --with numpy python scripts/z54_exactspin_stats.py layers.tsv`
(→ `stats.txt`) and `scripts/z54_exactspin_table.py` (→ `table.md`); hard primes → `layers_hard.tsv`. Total run time
≈ 2 min for 9 800 integers.

**Identity checks (CERTIFIED on all runs).** R − G = S₂ + S_o to 10⁻⁶ on every integer; the class/2-adic split
(x = 1 ⟺ x₂ = 1 and x_o = 1) on every shell point (0 mismatches); at the 600 odd squares R = G = S₂ = S_o = 0 and
Δ_k = 0 for every k with 4 | k (Lemmas 3.1, 3.2), while Δ₃, Δ₅, Δ₆, Δ₇ are non-zero (mean |Δ₃| = 0.24, 0.26, 0.21 at
10¹⁰, 10¹², 10¹⁴; Δ₆ = −Δ₃ exactly at squares, since at non-squares the d = 6, 2 terms of Lemma 3.2 vanish). The spin
dictionary (Lemmas 4.2, 4.4) is checked separately (§4).

**Main table** (`table.md`):

| sample | N | mean G/log²p | mean R / mean G | P(R=0) | var S₂ / var(R−G) | var S_o / var(R−G) | z(S₂) mean, sd | z(S_o) mean, sd | z(R−G) mean, sd | max_k mean z(Δ_k)/se | sd z(Δ_k) | orders ≤ 24 share (model / emp.) |
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

(The max over the 14 orders of |mean z|/se is a multiple-comparison statistic: 14 × 9 = 126 tests; the largest, 2.9 at
k = 24, 10¹², is within the expected range.)

**Reading (EVIDENCE).**
(a) *No spin law detected.* Every layer — 2-adic S₂, odd S_o, and each exact order k ≤ 24 — has z-scores with sd 0.92–1.12
and means within ≈ 0.06 of 0 (individually ≤ 2.9 standard errors before multiple-comparison correction) at 10⁹–10¹⁴, for
random primes and near-squares alike: at fixed p the class of the level divisor inside its genus coset behaves like an
independent uniform draw at every order tested. This is the *equidistribution* half of a spin theorem, observed; it does not
supply the missing Type I/II structure (§4–5).
(b) *The class-within-genus variance splits evenly:* var S₂ ≈ var S_o ≈ ½ var(R − G) (cov ≈ 0), as the uniform model
predicts for 𝒰 (where |A₂²| and |A_o| are comparable on average). Bounded orders carry a decreasing share (orders ≤ 24:
46 % → 23 % from 10⁹ to 10¹⁴, model 43 % → 21 %), as Lemma 3.3(b) predicts.
(c) *A small offset.* Pooled over the 8 600 random primes, mean z(R − G) = +0.0325 ± 0.0108 (3.0 se); mean R/mean G =
1.006–1.032. Its source is not resolved here. Candidate (not tested): the finite-size density offset T_u = M^cls_𝔉 − M_𝔉,
which GENUSX measured directly at 10¹⁰ as M^cls/M ≈ 1.01 in this window. It has the helpful sign.
(d) *(★)-zero primes* (`layers_hard.tsv`; R = 0, so R − G = −G = S₂ + S_o): the deficit splits differently from prime to
prime — e.g. (S₂, S_o) = (−1.50, +0.33) at 712321, (0, −1.16) at 5212561, (−0.75, −1.15) at 8813281, (−1.00, −0.33) at 329617:
the failures are not localised in one spin layer.

## 7. The four FRONTIER §4 hard screens (Assessment, except where labelled)

1. **T1 (odd squares): consistent, and located.** S₂ and S_o vanish pointwise at odd squares (Lemma 3.1, PROVED; CERTIFIED
   on 600 squares), but only because the genus does; the exact odd-order layers Δ_k (4 ∤ k) do *not* vanish at squares
   (Lemma 3.2; CERTIFIED: mean |Δ₃| ≈ 0.21–0.26). In the dictionary the p-part (π_u/p)_k becomes (π_u/m)_k² at n = m² and
   nothing degenerates. So a spin-cancellation statement is T1-blind: the square-sensitive step of any proof along these
   lines must remain Thm U's genus step (ηχ_{−4up} non-principal because p | conductor), and the spin input would only have
   to bound S₂, S_o. That division of labour is consistent; it also means spins cannot be the step that uses primality.
2. **8/131: not applicable** (structure/identity statements about the (★) family, not a solution mechanism).
3. **Tied modulus (B2): fails — this is where the lane ends.** The dictionary moves the tie into the coupling factor
   (π_{r_w}/2w)_k = Ξ_{2w}(θ_{r_w}) — the angle of the prime above the residual r_w = −p mod w, read modulo w. Every
   fixed-modulus fibre is a single integer's representation set and every fixed-argument fibre a single integer's divisor
   set (Lemma 4.5); the full class needs order u − 1, i.e. a field ℚ(ζ_{u−1}) of unbounded degree (Lemmas 3.3, 4.1).
4. **Fixed p (B6): passes.** Every statement is at fixed p; the free variables are w, w″, u, π and the root α mod c. Note
   that the earlier dismissal of spins as "averages over the prime" (GENUSREDEI §7.4, bsB_redei_oddpart) is not the
   operative obstruction here: FIMR and Koymans–Milovic sum over prime ideals of a fixed field, which would be a fixed-p
   operation in our setting. The operative obstruction is the fibre structure (screen 3).

## 8. Verdict, proposed FRONTIER §7 text, bottom line

**Verdict: narrowed** (no bound on T_uw; the spin route is mapped and its sub-routes are closed as scoped theorems).
* *Answered (PROVED, CERTIFIED check):* Q1 is answered **yes per fixed order, no for the layer**. At prime u, the order-k
  class of the level divisor is the Kummer symbol of the prime above u in ℚ(ζ_k, (−p/2w)^{1/k}) (Lemma 4.1). It factors as
  (a) the Frobenius of π_u in the **Kummer field ℚ(ζ_k, p^{1/k})** — the field depending only on p, a function of (p, u) —
  times (b) an anticyclotomic character of the *angle* π_u/π̄_u modulo 2w (Lemmas 4.2, 4.4; cubic case exact incl. the
  ramified prime 3). For k = 4 the p-part is a quartic character mod p of u times a Rédei bit (π_u/ρ_p)₂, and each split prime
  of w contributes a Rédei bit (π_u/κ)₂ from the field ℚ(i, √π_u), which depends only on u. The full class at prime u is the
  order-(u − 1) symbol, from a field of unbounded degree.
* *Decomposition (PROVED):* R_𝔉 − G_𝔉 = S₂ + S_o (2-adic Rédei/quartic layer + odd cubic/quintic layer). Both vanish
  pointwise off the genus, hence at odd squares (Lemma 3.1); the exact odd-order layers are T1-blind (Lemma 3.2).
* *Narrowed (PROVED, scoped):*
  * Fixed orders form a finite menu: they decide the class event only for λ(u) | K, a finite set of u. Their variance share is
    ≤ K^{ω(u)}/φ(u) per point (Lemma 3.3).
  * The density-level (Type I) cancellation exists: complete sums over a norm fibre vanish (Lemma 4.3). But the (★) support
    offers no such sum. Every (★) event has level divisor ≥ 4u − 1 > u, so each fixed-modulus fibre is one integer's
    representation set (Lemma 4.5).
  * The order-3 layer is a cubic-twisted shrinking-disc equidistribution problem for the 2-dimensional roots of
    N(α) ≡ −p (mod c) (Prop 4.6). Its Fourier/Weyl route needs better than square-root cancellation (δ > (1 − θ)(2 + A) > 1)
    at the scale forced by the (★) support (Prop 5.2).
  * Hypothesis table for FIMR / Koymans–Milovic / cubic and quartic large sieves (§5): field ✓ per order; Type I ✗;
    Type II ✗ (Assessment); uniformity in the order ✗.
* *EVIDENCE:* at 10⁹–10¹⁴ (8 600 random primes, 600 near-squares, 600 squares) every spin layer is unbiased at the ≈ 0.06σ
  level, with z-sd ≈ 1 (no spin law). S₂ and S_o each carry ≈ ½ of var(R − G). Orders ≤ 24 carry 46 % → 23 % of it. A
  small positive offset of R − G (+0.03σ, pooled) is unexplained, possibly finite-size T_u.
* *What survives (Assessment):* (i) a fixed-p theory of spins on a *moving* family of fields ℚ(ζ_{u−1}) or ℚ(i, √π_u),
  u ≤ p^{α₁} — no such theorem is known; (ii) signed/non-Fourier methods for the twisted 2-dimensional root problem, e.g.
  metaplectic (Kubota) spectral theory on hermitian forms of determinant p (§5 hatch 1), which would still be per fixed
  order; (iii) Type II structure in the residual map w ↦ r_w (no factorisation found; EXACTSUM's exponential-sum angle
  attacks the same map analytically).

*Proposed FRONTIER §7 text* (append to item 3, after the GENUSX entry):
> *(z54, `Z54_EXACTSPIN.md`, internal review.)* Spins / Kummer / Rédei symbols on the exact class layer.
> * R_𝔉 − G_𝔉 = S₂ + S_o (2-adic quartic/Rédei layer + odd cubic layer). Both vanish pointwise at odd squares, but only
>   via the genus; the exact odd-order layers are T1-blind (PROVED).
> * Dictionary (PROVED; CERTIFIED on 3 817 / 7 822 shell points): at prime u the order-k class of the level divisor is the
>   Frobenius of π_u in ℚ(ζ_k, (−p/2w)^{1/k}). This equals [Frobenius of π_u in the Kummer field ℚ(ζ_k, p^{1/k}), a field
>   depending only on p] × [an anticyclotomic character of the angle π_u/π̄_u modulo 2w]. For k = 4 the factors are a
>   quartic character of u mod p and Rédei bits (π_u/ρ_p)₂, (π_u/κ)₂ for κ | w.
> * Scoped no-gos (PROVED):
>   * Complete sums over norm fibres vanish, but every (★) event has level divisor > u, so no Type I sum exists on the
>     support in any variable.
>   * Fixed orders decide the class event only on a finite menu of u.
>   * The order-3 layer is a cubic-twisted equidistribution problem for roots of N(α) ≡ −p (mod c) in discs of radius
>     c^{θ−1}; its Fourier route needs better than square-root cancellation.
> * FIMR / Koymans–Milovic sum over prime ideals of a fixed field (so B6 is not the obstruction). They fail here on Type
>   I/II structure and on uniformity in the order: the full class needs ℚ(ζ_{u−1}).
> * EVIDENCE (10⁹–10¹⁴): no spin bias at any order ≤ 24 (z-means ≲ 0.06, sd ≈ 1). S₂ and S_o each carry ≈ ½ of
>   var(R − G).

**Bottom line.** The class of the level divisor inside its genus coset does have a precise spin/Kummer/Rédei description
at every fixed order. At prime u, its order-k part is the Kummer symbol of the prime above u, factored as a Frobenius in the
field ℚ(ζ_k, p^{1/k}), which depends only on p, times an anticyclotomic character of that prime's angle modulo the free
variable w. Numerically, every such layer is unbiased at fixed p, up to 10¹⁴. But the spin theorems cannot be brought to
bear, for three proved reasons:
* the (★) support offers no Type I sum in any variable, because the level divisor always exceeds the class modulus;
* fixed orders see the class only on a finite menu of u, while the full class lives in ℚ(ζ_{u−1}), a field of unbounded
  degree;
* the natural Fourier route for the cubic layer would need better than square-root cancellation.
B6 is not the obstruction: FIMR-type sums run over a fixed field and would be fixed-p operations. The obstruction is again
the tied modulus, now visible as the residual map w ↦ π_{r_w}. **ES remains OPEN.**

## 9. Review log
(pending: internal hostile review; cross-model review to follow.)
