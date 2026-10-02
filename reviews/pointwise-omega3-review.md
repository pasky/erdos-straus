# Hostile review of POINTWISE_OMEGA3.md (branch side-agent/omega-gpair @ bbe13d0)

Reviewer: side agent (review-omega3). Scope: Thm 3.2 (two-level minorant),
Lemma 3.1 (conditional LLL / HSS tilt), Lemma 3.3 (push-down), Thm 3.4,
Construction 4.1 / Lemma 4.2 / Thm 4.3, Thm 5.1 / 5.2 (k levels), plus
§1 and §2 in passing. Context read: PO §§3–5 (Thm 3.1 TZ, Thm 4.1
transfer), O2 §§1–3, 10, 11.

Verdict scale: SOUND / SOUND-AFTER-REPAIRS / DEFECTIVE.

(Items are filled in one at a time; see git log.)

## Item 1 — Thm 3.2 two-level composition (pointwise minorant, level, mass): **SOUND**

*What was checked by hand.*

* Minorant. For a surviving cell `C_i`, `F_2=F_2^{(i)}` on `C_i`. This uses
  only that level-2 events inside `P_i` are decided by `x_i`, that events
  meeting `P_i` partially either vanish or induce a single, and that the
  rest are untouched. So `c_iβ_i1_{C_i} ≤ c_iF_21_{C_i}` for `c_i>0` and
  `−|c_i|α_i1_{C_i} ≤ −|c_i|F_21_{C_i}` for `c_i<0`. Killed cells give
  `0=F_21_{C_i}`. Summing gives `B ≤ F_2B_3 ≤ F_2F_3`, where the last step
  uses `F_2≥0`. This is valid for **every** outcome, non-units included,
  and for any cell decomposition of `B_3` (merged or not).
* Level / moduli. PO Thm 4.1 has no level budget. Moduli enter only
  through `log Z = log Q + log max d_i`, and the TZ range `x≥q^{12}` is
  built into `log x ≥ C_1K·max(log Z,K)`. A composite cell is a product
  of a `B_3` cell (`≤3(L_3+1)` primes) and a `β_i`/`α_i` cell on
  disjoint primes (`≤2(L_2+1)` primes). Each prime contributes
  `ℓ^{e_ℓ}≤T`, so `log d ≤ (3L_3+2L_2+5)𝓛`. With `L_2,L_3=O(Ŝ²)`
  (after Lemma 3.3) this is `T^{o(1)}`. The worry about the level of
  products of level-2 and level-3 terms is therefore empty: there is no
  `T^θ` budget per term, only `log Z`, which is dominated by
  `log Q≍y`.
* Mean. `F_2F_3−B = F_2(F_3−B_3) + Σ_i|c_i|·|γ_i−F_2^{(i)}|1_{C_i}`,
  where `γ_i` is `β_i` or `α_i` and every summand is `≥0`. Also
  `γ_i, F_2^{(i)}` depend only on the coordinates outside `P_i`. So the
  bound `2e^{Λ_3}·2·4^{−(L_2+1)}e^{Λ_2}` for the second part is right.
  The arithmetic `≤e^{−3Σ}/200` follows from the choice of `L_2`.
* Mass. Unmerged `Σ|c_i|P(C_i) ≤ M_1(B_{L_3}) + 4^{L_3+1}EG^{cov} ≤ 2e^{Λ_3}`
  (O2 Lemma 10.1(2) with 10.2 untilted, using `2^u≤16^u`). Then
  `M_1(β_i) ≤ e^{Λ_2}+e^{Λ_2}`, so `M_1(B) ≤ 4e^{Λ_3+Λ_2}`. ✓.
* Conditioned level-2 system. Its degrees are a subset of the original
  ones, so `≤δ=e^{−50}=e^{−3z−2}` at z=16, and O2 Lemma 2.1 applies.
  Induced singles add `≤δ` per fixed vertex, so `≤3δ(L_3+1)`. ✓.
