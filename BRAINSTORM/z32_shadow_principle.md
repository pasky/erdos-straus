# z32 memo 2: the n = 1 shadow kills any finite slice set (O262; DISPROOF_AVENUES §3 Prop 3.1)

Labels as in DISCOVERIES.md. ES is not solved.

**Statement (PROVED; existence of such p CONDITIONAL on Dickson, on H if Type I {c,d} rows are used).** For any
finite set Θ of ET slices (six pair rows per type and the e-slices of both types), if p ≡ 1 (mod Q) with
q_θ N_θ(1) | Q and every cofactor N_θ(p)/N_θ(1) is prime, then all slices in Θ are empty. Reason: every divisor
of N_θ(p) is congruent mod q_θ to a divisor of N_θ(1), and at "p = 1" every class condition fails for size reasons
(4/1 = 1/x + 1/y + 1/z has no positive solution: n = 1 is an exceptional point — BM-obstructed in BL's sense, R274 repair). Q must also satisfy e(1+e) | Q for e-slices (R274).

**What it unifies.** (J)83 Thm 1.3 (windows ≤ M), (J)90 Thm 4.2 (b = 1 shifts ≤ σ), redteam-automorphic-2
Lemma 1.2.1, B1_LINE "T1 point 1"; POINTWISE_SIZE Thm C is the quadratic-character twin (n = m² instead of n = 1).

**Check (EVIDENCE, `scripts/z32_shadow_check.py`).** Q = 9240, nine slices: three primes near 2·10¹² have 0
solutions in all nine slices; random controls have 0–60.

**Barrier screen.** This is B1/B2 from the adversary's side: a finite Θ is killable; a growing Θ(p) costs
k ≲ log p/log log p prime conditions (Bateman–Horn) and kills only an O(log L/L) share (memo 3).

**Viability (Assessment).** Clean as an obstruction statement, useless as a disproof: the killed share → 0.
Promise for disproof 0/5; value as a unifying lemma 2/5 (novelty only in uniform form).
