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

### 5. §2.4 dichotomy and §2.5 (weights < 1) — **SOUND** (as labelled)

* Dichotomy: if `ε_λ ≤ e^{−Φ̄}/4` then (2.4) gives `Eν ≥ (|R|/Q₀)(3/4 − 1/2)e^{−Φ̄}`.
  Correct, and honestly labelled "a restatement of (2.4), nothing more". Squares:
  `≍ √N` avoiders give only a θ = 1 obstruction. Correct.
* §2.5 hit-pattern reduction (Q₀ = 1): `ν̂(Σ_S h_ℓ/ℓ) = d_S Π_S 1̂_{F_ℓ}(h_ℓ)` — other
  Walsh terms vanish on Θ_S since `ŷ_ℓ(0) = 0`. With (2.6) and weights
  `log(3/(8p⁺))`: `Π2p = Π(8/3)p·Π(3/4) ≤ Π(8/3)p·Π(1−p) ≤ e^{o(λ)}M_SΠ(8/3)p`. Correct.
  (H_eq) is properly marked CONJECTURE. Small point: "e^{−o(λ)}" must be uniform in
  S with s(S) > λ (a fixed function of λ), otherwise the tail sum is not controlled;
  say so in (2.6).
* "Weights < 1 open" is the honest residue; note that by N2 the per-class
  floor/ceiling and ψ-Vaaler bounds also belong here.

### 6. Lemma 3.1 (prime majorants ↔ reduced classes) — **SOUND**

Dirichlet in the reduced classes mod `L·Π_{removed ℓ}` with a unit residue
outside `F_ℓ(c)` at each removed ℓ (hypothesis `|F_ℓ(c)∖{0}| < ℓ−1`); 𝒫 finite
(N1 applies here too). One-directional statement is correct as given.

### 7. Thm 3.2 (Dirichlet-measure LP limit; E*-Lemma 2.9) — **SOUND** (one conservative slip)

* The four ingredients of ET Thm 2.5 hold under E* = uniform on (ℤ/L)^×: CRT product
  of uniform unit groups; x_ℓ independent Bern(p*_ℓ(c)) given c; conditional
  expectation of each term depends on x_{T_i}; `{c}×{x=0}` has positive E*-mass
  (unit outside F) and lies in 𝒜. ✔
* E*-Lemma 2.9: `1/φ(ms) ≤ 1/φ(s) ≤ Π_{ℓ|s}(ℓ−1)^{−1} = Π ℓ^{−1}·Π ℓ/(ℓ−1)`, level of
  s in `(λ−Λ₀, λ]`, Mertens ⇒ `≪ log λ`. ✔ (dropped negative terms: same estimate
  with level > λ; not written but immediate.)
* Selector computation for R*: c uniform on (ℤ/Q₀)^× projects to uniform on
  (ℤ/q₀)^×. ✔

**N4 (minor, conservative).** "`log(φ(Q₀)/|R*|) = log(P/φ(P))` for the selector".
For a selector `R = {(c,P)=1}` with `P | Q₀`, `R* = R ∩ (ℤ/Q₀)^× = (ℤ/Q₀)^×`, so the
R-term under E* is **0**, not log(P/φ(P)). The stated cap is still a valid upper
bound (it is larger), so nothing breaks; fix the equality to "= 0 (≤ log(P/φ(P)))".

### 8. Thm 3.3 (primality by a sieve costs O((log log N)²)) — **SOUND-AFTER-REPAIRS**

Mechanism correct: `𝒜 ∩ 𝒫_z` is the avoider set of the augmented system
(`F'_ℓ = F_ℓ ∪ {0}`, new slice primes 5 ≤ ℓ ≤ z with `F_ℓ = {0}`, ℓ = 2,3 into the
selector), so ν is a majorant of it; then compare the two instances of (2.4).
Profile increment `C₄Σ_{ℓ≤z}ℓ^{−1−α} ≤ C₄(log(1/α)+O(1))`; mass increment
`≤ log log z + O(1)`; `log(16(μ̄+Δ)+16) − log(16μ̄+16) ≤ log(1+Δ)`. ✔ The author
correctly notes this compares *bounds*, not optimal savings.

