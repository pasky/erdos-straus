# Z60_SIGNED — signed and multi-eigensystem automorphic proxies: in weight 3/2 the signed form of T1 is as strong as the support form (any mixture of quadratic nebentypus; in higher weight for one nebentypus only — mixtures escape, explicit counterexample off 𝔐); exponential objects with a dominant periodic term are square-blind; for multi-eigensystem support proxies cancellation is never the obstruction — what remains is a non-degeneracy of twisted central values plus a validity mechanism, neither supplied. Verdict: narrowed, no HOT LEAD

Status: z60 lane SIGNED (brief `z52bbriefs/z60_lanes.md` §SIGNED; common rules `z52bbriefs/z58_lanes.md`,
`z52bbriefs/z53_depth.md`). Internal; internally reviewed (§10). **ES is OPEN; nothing here proves or disproves ES, (★), (MS),
(MS⁺) or CONV-II.** Labels: PROVED / CONDITIONAL / CERTIFIED / EVIDENCE / CONJECTURE / Assessment.
Scripts `scripts/z60_signed_*`, data `data/z60/signed/`.

Notation as in `Z59_WALDS.md` / `Z58_TERNARY.md`: R(n) = #{(u,B,C) ∈ ℕ³ : 4uBC − u − B = n}; 𝔐 ⊂ (ℤ/840)^× Mordell's
classes; 𝒞₁(2N) = {n ≥ 1 : n ∈ ℤ_q^{×2} for every prime q | 2N}. A real arithmetic function g is a
* **support proxy** (valid) if g(n) ≠ 0 ⟹ R(n) ≥ 1 for all n ≡ 1 (4);
* **signed minorant** (valid) if g(n) > 0 ⟹ R(n) ≥ 1 for all n ≡ 1 (4) (AUTOMORPH's Q2′);
* **effective on a prime set 𝒫** if g(p) ≠ 0 (support) resp. g(p) > 0 (signed) for all sufficiently large p ∈ 𝒫.
Validity at odd squares (T1: R(m²) = 0) gives **(T1⁰)** g(m²) = 0 (support) resp. **(T1⁻)** g(m²) ≤ 0 (signed).

## 0. MANDATORY FALSIFIER TABLE (committed at checkpoint 1; final version, with the computed screens, in §7.3)

Mechanism examined: positivity at 𝔐-primes of a fixed-level automorphic proxy that is *signed* (minorant form) or a
*sum of several eigensystems* (cancellation), in half-integral weight (ternary/odd-rank theta class, any mixture of
nebentypus characters), plus exponentially growing (weakly holomorphic / Rademacher) objects.

| screen | behaviour |
|---|---|
| **F1 odd squares** | This is the whole content of §2–§3. The signed form only gives the *inequality* g(m²) ≤ 0, which in integral weight does **not** force anything (AUTOMORPH Prop B1: 5σ₂ − (2n²+3)τ is ≤ 0 at all odd squares, = p² − 1 > 0 at all primes). **Theorem S1/S2/S3 (PROVED rel. cited inputs):** in weight 3/2 the inequality at prime squares (S1) resp. at good squarefree-index squares (S2, any mixture of quadratic nebentypus), and in weight ≥ 5/2 for one nebentypus (S3), is as strong as the equality (mixtures in weight ≥ 5/2: false, §4.1): either the genus main term is *negative* on 𝒞₁ (then g(p) < 0 at every large prime of 𝒞₁, so the proxy is never positive there) or it vanishes on 𝒞₁ together with every t = 1 unary series and every Shimura component's anchor a(1), so on squarefree 𝒞₁ only Gauss-exceptional eigensystems survive (as in WALDS W1). Non-squareness is used at the t = 1 Shimura orbit (anchor) and at the genus density of m². |
| **F2 C-even (R₈)** | All negative statements (S1, S2, S4) are line-blind: they apply verbatim to R₈-minorants (R₈(m²) = 0), so nothing false is proved. The positive statement (Prop S5, reduction of effectiveness to a linear non-degeneracy) is an *equivalence* and applies to R₈ too; there it correctly requires R₈(p) ≥ 1 beyond the threshold on 𝒞₁, so any R₈-version must start above the 4 in-𝔐 R₈-zeros (largest 10 868 474 401). |
| **F3 composites** | Not used by S1/S2 (identities at squares + analytic bounds at primes). Squarefree composite zeros in 𝒞₁ enter the validity space exactly like prime zeros (S5: Z contains them). Mixed-nebentypus certificates (§5) use all known R-zero rows, composites included. |
| **F4 known zeros** | Nothing is proved positive. §6.1: at L = 168, 240, 280 every valid *mixed-ψ* proxy vanishes on 𝒞₁ ∩ [1, B] (CERTIFIED, all R-zero rows). §6.3: the two L = 420 lines vanishing at 5569, 9601 are, on numerical / BSD-dependent evidence, not prime-valid (102001, 712321, 1724209, 5212561, 8813281). |

## 1. Precise statements attacked

**(Q1, signed form in half-integral weight).** Let g be a real proxy in the ternary-theta class of TERNARY/WALDS
(g = Σ cᵢθ_{Lᵢ} + h ∈ M_{3/2}(Γ₀(4N), ψ), ψ quadratic, h cuspidal), or a finite sum of such over several ψ. If g is a
*valid signed minorant*, can it be effective on 𝒞₁(2N) ∩ primes (⊇ the 𝔐-primes for {3,5,7}-levels)?
TERNARY Thm F and WALDS W1 assume (T1⁰); AUTOMORPH B1–B2 show (T1⁻) does not kill integral-weight proxies; TERNARY §4.3
and WALDS (E-c) leave signed minorants and mixed nebentypus open. **Not closed before:** yes (TERNARY: "a signed
minorant (AUTOMORPH Q2′) is not addressed"; WALDS Remark (b): "Mixed-nebentypus combinations are not covered").

**(Q2, multi-eigensystem cancellation).** On squarefree t ∈ 𝒞₁, g(t) = Σ_{φ ∈ Φ_exc} g_φ(t) (W1). Each single line
vanishes at explicit 𝔐-primes (WALDS §6.1). Can a *sum* over several exceptional eigensystems be effective, and what
exactly must be controlled at a single p?

**(Q3, other fixed-level objects named in the brief).** Cosets / theta series with characteristics (WALDS E-b), higher
half-integral weight (E-d), weakly holomorphic / mock / Rademacher-type objects (AUTOMORPH E2), Fourier–Jacobi
coefficients — what survives (T1⁻)?

**(Q4)** What is left: the precise residual statement(s) and whether any of them is independent of (MS) (WALDS Prop W5).

## 2. Theorem S1 — the signed form of T1 is as strong as the support form (one nebentypus)

**Setting.** As TERNARY §3: N ≥ 1, ψ a quadratic character mod 4N, g = Σᵢ cᵢθ_{Lᵢ} + h ∈ M_{3/2}(Γ₀(4N), ψ) with real
Fourier coefficients, Lᵢ positive ternary lattices (so (H_δ) holds, TERNARY Remark F3), E := Σᵢ cᵢθ_{gen Lᵢ},
g = E + U + Σ_φ g_φ with U = Σ_{χ,t} κ_{χ,t}h_{χ,t} the unary part ((S3)) and g_φ ∈ S(4N, ψ, φ) the Waldspurger
eigencomponents ((W-P1); φ runs over finitely many weight-2 newforms of trivial character). c_φ := g_φ(1);
a_ℓ(φ) the Hecke eigenvalue, |a_ℓ(φ)| ≤ 2√ℓ; ε(ℓ) := ψ(ℓ)(−1/ℓ).

**Inputs** (beyond TERNARY (S1)–(S5) and WALDS (W-P1), (W-C2)):
* **(Sie)** Siegel: L(1, χ_D) ≫_ε |D|^{−ε} (ineffective).
* **(Duk)** Duke, Invent. Math. 92 (1988) 73–90, **Theorem 5** (§5; primary PDF read, §8): coefficients of spectral
  Maass forms of weight ±1/2 + 2ℓ satisfy ρ(n) ≪ |n|^{−2/7+ε} for squarefree n, and (p. 75–76) this "includes the
  interesting case of holomorphic cusp forms of weight 3/2"; in the normalisation of his (1.2) (Iwaniec, weight > 5/2)
  this is a(t) ≪ t^{k/2−2/7+ε}, i.e. |h(t)| ≪_{h,ε} t^{1/2−1/28+ε} for h ∈ U^⊥ ⊂ S_{3/2} and squarefree t.
* **(RS)** For weight-2 newforms φ, φ′ of trivial character (real Hecke eigenvalues), normalised λ_ℓ(φ) := a_ℓ(φ)/√ℓ:
  (RS1) L(s, φ) is entire and L(1, φ) ≠ 0 (non-vanishing on Re s = 1: Jacquet–Shalika 1976; for holomorphic newforms
  classical); (RS2) the Rankin–Selberg L(s, φ × φ′) is holomorphic and non-zero at s = 1 if φ ≠ φ′ (Ogg for
  GL₂ × GL₂, Shahidi in general) and has a simple pole at s = 1 if φ = φ′ (Rankin–Selberg). Verified: Sarnak,
  *Nonvanishing of L-functions on Re(s) = 1* (Shalika volume, 2002), §1, read from the primary PDF (§8). Taking −L′/L
  (prime powers ℓ^k, k ≥ 2, contribute O(1) at s = 1 because the unitary Satake parameters give |Λ(ℓ^k)| ≤ 4 log ℓ;
  finitely many bad ℓ are O(1)), with w_s(ℓ) := ℓ^{−s} log ℓ and s → 1⁺:
  Σ_{ℓ∉P} λ_ℓ(φ)w_s(ℓ) = O(1),   Σ_{ℓ∉P} λ_ℓ(φ)λ_ℓ(φ′)w_s(ℓ) = δ_{φφ′}/(s − 1) + O(1).          (RS*)
  (No prime number theorem or zero-free region is needed; only behaviour at the point s = 1.)

**Theorem S1 (PROVED relative to the inputs).** Suppose **(T1⁻_prime)**: g(ℓ²) ≤ 0 for all sufficiently large primes ℓ
(every valid signed minorant satisfies it, since R(ℓ²) = 0). Then E(1) ≤ 0, and:
(a) if E(1) < 0, then g(p) < 0 for every sufficiently large prime p ∈ 𝒞₁(2N) (ineffective threshold); so g is positive
    at only finitely many primes of 𝒞₁;
(b) if E(1) = 0, then E ≡ 0 on 𝒞₁(2N), all t = 1 unary coefficients κ_{χ,1} vanish, and c_φ = g_φ(1) = 0 for every φ.
    Consequently (Waldspurger Cor. 2, as in WALDS W1 Steps 4–5) for every squarefree t ∈ 𝒞₁(2N), t > 1:
    g(t) = Σ_{φ ∈ Φ_exc} g_φ(t), Φ_exc = {φ : g_φ ≠ 0, L(½, φ ⊗ ψχ_{−4}) = 0}.
In particular a valid signed minorant that is positive at infinitely many primes of 𝒞₁ lies in case (b): on squarefree
𝒞₁ it is a pure Gauss-exceptional cusp sum, exactly like a valid support proxy.

*Proof.* Let P be a finite set of primes containing those dividing 2N and those below the (T1⁻) bound, such that each
g_φ ≠ 0 is a T(ℓ²)-eigenform with eigenvalue a_ℓ(φ) for ℓ ∉ P. For ℓ ∉ P, TERNARY Thm F Step 2 gives
  g(ℓ²) = E(1)(1 + ℓ − ε(ℓ)) + 2ℓ·u(ℓ) + Σ_φ c_φ(a_ℓ(φ) − ε(ℓ)),   u(a) := Σ_χ κ_{χ,1}χ(a),      (2.1)
where χ runs over the odd primitive characters of the t = 1 unary basis series (moduli | 4N), u is real-valued
(the unary part of a real form has real coefficients 2ℓu(ℓ)) and **odd**: u(−a) = −u(a).
*Step 1 (E(1) ≤ 0).* Divide (2.1) by ℓ: E(1) + 2u(ℓ) + O(ℓ^{−1/2}) ≤ 0. For a ∈ (ℤ/4N)^× let ℓ → ∞ through primes
≡ a (mod 4N) (Dirichlet): E(1) + 2u(a) ≤ 0. Apply it to a and −a and add: 2E(1) ≤ 0.
*Step 2 (case E(1) < 0).* By TERNARY Thm F Step 1, E(n) = A·B(n) on 𝒞₁(2N) with B(n) = √n ∏_{ℓ∤2N} α_ℓ(L₁, n) > 0 and
A·B(1) = E(1) < 0. For a prime p ∈ 𝒞₁, p ∤ 2N, the good-prime densities are α_ℓ(L₁, p) = 1 + (−det L₁·p/ℓ)/ℓ (ℓ ≠ p)
and α_p(L₁, p) ≥ c₀ > 0, so B(p) ≫ √p·L(1, χ_{−det L₁·p}) ≫_ε p^{1/2−ε} (Sie). The unary part vanishes at primes
p ∤ N (TERNARY Thm F (iii)), and |Σ_φ g_φ(p)| ≪ p^{1/2−1/28+ε} (Duk). Hence g(p) = A·B(p) + O(p^{1/2−1/28+ε}) < 0 for
p large.
*Step 3 (case E(1) = 0: unary part).* Step 1 now gives u(a) ≤ 0 and u(−a) = −u(a) ≤ 0, so u ≡ 0 on (ℤ/4N)^×, and by
linear independence of the distinct characters χ (TERNARY Step 3) κ_{χ,1} = 0. E ≡ 0 on 𝒞₁ by Thm F Step 1.
*Step 4 (cusp anchors; the signed Dedekind step).* Now (2.1) reads Σ_φ c_φ(a_ℓ(φ) − ε(ℓ)) ≤ 0 for ℓ ∉ P.
(i) *c_φ are real.* Complex conjugation of Fourier coefficients preserves M_{3/2}(Γ₀(4N), ψ) (ψ real), the genus
part, the unary part, and each S(4N, ψ, φ) (the T(ℓ²) of (S4) have real coefficients and the a_ℓ(φ) are real), so by
uniqueness of the decomposition every piece of a real g is real; in particular c_φ ∈ ℝ.
(ii) Put G(ℓ) := Σ_φ c_φλ_ℓ(φ) (real; |G(ℓ)| ≤ K := 2Σ_φ|c_φ| by Deligne). Dividing by √ℓ, the inequality gives
G(ℓ) ≤ δ(ℓ) := |Σ_φ c_φ|ℓ^{−1/2}, so G⁺ := max(G, 0) ≤ δ. For s > 1:
Σ_{ℓ∉P}|G(ℓ)|w_s(ℓ) = Σ (2G⁺ − G)w_s ≤ 2Σ_ℓ δ(ℓ)w_s(ℓ) − Σ_φ c_φ Σ_ℓ λ_ℓ(φ)w_s(ℓ) = O(1)  (s → 1⁺)
(the first sum converges at s = 1; the second is O(1) by (RS*)). Hence Σ G(ℓ)²w_s(ℓ) ≤ K·Σ|G|w_s = O(1). By (RS*),
Σ G(ℓ)²w_s(ℓ) = Σ_{φ,φ′}c_φc_{φ′}Σ_ℓ λ_ℓ(φ)λ_ℓ(φ′)w_s(ℓ) = (Σ_φ c_φ²)/(s − 1) + O(1). So Σ_φ c_φ² = 0: all c_φ = 0.
*Step 5.* With c_φ = 0, WALDS W1 Steps 4–5 apply verbatim (they use only g_φ(1) = 0, Waldspurger Cor. 2 and Thm F (i),
(ii)): for squarefree t ∈ 𝒞₁, t > 1, g_φ(t)²L(½, φ ⊗ ψχ_{−4}) = 0, the genus and unary parts vanish at t, and the
conclusion follows. ∎

**Remarks.** (1) Only *prime* squares are used, and only their sign. As a by-product, WALDS W1 holds under the
prime-square hypothesis g(ℓ²) = 0 (ℓ large) alone — the route WALDS Remark (a) left "not verified, not used" (Step 4
with ≤ replaced by =; Step 2 is then not needed).
(2) Case (a) is a genuine alternative, not vacuous: g = −θ_{gen L} + (small cusp form) satisfies (T1⁻) and is negative
at all large primes of 𝒞₁. A signed minorant can be *valid* in case (a) — it is then simply useless on 𝒞₁.
(3) The analytic inputs enter only in case (a) (Sie, Duk) and in Step 4 (RS). Case (b) is PROVED relative to (RS),
Deligne and Waldspurger only.
(4) Step 4 is a *sign* version of WALDS's Dedekind step: a finite real combination of normalised Hecke eigenvalue
sequences of distinct newforms that is ≤ o(1) at every large prime is identically 0. It fails for Eisenstein-type
sequences (λ_ℓ = 1 + 1/ℓ ≥ 0), which is why the genus part needs Steps 1–2 instead.

## 3. Theorem S2 — mixed nebentypus (closes WALDS escape (E-c) in the ternary-theta class)

**Setting.** Ψ a finite set of quadratic characters ψ mod 4N; for each ψ, g_ψ ∈ M_{3/2}(Γ₀(4N), ψ) in the ternary-theta
class of §2 (real coefficients); g := Σ_ψ g_ψ (a form on Γ₁(4N)). Write, per ψ, E_ψ, unary part U_ψ, eigencomponents
g_{φ,ψ} with anchors c_{φ,ψ} := g_{φ,ψ}(1), ε_ψ(ℓ) := ψ(ℓ)(−1/ℓ). Note ε_ψ = ψχ_{−4} is an **odd** quadratic character
(ψ is even), so ε_ψ ≠ 1, and ψ ↦ ε_ψ is injective. (The genus density character ε₀(ℓ) = (−det L/ℓ) of TERNARY Step 2
equals ε_ψ under the theta-multiplier convention checked in TERNARY Remark F3 / WALDS §5.1; the proofs below use only
that ε₀,ψ and ε_ψ are odd quadratic characters, each injective in ψ — so they are insensitive to that convention.) Call m *good* if m is squarefree and all its prime factors lie
outside a finite set P ⊇ {ℓ | 2N} ∪ {small primes} (P also contains the finitely many primes where some g_{φ,ψ} is not
a T(ℓ²)-eigenform).

**Lemma 3.1 (square-orbit factorisation; PROVED rel. (S1), (S4)).** For good m:
g(m²) = Σ_ψ E_ψ(1)·M_ψ(m) + 2m·u(m) + Σ_{φ,ψ} c_{φ,ψ}·A_{φ,ψ}(m), where
M_ψ(m) := ∏_{ℓ|m}(1 + ℓ − ε_ψ(ℓ)),  A_{φ,ψ}(m) := ∏_{ℓ|m}(a_ℓ(φ) − ε_ψ(ℓ)),  u(m) := Σ_χ κ_{χ,1}χ(m)
(χ over the odd primitive characters of all t = 1 unary series occurring in the g_ψ).
*Proof.* Genus part: m² is a unit square at every q ∤ m, so by (S1) only the densities at ℓ | m and the archimedean
factor change; E_ψ(m²)/E_ψ(1) = ∏_{ℓ|m}ℓα_ℓ(ℓ²)/α_ℓ(1) = ∏(1 + ℓ − ε_ψ(ℓ)) (TERNARY Step 2, densities multiplicative).
Cusp part: for ℓ ∤ m′, (S4) at n = m′² gives a(ℓ²m′²) = (a_ℓ(φ) − ψ(ℓ)(−m′²/ℓ))a(m′²) = (a_ℓ(φ) − ε_ψ(ℓ))a(m′²); induct.
Unary part: only t = 1 series reach m² with gcd(m, N) = 1 (TERNARY Step 2), coefficient 2χ(m)m. ∎

**Theorem S2 (PROVED rel. the inputs of §2).**
(a) *(Support form.)* If g(m²) = 0 for every good m, then E_ψ(1) = 0, κ_{χ,1} = 0 and c_{φ,ψ} = 0 for **every** ψ, χ, φ.
Hence each g_ψ satisfies Thm F (i)–(iii) and W1 (ii)–(iii), and for squarefree t ∈ 𝒞₁(2N), t > 1:
g(t) = Σ_{(φ,ψ) exceptional} g_{φ,ψ}(t), "exceptional" meaning g_{φ,ψ} ≠ 0 and L(½, φ ⊗ ψχ_{−4}) = 0.
(b) *(Signed form.)* If g(m²) ≤ 0 for every good m, then E_ψ(1) ≤ 0 for every ψ, and: if some E_ψ(1) < 0 then
g(p) < 0 for every sufficiently large prime p ∈ 𝒞₁(2N); otherwise the conclusions of (a) hold.

*Proof of (a).* The functions m ↦ M_ψ(m), m ↦ m·χ(m), m ↦ A_{φ,ψ}(m) are multiplicative on good m with value 1 at
m = 1. Any two of them differ at infinitely many primes:
* M_ψ vs M_{ψ′} (ψ ≠ ψ′), and A_{φ,ψ} vs A_{φ,ψ′}: wherever ε_ψ(ℓ) ≠ ε_{ψ′}(ℓ), i.e. ψψ′(ℓ) = −1;
* M_ψ(ℓ) ∈ {ℓ, ℓ + 2} vs ℓχ(ℓ) = ±ℓ: they differ wherever ε_ψ(ℓ) = −1;
* ℓχ(ℓ) vs ℓχ′(ℓ): wherever χ(ℓ) ≠ χ′(ℓ);
* M_ψ(ℓ), ℓχ(ℓ) (absolute value ≥ ℓ) vs A_{φ,ψ′}(ℓ) (absolute value ≤ 2√ℓ + 1): at every ℓ ≥ 7;
* A_{φ,ψ} vs A_{φ′,ψ′} with φ ≠ φ′: if they agreed at all large ℓ then |λ_ℓ(φ) − λ_ℓ(φ′)| ≤ 2ℓ^{−1/2} there, so
  Σ_ℓ (λ_ℓ(φ) − λ_ℓ(φ′))²w_s(ℓ) = O(1) as s → 1⁺, whereas (RS*) gives 2/(s − 1) + O(1).
Dedekind-type independence (WALDS W1 Step 3, whose proof uses exactly this property and the relation at ℓm and m for
ℓ ∤ m, m good) now gives all coefficients 0 in the relation of Lemma 3.1. The rest is W1 Steps 4–5 per ψ. ∎

*Proof of (b).* **Step 1 (each E_ψ(1) ≤ 0).** Let Q := 4N and for ψ ∈ Ψ let S_ψ := {c ∈ (ℤ/Q)^× : ε_ψ(c) = −1};
since ε_ψ is a non-trivial quadratic character, |S_ψ| = φ(Q)/2, and S_ψ determines ψ. Fix ψ₀ and T ≥ 2. For each
c ∈ S_{ψ₀} choose a finite set of good primes ℓ ≡ c (mod Q), all > Y, with P_c := ∏(1 + 2/ℓ) ∈ [T, 2T] (possible:
Σ_{ℓ≡c} 1/ℓ = ∞ and 1 + 2/ℓ → 1); let m be the product of all chosen primes. Then
M_ψ(m)/m = ∏_{c ∈ S_{ψ₀} ∩ S_ψ} P_c ∈ [T^{|S_ψ∩S_{ψ₀}|}, (2T)^{|S_ψ∩S_{ψ₀}|}], with |S_ψ ∩ S_{ψ₀}| ≤ φ(Q)/2 − 1 for
ψ ≠ ψ₀ and = φ(Q)/2 for ψ₀. The cusp term satisfies |A_{φ,ψ}(m)|/m ≤ ∏_{ℓ|m}(2ℓ^{−1/2} + ℓ^{−1}) ≤ 1 for Y ≥ 9, and
|u| is bounded. So g(m²)/m = E_{ψ₀}(1)·Θ(T^{φ(Q)/2}) + O(T^{φ(Q)/2−1}) + O(1), which is positive for large T unless
E_{ψ₀}(1) ≤ 0.
**Step 2 (some E_ψ(1) < 0).** On 𝒞₁(2N), each E_ψ(n) = E_ψ(1)B_ψ(n)/B_ψ(1) with B_ψ > 0 (TERNARY Step 1), so for primes
p ∈ 𝒞₁: E(p) = Σ_ψ E_ψ(1)B_ψ(p)/B_ψ(1) ≤ E_{ψ₁}(1)B_{ψ₁}(p)/B_{ψ₁}(1) ≪ −p^{1/2−ε} (Sie), while the unary part vanishes
at p and the cusp part is O(p^{1/2−1/28+ε}) (Duk). So g(p) < 0 for large p.
**Step 3 (all E_ψ(1) = 0: unary).** Now g(m²)/m = 2u(m) + o(1) ≤ 0 (good m → ∞ in a fixed class mod Q); u is odd and
periodic mod Q, so as in §2 Step 3 u ≡ 0 on (ℤ/Q)^× and all κ_{χ,1} = 0.
**Step 4 (cusp: primes).** Write C_φ := Σ_ψ c_{φ,ψ}, H_φ(ℓ) := Σ_ψ c_{φ,ψ}ε_ψ(ℓ), D(ℓ) := Σ_φ H_φ(ℓ) (all real, §2
Step 4(i)). At m = ℓ: Σ_φ C_φ a_ℓ(φ) − D(ℓ) ≤ 0, i.e. Σ_φ C_φλ_ℓ(φ) ≤ |D(ℓ)|ℓ^{−1/2} = O(ℓ^{−1/2}). The sign
argument of §2 Step 4(ii) (with c_φ replaced by C_φ) gives C_φ = 0 for all φ. Then the inequality reads −D(ℓ) ≤ 0, i.e.
Σ_ψ D_ψε_ψ(a) ≥ 0 for every class a (D_ψ := Σ_φ c_{φ,ψ}; Dirichlet); summing over a ∈ (ℤ/Q)^× gives 0 (each ε_ψ is
non-trivial), so Σ_ψ D_ψε_ψ(a) = 0 for all a and, the ε_ψ being distinct characters, D_ψ = 0.
**Step 5 (cusp: products of two primes).** For good m = ℓ₁ℓ₂, expanding A_{φ,ψ}(ℓ₁ℓ₂) and using C_φ = 0 = D_ψ:
g(ℓ₁²ℓ₂²) = −Σ_φ [a_{ℓ₂}(φ)H_φ(ℓ₁) + a_{ℓ₁}(φ)H_φ(ℓ₂)] ≤ 0.
Fix ℓ₁ in a class a and let ℓ₂ run over all large primes; divide by √ℓ₂:
Σ_φ H_φ(a)λ_{ℓ₂}(φ) ≥ −ℓ₂^{−1/2}Σ_φ|a_{ℓ₁}(φ)H_φ(ℓ₂)| = O_{ℓ₁}(ℓ₂^{−1/2}).
The sign argument (applied to −Σ_φ H_φ(a)λ_ℓ(φ)) gives H_φ(a) = 0 for every φ and every class a; by independence of
the characters ε_ψ, c_{φ,ψ} = 0 for all φ, ψ. Conclude as in (a). ∎

**Remarks.** (1) Under the *equality* hypothesis at prime squares only, the relation at m = ℓ gives just
Σ_ψ E_ψ(1) = 0, C_φ = 0 and E_ψ(1) + D_ψ = 0 (the cusp anchors can absorb the second-order Eisenstein terms
ε_ψ(ℓ)E_ψ(1)), so the prime-square argument alone does not separate these terms; composite good m (Lemma 3.1) do.
(Whether a modular counterexample realising E_ψ(1) ≠ 0 with prime-square vanishing exists was not checked.) Valid
proxies satisfy T1 at all odd squares, so this is moot for them. (2) Non-quadratic ψ (forms on Γ₁(4N) beyond the ternary-theta class) — the same proof works with complex
a_ℓ(φ) (φ of nebentypus ψ²), conjugate pairs of components, and |G|² in place of G² (Rankin–Selberg against φ̄′);
stated only for quadratic ψ here. (3) TERNARY §4.4's gap "mixed nebentypus: only Σ_δ E_δ(1) = 0 follows" is exactly
Remark (1): it disappears once composite squares are used.

## 4. The other fixed-level objects of the brief: higher weight, cosets, exponential growth, Fourier–Jacobi

### 4.1 Proposition S3 — higher half-integral weight (WALDS escape (E-d)); PROVED rel. the listed inputs
Let κ = k/2, k odd ≥ 5, g = Σcᵢθ_{Lᵢ} + h ∈ M_κ(Γ₀(4N), ψ) with Lᵢ positive lattices of rank k (theta series of weight
κ), h cuspidal, real coefficients, **one** quadratic ψ (see the counterexample below for mixtures). Inputs: Siegel's formula in rank k ≥ 5
(classical; on 𝒞₁ the genus part is A·B(n) with B(n) = n^{κ−1}∏_{ℓ∤2N}α_ℓ(L₁, n) ≍ n^{κ−1}, the Euler product now
converging absolutely to a value bounded above and below — no Siegel-zero issue); Waldspurger Prop. 1 / Cor. 2 for
general odd k (as read from the primary source by WALDS, lit_verify #1, #5, stated there with weight k/2 and
χ₀(n) = χ(n)(−1/n)^{(k−1)/2}); Duke Thm 5 (all weights ±1/2 + 2ℓ: a(t) ≪ t^{κ/2−2/7+ε} at squarefree t); (RS*) for
weight-(k−1) newforms with λ_ℓ := a_ℓ/ℓ^{κ−1}.
**Statement.** If g(ℓ²) ≤ 0 for all large primes ℓ, then either
g(p) < 0 for all large primes p ∈ 𝒞₁(2N), or E ≡ 0 on 𝒞₁ and every Shimura anchor vanishes, so that on squarefree
t ∈ 𝒞₁, t > 1, only components with L(½, φ ⊗ χ₀^{−1}) = 0 survive (χ₀^{−1} = ψ for k ≡ 1 (4), ψχ_{−4} for k ≡ 3 (4)).
*Proof.* As §2/§3, with three simplifications: there are no unary theta series of weight ≥ 5/2; the genus term at ℓ²
is E(1)ℓ^{2κ−2}(1 + O(1/ℓ)), which dominates the cusp term (a_ℓ(φ) − ψ(ℓ)(−1/ℓ)^{(k−1)/2}ℓ^{κ−3/2})c_φ = O(ℓ^{κ−1})
(Shimura's T(ℓ²) in weight κ; Deligne), so (T1⁻) gives E(1) ≤ 0 at once; and in case E(1) < 0 the bound
|E(p)| ≫ p^{κ−1} beats the cusp bound p^{κ/2−2/7+ε} for κ ≥ 5/2. In case E(1) = 0, divide the cusp relation by
ℓ^{κ−1}: the ε-term is O(ℓ^{−1/2}) and §2 Step 4 applies verbatim. ∎
**Mixed nebentypus in weight ≥ 5/2.** The *support* form (S2(a)) extends (the genus square factors
M_ψ(ℓ) = ℓ^{2κ−2}(1 + ℓ^{−(2κ−2)} − ε_ψ(ℓ)ℓ^{−(κ−1/2)}) (rank-k unimodular densities, internal review R1) differ for distinct ψ wherever ε_ψ differ, and Dedekind
independence only needs that). The *signed* form does **not**: §3 Step 1 needs the divergence of Σ1/ℓ, whereas in
rank ≥ 5 the character-dependent corrections to M_ψ(ℓ)/ℓ^{2κ−2} are absolutely summable. **Counterexample (internal
review R1; coefficient inequalities checked numerically, `scripts/z60_signed_rank5_check.py 20000` →
`data/z60/signed/rank5_check.txt`):** E₁ = θ of x₁² + … + x₅² (nebentypus 1), E₂ = θ of x₁² + … + x₄² + 2x₅² (χ₈),
level 8, g := E₂/8 − (3/2)·E₁/10 (normalised at n = 1). Then g(m²) < 0 for all odd m ≤ 141 (max g(m²)/m³ = −0.131;
reviewer's proof for all good m: E₂(m²)/E₁(m²) ≤ exp(Σ_{n≥11}2/(n² − 1)) < 3/2), while g(p) > 0 at all 289 primes
p ≡ 17 (mod 24) ≤ 2·10⁴ (reviewer: E₂(p)/E₁(p) ≥ 25/16 from the factor at ℓ = 3) — p ≡ 17 (mod 24) lies in 𝒞₁(4).
So a mixed-ψ signed proxy in weight 5/2 can satisfy T1⁻ and be positive on a positive-density set of 𝒞₁-primes with a
non-zero genus part: **mixed-nebentypus signed proxies in weight ≥ 5/2 are an open escape** (like AUTOMORPH B1 in
integral weight). This particular g is negative at all 53 𝔐-primes ≤ 2·10⁴ (the ℓ = 3 boost is absent on 𝔐, where
(p/3) = 1; the 𝔐-prime ratio is ≤ ∏_{ℓ≥11,(2/ℓ)=−1}((1+ℓ^{−2})/(1−ℓ^{−2}))² ≈ 1.08); whether *some* mixed
higher-weight Eisenstein combination is T1⁻-compatible and positive at all large 𝔐-primes is a convex-geometry question
about Euler-product vectors at squares versus at 𝔐-primes — open (validity would in any case be (MS) there, W5).

### 4.2 Cosets / theta series with characteristics (WALDS escape (E-b)); partial, CONDITIONAL / Assessment
For a coset L + v (v ∈ ℚL), θ_{L+v} is modular on Γ₁(M) for suitable M, with characters that need not be quadratic.
Hypothesis **(SWc)**: Siegel's formula for lattice cosets — θ_{gen(L+v)}, the weighted average over the genus of the
coset with positive weights, has coefficients c·√n·∏_ℓ α_ℓ(L+v, n), and θ_{L+v} − θ_{gen(L+v)} is cuspidal. The literature
check (§8) located Weil 1965 (Schwartz–Bruhat Siegel formula) but did not confirm the precise statement or range.
**What follows under (SWc) (CONDITIONAL).** At good ℓ the coset is the lattice, so the good-prime factor is as before; at
q | M the coset density α_q(L + v, n) is a locally constant function of n ∈ ℤ_q^× of some finite modulus q^K (no longer
invariant under all unit squares). For one underlying genus (one determinant class), on each class n ≡ s (mod M^K) with
s a unit square mod M^K the genus part is β(s)·B(n); every prime p ∈ 𝒞₁(2M) lies in such a class, and so does ℓ² for
every prime ℓ ≡ √s (mod M^K). Running §2 Steps 1–2 with ℓ restricted to ℓ² ≡ s gives, **class by class**: β(s) ≤ 0 under
(T1⁻), and g(p) < 0 at all large primes p ≡ s (mod M^K) if β(s) < 0. Nothing forces the classes to behave alike
(internal review R2: g = −θ_{5ℤ³+(1,0,0)} is ≤ 0 everywhere, vanishes identically at n ≡ 4 (mod 5) and has non-zero
genus density at n ≡ 1 (mod 5)), so there is no global dichotomy; on classes with β(s) = 0 the unary and cusp parts
would still have to be handled (complex characters; residue-restricted Rankin–Selberg) — **not done**.
**Termwise coset recipes (CONDITIONAL on (SWc)).** The positivity argument of WALDS Lemma W0 does carry over: if
r_{L+v}(ℓ²) = 0 for all large primes ℓ, then β(s) = 0 for every unit square class s, so the genus average vanishes on
𝒞₁(2M), and by positivity of the Siegel weights r_{L+v}(n) = 0 for n ∈ 𝒞₁(2M). So non-negative combinations of coset
thetas whose representations all yield (★) certificates represent nothing in 𝒞₁.

### 4.3 Lemma S4 — square-blind asymptotics (exponential growth: weakly holomorphic, Rademacher, mock with principal part)
**Lemma S4 (PROVED, elementary).** Let g : ℕ → ℝ, M ≥ 1, and suppose that along n ≡ 1 (mod M),
g(n) = F(n)(1 + o(1)) with F eventually non-zero of constant sign. If g(m²) ≤ 0 for all large odd m, then g(p) < 0
for every sufficiently large prime p ≡ 1 (mod M) — a set containing a positive proportion of the 𝔐-primes.
*Proof.* Odd m ≡ 1 (mod M) have m² ≡ 1 (mod M), so F(m²) ≤ 0 for large such m; F has eventually constant sign, so
F < 0 eventually, and g(p) = F(p)(1 + o(1)) < 0. ∎
**Corollary S4′ (CONDITIONAL on an explicit asymptotic hypothesis).** Let g have real coefficients and suppose
**(Dom)**: there are M ≥ 1, a constant k ≠ 0 and a function Φ > 0 such that g(n) = k·Φ(n)(1 + o(1)) along n ≡ 1 (mod M)
(for a weakly holomorphic form or the holomorphic part of a harmonic Maass form this is what a Rademacher-type expansion
gives when, among all pairs (polar index m, denominator c) with c | M, the term of largest exponential rate √m/c has a
non-zero periodic coefficient at the class 1 (mod M) and the remaining terms are uniformly smaller — this has to be
verified for the particular form; it is not automatic, since several polar indices and cancellations can occur). Then
Lemma S4 applies: **a signed minorant satisfying (Dom) and T1⁻ is negative at all large primes ≡ 1 (mod M)**, a set
containing a positive proportion of the 𝔐-primes. If (Dom) fails for every M (e.g. all dominant periodic coefficients
vanish at the class of 1), nothing is claimed — that case is **unresolved** here.
*Reading.* Exponential-size objects are "square-blind" on residue classes: their dominant term at n depends only on
n mod c, and primes ≡ 1 (mod M) are indistinguishable from squares ≡ 1 (mod M). (Contrast: the integral-weight
Eisenstein proxy of AUTOMORPH Prop B1 escapes T1⁻ precisely because σ₂(n), τ(n) are multiplicative, not smooth in n.)

### 4.4 Fourier–Jacobi coefficients and indefinite theta lifts (Assessment, reductions only)
* A Fourier–Jacobi coefficient of index m of a holomorphic Siegel modular form of degree 2 is a holomorphic Jacobi
  form; by the theta decomposition its coefficient c(n, r) is a coefficient of a weight-(k − ½) vector-valued form at
  the discriminant 4mn − r² ≥ 0. A proxy n ↦ c(n, r) (fixed m, r) is therefore a half-integral-weight coefficient at a
  *linear function* of n, i.e. a section — AUTOMORPH's E2 shape, not a fixed-level object in the variable n. The (★)
  discriminant 4Cn + 1 ≡ 1 (mod 4) is never of the form 4mn − r² (≡ 0, 3 mod 4); it is the discriminant of the
  indefinite form [C, 1, −n], which belongs to skew-holomorphic Jacobi forms / weight-½ objects in the positive-
  discriminant direction (Skoruppa), again one level C at a time (E2).
* Indefinite theta lifts: R(n) counts γ = [[a, n], [c, e]] ∈ SL₂(ℤ) with 4 | c, a ≡ −1 (mod c), a, e > 0 (METAPLECTIC
  §3), i.e. vectors of the split quaternary lattice (det form, signature (2, 2)) of norm 1 with a prescribed coordinate
  — a partial (mixed-model) Fourier coefficient, which is a sum over the moduli c of level-c data (Kloosterman-type),
  E2 / H-A again; this is the TRACE lane's territory and is not pursued here.

## 5. Multi-eigensystem cancellation (WALDS escape (E-a)): for support proxies cancellation is never the obstruction

Fix a level and a finite-dimensional real space V of forms with real coefficients (e.g. the ternary-theta class of §3
at level 4N: genus thetas + cusp forms over the quadratic ψ ∈ Ψ; the abstract statement below needs no more). Let Λ be
the space of restrictions to 𝒞₁(2N) of the g ∈ V with g(m²) = 0 for **every** odd m (infinitely many conditions, but
finitely many suffice by finite dimension). Fix a basis s₁, …, s_k of Λ and put S(n) := (s₁(n), …, s_k(n)) ∈ ℝ^k for
n ∈ 𝒞₁. Each g_K := Σ_j K_j s_j, extended by 0 off 𝒞₁, is again a modular form — the projection onto a union of residue
classes mod 8∏_{q|N}q is a finite combination of character twists, so it **raises the level** to a larger fixed level —
and still vanishes at every odd square (squares outside 𝒞₁ are set to 0, those inside are already 0). Let
Z := {n ∈ 𝒞₁(2N) : R(n) = 0} (it contains 1 and the odd squares coprime to 2N, where S = 0) and
W := span_ℝ{S(z) : z ∈ Z} ⊆ ℝ^k.

**Proposition S5 (PROVED, elementary; support form).** For P₀ ≥ 1 the following are equivalent:
(i) some g_K is a valid support proxy (g_K(n) ≠ 0 ⟹ R(n) ≥ 1 for all n) and g_K(p) ≠ 0 for every prime p ∈ 𝒞₁, p > P₀;
(ii) S(p) ∉ W for every prime p ∈ 𝒞₁, p > P₀.
When (ii) holds, the valid K that work form the complement in W^⊥ of countably many proper subspaces; in coordinates
w.r.t. a basis of W^⊥ one may take the free coordinates algebraically independent over the (countable) field generated
by all values S(n).
*Proof.* g_K is valid iff g_K(z) = 0 for all z ∈ Z (off 𝒞₁ it is 0), i.e. iff K ∈ W^⊥ (annihilator for the pairing
⟨K, S⟩ = Σ K_jS_j). (ii) ⟹ (i): for each such p, H_p := {K ∈ W^⊥ : ⟨K, S(p)⟩ = 0} is a proper subspace of W^⊥, since
S(p) ∉ W = (W^⊥)^⊥ (finite dimension). A real vector space is not a countable union of proper subspaces (each is
Lebesgue-null), so some K ∈ W^⊥ avoids every H_p. (i) ⟹ (ii): K ∈ W^⊥ and ⟨K, S(p)⟩ ≠ 0 force S(p) ∉ W. ∎

**Consequences (scoped).**
1. *(ii) contains the prime target on 𝒞₁ above P₀* (PROVED): if p ∈ Z then S(p) ∈ W, so (ii) forces R(p) ≥ 1 for every
   prime p ∈ 𝒞₁, p > P₀ (WALDS Prop W5 again). It says nothing about composites.
2. *Cancellation can always be avoided* (PROVED): if (ii) holds, a generic valid K has g_K(p) ≠ 0 at **every** prime of
   𝒞₁ above P₀ simultaneously; no single-p control of cancellation is required. So the brief's suggested closure
   ("each exceptional piece vanishes at infinitely many 𝔐-primes; can cancellation be controlled?") cannot by itself
   close (E-a) for support proxies with unrestricted real coefficients: even if every line vanishes infinitely often
   (CKRS, WALDS §4.1), a generic valid combination vanishes at p only if S(p) ∈ W. WALDS's heuristic "pure-cusp
   proxies vanish at T^{3/4+o(1)} primes" concerns proxies with *rational* coefficients (one rational number per p,
   CKRS discretisation); it does not apply to generic K. (For rational-coefficient proxies the cancellation question
   remains a genuine one.)
3. *The residual condition in L-function language* (CONDITIONAL on the dictionary). If V is the ternary-theta class,
   Thm S2(a) writes every element of Λ, on squarefree t > 1, in terms of the exceptional components; **if** moreover
   each exceptional (φ, ψ) satisfies W1′'s hypothesis (an L-non-zero anchor in 𝒞₁, or (H2)), each contributes one line
   ℓ_φ with t-th entry ±κ_φ·t^{1/4}·L(½, G_φ ⊗ χ_t)^{1/2} (signs not determined by L-values; fixed local factors on
   𝒞₁). Λ may be a proper subspace of the span of the lines (T1 at squares m² with gcd(m, 2N) > 1). Then (ii) says
   that the coefficient vector (ℓ_φ(p))_φ is not annihilated by the fixed subspace Λ ∩ W^⊥ (in line coordinates). In the
   special case where Λ is the full span of the lines and W = 0 (sufficient: 𝒞₁(2N) contains no non-square R-zero),
   it is exactly
   **(𝒟_N): for every prime p ∈ 𝒞₁(2N), p > P₀, some exceptional G_φ has L(½, G_φ ⊗ χ_p) ≠ 0** —
   a disjunction of central-value non-vanishings. In general it is a linear condition on signed square roots of
   central values, not on the central values themselves.
4. *No validity mechanism is supplied* (Assessment). S5 is an exact criterion; it neither proves validity nor shows
   that validity can only be obtained circularly. A proof of (MS) along this route needs an *independent* reason why
   some g_K vanishes on Z (e.g. an identity g_K(n) = Σ_{certificates of n} w with structural weights); proving such an
   identity does not require enumerating Z, but none is known, and termwise recipes are excluded on 𝒞₁ (W0; §4.2).
5. *Heuristic status of (𝒟_N) (Assessment).* For k independent rational exceptional G_φ with CKRS-type vanishing
   probability p^{−1/4+o(1)} each, simultaneous vanishing has probability p^{−k/4+o(1)}, summable over primes for k ≥ 5:
   (𝒟_N) is then expected to hold above some P₀. So, unlike single-eigensystem positivity, the multi-eigensystem
   condition is *not* expected to fail. Known non-vanishing technology gives positive-proportion / infinitely-many
   results for single forms; no simultaneous result was verified (§8 item 8), and nothing pointwise.

**Signed version (corrected after internal review R3).** For a signed minorant the validity condition is
g(z) ≤ 0 at R-zeros, so the coefficient domain is the closed convex cone 𝒦 := {K : ⟨K, S(z)⟩ ≤ 0 ∀ z ∈ Z}, not W^⊥
(and Λ must be defined with g(m²) ≤ 0, whose 𝒞₁-restrictions are, by S1/S2(b), again in the span of the exceptional
components on squarefree t > 1 once eventual negativity is excluded). Effectiveness asks for K ∈ 𝒦 with
⟨K, S(p)⟩ > 0 for all large primes p ∈ 𝒞₁. No genericity argument is available for a strict sign condition: for a
single line it requires the sign of s(p) to be eventually constant on 𝒞₁-primes; for k lines it requires the
(normalised) vectors S(p) to avoid the polar of 𝒦 — a joint sign-distribution question. The finite data of §6.2 show
both signs at primes in the tested range for every computed line (which does not refute eventual constancy). Proven
sign-change results concern a(tn²) with t fixed or indices 8n (n odd squarefree; Lester–Radziwiłł), never primes
(§8 item 7). The §6.1 certificates are for support proxies only and do not transfer to signed minorants.

## 6. Computations

### 6.1 Mixed-nebentypus validity certificates (CERTIFIED, exact rational linear algebra)
`scripts/z60_signed_mixed.py L B 0 4 zrows` (driver `scripts/z60_signed_mixed_runs.sh`, output `data/z60/signed/mixed_runs.txt`):
V = ⊕_ψ M_{3/2}(Γ₀(L), ψ) over **all** quadratic ψ = (D/·) with D = 1 or a positive fundamental discriminant | L (8
characters at each level), full spaces; rows g(m²) = 0 for all odd m ≤ √B and (zrows = 1) g(z) = 0 at every n ≡ 1 (4),
n ≤ B, with R(n) = 0 (LOGIC census list, squares and composites included).

| L | B | dim V | rows (zero rows) | rank of mixed kernel on 𝒞₁ ∩ [1, B] | same, without zero rows | Σ_ψ per-ψ ranks (no zero rows) |
|---|---|---|---|---|---|---|
| 168 | 40 000 | 176 | 169 (168) | **0** | 3 (B = 40 000; 16 at B = 4000) | 1 (ψ = χ₁₆₈) |
| 240 | 30 000 | 272 | 150 (149) | **0** | 9 | 1 (ψ = χ₁₂₀) |
| 280 | 30 000 | 240 | 150 (149) | **0** | 6 | 1 (ψ = χ₅₆) |

**CERTIFIED:** at L ∈ {168, 240, 280}, every valid mixed-nebentypus *support* proxy g ∈ V vanishes on
𝒞₁(L/2) ∩ [1, B]. (Signed minorants: not covered — their validity domain is a cone, §5; no sign certificate computed.)
The no-zero-row ranks at L = 168 (16 at B = 4000, 3 at B = 40 000) are in `data/z60/signed/mixed_168_nozero.txt`.
**Finite-size caveat (EVIDENCE):** without zero rows the mixed T1-kernel restricted to 𝒞₁ is *larger* than the sum of the
per-ψ kernels (3, 9, 6 vs 1) — at these B the number of odd squares (100, 87, 87) is far below dim V, so many cross-ψ
cancellations at squares survive. Theorem S2(a) says they disappear when *all* odd squares are imposed; the finite
certificate does not rely on S2 (zero rows kill everything). At L = 168, B = 4000 the excess was 16, at B = 40 000 it is 3
(monotone decrease, as expected).

### 6.2 What the survivor lines see: G-specific Euler factors, not R (EVIDENCE)
`scripts/z60_signed_pseudosq.py L D 40000 G D′ 200 …` (cusp space, good odd squares, as WALDS's diag; outputs
`data/z60/signed/pseudosq_L_D.txt`). For each survivor line s (normalised primitive integral) and every squarefree
n ∈ 𝒞₁ ≤ 40 000: s(n); w(n) := s(n)²/√n (∝ L(½, G ⊗ χ_n) by Waldspurger Cor. 2); the partial Euler product
P_Y(n) = ∏_{ℓ≤200, good}(1 − a_ℓ(G)χ_n(ℓ)/ℓ + 1/ℓ)^{−1} of G ⊗ χ_n at the centre (the Birch–Swinnerton-Dyer "∏N_ℓ/ℓ"
statistic); R(n) by enumeration; n_p := least prime non-residue of n.

| (L, ψ), G | 𝒞₁-primes | s(p) = 0 by P_Y tercile (low/mid/high) | ρ_S(w, P_Y) | ρ_S(R, w) | ρ_S(R, n_p) | signs of s(p) ≠ 0 (+/−) | s at the 2 prime R-zeros 5569, 9601 |
|---|---|---|---|---|---|---|---|
| (168, χ₁₆₈), E₈₄ ⊗ χ_{−168} | 238 | 31/80, 19/79, 7/79 | 0.58 | 0.01 | −0.29 | 81/100 | 1, −1 |
| (280, χ₅₆), E₇₀ ⊗ χ_{−56} | 238 | 32/80, 14/79, 13/79 | 0.51 | −0.12 | −0.63 | 87/92 | 1, −1 |
| (560, χ₂₈₀), E₅₆ ⊗ χ_{−280} | 238 | 24/80, 23/79, 7/79 | 0.49 | 0.13 | −0.63 | 92/92 | 1, 1 |
| (420, χ₂₁), E₂₁₀ ⊗ χ_{−84} | 108 | 14/37, 6/36, 3/35 | 0.49 | −0.08 | 0.11 | 43/42 | **0, 0** |
| (420, χ₁₀₅), E₁₀₅ ⊗ χ_{−420} | 108 | 18/37, 11/36, 7/35 | 0.43 | 0.06 | 0.11 | 40/32 | **0, 0** |

(ρ_S = Spearman rank correlation over the 𝒞₁-primes; the squarefree-composite rows behave the same, see the files.
After internal review R11 the local factor at good ℓ | n is set to 1 (ramified twist); this changes only composite
rows — the prime rows and every number in the table are unchanged; driver `scripts/z60_signed_pseudosq_runs.sh` →
`data/z60/signed/pseudosq_summary.txt`. The interpretation of w as a central value inherits WALDS's line ↔ eigensystem
identification, EVIDENCE. Restricted to 𝔐-primes the sign counts are 30/42, 43/45, 40/40, 43/42, 40/32 (reviewer).)
Readings (EVIDENCE, finite range): (a) the Waldspurger dictionary is visible numerically — w tracks the partial Euler
product (ρ ≈ 0.43–0.58) and vanishing concentrates in the low-P_Y tercile; (b) **w is uncorrelated with R**
(|ρ_S(R, w)| ≤ 0.13 on all five lines), although R itself correlates with pseudo-squareness (ρ_S(R, n_p) down to −0.63);
the twisted central value weights the small primes by a_ℓ(G), a G-specific pattern, while R depends on the residue
pattern of n in a G-independent way. So the natural heuristic "both vanish at pseudo-squares, hence validity is
approximately automatic" is not supported (small rank correlation in a finite range — not a proof of independence);
(c) both signs occur at primes for every line in the tested range (which does not refute eventual constancy).

### 6.3 The L = 420 coincidence and *prime-only* validity (CERTIFIED ranks / EVIDENCE L-values)
WALDS §5.3 noted that both L = 420 survivors vanish at the (★)-zero primes 5569 and 9601. A line that vanished at *every*
(★)-zero prime of 𝔐 would be a "prime-only valid" proxy (g(p) ≠ 0 ⟹ R(p) ≥ 1 at primes — all that (MS) needs; TERNARY
§4.3's named escape), i.e. an L-function detector of R-zeros. Test (`scripts/z60_signed_zeros_rank.py`,
`scripts/z60_signed_t420.py`; outputs `zeros_rank_420.txt`, `t420_screen_run1.txt`, `t420_screen.txt`,
`t420_screen_102001.txt`): for all nine in-𝔐 (★)-zero primes, pari `ellrank` bounds (efforts 0–3) of G ⊗ χ_p
(rank ≥ 2 ⟹ L(½) = 0 unconditionally by Gross–Zagier–Kolyvagin; descent upper bound 0 ⟹ algebraic rank 0; the bounds
are CERTIFIED, their L-value reading is as stated below):

| p | 5569 | 9601 | 83449 | 102001 | 712321 | 1724209 | 1726201 | 5212561 | 8813281 |
|---|---|---|---|---|---|---|---|---|---|
| χ₂₁: E₂₁₀ ⊗ χ_{−84p} | 2 | 2 | 2 | **0** (L ≈ 0.380, num.) | 2 | **0** | 2 | 2 | **0** |
| χ₁₀₅: E₁₀₅ ⊗ χ_{−420p} | 2 | 2 | 2 | 2 | **0** | [0,2] | [0,2] | **0** | **0** |

(Root number +1 throughout; numerical analytic rank 2 at 5569, 9601, 83449 for both lines and at 102001 for χ₁₀₅.)
**Result (EVIDENCE; numerical / BSD-dependent).** Neither line is prime-valid, on the following evidence: the χ₂₁ line
is non-zero at the (★)-zero prime 102001 (numerical central value 0.380, analytic rank 0; W4(a) with any anchor t₀ where s(t₀) ≠ 0, e.g. t₀ = 1009; the identification of the computed line with
φ = E₂₁₀ is WALDS's EVIDENCE — so this is EVIDENCE, numerical) and has algebraic rank 0
at 1724209 and 8813281 (non-vanishing there needs BSD's converse direction — EVIDENCE); the χ₁₀₅ line has algebraic rank
0 at 712321, 5212561, 8813281 (EVIDENCE likewise). No combination K₁s₁ + K₂s₂ ≠ 0 vanishes at 102001 (χ₂₁ ≠ 0,
χ₁₀₅ = 0, so K₁ = 0) and at 712321 (χ₂₁ = 0, χ₁₀₅ ≠ 0 expected, so K₂ = 0) — conditional on the BSD-type reading at
712321. The coincidence is therefore not exact (on this evidence). Exact rank *bounds* are CERTIFIED; "non-zero" is numerical or
BSD-dependent; the line ↔ eigensystem identification is EVIDENCE; and a finite screen cannot exclude a proxy required
to be valid only beyond a larger threshold.
**Residual anomaly (EVIDENCE, weak; recorded for honesty).** Effort-matched base rates over 120 𝔐-primes in each band
(starting at 10⁵, 10⁶, 5·10⁶; `scripts/z60_signed_baserate.py`, `baserate_runs.txt`, `baserate_effort3.txt`,
`scripts/z60_signed_baserate_stats.py` → `baserate_stats.txt`): proven rank ≥ 2 in 24 %, 17 %, 12 % (χ₂₁) and 24 %,
18 %, 13 % (χ₁₀₅). At the seven zeros other than the two that motivated the test, χ₂₁ has proven rank 2 at 4/7
(expected 1.22; Poisson-binomial P(≥ 4) ≈ 0.019), χ₁₀₅ at 2/7 (expected 1.27; P ≈ 0.37). The other statistic
(pari's descent *upper bound* = 0 — not the 2-Selmer rank: pari's bound is C − T − s with C the 2-Selmer dimension, T the
2-torsion dimension and s the computed dimension of Sha[2]/2Sha[4]; internal review R8) shows no anomaly (χ₂₁: 3/7 vs
3.57 expected; χ₁₀₅: 3/7 vs 2.77). With two lines and two statistics tested (Bonferroni ≈ 0.08 for the smallest P), this
is not significant at the 5 % familywise level; in χ₂₁ the excess sits entirely in "upper bound 2 ⟹ two independent
points found" (4/4 at the zeros vs 29/55 = 53 %, 20/58 = 34 %, 14/64 = 22 % in the three base bands), which could reflect
Sha or point heights rather than ranks. These are plug-in exploratory tail probabilities, not a proved sampling model.
Not a lead.

## 7. What is left, verdict, screens, proposed FRONTIER text, bottom line

### 7.1 The map after this lane (PROVED pieces + Assessment)
For a *fixed-level* half-integral-weight proxy in the theta class and the square class 𝒞₁(2N) (⊇ the 𝔐-primes for
{3,5,7}-levels):
* **signed = support in weight 3/2, any mixture of quadratic nebentypus** (S1, S2(b)), and **in weight ≥ 5/2 for one
  nebentypus** (S3): T1⁻ at odd squares forces either eventual negativity at all large 𝒞₁-primes or the support-form
  structure (genus term 0 on 𝒞₁, unary t = 1 part 0, every Shimura anchor 0);
* **mixed ψ adds nothing for support proxies** (S2(a); also in weight ≥ 5/2) — on squarefree 𝒞₁ only exceptional (φ, ψ)
  components survive;
* **but mixed ψ in weight ≥ 5/2 escapes the signed form**: an explicit rank-5 Eisenstein combination satisfies T1⁻ and is
  positive at all primes ≡ 17 (mod 24) (§4.1; outside 𝔐; open on 𝔐);
* **cosets**: only a class-by-class statement and the termwise-recipe exclusion, CONDITIONAL on (SWc) (§4.2);
* **exponential growth** is square-blind under the dominance hypothesis (Dom) (Lemma S4, Cor S4′);
* **multi-eigensystem support proxies** (S5): cancellation is avoidable at all primes at once by generic real
  coefficients; a valid effective one exists ⟺ the non-degeneracy S(p) ∉ W for all large 𝒞₁-primes (which contains the
  prime target R(p) ≥ 1 there); with the Waldspurger dictionary and no non-square zeros it is the disjunction (𝒟_N),
  heuristically true for ≥ 5 independent rational exceptional lines (Assessment), far out of reach, and no substitute
  for a validity mechanism. For *signed* multi-eigensystem proxies the domain is a cone and the question is a joint
  sign-distribution one (open).
What is **not** covered and stays open (named escapes):
1. **A validity mechanism** (the real gap, at any level): an expansion g(n) = Σ_{certificates of n} w(cert) with
   structural weights, or any other non-termwise reason why g vanishes (support) or is ≤ 0 (signed) on the R-zeros.
   Termwise lattice/coset recipes cannot reach 𝒞₁ (W0; §4.2, CONDITIONAL for cosets). None is known.
2. **Off-𝒞₁ / varying level** (WALDS (E-e)): at primes p ∉ 𝒞₁(2N) the genus term survives and a *signed* proxy can be
   positive there (T1⁻ never sees classes with (p/q) = −1 for some q | N); validity there is equivalent to the target on
   that class (W5); a p-dependent level needs a prime q | N_p with (p/q) = −1, so q ≥ n_p — the B2 / n_p wall.
3. **Signed proxies with non-summable-free structure**: integral weight (AUTOMORPH Prop B1: 5σ₂ − (2n² + 3)τ) and mixed
   nebentypus in half-integral weight ≥ 5/2 (§4.1): T1⁻ does not constrain them; whether one is positive at all large
   𝔐-primes is easy in integral weight (B1) and open in weight ≥ 5/2; validity is the whole problem.
4. Non-quadratic nebentypus, coset cusp parts, non-genus Eisenstein / general mock objects of polynomial growth, forms
   failing (Dom); level sums / sections (AUTOMORPH E2, Fourier–Jacobi §4.4) — B2/H-A.

### 7.2 Verdict
**Narrowed** (no HOT LEAD). New PROVED scoped no-gos (relative to the cited inputs): S1 (signed T1 in weight 3/2, which
also yields WALDS W1 from prime squares alone), S2 (mixed quadratic nebentypus in weight 3/2: support and signed;
support also in weight ≥ 5/2), S3 (weight ≥ 5/2, one nebentypus, signed), Lemma S4 (square-blind asymptotics); Prop S5
(exact criterion for multi-eigensystem support proxies). CONDITIONAL: cosets (§4.2, class by class, on (SWc));
Cor S4′ (on (Dom)). A counterexample (internal review) shows the signed form does **not** extend to mixed nebentypus in
weight ≥ 5/2. CERTIFIED: mixed-ψ support-validity certificates at L = 168, 240, 280; rank bounds for 18 twists at the
nine in-𝔐 (★)-zero primes. EVIDENCE: survivor lines are (in the tested range) essentially rank-uncorrelated with R; the
L = 420 coincidence is not exact on numerical / BSD-dependent evidence (weak residual anomaly, not significant). The
brief's suggested closure for (E-a) — individual-line vanishing — is insufficient for support proxies with unrestricted
real coefficients (S5: cancellation can be avoided); what remains there is a non-degeneracy condition plus a validity
mechanism, neither supplied here.

### 7.3 Falsifier table (final)
Inventory: F1 all odd squares; F2 the 12 R₈-zero primes in [10¹⁰, 1.1·10¹⁰] (4 in 𝔐, largest 10 868 474 401); F3 the
285 non-square composite zeros ≤ 7 999 801 (15 in 𝔐, all squarefree); F4 the 14 (★)-zero primes (9 in 𝔐) and the 38
𝔊*-zero primes (20 in 𝔐; the 14 are among them).
| screen | behaviour of the best idea (fixed-level signed/multi-eigensystem proxies; S1–S5) |
|---|---|
| **F1 odd squares** | Used exactly once, at the anchor: T1⁻ (an inequality) is upgraded to the support-form conclusions at the t = 1 Shimura orbit and the genus density of m² (S1 Steps 1–4, S2 Steps 1–5, S3). Non-squareness enters as "t = p lies in a different Shimura orbit from t = 1, linked only through Waldspurger". Where T1⁻ does nothing — integral weight (AUTOMORPH B1) and mixed ψ in weight ≥ 5/2 (§4.1 counterexample) — the escape stays open. |
| **F2 C-even (R₈)** | All no-gos are line-blind and apply verbatim to R₈-proxies (R₈(m²) = 0): nothing false is proved. S5 is an equivalence; for R₈ it correctly demands R₈(p) ≥ 1 on 𝒞₁ beyond P₀, so P₀ ≥ 10 868 474 401 for R₈ on 𝔐-levels. Nothing in the survivor lines distinguishes C odd from C even. The 12 R₈ primes were not screened against the lines (conductors too large). |
| **F3 composites** | S1–S4 do not use composite data. S5's zero set Z contains the squarefree composite zeros of 𝒞₁ exactly like prime zeros; the mixed certificates (§6.1) used all R-zero rows ≤ B (squares and composites included; of the 285, those ≤ B) and kill every valid mixed support proxy on 𝒞₁ ∩ [1, B] at L = 168, 240, 280. Primality is never used beyond squarefreeness of t ∈ 𝒞₁ (as in WALDS). |
| **F4 known zeros** | §6.1 certificates (all R-zeros ≤ B); §6.2: three of the five computed lines are non-zero at 5569 and 9601 (the two in-𝒞₁ (★)-zero primes ≤ 4·10⁴), and lines are non-zero at composite zeros such as 1969, 2641, 5161; §6.3: the two L = 420 lines (zero at 5569, 9601) are, on numerical / BSD-dependent evidence, non-zero at 102001, 1724209, 8813281 (χ₂₁) resp. 712321, 5212561, 8813281 (χ₁₀₅) — all nine in-𝔐 (★)-zero primes screened. The other five (★)-zero primes (outside 𝔐) and the 𝔊*-zeros were not screened (𝔊*-zeros constrain only 𝔊*-support proxies, WALDS F4). |

### 7.4 FRONTIER §4 hard screens
T1 squares: S1/S2/S3 *are* T1 in signed form (with the weight ≥ 5/2 mixed-ψ exception). 8/131 (line): line-blind. Tied
modulus: invisible — the half-integral side sees only twisted central values, rank-uncorrelated with R in the tested
range (§6.2). Fixed p: everything is pointwise after the level is fixed; the positive direction (𝒟_N) is a fixed-p
disjunction of non-vanishings, not given by GRH.

### 7.5 Proposed FRONTIER text (do not edit FRONTIER here)
> *Signed and multi-eigensystem automorphic proxies (z60 SIGNED; PROVED rel. Siegel, Duke 1988 Thm 5, Waldspurger 1981
> Cor. 2, Rankin–Selberg / Jacquet–Shalika / Ogg–Shahidi at s = 1, Deligne).* In weight 3/2 the *signed* form of T1
> (g(m²) ≤ 0) is as strong as the support form, also for any mixture of quadratic nebentypus: a ternary-theta proxy is
> either negative at all large primes of the square class 𝒞₁ or, on squarefree 𝒞₁, a sum of Gauss-exceptional Shimura
> components (closes WALDS (E-c) and AUTOMORPH Q2′ in weight 3/2); the same holds in weight ≥ 5/2 for one nebentypus,
> but *not* for mixtures (explicit rank-5 counterexample positive at all p ≡ 17 mod 24, outside 𝔐). Cosets: class by
> class only, CONDITIONAL on coset Siegel–Weil. Exponentially growing objects with a dominant periodic term are
> square-blind on 1 (mod M). For several exceptional components, support proxies need no cancellation control
> (generic real coefficients avoid it at every prime at once): a valid effective proxy exists iff the coefficient
> vector S(p) avoids the span of its values at R-zeros for all large 𝒞₁-primes (this contains R(p) ≥ 1 there; with the
> Waldspurger dictionary and no non-square zeros: some L(½, G_j ⊗ χ_p) ≠ 0). No validity mechanism is supplied.
> CERTIFIED: mixed-ψ support-validity certificates at L = 168, 240, 280. The L = 420 survivors (zero at 5569, 9601)
> are not prime-valid on numerical/BSD-dependent evidence (102001, 712321, …). Open: a validity mechanism; off-𝒞₁ /
> p-dependent levels (q ≥ n_p, B2); signed proxies in integral weight (AUTOMORPH B1) and mixed-ψ weight ≥ 5/2.
> Add to §6: "signed (minorant) half-integral-weight proxies on 𝒞₁ in weight 3/2 (any quadratic ψ mixture) and for one ψ
> in higher weight; individual-line vanishing as a closure of multi-eigensystem support proxies (insufficient)".

### 7.6 Bottom line
The last automorphic escape left by AUTOMORPH/TERNARY/WALDS was "signed or multi-eigensystem proxies". In weight 3/2 it
closes in the expected way: replacing "g = 0 at odd squares" by "g ≤ 0 at odd squares" changes nothing, because the
only way to keep g(p) > 0 at large primes of the square class is for the genus term to vanish there, after which a
Rankin–Selberg sign argument kills every Shimura anchor, and mixing quadratic characters does not help. In higher weight
the same holds for one character, but a mixture of characters can satisfy the sign condition at squares and still be
positive on a positive-density set of primes of the square class (not on 𝔐 in the example found) — a genuine, if
unpromising, escape whose validity question is again the target. The multi-eigensystem question for support proxies
turns out to be mis-posed: cancellation between eigensystems can be avoided by generic coefficients, so no single-p
cancellation control is needed; what is needed is a non-degeneracy of twisted central values plus a reason for
validity, and this lane supplies neither. Numerically, the survivor lines follow their own Euler factors and are
rank-uncorrelated with R; the one striking coincidence (both L = 420 lines vanishing at the first two in-𝔐 (★)-zeros)
does not persist on numerical/BSD-dependent evidence. ES and (MS) remain open; the wall is again B2 — here in the form
"a reason for validity".

## 8. Literature verification log
Raw subagent report: `data/z60/signed/lit_verify_raw.md` (research mode). Lane checks:
| # | Used for | Source | How verified | Status |
|---|---|---|---|---|
| 1 | (Duk): weight-3/2 cusp coefficients ≪ t^{1/2−1/28+ε} at squarefree t; all weights ±1/2 + 2ℓ | W. Duke, Invent. Math. 92 (1988) 73–90, Thm 5 (§5) and pp. 74–76 ((1.2): Iwaniec, weight > 5/2, a(n) ≪ n^{k/2−2/7+ε}; "Theorem 5 includes the interesting case of holomorphic cusp forms of weight 3/2") | primary PDF (author-hosted scan of the published paper, math.ucla.edu/~wdduke/preprints/hyperbolic.pdf), text read | VERIFIED |
| 2 | (RS2): L(1+it, π × π′) ≠ 0 for π ≠ π′ (GL₂ × GL₂: Ogg; general: Shahidi); (RS1): L(s, π) ≠ 0 on Re s = 1 (Jacquet–Shalika 1976) | P. Sarnak, "Nonvanishing of L-functions on Re(s) = 1" (Shalika 60th birthday volume, 2002), §1 | primary PDF (publications.ias.edu/…/ShalikaBday2002.pdf), text read | VERIFIED (as stated there) |
| 3 | simple pole of L(s, φ × φ) at s = 1 | Rankin–Selberg theory (used in Sarnak §1 eq. (5) as the pole of L(s, π × π̃)) | standard; not separately quoted | standard |
| 4 | (Sie): L(1, χ_D) ≫_ε |D|^{−ε} | Siegel 1935 | classical; not re-read | standard |
| 5 | Waldspurger Prop. 1, Cor. 2 (any odd k ≥ 3), Shimura T(ℓ²) | inherited: WALDS `data/z59/walds/lit_verify.md` #1, #5, #13 (primary PDF read by WALDS; statements with general k) | inherited | as there |
| 6 | (SWc) Siegel's formula for lattice cosets | Weil, Acta Math. 113 (1965) located; exact coset statement/range not confirmed | subagent, partial | **not verified ⟹ §4.2 CONDITIONAL** |
| 7 | sign changes of half-integral coefficients | Bruinier–Kohnen 2008 Thm 2.1 (a(tn²), t fixed); Lester–Radziwiłł, Math. Ann. 379 (2021) Thms 1–2 (indices 8n, n odd squarefree; GRH for ≫X, unconditional X^{1−ε}); nothing for primes | subagent (primary records) + WALDS #11 | VERIFIED as stated; **no prime-index result found** |
| 8 | simultaneous non-vanishing of twists | nothing qualifying located | subagent | not found (used only in an Assessment) |
| 9 | Rademacher-type expansions (Cor S4′) | standard (Rademacher–Zuckerman; Bringmann–Ono) | not re-verified | Cor S4′ CONDITIONAL |
| 10 | Gross–Zagier–Kolyvagin (rank ≥ 2 ⟹ L(½) = 0) | inherited WALDS lit_verify #12 | inherited | as there |

## 9. Commands and files
All runs: `ulimit -v 4000000`, `timeout` ≤ 1800, ≤ 2 concurrent compute processes; Python via `uv run --with cypari2`.
* `bash scripts/z60_signed_mixed_runs.sh` → `data/z60/signed/mixed_runs.txt` (§6.1). Single runs:
  `scripts/z60_signed_mixed.py 168 4000 0 4 0` (excess 16, console), `… 168 40000 0 4 0` (excess 3, console);
  `… 168 90000 0 4 0` overflowed the PARI stack (`mixed_168_B90000.log`).
* `bash scripts/z60_signed_pseudosq_runs.sh > data/z60/signed/pseudosq_summary.txt` (runs
  `scripts/z60_signed_pseudosq.py L D 40000 "[a-invariants]" D′ 200 data/z60/signed/pseudosq_L_D.txt` for
  (168,168,E₈₄,−168), (280,56,E₇₀,−56), (560,280,E₅₆,−280), (420,21,E₂₁₀,−84), (420,105,E₁₀₅,−420); §6.2).
* `python3 scripts/z60_signed_rank5_check.py 20000 > data/z60/signed/rank5_check.txt` (§4.1 counterexample check).
* L = 168 no-zero-row runs: `scripts/z60_signed_mixed.py 168 {4000,40000} 0 4 0` → `mixed_168_nozero.txt`.
* `scripts/z60_signed_t420.py 2e15` (first run, killed after 83449: `t420_screen_run1.txt`), `… 2e15 83449,…`
  (`t420_screen.txt`, killed during an analytic-rank computation), `… 2e15 102001` (`t420_screen_102001.txt`);
  `scripts/z60_signed_zeros_rank.py <9 zeros> 3` → `zeros_rank_420.txt`.
* `scripts/z60_signed_baserate.py X 25|120 line [2]` → `baserate_chi21_8e4.txt`, `baserate_runs.txt`;
  `scripts/z60_signed_zeros_rank.py <the 360 base primes> 3` → `baserate_effort3.txt`;
  `python3 scripts/z60_signed_baserate_stats.py` → `baserate_stats.txt` (§6.3).

## 10. Review log
* **Internal hostile review** (deep-mode subagent; `data/z60/signed/internal_review.md`): 1 FATAL, 7 MAJOR, 5 MINOR. It
  re-derived S1 (all steps, incl. the s → 1⁺ Rankin–Selberg sign argument and Remark (1)), S2 for quadratic ψ in weight
  3/2 (Lemma 3.1, distinctness, Steps 1–5), single-ψ S3, Lemma S4 and the support version of S5 — all pass; re-ran the
  rank screen at 102001, 712321, 8813281 and the base-rate statistics (reproduced); recomputed the §6.2 table from the
  saved rows (all numbers reproduce); verified Duke 1988 Thm 5 (normalisation a(n) = (4πn)^{κ/2}ρ(n), eq. (2.5)) and the
  Sarnak note independently. Repairs:
  * FATAL R1 (mixed-ψ S3 false): S3 restricted to one nebentypus; the reviewer's rank-5 counterexample added to §4.1 with
    a numerical check (`rank5_check.txt`); mixed higher-weight signed proxies listed as an open escape; title, §0, §7
    corrected. The support version for mixtures in higher weight is kept (Dedekind step needs only distinctness).
  * R2 (cosets): §4.2 now states only the class-by-class conclusion and the termwise-recipe exclusion, both CONDITIONAL
    on (SWc); the reviewer's −θ_{5ℤ³+(1,0,0)} example recorded.
  * R3 (signed validity is a cone): §5 "Signed version" rewritten; §6.1 no longer claims transfer to signed proxies.
  * R4 (S5 scope / dictionary): V and Λ made explicit; Consequence 3 now CONDITIONAL on W1′'s hypotheses, phrased for
    signed square-root coefficient vectors; §7.5 uses the coefficient-vector criterion.
  * R5 (MS⁺ / circularity overreach): Consequence 1 is the prime target only; Consequence 4 rewritten ("no validity
    mechanism is supplied"; validity need not be circular); §7 wording adjusted.
  * R6 (S4′): explicit hypothesis (Dom); fallback claim deleted (case unresolved).
  * R7 (qualifications): numerical / BSD-dependent / identification caveats propagated to §0, §6.3, §7.
  * R8 (pari's ellrank upper bound ≠ Selmer rank): renamed and explained; base fractions 53 %/34 %/22 % corrected.
  * R9–R13: S2 Remark (1) weakened; S5 wording (level raise, free coordinates, infinitely many squares, W = 0 condition);
    PY statistic fixed at ramified ℓ (prime rows unchanged) and rerun; falsifier inventory with full counts and "three of
    five lines"; P₀ ≥; L = 168 logs saved; §8 item references fixed.