* Twist (item 4). There is one Haar-uniform coordinate `ℓ_0` with
  `Eχ_0=0`. Events through `ℓ_0` have `≤2` further primes, so HSS gives a
  factor `≤(1−1/8)^{−1}<1.3`. Then `|E[Fψ]| ≤ 0.041P(𝒜')`, and
  `0.01+0.043<0.2475`. ✓.

*Independent brute force* (`scripts/review_omega3_check.py compose`,
written from scratch; it does not import `omega3_compose_check.py`). The
check is exhaustive over every outcome of random product spaces (3–5
coordinates, alphabets 2–4).

* It uses the true `G^cov_{L+1}` (private covers) at level 3, which is
  what Thm 3.2 uses. The O4 script only uses `e_{L+1}(a)`, so this is a
  small evidence gap that is now closed.
* At level 2 it uses `e_{L+1}(a)`.
* Level-2 singles may be value **sets**, and vertices may be non-singleton
  sets.
* Six generators: `plain`, `hub` (one vertex in many events of both
  levels), `nested` (level-2 edges that are sub-pairs of level-3 events,
  i.e. the push-down shape), `dense` (all triples), `dup` (duplicate
  events), and `hyper_only`.
* Merged and unmerged cell decompositions are both checked, and
  `B_3≤F_3` is checked separately.
* Result: seeds 1–3 × 3000 systems, 628 729 outcomes, **0 violations** of
  `B≤F_2F_3` (merged and unmerged) and of `B_3≤F_3`. The negative control
  (β also for negative coefficients) gives 2142 / 2235 / 2068 violations.

No defect in the algebra. The minor presentation defects are listed
under D1 below.

## Item 2 — tilted moment `E[F_2 1[C]] ≤ P(𝒜_2)P(C)e^{|π(C)|/2}` (Lemma 3.1(2), Thm 3.2 Step 1): **SOUND**

* HSS (J. ACM 58 (2011) Thm 2.1) in the variable setting is
  `P(B|∩Ā) ≤ P(B)∏_{A∈Γ(B)}(1−x_A)^{−1}`, with `Γ(B)` the events sharing
  a variable with B. Its one-line proof is
  `P(B∩⋂Ā) ≤ P(B)P(⋂_{A∉Γ}Ā)` and `P(⋂Ā) ≥ P(⋂_{A∉Γ}Ā)∏_Γ(1−x_A)`. The
  hypotheses needed are only the asymmetric LLL condition for the
  level-2 family, which (P) gives with `Σ_{A∼E}x_A ≤ 3/16`. B = "C
  occurs" is determined by `π(C)`. ✓.
* `∏(1−x_A)^{−1} ≤ e^{1.07·|U|/16} ≤ e^{|U|/2}`, using `x_A≤1/16`. ✓.
* F_2 is the right object. The error to be bounded is exactly
  `E[F_2(F_3−B_3)]`, and `0 ≤ F_3−B_3 ≤ 2·4^{L+1}G^cov_{L+1}`. The
  pointwise private-family reduction of O2 Lemma 10.2 is a sum with
  nonnegative coefficients, so it can be multiplied by `F_2≥0` and the
  conditional bound applied term by term. The tilt `e^{|π(C)|/2}` is
  absorbed by `(1+w)→(1+w')`, and Lemma 10.2 uses `|π(C)|≤|V(K)|`. ✓.
* Hypothesis bookkeeping. `D = deg + 3U_0Δ^{(2)} ≤ δ_3+3(L_3+1)t = 2δ_3 = [2e·3(1+w')³]^{−1}`. ✓.
* The comparison with the true probability is `P(𝒜_2∩𝒜_3) ≥ P(𝒜_2)∏_{level 3}(1−2P(E))`
  (Lemma 3.1(1), the standard LLL chain applied to the level-3 events
  only). ✓.

*Independent exact check* (`review_omega3_check.py tilt`, seeds 1, 2;
40+400 systems). Each system has 4–6 coordinates under a non-uniform
product measure, scaled until (P) holds with equality at the heaviest
prime. Every private family C of level-3 events is checked exactly
against both the HSS product form and the `e^{|U|/2}` form, and the
LLL chain is checked against `P(𝒜_2∩𝒜_3)`. **0 failures.** The worst
ratio LHS/`e^{|U|/2}`-RHS is 0.24, and the HSS form is attained with
equality (when `Γ(C)=∅`).

