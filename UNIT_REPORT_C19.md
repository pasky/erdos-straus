# UNIT C19 report

## Outcome

Added §53 and `verify.py (az)`.  The requested raw-mass fixed-box theorem was not stated because its overlap premise is false: distinct slice labels can have the same radicand `c*k^2`.  Section 53 replaces it by the exact root-union mass and then proves the growing theorem from the duplicate-free squarefree-`c` subfamily.

## Proved

- **Lemma 53.1a:** common root classes force `q | 4(c1*k1^2-c2*k2^2)`; distinct radicands are disjoint above the sharp `4T^2` threshold.  Equal radicands remain permanent duplicates.
- **Theorem 53.1 (effective):** for fixed `T`, a reduced hard class has stacked upper-sieve exponent `1+m_#(C)`, where `m_#` is the exact root-union density.  The single-slice specialization agrees with Theorem 52.1.
- **Corollary 53.2:** every fixed class with an active slice has a zero-relative-density no-good-factor set; escape classes retain only dimension one.
- **Total mass:** `sum_{ck<=T} 2/phi(4ck) ~ C_sl (log T)^2`, with an Euler-product constant; only the elementary upper bound is used later.
- **Exact genus distribution:** prime-core bits for primes at least 5 are independent uniform signs over reduced hard classes modulo `Q_T`.
- **Lemma 53.2a:** one negative prime-core bit `q` deterministically supplies canonical active mass `>> log^2(T/q)/q`, including after a one-conductor Page deletion.
- **Theorem 53.3 (effective):** for every fixed `0<A<1`, the no-good-slice-prime set is
  `<<_A X/log X * exp(-c_A (log log X)^(3/2)/sqrt(log log log X))`;
  the proof uses the uniform-in-dimension beta-sieve fundamental lemma and an effective Landau–Page repair of Siegel–Walfisz.
- **Corollary 53.4 (effective):** the same bound holds for failures of the varying-cutoff `H_SPF(A)` event.

## Failed or corrected targets

- `m_raw(C)=sum 2/phi(4ck)` is not the union dimension.  `(5,2)` and `(20,1)` have the same radicand 20; on active classes their ray union contributes `1/8`, while raw addition gives `3/16`.  Claiming exponent `1+m_raw(C)` would overcount identical root classes.
- The proposed implication “above a resultant threshold all root classes across distinct slice labels are pairwise distinct” fails when the resultant is zero.  It is true only after grouping equal radicands.
- At `T=30`, the requested verification interval `(4*30^3,10^5]` is empty.  Block `(az)` checks the stronger nonvacuous interval `(4*30^2,10^5]`, containing 9,089 primes.
- No pointwise `H_SPF`, conspiracy-depth bound, lower bound for residual vanishing, or improvement to a §17 wall is claimed.

## Labels and effectivity

- Theorems/Lemmas/Corollaries 53.1a–53.4 are labelled **proved**.
- Computational 53.5 is labelled **exact ranges; informational**.
- The fixed-box theorem is effective.  The growing theorem is also effective after deleting moduli induced by the at-most-one Landau–Page conductor; Lemma 53.2a proves the retained mass stays of the same order.
- Named classical inputs: upper-bound beta-sieve fundamental lemma (Friedlander–Iwaniec, *Opera de Cribro*, Theorem 6.9), ordinary Mertens, Mertens in arithmetic progressions, Siegel–Walfisz, Landau–Page, and Selberg–Delange.  Bombieri–Vinogradov and Chebotarev are explicitly not used.

## Verification

`verify.py (az)` checks:

- exact overlap geometry for all 111 labels with `ck<=30`, one small collision, and one permanent duplicate;
- `Q_30=9,316,358,251,200`, 256 seeded random reduced hard classes plus a direct escape class, raw and corrected mass regressions, and empirical prime-bit diagnostics;
- all hard primes below 30,000 (or 100,000 under `ES_FULL_SCAN=1`), reproducing the `ck_pr<=30` counts and informational no-good-factor mass bands.

## Hostile-review priorities

1. Check the precise uniform-in-dimension consequence quoted from *Opera de Cribro*, Theorem 6.9, especially the absolute upper-sieve bound when `s >= B*kappa` and `kappa` grows like `(log log X)^2`.
2. Audit the Page-deleted Siegel–Walfisz statement uniformly on `[Q_T,z]` and the claim that summing its errors over `O(T log T)` slices is harmless.
3. Check the aggregate elementary remainder in (53.32), including the beta-sieve remainder coefficients.
4. Verify the Selberg–Delange Euler-product constant in (53.17); it is record-only and not load-bearing.
5. Recheck that the canonical pairing in Lemma 53.2a remains duplicate-free and survives every possible fundamental-discriminant conductor, including 8 and fixed conductor 4.
