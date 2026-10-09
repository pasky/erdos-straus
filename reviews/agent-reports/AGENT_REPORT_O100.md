# AGENT REPORT O100 (branch side-agent/r13-cover-all) — checkpoint 1

Deliverable: POINTWISE_MORDELL13C.md, data/mordell13c/tree6_6000.json.gz, scripts/m13c_*.

1. **Theorem 6.1 (PROVED by finite computation, two independent checkers).** Thm 3.1(b)'s six exceptional
   classes mod 720720 are refined by an adaptive tree certificate (136494 covered leaves, 2140 ET classes);
   ES holds for every prime with (p/13)=−1 outside 35459 explicit classes of total density 8.42e-5 of the six
   classes (≈2.3e-7 of the Mordell-hard (p/13)=−1 residues). Checkers: `m13c_check.py` (sympy engine of
   mordell_check) and `m13c_review_tree.py` (R80 engine review_mordell_check); negative controls fail as they should.
   **No class is removed**; every root keeps open leaves. Honest scope: adaptive Salez/ET level sieve.
2. Complete fixed-level witness engine `m13c_witness.py` (all classes with M | L, no size cap; validated vs brute
   force, 0 mismatches at L = 9240, 10920, 65520). At L = 6.96e10: 1399 survivors vs 1412 at M ≤ 1e8 —
   the modulus cap is not the bottleneck.
3. T-generic picture: {3,11,13}- and {7,11,13}-generic points are covered except in the (2,2) cell (k=2, M≤1e6).
   So only class 473761 has known uncovered T-generic points; the other five have no simple sterile candidate,
   yet the DFS does not close (open mass decays like a power of the node count).
4. x** = x(2,15): no I2/II1/I4 class with f,e ≤ 2e8 (was 2e7); T-exponent cap shown vacuous.
   II3 to 1e10 is NOT feasible in 6 h with the current engine (≈150 core-min per 1e9 of e, sieve 1 byte·e);
   a run (1e9, 2e9] is in progress (logs/o100_xss_PQ_1e9_2e9.log).
5. In progress: ES enumeration of 4/N for N = 11⁴13⁴ (the only ES level missing to make 13B's k=2 coverage of the
   (2,2) cell complete; /tmp/o100/run, logs/o100_es_11e4_13e4.log).

Not achieved: zero exceptions, or a proved sterile point. Next steps proposed: locate limit points of the open
leaves in the five non-(2,2) classes (418321 is smallest: open leaves ≡1 (17), three values at each of 19, 23, 31)
and test them with the targeted engines generalised to S-generic points.
