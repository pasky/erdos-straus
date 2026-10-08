# POINTWISE_MORDELL17B — the r = 17 tail: union measure, exact level 6, explicit hypotheses (task O93)

Status: O93 (branch `side-agent/r17-explicit-tail`), work in progress, not reviewed.
Builds on POINTWISE_MORDELL17.md (= "M17"; reviewed R83 rounds 1–2). Notation and labels as there.
`N = 17^K`, K odd; P-data at level K = N-points `(a,b,c,d)` of `Σ^II_N` with `a ≤ b`, `17∤cd`
(equivalently `(a,s,t) = (a,c,d)` with `f = 4ast−1 | s·N + a`, `b = (sN+a)/f ≥ a`); each gives the
two boxes `−f`, `−(4bcd−1)` mod `17^{(K+1)/2}`.

## 1. What has to be bounded (PROVED, elementary)

**Lemma 1.1 (the union is P ∪ Q, by first occurrence).** The union of all boxes of the seven families
meeting `C_5` equals the union of the (P)-boxes and the (Q)-boxes (Q⁻¹ = Q as sets of boxes, √Q = ∅,
U ⊂ P). Hence, writing `μ₅` for the Haar measure normalised to `μ₅(C_5) = 1`,
`μ₅(covered) ≤ μ₅(covered by P-boxes of level ≤5 and Q-boxes of level ≤7) + T_P + T_Q`, with
`T_P = Σ_{K ≥ 11 odd} 17^{(1−K)/2} · NB_P(K)`, `T_Q = Σ_{k ≥ 9 odd} 17^{1−k} · NB_Q(k)`,
where `NB_P(K)` (resp. `NB_Q(k)`) is the number of *new* (not contained in a box of lower level of
the same type) P-boxes of level `(K+1)/2` (Q-boxes of level k) meeting `C_5`. Trivially
`NB_P(K) ≤ 2 D_P(K)`, `NB_Q(k) ≤ 2 D_Q(k)`.
*Proof.* M17 Lemma 1.1 lists the box types; √Q = ∅ (M17 Lemma 1.3); Q⁻¹ = Q as sets (M17 Lemma 5.1,
consequences); every U-box meeting a cell lies in a P-box (M17 Lemma 5.2), which is counted in the
P-union whatever its level. P-boxes have level `(K+1)/2` and K is odd (M17 Lemma 1.3); Q-boxes
exist only at odd levels (M17 Lemma 1.3). A box contained in a box of lower level adds nothing
to the union. Boxes of level `L` have `μ₅ = 17^{1−L}`. ∎

So the base is the exact uncovered fraction `ρ₀` after P-levels ≤ 5 and Q-levels ≤ 7 (M17 Comp. 3.1
gives `1 − 0.322797`; the exact rational is recomputed in §3), and **a sterile point in `C_5` exists
as soon as `T_P + T_Q < ρ₀`** (same proof as M17 Theorem 4.1).

## 2. A complete N^{2/5}-type enumerator for P (PROVED completeness; CERTIFIED output)

**Lemma 2.1 (ET four-regime cover, made exact).** Let `(a,b,c,d,e)` be an N-point of `Σ^II_n` with
`a ≤ b`. If `X_e² X_ad X_ac X_cd ≥ n²` (positive integers), then `e ≤ X_e` or `ad ≤ X_ad` or
`ac ≤ X_ac` or `cd ≤ X_cd`. In each regime the point is recovered from a factorisation:
`e`: `4abd = n+e`; `ad`: `f | n+4a²d`, `f ≡ −1 (4ad)`; `ac`: `f | nc+a`, `f ≡ −1 (4ac)`;
`cd`: `f | 4c²dn+1`, `f ≡ −1 (4cd)` (ET (2.13), (2.19), (2.20), (2.21)).
*Proof.* With `a ≤ b`: `ce = a+b ≤ 2b` and `4abd = n+e` with `e ≤ a+b ≤ 2abd`, so `abd ≤ n/2` and
`acde ≤ 2abd ≤ n` (the proof of ET Lemma 2.8, which uses only the equations). Hence
`e²(ad)(ac)(cd) = (acde)² ≤ n²`. ∎