## Item 3 — Lemma 3.3 push-down, thresholds, mass flow: **SOUND**

* Non-circularity. The thresholds are `δ_3` and `δ` (absolute) and
  `t=t(Ŝ)=δ_3/(3(L_3+1))`, where `L_3` is a function of Ŝ alone. Ŝ is
  fixed *before* the push and only has to dominate `S_H`, and
  `S_H^{new}≤S_H`. The level-2 mass created by the push feeds only `L_2`
  (Thm 3.2 Step 2), never `t`. Nothing is circular.
* Degree hypothesis (D2) of O2 Lemma 2.1. Step (b) can create level-2
  vertices of large degree; this is exactly the `−4d²` clusters, of
  degree `≍c_θ ≫ δ`. Step (c) then removes every level-2 vertex of
  degree `>δ` by Markov, and deletions only lower degrees. So (D2) holds
  at the end, and the cost is `2S_2^{new}/δ = O(Ŝ/t) = O(Ŝ²)`. The
  pushed mass does break the degree bound *transiently*, but (c) repairs
  it before Thm 3.2 is invoked. ✓
* Markov sums. `Σ_{v at ℓ}p(v)deg_3(v)=w^{(3)}_ℓ`, and
  `Σ_{O∋v at ℓ}P(O)Δ_O=2w^{(3)}_ℓ` (two pairs of a 3-edge through its
  ℓ-vertex), `Σ_OP(O)Δ_O=3S_H`. The per-prime total is
  `≤c_0(2+1/δ_3+(1+2/t)(1+1/δ)) ≤ 9c_0/(tδδ_3) ≤ 1/32`. ✓
* Soundness of the replacement. A hyperedge deleted in (a), (b) or (c)
  contains a level-2 single or edge. An edge deleted in (c) contains a
  level-2 single. So `F_2F_3 ≤ 1[no original event]`. ✓
* After lifting to `ℓ^{e_ℓ}` the Markov identities are unchanged: each
  lifted hyperedge still has exactly one vertex at ℓ, and `P` is
  preserved.

*Independent exact check* (`review_omega3_check.py push`; seed 1 ×300, seeds 2–3 ×5000,
10 300 random systems with a planted hub vertex). The check:

* applies (a), (b), (c) literally;
* verifies all post-conditions (level-3 degree, pair codegree, level-2
  degree);
* verifies `S_H^{new}≤S_H`, `S_2^{new}≤S_2+3S_H/t`, and
  `S_1^{new}≤S_1+3S_H/δ_3+2S_2^{new}/δ`, with `S_2^{new}` read after
  (b) and before the (c) deletions, as the proof uses it;
* verifies `F_2F_3≤1[no original event]` at every outcome.

**0 failures.** A first run reported one failure. It came from my own
script, which read `S_2^{new}` after the (c) deletions; after the fix,
seeds 2 and 3 both give 0. Over seeds 2 and 3, about 38 000 (a)-, 880
(b)- and 2 700 (c)-pushes were exercised.

The only remark here is a presentation one, D2 below: the bound for
`S_1^{new}` refers to `S_2^{new}` *before* step (c), and the lemma does
not say so.

## Item 6 — independent end-to-end small instance (ES system → push-down → composed B → certificate): **checks pass**

`scripts/review_omega3_es_instance.py` is independent code. It does
**not** use the O2/O3 scripts. It reuses only my own
`review_omega3_check.composed_B`. The pipeline:

* builds all atoms `(M, −4D mod M)` for `M≤T`, `M≡3 (4)`, `D|A_M²`;
* applies survival w.r.t. Π (`c≡1 mod m_Π`);
* runs the iterated quarantine (O2 Lemma 11.2) at a toy threshold `c_0`
  and forms the distinct surviving events;
