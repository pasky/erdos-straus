# z52b Pass 1 — batch U05 (§2 untried, 207 items)

1. Batch U05 complete: 207 items, outcomes in `data/z52b/pass1/outcome_U05.jsonl`. ES remains OPEN; nothing here proves or claims progress beyond verified small-range facts.
2. Counts: covered 35, nothing 9, interesting 0, needs-compute 71, skipped 92.
3. Interesting items: none. The few surprises checked (Z1512 omega-stratified agreement, Z3151 prime witnesses, Z1581 mixture of failure reasons at p=409) each resolved into known or explained behaviour.
4. Covered most often by existing repo memos: FRIEZE_ES.md, FOREST_*.md, LORENZINI_W.md, fingerprint (isosceles law fingerprint-0229, x|z fingerprint-0190), free_fable #201/#164, data/z52b/variants*.json. Many §2 items are analogies or engineering (skipped), not ES steps.
5. Computed here (reproducible; data in `data/z52b/pass1/U05/`): Z1512/Z1608 numbers reproduced exactly; Z1478 F2-relaxation is necessary but wins only 9.1% of relax-holding pairs; Z2655 only 105 of the six U(n) sporadics is idoneal; C-form min witness Omega=1 for 373/380 primes (p<6000, C≤150).

## Scripts and data
* `scripts/z52b_p1_U05_fable.py` → `data/z52b/pass1/U05/fable.txt` (C-form census p≡1 mod 4, p≤6000, C≤150: 57,450 pairs, 1,522 wins). Covers Z1478, Z1512, Z1596, Z1608.
* `scripts/z52b_p1_U05_misc.py` → `data/z52b/pass1/U05/misc.txt` (Z1477 gcd lemma, Z1561 C=2 taxonomy, Z2655 idoneal test, Z0711 residues mod 4, Z0760 R(3^k), Z0857 isosceles).
* `scripts/z52b_p1_U05_409.py` → `data/z52b/pass1/U05/forensics409.txt` (Z1581 forensics, controls 401/433).
* `scripts/z52b_p1_U05_minomega.py` → `data/z52b/pass1/U05/minomega.txt` (Z1075 least winning C; Z3151 min Omega(d)).
* `scripts/z52b_p1_U05_outcomes.py` writes the outcome JSONL from the triage table.

## Key verified numbers
* Z1512: 8229 pairs (p<3000, C<40); 2356 have a subgroup containing −1; 1695 of those fail. Break-down by omega(N) for subgroup-containing pairs: omega=2: 308/2098 win; omega=3: 768/7534; omega=4: 395/4558 (8.7%); omega=5: 51/558. The hypothesis "≥95% agreement for omega≥4" is refuted.
* Z1608: among Omega≥5 failures (p≡1 mod 4, p≤6000, C≤150), 2531 of 4184 (60.5%) have subgroup∋−1 (multiplicity type); the rest (39.5%) have a −1-free subgroup (Galois type). Matches the repo's 61/39 split up to 2 extra failures in my count.
* Z1478: relaxation (−1 ∈ span of prime classes mod squares) is necessary (0 wins without it); holds for 16,736 pairs, of which 1,522 win (9.1%).
* Z1581: p=409 has no C-form witness for C≤2000; controls 401 and 433 win at C∈{1,4,17} and {2,8,11}. Failing C with all prime factors QR mod 409: 936 of 2000; the rest have a QNR factor. No single Legendre reason dominates.
* Z3151 / Z1075: over p≡1 mod 4, p≤6000 with a witness at C≤150: min Omega(d)=1 for 373 primes, 2 for 7, none needs 3; least winning C ≤40 (max at p=4789). 409, 577, 5569 have no witness at C≤150.
* Z2655: h(−4n) vs number of genera: n=105 idoneal (8=8); 2961 (48 vs 8), 3985 (24 vs 4), 25305 (80 vs 16), 111969 (240 vs 16), 978145 (424 vs 8) not idoneal.
* Z0857 (isosceles): checked for p<3000; a short proof (2/a+1/b=4/p ⇒ (4a−2p) | 2p²-type factorisation, odd-prime divisor analysis) gives no solution for p≡1 mod 4; already in fingerprint-0229.

## Items of note marked needs-compute (first real tests to run in a depth or follow-up lane)
* Z1596 (ω≥6 failures, stabiliser test): scan p≤1e5, C≤200.
* Z1729, Z1964, Z2618, Z2652, Z2677, Z2678 (graph/spectral computations on C-form, solution and forest graphs).
* Z1521 (do Type I certificates with d∈{1,2,3} cover all p≤1e7?) and Z1573 (census extension with OEIS check).
* Z1628 (residue table for p+u at p=409 vs controls); Z1945 (first-term offset k*(p)).

## Notes
* Several "covered" calls rely on keyword and file-level grep (e.g. FRIEZE_ES.md, LORENZINI_W.md, fingerprint memos) rather than a full read of each cited section; each covered outcome names the file.
* Z2651 (sandpile fan) is recorded as skipped: det M = p and (M⁻¹)₁₁ = (tu−1)/p are checked by hand, so the pairing reformulation is a restatement of ES₅.
* Z0706 lemma (4∤n ⇒ n | lcm of every solution) is PROVED by a parity/valuation argument; recorded as nothing because it does not bear on ES.
