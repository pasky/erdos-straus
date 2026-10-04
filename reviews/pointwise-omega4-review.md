# Hostile review of POINTWISE_OMEGA4.md (branch side-agent/omega-rate @ 5d19b4f)

Reviewer: side agent (worktree 0007). Subject files brought in via
`git checkout 5d19b4f -- POINTWISE_OMEGA4.md reviews/agent-reports/AGENT_REPORT_O6.md scripts data`.
Verdicts: SOUND / SOUND-AFTER-REPAIRS / DEFECTIVE. Defects numbered D1, D2, …

## Summary

| Item | Claim | Verdict |
|---|---|---|
| 1 | Thm 1.1 explicit k-level constants, Ẑ_r recursion, per-prime `e^{k+A_k}` | **SOUND** (D1 cosmetic, repaired in place) |
| 2 | Construction 2.0 / Thm 2.1, `y=2T^{1/(k+1)}` | **SOUND** |
| 3 | Cor 3.1–3.3 rates, k=k(T), uniformity | **SOUND** (editorial D2 missing label, D3 τ* argument) |
| 4 | HC(a,B), Lemma 4.1, Thm 4.2 | **SOUND** as implication (D4 unverified `h_ℓ≤1/100`, holds with factor-2 margin; D5 EVIDENCE overstated) |
| 5 | §4.1 anatomy, §4.3–4.4 ceilings | **SOUND-AFTER-REPAIRS** (D6 PROVED label over EVIDENCE/heuristics; D7 "log p ≥ K" wording) |
| 6 | Prop 5.1 Haar side | **SOUND** (D8 gap-ratio arithmetic) |

No DEFECTIVE item. The specific worry in the brief — dropping O3's
`exp(2𝓛/log𝓛)` from y — is unfounded: that factor was used only for O2's
(W),(G), which Lemma 11.2 replaces; (I), supports `≤k`, the vertex
structure (distinct primes, classes mod `ℓ^{e_ℓ}`, prime-square rough
parts lifted as in O2 §10.3) and all size bounds survive (Item 2). All
constants are explicit or absolute, so k=k(T) is legitimate (Item 3).
Required before merge: D2, D4, D6, D7, D8 (all text-level); D1, D3, D5
recommended.

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

## Item 3 — Corollaries 3.1–3.3 (rates). Verdict: **SOUND** mathematically; editorial repairs D2, D3 required

* **Uniformity in k.** Every constant in the chain is explicit or
  absolute: Thm 1.1 (all k), `C_2=6C_1e^{206}` (absolute, from PO Thm 4.1),
  the twist/LLL factors (bounded uniformly under (P_k), see Item 2), the
  level-error telescoping (`k` levels × `P(all)/(100k)`). The only
  implicit constants are in the S* bounds (ET: absolute `≪`; Wigert:
  `o(1)` in `log 2+o(1)`), and these do not depend on k. So letting
  `k=k(T)` is legitimate; no hidden `O_k`. ✔
* **(C_{k,T}) rewritten.** `6k²(k−1)!=6k·k!`. ✔
* **Cor 3.1 (ET).** `S*≪𝓛^4log𝓛` gives `log(3S*+k+1)≤5log𝓛+O(1)` for
  `k≤𝓛`. `b_k≤9k+C` holds with `C=13.5` (max of `5log k−0.94k` is
  `<3.4`); the text's `10.1` is not enough at small k but only "C" is
  used. With `k=κ(𝓛)`: the slack `6k·k!(log𝓛−O(1))` dominates
  `6k²log(C_2𝓛)` since `k!≥2k` for `k≥3`. ✔ `κ(X)~log X/log log X`
  (`log k!~k log k`). ✔ Then `log₂p≤𝓛/k≤𝓛`, κ nondecreasing, so
  `log W>𝓛≥k·log₂p≥κ(log₂p)·log₂p`, giving `(1+o(1))log₂p·log₃p/log₄p`. ✔
  (κ(log₂p) is defined, i.e. `≥3`, once `log₂p≳10^4`; since `p>T` only
  gives `log₂p>log𝓛`, this needs `𝓛≥e^{10^4}`-ish — harmless for an
  i.o. statement.) Spot check: `κ(10^{10})=9` ✔ by hand.
