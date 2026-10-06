# AGENT_REPORT_O83 — sterility at r = 17 (checkpoint 1)

Branch `side-agent/sterility-r17` (it merges `side-agent/mordell-13` and `side-agent/sign-point-sterility`,
as instructed; their claims are still unreviewed). Main file: `POINTWISE_MORDELL17.md`.
Scripts: `scripts/m17_enum.c`, `scripts/m17_union.py`, `scripts/m17_validate.py`.

## Outcome
The goal was to prove that the cell `C_5 = {x_17 ≡ 5 (17)}` (17-generic points) contains a sterile
point. I did **not** prove it. Instead there is a precise reduction (Theorem 4.1), exact data
through level 5, and an identification of the obstruction. ES is not solved, and nothing here
claims it.

| item | content | label |
|---|---|---|
| Lemma 1.1 | At T={17} the seven ET families give only four box types: P (=I1, I3 with 17∣cd, II3 with 17∣ad), Q (=II2, II3 with 17∣e), Q⁻¹ (=I2 with 17∣f), √Q (=I3 with 17∣f), U (=II1, I2 with 17∣ac), U⁻¹ (=I4). P∪Q∪Q⁻¹∪U∪U⁻¹ is closed under inversion, so C_5 ↔ C_7 | PROVED (elementary; uses the T-generic table of POINTWISE_MORDELL §2.1) |
| Lemmas 2.1–2.3 | Q-boxes of level k ↔ N-points of ET's Σ^I_{17^k}; U-boxes ↔ ES solutions `(iab,iac,ibc)` of 4/17^k; P-boxes ↔ N-points of Σ^II_{17^K} at **half level** ⌈K/2⌉ (nested in α). No level-0 boxes. Even levels: Q and P are empty (ET Prop 1.6) | PROVED |
| §2 consequence | `μ(⋃boxes) ≤ Σ 6f(17^k)17^{−k} + Σ f_II(17^K)17^{−⌈K/2⌉}`. This converges by ET Prop 1.7, but the bound is ineffective | PROVED (ineffective) |
| Comp. 3.1 | Exact union of all boxes of level ≤5 (Q,U for k≤5, P for K≤9). Covered: 0.2353, 0.3149, 0.3218, **0.3228** of each cell after levels 2–5. **67.72% of C_5 and of C_7 is uncovered.** u=5 and u=7 lie in no box of level ≤5 and in no Q/U box of level 7 | CERTIFIED (one engine). Soundness: 1152 rebuilt genuine classes. Completeness: it contains all brute-force boxes with M≤10⁵ |
| Thm 4.1 | If `Σ_{k≥6} 17^{1−k}B_k < 0.677207`, with `B_k = 8D_Q(k)+2D_U(k)+2D_P(2k−1)`, then C_5 (and C_7) contains a sterile point. Corollary 4.2 then rules out any finite polynomial-identity covering of the Mordell-hard primes with n_p=17 | PROVED reduction |
| §4 obstruction | **The critical family is P.** Its weight is N^{−1/2}, against ET's f_II ≪ N^{2/5+o(1)}, a margin of 1/10. Even with constant 1, the tail from K=11 is ≈0.84 > 0.677. Q and U are comfortable (margin 2/5). Elementary effective counts (Lenstra's ≤11 divisors in a residue class; explicit divisor bounds) fail, for the reasons given | precise negative statement |
| Empirics | D_P = 2, 32, 121, 258, 604 (K = 1,…,9 odd); D_Q = 2, 73, 245, 707; D_U = 4, 68, 310, 826 (k = 1,…,7 odd). Growth looks polylogarithmic. `D_Q+D_U ≤ 17^{k/2}` (k≥8) together with `D_P(K) ≤ 17^{K/4}` (K≥11) would already give a tail below 0.01 | EVIDENCE |

