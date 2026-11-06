# Z60_SIGNED — signed and multi-eigensystem automorphic proxies: in half-integral weight the signed form of T1 is as strong as the support form (any mixture of nebentypus, any odd rank); exponential objects are square-blind; for several eigensystems cancellation is never the obstruction — what remains is (MS) itself plus a non-degeneracy of twisted central values. Verdict: narrowed, no HOT LEAD

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
| **F1 odd squares** | This is the whole content of §2–§3. The signed form only gives the *inequality* g(m²) ≤ 0, which in integral weight does **not** force anything (AUTOMORPH Prop B1: 5σ₂ − (2n²+3)τ is ≤ 0 at all odd squares, = p² − 1 > 0 at all primes). **Theorem S1/S2 (PROVED rel. cited inputs):** in half-integral weight the inequality at prime squares (S1) resp. at good squarefree-index squares (S2, mixed nebentypus) is as strong as the equality: either the genus main term is *negative* on 𝒞₁ (then g(p) < 0 at every large prime of 𝒞₁, so the proxy is never positive there) or it vanishes on 𝒞₁ together with every t = 1 unary series and every Shimura component's anchor a(1), so on squarefree 𝒞₁ only Gauss-exceptional eigensystems survive (as in WALDS W1). Non-squareness is used at the t = 1 Shimura orbit (anchor) and at the genus density of m². |
| **F2 C-even (R₈)** | All negative statements (S1, S2, S4) are line-blind: they apply verbatim to R₈-minorants (R₈(m²) = 0), so nothing false is proved. The positive statement (Prop S5, reduction of effectiveness to a linear non-degeneracy) is an *equivalence* and applies to R₈ too; there it correctly requires R₈(p) ≥ 1 beyond the threshold on 𝒞₁, so any R₈-version must start above the 4 in-𝔐 R₈-zeros (largest 10 868 474 401). |
| **F3 composites** | Not used by S1/S2 (identities at squares + analytic bounds at primes). Squarefree composite zeros in 𝒞₁ enter the validity space exactly like prime zeros (S5: Z contains them). Mixed-nebentypus certificates (§5) use all known R-zero rows, composites included. |
| **F4 known zeros** | Nothing is proved positive. §6.1: at L = 168, 240, 280 every valid *mixed-ψ* proxy vanishes on 𝒞₁ ∩ [1, B] (CERTIFIED, all R-zero rows). §6.3: the two L = 420 lines vanishing at 5569, 9601 are not prime-valid (102001, 712321, 1724209, 5212561, 8813281). |

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

**Remarks.** (1) The *prime-square* hypothesis alone does **not** suffice for mixed ψ: at m = ℓ the relation only gives
Σ_ψ E_ψ(1) = 0, C_φ = 0 and E_ψ(1) + D_ψ = 0 (the cusp anchors can absorb the second-order Eisenstein terms
ε_ψ(ℓ)E_ψ(1)); composite good m (Lemma 3.1) separate them. Valid proxies satisfy T1 at all odd squares, so this is moot
for them. (2) Non-quadratic ψ (forms on Γ₁(4N) beyond the ternary-theta class) — the same proof works with complex
a_ℓ(φ) (φ of nebentypus ψ²), conjugate pairs of components, and |G|² in place of G² (Rankin–Selberg against φ̄′);
stated only for quadratic ψ here. (3) TERNARY §4.4's gap "mixed nebentypus: only Σ_δ E_δ(1) = 0 follows" is exactly
Remark (1): it disappears once composite squares are used.

## 4. The other fixed-level objects of the brief: higher weight, cosets, exponential growth, Fourier–Jacobi