* **Cor 3.2 (U).** `log S*≤(log2+o(1))𝓛/log𝓛` and `log 2=0.6931<0.7`, so
  `log(3S*+k+1)≤0.7𝓛/log𝓛` for large T ✔ (Nicolas–Robin makes Wigert
  explicit, so "effective" is fine). `4.2k·k!𝓛/log𝓛≤0.84𝓛` for
  `5k·k!≤log𝓛` ✔; the remainder `(log𝓛)^{O(1)}≤0.16𝓛` ✔.
  `κ_0(X)~log₂X/log₃X`, and at `X=log₂p` this is `log₄p/log₅p`. ✔
* **Cor 3.3.** `log log L_h(T) ≤ 𝓛/κ(𝓛) = (1+o(1))𝓛log₂𝓛/log𝓛`, resp.
  `𝓛log₃𝓛/log₂𝓛`. ✔ Comparison with O3 Thm 5.2 is fair.

**D2 (label; house rules).** Corollary 3.3 carries no status label. It
should read "PROVED modulo Thorner–Zaman and ET Prop. 1.4 (first form),
modulo Thorner–Zaman (second form); effective".

**D3 (cosmetic).** §3 bullet (U) writes `S*≤C log𝓛·𝓛³·τ*(T+2)`. O2
Lemma 11.1 sums `τ(4sr'²+1)` with `4sr'²+1≤4T+1`, so it should be
`τ*(4T+1)` (and `(3+𝓛)(1+𝓛)²` rather than `𝓛³`). No asymptotic effect:
`log τ*(4T+1)=(log2+o(1))𝓛/log𝓛` as well.

Remark: "effective" in Cor 3.1 presupposes ET Prop. 1.4's implied
constant is effective. ET's proof is elementary (divisor-sum / Type I
counting), so this is very likely, but the text should say "effective
provided ET Prop. 1.4 is" or cite the effectivity, as PO does not record
it either.

## Item 4 — Hypothesis HC(a,B), Lemma 4.1, Theorem 4.2. Verdict: **SOUND** (as a conditional implication); minor defects D4, D5

Checked step by step:

* **Pointwise validity with hub deletion.** HC is stated for the system
  *with H-hub events deleted*. This is legitimate: O3 Thm 1.1 gives
  `B≤1_{𝒜_1∩𝒜_2}` with `𝒜_1={X_ℓ∉𝓗_H(ℓ^{e_ℓ}) ∀ℓ}` and `𝒜_2` the void
  event of the *reduced* system; on `𝒜_1` no hub-containing event can
  occur, so `1_{𝒜_1∩𝒜_2}≤1[no event]≤1[W>T]` on `n≡1 (Q)` by (I). After
  deletion, sets O containing a hub have codegree 0, so HC (which only
  speaks of hub-free O) covers every set Lemma 10.2 needs. ✔
* **Step 1.** `|𝓑|≤kŜ/c=64k²·4ek17^k·e^{0.011k}Ŝ=e^{O(k)}Ŝ`. ✔ Per-prime
  under P′: `≤e^{0.011k}c=δ_k/(64k)`, which gives (G_k) and (W_k) of O2
  Thm 10.3. ✔
* **Step 2.** `(100/99)^k=e^{0.01005k}≤e^{0.011k}` ✔;
  `S_hub≤3H(1+log H)Σ_{y<ℓ≤T}1/(ℓ−1)≤3H(1+log H)(log(k+1)+1)` ✔.
* **Step 3.** From O2 Thm 10.3: `Λ′=17S_1^++2ek17^kS_H`,
  `S_1^+≤S_1+kS_H/δ_k`, `λ=3(S_1^++S_H)`, and `2ek17^k=1/(2δ_k)`; so
  `Λ′+λ≤(20k+½)Ŝ′/δ_k+23Ŝ′≤22kŜ′/δ_k` ✔, `L+1≤17kŜ′/δ_k` ✔. With
  `N≥k(L+1)`, the bound `Δ≤η_k=δ_k/(2N^{k−2})` gives
  `Σ_{j=1}^{k−2}N^jη_k≤δ_k`, i.e. (CD_k) in the form actually used in
  Thm 10.3 Step 3. ✔ Recomputed
  `log(1/η_k)=log(1/δ_k)+log2+(k−2)[log17+2log k+logŜ+0.011k+log(1/δ_k)]
  ≤(k−1)(logŜ+2.86k+3log k+6)` (per-factor constant 2.844k+5.22). ✔
