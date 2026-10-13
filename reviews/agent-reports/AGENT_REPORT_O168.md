# AGENT REPORT O168 — deterministic existence mechanisms mapped onto ES (checkpoint 1)

Branch `side-agent/deterministic-existence`. Main file `DETERMINISTIC_EXISTENCE.md`; scripts
`scripts/de_jacobi_slices.py`, `scripts/de_pell_factor.py` (both tiny output, < 15 min, 1 core).

## Verdict
No route to ES; no case of ES is claimed. Precise negative/structural results for the Legendre/Holzer and Pell
mechanisms; one small T1-safe deterministic statement (Jacobi forcing).

## Results
1. **Catalogue (§1, Assessment).** 29 mechanisms (Thue, Minkowski/LLL, descent, Legendre+Holzer, Hasse–Minkowski,
   Davenport–Cassels, genus/Rédei, Legendre's Pell argument, units, involutions, topological fixed points,
   Chevalley–Warning/CN, EGZ/Kneser, Hall, CFT/Chebotarev, Linnik/Duke, strong approximation, Siegel, Thue–Siegel/
   Baker/S-units/Faltings, Burgess, Linnik-AP, Croot/Bloom, greedy, Euclid–Schur, Weil, polynomial method,
   compactness, ternary class-number-one) with shape / ES-shape / failing step (mapped to B1–B6, T1) / evadable?
   Only rows 4, 6, 9, 10 fail at a non-barrier step.
2. **Legendre/Holzer (§3).** PROVED, elementary (novelty modest; genus/Yamamoto/Bright–Loughran in conic language):
   * Prop 3.1: isotropy of F_θ = congruences of p + an "all prime factors split" condition on a p-dependent
     integer (opposite logical shape to ES's "∃ divisor in a class").
   * Prop 3.2: a Type I solution of level d forces χ_{−4d}(p) = −1, i.e. the conic X²+dY² = pZ² is anisotropic.
   * Prop 3.3: Σ_e(N) ⊆ H_e(N); −1 ∉ H_e(N) ⇔ all primes of N split in an odd cyclic K_χ ⊂ ℚ(ζ_e); for e | 24
     the slice fails *exactly* on norm-form representations (e = 3: N primitively = X²+XY+Y²).
   * So Holzer's "Z = 1" forcing certifies slice **failures**; ES uses Legendre only contrapositively.
   * Prop 3.4 (Jacobi forcing, T1-safe): prime e ≡ 3 (4), (p/e) = −1 ⇒ −1 ∈ H_e((p+e)/4). Never fires at m².
     EVIDENCE (p ≡ 1 (24) < 2·10⁵, e < 200): slice success 0.169 when (p/e)=+1 vs 0.373 when (p/e)=−1; the
     63% residue is the multiplicity lottery (B2/B4).
3. **Pell (§4).** Legendre's unit splitting deterministically factors N_e, but its pair solves the slice in 17.8% vs
   14.3% for a random coprime splitting (EVIDENCE, 1681 slices). PROVED core: its only constraints are Rédei
   relations among the prime factors, invisible to the class mod e for e ∤ 24.
4. Iteration records (§3.5, §4) for each mechanism: v1 → barrier → modification → next barrier.

## Not done
§5 (Davenport–Cassels/Aubry descent on X_d with the side condition 4ad | f+p) is only planned.
No positive claim needs the 10⁶ triple check (none is made).

## Sparks (not pursued)
* Higher-order Jacobi forcing: group-level success at slice e is forced iff ord_e(p·4⁻¹) is even; look for slice
  families (composite e, small exponent of (ℤ/e)^×) where forced group-level success plus a forced second prime
  factor gives Σ-success deterministically.
* Joint forcing across slices: ℓ | N_e and ℓ | N_{e'} iff e ≡ e' (mod ℓ); a matching between Jacobi-forced primes
  and slices (Hall-type, H-A) might force a prime ℓ ≡ −1 (mod e) somewhere.
* Type I analogue of Jacobi forcing with modulus 4cd and χ_{−4d} (Prop 3.2 is the necessary side; is there a forcing side?).
* Euler's factoring method (two norm representations ⇒ a factor) as a factor source with class control.
* Aubry descent (§5).