### 4.1 Proposition S3 — higher half-integral weight (WALDS escape (E-d)); PROVED rel. the listed inputs
Let κ = k/2, k odd ≥ 5, g = Σcᵢθ_{Lᵢ} + h ∈ M_κ(Γ₀(4N), ψ) with Lᵢ positive lattices of rank k (theta series of weight
κ), h cuspidal, real coefficients; or a finite sum of such over quadratic ψ. Inputs: Siegel's formula in rank k ≥ 5
(classical; on 𝒞₁ the genus part is A·B(n) with B(n) = n^{κ−1}∏_{ℓ∤2N}α_ℓ(L₁, n) ≍ n^{κ−1}, the Euler product now
converging absolutely to a value bounded above and below — no Siegel-zero issue); Waldspurger Prop. 1 / Cor. 2 for
general odd k (as read from the primary source by WALDS, lit_verify #1, #5, stated there with weight k/2 and
χ₀(n) = χ(n)(−1/n)^{(k−1)/2}); Duke Thm 5 (all weights ±1/2 + 2ℓ: a(t) ≪ t^{κ/2−2/7+ε} at squarefree t); (RS*) for
weight-(k−1) newforms with λ_ℓ := a_ℓ/ℓ^{κ−1}.
**Statement.** If g(ℓ²) ≤ 0 for all large primes ℓ (one ψ; for several ψ: g(m²) ≤ 0 for good m), then either
g(p) < 0 for all large primes p ∈ 𝒞₁(2N), or E ≡ 0 on 𝒞₁ and every Shimura anchor vanishes, so that on squarefree
t ∈ 𝒞₁, t > 1, only components with L(½, φ ⊗ χ₀^{−1}) = 0 survive (χ₀^{−1} = ψ for k ≡ 1 (4), ψχ_{−4} for k ≡ 3 (4)).
*Proof.* As §2/§3, with three simplifications: there are no unary theta series of weight ≥ 5/2; the genus term at ℓ²
is E(1)ℓ^{2κ−2}(1 + O(1/ℓ)), which dominates the cusp term (a_ℓ(φ) − ψ(ℓ)(−1/ℓ)^{(k−1)/2}ℓ^{κ−3/2})c_φ = O(ℓ^{κ−1})
(Shimura's T(ℓ²) in weight κ; Deligne), so (T1⁻) gives E(1) ≤ 0 at once; and in case E(1) < 0 the bound
|E(p)| ≫ p^{κ−1} beats the cusp bound p^{κ/2−2/7+ε} for κ ≥ 5/2. In case E(1) = 0, divide the cusp relation by
ℓ^{κ−1}: the ε-term is O(ℓ^{−1/2}) and §2 Step 4 (resp. §3 Steps 4–5) applies verbatim. ∎

### 4.2 Cosets / theta series with characteristics (WALDS escape (E-b)); CONDITIONAL
For a coset L + v (v ∈ ℚL), θ_{L+v} is modular on Γ₁(M) for suitable M, with characters that need not be quadratic.
**Claim (CONDITIONAL on (SWc): Siegel's formula for lattice cosets — θ_{gen(L+v)}, the weighted average over the genus of
the coset with positive weights, has coefficients c·√n·∏_ℓ α_ℓ(L+v, n), and θ_{L+v} − θ_{gen(L+v)} is cuspidal).**
The literature check (§8) located Weil 1965 (Schwartz–Bruhat Siegel formula) but did not confirm the precise statement
or range; hence CONDITIONAL. *Sketch.* At good ℓ the coset is the lattice, so the good-prime product B(n) is as before;
at q | M the coset density α_q(L + v, n) is a locally constant function of n ∈ ℤ_q^× of some finite modulus q^K (it is no
longer invariant under all unit squares). Restrict to a class n ≡ s (mod M^K) with s a unit square mod M^K. Every
prime p ∈ 𝒞₁(2M) lies in such a class, and so does ℓ² for every prime ℓ ≡ √s (mod M^K) (Dirichlet). On that class the
genus part is β(s)·B(n) with β(s) real, so the §2 Steps 1–2 argument, run with ℓ restricted to ℓ² ≡ s, gives
β(s) ≤ 0 under (T1⁻), and g(p) < 0 at large primes p ≡ s if β(s) < 0. Weight-3/2 unary coset series contribute
m·(1_{m ≡ v} − 1_{−m ≡ v}) at m², odd in m, and die as in Step 3; the cusp part is a Γ₁-form, handled by §3 Remark (2)
(complex characters, Rankin–Selberg against conjugates). So cosets behave like lattices: on 𝒞₁ a valid support or
signed coset proxy is (eventually negative or) a pure exceptional-cusp sum. In particular termwise coset recipes
(non-negative combinations of θ_{L+v} with every representation yielding a certificate) represent nothing in 𝒞₁ — the
coset version of WALDS Lemma W0, by the same positivity-of-weights argument under (SWc).

### 4.3 Lemma S4 — square-blind asymptotics (exponential growth: weakly holomorphic, Rademacher, mock with principal part)
**Lemma S4 (PROVED, elementary).** Let g : ℕ → ℝ, M ≥ 1, and suppose that along n ≡ 1 (mod M),
g(n) = F(n)(1 + o(1)) with F eventually non-zero of constant sign. If g(m²) ≤ 0 for all large odd m, then g(p) < 0
for every sufficiently large prime p ≡ 1 (mod M) — a set containing a positive proportion of the 𝔐-primes.
*Proof.* Odd m ≡ 1 (mod M) have m² ≡ 1 (mod M), so F(m²) ≤ 0 for large such m; F has eventually constant sign, so
F < 0 eventually, and g(p) = F(p)(1 + o(1)) < 0. ∎
**Corollary S4′ (CONDITIONAL on the standard exact/asymptotic Rademacher-type formula, cited not re-verified).** Let g be
weakly holomorphic (or the holomorphic part of a harmonic Maass form) of real weight with non-zero principal part, so
that a(n) = Σ_{c} k_c(n)·Φ_c(n) + O(n^A) with k_c(n) periodic in n of period c (Kloosterman/Salié sums against the
principal part) and Φ_c(n) > 0 growing like exp(4π√(m₀n)/c). If k_c(1) ≠ 0 for some c, put c* := the least such c and
M := lcm{c ≤ c*}: on n ≡ 1 (mod M) the terms c < c* vanish, the c* term dominates the tail, and Lemma S4 applies —
**a signed minorant with genuinely exponential coefficients on the square class is negative at all large primes
≡ 1 (mod M).** If k_c(1) = 0 for every c, the principal part contributes o(exp(ε√n)) on n ≡ 1 (mod M(ε)), and such a
proxy falls back to the polynomial-growth (holomorphic / mock-Eisenstein) analysis, which §§2–4.1 cover for the
theta-type classes and which is not done here for general mock objects.
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

## 5. Multi-eigensystem cancellation (WALDS escape (E-a)): cancellation is never the obstruction

Fix a level (N, Ψ) as in §3. Let Λ be the real vector space of restrictions to 𝒞₁(2N) of all g ∈ ⊕_{ψ∈Ψ}M_{3/2}(Γ₀(4N), ψ)
with g(m²) = 0 for every odd m (finite-dimensional; by Thm S2(a) and W1′, on squarefree t > 1 its elements are
combinations of the exceptional lines). Fix a basis s₁, …, s_k of Λ and put S(n) := (s₁(n), …, s_k(n)) ∈ ℝ^k for
n ∈ 𝒞₁. Each g_K := Σ_j K_j s_j, extended by 0 off 𝒞₁, is again a modular form (projection to a union of residue
classes mod 8∏_{q|N}q is a finite twist) and still vanishes at every odd square (squares outside 𝒞₁ are set to 0, those
inside are already 0). Let Z := {n ∈ 𝒞₁(2N) : R(n) = 0} and W := span_ℝ{S(z) : z ∈ Z} ⊆ ℝ^k.

**Proposition S5 (PROVED, elementary).** For P₀ ≥ 1 the following are equivalent:
(i) some g_K is a valid support proxy (g_K(n) ≠ 0 ⟹ R(n) ≥ 1 for all n) and g_K(p) ≠ 0 for every prime p ∈ 𝒞₁, p > P₀;
(ii) S(p) ∉ W for every prime p ∈ 𝒞₁, p > P₀.
Moreover, when (ii) holds, the set of K giving such a proxy is the complement in W^⊥ of countably many proper
subspaces (so "almost every" valid K works), and K may be taken with coordinates algebraically independent over the
field generated by all values S(n) restricted to W^⊥-coordinates.
*Proof.* g_K is valid iff g_K(z) = 0 for all z ∈ Z (off 𝒞₁ it is 0), i.e. iff K ∈ W^⊥ (annihilator for the pairing
⟨K, S⟩ = Σ K_jS_j). (ii) ⟹ (i): for each such p, H_p := {K ∈ W^⊥ : ⟨K, S(p)⟩ = 0} is a proper subspace of W^⊥, since
S(p) ∉ W = (W^⊥)^⊥ (finite dimension). A real vector space is not a countable union of proper subspaces (each is
Lebesgue-null), so some K ∈ W^⊥ avoids every H_p. (i) ⟹ (ii): K ∈ W^⊥ and ⟨K, S(p)⟩ ≠ 0 force S(p) ∉ W. ∎

**Consequences (PROVED from S5 + W1′ + S2, scoped to this class).**
1. *(i) contains (MS) on 𝒞₁ above P₀*: if p ∈ Z then S(p) ∈ W. (This is WALDS Prop W5 again, now as one side of an
   equivalence.)
2. *Cancellation can always be avoided.* If (ii) holds, a generic valid K has g_K(p) ≠ 0 at **every** prime of 𝒞₁ above
   P₀ simultaneously; no single-p control of cancellation is required. The brief's suggested closure ("each exceptional
   piece vanishes at infinitely many 𝔐-primes — can cancellation be controlled?") therefore cannot close (E-a): even if
   every line vanishes infinitely often (CKRS, WALDS §4.1), a generic sum vanishes only where **all** lines vanish
   modulo W. WALDS's heuristic "pure-cusp proxies vanish at T^{3/4+o(1)} primes" concerns proxies with *rational*
   coefficients (a single rational number per p, CKRS discretisation); it does not apply to generic K.
3. *What actually remains* is the non-degeneracy (ii). Under W1′ (each line's t-th entry is ±(const)·t^{1/4}·
   L(½, G_j ⊗ χ_t)^{1/2}), if W = 0 — i.e. 𝒞₁(2N) contains no R-zero — (ii) reads
   **(𝒟_N): for every prime p ∈ 𝒞₁(2N), p > P₀, some exceptional G_j has L(½, G_j ⊗ χ_p) ≠ 0** —
   a *disjunction* of central-value non-vanishings, a statement about L-functions alone. If W ≠ 0, (ii) is the
   condition that S(p) avoids a fixed proper subspace spanned by the zero vectors.
4. *Validity is still (MS).* (i) presupposes knowing Z (all R-zeros in 𝒞₁); K ∈ W^⊥ is chosen *from* Z. So the proxy
   route on 𝒞₁ is exactly "(MS⁺ on 𝒞₁) ∧ (non-degeneracy)": it re-packages (MS) and adds an L-function condition; it
   supplies no reason for validity. A proof of (MS) through it would need an *independent identity* forcing g_K to
   vanish on Z — e.g. an expansion g_K(n) = Σ_{certificates of n} w with structural weights. None is known; termwise
   recipes are excluded on 𝒞₁ (W0; cosets §4.2).
5. *Heuristic status of (𝒟_N) (Assessment).* For k independent rational exceptional G_j with CKRS-type vanishing
   probability p^{−1/4+o(1)} each, simultaneous vanishing has probability p^{−k/4+o(1)}, summable over primes for k ≥ 5:
   (𝒟_N) is then expected to hold above some P₀ (finitely many exceptions). So, unlike single-eigensystem positivity,
   the multi-eigensystem condition is *not* expected to fail — the escape (E-a) is heuristically consistent, and
   provably non-closable by vanishing statements about individual lines. Known non-vanishing technology gives only
   positive-proportion / infinitely-many results for one or two forms (§8 item 5: no simultaneous result verified), so
   (𝒟_N) for all large p is far out of reach; it is not B2, but it is not progress on B2 either.

**Signed version.** With signs, (i) becomes "some K ∈ W^⊥ has ⟨K, S(p)⟩ > 0 for all large p ∈ 𝒞₁", i.e. the projected
vectors π(S(p)) ∈ (W^⊥)* all lie in one open half-space. For a single line this is "the sign of s(p) is eventually
constant", which fails numerically for every survivor computed (§6.2: both signs occur at primes of 𝔐 for all five
lines); sign-equidistribution conjectures (Bruinier–Kohnen type; proven results cover a(tn²) with t fixed, or
fundamental discriminants 8n under GRH — Lester–Radziwiłł Thm 1 — never primes, §8 item 4) would make it fail for any
fixed k. So the *signed* multi-eigensystem route is expected (CONJECTURE) to be ineffective, while the *support* route
is expected to be effective but is circular (point 4).