* splits the events into singles, edges and 3-hyperedges (asserting
  `Ω≤3` from `y⁴>T`);
* applies Lemma 3.3 (a), (b), (c) at toy quantile thresholds;
* forms the Thm 3.2 composed minorant B at small `L_3, L_2`, evaluated
  pointwise at integers `n≡1 (mod Q)`;
* computes `W(n)` by brute force (`n mod M ∈ 𝓡(M)` for some `M≤T`).

One deviation from the text: vertices are classes mod `ℓ^a`, not lifted
to `ℓ^{e_ℓ}`. This is pointwise-irrelevant.

The test points are:

* random n (Haar-like);
* constructed survivors: CRT residues chosen prime by prime to avoid
  every original and final-level event;
* *planted* points: a random level-3 event is forced first, so that
  level-3 cells of `B_3` are exercised.

The checks are `(I)` (no original event ⇒ `W>T`) and `B(n)≤1[W(n)>T]`.

| T | y | c₀ | L₃,L₂ | events s/e/h (final) | pushes (a),(b),(c) | n tested (rand+surv) | (I) viol. | `B≤1[W>T]` viol. | survivors with B(n)=1 |
|---|---|---|---|---|---|---|---|---|---|
| 30000 | 14 | 1.5 | 2,3 | 79098/45495/30 | 7,0,0 | 60+40 (20 planted) | 0 | 0 | 20 |
| 30000 | 14 | 1.5 | 1,2 | 79110/40288/6 | 13,0,22 | 100+60 (30 planted) | 0 | 0 | 30 |
| 30000 | 14 | 1.2 | 2,3 | 79185/28700/0 | 0,0,99 | 100+60 | 0 | 0 | 60 |

* Every survivor with `B(n)=1` has `W(n)>T`, confirmed by brute force.
  These are honest certificates at `T=30000`, for n of about 28 000 bits.
* As expected at toy truncations, the Monte-Carlo Haar mean of B is
  hugely **negative** (≈ −10⁵…−10⁷). The theorem needs
  `4^{L+1} ≳ e^{Λ+3Σ}`, which is astronomically out of reach. This
  matches O3 §6 "No numerical instance". So the instance checks the
  *pointwise* logic end to end ((I), survival, push-down, composition),
  not μ>0.
* At this scale step (b) never fires on the ES system (only 54
  hyperedges exist). Pair pushes are exercised in the abstract test,
  item 3.
* With realistic `c_0<1`, the quarantine eats every free prime up to
  about 40 and leaves no hyperedges at `T≤10⁵`. The toy `c_0>1` (per-prime
  masses up to 1.27) was needed to see level 3 at all. This is a
  finite-size effect, not a defect.

## Item 4 — Thm 5.1 k-level induction: **SOUND** (minor presentation defects D3, D6)

* **Mass flow and freezing.** Level r is processed only after every
  level `s>r` has pushed into it. Afterwards it only loses events, and
  only levels `<r` gain. So the frozen `Σ_r` dominates the final level-r
  mass. `L_r, N_r, H_r, Λ_r, 𝔐_{r+1}` are functions of the frozen data of
  levels `≥r`. Nothing is circular.
* **Error budget is relative, not absolute.** At level r the error is
  bounded relative to `P(𝒜_{<r})`, through Lemma 3.1(2) applied to
  `C_i∩{C occurs}`. The prime set is `P_i∪π(C)`, which accounts for the
  factor `e^{H_r/2}` in `L_r`. It is compared with
  `P(all) ≥ P(𝒜_{<r})e^{−3Ŝ_{≥r}}`, the LLL chain over levels `≥r`. So
  `L_r` never sees the masses below r. This is the same mechanism as
  Thm 3.2, verified in items 1–2. The telescoping is
  `E[F_{<r}(F_{≥r}−B_{≥r})] = E[F_{<r+1}(F_{≥r+1}−B_{≥r+1})] + Σ_i|c_i|E[F_{<r}1_{C_i}|γ_i−F_r^{(i)}|]`.
  It holds pointwise because `F_r=F_r^{(i)}` on `C_i`. ✓
