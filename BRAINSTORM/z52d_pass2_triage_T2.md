# z52d Pass-2 triage of "interesting" items, shard T2 (18 items from TO0b/ZF0/ZF1; Opus)

ES is OPEN; nothing here bears on it beyond calibration. Input `data/z52b/pass2/triage_input_T2.jsonl`; verdicts in
`data/z52b/pass2/triage_interesting_T2.json`; per-item notes in `triage_notes_T2.jsonl`. Re-runs in `/tmp/t2x/*`
(each under `timeout 300`, `ulimit -v 6e6`). Every PROVED claim below was checked step by step by hand unless marked.

## Counts
NEW-CALIBRATION 8 · EXPLAINED-BY 4 · REDISCOVERY 4 · ARTIFACT/WEAK 2 · NEW-STRUCTURAL 0 · DEPTH 0.

## PROVED claims: status after checking
- **Z2797** (BALANCED_LATTICE caps): VERIFIED. BLPS Lemma 2.1 (Banaszczyk 1996 Lemma 3) is applied with K = cube and
  H = cross-polytope, which gives μ∞·min(1,𝔻_min) ≤ C₀·k√log k. The CONDITIONAL exponents improve: Thm 4.1 13/2 → 6,
  Thm 4.2 9/2 → 4. C₀ is not explicit. The finite caps were reproduced independently: 4385 → 3710 and 1205 → 775.
  This refines the cap route only (cap ≠ ES). Suggested: a remark in BALANCED_LATTICE §1/§4.
- **Z2834** (Br S_{3861,4}): VERIFIED. Pic S̄ = Z_sign over Q(√Δ), Δ = 31·167·857·12973, so Br₁/Br₀ = ⟨(Δ,d)⟩. The
  Gysin computation on A² ∖ H with residues vanishing at the degree-2 base points (−q₀ = ((nq₀+n²)/8)²) gives
  Br(S)/Br(Q) = (Z/2)² = ⟨A,B⟩. The local points are orthogonal to both classes, and the complete search still gives
  0 positive triples. So the zero at 3861 is not a BM obstruction for this model. The six-cycle cross-check was not
  re-verified, and my automated Hilbert-symbol script hung and was killed. All symbols were done by hand instead.
- **Z2835** Thm 1(b) (Mordell locus 4k+n³ = s²): VERIFIED; every local case was checked. Re-run: 248/248
  hypothesis-true pairs are empty (n ≤ 501, k ≤ 2·10⁴).
- **Z0086** (positive ES over O_{Q(√3)}, rational n): VERIFIED with exact arithmetic. η = (2+√3)⁵ ≡ −1 (mod 11),
  κ = 33+19√3, e = 11.
- **Z2776** (I3(3^k+2), k ≥ 3, k ≠ 4): VERIFIED via the three L-word congruences (mod 8, 15, 90). The 3^k−2
  non-coverability claim was NOT re-verified.
- **Z2306** (parity lemma): true and elementary, but the content was already in the repo (EXPLAINED-BY).
- **Z0077** (inert-prime reduction): true and elementary. The positivity obstruction is CONJECTURE.
- **Z0087**: correct, but the "every odd ℓ" proof is already in the repo (avenue out_P00 Z0052).
- **Z2418, Z3054**: their effectivisation sketches (effective BV off one modulus; the Tatuzawa upgrade) are unreviewed
  Assessments and were NOT verified here. Treat them as Assessment, not PROVED.
- **Z1894**: Lean formalisation of an already-PROVED theorem (parent build-verified).

## NEW-CALIBRATION (one line each)
- Z0005: FF with leading coefficients in the squares: 0 failures where monic fails (q=5 n≤4; q=7 n≤3). Re-run matches.
- Z0086: D = 3 upgraded from EVIDENCE to PROVED in other_rings §3 (twin world, no transfer).
- Z0077: the cyclic-cubic Galois-orbit world is p-independent at inert p (PROVED). The 4 ∤ Tr(1/z) positivity
  obstruction is CONJECTURE.
- Z2797: norm-aware transference; CONDITIONAL cap exponents 6 and 4 (above).
- Z2834: full Br of S_{3861,4}; the empty fibre is not explained by Brauer–Manin (disproof side).
- Z2776: new I3 thin family 3^k+2 (no transfer to primes).
- Z2835: second BM locus of the pencil (Mordell locus); "T1 = k→0 limit" is an Assessment.
- Z3054: inventory of the Siegel-type inputs; the Tatuzawa remark is unverified.

## Corrections worth filing
- Z0178: farey_ford_cf §4's misses {5,17,41,241} are a *primitive*-triple count (gcd(a,b,c) = 1). The witnesses for 41
  and 241 are non-primitive but valid ES solutions (4/41 = 1/12+1/72+1/2952). Without the gcd condition the misses
  ≤ 8000 are exactly {5,17} (re-run). §4 should say "primitive".
- Z0114/Z0115: the 3-term local obstructions are TRUE. The records refuted 2- or 4-term variants (ARTIFACT/WEAK).

## Other dissolutions
Z0214: m = 9/25 exception sets reproduced (3 and 80 primes < 3·10⁴). This is a numerator-size effect; m = 9 is
already in avenue Z0735. Z2080: the over-dispersion sits on the edge line E(p) = #{d | p+1 : d ≡ 3 (4)} (single-integer
divisor overdispersion). Z0094: the Dirichlet unit theorem plus other_rings §4.