* **Step 4 / Lemma 4.1.** O3 Cor 1.2 output, `J+1=O(S_hub+kŜ′/δ_k)=O(K)`,
  so primes per modulus `≤e^X` after the `O(1)`. `|𝓑|=e^{O(k)}𝓛^5≤e^X`
  since `X≍k²/a≫k+log𝓛`. `log Z≤2.52(k+1)T^{1/(k+1)}+3e^X𝓛+O(1)≤…+e^{X+2}𝓛`. ✔
* **Step 5.** `min_k(2.86k²/a+𝓛/k)` is at `k³=a𝓛/5.72` ✔; then
  `X=(0.5+o(1))(5.72/a)^{1/3}𝓛^{2/3}`, `𝓛/k=(1+o(1))(5.72/a)^{1/3}𝓛^{2/3}`,
  max is the first branch, `log₂p≤(1.5+o(1))(…)`; inverting,
  `𝓛≥(1−o(1))(a/5.72)^{1/2}1.5^{−3/2}(log₂p)^{3/2}`;
  `5.72^{−1/2}·1.5^{−3/2}=0.2276>0.2`. ✔ Lower-order terms
  (`(k/a)5log𝓛`, `(B/a)log𝓛`, `log log H`, `O(log k)`) are `o(𝓛^{2/3})`. ✔
  `k≈𝓛^{1/3}` is inside HC's range `k≤𝓛^{1/2}`. ✔
* **ET is genuinely needed** (label correct): with only (U),
  `logŜ≈0.7𝓛/log𝓛` makes `(k/a)logŜ` dominate and the optimum collapses
  to `log W≳log₂p·(log₃p)^{1/2}`, weaker than Cor 3.2.
* **Sanity check of HC (reviewer).** Every atom's class is `−a/b` with
  `ab=(M+1)/(4s)≤T/4` (O3 Lemma 2.1), so for `H≥T/4` every event vertex
  is an H-hub and HC is vacuous; HC therefore only constrains `H<T`, and
  the decay `H^{−a}` for κ-monochromatic sets of height `h>H`
  (`Δ≍1/h`) forces `a≤1`. No inconsistency found; HC is correctly
  labelled open.

**D4 (unverified step).** Step 2 asserts `h_ℓ≤1/100` "since `ℓ>y≫H`".
This is needed for O3 Lemma 1.3 and it is *not* automatic: at the chosen
k, `log H=(1+o(1))X=(0.5+o(1))(5.72/a)^{1/3}𝓛^{2/3}` while
`log y=(1+o(1))(5.72/a)^{1/3}𝓛^{2/3}`, i.e. `H=y^{1/2+o(1)}`. So it holds,
with a factor 2 in the exponent to spare, but only *because of* the
optimisation; for a larger k (smaller y) it would fail. The proof
should state `log H≤(½+o(1))log y` explicitly (or impose `k` so that
`300H(1+log H)<y`).