**N5 (minor, bookkeeping).** The first displayed increment
`C₄Σℓ^{−1−α} + (G/2)log(1+log log z+O(1))` omits (i) the change of G (s_* drops from
log ℓ₀ to log 5, so G grows by O(1) bands, each costing `75 + log(2+λ/s_*)` and a
`½log(16μ_g+16)` term), (ii) the change of `log(2+λ/s_*)` inside the existing G
terms, and (iii) the R-term increase `log 3` from putting 2, 3 into the selector
(zero if 6 | P already). All are `O(log λ)` and are absorbed by the second line
`O(log²λ)`, so the conclusion stands, but the first line is not an upper bound as
written. Repair: drop the first line or add "+ O(log λ)".

Also note: the hypothesis "ν has level ≤ λ in the augmented system" is a real
restriction (a prime-detecting sieve of dimension one at level D = z² ≤ e^λ meets
it; but it must be imposed, not derived). It is stated; fine.

### 9. Remark 3.4 (Assessment) — **SOUND as Assessment**

VK: best known unconditional relative error is `exp{−c(log N)^{3/5}(log log N)^{−1/5}}`,
weaker than `exp{−(log N)^{3/4}}`; BV/BDH save powers of log only. Correct.
Wording: "save at most" should be "the best known saving is" (it is a statement
about known results, not an upper bound). The level argument (moduli > N cost
|a_i| absent knowledge of which classes contain primes ≤ N) is an Assessment and
is what bridges Thm 3.2 (level-λ) to arbitrary prime-majorant arguments; it should
be cited wherever "BV/BDH/EH/GRH cannot beat 3/4" is stated as PROVED (see N6).

### 10. Prop 4.1 (moment bounds are CRT majorants) — **SOUND-AFTER-REPAIRS** (prime clause)

Integer clause: `f(n) ∈ ℤ_{≥0}`, `P ≥ 0` there, `P(0) ≥ 1` ⇒ `P∘f ≥ 0` on ℤ and ≥ 1
on {f = 0}; products of class indicators are class indicators of intersections.
A CRT evaluation of the moments with per-tuple error O(1) has rounding
≥ Σ|a_i| (with multiplicity) ≥ R_1(P∘f), so Cor 2.4/2.5 apply with no level
hypothesis. ✔

**N6 (moderate, missing step).** "With prime moments `Σ_{p≤N}P(f(p))` it is covered by
Theorem 3.2." Thm 3.2 is a level-λ statement, and there is no Fourier/Thm-2.3
analogue for E*. A degree-k moment over witness moduli ≤ N^A has terms of level up
to `kA log N`, so Thm 3.2 alone caps the saving only at `C(kA log N)^{3/4}`.
Combining with Prop 4.2 (`O(k log log N)`) does **not** close the gap: the minimum
of the two caps, maximised over k, is ≈ `(log N)^3/(log log N)^3`, far above
`(log N)^{3/4}`. What closes it is the E*-version of Lemma 2.9 (item 7) applied to
the terms of level > A log N, which needs (i) those terms to be charged ≥ |a_i|
each (Remark 3.4, an *Assessment*: for lcm > N one has π(N;d,b) ∈ {0,1} and no known
input beats the trivial cost), (ii) `Σ_{high}|a_i| < π(N)`, (iii) slice primes
≤ N^{O(1)}. Repair: state the prime clause as "covered by Thm 3.2 + E*-Lemma 2.9
under (i)–(iii)", and downgrade the §0/§6 claim "(c) … capped by (a)/(b)" for prime
moments of unbounded order to "PROVED for level ≤ A log N; beyond that via the
Remark 3.4 Assessment". The same caveat applies to the §0 phrase "BV/BDH/EH/GRH
cannot beat 3/4" (true at level N^{O(1)}, which is where those inputs live — fine,
but say "majorants evaluated at level N^{O(1)}").

### 11. Prop 4.2 (degree-k CRT mean saves O(k log log N)) — **SOUND-AFTER-REPAIRS** (constant)

