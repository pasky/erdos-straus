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

## Item 2 — Construction 2.0 / Theorem 2.1 (y = 2T^{1/(k+1)}). Verdict: **SOUND**

The brief asked to check the replacement of O3's
`y=T^{1/k}exp(2𝓛/log𝓛)` by `y=2T^{1/(k+1)}` carefully. I traced every use
of y in the chain O2 Lemma 4.3 → O3 Lemma 4.2 → O3 Thm 5.1/5.2:

* **Where the exp factor was used.** In O2 §4 (θ=1/3) it is used *only*
  in (W) (`T/y³=exp(−6𝓛/log𝓛)`) and (G) (the 𝓑-term). O3 Lemma 4.2
  replaced (W),(G) by the Lemma 11.2 per-prime bound, and its four items
  are (I), per-prime `≤c`, total mass `≤S*`, `log Q`. In O3 Thm 5.2 the
  factor only guarantees `y^k>T` (support `≤k−1`) and is harmless there
  because K is anyway `exp(O_k(𝓛/log𝓛))`. Nothing in O3 Thm 5.1 refers
  to y at all. So the factor is indeed dead weight once Lemma 11.2 is in
  place. ✔
* **(I).** O2 Lemma 4.3 (I)'s proof uses only: `ℓ^v‖M, ℓ∈Π ⇒ ℓ^v≤T`, so
  `m_Π(M)|Q`; and that every surviving atom's event lives on free primes,
  i.e. every prime of `r_Π(M)` lies in `𝒫`. The latter needs
  `Π⊇{ℓ≤y}` and `𝒫={y<ℓ≤T}∖𝓑`, both true. Replacing Q by `Qℓ_0`
  (ℓ_0>T, so coprime to all d_i and to Q) only shrinks the class. ✔
* **Supports ≤ k.** All prime factors of `r_Π(M)` exceed y, `r≤M≤T`, and
  `y^{k+1}=2^{k+1}T>T`, so `Ω(r)≤k`; the number of *distinct* primes (the
  support) is `≤Ω(r)≤k`. Prime-square rough parts (`ℓ²|r`, possible since
  `y<√T`) are lifted to classes mod `ℓ^{e_ℓ}` as in O2 §10.3 remark; this
  was already the case in O3 §4 (k=4: `y≈T^{1/4}`, `r=ℓ²ℓ'` possible) and
  in O3 Thm 5.2, so no new structure arises. Every vertex is a unit class
  mod `ℓ^{e_ℓ}` at distinct primes, as O3 Setting 5.0 requires. ✔
* **Lemma 11.2 count.** `log y>𝓛/(k+1)` gives `⌊𝓛/log y⌋≤k`, so
  `|𝓑|≤kS*/c`. ✔ Per-prime: `w_ℓ(Π)` is the mass of *distinct* events
  through ℓ, which dominates O3's per-prime total; merging/lifting do not
  increase it (O3 Lemma 4.2 bullet 2). ✔ Total mass `S_tot(Π)≤S*<Ŝ`. ✔
* **Sizes.** `π(y)𝓛≤1.26(k+1)y` (RS `π(y)<1.25506y/log y`;
  `𝓛<(k+1)log y`). `k³Ŝ≤e^{2A}` since `A≥(k−1)!b_k≥8k` and
  `A≥log(3Ŝ)`. `log Z ≤ log Q+log 2R+log max d_i ≤ 2.52(k+1)T^{1/(k+1)}
  +e^{104+4A}𝓛` ✔, and `max(log Z,K)` is ≤ the bracket since
  `K≤e^{102+A}`. ✔
* **The two inequalities.** First term `≤T^{1/k}/2` ⟺
  `A+log(5.04C_1e^{102}(k+1)) ≤ 𝓛/(k(k+1))`; from (C) since
  `𝓛/(k(k+1))≥𝓛/(2k²)≥3(A+log C_2𝓛)` and `C_2𝓛≥5.04C_1e^{102}(k+1)`. Second
  `⟺ 5A+log(2C_1e^{206}𝓛)≤𝓛/k`; from (C) since `𝓛/k≥6k·𝓛/(6k²)≥18(A+log C_2𝓛)`. ✔
* **PO Thm 4.1 range.** Thm 4.1 is stated in terms of
  `log x ≥ C_1K·max(log Z,K)`; the TZ range `x≥Z^{12}≥q_i^{12}` is
  absorbed into C_1 (PO §4 Setup), so no extra condition arises. The
  twist step (O3 Thm 5.1 last bullet / O2 Thm 10.3 step 4) costs
  `(1−O(1/k))^{k−1}`-type factors bounded uniformly in k under (P_k). ✔
* `p>ℓ_0>T`, `840|Q` (y≥7 is forced by (C)), `(log p)^k≤T<W(p)`. ✔

Remark (not a defect): with `y=2T^{1/(k+1)}` the support is k (not k−1 as
in O3), so Thm 2.1's k corresponds to O3's k+1 in the support count; the
final exponent `log p≤T^{1/k}` is the same as O3's up to the
`T^{o(1)}` factor, which is exactly what lets k grow.
