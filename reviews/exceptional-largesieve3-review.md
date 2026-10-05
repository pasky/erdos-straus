# Hostile review of EXCEPTIONAL_LARGESIEVE3.md (task R59)

Reviewer branch `side-agent/review-ls3`; author branch `side-agent/hls-sparse`
(merged ff at review start). Scripts: `scripts/review_ls3_*.py` (from scratch).

## Verdict summary (in progress)

| claim | verdict |
|---|---|
| Thm 1.1 | SOUND |
| Lemma 2.1 | SOUND (minor D1) |
| Thm 3.1 | SOUND (conditional on reviewed internal K2 inputs + ElT Prop 1.4, as labelled) |
| Lemma 4.1 | SOUND |
| Lemma 4.2 | SOUND (computation); "symmetric route fails" is Assessment (D4) |
| §4.3 | (pending) |

## Claim-by-claim

### Thm 1.1 (smooth–rough splitting): SOUND

Re-derived line by line.
* Decomposition `𝒜 mod M₀ = {(c,r): c∈𝒜_s, r∈𝒜_c}`: a class `b mod G` with
  `G_r>1` contains `(c,r)` iff `c≡b (G_s)` and `r≡b (G_r)`; correct.
* HY step: with `f(c)=M_sπ_s(c)π̂_c(θ_r)` one has `f̂(θ_s)=π̂(θ_s+θ_r)`;
  HY on `ℤ/M_s` (normalised Haar on the group, counting measure on the dual,
  `1<p≤2`) gives `‖f̂‖_{p'} ≤ ‖f‖_{L^p}`;
  `E_c|f|^p = Σ_cπ_s(c)(M_sπ_s(c))^{p−1}|π̂_c|^p ≤ ρ^{p−1}E_{π_s}|π̂_c|^p`;
  `(p−1)p'/p = 1` (since `p' = p/(p−1)`), so the density enters exactly to the
  first power; Jensen `(E X^p)^{p'/p} ≤ E X^{p'}` as `p'/p ≥ 1`. Correct.
  Non-uniformity of π_s is harmless: only `sup π_s ≤ ρ/M_s` is used.
* Hölder: `|π̂|² = |π̂|^{p'/(1+β)}` and
  `Σ w|π̂|² = Σ w^{β/(1+β)}(w|π̂|^{p'})^{1/(1+β)}`; correct. `Σw≤1` (LS Fact
  4.0), `w≤1/N` (LS Fact 1.1), distinct θ, `π̂=0` off `den θ | M₀` (π lifted
  uniformly on unresolved digits, LS Rem 3.3 sharpening). Correct.
* Final algebra `log(N/B) ≤ (β log N + log 𝓡)/(1+β)` checked.
* Brute force (from scratch): `scripts/review_ls3_thm11.py` — see §Numerics.

Remark 1.1(c) (level-split form): re-derived. Low part: Cauchy–Schwarz
`|E_π h|² ≤ E_π|h|² = Σ_cπ_s(c)E_{π_c}|h(c,·)|²`; for fixed c, `|h(c,·)|²` has
rough frequencies of rough level ≤ 2λ', so the comparison applies;
then `≤ e^{S_r}ρ E_U|h|² ≤ ρe^{S_r}/N` (LS2 Lemma 2.2, Δ=1). High part:
`|π̂(θ)| ≤ E_{π_s}|π̂_c(θ_r)| ≤ (e^{S_r}/N)^{1/2}` (no ρ). Total
`(ρ+1)e^{S_r}/N`, so `log(N/B) ≤ log ρ + S_r + log 2` (ρ ≥ 1). SOUND, but the
hypotheses must hold for **every** c in supp π_s (not on average, unlike the
Hölder form); the doc says this implicitly ("for c in a set of probability
≥ 7/8" in §4 is then absorbed through the event E of Lemma 2.1 — fine, but
see D3).

### Lemma 2.1 (density of the z-smooth part): SOUND (minor presentational gaps)

* Failure probabilities: leak `Σ_ℓ E[p_ℓ1{p_ℓ>ℓ^{−1/2}}] ≤ 1/8` bounds
  `Q'(∃ℓ: y_ℓ∈F_ℓ)` (light coordinates never land in F_ℓ); `Q'(∃ℓ:p_ℓ>1/2)
  ≤ Σ4Ep_ℓ²`; Markov; plus `Q'(E)≤1/8`: total ≤ 1/2. Correct.
* Support: on G every class with z-smooth modulus is avoided (W-smooth ones
  by K2 Lemma 2.3(1); others are decided at their top prime ≤ z and can only
  be hit by `y_ℓ∈F_ℓ`). Classes with a prime > z are never activated at ℓ ≤ z.
  Correct.
* Density: `Q'(c) = base(c_W)·Π_{W<ℓ≤z}P(y_ℓ|past)`, each factor
  `≤ ℓ^{−E_ℓ}(1−p_ℓ)^{−1}` (light) or `= ℓ^{−E_ℓ}` (heavy);
  `−log(1−p) ≤ 2p` for `p ≤ 1/2` (true: `log 2 < 1`); conditioning on an event
  determined by c with probability ≥ 1/2 at most doubles. Correct.
* Inputs checked against K2: (Q1) = K2 §3 Step 1 + Cor 3.7 (`𝔐` is over the
  **universe** 𝔘, so uniform in 𝔊, `y ≥ y₀(W)`); (Q2),(Q3) = K2 Lemma 4.3
  ("every family 𝔊 ⊆ 𝔘", `C(W) ≤ C(log W)^c`, B-free); (Q4) = K2 §2 end
  (`γ'(ℓ) = (1−ℓ^{−1/2})^{−1}` from the caps); base = K2 Lemma 2.3(2). All
  match. K2 Thm 5.1 / Lemmas 2.3, 4.3 were reviewed SOUND
  (`reviews/exceptional-kary2-review-2.md`).