`scripts/m17b_penum.py K` implements this with `X_cd ≈ n^{0.3}`, to keep `4c²dn+1` moderate (≈ 1.5·10²⁶ at K = 13; harmless, as `factor` is GMP-based; R93 repair m8: was "< 10²⁵"), and
`X_e = X_ad = X_ac = ⌈(n²/X_cd)^{1/4}⌉+1`. Factorisations use GNU coreutils `factor` (GMP; primality
proved by a Lucas test). Every candidate is checked against `4abcd = a+b+nc`. **Validation:** the output
coincides *as a set of (a,b,c,d)* with the naive scan `scripts/m17b_brute.py` (all `a ≤ b`,
`2ab ≤ n`, `e = (−n mod 4ab) | a+b`, M17 §6) for K = 5, 7. Its counts equal M17's `D_P(K)` (both engines)
for K = 1, 3, 5, 7, 9. Run times: K = 9 takes 9 s and K = 11 a few minutes (vs 8 min for K = 9 with `m17_enum`).

**Computation 2.2 (CERTIFIED: O93 engine + R93 engine; R93 repair m1).** The R93 review (`review_m17b_k11.c`, `review_m17b_k13.c`, independent sieve-based C code) reproduces both counts. Its sorted point sets have the same sha256 as ours (K = 11 `19cbd5ac…`, K = 13 `2ec22df7…`). The sets for K ≤ 13 are stored in `data/m17b/p{K}.txt` with `SHA256SUMS`. `D_P(11) = 836` and `D_P(13) = 1463`. K = 13 took ≈ 1.5 h:
the regimes `e ad` and `ac cd` ran in parallel and gave 1415 and 925 data, overlapping. So
`D_P(K) = 2, 32, 121, 258, 604, 836, 1463` for K = 1, …, 13 (odd).

## 3. Exact union through level 6 (CERTIFIED)

`scripts/m17b_union.py` computes the exact union in `C_5` of the P-boxes from `m17b_penum` and the Q-,
U-boxes (and their inverses) from `m17_enum`. Levels ≤ 5: `covered = 26960/83521`, uncovered
`56561/83521`, which reproduces M17 Comp. 3.1 exactly. Adding Q/U level 7 gives uncovered `16346035/24137569`,
also reproducing M17. Adding the **P-boxes of level 6 (K = 11)** gives 161 boxes in `C_5`, of which 100 are new:

| level | new boxes in C_5 | measure added (fraction of cell) |
|---|---|---|
| 5 | 83 (P 54, Q 29) | 9.94·10⁻⁴ |
| 6 | 100 (P) | 7.04·10⁻⁵ |
| 7 | 272 (P 178, Q 94) | 1.13·10⁻⁵ (P 7.37·10⁻⁶, Q 3.89·10⁻⁶; R93 repair m3: was 6.6·10⁻⁶) |

**Computation 3.1.** After all P-boxes of level ≤ 6 and all Q/U boxes of level ≤ 7, the uncovered
fraction of `C_5` is **ρ₁ = 16344335/24137569 = 0.677132606…** (CERTIFIED). Adding P-level 7 (K = 13), the uncovered fraction after
all boxes of level ≤ 7 is **ρ₂ = 961421/1419857 = 0.677125231…** (CERTIFIED; `m17b_union.py . 13 7`).

## 4. Explicit conditional theorem (PROVED reduction; hypothesis = CONJECTURE)

**Theorem 4.1.** Suppose that for some θ, C > 0
`(H_P)  D_P(K) ≤ C·17^{θK}` for every odd `K ≥ 13`, and `(H_Q)  D_Q(k) ≤ 17^{3k/5}` for every odd `k ≥ 9`,
and that `T_P + T_Q < ρ₁` with `T_P = 2C Σ_{K≥13 odd} 17^{θK+(1−K)/2}` and `T_Q = 2Σ_{k≥9 odd} 17^{3k/5+1−k} = 1.4106·10⁻³ < 1.411·10⁻³` (R93 repair: no rounding down of a subtracted term).
Then `C_5` and `C_7` contain sterile points. Hence (M17 Cor. 4.2) no finite set of ET Prop. 1.9 classes covers all sufficiently large
primes `p ≡ 1 (24)` with `(p/17) = −1` and `(p/q) = 1` for `q = 5, 7, 11, 13`. The admissible pairs, from `scripts/m17b_tail.py 13 9 16344335 24137569`, are:

| θ | 0.25 | 0.30 | 0.35 | **0.40** | 0.42 | 0.45 |
|---|---|---|---|---|---|---|
| largest admissible C (rounded **down**) | 619.2 | 87.88 | 11.76 | **1.409** | 0.5686 | 0.1275 |
| same, hypothesis from K ≥ 15 (base ρ₂) | 2553 | 272.9 | 27.53 | **2.484** | 0.8947 | 0.1692 |

(R93 repair M1/m2: entries previously rounded *up*. In particular C = 1.41 at θ = 0.4 is **not** admissible: the exact
threshold is 1.409796…, and C = 1.41 gives `T_P + T_Q = 0.677230 > ρ₁`. `m17b_tail.py` now prints floor-rounded values
and adds the exact geometric remainder of the power series beyond K = 999.)