## Other answers to the brief
* **Corrections to POINTWISE_MORDELL §5.** Level-2 boxes in C_5 do exist (4 of them, all P with K=3; e.g. 56 mod 289). Their moduli exceed 10⁵, which is why the earlier brute-force run did not see them. The rigid II-only count (13 of 289 at level 3, 4.5%) badly underestimates coverage: with all families, 31.5% is covered after level 3. Comp. 5.1 (u=5 in no class with M≤10⁶) is consistent with this.
* **Decidability of x̃ (u=5).** This does not reduce to a finite check. Every ET class meeting the 17-generic line is periodic in k (`17^k mod M`), so its boxes are nested around one center: an integer (−4a²d, −e, −f), the inverse of one, or a quadratic irrationality. There are infinitely many classes, though, and their centers have height up to about 17^{2k} at level k. So Strassmann-type finiteness does not apply, and Liouville or Ridout separation would need center heights below 17^{k/2}. That fails for Q and P (f can be as large as about 17^K).
* **Novelty.** The obstruction is not square-mimicking, so Theorem C does not explain it (POINTWISE_MORDELL §4). ET §1 (after Prop 1.6) notes that covering strategies fail at odd squares, and Salez filters a single prime. The ES-solutions-at-prime-powers description of the T-generic boxes (Lemmas 2.1–2.3) does not appear in POINTWISE_MORDELL, and I don't know of it in the literature. I have not done a literature search beyond ET.

## Requests / next steps (parent decides)
1. A hostile review of Lemma 1.1 and Lemmas 2.1–2.3. Lemma 1.1 inherits the unreviewed §2.1 table.
2. Possible extensions:
   * P at K=11 (level 6) needs ET's N^{2/5}-type algorithm with factoring; my O(N) scan is infeasible there.
   * Q and U at k=9 take about 5 h each with the current code.
   * None of these would close the tail. Only an explicit bound for f_II(17^K) would.
3. Optional: the same machinery applies to r=13 at T={11,13}, where the boxes become ES solutions with n = 11^α13^β.

## Replay
See POINTWISE_MORDELL17.md, section "Replay". All runs take at most about 8 minutes on one core.

---

# Checkpoint 2 (round 2: the tail) — POINTWISE_MORDELL17 §5–6

| item | content | label |
|---|---|---|
| Lemma 5.1 | In-cell Q- and P-boxes are balls centred at the rational `−a/b` of their ES point: Q via `4abd≡1 (17^k)`, P via `bf=Nc+a`. Hence **Q⁻¹ = Q** (the reflection `a↔b`), so the I2 boxes duplicate the II2 boxes | PROVED |
| Lemma 5.2 | **U-boxes are never new.** Every in-cell U-box (II1/I4, and I2 with 17∣ac) lies inside a P-box of strictly lower level with the same centre. α>β reduces to a Type II point of `4/17^{α−β}`; α=β is impossible. Also proves that U is empty at even levels | PROVED |
| (a) nesting | New boxes per level in C_5: 4, 23, 34, 83 (levels 2–5), 94 Q-only at level 7. That is about ½ of all boxes: a constant factor, the same exponent. New = first admissible K for a centre, and first occurrences are not provably rarer | EVIDENCE + remark |
| (b) prime powers | A P-point with a≤b is determined by (a,b): `e = (−17^K mod 4ab)` must divide a+b. In-cell data are all primitive (17∤ab, and 17∤abcd for Q). Scaled points (17∣a,b) are not P-data and have centre ≡1. So the P-tail is exactly a **small-residue problem**: `#{(a,b): ab≤17^K, (−17^K mod 4ab) ∣ a+b} ≤ C·17^{(1/2−δ)K}` with explicit C. Elementary counting, Lenstra and CHN give only O(N), because there are ≍N pairs and the bounds are per pair. ET gives `N^{2/5+o(1)}`, which is ineffective. Heuristically the count is ≍ log³ | precise obstruction |
| digit/Cantor test | A digit-restricted u, with 1/u also restricted, would avoid every box with a small integer centre. The construction is feasible, since the new digit of 1/u is an affine function of the new digit of u with slope 2. But the boxes are only mildly biased: `t = min(z_r, z_{1/r})/17^k` has median 0.15–0.2 and maximum 0.87–0.99. So no fixed threshold works | EVIDENCE (negative) |
| (c) cutoff | Not raised. Theorem 4.1 needs a bound for every K, so more exact levels cannot close the tail on their own. P at K=11 would need an N^{2/5} factoring-based enumerator | decision |

**Bottom line.** The tail is not closed. Sterility of C_5 is reduced, exactly, to an explicit
bound of θ<1/2 type on small residues of `17^K` modulo `4ab`, i.e. on primitive Type II solutions
of `4/17^K`. I recommend recording Theorem 4.1 plus the conjecture (EVIDENCE: 67.7% of each cell
uncovered through level 5). The new proved facts (Q⁻¹=Q, U never new) simplify the box picture to
**two families: P (critical) and Q**.