Degree bookkeeping checked: given c, `f = Σ_ℓ φ_ℓ(n mod ℓ)` with φ_ℓ ≥ 0 supported on
F_ℓ(c) (multiplicities allowed); `f^j` expands into products of ≤ j ≤ k factors,
each a function of ≤ k slice coordinates; conditional expectation given (c,x)
keeps each term a function of ≤ k of the x_ℓ (independence). With all s_ℓ = 1:
λ = k, s_* = 1, one nonempty band (G = 1 after discarding empty bands, ET Step 0),
`|Λ'| ≤ k+1`, `Σ p_i e^{−αs_i} = e^{−α}μ`. `ν_c(0) = P(0) ≥ 1` since x = 0 ⇒ f = 0.
The displayed bound is exactly ET (2.3) with these data + Jensen over c. ✔

**N7 (minor, constant).** With `x = C₄μ̄/(19k)` and `α = max(1, log x)`, the value
`19αk + C₄e^{−α}μ̄` equals `19k(1+log x)` if x > e, but `19k(1 + x/e)` if x ≤ e, and
`x/e ≥ log⁺x` (strictly for x < e). So the claimed `19k(1+log⁺x)` understates by up
to `19k/e` when x ≤ 1. Repair: `19k(2 + log⁺(C₄μ̄/(19k)))`. Consequence
`O(k log log N)` unaffected.

Consequence paragraph: `μ̄ ≪ (log N)³` for witness moduli ≤ N^{O(1)} (Cor 3.4 profile);
k = 2 ⇒ saving O(log log N) ⇒ θ = 0. ✔ The scope is CRT means (stated).

