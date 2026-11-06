# Z60_SIGNED — signed and multi-eigensystem automorphic proxies (checkpoint 1)

Status: z60 lane SIGNED (brief `z52bbriefs/z60_lanes.md` §SIGNED; common rules `z52bbriefs/z58_lanes.md`,
`z52bbriefs/z53_depth.md`). Internal, not yet reviewed. **ES is OPEN; nothing here proves or disproves ES, (★), (MS),
(MS⁺) or CONV-II.** Labels: PROVED / CONDITIONAL / CERTIFIED / EVIDENCE / CONJECTURE / Assessment.
Scripts `scripts/z60_signed_*`, data `data/z60/signed/`.

Notation as in `Z59_WALDS.md` / `Z58_TERNARY.md`: R(n) = #{(u,B,C) ∈ ℕ³ : 4uBC − u − B = n}; 𝔐 ⊂ (ℤ/840)^× Mordell's
classes; 𝒞₁(2N) = {n ≥ 1 : n ∈ ℤ_q^{×2} for every prime q | 2N}. A real arithmetic function g is a
* **support proxy** (valid) if g(n) ≠ 0 ⟹ R(n) ≥ 1 for all n ≡ 1 (4);
* **signed minorant** (valid) if g(n) > 0 ⟹ R(n) ≥ 1 for all n ≡ 1 (4) (AUTOMORPH's Q2′);
* **effective on a prime set 𝒫** if g(p) ≠ 0 (support) resp. g(p) > 0 (signed) for all sufficiently large p ∈ 𝒫.
Validity at odd squares (T1: R(m²) = 0) gives **(T1⁰)** g(m²) = 0 (support) resp. **(T1⁻)** g(m²) ≤ 0 (signed).

## 0. MANDATORY FALSIFIER TABLE (checkpoint version; final version in §7)

Mechanism examined: positivity at 𝔐-primes of a fixed-level automorphic proxy that is *signed* (minorant form) or a
*sum of several eigensystems* (cancellation), in half-integral weight (ternary/odd-rank theta class, any mixture of
nebentypus characters), plus exponentially growing (weakly holomorphic / Rademacher) objects.

| screen | behaviour |
|---|---|
| **F1 odd squares** | This is the whole content of §2–§3. The signed form only gives the *inequality* g(m²) ≤ 0, which in integral weight does **not** force anything (AUTOMORPH Prop B1: 5σ₂ − (2n²+3)τ is ≤ 0 at all odd squares, = p² − 1 > 0 at all primes). **Theorem S1/S2 (PROVED rel. cited inputs):** in half-integral weight the inequality at prime squares (S1) resp. at good squarefree-index squares (S2, mixed nebentypus) is as strong as the equality: either the genus main term is *negative* on 𝒞₁ (then g(p) < 0 at every large prime of 𝒞₁, so the proxy is never positive there) or it vanishes on 𝒞₁ together with every t = 1 unary series and every Shimura component's anchor a(1), so on squarefree 𝒞₁ only Gauss-exceptional eigensystems survive (as in WALDS W1). Non-squareness is used at the t = 1 Shimura orbit (anchor) and at the genus density of m². |
| **F2 C-even (R₈)** | All negative statements (S1, S2, S4) are line-blind: they apply verbatim to R₈-minorants (R₈(m²) = 0), so nothing false is proved. The positive statement (Prop S5, reduction of effectiveness to a linear non-degeneracy) is an *equivalence* and applies to R₈ too; there it correctly requires R₈(p) ≥ 1 beyond the threshold on 𝒞₁, so any R₈-version must start above the 4 in-𝔐 R₈-zeros (largest 10 868 474 401). |
| **F3 composites** | Not used by S1/S2 (identities at squares + analytic bounds at primes). Squarefree composite zeros in 𝒞₁ enter the validity space exactly like prime zeros (S5: Z contains them). Mixed-nebentypus certificates (§5) use all known R-zero rows, composites included. |
| **F4 known zeros** | Nothing is proved positive. §5 computes, at levels with several Gauss-exceptional lines (mixed ψ), whether some *combination* vanishes at every known in-class R-zero ≤ B (a valid mixed proxy up to B) — the multi-eigensystem version of WALDS §5.3. |

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