## 6. Computations

### 6.1 Mixed-nebentypus validity certificates (CERTIFIED, exact rational linear algebra)
`scripts/z60_signed_mixed.py L B 0 4 zrows` (driver `scripts/z60_signed_mixed_runs.sh`, output `data/z60/signed/mixed_runs.txt`):
V = ⊕_ψ M_{3/2}(Γ₀(L), ψ) over **all** quadratic ψ = (D/·) with D = 1 or a positive fundamental discriminant | L (8
characters at each level), full spaces; rows g(m²) = 0 for all odd m ≤ √B and (zrows = 1) g(z) = 0 at every n ≡ 1 (4),
n ≤ B, with R(n) = 0 (LOGIC census list, squares and composites included).

| L | B | dim V | rows (zero rows) | rank of mixed kernel on 𝒞₁ ∩ [1, B] | same, without zero rows | Σ_ψ per-ψ ranks (no zero rows) |
|---|---|---|---|---|---|---|
| 168 | 40 000 | 176 | 169 (168) | **0** | 3 | 1 (ψ = χ₁₆₈) |
| 240 | 30 000 | 272 | 150 (149) | **0** | 9 | 1 (ψ = χ₁₂₀) |
| 280 | 30 000 | 240 | 150 (149) | **0** | 6 | 1 (ψ = χ₅₆) |