* **Conditioned codegrees.** `Δ'_O ≤ Σ_{i≥0}binom(h,i)·max_{|F'|=i}Δ_{O∪F'}`
  with `h≤H_r≤N_r`. Sets of size `r` have codegree 0. The thresholds
  `δ_r(4N_r)^{−j}/(2r)` give `Δ'_v≤δ_r` and
  `Δ'_O≤δ_r(4N_r)^{−(|O|−1)}/r`. With `rU_0≤N_r` this gives
  `D≤δ_r(1+1/(3r))≤2δ_r=[2er(1+w')^r]^{−1}`. ✓
* **Induced mass.** `≤hδ_r/2+(δ_r/2r)·h·Σ_{i≥2}4^{−(i−1)} ≤ hδ_r`. ✓
  The repair from the O4 self-review is correct: the degree sum alone is
  not enough when several vertices of one event are fixed.
* **Polynomial growth for fixed k.** `Σ_k≤Ŝ` and `L_k,N_k=O_k(Ŝ)`. The
  push from level r into level `j+1` costs a factor `O_k(N_r^{j})`. So
  `Σ_{r−1}` is polynomial in the data above, and there are k steps. So
  `A_k<∞`, of factorial size as admitted. The per-prime masses are
  amplified by the same polynomials, which `c_k=Ŝ^{−A_k}/C_k` absorbs.
* **"Every k".** Each fixed k gives finite effective `C_k, A_k`. For
  `W(p)>(log p)^A` take `k>A`. For H_MIN(θ) take `k>1/θ`. Nothing
  diagonal is claimed, and the claim survives the k-dependence.
* **Twist.** Events through `ℓ_0` have `≤k−1` other primes, with
  neighbour x-sum `≤(k−1)/(32k)`, so the factor is `≤1.04`. ✓
* **Not brute-forced.** Constants of size `e^{98}` make any numerical
  instance at `k≥4` meaningless. The k-level algebra is the Thm 3.2
  algebra iterated: each step is `B_{≥r} ≤ F_rB_{≥r+1}` with `F_r≥0`.

## Item 5 — instantiation for ES (Constr. 4.1, Lemma 4.2, Thms 4.3, 5.2) vs PO Thm 4.1: **SOUND** (modulo Thorner–Zaman, as labelled)

* **(I).** O2 Lemma 4.3 (I) applies verbatim. It uses only that
  `ℓ^v‖M`, `ℓ∈Π` ⇒ `ℓ^v≤T`, so `m|Q`, and that `n≡1 (m)` forces
  `m|4D+1`. Confirmed numerically, item 6: 0 violations.
* **Per-prime masses.** Lemma 11.2 bounds the mass of the *distinct*
  events at ℓ, which dominates `g_ℓ+w^{(2)}_ℓ+w^{(3)}_ℓ`. `|𝓑|≤4S*/c_0=O(Ŝ²)`,
  and `O_k(Ŝ^{A_k+1})` for k levels. That is `T^{o(1)}` extra primes in
  Q, each costing `≤𝓛`.
* **Ω bound.** For `y=T^{1/4}e^{2𝓛/log𝓛}`, `y⁴>T`, so `Ω(r)≤3`. For
  `y=T^{1/k}e^{…}` we even get `Ω(r)≤k−1`; see D3.
* **PO Thm 4.1 hypotheses.**
  * Moduli: products of free `ℓ^{e_ℓ}≤T`, coprime to Q, unit classes.
  * Minorant on `n≡1 (Q)`.
  * `μ>0` (Thm 3.2(2)).
  * Twist for every real primitive ψ with free conductor (Thm 3.2(4);
    Thm 5.1). Odd squarefree f because `2|Q`.
  * `ℓ_0∈(R,2R]` with `R=max(T,max d_i)`: this keeps μ, `M_1`, `μ_ψ`
    unchanged and makes `p>T`.
