# AGENT_REPORT_O179 — spark relay F: explicit sterile point for ES₃(T²)? (checkpoint 1)

Main file: `FF_STERILE_PROOF.md`. Scripts: `scripts/fsp_enum.py`, `scripts/fsp_cyclo.py`. Data: `data/fsp_cyclo_K15_150.txt`.
Merged: side-agent/ff-sterile-point, side-agent/spark-signlayer, main (R175 review).

## SHARP:
1. **O(q, A) is Haar-null in R̂^*, for every q and monic A (Thm 3.2, PROVED, ~5 lines).** Almost every x is covered by
   infinitely many families of the single shape (ℓ prime; types 0,2; a₀ = b₀ = 1). The proof uses π-weights:
   validity at a prime ℓ | E depends on x mod ℓ only through π^{w(t_a)} vs π^{w(t_b)}, w = (0,1,1,2), and the
   (0,2) condition x ≡ −A (mod ℓ) is independent across primes; Borel–Cantelli II + PNT in progressions.
   Consequences: settles R166 D11 (the ≈ 1 % ffl_tree plateau is a truncation artefact, not mass); a sterile point
   must be non-generic at almost all primes, and the slice x ≡ 1 off T is its natural home (it merges all type
   pairs into Case A/B). Types {1,2} are π-free: the Case B system exists at *every* x (with E ≡ −x mod L').
2. **Genus parity lemma (Lemma 2.1, PROVED; 312/312 solutions checked):** every Case B solution on the slice has
   deg E, deg E' even, λ = deg L'' ≡ K, deg r ≡ K (mod 2). Quadratic reciprocity in F₃[T] applied to
   E | 1 + M Y² (M = L'' or TL''). This also supplies the missing step of O175 Lemma 3.1(ii) (R175 D7) and shows
   cyclotomic (r constant) solutions exist only at even K.
3. **The covered slice measure is NOT 1/2 (Assessment) and cannot be a character effect (PROVED):** 1 + TF₃[[T]] is
   pro-3 (no ±1 characters); a continuous swap of covered/uncovered forces C clopen. Exact decomposition:
   1/3 (the K = 2 cyclotomic family) + 2/27 (K = 5) + 4/81 (K = 8) + tail; extrapolated limit ≈ 0.493.

## Goal (1) — NOT achieved (honest)
No explicit sterile point. At x*_c the problem reduces exactly (§4) to: no factorisation T^K + r = H·H'·L'' with
H + H' = Tg'r and H + (1 + cT)H' ≡ 0 (mod T^{⌈K/2⌉+1}) — a divisor-in-a-class problem with moving modulus r,
i.e. the function-field B2. Every elementary count of solutions stops at exactly 3^{K/2} (§6: min(3^ρ, 3^{K−ρ})),
which is the cylinder mass: the measure route needs #sol(K) ≤ 3^{(1/2−δ)K} (data: ≈ 3^{0.2K}). Choosing a point
other than x*_c does not help: off-slice points meet Thm 3.2; global points x ≡ θ add families; on the slice all
points face the same lottery. New partial facts at x*: deg E, deg E' ≥ N + 1 via the genus lemma (weaker than
O173's l ≥ (N+1)/4 in most ranges).
EVIDENCE beyond K = 19: **all cyclotomic solutions for 15 ≤ K ≤ 150** (34 (K, r₀) with > 3·10⁵ splits skipped,
listed in the log) — none covers x*_{±1}; closest v_T = 12 vs needed 14 at K = 26.

## Goal (2) — answered (§5): no exact 1/2; table of exact measures; no character/involution mechanism.
## Goal (3) — not reached (depends on (1)). Thm 3.2 holds for all q, A as stated.

## Checks
`fsp_enum.py 14` (independent arithmetic, explicit verification of (I),(II)) = `bsB_caseB 14` exactly (312 lines);
`fsp_cyclo.py 2 14` cyclotomic counts = fsp_enum's. Measure table recomputed from a fresh `bsB_caseB 19` run.
Nothing claimed about ES over Z.

## Sparks (not pursued)
* Thm 3.2's BC-II argument may refine to an integer statement: "for almost all residue patterns" ES via one fixed
  family shape — compare with the known density-1 results; probably just a restatement (check before chasing).
* Artin–Schreier (cubic) symbols at T *do* see the T-adic digits of u; if D = 1 + T^{K+2}L'g' had a norm structure
  from a cyclic cubic extension, a cubic genus constraint could exclude whole cylinders. I saw no such structure.
* Cube trick in char 3: (T^n + r₀)³ = T^{3n} + r₀ gives near-solutions at x*_{−1} of the a-big cyclotomic type,
  killed only by g' failing to be monic (the sign layer again). A systematic "sign-layer near-miss" family might be
  where a proof for x* would have to look — or where a covering of x* at huge K hides.
* Equidistribution of T^K mod (T X − 1) over polynomials X with prescribed low digits (a Kloosterman/Weil-type
  sum mod T^s) is the precise input that would give O(3, T²) ∩ slice ≠ ∅ by §6.
* Why T^K + 1 has cyclotomic solutions only for K ≡ 4 (mod 8) (observed to K = 150) — probably a quartic-residue
  refinement of Lemma 2.1; could be a second sign-layer constraint.