* Minor: see D1 (Q₀ vs M_s).

### Thm 3.1 (rough-slice mixtures): SOUND (conditional on K2 Cor 3.7, Lemma 4.3 — internal, reviewed; Case A via ElT Prop 1.4)

* "Fibre forbidden sets are exactly K2's activated sets at ℓ > z": a class
  with exactly one prime ℓ > z has top prime ℓ and z-smooth cofactor, so its
  activation depends on c only, and it is activated at ℓ iff c meets the
  cofactor class — i.e. iff its fibre class lies in `𝔊_c`. Correct. Hence
  `p^r_ℓ(c)` is a function of c with the Q'-law of K2's `p_ℓ`, and (Q2), (Q4)
  apply.
* `Q'(E₁) ≤ Σ_{ℓ>z}ℓ^{1/2}Cℓ^{−7/4}(log ℓ)^c ≪ z^{−1/4}(log z)^c`; Markov for
  E₂. Correct.
* Local bound: for uniform on the complement of a set of density p in
  `ℤ/ℓ^{E}` (lifted classes mod `ℓ^v`, v ≤ E), `|φ(a)| ≤ p/(1−p)` and
  `Σ_{a≠0}|φ|² = p/(1−p)` hold verbatim; `g^{1+2β} ≤ 2p·2^{2β}ℓ^{−2β(1−κ)}
  ≤ 4pℓ^{−α}`. Checked numerically (script).
* J: partial summation correct (boundary term `−z^{−α}𝔐(z) ≤ 0`,
  `𝔐(y)y^{−α} → 0`), `α∫_0^∞t³log³(e+t)e^{−αt}dt ≍ α^{−3}log³(1/α)` with
  `α = (log N)^{−1/4}/2`: gives `(log N)^{3/4}(log log N)³`. Correct.
* Assembly: `β log N = (log N)^{3/4}`, `16𝔐(z) ≤ 16K₃(log N)^{3/4}((1/4)log log N)³`,
  `64J`. Correct. N must be large enough that `z ≥ max(W₁, y₀)` and
  `Q'(E₁) ≤ 1/16`; implicit in "C".

### Lemma 4.1 (two-copy form): SOUND

`Σ_{a mod ℓ^E, a≢0}e(a(x−y)/ℓ^E) = ℓ^E1[x≡y (ℓ^E)] − 1` is right; the
product over S and the σ⊗σ average give `P_S`; Möbius/Parseval mod `M_T`
gives the collision identity; `|σ̂|^{2+2β} ≤ s_S^{2β}|σ̂|²` termwise.
Verified from scratch on random non-product measures mod `9·5·7` and
`4·3·5·7` (prime powers included), all S, β ∈ {0.05, 0.25, 0.5}:
`scripts/review_ls3_lemmas.py` (b).

### Lemma 4.2 (residue concentration): SOUND as a computation; the heading claim is an Assessment (D4)

* `−4 ∈ ℛ(M)`: definitional (K2 Def 2.0 / notes Lemma 18.1, `D = 1 | A²`).
  Re-verified forcedness from scratch through notes (16.1) with
  `u = w = 1, v = A`: for `n ≡ −4 (M)`, `s = (nA+1)/M ∈ ℤ` and
  `4/n = 1/s + 1/(nsA) + 1/(nA)` exactly, 959 pairs `(M,n)`, `M ≤ 159`.
  (A naive `x = kA` identity fails, e.g. `M = 3, n = 5` — irrelevant to
  the doc, noted only because it shows the check is not vacuous.)
* `m*(p,−4) = Σ_{M'}1/M' ≍ log X/log z`: correct up to the constant
  (`Σ_{M'≤X, z-rough}1/M' ~ e^{−γ}log X/log z`; the "half in the right class
  mod 4" is fine at the ≍ level). Numerically `1.91` vs `log X/log z = 4.27`
  for z = 30, X = 2·10⁶, p = 10007 — consistent with a constant `≈ 0.45`.
  Note: requires `M'` composite with many rough primes; with `X = N^A` this is
  allowed in the family.

## Numerics (from scratch, reviewer)

    ulimit -v 8000000
    timeout 600 uv run --with numpy python scripts/review_ls3_thm11.py
    timeout 900 uv run --with numpy python scripts/review_ls3_lemmas.py

* `review_ls3_thm11.py`: `M_s = 60`, `M_r = 7·11·13`; 180 random families
  of classes `b mod G`, `G | M₀` (**including multi-rough-prime classes**,
  which the author's check omits), correlated non-product π_s (random,
  heavy-tailed "spiky", uniform), fibre laws random or Dirac (worst case).
  Core inequality `𝓡_{p'}(π) ≤ ρE_{π_s}𝓡_{p'}(π_c)`: max ratio 0.970
  (spiky), **equality 1.000000** attained for π_s uniform on `ℤ/M_s` and a
  c-independent fibre law (so the constant ρ is sharp). π supported on 𝒜
  always. Hölder step with random weights (`w ≤ 1/N`, `Σw ≤ 1`): max ratio
  0.475.
* `review_ls3_lemmas.py`: (a) Lemma 4.2 forcedness + Mertens number; (b)
  Lemma 4.1; (c) Thm 3.1 local bound (`|φ| ≤ g`, Parseval `= g`,
  `Σ|φ|^{p'} ≤ g^{1+2β} ≤ 4pℓ^{−α}` for unions of classes mod `ℓ^v` in
  `ℤ/ℓ^E`, E ≤ 2): worst ratio 0.797.

## Defects

(see below)