* **Sizes.** `K=1+log(M_1/μ)=O(Ŝ²)` and `log max d_i ≤ O(Ŝ²)𝓛`. Then
  `log Z ≤ log Q+log ℓ_0+log max d_i ≤ 5y+T^{o(1)}`, and
  `log p ≤ C_1K·max(log Z,K) = y·exp(O(𝓛/log𝓛))`. The TZ range
  `x≥q^{12}` is inside `C_1`. Inverting gives exponent `4−o(1)` with
  the stated loss.
* **Effectivity.** `S*` (O2 Lemma 11.1) uses only the divisor bound, and
  every L, t, c is explicit. TZ Cor 1.4 plus the quoted McCurley region
  are effective (inherited label "modulo Thorner–Zaman").
* **Cor 4.4** (joint with `ck_min`). Same as O2 Cor 5.2, since
  `p≡1 (ℓ)` for all `ℓ≤y`. ✓

## Numbered defects

None of these touches a headline claim. No fatal, structural or
moderate defect was found.

* **D1 (minor; Setting 3.0, (D3)).**
  * Quote: "`t := δ_3/(C_3(S_H+1))` (constants of O2 Thm 10.3 for k=3,
    with the weight `1+w=17` replaced by `1+w':=17e^{1/2}`; see Step 1
    below)".
  * The operative definition, in "*Constants*", is
    `t(Ŝ):=δ_3/(3(L_3+1))`, with `L_3` defined from Ŝ, not from `S_H`
    or O2's `C_3`. Two incompatible definitions of t are on the page.
  * Fix: replace the (D3) formula by "`t:=t(Ŝ)`, defined below".
* **D2 (minor; Lemma 3.3, mass display).**
  * Quote: "`S_1^{new} ≤ S_1 + 3S_H/δ_3 + 2S_2^{new}/δ`".
  * This is true only if `S_2^{new}` means the level-2 mass **after (b)
    and before the (c) deletions**. With the final level-2 mass it is
    false.
  * Counterexample found by `review_omega3_check.py push`: `S_1=1.5`,
    `S_2=1.25`, `S_H=0.25`, `δ_3=0.75`, `t=1`, `δ=0.5`. Step (c) deletes
    every edge, so the final `S_2=0`, and `S_1^{new}=3.0 > 2.5`.
  * The `O(Ŝ²)` consequence is unaffected.
  * Fix: write `S_2^{(b)}:=S_2+(\text{pushed pairs}) ≤ S_2+3S_H/t` and
    `S_1^{new} ≤ S_1+3S_H/δ_3+2S_2^{(b)}/δ`.
* **D3 (minor; Thm 5.2 proof).**
  * Quote: "`y:=T^{1/k}exp(2𝓛/log 𝓛)` (so every rough part has
    `Ω(r)≤k`)".
  * Since `y^k>T`, in fact `Ω(r)≤k−1`, so Thm 5.1 is needed only with
    `k−1` levels. As written, the k of Thm 5.1 and the k of Thm 5.2 are
    off by one, and the k of Lemma 11.2 (free primes per M) is a third k.
  * Harmless: the statement is weaker than what is proved.
  * Fix: say `Ω(r)≤k−1` and apply Thm 5.1 with `k−1` levels, or rename.
* **D4 (minor; §1, Lemma 1.3 vs Thm 1.1/Cor 1.2).**
  * Thm 1.1 and Cor 1.2 assume `h_ℓ≤1/2` (and use `V≥e^{−2S_hub}`).
  * The twist conclusion after Lemma 1.3 ("`|E[Bψ]| ≤ … < μ(B)/4`")
    needs Lemma 1.3, which assumes `h_ℓ≤1/100`.
  * Fix: state `h_ℓ≤1/100` in the combined claim. §1 is not used by
    §§3–5, as the text says.
* **D5 (minor; evidence, §6 "Composition algebra").**
  * Quote: "The script uses O2 Lemma 1.2's `G=e_{L+1}(a)` at both
    levels."
  * Thm 3.2 uses `G^cov_{L+1}` at level 3, so the EVIDENCE did not test
    the object of the theorem. The remark that the composition does not
    depend on the majorant is correct.
  * Closed by `scripts/review_omega3_check.py compose`: true `G^cov`,
    value-set events, merged and unmerged decompositions, adversarial
    generators, 0 violations.
  * Fix: cite it, or switch the O4 script to `G^cov`.
