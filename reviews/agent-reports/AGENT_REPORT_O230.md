# AGENT_REPORT_O230 — Synthesis V (cross-combinations of wave Y, (J)39–(J)56)

Branch side-agent/synthesis-five. Deliverables:
* SYNTHESIS_SPARKS5.md (deep file);
* 7 memos BRAINSTORM/s5_*.md (indexed in BRAINSTORM/README.md);
* scripts scripts/s5_* (C censuses + small Python checks).

The brief asked for 8–12 memos. I wrote 7 rather than pad: the extra own ideas went into the deep file. **ES is not
solved; no infinite case is claimed.**

## SHARP
1. **Three side numbers (PROVED, elementary).** Every word w = (t, u, v) lies on N_t = tp + 1 = AB, N_u = p + u = Av and
   N_v = p + v = Bu. On each side, χ is the genus character (−X/·). A clean side forces χ = +1 (Lemma S). There is a new
   u-side deformation u(K + u) = □ alongside (J)53's tK + 1 = □. Also gcd(tp + 1, p + u) = tu − 1 = A exactly, so
   χ = ψ(gcd(N_t, N_u)).
2. **Near-square hardness, mostly explained (EVIDENCE, 169 410 primes to 5·10⁶).** Exact three-side cleanliness removes
   about 70–80 % of the within-cell residual depletion for 10 ≤ K0 < 300, and all of it at K0 = 16 and 24. This was
   R225 spark S2, left open by (J)55. The K0 = 8 remainder is a *defective deformation*: primality forces 3 | m, and
   the sides are clean except for an exact 3². This is supported at K0 = 8 only. Generic square-defect sides are not
   depleted.
3. **Forced/unforced hardness law (EVIDENCE, 928 779 primes < 3·10⁷).**
   * N₋ ≤ U (PROVED), where U = words with no clean side.
   * corr(N₋, U) = 0.966.
   * Every hard prime ((J)48's 13, and each dyadic block minimum to 3·10⁷) is almost fully forced: N₋ = U or nearly,
     with a forced fraction of 0.55–0.89 against a median of 0.12.
   * **N₋/U is scale-stable at ≈ 0.75** (0.770 for p ≡ 1 (8), 0.739 for p ≡ 5 (8)), while N₋/N drifts 0.59 → 0.67. So
     the drift is the forced fraction, ≈ 0.5/√log p.
4. **CONJECTURE U (EVIDENCE to 2·10⁵).** For odd non-squares n ≡ 1 (4), U(n) = 0 only at n = 105. This is weaker than
   SQ₅ and has the same exception.
5. **REFUTED (useful negative).** "N₋ ≥ U/2", which would have made ES-five ⟺ U ≥ 1, holds at every prime below 5·10⁶
   (minimum 0.506) but fails at **p = 5 270 849, 17 188 937, 21 387 257** and at the composite 110 897. Nobody should
   chase an involution here.

## Mandatory combinations
* (i) The deformation is the binary norm-form shadow of (J)48's ℤ³ embedding, on three sides. No canonical
  non-embeddable lattice: B2.
* (ii) and (iii) **Prop R (PROVED, negative with exact scope).** Every local-invariant index of a word (Hilbert,
  Maslov, Dedekind/Rademacher, theta multiplier) is a function of (w mod 8, sgn w). So index sums are cell-occupation
  counts, and reciprocity can only relocate signs. Anti-T1 is the five-slice cells, i.e. ES itself.
* (iv) **Prop C (PROVED dictionary).** Certificate primes are the primes h with Frobenius c_∞σ_p, i.e. split completely
  in the CM field ℚ(ζ_M)⁺(√(p(θ² − 4))). T1 = "the twisted conjugation ceases to exist". Chebotarev plus divisibility
  is B2. Checked with 422 000 Legendre-pair tests and 1 723 PM-II certificates.
* (v) A uniform profinite sterility statement. The unavoidable global input is the size/degree coupling (the box), not
  sign and not congruences (Assessment).

## Verification done
* Lemma S: 0 violations over 220.7 M words (primes to 3·10⁷), and over all n ≡ 1 (4) ≤ 2·10⁵ with Jacobi ψ.
* The ns_census totals on (10⁵, 10⁶) are reproduced exactly.
* T1 control: at odd squares every side is clean by definition (U = 0). s5_U skips squares; Lemma S is vacuous there.
* I did not separately re-run odd squares through the C code.
* Caveat: the residual tables use naive standard errors. The 74 040-cell refinement was discarded because singleton
  cells shrink residuals.

## For the reviewer
* The census definition of "clean" includes the prime 2 (ψ(2) must be +1).
* Lemma S needs p ≡ 1 (4). For n ≡ 3 (4), χ = −ψ(A). My first composite run forgot this, produced spurious
  "violations", and was fixed by restricting to n ≡ 1 (4).
* The u-side deformation needs gcd(m, K + u) = 1 and p ≡ 1 (8) for full cleanliness.

## Sparks (not pursued)
* CONJECTURE D: defective deformations (gcd > 1) deplete. Test at other K0 ≡ 2 (mod 3), and at K0 = 28 and 12, which
  keep −0.03 and −0.025.
* Apply the three-side forced/unforced split to SQ_± (signed words, (J)52 steering rule). Does SQ_±'s record
  (|t| = 54) sit at a fully forced n?
* Derive the per-class constants 0.770 and 0.739 of N₋/U from 2-adic cell masses of unforced words.
* A heuristic for f(p) and for record-hard primes built on U(p) rather than N(p). It predicts that records sit at
  p ≡ 1 (mod 840) with large lnr; the observed block minima agree.
* Is CONJECTURE U provable? It only needs one word with three unclean sides, a much weaker "anti-Landau" event than a
  certificate. Its equivalence with SQ₅'s exception set (only 105) is suggestive.
