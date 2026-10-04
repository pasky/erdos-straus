# Hostile review — EXCEPTIONAL_NONCRT.md (task O11, checkpoint 1)

Subject: branch `side-agent/noncrt-inputs-2` @ becb4ca — `EXCEPTIONAL_NONCRT.md`,
`reviews/agent-reports/AGENT_REPORT_O11.md`, `scripts/noncrt_checks.py`,
`data/noncrt/checks_m8.txt`. Checked against EXCEPTIONAL_THETA.md (ET-file:
Prop 2.4, Thm 2.5, Lemma 2.9, Cor 3.4, §6.1) and Elsholtz–Tao 1107.1010.
Reviewer branch: `side-agent/review-noncrt`.

Verdict scale: SOUND / SOUND-AFTER-REPAIRS / DEFECTIVE. Defects numbered N1, N2, …

## Items

### 1. Prop 2.1 (Boolean sieve limit with high-level Walsh tail) — **SOUND**

Checked line by line.
* `|y^S(0)| = Π_S p_i` ⇒ `f_lo(0) ≥ 1 − r₀`; `E|y_i| = 2p_i(1−p_i)` +
  independence ⇒ `E|f_hi| ≤ r₁`; `E f_hi = 0` since every S in f_hi is
  nonempty (s(∅) = 0 ≤ λ). Correct.
* f_lo depends only on `x_V` (every S with s(S) ≤ λ lies in V). `f ≥ 0` ⇒
  `f_lo ≥ −|f_hi|` ⇒ (conditioning on x_V) `f_lo ≥ −h`. Correct.
* Thinning: with w fixed, `y_i = u_i w_i − p_i` is affine in u_i, so the
  multilinear expansion of `f_{lo,w}` has monomials `u^{S'}`, `S' ⊆ S ∩ Z`,
  multidegree in Λ. `h_w` depends only on `u_Z` (u∘w vanishes off Z).
* Symmetrisation: `Q(k) = E[f_{lo,w} | K = k]` because the iid Bern(q_g) law of
  u is uniform on each count-fibre; hence `Q ≥ −H` on the support. The
  Λ'-reduction only changes Q off the support (0 is in the support). Correct.
* Interpolation: `c_j L Q = c_j L (Q+H) − c_j L H ≤ |c_j L|(Q+H) + |c_j L|H`
  uses only `Q + H ≥ 0` at grid (= support) points; extending the grid sum to
  the full support uses `Q + 2H ≥ H ≥ 0`. Gives
  `1 − r₀ ≤ e^{Φ(w)}(E_u f_{lo,w} + 2E_u h_w)`. Correct.
* Averaging over w: `(1−r₀)E_w e^{−Φ(w)} ≥ (1−r₀)e^{−E_wΦ(w)}` needs
  `1 − r₀ ≥ 0`, which the proof handles (r₀ ≥ 1 trivial). ET Step 5 then
  applies verbatim (bands need `q_g ≤ 1/4`, guaranteed by `p_i ≤ 1/4` for all i).

No defect. (Prop 2.1 is a genuine, clean extension of ET Prop 2.4.)

### 2. Lemma 2.2 (Walsh coefficient at S ≤ Fourier ℓ¹ mass on Θ_S) and (2.2)–(2.3) — **SOUND-AFTER-REPAIRS** (repair is wording only)

Fourier/Walsh correspondence checked:
* `d_S(c)Π_S p(1−p) = E[ν_c y^S] = E[ν y^S | n≡c (Q₀)] = Q₀ E_n[ν g]`: orthogonality
  (`E(y^S)² = Π p(1−p)`), tower property, `P(n≡c) = 1/Q₀`. Correct.
* g = (function of n mod Q₀) × Π_{ℓ∈S}(function of n mod ℓ), moduli pairwise
  coprime, so ĝ is the convolution = product of coefficients at summed
  frequencies. `1̂[·≡c (Q₀)](a/Q₀) = e(−ac/Q₀)/Q₀`; `ŷ_ℓ(0) = p − p = 0`;
  `|ŷ_ℓ(h/ℓ)| = |1̂_F(h)| ≤ |F|/ℓ`. So supp ĝ ⊆ Θ_S, `|ĝ| ≤ Q₀⁻¹Π_S p_ℓ`.
  Parseval with g real. Direction of the inequality correct.
