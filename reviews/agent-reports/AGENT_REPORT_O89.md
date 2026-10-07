# Agent report O89 (branch `side-agent/redei-sign-point`) — checkpoint 1

Deliverable: `POINTWISE_TYPEI4.md`, scripts `scripts/typei4_{pell.py,pqsearch.c,dgraded.py,level.c,lb.c}`.
Sterility of `x̂_9` is **not** proved. No higher-reciprocity obstruction was found. Below is what was found
instead, with a precise statement of where it blocks.

## Main results
1. **Pell form (PROVED, Prop 1.2).** A certificate in the fibre `w≡9 (16)` at level `L=α+2γ` corresponds to a
   norm-1 unit `ε=A+8k_o√d` of `ℤ[√d]`, `d=c_o(c_oδ²+2^{L−4})`, δ odd, with `ε=(4X√P+7^b√Q)²`:
   `16PX²−Q·49^b=1`, `PQ=d`, `c'|P`, `7^a‖Q` (1.1). The sign conditions of (2.2) are exactly this square-root
   factorisation. For `L≥7`, 2 splits in `ℚ(√d)`, and `d` is of Richaud–Degert type iff `L≤6`; this explains why the
   TYPEI3 descent stays integral exactly up to level 6. In all 87 examples the unit is the fundamental unit (EVIDENCE).
2. **Reduced equation (PROVED, Cor 1.4 / Remark 1.6).** Fibre certificates of level `L` ⇔ `c'gh−P_1=2^{L−4}7^{a+2b}`,
   `g+h=8P_1X`, `h−g=2·7^{a+b}δ`; equivalently `F=8c'Xg−1`, `e=8c'Xh−1`, `Fe=1+2^{L+2}c'7^{a+2b}X²`.
3. **Finite per `(L,b)` with explicit bounds (PROVED, Lemma 3.1).** `c'gδ<2^{L−4}7^b`, `P_1 | 2^{L−4}7^b−c'gδ`, and
   `7^a<max(2^{L−5}, 2^{2L−10}7^b)=2^{2L−10}7^b` (max over the two cases of Lemma 3.1(iv); R89 repair D4, applied by
   reviewer). `L=7`, `7∤k` is done by hand (Prop 3.3).
4. **Computations (CERTIFIED once replayed; complete at all heights).** There is no fibre certificate at `L=7..10` with
   `v_7(k)≤7`. Fibre certificates exist at `L=11,13,14,16,18–26`, but none at `L=12,15,17` with `v_7(k)≤3`.
   **No certificate at `x̂_9` has `L≤22`, `v_7(k)≤3`, or `L≤26`, `v_7(k)≤1`, at any height** (Cor 3.5). This is a
   new kind of bound, orthogonal to the f-graded `f<10¹²` search. Three engines agree on overlaps (pqsearch,
   d-graded Pell, level/lb); only `lb` is complete. A second complete engine (review R89, `review_typei4_jsearch.c`)
   reproduces it on `L≤17, b≤3`; `L≤18, b≤2`; `L≤23, b≤1`; `L≤26, b=0`; `L≤10, b≤5`; the rest is single-engine
   (R89 repair D5, applied by reviewer).
5. **Scope (PROVED, Prop 4.1).** For `L≥11`, no argument that sees `w` only mod 16 can work: the fibre is
   inhabited, e.g. `(42,32,71)` is a certificate at every `w≡185 (256)`. The 34 "level-7 near misses" of TYPEI3
   Remark 5.6 have δ even (`F≡15 (16)`), so they are not fibre certificates at all.

## Negative / assessment (§4)
* The quadratic test in these coordinates reduces to an identity. Quartic symbols are vacuous, since all divisors
  are `≡3 (4)`. At fixed `(L,a,b)` finiteness is archimedean. Across levels the problem is exponential-Diophantine
  (a Pell `y`-coordinate must be `7^b`, or the 2-power tower), so linear forms in logarithms look like the right
  tool, not reciprocity.
* The 2-adic closeness of fibre certificates to 9 reaches `v_2=14` for `f<10⁹`. If it is unbounded, no
  finite-2-adic test proves sterility.

## Open (precise blocking points)
* The 7-adic tower `b→∞` at fixed `L∈{7..10}`. Each `b` is a finite check, and the "window" candidates are very
  rare for `L=7,8`, but there is no uniform bound on `b`.
* Whether `sup v_2(f+9)` over fibre certificates is finite.

## Replay
See `POINTWISE_TYPEI4.md` § Replay. All runs take seconds to minutes; the longest is `lb` at `L=23..26` (~15 min).

## Checkpoint 2 (one bounded step on the 7-adic tower, `L=7`)
* **Lemma 3.6 (PROVED; `POINTWISE_TYPEI4.md` §3.6).** At `L=7` put `u=7^b` and `j=4u−y` (the "gap"), and assume
  `7∤j`. Then the reduced equation becomes (3.1), `ρ[(4u−j)²−2mj7^au]=m(4u+j)` with `m=c'δ²`, `m j 7^a<8u`.
  A congruence mod `u` introduces an even integer `λ∈[2,4j+j²/u]` (`λ=0` is impossible mod 7). A resultant
  divisibility then bounds `7^{b−a}<2λj³+10j²+37j` and `m`, and `u` is a root of a non-zero quadratic: the leading
  coefficient would need `jm=8·7^e`, which is impossible by parity. **So for each fixed gap `j`, `b` is bounded
  explicitly.** `j=1` is excluded for all `b` by hand.
* **Not closed:** the regime `j→∞`, `b→∞`, with `m<8u/(7j)` small. For fixed `(m,a,ρ)` it is a conic whose
  points with `u=7^b` are finite only by Baker/S-unit theory (not made explicit), and `ρ` is unbounded. The case
  `7|j` is not treated. `L=8..10` follow the same method but were not done.
* No literature citation was needed. Bilu–Hanrot–Voutier would only enter for the fixed-coefficient Pell
  sub-family of Assessment 4.2(c).