**CERTIFIED:** at L ∈ {168, 240, 280}, every valid mixed-nebentypus proxy g ∈ V (support form) vanishes on
𝒞₁(L/2) ∩ [1, B]. (For signed minorants the analogous finite certificate would need sign rows; not computed — Thm S2(b)
reduces them to the same kernel asymptotically.)
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

(ρ_S = Spearman rank correlation over the 𝒞₁-primes; the squarefree-composite rows behave the same, see the files.)
Readings (EVIDENCE, finite range): (a) the Waldspurger dictionary is visible numerically — w tracks the partial Euler
product (ρ ≈ 0.43–0.58) and vanishing concentrates in the low-P_Y tercile; (b) **w is uncorrelated with R**
(|ρ_S(R, w)| ≤ 0.13 on all five lines), although R itself correlates with pseudo-squareness (ρ_S(R, n_p) down to −0.63);
the twisted central value weights the small primes by a_ℓ(G), a G-specific pattern, while R depends on the residue
pattern of n in a G-independent way. So the natural heuristic "both vanish at pseudo-squares, hence validity is
approximately automatic" is not supported; (c) signs are balanced at every line (signed single-line proxies are not
eventually positive in the computed range).

### 6.3 The L = 420 coincidence and *prime-only* validity (CERTIFIED ranks / EVIDENCE L-values)
WALDS §5.3 noted that both L = 420 survivors vanish at the (★)-zero primes 5569 and 9601. A line that vanished at *every*
(★)-zero prime of 𝔐 would be a "prime-only valid" proxy (g(p) ≠ 0 ⟹ R(p) ≥ 1 at primes — all that (MS) needs; TERNARY
§4.3's named escape), i.e. an L-function detector of R-zeros. Test (`scripts/z60_signed_zeros_rank.py`,
`scripts/z60_signed_t420.py`; outputs `zeros_rank_420.txt`, `t420_screen_run1.txt`, `t420_screen.txt`,
`t420_screen_102001.txt`): for all nine in-𝔐 (★)-zero primes, pari `ellrank` bounds (efforts 0–3) of G ⊗ χ_p
(rank ≥ 2 ⟹ L(½) = 0 unconditionally by Gross–Zagier–Kolyvagin; upper bound 0 ⟹ algebraic rank 0):

