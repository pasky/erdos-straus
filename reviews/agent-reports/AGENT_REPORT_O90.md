# AGENT REPORT O90 — CRT alignment for (W)

Branch `side-agent/crt-alignment-w`. Deliverable: `EXCEPTIONAL_WEIGHTS2.md`, `scripts/weights2_checks.py`,
`data/weights2/checks.txt`. Not reviewed yet. No θ > 3/4 claimed; ES not solved.

**Outcome: (W) neither proved nor refuted; the CRT-alignment plan as specified provably fails.**

| item | statement | label |
|---|---|---|
| Lemma 1.1, 1.2 | (W_{𝔉_A}) ⟺ (W) for the single maximal family 𝔊_max(N). (R90 repair, D1/D2:) only a bound M_𝔊 ≤ Ne^{−(log N)^θ}, θ>3/4, for all large N and a prime-forced 𝔊 ⊇ 𝔊_X gives θ>3/4 for E_pr; a bare refutation of (W) gives an ω(N)→∞ gain along a subsequence; via 𝔊_max (selector classes 0 mod p) no E_pr bound at all | PROVED |
| Lemmas 2.1–2.3 | windows are forced to pay the density only for subfamilies of period ≤ N (Lemma 2.1 gives "if"); cost (log N)^{o(1)} for prime slices (2.2); (R90 repair, D3:) ≪ log N/log log N for composite ℛ/selector subfamilies via Jacobi symbol −1 and unit squares (2.3); (log N)^{o(1)} for all of 𝔉_A is CONJECTURE; Case-A not covered | PROVED / CONJECTURE |
| Prop 3.1, Cor 3.2 | prime slices ℓ ≤ Y give dens ≤ exp(−c(log Y)²) (BV, ineffective); so step (2): YES, density < e^{−(log N)^{3/4+2ε}} from Y = exp((log N)^{3/8+ε}) — but not forced, M ≫ N·dens·N^{100} | PROVED |
| Prop 4.1, Cor 4.2 | random shifts uniform on a prime set L give E count ≤ NΠ_L(1−p_ℓ): step (1) loses e^{−c(log N)²}; a proof of (W) must align the primes carrying all but O((log N)^{3/4}) of the medium mass jointly (R90 repair, D7) | PROVED |
| Prop 4.3 | size-biased bound = Fejér sum of r(h); r(h)/dens = e^{O(self-overlap mass)} | formula PROVED; size Assessment + EVIDENCE |
| Lemma 5.1, Prop 5.2 | prime slices: M(N) = largest F-admissible subset of an N-interval (growing-dimension Hensley–Richards); bounded dimension: max ≍ density. (R90 repair, D10:) "(W) is precisely attainment" holds only for prime slices at their own exponent; the 2/3 limit is Assessment | PROVED |
| Prop 5.3 | all ℛ(ℓ) ⊆ QNR; quadratic alignment caps at √(N log N) | PROVED |
| §6 | mass/(log Y)² ≈ 0.12 to Y = 3·10⁶; self-overlap ≈ 10% of mass; 0 QNR failures | EVIDENCE |

Points for the reviewer: the BV-with-2^{ω(q)} weights step in Prop 3.1 (sketched, standard);
the exchange argument in Lemma 2.2; the Assessment in Prop 4.3 (overlap mass bound not proved).
Open: an attainment/inverse theorem for the growing-dimension large sieve (would prove (W));
any shift-uniform bound below the sieve limit (would refute it).
