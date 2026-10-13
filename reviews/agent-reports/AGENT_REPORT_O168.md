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

## Checkpoint 2 (parent requests 1–4)
5. **Aubry/Davenport–Cassels (§5, PROVED).** The Type I level conics 4cd·ea − 4da² − pe = 1 have positive rational
   points for every p (Prop 5.1), while integral ones are obstructed (Prop 3.2); so no rational⇒integral principle
   (any rounding, with positivity, with decreasing-denominator descent) holds on any quadric piece (Cor 5.2). Row 6 ✗.
6. **Higher-order forcing (§6, PROVED).** Box form Σ_e(N) = image of ∏[−k_i,k_i] (Prop 6.1). Group-level success
   is forced by residue data ⇔ −1 ∈ ⟨p·4⁻¹ mod e⟩ (Prop 6.2; 2-adic-valuation criterion for composite e; never at
   squares). Σ = H for all N ⇔ e | 24 (Prop 6.3), so Σ-success is residue-forced only for p ≡ −4 (mod e).
7. **Joint forcing / Hall (§7).** Sharing dichotomy: slices couple only through primes < E/4, whose incidence is
   congruence data (Prop 7.1). Joint data force exactly "block witnesses" (private cofactor as one block; Prop 7.2).
   **Thm 7.3:** every prime p ≡ 1 (mod M_E) (log M_E ≲ 1.5E) has no block witness at any Type II slice e ≤ E
   (elementary; checked on 20 primes for each E ∈ {7,…,31}, up to 2.4·10¹⁷). **Cor 7.4** (Linnik): infinitely
   many primes have no block witness at any slice e ≤ c₀ log p. Hall: matching fails for 34% of primes
   (E = 120) with no relation to success; Hall/Kőnig/LP reduce one-edge existence to counting.
   EVIDENCE: block witnesses solve 99.95% (p < 2·10⁵, E = 120) and 97.9% (p < 10⁶, E = 40) of p ≡ 1 (24).
8. **Type I forcing side empty (§8, PROVED):** for p ≡ 1 (4), residue data never force group-level success for Type I
   ((c,d)-form or e-slice), by a mod-4 / square-class argument.

Net: the deterministic (residue + sharing) content of the slice structure is characterised exactly; what lies beyond
it is the factorisation of private cofactors (H-A/H-B). No route to ES; no case of ES claimed. Novelty: Props are
elementary (genus/Yamamoto-type); Thm 7.3/Cor 7.4 are clean scope statements, probably new in this form (unchecked).

## Sparks (not pursued)
* Scale of Cor 7.4 vs truth: how large must E be (as a function of p) for block witnesses to exist for all p ≤ X?
  A computational curve E_block(X) would show whether block certificates need e ≫ log p in practice.
* Composite forced slices (Prop 6.2) with many prime factors ≡ 3 (4) give several Jacobi-forced primes at once
  (one per prime q | e? — no: one ℓ per character); check whether CRT-composite slices raise the Σ-rate.
* Euler's factoring method (two norm representations ⇒ a factor) as a private-cofactor splitter with class control.
* Involution/parity on the private part only (row 11 restricted to P_e): the residual problem after Prop 7.2 is
  "split P_e into a coset", a smaller target for H-B-type parity.