*Proof.* Lemma 1.1, Computation 3.1, and `NB ≤ 2D`. The two series are summed numerically, with a geometric remainder bound. ∎

In words: **ET's own exponent 2/5, with constant 1.40 and no `o(1)`, from K = 13 on, suffices** (R93 repair M1: was 1.41; with K ≥ 15 and base ρ₂, constant 2.48). For Q, ET's exponent 3/5
with constant 1 suffices; even `17^{3k/4}` gives `T_Q = 0.076`. For comparison, the data give `D_P(K)/17^{0.4K}` = 0.64, 1.07,
0.42, 0.093, 0.022, 0.0032, 0.00058 (K = 1, …, 13). So the needed constant 1.40 is exceeded by none of the computed K (R93 repair M1). Polynomial versions of the hypothesis:
`D_P, D_Q ≤ 2K³` gives `T_P+T_Q = 4.0·10⁻⁴`, `≤ K⁴` gives `2.6·10⁻³`, and `≤ K⁵` gives `3.5·10⁻²`, all far below ρ₁.

**Conjecture 4.2 (CONJECTURE; EVIDENCE: data below; R93 repair m7).** `D_P(K) ≤ K⁵` for every odd `K ≥ 15`, and
`D_Q(k) ≤ k⁵` for every odd `k ≥ 9`. With base ρ₂ this gives `T_P + T_Q ≤ 4.2·10⁻³ ≪ ρ₂`, so Theorem 4.1 (K ≥ 15 row)
applies with a wide margin. From K ≥ 13 with base ρ₁ the tail would be 0.035.
*Observation (EVIDENCE, tighter and more fragile).* Data: D_P = 2, 32, 121, 258, 604, 836, 1463 against
2K³ = 2, 54, 250, 686, 1458, 2662, 4394 (K = 1, …, 13), with equality at K = 1. D_Q = 2, 73, 245, 707 against
3k³ = 3, 81, 375, 1029 (k = 1, …, 7): only four points, one at 90% of the bound. `2k³` fails for Q at k = 3 and k = 7.
The random discrete-log model of M17 §6 (`17^K` equidistributed mod `f = 4ast−1`) predicts `D_P(K) ≍ K³` *on average*,
with fluctuations. That is why the main conjecture is stated with the robust exponent 5 rather than with 2K³/3k³.
(R93 repair m7: previously the 2K³/3k³ form was the conjecture, labelled "explicit, EVIDENCE".)

## 5. Unconditional explicit bounds: what averaging over K does and does not give

**Lemma 5.1 (first-occurrence form; PROVED; R93 repair m4).** Only pairs `(a,b)` with `17 ∤ ab` matter. If `17 | ab`, then
`17 | a` and `17 | b` (M17 §6), and the boxes are `≡ 1 (mod 17)`, which miss the cells. For `17 ∤ ab` put `m = 4ab`.
* The admissible K are those with `(−17^K mod m) | a+b`, `4ab ≤ 17^K + a + b` and `17∤cd`. Since `0 < e ≤ a+b < 4ab`,
  `e` is the least positive residue of `−17^K`, so `17^K ≡ −e (mod m)` fixes K mod `ord_m(17)`. Hence the admissible K
  lie in at most `#{e | a+b : −e ∈ ⟨17⟩ ⊂ (ℤ/m)^×}` residue classes mod `ord_m(17)`, one per `e`.
* By M17 Lemma 5.1(ii), every box of `(a,b)`, for every K and every `e`, is a ball around the same centre `−a/b`.
  So all boxes of the pair are nested, and
  `T_P ≤ 2 Σ_{(a,b): 17∤ab, K_min(a,b) ≥ 13} 17^{(1−K_min(a,b))/2}`, where `K_min(a,b)` is the least admissible K.
  Pairs with an admissible `K ≤ 11` contribute nothing.
*Proof.* As stated; `d = (17^K+e)/m` and `c = (a+b)/e` are determined by `(a,b,K)`. ∎
This is an upper bound for `Σ_K 17^{(1−K)/2} NB_P(K)`, not equal to it (R93 repair m4: was "the same sum").

