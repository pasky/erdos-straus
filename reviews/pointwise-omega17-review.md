# Hostile review of POINTWISE_OMEGA17.md (task R68b, round 1)

Reviewer branch `side-agent/review-omega17` (merged `side-agent/support-aware` at d33aff5).
From-scratch scripts: `scripts/review_o17_*.py` (none reuse the author's code).

## Verdicts per claim

| item | verdict | notes |
|---|---|---|
| Lemma 5.2 (capped planting) | SOUND | re-derived; exact-rational brute force, 192 random instances (n≤8, k≤3) + equal-odds boundary cases, `scripts/review_o17_capped.py`. Bound is attained for k=0 (dev = 1/R = s−1). |
| Lemma 1.2 | SOUND (MINOR wording) | the q>x claim is true and trivially so; see D1. |
| Lemma 1.3 | SOUND | dual re-derived; 200 random SALC LPs: primal = dual to 1e-15 (`scripts/review_o17_lemmas.py`). LP version only (integral version has no such duality; the text says so). |
| Rem 1.4 | SOUND | min is attained (compact polytope), so "valid ⇔ no fake supported on S∖A"; slack `|S_T|/N_x≍log x/𝓛` re-derived (Q's primes >T change it by `1+o(1)` as `Q≤x^δ`). |
| Lemma 2.1 | SOUND | identity re-derived; ψ≥0 not even needed. LP brute force on {0,1}^n, n≤6: monotone fake infeasible 100/100, non-monotone feasible 87/100. "Harris" is a misnomer-ish attribution (it is a one-line Efron–Stein/Russo identity), harmless. |
| Prop 3.1 (i)–(iii) | SOUND | Charlier normalisation matches `₂F₀(−n,−j;;−1/R)`; (ii) checked exactly (`E[ψ_n(N)_m]=R^m`, m<n≤7, three R); (iii) uses `Σ_{|Y|=r}1[Y on]=(N)_r/r!`. |
| Construction 3.2 | label correct (Assessment) | Haar-weighted ℓ¹ norm `2^n` re-derived (`Σ_JΣ_{Y⊆J}∏_Jp=2^ne_n(p)`); Poisson limit of `1−e_n(z−p)/e_n(−p)` is `1−C_n(N;R)` (checked by hand). Stray ∎: D4. |
| §4 x_s-centred ψ′, Assessment 4.2 | labels correct (heuristic) | `ψ′=e_n(p)·ψ`, `ψ′(0)=0`, tilt `E[ψ′|x_s]=e_n(p(x_s))` verified. |
| Lemma 4.1 | SOUND | entire-function argument correct; scope example `j(j−5)²/12` re-checked exactly at R=2,3. |
| Lemma 5.1 | SOUND | aggregated LP = full LP on 200 random instances (max diff 9e-16). |
| Prop 3.1 (iv) table | SOUND (EVIDENCE label correct; can be strengthened) | all 15 R_min values reproduced, positivity on **all** integers j≥0 with a rigorous (Fujiwara) root cutoff, `scripts/review_o17_charlier.py`, `data/review_o17/charlier.txt`. |

## Lemma 5.2 — details

Re-derivation: `(ν−P)(1_y)/P(1_y)=(−1)^{|y|+1}e_{k+1−j}(r_{∖y})/e_{k+1}(r)` follows directly from
O14 Lemma 1.1's definition (`Σ_{J⊇y}w_J=∏_y r·e_{k+1−j}(r_{∖y})/e_{k+1}(r)`). The chain uses the
*full* vector r (not `r_{∖y}`), so only `R−(n−1)r*>0` for `n≤k+1` is needed, which follows from
`R−kr*≥(k+1)/(s−1)≥k+1`; also `e_{k+1}(r)>0` since `R>kr*`. Each factor
`(k+1−i)/(R−(k−i)r*)≤(k+1)/(R−kr*)≤s−1` and `(s−1)^j≤s−1` as `s≤2`. Correct.
Script: builds ν by explicit summation over all `J`, checks `ν(0)=0`, `ν≥0`, equality of all
`≤k`-marginals, and `max_{y≠0}|dν/dP−1|≤s−1` with the tightest admissible
`s=1+(k+1)/(R−kr*)`; all pass, ratio max 1.0 (k=0 equality case).

## Prop 3.1 — details

(i) `C_n(0;R)=1`. (ii) Standard Charlier orthogonality under Poisson(R); reproduced in exact
rationals via `(N)_r(N)_m=Σ_i C(r,i)C(m,i)i!(N)_{r+m−i}` and `E(N)_a=R^a`. (iii) correct
(`C(N,r)` counts the r-sets of events that hold; in the ES reading, two events at the same ℓ with
distinct residues have empty intersection, which does not change the identity).
(iv) From scratch, integer arithmetic on `R^nψ_n(j)`: for each odd n in the table and each
integer R in `[1,R_min+40]` (n≤41) resp. `[R_min−3,R_min+40]` (n=61,81) I computed the
power-basis coefficients, a Fujiwara root bound B (beyond which `R^nψ_n>0`, leading coefficient
positive for n odd; float evaluation with 0.1% safety margin), and evaluated ψ_n at **every**
integer `0≤j≤B` (B up to 51245). Result: the table's R_min is exactly the least good integer R
in every case, the good set is up-closed on each window, and the first failure at `R_min−1`
lies at j between 3 and 567, far below the author's cutoff `4R+6n+20`. So the caveat "the
cutoff is not proved to be beyond the last sign change; a root bound is owed" is now discharged
for the listed (n,R) pairs (reviewer computation; not inserted into the author's text as
new mathematics). Still unverified: non-integer R, and monotonicity in R beyond the windows.

**Observation (not a defect).** For s=2 Lemma 5.2 gives `ν≥0` under `R≥(k+1)+kr*`, which is
*weaker* than O14 Lemma 1.1's `(1.1) R≥(k+1)+(2k+1)r*` (O14 passes to `r_{∖y}` before the chain
and loses `(k+1)r*`; Lemma 5.2 bounds `e(r_{∖y})≤e(r)` first). My exact check includes the
equal-odds boundary cases `R=kr*+(k+1)` with ν≥0. So the planting threshold improves by `(k+1)r*`
(constants only; irrelevant for the `R≍k` conclusions). The author's remark "for s=2 this is
O14's dν/dP≤2 with a slightly different hypothesis" is correct but undersells this.

## Defects

**D1 (MINOR) — Lemma 1.2 wording.** (a) "If `C∩S=∅`, the constraint is vacuous on 𝔐 (or
false)": "(or false)" cannot occur, since `𝒫_x⊆S` gives `m_x(C)=0` and the bounds are true, so
`l_C≤0≤u_C`. (b) Proof: "`m_x(C)=1[n prime]`" should be `1[n∈𝒫_x]` (a prime of S dividing L is
not counted, as the statement itself says). Repair: delete "(or false)"; replace by
`1[n∈𝒫_x]`. *Applied by reviewer.*
Answer to the brief's question "is it really true that moduli `>x` give only the box or
primality tests?": **yes, for single-class bounds**, and trivially (a class mod `q>x` meets
`[1,x]` in ≤1 integer; brute-forced for x<60). It is **not** true for *unions* of such classes,
which are arbitrary subsets of `[1,x]` (e.g. intervals); see D2.