* Disjointness of Θ_S: the CRT decomposition of the dual of ℤ/Q_tot; a/Q₀ has
  trivial ℓ-component since ℓ ∤ Q₀; S is recovered as the set of slice primes
  where θ has a component of order exactly ℓ. Frequencies with ℓ²-components or
  components at non-slice primes lie in no Θ_S and correctly never enter.
  0 ∉ Θ_S (S ≠ ∅). (2.2) correct.
* (2.3): `|d_S| ≤ A_S Π 1/(1−p)`, so `r₀ ≤ Σ A_S Π p/(1−p) ≤ Σ A_S Π(4/3)p`,
  `r₁ ≤ Σ A_S Π 2p`; with `s_ℓ = log(1/(2p_ℓ⁺))` both are `≤ Σ_{s(S)>λ} A_S e^{−s(S)}`.
  Correct.

Numerics: the author's Part 1 reproduces bit-for-bit (max lhs−rhs = −1.747e−17).
That statistic is weak: the maximum is attained at degenerate (c,S) with
`A_S = 0 = lhs`, so it only shows "no violation", not how tight. My extended
check `scripts/review_noncrt_lemma22.py` (Q₀ = 9 prime power, moduli with 25 and
49, extra non-slice prime 2, dense ν with up to 200 classes) gives
max lhs/rhs = 0.910 over 900 non-degenerate (c,S), max lhs−rhs = −2.2e−4. Lemma
holds, including the prime-power / non-slice frequency bookkeeping.

**N1 (minor, scope wording).** §2.2 says "Restrict 𝒫 to the slice primes dividing
some d_i; this keeps ν ≥ 1 on the new avoider set by the CRT modification
argument … So 𝒫 is finite", suggesting 𝒫 may be infinite beforehand. For
infinite 𝒫 the modification argument is false: enumerate the integers
`n_1, n_2, …` and give each a fresh prime `ℓ_k` with `F_{ℓ_k} = {n_k mod ℓ_k}`
(p = 1/ℓ ≤ 1/4); then 𝒜 = ∅ and ν ≡ 0 is a "majorant". The ET-file defines 𝒫 as
finite, and with 𝒫 finite the CRT step is correct. Repair: say "𝒫 is finite (ET §1);
restricting to the primes dividing some d_i is the ET Step-0 reduction". This also
bounds the reach of the "no bound on slice-prime size" claim (item 4): it holds for
every *finite* family, with primes of any size, which is what ET §6.1 item 7 is about.

### 3. Thm 2.3, Cor 2.4, Cor 2.5 (the cap) — **SOUND** (two cosmetic notes)

* Thm 2.3: `Eν ≥ (|R|/Q₀) avg_c Eν_c` (ν ≥ 0); `ν_c(0) ≥ 1` because the event
  `{c}×{x=0}` in ℤ/Q_tot is inside 𝒜 (finite 𝒫, see N1) and has positive
  probability; ν_c ≥ 0. Weights `s_ℓ = log(1/(2p_ℓ⁺))` are c-independent, so the
  band structure is common to all fibres and the ET Jensen step (exp convex,
  `log(16μ+16)` concave, profile term affine in p_ℓ(c)) goes through. The ε ≥ 1/3
  branch: RHS ≤ (2/3)·1 − 2/3 ≤ 0. Correct. `s_ℓ ≥ log 2 = s_*` from `p ≤ 1/4`.
* Cor 2.4: only `R_1 ≤ (rounding bound) ≤ N e^{−s} ≤ N` is used, then
  `ε ≤ e^{−λ}N ≤ e^{−Φ̄}/4`, `(1−ε) ≥ 3/4`, `2ε ≤ e^{−Φ̄}/2` ⇒ `Eν ≥ (|R|/Q₀)e^{−Φ̄}/4`.
  Arithmetic and direction correct. Note the corollary is really "any bound
  `N·Eν + B` with `B ≥ R_1(ν)`"; stating it that way would make the scope (item 4)
  transparent.
* Cor 2.5: `|F_ℓ(c)| ≤ ℓ^{C+o(1)}` uniformly in c (union over q₀ ≤ ℓ^C of
  ≤ M^{o(1)} classes), so `p_ℓ⁺ ≤ 1/4` and `s_ℓ ≥ ((1−C)/2)log ℓ` for ℓ ≥ ℓ₀(C);
  profile `Σ p̄_ℓ ℓ^{−α'} ≪ α'^{−3}` via ET Lemmas 3.1/3.2/3.7 summed over *all* ℓ;
  truncated mass over `s_ℓ ≤ λ` ⇒ `ℓ ≤ e^{2λ/(1−C)}` ⇒ `μ̄ ≪_C λ³`;
  `G = O(log λ)`; `λ_N = 2log(4N)` satisfies the fixed-point condition for
  N ≥ N₀(C). Correct. The removal of ET §6.1 item 7 is valid for finite
  prime-slice families meeting the Cor 3.4 hypotheses, with slice primes of any size.