Elsholtz–Tao Remark 1.3 is quoted correctly ("higher moments … out of reach of our
methods, as the level of the relevant divisor sums becomes too great"). Calling
this "the obstruction of Cor 2.5 in their language" overreads it: ET's obstruction
is level of distribution of error terms (BV range), not the CRT-mean cap. Suggest
"compatible with" instead.

### 12. Numerics (§5, `scripts/noncrt_checks.py`) — **SOUND** (labels need touch-up)

Rerun (`ulimit -v 8000000`, `uv run --with scipy python scripts/noncrt_checks.py 8`):
output **identical** to `data/noncrt/checks_m8.txt`; wall time 3 s (doc says ~1 min).
The toy LP formulation is right: (C) `Σ|e_T|Π_T f_ℓ` is the class-coefficient sum of
the monomial expansion (x_ℓ = Σ_{b∈F} 1[n≡b]); (F) `Σ_{S≠∅}|d_S|Π a_ℓ` is exactly
R_1(ν) for Q₀ = 1 hit-pattern ν (item 5 identity). Labelled EVIDENCE, toy only. ✔

**N8 (minor, labels).** (i) §0 table says Lemma 2.2 has an "exact numerical check";
it is floating point (§5 says so) and its max statistic is attained at degenerate
cases (item 2) — report the max ratio instead. (ii) "per-frequency rounding acts
like the coefficient budget × ≈ 4–8": from the table, F(2) ≈ C(4), F(8) ≈ C(16–32),
F(32) ≈ C(128), F(128) ≈ C(1024): the factor grows from ≈ 2 to ≈ 8. Say "≈ 2–8,
growing with B". (iii) runtime "~1 min" → seconds.

## Summary

| item | verdict |
|---|---|
| 1 Prop 2.1 | SOUND |
| 2 Lemma 2.2, (2.2)–(2.3) | SOUND-AFTER-REPAIRS (N1, wording) |
| 3 Thm 2.3, Cor 2.4, Cor 2.5 | SOUND |
| 4 scope "w ≥ 1" examples | SOUND-AFTER-REPAIRS (N2, N3 overclaims) |
| 5 §2.4 dichotomy, §2.5 | SOUND (CONDITIONAL part correctly labelled) |
| 6 Lemma 3.1 | SOUND |
| 7 Thm 3.2 | SOUND (N4 conservative slip) |
| 8 Thm 3.3 | SOUND-AFTER-REPAIRS (N5) |
| 9 Remark 3.4 | SOUND as Assessment |
| 10 Prop 4.1 | SOUND-AFTER-REPAIRS (N6: prime-moment clause) |
| 11 Prop 4.2 | SOUND-AFTER-REPAIRS (N7 constant) |
| 12 numerics | SOUND (N8 labels) |

No item is DEFECTIVE. The mathematical core — Prop 2.1 + Lemma 2.2 ⇒ Thm 2.3 — is
correct and is a real strengthening of the ET-file: the cap needs only
`R_1(ν) = Σ_{θ≠0}|ν̂(θ)| < N`, no level hypothesis, and no bound on slice-prime size
(finite families). Every inequality direction checked.

### Defects

* **N1** (minor) §2.2: restriction of 𝒫 is valid only for finite 𝒫 (counterexample
  with 𝒜 = ∅ for infinite 𝒫); say 𝒫 finite as in ET §1.
* **N2** (moderate) "sawtooth bound" covered only as `min(N,1/(2‖θ‖))`; ψ-based
  Erdős–Turán/Vaaler and per-class floor/ceiling roundings are not of the w ≥ 1 form
  and stay open; ET §6.1 item 2 only partly closed.
* **N3** (moderate) "Kloosterman cancellation": only complete single-frequency sums
  are covered; Kloosterman/dispersion cancellation over moduli is inter-frequency
  (and uses smooth weights) — open. Fix §0, §2.3 "What this closes", §6 row (a),
  AGENT_REPORT, and the suggested ledger text (D)15.
* **N4** (minor, conservative) Thm 3.2: R-term under E* for a selector is 0, not
  log(P/φ(P)).
* **N5** (minor) Thm 3.3 first display omits G/s_* changes and the log 3 selector
  term; all O(log λ), conclusion stands.
* **N6** (moderate) Prop 4.1 prime clause / §6 row (c): prime moments of unbounded
  order are capped only via E*-Lemma 2.9 under the Remark 3.4 Assessment
  (high-level terms charged |a_i|, Σ_high|a_i| < π(N), slice primes ≤ N^{O(1)});
  Thm 3.2 + Prop 4.2 alone leave a gap up to `(log N)^3/(log log N)^3`.
* **N7** (minor) Prop 4.2 constant: `19k(2+log⁺(…))`, not `19k(1+log⁺(…))`.
* **N8** (minor) numerics labels: "exact" check, factor "4–8" (really 2–8), runtime.

Ledger suggestion (D)15 is acceptable after N3 and N6 are reflected: replace
"per-frequency signed rounding" by "per-frequency (complete-sum) signed rounding",
and qualify prime moment methods by "at level N^{O(1)} (beyond: Assessment)".

Replay of this review's extra check:
`PYTHONPATH=scripts uv run --with scipy python scripts/review_noncrt_lemma22.py` (~10 s).

---

# Round 2 (branch head 6ed4f30)

Files re-imported from `side-agent/noncrt-inputs-2` @ 6ed4f30 (repairs commit
51cd78d/6ed4f30 + follow-up §8, `scripts/noncrt_interval.py`, `data/noncrt/interval_*`).

## R2.0 Repairs N1–N8 — all **FIXED**

| defect | where fixed | status |
|---|---|---|
| N1 finite 𝒫 | §2.2 now says 𝒫 finite (ET §1), with the 𝒜 = ∅ counterexample for infinite 𝒫; §0/§6 "finite prime-slice families" | fixed |
| N2 sawtooth scope | §0 row, §1, §2.3 "What this closes", §2.5 list, §6 row (a), AGENT_REPORT: sawtooth only as `min(N,1/(2‖θ‖))`; Vaaler/ψ and floor/ceiling listed as not covered; ET §6.1 item 2 "only partly closed" | fixed |
| N3 Kloosterman scope | same places: "complete" sums only; dispersion/DI over moduli = inter-frequency, w < 1, not covered; ledger text (D)15 now "complete-sum, w ≥ 1" | fixed |
| N4 R*-term | §3: R* = (ℤ/Q₀)^×, term 0 (≤ log(P/φ(P))) | fixed |
| N5 Thm 3.3 increment | display now `C₄Σℓ^{−1−α} + O(log²λ)` with the O-term itemised (mass, G, s_*, log 3) | fixed |
| N6 prime moments | Prop 4.1 states (i)–(iii) and the Assessment dependence, records the `(log N)³/(log log N)³` gap; §0, §6 rows and AGENT_REPORT relabelled "prime moments of unbounded order: Assessment" | fixed |
| N7 constant | `19k(2+log⁺(…))` | fixed |
| N8 numerics labels | "floating-point", max ratio reported (rerun: 0.9228, output identical to `checks_m8.txt`), "2–8 growing with B", runtime "seconds" | fixed (one leftover: AGENT_REPORT l. 66 still says "about 1 min") |

Unnumbered round-1 notes not acted on (cosmetic, optional): Thm 2.3 still does
not restate `μ̄ = Σ_{s_ℓ≤λ}p̄_ℓ`, G, s_*; Remark 3.4 still says "save at most" for
known VK/SW error terms; the uniformity of `e^{−o(λ)}` in (2.6).

## R2.1 Thm 8.1 (quantitative dichotomy) — **SOUND**

If (H) fails, (2.4) gives `Eν ≥ (|R|/(4Q₀))e^{−Φ̄}`; subtracting `Σν ≤ Ne^{−s}` gives (D).
If moreover `s ≥ Φ̄ + log(8Q₀/|R|)`, then `e^{−s} ≤ ½Eν`. ✔ For Cor 2.5 families
`Φ̄ ≤ Cλ^{3/4} + O(log²λ)`, so the condition holds for `λ ≤ c s^{4/3}` (≫ log N when
θ > 3/4), provided also `log(P/φ(P)) ≤ s/2` (true; worth saying). Correctly labelled a
restatement of Thm 2.3. (H) is the *weighted* mass `Σ_{s(S)>λ}A_S e^{−s(S)}`, as stated.

## R2.2 Lemma 8.2, Cor 8.3 (classes above M₀ ≍ N² are empty on [1,N]) — **SOUND-AFTER-REPAIRS** (one justification)

* Lemma 8.2 is exactly (60.9) of notes Thm 60.1 (`M = 4gu−1`, `g ≤ B`, `u ≤ g+v ≤ 2B`),
  valid for every datum of every n ≥ 1. I re-derived it and checked it: my
  normal-form enumerator agrees with brute force over (M,D) for all n < 25, and for
  n ≤ 300 max M = 22799 ≤ M₀ = 80000 (`scripts/review_noncrt_lemma82.py`).
* Cor 8.3: ν' ≥ 0, ν' = G(0) ≥ 1 on 𝒜_{𝒲₀}, and ν = ν' on [1,N]. ✔ (Requires G ≥ 0 on
  all of {0,1}^𝒲, not only on realised patterns; true for P∘f with P ≥ 0 on ℤ_{≥0}
  and for Selberg squares — say "G ≥ 0 on {0,1}^𝒲".)

