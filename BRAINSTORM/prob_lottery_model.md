# Brainstorm memo: a statistical-mechanics model of the ES lottery (O142(b))

Labels as in DISCOVERIES.md. ES is not solved, and nothing here proves any case of it. Everything
quantitative below is **EVIDENCE** (finite computation) or **Assessment** (heuristic model).

Verdict up front: **COLLAPSES as a proof route.** The heuristic is not a proof, and the one
proof-relevant phenomenon one could hope for, rigidity (sub-Poisson number variance), is
**absent** in the data. As a model it works well, and several by-products are EVIDENCE.

## 1. Idea

Build the best random model for `f_II(p)`, with the correct square-class and genus dependence.
Use it to predict `P(f_II(p) = 0)`, the number of sterile primes, and `min f_II/log³p` up to 10⁸.
Then look for a "rigidity" mechanism: negative correlation or repulsion that would make a zero
count impossible, in the way eigenvalue repulsion forbids large gaps in random-matrix ensembles.

Only rigidity could matter for a proof. In a determinantal process the number variance grows
only like the log of the mean (Dyson–Mehta), so the zero-count event is suppressed
super-exponentially, and in some integrable models it is forbidden outright.

## 2. Literature anchor

* Elsholtz–Tao 2013, Thm 1.7 (from memory, as quoted in the campaign ledger B2):
  `Σ_{p≤N} f_II(p) ≍ N log²N`, so the mean of `f_II(p)` is ≍ `log³p`.
  The Type I analogue, without ET's `log log N`, is (D)32b.
* Small values of Euler products and of `L(1,χ_d)`: Granville–Soundararajan, GAFA 2003. The
  distribution function has a double-exponential tail (from memory, unverified constants).
* Number variance of sine-kernel (CUE/GUE) processes, `(1/π²)log N`: Dyson–Mehta 1963; see
  Mehta, *Random Matrices* (from memory).
* Divisor functions of shifted primes: the Titchmarsh divisor problem (Linnik; Bombieri–
  Friedlander–Iwaniec). Erdős–Kac-type log-normal behaviour of `τ`.
* Campaign: the cubic Haar exponent (ET Remark 1.2, audit 10b), the mass spread over ≍ 𝓛³ blocks
  (O132 H-A), the Ω-results `W(p) ≥ (log p)^k` i.o. (OMEGA2/3), and X5: `N_T(p) = 0` i.o. with
  `log T ≍ (log p)^{1/4}` (redteam Prop 2.3).

## 3. The model (Assessment), and what the data say (EVIDENCE)

Data: `scripts/bs_prob_fII.c` gives exact `f_II(p)` for all primes ≤ 10⁸. It reproduces R128b:
`f_II(5) = 2`, min 36 at `p = 2031121`, no zeros. It also gives the split by the slice
parameter e, where `p + e = 4abd` and `N_e = (p+e)/4`; this is the e-slice of LONGSHOT_PIGEONHOLE
Lemma 1.1. Logs: `logs/bs_prob_{model,euler,bulk,shifts}.txt`.

**3.1 Two-level structure.** Write `f_II(p) = Σ_e X_e(p)`, where `X_e(p)` counts factorisations
`N_e = a·b·d` with `b ≡ −a (mod e)`. Its mean is ≈ `τ₃(N_e)/φ(e)`, so the mass is harmonic in e.
* *Small e (heavy-tailed part).* For primes in [2²⁰, 3·10⁷], e ≤ 16 (only four values of e)
  carries **40%** of f. This part has CV 1.56 and correlation 0.98 with f. Its fluctuations are
  those of the divisor counts of four shifted integers `(p+e)/4`. The 200 hardest primes in
  [2²⁴, 2²⁵] have mean `Σ_{e≤16} τ((p+e)/4)` = 39, against 65 for random primes, and
  `corr(log f/L³, log Στ) = 0.61`. Of the 8 dyadic record minima checked, 6 have
  `τ((p+3)/4) ≤ 4`, and two have `(p+3)/4` prime: 2031121 and 20180449. **The hardest primes are near-prime-tuple shifts.**
* *Large e (bulk).* e > 256 carries ≈ 36% (it grows with p). Its CV is 0.27 and its correlation
  with f is only 0.34.

**3.2 Quenched disorder = local data.** Let `λ(p)` be the mean of the bulk over primes in the
same class mod 120120 and the same dyadic range. The bulk is then a compound Poisson variable,
`bulk ≈ κ·Poisson(λ/κ)` with **κ = 3.06** in the counter's weight-2 units (ordered (b,a)), that
is ≈ 1.5 per unordered solution. Calibration on 1.29M primes:

| model lower-tail level | 1e-2 | 1e-3 | 1e-4 | 1e-5 |
|---|---|---|---|---|
| observed fraction | 7.8e-3 | 6.6e-4 | 5.1e-5 | 4.5e-6 |

min bulk/L³: observed **0.00196**; model, 20 simulations: median **0.00209**, range [0.00101, 0.00303].
The model is calibrated to within a factor of 2 down to the 10⁻⁵ quantile. Part of the residual
lightness is plausibly the noise in estimating λ from ~40 primes per cell.

**3.3 The quenched factor S(p) and square classes.** Fitting a marginal Euler product
`S_y(p) = Π_{ℓ≤y} σ_ℓ(p mod ℓ)` (y up to 400) explains only R² = 0.45 of `log f/L³`; the rest is
the small-e part of 3.1. The square-class depression **saturates**. The mean of f/L³ on
`p ≡ 1 (mod Q)`, relative to all primes, is