**D2 (MAJOR, scope) — Def 1.1 / SAP omit size (archimedean) information, the most natural
support-aware input.** Def 1.1 allows only bounds on `m(C∩S)` for residue classes C, at the single
scale x. True prime information that uses the support `[1,x]` *non-trivially* is about sizes:
`π(y;q,a)` for all `y≤x` (Siegel–Walfisz/Bombieri–Vinogradov hold at every y), short-interval
counts, smooth weights `Σ_p w(p/x)1_C(p)`. None of these is a class bound (an interval in `[1,x]`
is a union of many classes mod any `q>x`, which is exactly the "family" information Lemma 1.2's
reading sets aside). A fake on `S_T∖A` must also be distributed correctly in size: with slack
`|S_T|/N_x≍log x/𝓛≫2` the box does not prevent e.g. concentrating all mass on `[1,x/2]`, which
the true count `π(x/2)` forbids. Consequently: §6(a) "Def 1.1 adds to O15 Def 2.1 *exactly* the
three forbidden items" and "the residual is now the following integer statement" overclaim:
SAP's profile `𝒥(δ)` has no size component, so SAP (even if true) does not cover certificates
using `π(y;q,a)`, `y<x`. (No PROVED item is affected; the SAP *Consequence* paragraph already
says "nothing about information outside 𝒥(δ)", which is literally correct.)
Repair: (i) state in Def 1.1 that the information is class counts at the single scale x, and
that size-localised information (`C∩[1,y]`, intervals, smooth weights) is outside the
definition; (ii) in §6 replace "exactly" / "the residual is now" by scoped wording and list
size-localised information among what SAP does not cover; (iii) (author, optional) extend SAP by
a profile item for `m(C∩[1,y])`, `x^{1−δ}≤y≤x` — heuristically harmless (a Haar-like fake can be
taken size-equidistributed, the fundamental lemma works on `[1,y]`) but that is unproved.
Wording parts (i),(ii) *applied by reviewer*.

**D3 (MINOR) — Prop 3.1 / §3 LP wording.** (a) "(iv) … `ψ_n≥0` on ℕ iff `R≥R_min(n)`" is
asserted for real R but only integer R were tested (by author and reviewer); monotonicity in R is
assumed. (b) "finds least degree `d=k+1` (k even) / `k+2` (k odd) when `R≥2k`" is stated without
the grid restriction (author's script: R∈{4,8,16,32}, k≤8). As a general statement it is false
by the author's own table: k=16 needs d=17 with ψ=1−C_17 (see (c)), but `R_min(17)=33>2k=32`
(reviewer check: `ψ_17(82;32)<0`). (c) Not a defect but worth recording: `d≥k+1` and "at d=k+1 the
fake is forced to be `1−C_{k+1}`" are elementary (if deg ψ≤k, take q=1−ψ: `E[ψ(1−ψ)]=0`,
`Eψ=1` ⇒ `Varψ=0` ⇒ ψ≡1, contradicting ψ(0)=0; at d=k+1, `ψ−1⊥` all degree ≤k ⇒ `ψ=1+cC_{k+1}`,
ψ(0)=0 ⇒ c=−1), so for k odd `d=k+1` fails globally (even degree, negative leading coefficient)
and the finite-grid caveat only concerns `d≥k+2`. Repair: say "for integer R" in (iv); add "on
the grid R∈{4,8,16,32}, k≤8" to the LP sentence. *Applied by reviewer* ((c) not inserted: new
mathematics).

**D4 (MINOR) — Construction 3.2 ends its outline with "∎".** An Assessment-level outline should
not carry an end-of-proof mark. Repair: drop ∎. *Applied by reviewer.*
