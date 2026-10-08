# AGENT_REPORT_O95: x* (r=13) as a Diophantine problem (checkpoint 2)

Branch `side-agent/r13-diophantine`. File: POINTWISE_MORDELL13B.md. Not reviewed.

## Headline: x* is NOT sterile. Conjecture 4.2 of POINTWISE_MORDELL is false.

**Theorem 3.1 (PROVED by explicit check).** x* lies in the II3 class `(a,d,e)=(8,33,11999)`. Its modulus
is `M=12670944=2⁵·3·11·13²·71` and its residue is `r=12650497`, with `r≡1 (mod M')` and
`r≡2 (mod 11·13²)`. It also lies in the I2 class `(125,88,11999)`, with modulus `M=527956000`.
* Computation 4.1 stays correct: both moduli are `>10⁶`, and both families are outside the
  II1/II2/I4 rigid search.
* A hand check of the Lemma 1.1 conditions is in §3.
* Two independent checks were run:
  - the stand-alone sympy engine of `mordell_check.py` (`scripts/m13b_check_hit.py`): polynomial
    identity, positivity, and integrality on the CRT lift of x*;
  - `mordell_lib.solve` on 200 members of each class. The members include the prime
    `p=12650497 ≡ 2 (mod 11 and 13)`, with `4/p=1/3165624+1/3339731208+1/5005839614391`.

## Other results
* Lemma 1.1 (all seven families at x(u)) and Lemma 1.2 (reciprocity parities): from checkpoint 1.
* **§2 (PROVED):** every T-generic datum of every family is an ES solution of `4/N` for an explicit T-unit
  `N` (its ES level), with `M_T ≤ N ≤ M_T²`. Lemmas 2.1–2.4 cover the mixed placements: P/Q for II3,
  P/√Q for I3, U/Q⁻¹ for I2. The datum is recoverable from the ES solution (Corollary 2.5).
* **§4 (CERTIFIED, one engine):** complete enumeration for all 32 T-units `N≤4·10⁷`, with
  `m13b_es.c` + `m13b_invert.py`.
  - *Cross-check:* all 1157 brute-force boxes from `mordell_tgen` with ES level `≤3·10⁶` are
    reproduced, 0 missing. A first run missed 374 P-type boxes because of an `a_T` loop bug; this
    check found it, and it is fixed.
  - Only the two data above, plus their dilations, contain x*.
* **Coverage of the (2,2) cell:** 10.5% uncovered at k=2, 4.74% at k=3, and 4.64% at k=4 (this last is
  incomplete, since N only reaches 4·10⁷). Previously it was 24.8% at k=4. Near-product survivor sets.
  Small-height survivors at k=4 include `(x_11,x_13)=(2,15)`, `(2,1/7)` and `(2,−7/3)`. **A new
  candidate x\*\* is `(2,15)`** (EVIDENCE only).

## Step 3 (uniform kill)
This step is now moot for x*. The simultaneous-approximation idea is still meaningful for a new
candidate such as x\*\*, but the integer simplification is lost there because `u_11≠u_13`.

## Downstream text needing repair (parent's call)
The following treat x* as a sterile candidate:
* POINTWISE_MORDELL §4 (Conjecture 4.2, the "Why Theorem C does not explain it" paragraph, the
  Consequence wording);
* any STATUS/DISCOVERIES entry citing Conjecture 4.2;
* the r=13 part of Theorem 3.1(b)'s remark that "it apparently never reaches zero exceptions".

The Consequence of Computation 4.1 is still correct as stated.

## Suggested next step
Rerun the uncovered-cell analysis with the engine at larger N (k=4 needs N up to `(11⁴13⁴)²`, so a
targeted search is needed). Then test x\*\* = (2,15), and decide whether the T-generic set for
T={11,13} can be covered at all.

# Checkpoint 3 (after the parent's steps 1–3)

(1) **Targeted searches at a given point, with no cap on the {11,13}-level** (§5). The T-part is solved as a
discrete logarithm in the T-units:
* `m13b_target.c` covers II3/I3/I1/II2;
* `m13b_target2.c` covers I2/II1/I4.

Validated against the complete engine of §4 at random box centres: 60/60 for each of the three family
groups, plus a T-in-`ad` II2 example. At x* both programs recover Theorem 3.1's data.

(2) **The small-height survivors are not covered within the searched ranges** (Computation 5.1). The points
`(u_11,u_13)=(2,15), (2,1/7), (2,−7/3), (−5/3,15)` lie in no class within these ranges:
* II3/I3/I1: `e≤10⁸` (first two), `3·10⁷` (last two);
* II2: `f≤3·10⁷`;
* U/I2: `≤2·10⁷` resp. `10⁷`;
* T-exponents `≤20` resp. `≤12`.

For comparison, x* was caught at `e=11999`. New **Conjecture 5.2:** `x** = x(2,15)` is sterile. This is
EVIDENCE only; the near-product survivor set is in §4. The Consequence (every finite covering needs a class
outside these ranges) is PROVED from 5.1.

(3) **Coverability of the T-generic set.** Not settled. The candidates did not fall, so I did **not**
attempt a finite-exception improvement of Theorem 3.1(b): its exceptional classes contain the surviving
points. Settling it would need a tail bound in the style of MORDELL17 Theorem 4.1, which is out of reach.

Possible next steps:
* push the targeted search for x** to `e≤10⁹` (about 4 h per point on one core);
* run the complete engine of §4 restricted to boxes that contain x** (the k=4 levels).
