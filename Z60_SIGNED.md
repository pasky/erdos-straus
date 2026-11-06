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
(ψ is even), so ε_ψ ≠ 1, and ψ ↦ ε_ψ is injective. Call m *good* if m is squarefree and all its prime factors lie
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