*Assessment (R93 repair m5: previously unlabelled).* Averaging over K gives no unconditional gain that I can see.
Lemma 5.1 bounds the *number* of classes but not where `K_min` falls, and that position is a discrete logarithm of
`−e` modulo `4ab`. An unconditional statement placing `K_min` well above `log_17(4ab)` for most `(a,b)` amounts to
counting ES solutions of `4/17^K` with small `d = (17^K+e)/(4ab)`, i.e. to a bound on `D_P(K)`. Separating out small
order does not obviously help. Pairs with `ord_{4ab}(17) = L` satisfy `4ab | 17^L − 1`, so `4ab ≤ 17^L`. They are finitely
many for each L, and their first admissible K lies in `[K_min, K_min + L)` with `K_min ≈ log_17(4ab) ≤ L`, so `K < 2L`,
i.e. level `≲ L`. (R93 repair m5: was "`≲ L/2`, mostly inside the exact range"; the latter is unsupported and dropped.)
The difficulty is with typical `m`, where `ord_m(17)` is large and nothing unconditional locates the discrete log.

**Assessment 5.2 (obstruction; revised, R93 repair m6).** Theorem 4.1 needs, for *every* odd `K ≥ 13`, a bound
`D_P(K) ≤ 1.40·17^{0.4K}` (R93 repair M1), or `≤ 2.48·17^{0.4K}` for `K ≥ 15`, or a trade-off from the table. The known
unconditional route (ET §3, Lemma 2.1 here) bounds `D_P(K)` by a sum over four regimes, each a sum over `≍ X log X` pairs
(`X ≈ n^{2/5}`) of a count of divisors of some `M` in a residue class. The ingredients:
* *Pointwise divisor bound.* With Nicolas–Robin, `τ(M) ≤ M^{1.5379 log 2 / log log M}`, and taking `M ≈ n^{1.8}` (the size in
  the `cd` regime), the per-K terms `17^{(1−K)/2}·X log X·τ(M)` decay only once `0.4 + 1.92/log log M < 0.5`, i.e.
  `log log M > 19.2`, `K ≳ 4·10⁷`. Before that they are not small, so this route alone is useless.
  (R93 repair m6a: the size assumption is now stated, and the claim is about the terms, not about convergence.)
* *Divisors in residue classes.* Lenstra (O(1) divisors in a class mod `s ≥ M^{1/3}`) and Coppersmith–Howgrave-Graham–Nagaraj
  (`O_ε(1)` for `s ≥ M^{1/4+ε}`; cited from the reviewer's memory, not checked here) make the count per pair O(1) for most
  pairs of the `ad` regime (`M ≍ n`, modulus `4ad ≥ n^{1/4+ε}`). The failing pairs, `n^{1/4+o(1)}` of them, are negligible.
  The `ac` regime is similar: its failing pairs number `≲ n^{0.35}`. (R93 repair m6b: previously these regimes were
  described as blocked by Lenstra's `M^{1/3}` threshold.)
* *The actual bottleneck.* It is (i) the `e`-regime, an average of `τ_3((n+e)/4)` over the short interval `e ≤ n^{2/5}`
  (Shiu type); (ii) the `cd` regime, where `M ≈ c²dn` and the modulus `4cd` is small relative to M, so the cover would have to be
  rebalanced; and (iii) the explicit constants (of CHN and of the short-interval divisor sums). Even a successful version would
  give at best `D_P ≪ n^{2/5}(log n)^{O(1)}`, with large explicit constants. By the table that needs a tiny constant at
  θ ≈ 0.45 (≤ 0.169 from K ≥ 15), or exact data up to a large K.
I do not see how to make this explicit at the required strength. So the outcome remains CONDITIONAL; **no unconditional
sterile point.**

## Replay

```
mkdir -p /tmp/o93 && cd /tmp/o93 && W=<worktree>
for K in 1 3 5 7 9 11; do PYTHONPATH=$W/scripts uv run --project $W python $W/scripts/m17b_penum.py $K > p$K.txt; done   # K=11: minutes
uv run python $W/scripts/m17b_brute.py 5 | sort | diff - <(sort p5.txt)        # and K=7 (slow): completeness check
gcc -O2 -o m17_enum $W/scripts/m17_enum.c
for m in Q U; do for k in 1 3 5 7; do ./m17_enum $m $k | sort -u > $m$k.txt; done; done
python3 $W/scripts/m17b_union.py . 9 5     # = 56561/83521 (M17 Comp. 3.1)
python3 $W/scripts/m17b_union.py . 11 7    # rho_1 = 16344335/24137569
python3 $W/scripts/m17b_tail.py 13 9 16344335 24137569   # Theorem 4.1 table
# K=13 (≈ 1.5 h on 2 cores): run m17b_penum.py 13 "e ad" and "ac cd" in parallel, sort -u the union into p13.txt (1463)
python3 $W/scripts/m17b_union.py . 13 7   # rho_2 = 961421/1419857
python3 $W/scripts/m17b_tail.py 15 9 961421 1419857
```
