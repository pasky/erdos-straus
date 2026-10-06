# AGENT REPORT O72 — is the sign point x̂_9 sterile? (branch side-agent/sign-point-sterility)

Deliverable: `POINTWISE_TYPEI3.md`, scripts `scripts/typei3_*`.

## Outcome (one paragraph)
Sterility of `x̂_9` (Conjecture 3.4 of POINTWISE_TYPEI2) is **not proved**. I prove that no
non-empty clopen subset of Σ_7 is sterile (Prop 3.1: the sterile set of Σ_7 is closed and nowhere
dense; this holds around every point and is not specific to x̂_9 — R72 repair D3, applied by reviewer). So a proof cannot rest on one finite-modulus congruence class; fibre-based proofs are not excluded. I found **no certificate**, using a new complete
search graded by the smaller divisor `f=min(F,e)` (Lemma 1.1). It reaches all heights for a
given f, and Lemma 1.2 converts it into a height bound. Result: no certificate with
`f<10¹²`, hence every Type-I covering of {n_p=7} has height `>1.32·10¹²`, and under H
`C(7)>1.32·10¹²` (was `>3·10⁹`). The f-graded near-miss statistics in the sign fibre support Conjecture 3.4
(and suggest that ≈60% of the fibre is sterile; depth-truncated computation, error ≤0.0013). They also give a precise reduction (Remark 4.1):
an explicit tail bound for the near-miss count would give a sterile point
(not necessarily `x̂_9`), hence `C(7)=∞` under H.

## Results and labels
| item | label |
|---|---|
| L1.1 small-divisor reduction; L1.2 f-bound ⇒ height bound `1.3229(Y−1)` | PROVED |
| C2.3 r=23,31,47: no certificate with f<10¹¹ ⇒ covering heights >2.39/2.78/3.42·10¹¹ | CERTIFIED (r=23: two engines, R72 re-run; r=31, 47: one engine — R72 repair D4, applied by reviewer) |
| Prop 3.1 sterile points nowhere dense (no non-empty clopen subset of Σ_7 is sterile; not specific to x̂_9 — R72 repair D3, applied by reviewer) | PROVED |
| L5.1 Vieta descent (`Fe=1+4ck²`, `e−F=4ckδ` ⇒ `F≡1 mod 4cδ`); C5.2 certificates at x̂_9 need `t≥5`, `α+2γ≥5`; P5.3 levels `α+2γ∈{5,6}` force `c'=1`; P5.4 level `α+2γ=5` empty (deduction from self-review R72); P5.5 level `α+2γ=6` empty ⇒ certificates need `α+2γ≥7` | PROVED |
| C2.1 no certificate at x̂_9 with f<10¹² ⇒ covering height >1.32·10¹²; C(7)>1.32·10¹² under H | CERTIFIED (two engines to 10¹¹ (incl. r=23), one engine to 10¹² — R72 repair D4, applied by reviewer; cross-checked vs typei2_signcheck on 10 (r,w) pairs at X=2·10⁵ and 3 at X=3·10⁶) / CONDITIONAL (H) |
| §4 f-graded mass, 60.9–61.0% of the fibre uncovered for f<10¹⁰ (depth-truncated t≤40), t_min ≈ ½log₂f | EVIDENCE / Assessment |
| Remark 4.1 measure route (tail bound ⇒ sterile point) | PROVED reduction; input open |

## What did not work
The Vieta descent (Lemma 5.1) is integral only when `4c/4^{t−4}∈ℤ` (`α+2γ≤6`). Beyond that it runs in `ℤ[1/2]`
and ends at reduced pairs with `F_end∈(0,1]∩ℤ[1/2]` (several classes). Mod `2^{10}` (with `c_o` a power of 7) level 6 shows no 2-adic obstruction.
Quadratic reciprocity / genus characters are exactly the Lemma 2.1 test and pass at x̂_9.
The 2-adic refinement (F=2^t g−9, 9e=2^t h−1, `2^t gh−g−9h=9nk`) is consistent at all
levels. A heuristic Lenstra-type sketch suggests only ≪Λ^{1/2+ε} near misses per level (borderline; not proved).

## Self-review
`reviews/pointwise-typei3-selfreview.md` (deep reviewer subagent). Verdict: request changes. Three MAJOR findings
(an unrestricted completeness claim, depth truncation in §4, an overreaching Prop 3.1 consequence) are all fixed.
The review also contributed Prop 5.4. The full 10¹²/10¹¹ searches were cross-checked against typei2_signcheck on small ranges (X≤3·10⁶). (R72 repair D4,
applied by reviewer:) review R72 re-ran `x̂_9` with `f<10¹¹` and r=23 with `f<10¹¹` using an independent engine
(0 certificates, same f counts); `[10¹¹,10¹²)` and r=31, 47 remain one-engine.

## Follow-up (parent request): level α+2γ=6 — CLOSED (Prop 5.5, PROVED)
The integral chain is a Pell orbit `ε^m`, with `ε=(D+2+√(D(D+4)))/2` and `D=7^aδ²`. Mod 32, `v_2(H)=4` forces m to be an odd
multiple of 3. Then `D+3=U_3` divides both `H` and `(X−2)`, so an odd prime `q|(D+3)/2`, `q≠7`, divides `k'`
while `F≡+1 (mod q)`. This clashes with `F≡−1 (mod k')`. No primitive-divisor theorem is needed. Checks:
`scripts/typei3_level6.py` (mod-32 period check, polynomial identity for m≤33, and 777 chain positions
with a ∈ {1,3,5}, δ<150: 0 violations).
Next level α+2γ=7 (Remark 5.6, open): `4c̃=c_o/2∉ℤ`, so the descent runs in ℤ[1/2] with several reduced classes.
Unlike levels 5–6, level 7 already contains 34 near misses up to ck ≤ 10⁸.

## Suggested next steps
* Level `α+2γ=7`: classify the ℤ[1/2]-orbits (reduced pairs with `F_end∈(0,1]∩ℤ[1/2]`) and test the sign split
  on each orbit, as in P5.5.
* Measure route (Remark 4.1): an explicit summable bound for near-miss counts would give `C(7)=∞` under H
  without deciding `x̂_9`.
* An independent re-run of Computation 2.1 on `[10¹¹,10¹²)` (≈9–18 core-hours; `[1,10¹¹)` done in R72).

## Replay
See POINTWISE_TYPEI3.md, Replay section.