| Q | 24 | 120 | 840 | 9240 | 120120 | 2042040 |
|---|---|---|---|---|---|---|
| ratio | 0.70 | 0.65 | 0.58 | 0.53 | 0.505 | 0.49 (12 primes) |

The increments at ℓ = 11, 13, 17 are 0.91, 0.95, 0.98.

*Assessment (why it saturates).* A square-class constraint at ℓ ≤ y kills or depletes only
the witness moduli whose genus character is decided at small primes. In log-scale those carry a
fraction ≈ `log y / log p` of the cubic mass, which → 0 for y = p^{o(1)}. This is consistent with
X5: there, all moduli up to `T = exp(c(log p)^{1/4})` die, a mass fraction
`≈ (log T/log p)³ → 0`. **So in the model the quenched mean is λ(p) ≍ log³p uniformly**,
provided χ_p is not biased on primes of size `p^{Ω(1)}`. That is a Vinogradov/GRH-type
statement about χ_p, and it is false exactly at squares.

**3.4 Predictions (Assessment, calibrated by 3.2).** `P(f_II(p) = 0) ≤ P(bulk = 0) ≈ exp(−λ(p)/κ)`.
* Over [2²⁰, 3·10⁷]: the expected number of bulk zeros is **0.019**, even ignoring the
  small-e part. Observed: 0 zeros of f.
* At p ≈ 10⁸: min-cell `λ ≥ 0.0175·L³ ≈ 109`, so `P ≲ e^{−36}`. The expected number of sterile
  primes in (10⁸, ∞) is `≲ 10⁻⁸`. The sum `Σ_p exp(−c log³p)` converges extremely fast.
* Predicted `min f/L³`: about flat, since by 3.3 the minimum is set by the quenched floor times a
  near-prime-shift factor. Observed: dyadic minima of f/L³ are 0.0117–0.0170 over 2¹⁷–2²⁶, while
  the number of primes grows 170-fold. The mean drifts 0.076 → 0.065 and the CV drifts
  0.62 → 0.66 (Erdős–Kac-slow).

**3.5 Rigidity test: negative.** Per unordered solution the bulk has number variance/mean
≈ 1.5 > 1 (κ by dyadic range: 1.9 → 3.2 in weight-2 units; the low values at 2²⁰ are biased down
by cells with ~3 primes). There is no sign of a sub-Poisson, determinantal or "repulsive"
regime. The bulk events are mildly **positively** clustered: several c share one (a,d), i.e.
one integer `p + 4a²d`. Any eigenvalue-repulsion analogue is empirically false for this
lottery (EVIDENCE, scope ≤ 3·10⁷).

**3.6 No conservation law between the types; a common driver (EVIDENCE).** One could hope that Type I
and Type II are complementary (a "conservation law": when one is small the other is large).
The data say the opposite. Exact `f_I` comes from R123's counter `scripts/review_r123_count.c`,
over 1.29M primes in [2
data]

## 4. Barrier screen

* **B1/B5 (odd squares).** The model passes T1 only through its genus factor: at n = m², χ_n is
  principal off m, every witness needs `(n/f) = −1`, and so λ(m²) = 0 exactly. The step that is
  false at squares is "χ_p equidistributes on primes up to `p^θ`" (3.3). That step is
  heuristic/GRH-level and says nothing about the realised count.
* **B2.** The model *is* the lottery. The quenched/annealed split is exactly "genus/congruence
  data" plus "divisor events at Planck scale". The heavy-tailed small-e part makes it explicit
  that fixed slices fail with only polylog-small probability: `X_3(p) = 0` whenever `(p+3)/4`
  is a prime ≡ 1 (mod 3).
* **B3.** The main term is λ ≍ L³ = p^{o(1)}, consistent with the scale constraint. The model
  offers no bounded-multiplicity certificate.
* **B6/T7.** Every number in §3 is an average over p, within residue cells. Calibration of the
  annealed part is by definition across primes. At a single p the model predicts but does not
  certify.
* **T2.** Per-e pieces with e ≤ 16 have main term ≫ 1, but their zero probability is ≍ polylog⁻¹
  (prime shifts), so group control is still required.

## 5. Viability

**COLLAPSES** as a proof route: to B6/T7 at the step "annealed part at a single p", and to H-A
for its replacement. The hoped-for escape, rigidity, is refuted empirically (§3.5).

By-products (EVIDENCE; small, possibly useful for the barrier note or for future heuristics):
1. f_II(p) splits into a heavy-tailed part (four shifted divisor counts, 40% of the mass at 10⁷,
   ≈ all of the variance) and a compound-Poisson bulk, κ ≈ 1.5 per unordered solution.
2. The hardest primes are those whose shifts `(p+e)/4`, e ≤ 16, have few divisors, on top of
   square classes mod 840.
3. The square-class depression of the mean saturates near 0.5 at y ≤ 17 (Assessment: → 1 as
   p → ∞ at fixed y).
4. The calibrated model predicts ≈ 0.02 bulk-sterile primes in [2²⁰, 3·10⁷] and `≲ 10⁻⁸` beyond
   10⁸.

None of these is a theorem. A Hardy–Littlewood-type asymptotic `f_II(p) ~ L³·𝔖(p)` is
false in the data, because of the small-e heavy tail. The natural replacement CONJECTURE,
`f_II(p) ≥ c·L³` for all large p, is just a strengthening of ES.
