# AGENT_REPORT_O74 — ADM_m (branch `side-agent/adm-m`), checkpoint 1

Deliverable: `POINTWISE_MN2.md` (§§0–6), `scripts/mn2_delta.py`.

## Result in one paragraph
ADM_m is **not** proved. What is proved (modulo Henriot's coefficient-uniform Nair–Tenenbaum bound
(H), the uniform form of the NT input O13 already uses): after **any** prefix law ν on hard classes
mod `Q(q_0)` with density `≤ C_ν`, the AUP run in increasing order of prime powers (then MN's
adaptive rule) has per-prime drift `≤ K = (1−θ)^{−2}` (e.g. 4) except with probability
`≤ C_ν(c_1q_0^{−1/2+ε} + o(1))` (Thm 3.1). The analytic core is Lemma 2.1: the sums over atoms
completed at a step q are **T-uniform**, `≪ q^ε + (log q)^{C}` (Rankin weight + (H); NT alone loses
the Dickman decay). So ADM_m reduces exactly to the prefix.

## The obstruction found (Assessment, §4)
The brief's plan "certified finite prefix + first/second moments" is circular: (1) `c_1` is
ineffective (constants of (H)), so no finite computation certifies a q_0; (2) every prefix law with
pointwise-controlled density has `C_ν` growing faster than `q_0^{1/2}`: uniform-on-hard has
`C_ν = 1/δ_m(Q(q_0))` (exact data m=5: 4, 8, 10.9, 19.2, 31.6, 61.1 for q_0 = 8..19;
`q_0^{−1/2}/δ` grows 1.4 → 14), a single class has `φ(Q_0)`, the AUP prefix is ADM again.
The lossy step is MN's `E_ν[p_0] ≤ P_H/δ_0`; the proof only needs ν-averages over completed atoms.

## Exact missing input
Prop 5.1: hypothesis SI (ν-weighted completed-atom sums → 0) ⇒ ADM_m ⇒ exponent 1/4 for W_m
(with MN Thm 5.1, Lemma 1.1). Candidate ν = class of one mod Q(q_0) (no prefix drift, no death):
SI becomes a q_0-smooth divisor-count `τ(P_{q_0})`, `P = ma²d+1`, inside T-uniform sums — the
completed-atom analogue of O13's Hypothesis M(Y). Labelled CONJECTURE (expected provable with (H)
in each variable + regime split; not attempted in detail).

## Other proved structural facts (§1)
Lemma 1.1: MN Thm 5.1 needs only success probability ≥ s_0 > 0 and any bounded-density prefix.
Lemma 1.2: increasing-order steps have T-independent laws. Lemma 1.3: `f ≤` completed-atom mass.

## Decision needed from parent
(a) Continue on SI for the class-one prefix (substantial analytic work, multi-regime Henriot), or
(b) stop here and record Thm 3.1/Prop 5.1 as the reduction, ADM_m remaining CONDITIONAL.

## Replay
`cd scripts; (ulimit -v 8000000; timeout 1500 uv run python mn2_delta.py 5 8 9 11 13 16 17 19)`
(also `7 8 11 13 17 19`, `6 11 13 17 19`; ≤ 2 min each).
