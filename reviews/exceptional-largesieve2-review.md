# Hostile review R27 of EXCEPTIONAL_LARGESIEVE2.md (task O27)

Reviewer: side-agent/review-largesieve2. Reviewed: branch
`side-agent/ls-escapes` (checkpoint 1). From-scratch scripts:
`scripts/review_ls2_*.py`. Status: **round 1 complete**.

## Verdict per claim

| claim | verdict |
|---|---|
| Lemma 1.1 (comparison measure) | SOUND (conditional on K2 Thm 5.1, as labelled) |
| Lemma 1.2 (unit version) | SOUND (conditional on PL Thm 3.1) |
| Lemma 2.2, Lemma 2.3 | SOUND |
| Thm 2.4, Cor 2.5 (hybrid / twisted / multiplicative cap) | SOUND (minor: M' must contain the twists' periods, m1) |
| Thm 3.1 (prime large sieve) | SOUND (conditional on PL Thm 3.1); scope = type (i)/(iii) fibres only, as stated |
| Lemma 4.1, Thm 4.2 | SOUND (minor m2: add 1 to 𝒟) |
| **Thm 4.3** (Gallagher, 26 log log N, unconditional) | SOUND, modulo K2 Lemmas 2.3, 4.1–4.3 and the W-uniformity `C(W) ≤ C(log W)^c` (checked against K2 Lemma 3.1's proof); wording m3 |
| Prop 5.1, Prop 5.2 | SOUND; (H_LS∞) correctly labelled CONJECTURE |
| Prop 6.1 | SOUND but trivial; its *reading* is overstated in the bottom line and the ledger suggestion (m4) |
| §6.3 | Assessment, fine; one inaccurate aside (m5) |

No FATAL or MAJOR defects found. Every key inequality was re-derived by
hand, and Lemma 1.1, Lemma 2.2, Thm 2.4 type (i) (additive **and**
multiplicative/character rows, random twists `|ψ| ∈ [1,3]` of random
period), Lemma 4.1, the Thm 4.2 chain, Prop 6.1 and Thm 4.3's elementary
constants were checked by independent code (`data/review_ls2/`).

## Claim-by-claim notes

### Lemma 1.1

Re-derived. Primal: `min E_U ν` over the subspace `V_𝒟` (free
coordinates) subject to `ν(x) ≥ 1_𝒜(x)` for all `x ∈ ℤ/M'` (the `ν ≥ 0`
constraints on 𝒜 are implied, off 𝒜 they are the same family). Finite LP,
feasible (`ν ≡ 1`), bounded below by 0, so strong duality: there is
`μ ≥ 0` on `ℤ/M'` with `Σ_x μ(x)ν(x) = E_U ν` for all `ν ∈ V_𝒟` (equality
because ν is free in a subspace) and `μ(𝒜) = m*`. Signs are right. Since
`1 ∈ V_𝒟`, μ is itself a probability (not stated, harmless). π = μ|_𝒜/m* is
supported on `𝒜 mod M'` by construction; for `f ≥ 0` the dropped mass off 𝒜
only helps. No compactness issue (finite dimension). K2 Thm 5.1's
majorant class (`ν = Σ a_i 1[n≡b_i (d_i)] ≥ 0` on ℤ, `≥ 1` on 𝒜, each
`d_i` of W-rough level `≤ λ`, `λ ≥ λ₀`) contains every primal-feasible ν
(the d ∈ 𝒟 divide M', so "on ℤ/M'" = "on ℤ"), hence `m* ≥ e^{−S(λ)}`.
Remark (iii) / (1.2): checked; the lifted `F(n) = f((n−c)/Q₀)1[n≡c (Q₀)]`
needs `Q₀d | M'`, which holds as `Q₀d ∈ 𝒟`. Converse direction (Remark
(i)) correct.

Numerical check from scratch (`scripts/review_ls2_lp.py`, seed 1, output
`data/review_ls2/lp_seed1.txt`): toy M' = 2310, random forced-class
avoiders (densities 0.33–0.73), 𝒟 = divisors with ≤ k of {5,7,11}
(k = 0,1,2). HiGHS duals: stationarity ≤ 4·10⁻¹², μ is a probability,
μ(𝒜) = m*, π has no mass off 𝒜, and the second LP
`max{E_πf : f ∈ V_𝒟, f ≥ 0, E_Uf = 1}` equals `1/m*` in every case
(e.g. 2.4367 = 1/m* at k = 2).

### Theorem 4.3 (unconditional O(log log N) cap for Gallagher) — first pass

Chain re-derived; I find it SOUND (details and constant checks below).
* The law σ: base uniform on K2's `R_W^□` (K2 Lemma 2.3 is stated for
  every `W ≥ 3`; (R1) avoids all W-smooth classes of all four types,
  selectors included — proof is internal, uses K2 Lemmas 2.1–2.2 only),
  then plain sequential singletons with caps `δ_ℓ = ℓ^{−1/2}`. EK Lemma
  2.1(2) gives per-prime inflation `(1−δ_ℓ)^{−1} = γ'(ℓ)`, exactly K2's
  Γ, so K2's chain rule `σ(n≡b (m)) ≤ Γ(m)/m` holds and K2 Lemmas 4.1–4.3
  apply verbatim (their proofs use only the chain rule; checked).
* W-uniformity (the critical point, since W = (log 3Q)^8 grows): K2 Lemma
  4.3 states `C(W) ≤ C(log W)^c`. Checked against K2 Lemma 3.1's proof:
  primes `p ≤ W` contribute `≤ C(H,a)(log W)^{eH2^a}` — a polylog in W
  with an enormous but absolute exponent; Lemma 4.2's short-block
  pointwise bounds use `Γ(q) ≤ 8·3^{ω(q)}` (W-free); Shiu / K2 Lemma 3.5
  constants are W-free. So `𝔏 ≤ C(log W)^{c'}W^{−1/4}` and
  `𝔏·log Q ≤ C(8 log log 3Q)^{c'}(log 3Q)^{−2}log Q = O(1)`. OK.
* Leak: EK Lemma 2.1(1) + `E[p1{p>δ}] ≤ Ep²/δ` gives
  `Σ ℓ^{1/2}Ep_ℓ²`. OK.
* Conditioning: `π(b) ≤ σ(b)/(1−𝔏)` ⇒ `1+χ²(π) ≤ (1+χ²(σ))(1−𝔏)^{−2}`
  and `(1−x)^{−2} ≤ 1+4x` on `[0,1/4]` (checked numerically).
* Marginals: rough ℓ: convexity of χ² in the mixture over histories,
  `χ²(Unif(Ω∖F)) = p/(1−p)`; contraction under `ℤ/ℓ^E → ℤ/ℓ^v`; OK.
  W-smooth p: reduction of unit squares mod `p^e` onto unit squares mod
  `p^v` is a surjective group homomorphism ⇒ uniform; χ² = (p+1)/(p−1)
  (odd p), 1, 3, 7 for `2, 4, 2^v (v≥3)`. Checked from scratch.
* Sum: `Σ_{p≤W} log p/(p−1)·(2+12𝔏) = 2 log W + O(1)` (𝔏 log W = o(1)),
  so `≤ 3 log W + C = 24 log log 3Q + C`. OK (the "2" in front comes from
  χ² ≤ 2 for odd p; p = 2 bounded).
* Consequence via LS Thm 6.2's proof: `N/B ≤ 1 + NX/(ψ(Q)−log N)`; need
  `D* > log N`, `D_u ≤ log Q + c₀` ⇒ `Q ≥ Ne^{−c₀−X}`; for `Q ≤ N²`,
  `(log 3Q)^{24} ≤ 3^{24}(log N)^{24}` so `Q ≥ N(log N)^{−25}` for large N;
  `X ≤ 25 log log N`, saving `≤ 25 log log N + log log log N + C ≤ 26 log
  log N + C`. `Q > N²`: `4NX/Q ≤ 1`. OK.
* Constants checked from scratch (`scripts/review_ls2_small.py`,
  `data/review_ls2/small.txt`): unit-square χ² = 2, 1.5, 4/3, 1.2 for
  p = 3, 5, 7, 11 (all v), and 1, 3, 7, 7, … for 2^v; reduction
  `p^{v_max} → p^v` uniform on unit squares in every case;
  `(1−x)^{−2} ≤ 1+4x` on `[0,1/4]`.
* Labels: "no external input" is K2's convention (no ElT Prop 1.4); the
  chain does use published standard results (Shiu's theorem inside K2
  Lemma 4.2, Mertens). See m3.

### Lemma 1.2, Theorem 3.1

PL Thm 3.1 is stated for prime majorants (PL Def 1.1); PL Lemma 1.2
(Dirichlet) shows LP (1.1) on units mod L is equivalent, and feasibility
on units mod any multiple M' of L is the same condition. So Lemma 1.2's
LP on `(ℤ/M')^×` is covered; the dual argument is identical. Thm 3.1:
`E*F ≤ (M'/φ(M'))E_U F` for `F ≥ 0`; type (iii) `π*(c) ≤ e^S/φ(Q₀) ≤
e^S(M'/φ(M'))/Q₀`; Mertens `M'/φ(M') ≤ e^γ A log N(1+o(1)) ≤ 2A log N`;
the step `N/(4A log N) ≥ π(N)/(5A)` needs `π(N) ≤ 1.25N/log N`, true for
all N > 113 (checked to 2·10⁵; holds asymptotically). SOUND. Scope:
type-(ii) prime-majorant fibres only sketched, as the author says.

### Theorem 2.4 / Corollary 2.5

Re-derived (Cauchy–Schwarz with ψ, (1.2), Lemma 2.2 averaged over all
translates — valid also when N > period). The admissibility notion
(`L ≤ R̃(π)/E_π|ψ|²` for all π on 𝒜) is exactly what (2.1) with
`a_n = ψ1_A` yields, and includes methods that bound `R̃` from below and
`E|ψ|²` from above separately. `|ψ| ≥ 1` is only a normalisation. Lemma
2.3 checked: level counts distinct primes, so the prefix argument gives
`d' > N_c` even with large exponents. Numerics: Lemma 2.2 and the type-(i)
inequality `R̃(π)/E_π|ψ|² ≤ Δ/(N m*)` hold with ratios ≤ 0.31 (additive)
and ≤ 0.47 (character rows mod q | 2310, all characters, weight
`(q/φ(q))^{1/2}`), Δ computed exactly as the max over **all** 2310
translates of the Gram norm. Consistency: Vaughan's `N exp(−c(log N)^{2/3})`
(large sieve) is below the cap.

### Lemma 4.1, Theorem 4.2

Re-derived; Lemma 4.1 checked exactly on random kernels, and the identity
`D(π)−D_u = Σ_{θ≠0} w̃_θ|π̂(θ)|²` plus the bound `≤ max_{θ≠0}w̃_θ/m*` on
the LP measure (ratios well below 1).

### Propositions 5.1, 5.2

Re-derived. In 5.2, (a) needs `f` of level `≤ 2λ'` because
`θ−θ'` has denominator `lcm(den θ, den θ')`; (H_LS∞) with
`λ' = (log N)/η` gives `|π̂|² ≤ e^{2S(λ')}N^{−2}`, more than enough.
SOUND.

### Proposition 6.1

Brute force (`review_ls2_small.py`): all N < 1500, three random subsets
of the primes each, `q = nextprime(N) ≤ 2N`: `Σ_{p≤N}ν(p)` equals the count
exactly, 0 failures. The statement is correct and trivial. Note
`N·E_Uν = N|A|/q ∈ [|A|/2, |A|)`: only the prime-point evaluation is
exact, which is the author's point (certification needs the location of
the primes).

