# z52 deep lane D (Astra): pointwise existence in thin regimes

**Status: WORK IN PROGRESS. ES is OPEN.**

## Summary

Pending source verification and hostile review. All proposed ES transfers are conjectural unless explicitly proved.

## §0. Taxonomy and novelty audit

**Assessment / scope.** This is a source-limited catalogue, not a claim to have exhausted all mathematics. “Expected count” needs a specified sampling model and height cutoff. Below, **thin** means a bounded or polylogarithmic *number of final witnesses*, not a short description, a sparse ambient set, or a theorem whose statement merely says “there exists”. Exact counts override heuristics. Most examples proposed in the brief are useful countercomparisons, not thin precedents.

| Class | Decisive structural feature; representative | ES verdict and prior screening (Assessment) |
|---|---|---|
| α: exact identity / unique factorization | Norm factorization; two squares at a prime has one representation up to signs/order | Fixed norm recipes screened in `POINTWISE_BINARYFORM.md`, `DETERMINISTIC_EXISTENCE.md` §§3–4; B1 excludes their fixed-menu transfers, not every nonlinear construction. |
| β: mass / analytic surplus | Ternary/quaternary forms have power-scale representation reservoirs in their nondegenerate ranges | `LITERATURE_AUTOMORPHIC.md` §3; B3. Universality is not evidence for a polylog main term. |
| γ: generation / expansion | A large orbit and enough room to hit the target; Zaremba with large alphabet | `B2_ACROSS_FIELDS.md` §4.1 already records the 2026 full claims. B3 remains; “all thin-orbit results are almost-all” is obsolete, not the corrected verdict. |
| δ: rigidity / local–global | Homogeneous actions or an actual local–global theorem in the right category | `BRAINSTORM/z31_dynamics_ergodic.md`, `GEOMETRY_ES.md`; rational points and dense real orbits are not positive integral ES points (checklist 13). |
| ε: geometry of numbers / collision | Convex volume or pigeonhole, followed by an exact size-to-equality step | `DETERMINISTIC_EXISTENCE.md` rows 1–2; B4 does **not** exclude arbitrary target-specific arguments. Divisibility by one prescribed integer is not convex. |
| ζ: descent / finite carry algorithm | A potential decreases while preserving the certificate class; palindrome addition | `CONSTRUCTIVE_ES.md`, `PROPAGATION_CLOSURE.md`, `DETERMINISTIC_EXISTENCE.md` §5; no cross-slice potential known. The palindrome paper itself is not substantively screened in the grep hits, but its reservoir is not thin. |
| η: parity / degree / count congruence | A finite auxiliary set has a computable index, and nonzero index forces a desired fixed point | `INVOLUTION_ES2.md`, `MARKOFF_ES.md`; finite affine menus excluded in their precise scope. A growing, arithmetic-dependent **quotient index** remains unexcluded, not demonstrated. |
| θ: growing covering / Ramsey compactness | Arbitrarily large reservoir; finite-color or finite-type obstruction | `DETERMINISTIC_EXISTENCE.md` row 28 and `B2_ACROSS_FIELDS.md` §3. No passage from profinite witnesses to integral height bounds (B1, checklist 12). |
| ι: induction with transport | A witness at a predecessor is transported with no loss of constraints | `TRANSPORT_LAW.md`, `PROPAGATION_CLOSURE.md`; multiplication propagates ES to composites, not new primes; numerator-8 controls prevent blind transport. |
| κ: character / Chebotarev detection | Search is over freely chosen primes or integers, not divisors of a prescribed number | `CLASS_FORCING.md`, `OAI_DUMP_IMPACT.md` §5; checklist 9 and B-fin. Least-QNR bounds do not finish a witness. |
| λ: probabilistic / spectral selection | Free output choices, with a positive-probability or interlacing certificate | `BRAINSTORM/prob_lll_fixed_p.md`, `BRAINSTORM/z45_interlacing_stable.md`; Legendre data at fixed p are not free signings. |
| μ: polynomial divisibility / nonvanishing | Degree deficit, a known zero, or a nonzero grid coefficient | `BRAINSTORM/polynomial_method.md` **including errata**; CW is not a generic “3 unknowns, cubic” theorem. Homogenization supplies a fourth variable but loses integrality; §2.2 computes the loss. |
| ν: targeted additive relations | A relation with prescribed nonidentity value inside an exact exponent budget | `BRAINSTORM/z33_target_davenport.md`, `EXSET_CHAR_FORCING.md`; ordinary Davenport forces identity, not −1. A target-sensitive coefficient or quotient relation remains outside blanket B4 claims. |

**Assessment / novelty boundary.** No broad class above is wholly unscreened. The new work here is (i) source-verified count/quantifier triage, (ii) the explicit homogenized boundary calculation, and (iii) three narrowly specified first tests in §2. The names “CW”, “zero-sum”, “parity”, and “descent” are not new ES ideas. Existing errata already repair the old claim that hitting −1 requires full coverage; this memo does not claim credit for that correction.

**Audit trail.** Before recording transfers, ran `git grep -il` for Chevalley, zero-sum, Davenport constant, Nullstellensatz, involution, palindrome, sensitivity, G4, Kneser, homogenization, and the theorem names in the three source ledgers. Read `FRONTIER.md` §§2–7, the required literature/update files, `OAI_DUMP_IMPACT.md` §5–6, `BREADTH_Z45.md` §§15–16, `B2_ACROSS_FIELDS.md`, and the specific screens cited here. Claims about scope below are Assessments, not no-go theorems for all possible ES proofs.

## §1. Source-verified catalogue

Pending. Each entry records quantifiers, witness scale, forcing mechanism, source/version/access, and ES barrier.

## §2. Candidate mechanisms and falsifiable first lemmas

Pending. Three to six candidate refinements, not recycled claims of solving B2; include numerical controls and hostile review.

## §3. Sources, checks, and limitations

Pending. Short decisive excerpts in `sources/z52/`; memory-bounded scripts under `scripts/z52_thin_*`.