Cosmetic: (i) Thm 2.3 uses μ̄ without redefining it; it must be
`Σ_{s_ℓ≤λ} p̄_ℓ` (not ET's `Σ_{ℓ≤e^λ}`), as Cor 2.5's proof does. (ii) G and s_*
should be restated (`s_* = log 2`, `G = ⌊log₂(λ/log 2)⌋+1`).

### 4. Scope of "per-frequency weight w(θ) ≥ 1" and the claimed examples — **SOUND-AFTER-REPAIRS** (overclaim in summary/verdict)

What Cor 2.4 actually covers: any final bound `N·Eν + B` with `B ≥ R_1(ν) =
Σ_{θ≠0}|ν̂(θ)|`. Checked members:
* `Σ|a_i|`: each class has `Σ_{θ≠0}|1̂| = 1 − 1/d`, so `R_1 ≤ Σ|a_i|`. ✔
* `w(θ) = min(N, 1/(2‖θ‖))`: valid since `|S_N(θ)| = |sin πNθ|/|sin πθ| ≤ 1/(2‖θ‖)`,
  and `w ≥ 1` for θ ≠ 0. ✔
* Any pointwise bound `B(θ) ≥ |ν̂(θ)|` (Weil/Gauss/Ramanujan bound for the complete
  sum `Σ_{classes of one modulus} a_i e(−b_iθ)/d_i`) inserted into either. ✔

**N2 (moderate, overclaim: "the sawtooth bound").** "Sawtooth bound" is covered
only in the specific Fourier-majorised form `Σ|ν̂(θ)|min(N,1/(2‖θ‖))` (§1 defines
it so). The standard sawtooth route — exact per-class identity
`#{n≤N: n≡b (d)} − N/d = ψ(−b/d) − ψ((N−b)/d)` followed by Erdős–Turán/Vaaler
or by per-class floor/ceiling bounds (`a_i⌈N/d_i⌉` for a_i > 0, `a_i⌊N/d_i⌋` for
a_i < 0) — is *not* of this form: Vaaler's main term carries the factor
`|e(Nθ)−1| = 2|sin πNθ|` (weight < 1 near ‖Nθ‖ ≈ 0), and the ceiling/floor
rounding `⌈N/d⌉ − N/d` can be ≈ 0 (e.g. d | N, or d slightly above N), below the
class's R_1 share `1 − 1/d`. These use where the classes sit relative to N, i.e.
they belong to (a′)/(a″) and remain open (ET §6.1 item 2 is only partly closed).
Repair: in §0, §2.5 first paragraph and the AGENT_REPORT, write "the sawtooth bound
`|S_N(θ)| ≤ min(N,1/(2‖θ‖))`" and add the ψ/Erdős–Turán/Vaaler and per-class
ceiling bounds to the list of what is *not* covered.

**N3 (moderate, overclaim: "Kloosterman cancellation").** Covered is only
cancellation in a *complete* sum over classes sharing one frequency (a complete
Gauss/Kloosterman/Ramanujan sum bounding `|ν̂(θ)|`). The way Kloosterman sums
actually enter sieve remainder terms (Poisson summation in n with a smooth weight,
then cancellation in the sum over moduli d of `e(h\bar b_d/d)`-type terms —
Deshouillers–Iwaniec / BFI dispersion) is cancellation among `ν̂(θ)S_N(θ)` at
*different* θ = h/d, plus smooth weights with w < 1. That is (a′)+(a″), which the
file correctly lists as open in §2.4–2.5 — but §0 ("this contains … all
Gauss/Kloosterman/divisor-exponential-sum cancellation within a frequency"), §2.3
"What this closes" ("Candidate (a) in its natural form … Gauss/Kloosterman/divisor
exponential sums … is capped") and the §6 row (a) present the closed part as the
natural form. Repair: say explicitly that sums over moduli (dispersion,
Kloosterman-fraction bilinear forms) are inter-frequency and *not* capped; label the
closed part "complete-sum (single-frequency) cancellation".