* **D6 (minor; Thm 5.1 Step B, conditioned systems).**
  * Different events e, e′ can induce the same event
    `e∖F′ = e′∖F″`. The conditioned level-r system is then not simple,
    while O2 Setting 10.0 / Lemma 10.2 assume a simple hypergraph.
  * Harmless. Merging identical induced events leaves the void indicator
    unchanged and only lowers masses and codegrees. The proof of Lemma
    10.2 also runs with multiplicity, because a private family cannot
    contain two copies.
  * Fix: one sentence, "identical induced events are merged".

## Verdict summary

| item | verdict |
|---|---|
| 1. Thm 3.2 two-level composition: pointwise minorant, level/moduli, mass, mean, twist | **SOUND** (D1) |
| 2. Lemma 3.1 / tilted moment via HSS | **SOUND** |
| 3. Lemma 3.3 push-down: thresholds non-circular, (D2) restored by (c), Markov masses | **SOUND** (D2) |
| 4. Thm 5.1 k-level induction: freezing, relative error budgets, conditioned codegrees, induced mass, k-dependence | **SOUND** (D3, D6) |
| 5. ES instantiation vs PO Thm 4.1 (twist, moduli, TZ range, effectivity) | **SOUND** modulo Thorner–Zaman (D3) |
| 6. Independent brute force (abstract + ES end-to-end) | 0 violations; certificates `B(n)=1` ⇒ `W(n)>T` brute-force confirmed at T=30000 |
| §1 Thm 1.1 / Cor 1.2 (not load-bearing) | SOUND (D4) |
| §2 triples / hub families / EVIDENCE 2.4 (explanatory only) | SOUND as explanation; 1e9 row replays |

**Headline claims.**

* **Thm 4.3** (`W(p)≥(log p)^4·exp(−C log log p/log log log p)` i.o.;
  H_MIN(θ) for θ>1/4): **I could not break it.** It stands as PROVED
  modulo Thorner–Zaman.
* **Thm 5.2** (`W(p)>(log p)^A` i.o. for every A; H_MIN(θ) for all θ>0;
  `log L_h(T)≤T^{o(1)}`): **I could not break it.** It stands as PROVED
  modulo Thorner–Zaman, with constants depending on k (effective for
  each fixed k) and no rate for `k→∞`.

The decisive idea holds up under attack. The conditional local lemma
makes the level-3 truncation error *relative to* `P(𝒜_2)`. So `L_3`,
and with it the pair threshold `t≍1/L_3`, depend only on the level-3
mass, while the hub quarantine cost goes into the graph level, which
has no codegree condition. This really does dissolve the G_pair
circularity of O2 §11.4. I recommend accepting it after the six minor
textual repairs D1–D6.

**Reviewer caveat.** These are hand checks plus finite brute force. I
did not re-derive O2 Lemmas 2.1 and 10.2 from scratch; I rely on their
earlier review (O2 r3: SOUND, D5). The O3 argument leans on Lemma 10.2
harder than O2 did (tilted weights, mixed-size induced events), and
both uses were checked above against its stated hypotheses.

## Replay

```
export PYTHONPATH=scripts   # all runs under ulimit -v 8000000
for s in 1 2 3; do uv run python scripts/review_omega3_check.py compose 3000 $s; done   # ~1 min each
uv run python scripts/review_omega3_check.py tilt 400 2                                 # ~1 min
for s in 1 2 3; do uv run python scripts/review_omega3_check.py push 5000 $s; done      # seconds
uv run python scripts/review_omega3_es_instance.py 30000 14 1.5 2 3 60 40 1 0.9 0.99999   # ~15 s
uv run python scripts/review_omega3_es_instance.py 30000 14 1.5 1 2 100 60 2 0.7 0.999
uv run python scripts/review_omega3_es_instance.py 30000 14 1.2 2 3 100 60 4 0.8 0.995
```
