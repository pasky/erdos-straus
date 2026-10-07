# AGENT_REPORT_O91 — consolidation after the 2026-10-07 round

Branch `side-agent/consolidate-oct7`. No new mathematics; no label changed. ES is not solved.

1. **verify.py (eb), (ec)** (commit "verify.py: blocks (eb) …").
   * (eb) POINTWISE_TYPEI4, from the R89 scripts: `review_typei4_jsearch.c` (complete engine, gcc) on
     L = 7..22 with b ≤ 1, and L = 7..10 with b ≤ 3 (≈ 20 s). It finds exactly the (L,b) pattern and the F values of Comp 3.4:
     18 fibre certificates, none at L = 7..10, 12, 15, 17. `review_typei4_verify.py` re-checks them with big integers: 0 bad, 0 at x̂_9.
     Inline checks on every hit: Prop 1.2 (Pell form, shapes, P₁Q₁ = M, (1.1), converse reconstruction), Cor 1.4 (1.2), Remark 1.6, Lemma 3.1(iii).
     Also: the R89 brute force from the definition (`review_typei4_identities.py 45 14`); example (42,32,71) via
     `typei3_verify.check` (certificate at w = 185, not at w = 9); Prop 4.1 (every hit, every split α+2γ = L,
     is a certificate at w := −F mod 2^t ≡ 9 (16), and not at w = 9; levels {11,13,14,16,18,…,22});
     Lemma 3.6 (sympy: (3.1) = u·(3.2), quadratic, resultant C; R89 script). For j = 1 there is no odd root m for any b < 30, odd a ≤ b, λ ∈ {2,4}. A direct
     search of (3.1) at j = 1 for b ≤ 5 is also empty.
   * (ec) EXCEPTIONAL_WEIGHTS2: R90 `review_weights2_slices.py 3000 100000` checks QNR for ℓ ≤ 3000, Jacobi for M ≤ 300, and
     the mass table at Y = 10²..10⁵ (exact strings). Inline (sympy, from the (u,v) definition): 3239 classes QNR
     for ℓ ≤ 2000, Jacobi −1 on the 43 composite M ≡ 3 (4) ≤ 300, and S(Y)/(log Y)² = 0.1308, 0.1258, 0.1237, 0.1224.
   * Full run: `ulimit -v 8000000; OMP_NUM_THREADS=2 OPENBLAS_NUM_THREADS=2 timeout 2400 uv run --with scipy
     --with mpmath python verify.py` → **all checks passed** (EXIT 0, no block skipped; ≈ 7.5 min; (eb) 26.9 s, (ec) 0.5 s).
     STATUS Housekeeping bullet added.
2. **STATUS.md** refresh 4 (ledger through (D)30): short-interval theorem ((D)30) under "Best proved bound";
   (W) follow-up (WEIGHTS2) under "Open"; TYPEI4 (Pell form, any-height bound, scope, L = 7 tower) under finite
   coverings. **CAMPAIGN_SUMMARY.md**: header; §1; §2.4 (W) paragraph; new §2.5 (EXCEPTIONAL_SHORT); §3.3
   TYPEI4 follow-up 3; table rows E27 (WEIGHTS2), E28 (SHORT), P50 (TYPEI4); §5 not-audited list; §6 items 2, 6;
   §7 reading guide.
3. **paper/es-coverings-note.tex**: new §4.6 placed after "Low 2-adic levels". It cannot go directly after the f-graded
   Computation 4.7 because it uses Prop 4.10 (levels ≥ 7). It contains Prop 4.12 (Pell form, PROVED, with a proof sketch
   and pointer), the Lemma 3.1 bounds in the text, Computation 4.13 (the CERTIFIED any-height bound, with the per-range scope of the two engines), Remark 4.14
   (scope / example (42,32,71); the falsity statement is CERTIFIED, the "mod 16 arguments" sentence is an Assessment), and a paragraph on Lemma 3.6 (PROVED partial; j ≥ 2 and 7 | j open; LFL
   Assessment). The level-7 sentence of §4.5, the Results bullet, Problem 2, the provenance line and bibitem PT4 were also updated.
   It compiles twice cleanly (22 pp): no undefined references and no overfull boxes. One pre-existing underfull box is in the r = 17 section,
   and the 15 hyperref "Token not allowed" warnings are pre-existing. The referee-file line was added.

Open for the parent: the new §4.6 has not been re-refereed (as noted in the referee file).
