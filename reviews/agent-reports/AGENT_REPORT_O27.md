# AGENT REPORT O27 — remaining large-sieve and prime-law escapes (branch `side-agent/ls-escapes`)

Deliverable: `EXCEPTIONAL_LARGESIEVE2.md` (checkpoint 2), script
`scripts/largesieve2_checks.py`, output `data/largesieve2/checks.txt`.

## Results

1. **Lemma 1.1 / 1.2 (PROVED, conditional on K2 Thm 5.1 / PL Thm 3.1).**
   LP duality turns K2's cap into one *comparison measure* π on 𝒜 with
   `E_π f ≤ e^{S(λ)}E_U f` for every nonnegative level-λ f (unit-measure
   version from PL). This is the engine for everything below.
2. **Escape 3 closed (Thm 2.4, Cor 2.5).** Any periodic Bessel system
   (additive, multiplicative, hybrid χ(n)e(nθ), Gauss-sum or other periodic
   rows) of polynomial row period, applied to `ψ·1_A` with any periodic
   twist `|ψ| ≥ 1` on 𝒜 (any period; Cauchy–Schwarz removes ψ), fibrewise
   over `Q₀ ≤ min(N^A, N/2)`, and mixed fibre by fibre with
   majorant-with-rounding fibres: saving `≤ C_A(log N)^{3/4}(log log N)^{3/4}`.
   This also writes out LS §1's "hybrid" sketch.
3. **Prime large sieve closed (Thm 3.1).** Same cap relative to `π(N)`,
   provided all primes of `M'` (family, rows, twists, `Q₀`) are `≤ N^A`.
4. **Escape 2 closed for prime-power kernels (Thm 4.3); composite kernels partial (Thm 4.2).** (H_Gal) is PROVED, unconditionally:
   the plain sequential law with base `R_W^□`, `W ≍ (log Q)^8`, conditioned
   on 𝒜, has `Σ_{ℓ^v≤Q}(log ℓ/ℓ^v)χ²_{ℓ^v} ≤ 24 log log 3Q + C`, so
   Gallagher's larger sieve (optimal and Cauchy–Schwarz forms, any Q) saves
   `≤ 26 log log N + C` over every mixture. Uses only K2 Lemmas 2.3,
   4.1–4.3 and EK Lemma 2.1 (no K2 Thm 5.1, no ElT Prop 1.4). Arbitrary
   kernels (composite moduli of level ≤ λ_𝒮) are capped by Thm 4.2 only up to
   the factor `1 + Nh/(W_K−h)`, which is not controlled in general (kernels
   with `W_K − h ≪ Nh` stay open).
5. **(E1)/(H_LS) sharpened, not closed (Props 5.1, 5.2).** Only frequencies
   whose denominators have `≥ (log N)^{4ε/3−o(1)}` distinct family primes can
   beat `(log N)^{3/4+ε}`; and the cap follows from Lemma 1.1 at level 2λ'
   plus a *sup* Fourier bound at level > λ' for the same π (no cross terms;
   a criterion different from — neither stronger nor weaker than — LS's
   ℓ^{2+2β} form). (H_LS∞) remains CONJECTURE; the
   obstacles (abstract dual π, reweighted KARY law, top-prime-only decay of
   the plain law, density loss of product sub-laws) are listed.
6. **PL finite-range relaxation (Prop 6.1), one of two bullets.** With "ν ≥ 1
   only at primes of 𝒜 ∩ [1,N]" the LP value is the exact count, attained at level `log 2N`
   by a nonnegative ν; no cap of any kind exists — the gap is certification
   (non-CRT), not majorant design. Signed unconditional errors: Assessment.

## Self-review (deep reviewer subagent, applied)

No errors in Lemma 1.1, Thm 2.4, Thm 4.3 (incl. transfer of K2 Lemma 4.3
to the singleton law and the constants 24/26), Lemma 4.1/Thm 4.2. Applied:
composite-kernel overclaim removed; prime-cap hypothesis (primes of `M'`
`≤ N^A`) added; "weaker than (H_LS)" corrected to "different criterion";
`Q₀ ∈ 𝒟` hypothesis in Rem (iii); `max(λ₀,·)` in Prop 5.1; NumPy seeded.

## Points for the reviewer to attack

* Lemma 1.1's LP duality (sign conventions; that π may depend on 𝒟 is
  harmless because every application fixes a finite 𝒟 first).
* Thm 2.4's admissibility definition for twisted sequences (lower bound
  must hold for all π on 𝒜; requires `|ψ| ≥ 1` on 𝒜) and the fibre
  bookkeeping (1.2).
* Thm 4.3: that K2 Lemma 4.3 transfers to the plain singleton law σ with a
  Q-dependent W (only chain-rule inflation is used), the χ² conditioning
  inequality, and the case analysis in the consequence.
* Prop 6.1 is deliberately simple; check that its reading (the relaxation
  is vacuous) is fair to PL §6 item 2's mixed variant, which is left as an
  Assessment.

