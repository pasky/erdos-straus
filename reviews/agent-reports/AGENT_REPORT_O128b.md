# AGENT_REPORT_O128b — round 2: the algebraic angle (ternary lattice, spinor, Kudla/GKZ) + 10⁸ numerics

Branch `side-agent/typeii-spectral`. New sections §§7–10 of `POINTWISE_TYPEII_SPECTRAL.md`. R128 repairs D1–D8 are
applied and marked "(R128 repair Dk)". The review branch was merged. Scripts: `t2s_ternary.py` (+out: Gram, Pell,
divisor identity for p < 160, squares s ≤ 21), `t2s_eis.py` (+out), `t2s_numerics_1e8.out.txt`.

## Answers to the round-2 questions
**(i) Lattice data (PROVED, §7).**
* The lattice is `L` = binary forms with `q = B² − 4AC`, signature (2,1).
* A Type II solution is a pair `Q = [f,4ad,de]` (q = −4dp), `S_c = [0,2c,1]` (q = 4c²) with `b(Q,S_c) = 4`, i.e. an
  embedding of `4·T₀`, `T₀ = [−dp, 1, c²]`, `disc T₀ = 4c²dp+1`.
* Extra data: the class `k ≡ 1 (2c)` of S, and the level `B ≡ 0 (4d)`, `d | C`, gcd.
* Bonus (Prop 7.2): Type II solutions are unusually small units `T + 2c√D'` with `D' = d²(a−b)² + dp` and
  `T = 2cd(a+b) − 1`. This is the Type II analogue of TYPEI4's Pell certificates.

**(ii) Invariance / reduction theory (PROVED, §8.2).**
* `Stab_{SL₂(ℤ)}(S_c) = ±I`. Once S is normalised there is no group left to reduce by.
* The ES conditions other than positivity are not invariants of the Gram matrix; they are a class condition on S
  plus level data.
* Positivity is the choice between the classes k = ±1.

**(iii) What existence reduces to (PROVED, §8.1/8.3).**
* Exactly the divisor condition: some `4c²dp+1` has a positive divisor ≡ −1 (mod 4cd). The formulation is neither
  weaker nor different.
* Local, genus and spinor data hold for **every** n, including odd squares, where f_II = 0. In fact
  `Q₀ = [−1,0,−dn]` is a global integral solution of everything except the sign.
* So "local + spinor ⇒ global" is false for this problem.
* The obstruction is the ray class group mod `4cd·∞` of a split torus (sign at ∞ vs residue −1). Strong
  approximation is unavailable, which is why the three-squares mechanism does not transfer.

**Generating series (§9).**
* Prop 9.1 (PROVED): `F(n) = Σ_{c,d} φ(4cd)^{-1} Σ_η η(−1)σ_η(4c²dn+1)`. This is a sum over ≍ n log n levels of
  Eisenstein coefficients: weight-1 for odd η, weight-0 for even η.
* Prop 9.2 (PROVED): genus pairing η ↔ ηχ_{−4d}. At odd squares every even coefficient cancels exactly against
  its odd twin, which is ET Prop 1.6 in Eisenstein form.
* Fixing Q instead gives CM theta series of ℚ(√−dp), which do have cusp parts. But Type II sums over the whole
  genus, and Siegel–Weil leaves only Eisenstein (Assessment).
* Kudla/GKZ:
  * There is no fixed form: p enters only through T₁₁ = −4dp, and the levels are unbounded.
  * There is no cusp part to bound.
  * The bounded-level truncations are empty for many p: the d = 1 family alone fails for ~150–200 primes per
    block near 10⁸.
* **Verdict: no real automorphic pointwise route from this structure. The problem is multiplicative:
  divisors of `4c²dp+1` in classes mod 4cd.**
* EVIDENCE: the genus main term (η = 1, χ_{−4d}) only partly explains the hard primes (act/MT 0.27–0.79 vs
  0.70–1.72 for random primes). The deficit is spread over many small-conductor characters.

**(b) Numerics to 10⁸ (EVIDENCE, §10).**
* f_II(p) ≥ 1 for all primes ≤ 10⁸. Dyadic minima are 62 / 74 / 88 / 94 for the blocks 2²³–2²⁶.
* min f_II/log³p is about 0.015 (overall 0.0117 at p = 2031121).
* The hard primes are again the square classes mod 840.
* min R falls slowly, 0.27 → 0.24. The 0.1% quantile is stable at about 0.37.

## Caveats
* §9.3/9.4 (Siegel–Weil and Kudla readings) are Assessments. The PROVED content is Props 9.1–9.2, which are
  elementary.
* The weight-0 identification for even η is up to normalisation.
* The ternary checks run only to p < 160 (Python divisor enumeration). The identities are elementary.

Checkpoint reached. Waiting for the parent.
