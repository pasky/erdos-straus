# AGENT REPORT O90 — CRT alignment for (W)

Branch `side-agent/crt-alignment-w`. Deliverable: `EXCEPTIONAL_WEIGHTS2.md`, `scripts/weights2_checks.py`,
`data/weights2/checks.txt`. Not reviewed yet. No θ > 3/4 claimed; ES not solved.

**Outcome: (W) neither proved nor refuted; the CRT-alignment plan as specified provably fails.**

| item | statement | label |
|---|---|---|
| Lemma 1.1 | (W_{𝔉_A}) ⟺ (W) for the single maximal family 𝔊_max(N); refuting it with 𝔊 ⊇ 𝔊_X = a θ>3/4 theorem for E_pr | PROVED |
| Lemmas 2.1–2.2 | windows are forced to pay the density only for subfamilies of period ≤ N; that mass is (log N)^{o(1)} | PROVED |
| Prop 3.1, Cor 3.2 | prime slices ℓ ≤ Y give dens ≤ exp(−c(log Y)²) (BV, ineffective); so step (2): YES, density < e^{−(log N)^{3/4+2ε}} from Y = exp((log N)^{3/8+ε}) — but not forced, M ≫ N·dens·N^{100} | PROVED |
| Prop 4.1, Cor 4.2 | random shifts uniform on a prime set L give E count ≤ NΠ_L(1−p_ℓ): step (1) loses e^{−c(log N)²}; a proof of (W) must align almost all medium primes jointly | PROVED |
| Prop 4.3 | size-biased bound = Fejér sum of r(h); r(h)/dens = e^{O(self-overlap mass)} | formula PROVED; size Assessment + EVIDENCE |
| Lemma 5.1, Prop 5.2 | prime slices: M(N) = largest F-admissible subset of an N-interval (growing-dimension Hensley–Richards); bounded dimension: max ≍ density | PROVED |
| Prop 5.3 | all ℛ(ℓ) ⊆ QNR; quadratic alignment caps at √(N log N) | PROVED |
| §6 | mass/(log Y)² ≈ 0.12 to Y = 3·10⁶; self-overlap ≈ 10% of mass; 0 QNR failures | EVIDENCE |

Points for the reviewer: the BV-with-2^{ω(q)} weights step in Prop 3.1 (sketched, standard);
the exchange argument in Lemma 2.2; the Assessment in Prop 4.3 (overlap mass bound not proved).
Open: an attainment/inverse theorem for the growing-dimension large sieve (would prove (W));
any shift-uniform bound below the sieve limit (would refute it).
