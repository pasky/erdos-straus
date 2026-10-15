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
