# AGENT REPORT O72 — is the sign point x̂_9 sterile? (branch side-agent/sign-point-sterility)

Deliverable: `POINTWISE_TYPEI3.md`, scripts `scripts/typei3_*`.

## Outcome (one paragraph)
Sterility of `x̂_9` (Conjecture 3.4 of POINTWISE_TYPEI2) is **not proved**. I prove that it
cannot be proved by any congruence argument modulo a fixed modulus (Prop 3.1: the sterile
set of Σ_7 is closed and nowhere dense). I found **no certificate**, using a new complete
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
| C2.3 r=23,31,47: no certificate with f<10¹¹ ⇒ covering heights >2.39/2.78/3.42·10¹¹ | CERTIFIED (one engine) |
| Prop 3.1 sterile points nowhere dense (no fixed-modulus proof of sterility) | PROVED |
| L5.1 Vieta descent (`Fe=1+4ck²`, `e−F=4ckδ` ⇒ `F≡1 mod 4cδ`); C5.2 certificates at x̂_9 need `t≥5`, `α+2γ≥5`; P5.3 levels `α+2γ∈{5,6}` force `c'=1` | PROVED |
| C2.1 no certificate at x̂_9 with f<10¹² ⇒ covering height >1.32·10¹²; C(7)>1.32·10¹² under H | CERTIFIED (one engine, cross-checked vs typei2_signcheck on 10 (r,w) pairs at X=2·10⁵) / CONDITIONAL (H) |
| §4 f-graded mass, 61% of the fibre uncovered for f<10¹⁰, t_min ≈ ½log₂f | EVIDENCE / Assessment |
| Remark 4.1 measure route (tail bound ⇒ sterile point) | PROVED reduction; input open |

## What did not work
The Vieta descent (Lemma 5.1) is integral only when `4c/4^{t−4}∈ℤ` (`α+2γ≤6`). Beyond that it runs in `ℤ[1/2]`
and ends at reduced pairs with `F_end∈(0,1]∩ℤ[1/2]` (several classes). Mod `2^{10}` the levels `α+2γ∈{5,6}` show no 2-adic obstruction.
Quadratic reciprocity / genus characters are exactly the Lemma 2.1 test and pass at x̂_9.
The 2-adic refinement (F=2^t g−9, 9e=2^t h−1, `2^t gh−g−9h=9nk`) is consistent at all
levels. A heuristic Lenstra-type sketch suggests only ≪Λ^{1/2+ε} near misses per level (borderline; not proved).

## Replay
See POINTWISE_TYPEI3.md, Replay section.