## Numbered defects

No FATAL, no MAJOR.

**m1 (MINOR; Thm 2.4 / Cor 2.5 / Rem (a), periods of ψ).** `E_{π_c}[ψ_cφ̄_j]`
is defined only if π (hence M') resolves the period of `ψ_c` (lifted:
`Q₀·per(ψ_c)`). Lemma 1.1 defines M' as a common multiple of M₀ and 𝒟;
the proof of Thm 2.4 never says M' also contains the twists' (and rows')
periods. Harmless (Lemma 1.1 holds for every multiple M', 𝒟 unchanged),
but "the twist never enters the level" relies on it. *Repair:* in Thm
2.4's proof, "take M' a common multiple of M₀, 𝒟, Q₀·(all row and twist
periods)".

**m2 (MINOR; Thm 4.2 proof).** Lemma 1.1 needs `1 ∈ 𝒟`;
`𝒟 = {lcm(q,q')}` need not contain 1. *Repair:* `𝒟 = {1} ∪ {lcm(q,q')}`.

**m3 (MINOR; Thm 4.3 labels and constants).**
(a) "no external input" should read "no ElT Prop 1.4 and nothing
conditional; uses Shiu's theorem and Mertens via K2 Lemmas 3.1, 4.2".
(b) The leak bound `𝔏 ≤ 1/4` (needed for χ² ≤ (4/3)p and for
`(1−𝔏)^{−2} ≤ 1+4𝔏`) requires a W₀ larger than K2's (which gives
`𝔏 ≤ 1/2`); say so. (c) The W-uniformity `C(W) ≤ C(log W)^c` is the
load-bearing input when W = (log 3Q)^8 grows; cite it explicitly as K2
Lemma 4.3 "W-dependence" (proof via K2 Lemma 3.1's `(log W)^{eH2^a}`),
and note that c is huge but absolute, so `𝔏 log Q = O(1)` only for
`Q ≥ Q₀(c)` (absorbed into C). (d) The W-smooth sum is
`2 log W + 12𝔏 log W + O(1)`; writing `(2+12𝔏)` with `𝔏 ≤ 1/4` gives
5 log W, so the 3 log W step uses `𝔏 log W = o(1)`; state it.

**m4 (MINOR but ledger-relevant; scope of Prop 6.1).** Prop 6.1 covers
PL §6 item 2's *second* bullet (`ν ≥ 1` only on `𝒜 ∩ [1,N]`), which PL
already called non-CRT; it does **not** cover the *first* bullet
(`ν(p) ≥ 0` only for `p ≤ N`, but `ν ≥ 1` on all primes of 𝒜): there the
Prop 6.1 construction fails (Dirichlet puts primes of 𝒜 above N into
every reduced class mod q), and the author rightly leaves it as an
Assessment ("mixed variant"). But the bottom line ("the finite-range
prime relaxation is shown to be no sieve limit at all") and the report's
ledger suggestion ("(D)22: 'ν ≥ 0 only at primes ≤ N' annotated by Prop
6.1") read as if that bullet were settled. *Repair:* in §0/bottom line
and the ledger, say "the `ν ≥ 1 only on 𝒜∩[1,N]` relaxation is vacuous
(Prop 6.1); the `ν ≥ 0 only at primes ≤ N` relaxation stays open
(Assessment)".

**m5 (MINOR; §6.3 aside).** For `d ≤ (log N)^{O(1)}` the uniform
unconditional error is Siegel–Walfisz's `N exp(−c(log N)^{1/2})`
(ineffective); the `3/5` exponent (Vinogradov–Korobov) applies only away
from a possible exceptional zero / for fixed small d. The conclusion
(errors exceed `π(N)e^{−(log N)^{3/4}}`) is unaffected — it is even
stronger. *Repair:* state both exponents.

**m6 (MINOR; Lemma 1.1 proof, presentation).** Note that `1 ∈ V_𝒟`
forces `Σ_x μ(x) = 1`, so μ is already a probability and π is μ
conditioned on 𝒜; this makes "supported on 𝒜" and `μ(𝒜) = m* ≤ 1`
transparent.

## Sources

K2, EK, PL, LS read in-repo (relevant lemmas checked line by line;
K2's Lemma 4.2 Case-A Shiu/Lemma 3.5 machinery taken as reviewed in
K2's two reviews, not re-derived here). No external PDF needed.