**N9 (minor, wrong justification, conclusion true).** "every Lemma 3.2 class, which is
a subclass for n ≥ 1" — an ET Lemma 3.2 class `n ≡ −(4D+a) (mod 4a·g(D))` is *not*
a subclass of one ℛ(M) class: along the class, `M = (n+4D)/a = 4g(D)j − 1` varies
with n. The conclusion (such classes of modulus > M₀ miss [1,N]) is still true, by
a different route: for n ≤ N in the class, the datum has normal form with
`D = gd`, `d | g`, so `D | g²` and `g(D) | g`; with `a ≤ 2B`, `g ≤ B` this gives
`4a·g(D) ≤ 8B² = M₀`. Numerically, for n ≤ 300 the largest such modulus is
40400 ≤ 80000. Repair: replace "which is a subclass" with this argument.

The "Meaning" paragraph is fine: after Cor 8.3, level above λ needs at least
`λ/(2 log N + O(1))` classes of modulus ≤ M₀ in one product.

## R2.3 §8.3 interval-vs-CRT LPs (EVIDENCE) — **SOUND-AFTER-REPAIRS** (qualitative finding stands; two statements wrong)

Reran all four runs of `scripts/noncrt_interval.py`: outputs **identical** to
`data/noncrt/interval_*.txt` (6–23 s, ≤ 220 MB). Every row with Y ≥ N and
2 ≤ k ≤ 10 has interval saving < CRT saving, as claimed. Table entries match the files.
The LP is the right object for "best degree-k polynomial in the hit count,
evaluated exactly on the chosen integers": `Σ_{n≤N}P(H(n)) = N·E_emp P(H)`.
Diagnostics are in `scripts/review_noncrt_interval.py`.