## Numerics

`OMP_NUM_THREADS=2 ... python scripts/largesieve2_checks.py` (~7 s): duality
and comparison identity of Lemma 1.1 exact on a 9240-periodic toy family;
Lemma 2.2/Thm 2.4 and Lemma 4.1/Thm 4.2 inequalities; Thm 4.3's proof steps
on the exact sequential law. EVIDENCE only.

## Checkpoint 2: hostile review R27 applied

R27 (`reviews/exceptional-largesieve2-review.md`): all claims SOUND, no
FATAL/MAJOR. Applied: m1 (M' contains row and twist periods in Thm 2.4),
m2 (`1 ∈ 𝒟` in Thm 4.2), m3 (Thm 4.3 label "unconditional; Shiu + Mertens,
no ElT Prop 1.4"; enlarged W₀ for 𝔏 ≤ 1/4; W-uniformity of K2 Lemma 4.3
cited; `𝔏 log W = o(1)` step made explicit), m4 (Prop 6.1 covers only the
"ν ≥ 1 only on 𝒜∩[1,N]" relaxation; "ν ≥ 0 only at primes ≤ N" stays open),
m5 (Siegel–Walfisz exponent 1/2 vs Vinogradov–Korobov 3/5), m6 (μ is a
probability). Also: KARY3 Thm 4.1 ((D)24) removes the `(log log N)^{3/4}`
factor from every K2-based cap here (Lemma 1.1, Thms 2.4, 4.2, Cor 2.5,
Prop 5.1); for the unit-measure Thm 3.1 via KARY3 §4.3 (pointer level).

## Ledger suggestion (for the parent)

(D)19 open escapes: twisted/hybrid forms closed (Thm 2.4); Gallagher's
larger sieve over mixtures closed for prime-power kernels, unconditionally,
saving `O(log log N)` (Thm 4.3); composite kernels capped only where
`Nh/(W_K−h)` is controlled (Thm 4.2); keep (E1) as (H_LS∞). With KARY3 the
caps are `C_A(log N)^{3/4}`. (D)22 open: "the large sieve applied to primes"
closed (Thm 3.1); "ν ≥ 1 only on 𝒜∩[1,N]" shown vacuous (Prop 6.1);
"ν ≥ 0 only at primes ≤ N" stays open (Assessment).

## Checkpoint 3 (§§8–9, unreviewed)

Task: serious attempt on H_LS / H_LS∞ and on composite kernels with
`W−h ≪ Nh`.

1. **(E1): explicit escape, for dense abstract families (Thm 8.5, PROVED).**
   Band family: for disjoint prime pairs `D_i = ℓ_iℓ'_i`, forbid the
   ≍ηD_i classes mod `D_i` whose phase `na_i/D_i` lies within η of 1/2.
   * Lemma 8.1 (Gale's supply–demand theorem): there is a measure on each
     band set with uniform one-prime marginals. Hence every majorant whose
     terms have level `< L_i` has mean `≥ 1` (Prop 8.2(a)): the level-λ
     comparison measure exists with `S = 0`. If the primes are only
     `> e^{λ/d}`, EK Thm 2.5 gives saving `O_d(log K)` (Prop 8.2(b)).
   * A Montgomery–Vaughan large sieve on the sumset `{Σ m_iθ_i}`, using
     products of an explicit L²-small arc majorant (Lemma 8.3), saves
     `≥ c log N` (Prop 8.4). Its frequencies have level `≥ Kλ`.

   So (E1) **cannot** be closed by Lemma 1.1 plus the large-sieve axioms. A
   proof of (H_LS∞) for forced families must use the sparsity (Sp) — mass
   `≤ D^{−1+o(1)}` on classes with modulus divisible by D — or K2's moment
   hypotheses, both of which the band family violates. (H_LS∞) for forced
   families remains CONJECTURE (budget heuristic, §8.2).
2. **Composite kernels (Thm 9.1, Prop 9.2).** The level hypothesis of Thm
   4.2 is removed entirely: moduli `≥ N` are controlled by anti-concentration
   of the comparison measure via prefixes. For T-rough kernel moduli the
   factor `1 + Nh/(W_K−h)` is harmless up to `T^{1/4−o(1)}` (unconditional).
   Open: kernels with `Nh/(W_K−h) ≥ e^{(log N)^{3/4}}` and small prime
   factors in their moduli. There 𝒜 is genuinely non-uniform (selectors,
   ℛ(3)). No escape is known; the band family does not give one for kernels.
3. Numerics: check (5) of the script verifies Prop 8.2(a) by LP (value
   exactly 1) and Lemma 8.3 numerically.

Ledger suggestion: (D)25 (E1) entry: add "explicit escape for dense
abstract class families (LARGESIEVE2 Thm 8.5); a cap needs sparsity (Sp)";
composite kernels: "capped at any level up to `1+Nh/(W_K−h)`
(Thm 9.1); open only for small-prime kernels with `Nh/(W_K−h)` huge".
