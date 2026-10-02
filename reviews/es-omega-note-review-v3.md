# Referee report: paper/es-omega-note.tex v3 (side-agent/omega-gpair @ 9eb1d03)

Hostile journal-referee pass. Checked against POINTWISE_OMEGA3 / OMEGA2 /
OMEGA at the same commit. Sections are written and committed one by one.

## §0 Repairs from review-2 (POINTWISE_OMEGA3 review-2) — APPLIED

`git diff bbe13d0 9eb1d03 -- POINTWISE_OMEGA2.md POINTWISE_OMEGA3.md`:
* D1 (two definitions of t): Setting 3.0 now refers to `t(Ŝ)` under
  *Constants*. ✓
* D2 (level-2 error budget): `L_2` is now least with
  `4^{L_2+1}≥200k𝔐_3e^{Λ_2+3Ŝ_{≥2}}`, with `Λ_2:=16(S_1+δH_2)+16e^{98}S_2`,
  so every level contributes `≤P(all)/(100k)`. ✓ (Check: induced level-2
  singles `≤δ|P_i|≤δH_2`, degrees ≤δ, so Lemma 2.1 with z=16 gives Λ_2. ✓)
* D3 (Ω(r)≤k−1): Thm 5.2's proof now applies Thm 5.1 with `k':=max(k−1,3)`
  levels and `|𝓑|≤(k−1)S*/c_{k'}`. ✓
* 2a (fixed-slot encoding) and 2b (simplicity not needed) added to O2
  Lemma 10.2's proof. ✓ Additionally merged identical induced events in
  Thm 5.1 (harmless; consistent with 2b).

## §1 Build — CLEAN

Three `pdflatex` passes on the committed `.tex` (scratch copy): exit 0,
30 pp, **0 warnings** in the log (no undefined refs, no over/underfull
boxes reported).

## §2 `sec:hyper` (Lemmas cov, hypmom) — faithful, complete. No defect.

Matches O2 Lemmas 10.1/10.2 with the review-2 repairs: tilt parameter
`ρ≥1` stated as the primary form (cleaner than O3's "rerun with w'"),
fixed-slot encoding `N=kh` (2a), repeated hyperedges allowed (2b). The
reduction `Σ_u w^uG^cov_u ≤ Σ_C(1+w)^{|π(C)|}1[C]` is now stated
*pointwise* in the proof, which is exactly what the tilted use in
`thm:twolevel` needs. Constants re-checked (`Σ_jbinom(kh,j)Δ^{(j+1)}≤D`,
`N^{h−1}/(h−1)!≤e(ke)^{h−1}`, geometric sum under `ρ^kkeD≤1/2`).

## §3 `sec:multi` (Lemma compare, Thm twolevel, Lemma push, Cor crit3, Thm klevel, Rem hubs)

Faithful to O3 §§3, 5 (post-repair). Re-checked against the source and
re-derived where the paper changed constants:

* **Lemma compare.** (a) uses `1−x≥e^{−1.1x}` (valid, x≤1/32k); (b)
  `Σ_{Γ(B)}x_A≤|U|/32` ✓. The proof of the conditional LLL is now in
  `lem:lll` (elementary; HSS cited only as "cf.") ✓.
* **Thm twolevel.** The paper takes (P₃) = per-prime ≤1/192 (O3: 1/32)
  and compensates in Lemma push with `c_0≤δδ_3t/1728` (`9/1728=1/192` ✓).
  This is a harmless change of normalisation, not a strengthening of any
  claim. Twist numerics re-derived: mass at ℓ₀ ≤1/192, conditional factor
  `(1−1/96)^{−2}<1.1`, so `|E[Fψ]|<0.01P(Ā')` and
  `|μ_ψ|≤0.01P+0.0101P<0.03P(𝒜_{<4})<μ/4` ✓. Error terms
  `P/200+e^{−3Σ}/200` and `M_1≤4e^{Λ_2+Λ_3}` ✓.
* **Lemma push / Cor crit3.** Uses the repaired `S_2^{(b)}` bookkeeping ✓.
  `Σ≤S_1+3Ŝ/δ_3+(1+2/δ)S_2^{(b)}+Ŝ=O(Ŝ²+1)` ✓.
* **Thm klevel.** Same thresholds, `N_r`, `H_r`, `𝔐_{r+1}` as O3 Thm 5.1.
  The review-2 D2 repair is in (`L_2` with `200k𝔐_3`), so each of the
  k−1 levels contributes `≤P(all)/(100k)` ✓. Conditioned-codegree and
  induced-mass displays match O3 and my re-derivation ✓. Merging of
  identical induced events stated ✓.

Defects:

* **P1 (minor; stand-alone completeness).** The downward induction in
  Step A ("By downward induction all of `L_r,N_r,H_r,Σ_r≤C_kŜ^{A_k}`, and
  for `c_k(Ŝ)` small enough (P_k) holds at the end") is one sentence. For
  the paper's headline theorem this should be two or three lines:
  (i) `log𝔐_{r+1}=Σ_{s>r}(log4+Λ_s)` and `Λ_s`, `H_r`, `Ŝ_{≥r}` are
  linear in the earlier quantities, so `L_r,N_r=O_k(1+Σ_{s≥r}Σ_s+H_r)`;
  (ii) the pushes from level r add total mass `≤2^rΣ_r(4N_r)^r·2r/δ_r`
  and per-prime mass `≤ (per-prime mass of level r)·2^r(4N_r)^{r}·2r/δ_r`,
  so after k−2 steps every total is `Ŝ^{O_k(1)}` and every per-prime mass is
  `≤c_k(Ŝ)Ŝ^{O_k(1)}`; (iii) hence (P_k) for `A_k` large. The current
  sentence is correct but leaves this to the reader.
* **P2 (minor; label).** Remark `rem:hubs` is headed "proved for the
  stated lower bound", and the summary lists only "the lower bound in
  Remark rem:hubs" as proved — fine — but the remark also asserts, without
  label, that "the number of such classes with φ(4n)≤X grows like X log X"
  and that "removing the heavy pairs costs more than L". The source (O2
  §10.4) explicitly marks the cost bound as **Assessment, not proved**
  ("We have *not* proved this lower bound"), and O3 Def 2.3 proves only the
  *upper* bound `|𝓗_X|≤3X(1+log X)`. Mark these two sentences as
  Assessment (the theorems do not use them).

## §4 `sec:main` (Lemma qmass, Lemma iterq, Prop hmin, proof of Thm main)

Faithful to O2 Lemmas 11.1/11.2 and O3 Thm 5.2 (post-D3: `k'=max(k−1,3)`,
`κ≤k−1`, `|𝓑|≤(k−1)S*/c_{k'}`) ✓. Re-checked: (I) uses only
`ℓ^v‖M, ℓ∈Π ⇒ ℓ^v≤T` ✓; `log Q≤(π(y)+|𝓑|)𝓛+log24≤(k+1)y` ✓;
`log Z≤(k+2)y` (ℓ₀ and the moduli are `T^{o(1)}`) ✓; inversion
(two cases `𝓛≥(k+1)loglog p` / otherwise) ✓; `p>ℓ₀>T` gives distinct
primes ✓. The k=3 aside (Thm crit with `c_0=δ/32`) is consistent with
(G),(W). Prop hmin is correctly labelled Proved (no analytic input) and
Thm Hmin / Thm main "Proved modulo Thorner–Zaman" ✓. No hidden `T^c`
term (as in review-2 Item 7).

## §5 Front matter, limits, Haar side, summary

* **P3 (minor; overstatement in the abstract).** "for every fixed k,
  W(p) ≥ (log p)^k… for infinitely many p; *equivalently*, the least hard
  prime with W(p)>T is at most exp(T^{o(1)})". The second statement
  (for **all** large T) implies the first but not conversely: an
  infinitely-often bound for each k says nothing about `L_h(T)` for T
  between the realised values `W(p_j)`. The paper proves the stronger
  form (Thm main, "More precisely…"), so replace "equivalently" by "more
  precisely" / "in fact".
* **P4 (minor; stale headline).** Theorem `thm:haar-intro` in the
  introduction still states `log(1/δ*(T))≤T^{1/3+o(1)}`, while
  Theorem `thm:iterq` (Proved) gives `T^{o(1)}` and the abstract and
  the intro prose already cite `T^{o(1)}`; §Haar then says "This improves
  Theorem haar-intro". A referee will ask why the introduction headlines
  the weaker result. Either state `thm:iterq` in the introduction (keeping
  `T^{1/3+o(1)}` as the elementary-route remark) or relabel
  `thm:haar-intro` as the warm-up bound.
* Limits (`prop:complete`, `prop:ceiling`, `prop:bonf`), `hyp:min` header
  "(proved for every θ>0 (Prop hmin))", `thm:Hmin`, and the closing
  "Below θ=1/3" paragraph are consistent with the new results; the latter
  only claims that hub codegrees violate the `≲1/L` requirement, which is
  proved (constant codegrees), not the cost assessment (cf. P2) ✓.
* Summary of status: every theorem/lemma of the new sections is listed
  with the right label; TZ, Lau–Wu, Chang, ET inputs are separated ✓.
  The "Open" item (explicit rate beyond every fixed power) matches O3's
  "we claim no explicit rate" ✓.

## Verdict: **MINOR REVISION**

The mathematics is faithful to POINTWISE_OMEGA3/OMEGA2/OMEGA at this
commit, with no strengthening of any claim; the review-2 repairs D1, D2,
D3, 2a, 2b are all applied (in the notes and in the paper); headers are
labelled; cited inputs (TZ + McCurley, Lau–Wu, Chang, ET) are separated
from proved statements; the build is clean (3 passes, 30 pp, 0
warnings). Requested changes, none affecting a theorem:

| # | Where | Type |
|---|---|---|
| P1 | Thm klevel, Step A | spell out the downward polynomial induction (2–3 lines) |
| P2 | Rem hubs | mark "grows like X log X" and "removing heavy pairs costs more than L" as Assessment |
| P3 | Abstract | "equivalently" → "more precisely" |
| P4 | Intro, thm:haar-intro | headline `T^{o(1)}` (thm:iterq), not the superseded `T^{1/3+o(1)}` |