**D5 (EVIDENCE misreported).** §4.2 says the O3 §2 maximum outside
`𝓗_X` shows "no growth in T over `10^9…10^13`". O3 EVIDENCE 2.4's table
shows growth at small X: outside `𝓗_16`, 0.034 → 0.052 → 0.086 → 0.089;
outside `𝓗_64`, 0.013 → 0.019 → 0.033 → 0.038. Only the `𝓗_1024` column is
flat. Also θ (hence y) varies with T in that table, and it is one pair
per T. (HC tolerates `𝓛^B` growth, so this does not contradict HC, but
the sentence overstates the evidence; O3's own phrasing is inherited.)
Note also the O3 data are maxima over joint classes `c mod ℓ_1ℓ_2`
outside `𝓗_X(q)`, *without* deleting hub events, which dominates the
HC quantity (hub-free vertices ⇒ `c∉𝓗_X(q)`; deletion lowers
codegrees) — the right direction, worth saying.

**Minor wording.** "So the factorial of Theorem 1.1 is *entirely* the
cascade" after Thm 4.2 is an Assessment: Thm 4.2 shows HC suffices to
avoid it, not that nothing else could force factorial growth. Label it.

## Item 5 — §4.1, §4.3–4.4 (anatomy and ceilings; labels). Verdict: **SOUND-AFTER-REPAIRS** (label/wording repairs D6, D7)

* **§4.1 first paragraph** (the factorial arises only from the Markov
  push in Step 1, and every other parameter enters through `Ẑ_r` as the
  additive `b_k`) is a correct statement about the proof of Thm 1.1 and
  the worst-case recursion (confirmed by `omega4_rates.py recursion`). ✔
* **"Markov is sharp at the first push"** correctly cites O2 Prop 11.4,
  but that proposition is for *fixed* t, is *ineffective*
  (Siegel–Walfisz), uniform only for `D*≤(log T)^A`, and is proved for
  the θ-system with `R=(y,T^{1/3}]`. The O4 sentence drops all three
  qualifications.

**D6 (label).** §4.1 is headed "(PROVED, about the scheme)", but its
second bullet ("The cascade is an artefact") rests on EVIDENCE (O3 §2,
one pair per T, k=3) and on unproved heuristics ("a pushed
κ-monochromatic j-set has level-j sub-codegrees ≍1", "final cost
`≈Σ1/ℓ≈log(k+1)` per κ", "heavy sets are κ-monochromatic" for `j≥3`).
Repair: label the second bullet Assessment/EVIDENCE, and add the O2
Prop 11.4 qualifications to the first. Also make explicit that "the
factorial is real for the scheme as written" (here and in §6) refers to
the *worst-case parameter recursion* with Markov-saturated pushes, not
to the actual pushed masses of the ES system, which are not computed.

* **§4.3 (Assessment) — content checked.** Item 3: for n disjoint
  occurring events of support k, `B_L=Σ_{j≤⌊L/k⌋}(−1)^jbinom(n,j)=
  (−1)^{⌊L/k⌋}binom(n−1,⌊L/k⌋)` ✔ (≤`2^{n−1}`; "≈2^n" is an upper bound).
  Item 2's ceiling `H≳(kL)^{k−2}` is consistent with Thm 4.2's choice
  `H≈N^{(k−2)/a}`. Consequence 2: minimising `(k/a)·5log𝓛+𝓛/k` gives
  `k≍(a𝓛/log𝓛)^{1/2}` and `log W≳a(log₂p)²/log₃p` ✔. Labels correct.
* **§4.4 PROVED part.** `p≡1 (Q)`, `p>1` ⇒ `log p>log Q≥θ(y)`; hence
  `log p≤𝓛^{1/c}` forces `y≤𝓛^{O(1)}` and supports up to `≍𝓛/log𝓛`. ✔
  (Trivial but correct.)

**D7 (wording, §4.4 Assessment).** "Then `log p ≥ K ≥ T^{c'}`" is wrong as
stated: PO Thm 4.1 gives an *upper* bound `log p≤C_1K·max(log Z,K)` for
the prime it produces; nothing forces the actual p to be large. The
intended statement is "the bound the method certifies is `≥K≥T^{c'}`".

## Item 6 — Proposition 5.1 (Haar side). Verdict: **SOUND**; arithmetic slip D8

* O2 Thm 11.3's proof with z free: Lemma 11.2 at `c_0=1/(8k_z)` gives
  `|𝓑|≤k_zS*/c_0=8k_z²S*`; every event has `≤k_z` free primes, so the LLL
  neighbour sum is `≤2k_zc_0=1/4`, and `P(no event)≥exp(−4S_tot)≥e^{−4S*}`;
  the class of one costs `≤(π(z)+|𝓑|)𝓛`. ✔ (Needs `z≤T` so `k_z≥1`;
  harmless.)
* With `z=𝓛²` and ET: `8k_z²S*𝓛≈2𝓛³S*/(log𝓛)²≪𝓛^7/log𝓛`. O4 writes
  `≪𝓛^7log𝓛`: true but weaker by `(log𝓛)²` than what the same proof (and
  O2 Thm 11.3) gives. Cosmetic.
* "Haar form of `exp((log p)^{1/7−o(1)})`" is correctly labelled as
  resting on the density heuristic (Assessment).

**D8 (arithmetic).** §5 last bullet: "The prime side is weaker by a
factor `≍𝓛/log₂𝓛` in the doubly logarithmic scale." The two quantities
are `(1+o(1))𝓛log₂𝓛/log𝓛` and `(7+o(1))log𝓛`, whose ratio is
`≍𝓛·log₂𝓛/(log𝓛)²`, not `𝓛/log₂𝓛`. (Results-at-a-glance item 5 states
the two quantities correctly.)
