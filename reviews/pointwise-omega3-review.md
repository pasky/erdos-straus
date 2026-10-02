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

*Independent exact check* (`review_omega3_check.py push`; seeds 1–3,
5300 random systems with a planted hub vertex). The check:

* applies (a), (b), (c) literally;
* verifies all post-conditions (level-3 degree, pair codegree, level-2
  degree);
* verifies `S_H^{new}≤S_H`, `S_2^{new}≤S_2+3S_H/t`, and
  `S_1^{new}≤S_1+3S_H/δ_3+2S_2^{new}/δ`, with `S_2^{new}` read after
  (b) and before the (c) deletions, as the proof uses it;
* verifies `F_2F_3≤1[no original event]` at every outcome.

**0 failures.** A first run reported one failure. It came from my own
script, which read `S_2^{new}` after the (c) deletions; after the fix,
seeds 2 and 3 both give 0. A further 2× its total: about 38 000 (a)-, 880
(b)- and 2 700 (c)-pushes were exercised.

The only remark here is a presentation one, D2 below: the bound for
`S_1^{new}` refers to `S_2^{new}` *before* step (c), and the lemma does
not say so.
