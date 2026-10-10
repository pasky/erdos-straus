# AGENT REPORT O131 — exact-formula hunt (branch side-agent/exact-formula)

Deliverable: `EXACT_FORMULA.md`. Scripts: `scripts/exf_*` (engine `exf_engine.c`, Hurwitz table `exf_hurwitz.c`,
validation `exf_validate*.py`, columns/rank search `exf_columns.py`/`exf_nullspace.py`, Hecke test `exf_hecke.py`,
genus comparison `exf_genus.py` → `data/exf/genus_out.txt`, residuals `exf_residual.py`, identity check
`exf_check41.py`). Binary dumps in `data/exf/` are not committed (regenerate: `exf_engine 20000 data/exf/n2e4`,
`exf_engine 20000 data/exf/m2e4 -1`, `exf_hurwitz 1400000 data/exf/H12_1p4e6.bin`, then `exf_arrays.py`, `exf_columns.py`).
Branches merged for reading: spectral-flip, typeii-spectral (incl. round 2), geometry-es.

## Verdict
**Negative, with exact scope. No exact identity with a structurally positive part was found.**

PROVED (elementary):
1. Lemma 1.1: completion of the Type I enumeration for composite n (scaling by k = f/gcd(f, 4a²d ± 1)).
2. Prop 2.1: T2⁺(m²) = 0 for every m (no gcd hypotheses). Prop 4.2: T1±(2^k) = 0.
3. §3.2: for cd | 6, the Type II (c,d)-slice is an exact combination of binary theta (genus-character)
   coefficients at 4c²dn + 1.
4. Prop 4.1: the signed decomposition. 2(T2⁻ ∓ T2⁺) − diag = Σ_{c,d} [odd/even Eisenstein part − 2]. The −2 is the
   trivial factorisation, a boundary term analogous to λ(n) in Kronecker–Hurwitz.
In each case positivity reduces to "some 4c²dn + 1 has a divisor in a given residue class". That is the
original problem, so none of these is a positivity mechanism.

EVIDENCE (exact computations, n ≤ 2·10⁴):
* Hecke test (no relation F(nℓ²) ~ F(n), F(n/ℓ²), twists; residual 14–51 %).
* Rank search: dim(span ES ∩ span classical) = 0 on all n, odd n, primes, p ≡ 1, 3 (4), p ≡ 1 (24).
  56 ES variants (weights 1, diagonal/Aut, a = 1, primitive, d- and c-slices, signs) vs 54 classical columns
  (H(kn), Σ_x H(mn − x²) with (−1)^x, χ₋₄(x), 3|x twists, τ, σ, λ, Σχ_D(d), τ of n ± 1, 4n ± 1, n² + 1, n² + 4, …).
* Best fits leave 46–72 % of the centred norm.
* Genus vs orbit: corr 0.50–0.74 for q ∈ {20, 28, 40}; genus mass Σ_{c≤C} grows like log²C while the ES count is
  finite (tables in §3.3–3.4).

## Overlap with O128 round 2
O128's Prop 9.1/9.2/8.3 independently contain the §3.1 decomposition (Eisenstein, genus pairing; sign at ∞). I
credit them in §3 and do not duplicate. My additions are the exponent-2 levels (genus = class, exact theta
identities), the numerical non-summability of the genus mass, Prop 4.1 (boundary form), the composite-n
completion and the rank/Hecke searches.

## Scope limits (honest)
* The dictionary is finite. Sums over d ≤ D(n) of class-number convolutions were not included beyond m ≤ 20.
  Weight-3/2 and Brandt-matrix theta coefficients of level n were not tested, since there is no PARI mf in the
  project env; `uv run --with cypari2` works if wanted. Note the size mismatch: all ES counts are ≍ log³n on
  average, with no √n part. So any identity with class numbers needs exact √n cancellation.
* The relation search used 500 random rows per set (more than the 110 columns), with an exact rank mod 2³¹ − 1. A
  relation valid only on a sparse subset (e.g. the Mordell-hard classes) would not be seen.
* Not explored: the Type I torus is anisotropic (divisors of N(n + 2c√−d), a CM torus), which is the one place
  class groups could enter. But the condition is on the *norm* class mod 4cd, so I expect the same split behaviour.
  Possible follow-up.

## Suggested ledger entry
(I)x O131 EXACT_FORMULA.md: exact Eisenstein/theta identities for ES slices exist (cd | 6 theta; signed
decomposition with boundary −2 per level), but no structurally positive one. No exact relation with 54 classical
functions up to 2·10⁴ (EVIDENCE). The genus/Siegel–Weil mass is not summable over c. Negative.
