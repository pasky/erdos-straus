# CAP_INTERPOLATION — the exponent cap as a sieve-dimension knob, uniformly in e (task O234, spark relay Z4)

Status: in progress (O234). **ES is not solved here, nor any infinite case of ES.** Labels as in DISCOVERIES.md.
Builds on CAP_GROWING (O229: Prop 1.3 overflow cube, Thm 1.4), EXPONENT_CAP ((J)34: Def 1.1, Prop 1.2, Prop 3.1,
Dictionary 3.3), PHASE_DIAGRAM ((J)43: Thm 5.1), FROBENIUS_FIRING (Thm 4.2, Thm 4.4), the 3/4 note
(paper/es-threequarter-note.tex, §"heuristic mass-driven ceiling"). Scripts `scripts/z10_*`, outputs `data/z10/`.

Notation. λ := log log N, log₃ := log log log. For a prime ℓ ≡ 3 (mod 4), K := (ℓ+1)/4. A *cube triple* is
τ = (c₀, d₀, R) with c₀, d₀ odd, squarefree, coprime, c₀d₀ | K, rad R | c₀; V(τ) := c₀²d₀R²; the triple has
*cap e* if v_s(R) ≤ e for all s. Its class is −4V(τ) mod ℓ (CAP_GROWING Prop 1.3).
κ := e + 2 (the number of local options per prime of c₀d₀: s | d₀, or s | c₀ with v_s(R) ∈ {0, …, e}).

## 0. Iteration log

(Z4-1) Goal 1, first pass. O229's c_e came from Lemma 1.1 of CAP_GROWING (Bombieri–Vinogradov with divisor-bounded
weights h(q) ≤ κ^{ω(q)}). That step is NOT uniform: Cauchy–Schwarz against BV needs Σ h(q)²/q ≤ (log x)^{A}, i.e.
κ² ≪ A. Barrier hypothesis identified: "BV with fixed A". Modification: the moduli 4c₀d₀ only need to be
≤ X^{1/(10κ)}, and then log x/log q ≥ 5κ → ∞: Gallagher's prime number theorem gives a *relative* error
exp(−cκ) per modulus, with no weight problem. Result: c_e ≍ 1/(e log e), uniformly (§1–2, Thm 2.1).
(Z4-2) Letting e = e(N) grow: the bound (log N)^{κ/(κ+1)}/(κ log κ) is maximised at κ ≍ log log N, where it
equals log N/(log₂N·log₃N). A Rankin computation shows this is the CEILING of the prime-modulus large sieve with
the overflow-cube classes at ANY cap, including e = ∞ (Thm 3.1). So the knob saturates at e ≍ log log N, and the
sieve side never reaches "all n ≥ n₀" — not even for ES^{(y)} = e = ∞, which is a pointwise THEOREM.
(Z4-3) Goal 1 from the pointwise side: … (§4).
(Z4-0, after R230) Calibration fixed by R230 D1: "e = 0 is Vaughan's 2/3" is a statement about the *prime-modulus*
large sieve only; ES's record is (log N)^{3/4} (composite multipliers kℓ, 3/4 note) and KARY3 caps CRT methods for
ES at 3/4. Everything in §§1–3 is prime-modulus large sieve; §5 treats composite moduli.

## 1. A uniform class supply (no Bombieri–Vinogradov weights)

**Input (G) (Gallagher's prime number theorem; Gallagher, Invent. Math. 11 (1970) 329–339, Thm 7; cited, not
re-derived).** There are absolute c₁, c₂ > 0, C₁ such that for x ≥ 3 and 1 ≤ T ≤ x^{c₂}:
Σ_{q≤T} Σ*_{χ mod q} |ψ(x, χ)| ≤ C₁ x (exp(−c₁ log x/log T) + exp(−c₁ √log x)), where Σ* runs over primitive
non-principal characters other than the (at most one) exceptional real character χ₁ of conductor q₁ ≤ T.
Consequence (standard): for every q ≤ T with q₁ ∤ q and (a, q) = 1,
`  |ψ(x; q, a) − x/φ(q)| ≤ (x/φ(q))·η(x, T),   η := C₁(exp(−c₁ log x/log T) + exp(−c₁√log x)) + O(log²(qx)/x^{1/2}).`
(ψ(x;q,a) = φ(q)^{−1}Σ_χ χ̄(a)ψ(x,χ); χ₁ does not occur mod q when q₁ ∤ q; each χ ≠ χ₀ is induced by a primitive
χ* of conductor d | q, d ≤ T, and |ψ(x,χ) − ψ(x,χ*)| ≤ log²(qx).)

