# s8_perj_lottery — per-j failure, cross-j correlation, privacy of large primes (O258; §2)

**Idea.** Model the per-j failure of F_j: "jp + 1 has a divisor w ≡ −1 (mod 4j), w ≥ 3" and its correlation across j. Is there
a deterministic mechanism (Chebotarev, reciprocity, pigeonhole across j) forcing one j?
**Literature.** CAP_BOUNDED Lemma 1.1 (Jacobi transfer); FORCED_WINDOW Lemma 1.1; Burgess and Ankeny for least non-residues.
**Barrier screen.** Lemma 2.3 (PROVED): gcd(jp + 1, j′p + 1) | j − j′, so large primes are private to one j. Cross-j pigeonhole
sees only primes ≤ J, i.e. congruences (B1, T1-blind). Chebotarev on prime w: p ≡ −4d (mod w) for d | (w + 1)/4 are
independent CRT events whose complement has Haar measure 0 but contains every square (B1/T1). Reciprocity (Lemma 2.2) gives
the parity (w/p) = −1 and "forced levels" = non-residues d, never the class.
**Cheap numerics.** `s8_lines perj 1e6 24`: failure 0.128 (j = 1), 0.389, 0.474, 0.523, …, 0.907 (j = 24). Joint/product ratio
mean 1.004 (max 1.27). All 24 j fail at 10 primes against 6.6 predicted by independence. Odd j ≥ 3: prime support impossible
(rate 1.000), as 2.1 predicts.
**Assessment.** PROVED (Lemmas 2.2, 2.3) + EVIDENCE. No deterministic mechanism; the across-j route is void.
