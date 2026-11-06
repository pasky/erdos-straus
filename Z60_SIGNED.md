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
* **(Duk)** Duke 1988 / Iwaniec 1987: for h ∈ U^⊥ ⊂ S_{3/2}(Γ₀(4N), ψ), |h(t)| ≪_{h,ε} t^{1/2 − 1/28 + ε} for squarefree t
  (verification from source: §8, pending).
* **(RS)** For weight-2 newforms φ, φ′ of trivial character (real coefficients):
  Σ_{ℓ≤X} a_ℓ(φ)ℓ^{−1/2} log ℓ = o(X) and Σ_{ℓ≤X} a_ℓ(φ)a_ℓ(φ′)ℓ^{−1} log ℓ = δ_{φφ′}X + o(X)
  (prime number theorems for L(s, φ) and L(s, φ × φ′); reference check §8, pending).

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
(i) *c_φ are real.* g real ⟹ g(ℓ²) real ⟹ Σ_φ Im(c_φ)a_ℓ(φ) = Im(Σ_φ c_φ)ε(ℓ) =: β ε(ℓ); by (RS),
Σ_{ℓ≤X}|Σ_φ Im(c_φ)a_ℓ(φ)|²ℓ^{−1}log ℓ = (Σ_φ Im(c_φ)²)X + o(X), while the right side gives ≤ β²Σ_{ℓ≤X}ℓ^{−1}log ℓ = O(log X);
so Im c_φ = 0.
(ii) Put G(ℓ) := Σ_φ c_φ a_ℓ(φ)/√ℓ (real, |G(ℓ)| ≤ K := 2Σ_φ|c_φ|). The inequality gives G(ℓ) ≤ |Σ_φ c_φ|/√ℓ, so
G⁺(ℓ) := max(G(ℓ), 0) ≤ |Σc_φ|ℓ^{−1/2}. With θ(X) := Σ_{ℓ≤X, ℓ∉P} log ℓ:
Σ_{ℓ≤X}|G(ℓ)| log ℓ = Σ (2G⁺(ℓ) − G(ℓ)) log ℓ ≤ 2|Σc_φ|Σ_{ℓ≤X}ℓ^{−1/2}log ℓ − Σ_{ℓ≤X} G(ℓ) log ℓ = O(√X) + o(X)
by (RS, first part). Hence Σ_{ℓ≤X} G(ℓ)² log ℓ ≤ K·Σ|G| log ℓ = o(X). By (RS, second part) the left side is
(Σ_φ c_φ²)X + o(X). So Σ c_φ² = 0 and all c_φ = 0 (c_φ real).
*Step 5.* With c_φ = 0, WALDS W1 Steps 4–5 apply verbatim (they use only g_φ(1) = 0, Waldspurger Cor. 2 and Thm F (i),
(ii)): for squarefree t ∈ 𝒞₁, t > 1, g_φ(t)²L(½, φ ⊗ ψχ_{−4}) = 0, the genus and unary parts vanish at t, and the
conclusion follows. ∎

**Remarks.** (1) Only *prime* squares are used, and only their sign. As a by-product, WALDS W1 holds under the
prime-square hypothesis g(ℓ²) = 0 (ℓ large) alone — the route WALDS Remark (a) left "not verified, not used" (Step 4
with ≤ replaced by =; Step 2 is then not needed).
(2) Case (a) is a genuine alternative, not vacuous: g = −θ_{gen L} + (small cusp form) satisfies (T1⁻) and is negative
at all large primes of 𝒞₁. A signed minorant can be *valid* in case (a) — it is then simply useless on 𝒞₁.
(3) The analytic inputs enter only in case (a) (Sie, Duk) and in Step 4 (RS). Case (b) is unconditional relative to
(RS), Deligne and Waldspurger.

## 3. (planned) Theorem S2 — mixed nebentypus (support and signed)
## 4. (planned) Cosets, higher weight, exponential growth (square-blind asymptotics)
## 5. (planned) Multi-eigensystem: genericity reduction (Prop S5) and mixed-ψ certificates
## 6. (planned) Residual statement and its relation to (MS)
## 7. Verdict / screens / FRONTIER text (final)
## 8. Literature verification log (pending)