| p | 5569 | 9601 | 83449 | 102001 | 712321 | 1724209 | 1726201 | 5212561 | 8813281 |
|---|---|---|---|---|---|---|---|---|---|
| χ₂₁: E₂₁₀ ⊗ χ_{−84p} | 2 | 2 | 2 | **0** (L ≈ 0.380, num.) | 2 | **0** | 2 | 2 | **0** |
| χ₁₀₅: E₁₀₅ ⊗ χ_{−420p} | 2 | 2 | 2 | 2 | **0** | [0,2] | [0,2] | **0** | **0** |

(Root number +1 throughout; numerical analytic rank 2 at 5569, 9601, 83449 for both lines and at 102001 for χ₁₀₅.)
**Result.** Neither line is prime-valid: the χ₂₁ line is non-zero at the (★)-zero prime 102001 (numerical central value
0.380, analytic rank 0; W4(a) with any anchor t₀ where s(t₀) ≠ 0, e.g. t₀ = 1009; the identification of the computed line with
φ = E₂₁₀ is WALDS's EVIDENCE — so this is EVIDENCE, numerical) and has algebraic rank 0
at 1724209 and 8813281 (non-vanishing there needs BSD's converse direction — EVIDENCE); the χ₁₀₅ line has algebraic rank
0 at 712321, 5212561, 8813281 (EVIDENCE likewise). No combination K₁s₁ + K₂s₂ ≠ 0 vanishes at 102001 (χ₂₁ ≠ 0,
χ₁₀₅ = 0, so K₁ = 0) and at 712321 (χ₂₁ = 0, χ₁₀₅ ≠ 0 expected, so K₂ = 0) — conditional on the BSD-type reading at
712321. The coincidence is therefore not exact.
**Residual anomaly (EVIDENCE, weak; recorded for honesty).** Effort-matched base rates over 120 𝔐-primes in each band
(starting at 10⁵, 10⁶, 5·10⁶; `scripts/z60_signed_baserate.py`, `baserate_runs.txt`, `baserate_effort3.txt`,
`scripts/z60_signed_baserate_stats.py` → `baserate_stats.txt`): proven rank ≥ 2 in 24 %, 17 %, 12 % (χ₂₁) and 24 %,
18 %, 13 % (χ₁₀₅). At the seven zeros other than the two that motivated the test, χ₂₁ has proven rank 2 at 4/7
(expected 1.22; Poisson-binomial P(≥ 4) ≈ 0.019), χ₁₀₅ at 2/7 (expected 1.27; P ≈ 0.37). The effort-robust statistic
(Selmer rank 0) shows no anomaly (χ₂₁: 3/7 vs 3.57 expected; χ₁₀₅: 3/7 vs 2.77). With two lines and two statistics
tested, P ≈ 0.02 is not significant; in χ₂₁ the excess sits entirely in "Selmer rank 2 ⟹ points found" (4/4 at the
zeros vs roughly 35–50 % in the base), which could reflect Sha[2] or point heights rather than ranks. Not a lead.

## 7. What is left, verdict, screens, proposed FRONTIER text, bottom line

### 7.1 The map after this lane (PROVED pieces + Assessment)
For a *fixed-level* half-integral-weight proxy in the theta class (lattices of odd rank ≥ 3, any finite mixture of
quadratic nebentypus, support or signed; cosets CONDITIONAL on (SWc)) and the square class 𝒞₁(2N) (⊇ the 𝔐-primes for
{3,5,7}-levels):
* **signed = support** (S1, S2(b), S3): T1⁻ at odd squares forces either eventual negativity at all large 𝒞₁-primes or
  the support-form structure (genus term 0 on 𝒞₁, unary t = 1 part 0, every Shimura anchor 0);
* **mixed ψ adds nothing** (S2): on squarefree 𝒞₁ only exceptional (φ, ψ) components survive;
* **exponential growth is square-blind** (S4, S4′ CONDITIONAL): on the class 1 (mod M) primes and squares have the same
  dominant term;
* **multi-eigensystem sums** (S5): cancellation is avoidable at all primes at once by generic coefficients; a valid
  effective proxy exists ⟺ (MS on 𝒞₁ beyond P₀) ∧ (non-degeneracy S(p) ∉ W); with no zeros in 𝒞₁ the latter is the
  disjunction (𝒟_N) of twisted central-value non-vanishings, heuristically true for ≥ 5 independent rational exceptional
  lines (Assessment), unprovable with current technology, and in any case **no substitute for a validity mechanism**.
What is **not** covered and stays open (named escapes):
1. **A validity identity** (the real gap, at any level): an expansion g(n) = Σ_{certificates of n} w(cert) with structural
   weights w, or any other non-termwise reason why g vanishes on the R-zeros. Termwise lattice/coset recipes cannot reach
   𝒞₁ (W0; §4.2). No candidate is known.
2. **Off-𝒞₁ / varying level** (WALDS (E-e)): at primes p ∉ 𝒞₁(2N) the genus term survives and a *signed* proxy can be
   positive there (T1⁻ never sees classes with (p/q) = −1 for some q | N); validity there is (MS) on that class (W5); a
   p-dependent level needs a prime q | N_p with (p/q) = −1, so q ≥ n_p — the B2 / n_p wall.
3. **Integral weight, signed form**: AUTOMORPH Prop B1 stands — T1⁻ does not constrain 𝓗 (5σ₂ − (2n² + 3)τ is ≤ 0 at odd
   squares and p² − 1 at primes). Effective T1⁻-compatible signed functions exist there; validity is the whole problem.
4. Non-quadratic nebentypus and non-genus Eisenstein / general mock objects of polynomial growth (S2 Remark (2) indicates
   the proof extends; not written out); level sums / sections (AUTOMORPH E2, Fourier–Jacobi §4.4) — B2/H-A.

### 7.2 Verdict
**Narrowed** (no HOT LEAD). New PROVED scoped no-gos (relative to the cited inputs): S1 (signed T1 in weight 3/2, also
giving WALDS W1 from prime squares alone), S2 (mixed nebentypus, support and signed), S3 (higher half-integral weight),
Lemma S4 (square-blind asymptotics); Prop S5 (exact reduction of the multi-eigensystem escape). CONDITIONAL: cosets
(§4.2, on coset Siegel–Weil), Cor S4′ (on Rademacher-type expansions). CERTIFIED: mixed-ψ validity certificates at
L = 168, 240, 280; ranks of 18 twists at the nine in-𝔐 (★)-zero primes. EVIDENCE: survivor lines are uncorrelated with R;
the L = 420 coincidence is not exact (weak residual anomaly, not significant). The brief's suggested closure for (E-a)
("each exceptional piece vanishes infinitely often, so cancellation cannot be controlled") is shown to be the wrong
target: by S5 cancellation can always be avoided; what remains is a non-degeneracy condition plus validity, and validity
is (MS).

### 7.3 Falsifier table (final)
| screen | behaviour of the best idea (fixed-level signed/multi-eigensystem proxies; S1–S5) |
|---|---|
| **F1 odd squares** | Used exactly once, at the anchor: T1⁻ (an inequality) is upgraded to the support-form conclusions at the t = 1 Shimura orbit (S1 Steps 1–4, S2 Steps 1–5) and the genus density of m². Non-squareness is the step "t = p lies in a different Shimura orbit from t = 1, linked only through Waldspurger". In integral weight T1⁻ does nothing (AUTOMORPH B1) — the reason that escape stays open. |
| **F2 C-even (R₈)** | All no-gos are line-blind and apply verbatim to R₈-proxies (R₈(m²) = 0): nothing false is proved. S5 is an equivalence; for R₈ it correctly demands R₈(p) ≥ 1 on 𝒞₁ beyond P₀, so P₀ > 10 868 474 401 for R₈ on 𝔐-levels. The pseudo-square test (§6.2) shows the survivor lines track G-specific Euler factors; nothing in them distinguishes C odd from C even. |
| **F3 composites** | S1–S4 do not use composite data. S5's zero set Z contains the squarefree composite zeros of 𝒞₁ exactly like prime zeros; the mixed certificates (§6.1) used all R-zero rows ≤ B (composites and squares included) and kill every valid mixed proxy on 𝒞₁ ∩ [1, B] at L = 168, 240, 280. Primality is never used beyond squarefreeness of t ∈ 𝒞₁ (as in WALDS). |
| **F4 known zeros** | §6.1 certificates; §6.2: survivor lines are non-zero at known in-class R-zeros (e.g. 1969, 2641, 5161; 5569, 9601 for four lines); §6.3: the two L = 420 lines, which vanish at 5569, 9601 and (χ₂₁) at four further (★)-zero primes, are non-zero (numerically) / have rank 0 at 102001, 1724209, 8813281 resp. 712321, 5212561, 8813281 — no prime-only valid line or combination at L = 420. 𝔊*-zeros: not screened (they constrain 𝔊*-support proxies only, WALDS F4). |

### 7.4 FRONTIER §4 hard screens
T1 squares: S1/S2/S3 *are* T1 in signed form. 8/131 (line): line-blind. Tied modulus: invisible — the half-integral side
sees only central values L(½, G ⊗ χ_p), uncorrelated with R (§6.2). Fixed p: everything is pointwise after the level is
fixed; the positive direction (𝒟_N) is a fixed-p disjunction of non-vanishings, not given by GRH.

### 7.5 Proposed FRONTIER text (do not edit FRONTIER here)
> *Signed and multi-eigensystem automorphic proxies (z60 SIGNED; PROVED rel. Siegel, Duke 1988 Thm 5, Waldspurger 1981
> Cor. 2, Rankin–Selberg/Jacquet–Shalika–Ogg–Shahidi at s = 1, Deligne).* In half-integral weight the *signed* form of
> T1 (g(m²) ≤ 0) is as strong as the support form: a theta-class proxy (lattices of odd rank ≥ 3, any mixture of
> quadratic nebentypus) is either negative at all large primes of the square class 𝒞₁ or, on squarefree 𝒞₁, a sum of
> Gauss-exceptional Shimura components (closes WALDS (E-c), (E-d), AUTOMORPH Q2′ in half-integral weight; cosets
> CONDITIONAL on coset Siegel–Weil). Exponentially growing objects are square-blind on 1 (mod M). For several exceptional
> components, cancellation is never the obstruction (generic coefficients avoid it at every prime at once): a valid
> effective proxy exists iff (MS) holds on 𝒞₁ beyond the threshold **and** the vector of twisted central values avoids the
> span of its values at R-zeros (with no zeros: some L(½, G_j ⊗ χ_p) ≠ 0). So the automorphic route re-packages (MS) and
> adds an L-function condition; it never supplies validity. CERTIFIED: mixed-ψ validity certificates at L = 168, 240,
> 280. The L = 420 survivors (vanishing at 5569, 9601) are not prime-valid (non-zero / rank 0 at 102001, 712321, …).
> Open: a validity identity; off-𝒞₁ / p-dependent levels (q ≥ n_p, B2); integral-weight signed proxies (AUTOMORPH B1).
> Add to §6: "signed (minorant) and mixed-nebentypus half-integral-weight proxies on 𝒞₁; cancellation-control as the
> missing step for multi-eigensystem proxies (it is not)".

### 7.6 Bottom line
The last automorphic escape left by AUTOMORPH/TERNARY/WALDS was "signed or multi-eigensystem proxies". In half-integral
weight it closes in the expected way: replacing "g = 0 at odd squares" by "g ≤ 0 at odd squares" changes nothing,
because the only way to keep g(p) > 0 at large primes of the square class is for the genus term to vanish there, after
which a Rankin–Selberg sign argument kills every Shimura anchor; mixing characters or raising the weight does not help,
and exponentially large objects cannot even tell p from a square in the class 1 (mod M). The multi-eigensystem question
turns out to be mis-posed: cancellation between eigensystems can always be avoided by generic coefficients, so no
"single-p cancellation control" is ever needed — what is needed is (MS) itself (to know where the zeros are) plus a
non-degeneracy of twisted central values, and nothing in the modular world supplies the former. Numerically, the
survivor lines follow their own Euler factors and ignore R; the one striking coincidence (both L = 420 lines vanishing
at the first two in-𝔐 (★)-zeros) does not persist (102001, 712321, …). ES and (MS) remain open; the wall is again B2 —
here in the form "a reason for validity".

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
* `scripts/z60_signed_pseudosq.py L D 40000 "[a-invariants]" D′ 200 data/z60/signed/pseudosq_L_D.txt` for
  (168,168,E₈₄,−168), (420,21,E₂₁₀,−84), (420,105,E₁₀₅,−420), (280,56,E₇₀,−56), (560,280,E₅₆,−280) (§6.2; summary lines
  are console output reproduced in §6.2).
* `scripts/z60_signed_t420.py 2e15` (first run, killed after 83449: `t420_screen_run1.txt`), `… 2e15 83449,…`
  (`t420_screen.txt`, killed during an analytic-rank computation), `… 2e15 102001` (`t420_screen_102001.txt`);
  `scripts/z60_signed_zeros_rank.py <9 zeros> 3` → `zeros_rank_420.txt`.
* `scripts/z60_signed_baserate.py X 25|120 line [2]` → `baserate_chi21_8e4.txt`, `baserate_runs.txt`;
  `scripts/z60_signed_zeros_rank.py <the 360 base primes> 3` → `baserate_effort3.txt`;
  `python3 scripts/z60_signed_baserate_stats.py` → `baserate_stats.txt` (§6.3).

## 10. Review log
(pending)