**Lemma 1.1 (Rankin lower bound for κ^{ω}; PROVED, elementary + Mertens).** There are absolute C₂, C₃ such that for
every integer κ ≥ 1, every set 𝒫' of primes containing all odd primes except at most one, and Z with
log Z ≥ 4(C₂κ + 1):
`  F_Z := Σ_{m ≤ Z, μ²(m)=1, p|m ⇒ p∈𝒫'} κ^{ω(m)}/m  ≥  ½ exp{κ (log log Z − log κ − log log(κ+2) − C₃)}.`
*Proof.* For σ ∈ (0, ½] put F(σ) := ∏_{p∈𝒫'}(1 + κp^{−1−σ}) = Σ_m κ^{ω(m)} m^{−1−σ}. Then
F_Z ≥ Σ_{m≤Z} κ^{ω}m^{−1−σ} ≥ F(σ) − Z^{−σ/2}F(σ/2). Per prime, (1+aX)/(1+aY) ≤ 1 + a(X − Y) for X ≥ Y, so
log(F(σ/2)/F(σ)) ≤ κ Σ_p p^{−1−σ/2}(1 − p^{−σ/2}) ≤ κ[Σ_{p ≤ e^{2/σ}} (σ/2)(log p)/p + Σ_{p > e^{2/σ}} p^{−1−σ/2}]
≤ C₂κ (Mertens Σ_{p≤y} log p/p = log y + O(1); the tail is ≤ ∫_{2/σ}^∞ e^{−σt/2}dt/t + O(1) = O(1)). Choose
σ := 2(C₂κ + 1)/log Z ≤ ½; then Z^{−σ/2}F(σ/2) ≤ e^{−1}F(σ) and F_Z ≥ ½F(σ). Lower bound: for p > κ,
log(1 + κp^{−1−σ}) ≥ κp^{−1−σ} − κ²p^{−2}/2, and Σ_{p>κ} p^{−2} ≤ 1/κ; Σ_p p^{−1−σ} = log(1/σ) + O(1)
(log ζ(1+σ) = log(1/σ) + O(σ)); removing p ≤ κ, p = 2 and the one excluded prime costs log log(κ+2) + O(1). Hence
log F(σ) ≥ κ(log(1/σ) − log log(κ+2) − C) and 1/σ = log Z/(2(C₂κ+1)) ≥ log Z/(2(C₂+1)κ). ∎

**Proposition 1.2 (uniform cube supply; PROVED relative to (G)).** There are absolute κ₀, C₄ such that for every
e ≥ κ₀ − 2 (κ = e + 2), and X ≥ X₀ with u := log X ≥ 40(C₂+1)κ²:
`  S_e(X) := Σ_{X^{1/2}<ℓ≤X, ℓ≡3 (4)} ω_e(ℓ)/ℓ ≥ exp{κ(log u − 2 log κ − log log(κ+2) − C₄)},`
where ω_e(ℓ) counts the distinct classes −4V(τ) mod ℓ of cap-e cube triples with V(τ) ≤ X^{1/5}. Moreover
ω_e(ℓ) ≤ X^{1/5} ≤ ℓ^{2/5}.
*Proof.* Put Y := X^{1/5}, Z := Y^{1/(2e+2)} (log Z = u/(10(e+1))), T := 4Z. For squarefree odd m ≤ Z, every
assignment "s | d₀" or "s | c₀ with v_s(R) = ρ_s ∈ [0, e]" (s | m) is a cap-e triple with c₀d₀ = m and
V ≤ m^{2+2e} ≤ Y: κ^{ω(m)} triples, whose classes are pairwise distinct (CAP_GROWING Thm 1.4: τ ↦ V(τ) is
injective) and are valid at every prime ℓ ≡ −1 (mod 4m) (ℓ > 4Y; CAP_GROWING Prop 1.3 — the hypothesis
v_s(c₀) = v_s(K) for s | R is NOT needed for cap e, see Remark 1.3). If the exceptional modulus q₁ (w.r.t. T) exists,
its odd part m₁ is > 1 for T ≥ T₀ (χ₋₄, χ_{±8} have no real zero near 1), and we drop one prime s₁ | m₁ from 𝒫'.
For x ∈ [X^{1/2}, X]: log x/log T ≥ (u/2)/(u/(10(e+1)) + 2) ≥ 4κ, so η ≤ 1/6 for κ ≥ κ₀; dyadic summation of
θ(2y; q, −1) − θ(y; q, −1) ≥ (1 − 3η)y/φ(q) gives Σ_{ℓ∈(X^{1/2},X], ℓ≡−1 (q)} 1/ℓ ≥ 1/(5φ(q)) for q = 4m. So
S_e(X) ≥ Σ_m κ^{ω(m)}/(10m) = F_Z/10 with 𝒫' = odd primes ∖ {s₁}. Lemma 1.1 (log Z ≥ 4(C₂κ+1) by the hypothesis on u)
and log log Z = log u − log(10(e+1)) give the claim. ω_e(ℓ) ≤ #{V ≤ Y} ≤ Y. ∎

**Remark 1.3 (the exactness condition is unnecessary; PROVED).** In CAP_GROWING Prop 1.3 drop "v_s(c₀) = v_s(K) for
s | R". With σ := v_s(K) ≥ 1 = v_s(c₀), ρ := v_s(R) ≥ 1: v_s(E) = 0 and x = EK − c₀²d₀R², z = p·x·j/(c₀R²),
v_s(j) = σ − 1. If σ < 2 + 2ρ: v_s(x) = σ, v_s(z) = 2σ − 2 − 2ρ ∈ [−2ρ, 0) ∪ [0, ∞) — even, ≥ −2ρ. If σ ≥ 2 + 2ρ:
v_s(x) ≥ 2 + 2ρ and v_s(z) ≥ σ − 2 ≥ 0 (if σ > 2+2ρ, v_s(x) = 2+2ρ exactly; if σ = 2+2ρ, v_s(x) ≥ σ). In all cases
v_s(z) is even when negative, ≥ −2e, and s | y = p c₀ d₀ j. So every cap-e triple with c₀d₀ | K gives an
ES^{(y,e)}(p) solution (den z = ∏ s^{2 max(0, 1+ρ_s−σ_s)}). Checked numerically in §6 (z10_cube_check).