**N10 (moderate, numerics; conclusion survives).** The cap HCAP = 80 does two things.
It relaxes positivity, and it also **truncates both laws**: `bincount(...)[:HCAP+1]`
and the length-81 CRT pmf recursion silently drop all mass at H > 80. At N = 30000
(primes), Y = 3·10⁷, max H on the primes is **129**, and 0.31% of them have H > 80;
that mass is simply deleted. The claim that the relaxation "helps both sides equally"
is false. With positivity imposed on 0..200 and untruncated laws (k = 10):

| run | int (HC=80 → 200) | CRT (HC=80 → 200) |
|---|---|---|
| N=3000 all, Y=N | 3.62 → 3.60 | 6.30 → 5.34 |
| N=3000 all, Y=M₀ | 3.38 → 3.17 | 12.68 → 11.09 |
| N=3000 primes, Y=M₀ | 4.33 → 3.85 | 12.68 → 11.09 |
| N=30000 primes, Y=N | 5.18 → 4.64 | 8.04 → 7.90 |
| N=30000 primes, Y=3·10⁷ | 4.88 → 4.21 | 13.41 → 11.75 |

So the CRT side moves by up to 1.6 and the interval side by up to 0.7. The gap
narrows at Y = N (N = 3000: 2.7 → 1.7) but keeps its sign everywhere. Repair: set
HCAP ≥ max H (or assert that no mass is dropped), drop "helps both sides equally",
and regenerate the table.

**N11 (moderate, wrong inference).** "So for this natural family `Δ_N(ν) < 0`: the
interval carries *more* than its CRT share … the opposite of branch (D)." What the
LPs compare is `min_P E_int P(H)` against `min_P E_CRT P(H)`. Those are the optima of
two different problems; neither is `Δ_N(ν)` for a fixed ν. Cross-evaluating
(HC = 200):
* for the **CRT-optimal** P, Δ_N < 0 — e.g. N=3000 all, Y=M₀, k=10: E_int ↔ saving
  2.16 vs E_CRT ↔ 11.09;
* for the **interval-optimal** P, Δ_N > 0 in most rows: the interval carries *less*
  than the CRT mean. At N=3000 all, Y=M₀, k=10, E_int ↔ 3.17 vs E_CRT ↔ 2.87. At k=2,
  E_CRT[P_int] > 1 (saving −0.56) while E_int ↔ 1.37, a factor e^{1.9}. At N=30000
  primes, Y=3·10⁷, k=10: 4.21 vs 3.91.

So branch-(D)-type behaviour does occur, in a mild form: the interval count is below
the CRT mean of the *same* majorant. It does not help, because the interval optimum
still saves far less than the CRT optimum. Repair: say "the exact interval optimum
saves less than the CRT optimum (so there is no gain from inter-frequency
cancellation in this family)". Drop the claims "Δ_N < 0" and "opposite of
branch (D)" in §8.3, §8.6 and the AGENT_REPORT.

Additional caveats (state them):
* For "all n" and "non-squares" the interval saving is capped by the void:
  `E_int P(H) ≥ π_int(0)` because `P(0) ≥ 1`. That is 3.9 (all n, void 0.02, mostly
  squares) and 6.2 (non-squares). The "all n" rows mostly measure the squares floor,
  not inter-frequency effects. The prime rows (void ≈ 0) are the informative ones.
* The CRT model for the prime rows is the integer measure `Bern(|F_ℓ|/ℓ)`, not the
  Dirichlet measure E* of Thm 3.2. The difference is a factor `ℓ/(ℓ−1)` per ℓ and
  does not matter qualitatively.
* Single sub-family: prime moduli ℓ ≡ 3 (4) with F = ℛ(ℓ), and polynomials in
  the *count* H only (not general hit-pattern majorants).
* "often by a factor e^5–e^9" holds for Y ≫ N. At Y = N the gap is e^{1.6–2.9}
  (HC = 80) or e^{1.7–3.3} (HC = 200).
