# Hostile review of POINTWISE_OMEGA4.md (branch side-agent/omega-rate @ 5d19b4f)

Reviewer: side agent (worktree 0007). Subject files brought in via
`git checkout 5d19b4f -- POINTWISE_OMEGA4.md reviews/agent-reports/AGENT_REPORT_O6.md scripts data`.
Verdicts: SOUND / SOUND-AFTER-REPAIRS / DEFECTIVE. Defects numbered D1, D2, …

(in progress — items are appended one at a time)

## Item 1 — Theorem 1.1 (explicit k-level constants). Verdict: **SOUND** (one cosmetic defect, D1)

Re-derived every inequality of Steps 1–4 against O3 Thm 5.1 as written
(O3 lines 547–676):

* constants: `1+w'=17e^{1/2}`, `δ_r=[4er(1+w')^r]^{−1}` decreasing in r so
  `δ_*=δ_k`; `β_k=8k2^k/δ_k=32e·k²(34e^{1/2})^k`; `log(34e^{1/2})=4.026`,
  `b_k=2logβ_k+log3k ≤ 8.054k+5log k+10.04`. ✔
* `Λ_r=(Σ_r+H_r+1)/(2δ_r)` matches O3's `2er(1+w')^r(Σ_r+H_r+1)`. ✔
* Ẑ monotone: `Ẑ_{r−1}−Ẑ_r = 2Σ_{r−1}+1−Σ_r+k(L_r+1)+Λ_r ≥ Λ_r−Σ_r ≥ 0`. ✔
* `(L_r+1)log4 ≤ log(800k)+k log4+Σ_{t>r}Λ_t+H_r/2+Λ_r+3Ŝ_{≥r} ≤ Ẑ_r/δ_r`;
  `4N_r ≤ 8kẐ_r/δ_*`. ✔
* Markov push: `Σ_{|O|=j}P(O)Δ_O=binom(r,j)Σ_r` and the per-prime analogue
  `binom(r−1,j−1)w_ℓ^{(r)}`; thresholds `δ_r/2` (j=1) and
  `δ_r(4N_r)^{−(j−1)}/(2r)` (j≥2) give `≤(β_kẐ_r)^j`, resp.
  `β_k^jẐ_r^{j−1}w_ℓ`. ✔
* `Ẑ_{r−1} ≤ Ẑ_r(1+(k+1)/δ_*)+2Σ_{r−1}+1` (exact expansion). ✔
  `z_{r−1}≤(r−1)z_r` ⟺ `(r−3)(logβ_k+log3k)≥0`. ✔ `Ẑ_k≤3Ŝ+k+1`. ✔
  `z_2 ≤ (k−1)!z_k`, so `logẐ_2 ≤ A_k−b_k`. ✔
* Step 3: `S_1^{new}≤(1+2e^{50})Ẑ_2`, `Λ_2≤17e^{98}Ẑ_2`,
  `Ŝ_tot≤4e^{50}Ẑ_2`, `L_2+1≤e^{101}Ẑ_2`, `K≤18e^{98}Ẑ_2`,
  #primes `≤H_2+2(L_2+1)≤e^{102}Ẑ_2`. ✔ (O3's own prime count is
  `Σ_r k(L_r+1)`; the O4 version `Σ s(L_s+1)+2(L_2+1)` is ≤ it and is the
  correct count; either is `≤e^{102}Ẑ_2`.)
* Step 4: `m^{(r)}≤m^{(r+1)}(1+β^{r−1}Ẑ_r^{r−2})`, the telescoping
  `Σ_{r≥3}(r−2)/(r−1)!=1`, and the final
  `e^{51}k·e^{k+A}·k^{−2}e^{−56−2A} = e^{−5+k−A}/k ≤ e^{−5}/k < 1/(64k)`
  (using `A_k≥b_k≥8k≥k`). ✔

**D1 (cosmetic, repaired in place).** Level 2 holds singles *and* edges,
but Step 2 writes `Σ_{r−1} ≤ Ŝ+Σ_{s≥r}(β_kẐ_s)^{r−1}` also for `r−1=2`,
omitting the singles pushed (j=1) from every level `s≥3` (and Step 4
likewise omits the j=1 per-prime term at level 2). Repair: Markov gives
for j=1 plus j=2 together a mass `≤(binom(r,1)+binom(r,2))·(2k/δ_*)(8kẐ_r/δ_*)Ẑ_r
≤ 2^k(2k/δ_*)(8k/δ_*)Ẑ_r² ≤ (β_kẐ_r)²` since `binom(r,1)+binom(r,2)<2^r≤2^k`
(the `2^k` in β_k was a bound for a *single* binomial). Same for the
per-prime term. So the displayed inequalities hold verbatim once the
bound is read as "mass pushed into level j" rather than "into size j".
No constant changes.

The script `omega4_rates.py recursion` was re-run: output identical to
`data/omega4/recursion.txt`, all bounds OK (it implements the same
worst-case recursion, so it is a consistency check, not independent
evidence).
