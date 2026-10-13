# bsB_rayclass_norm_pullback — the ray-class escape of WR Remark 10.4 is pulled back from ℚ (O175)

**ES is not solved here.** Labels as in DISCOVERIES.md.

## Idea
WR Remark 10.4: ray class groups Cl_(t)(K), K = ℚ(√−tp), *do* see the full Type I condition N𝔪 ≡ −1 (t) on the
divisor hypercube of 1 + √−tp. Hope: Hecke Grössencharacters of Cl_(t)(K), their L-functions, a Chebotarev
theorem in the ray class field, or the class-group structure of K could force the hypercube into the class.
Make precise which characters of Cl_(t)(K) the condition actually uses.

## Results (PROVED, elementary + standard CFT)
Let t ≡ 3 (4) squarefree, p ≡ 1 (4) prime, p ∤ t, K = ℚ(√−tp) (so d_K = −tp), ω = (1 + √−tp)/2 ∈ O_K (primitive:
no rational prime divides ω), N := Nω = (tp + 1)/4. G := Cl_(t)(K), σ = complex conjugation.
1. **Hypercube = divisor lattice of N.** Every prime ℓ | N splits in K (−tp ≡ 1 mod ℓ, a square), and by
   primitivity exactly one prime above ℓ divides (ω), to the full power. So 𝔪 ↦ N𝔪 is a bijection
   {ideals 𝔪 | (ω)} → {positive d | N}. (Standard.)
2. **Only norm-pulled-back characters enter.** The event "N𝔪 ≡ −1 (t)" is measurable for N: G → (ℤ/t)^*, so
   `#{𝔪 | ω : N𝔪 ≡ −1 (t)} = φ(t)⁻¹ Σ_{χ mod t} χ̄(−1) Σ_{d | N} χ(d)`.
   Characters of G not of the form χ∘N contribute nothing to any detector of the event. For ψ = χ∘N_{K/ℚ},
   `L(s, ψ) = L(s, χ) L(s, χχ_K)` (induction), and θ_ψ is an **Eisenstein** series. So every Grössencharacter
   L-function, Chebotarev density or equidistribution statement in the ray class field that bears on the
   hypercube event is a statement about Dirichlet characters mod t and mod 4tp; the cuspidal (CM) Hecke
   characters — the only genuinely "K-arithmetic" ones — do not enter. The only K-datum left is χ_K = (−tp/·).
3. **Where the sign lives in G.** [𝔞]^{1+σ} = [(N𝔞)] is trivial in G iff ±N𝔞 ≡ 1 (t) (units ±1). So the
   sign-blind set (N𝔪 ≡ ±1) is the hypercube ∩ G[1+σ], and on G[1+σ] the norm is a *quadratic character*
   ν: G[1+σ] → {±1}. Genus product formula (χ_{d_K} = ∏ of prime-discriminant characters is 1 on norms):
   `(N𝔞/p) = (N𝔞/t)` (Jacobi), so **ν = χ_p∘(G → Cl(K)) on G[1+σ]**: the ES sign is the genus character at p
   restricted to the anti-invariant part. GI Prop 4.1 is exactly this. Internal group operations of G (like
   1 + σ) lose the sign (the ±1 ambiguity of generators); this is the ray-class form of "X₁(t) identifies P
   with −P" (GI Prop 2.1 reading).
Checked: `scripts/bsB_genus_pullback.py 200000` — 9859 random norms m ≡ ±1 (t), 0 violations of (m/p) = ±1.

## Literature
Neukirch, *Algebraic Number Theory*, VI.6–VII.10 (ray class groups, Hecke L-functions; L(s, χ∘N) =
L(s, χ)L(s, χχ_K) by induction); Cox, *Primes of the form x² + ny²*, §§3, 8–9 (genus theory, ring class fields).

## Barrier screen
* Item 2 is a proved collapse of the "Hecke L-function / ray-class Chebotarev at fixed p" sub-idea of the brief:
  at fixed (t, p) the hypercube is one integer's divisor set, character expansion = B2's divisor-in-class sum.
* Iteration 1 (vary t at fixed p): the fields K_t = ℚ(√−tp) all differ; the only uniform object is the product
  ∏_t over Dirichlet data mod t — no common field, B6/H-A.
* Iteration 2 (use characters NOT factoring through N, e.g. a cusp form θ_ψ and its coefficient at N): they
  detect the *ideal class* of 𝔪 in G/ker-ish directions orthogonal to the event, so by item 2 their
  contribution to the count is identically 0; a mechanism using them would have to be "class ⇒ norm", which
  WR Prop 10.3 shows is genus-shadow only. Dead.
  (R175 repair, D10: Prop 10.3 is the wrong citation. It concerns Cl(O), where norms mod ℓ are class invariants only
  up to squares; in G = Cl_(t)(K) the norm mod t *is* a class invariant (Remark 10.4). The correct reason is the
  push-forward: the event depends only on the residues mod t of the prime factors of N, so anything a G-mechanism
  proves about it at fixed (t, p) pushes forward along N to a statement about those residues.)
* T1: at n = k² in GI Prop 4.1 (outside this memo's hypothesis p prime; R175 repair) the genus character at n is trivial on norms — ν ≡ +1 (consistent).

## Assessment
(R175 repair, D10, scope.) What is PROVED: (a) at fixed (t, p) the hypercube event is a function of the residues mod t
of the prime factors of N, so the *target* contains no ray-class information beyond N; (b) every *linear character
detector* of the event (Fourier expansion on G, Hecke L-functions, theta series, Chebotarev densities of the event)
uses only χ∘N. It is **not** a theorem about all ray-class *proof methods*. In particular, Chebotarev or
equidistribution arguments in the ray class fields of the varying K_p, used to force families of N to have prime
factors in prescribed classes, are only classified (B6/H-A, a barrier), not excluded. Read "pulled back from ℚ"
below with this scope.
PROVED (elementary/standard). Sharpens WR Remark 10.4 from "equivalent restatement" to "**pulled back from ℚ**:
the ray-class picture adds exactly one K-datum, the genus character χ_p on G[1+σ], which is the sign layer".
Promise 0/5 as a route; it closes the "Grössencharacter non-vanishing" sub-idea of the brief.
