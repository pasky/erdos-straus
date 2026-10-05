# AGENT REPORT O27 — remaining large-sieve and prime-law escapes (branch `side-agent/ls-escapes`)

Deliverable: `EXCEPTIONAL_LARGESIEVE2.md` (checkpoint 1), script
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
6. **PL finite-range relaxation (Prop 6.1).** With "ν ≥ 1 only at primes of
   𝒜 ∩ [1,N]" the LP value is the exact count, attained at level `log 2N`
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

## Ledger suggestion (for the parent)

(D)19 open escapes: replace "the larger sieve over mixtures; twisted/hybrid
forms" by "closed (LARGESIEVE2 Thms 2.4, 4.2, 4.3)"; keep (E1) as
(H_LS∞). (D)22 open: "the large sieve applied to primes" closed (Thm 3.1);
"ν ≥ 0 only at primes ≤ N" annotated by Prop 6.1.
