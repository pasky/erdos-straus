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

`scripts/m17b_penum.py K` implements this with `X_cd ≈ n^{0.3}` (so that `4c²dn+1 < 10^{25}`) and
`X_e = X_ad = X_ac = ⌈(n²/X_cd)^{1/4}⌉+1`. Factorisations use GNU coreutils `factor` (GMP; primality
proved by a Lucas test). Every candidate is checked against `4abcd = a+b+nc`. **Validation:** the output
coincides *as a set of (a,b,c,d)* with the naive scan `scripts/m17b_brute.py` (all `a ≤ b`,
`2ab ≤ n`, `e = (−n mod 4ab) | a+b`, M17 §6) for K = 5, 7. Its counts equal M17's `D_P(K)` (both engines)
for K = 1, 3, 5, 7, 9. Run times: K = 9 takes 9 s and K = 11 a few minutes (vs 8 min for K = 9 with `m17_enum`).

**Computation 2.2 (CERTIFIED by one engine, validated above).** `D_P(11) = 836`.
So `D_P(K) = 2, 32, 121, 258, 604, 836` for K = 1, …, 11 (odd).

## 3. Exact union through level 6 (CERTIFIED)

`scripts/m17b_union.py` computes the exact union in `C_5` of the P-boxes from `m17b_penum` and the Q-,
U-boxes (and their inverses) from `m17_enum`. Levels ≤ 5: `covered = 26960/83521`, uncovered
`56561/83521`, which reproduces M17 Comp. 3.1 exactly. Adding Q/U level 7 gives uncovered `16346035/24137569`,
also reproducing M17. Adding the **P-boxes of level 6 (K = 11)** gives 161 boxes in `C_5`, of which 100 are new:

| level | new boxes in C_5 | measure added (fraction of cell) |
|---|---|---|
| 5 | 83 (P 54, Q 29) | 9.94·10⁻⁴ |
| 6 | 100 (P) | 7.04·10⁻⁵ |
| 7 | 94 (Q only; P K=13 pending) | 3.9·10⁻⁶ |

**Computation 3.1.** After all P-boxes of level ≤ 6 and all Q/U boxes of level ≤ 7, the uncovered
fraction of `C_5` is **ρ₁ = 16344335/24137569 = 0.677132606…** (CERTIFIED).

## 4. Explicit conditional theorem (PROVED reduction; hypothesis = CONJECTURE)

**Theorem 4.1.** Suppose that for some θ, C > 0
`(H_P)  D_P(K) ≤ C·17^{θK}` for every odd `K ≥ 13`, and `(H_Q)  D_Q(k) ≤ 17^{3k/5}` for every odd `k ≥ 9`,
and that `T_P + T_Q < ρ₁` with `T_P = 2C Σ_{K≥13 odd} 17^{θK+(1−K)/2}` and `T_Q = 2Σ_{k≥9 odd} 17^{3k/5+1−k} = 1.41·10⁻³`.
Then `C_5` and `C_7` contain sterile points. Hence (M17 Cor. 4.2) no finite set of ET Prop. 1.9 classes covers all sufficiently large
primes `p ≡ 1 (24)` with `(p/17) = −1` and `(p/q) = 1` for `q = 5, 7, 11, 13`. The admissible pairs, from `scripts/m17b_tail.py 13 9 16344335 24137569`, are:

| θ | 0.25 | 0.30 | 0.35 | **0.40** | 0.42 | 0.45 |
|---|---|---|---|---|---|---|
| largest admissible C | 619 | 87.9 | 11.8 | **1.41** | 0.569 | 0.128 |

*Proof.* Lemma 1.1, Computation 3.1, and `NB ≤ 2D`. The two series are summed numerically, with a geometric remainder bound. ∎

In words: **ET's own exponent 2/5, with constant 1.41 and no `o(1)`, from K = 13 on, suffices.** For Q, ET's exponent 3/5
with constant 1 suffices; even `17^{3k/4}` gives `T_Q = 0.076`. For comparison, the data give `D_P(K)/17^{0.4K}` = 0.64, 1.07,
0.42, 0.093, 0.022, 0.0032 (K = 1, …, 11). So the needed constant 1.41 is exceeded by none of the computed K. Polynomial versions of the hypothesis:
`D_P, D_Q ≤ 2K³` gives `T_P+T_Q = 4.0·10⁻⁴`, `≤ K⁴` gives `2.6·10⁻³`, and `≤ K⁵` gives `3.5·10⁻²`, all far below ρ₁.

**Conjecture 4.2 (explicit, EVIDENCE).** `D_P(K) ≤ 2K³` for all odd K, and `D_Q(k) ≤ 3k³` for all odd k.
Data: D_P = 2, 32, 121, 258, 604, 836 against 2K³ = 2, 54, 250, 686, 1458, 2662 (K = 1, …, 11); D_Q = 2, 73, 245, 707
against 3k³ = 3, 81, 375, 1029 (k = 1, …, 7). (`2k³` fails for Q at k = 3 and k = 7.) Under Conjecture 4.2,
`T_P + T_Q < 4.1·10⁻⁴ ≪ ρ₁`, so Theorem 4.1 applies with an enormous margin.
The random discrete-log model of M17 §6 (`17^K` equidistributed mod `f = 4ast−1`) predicts
`D_P(K) ≍ K³`. The conjecture is a *quantitative* form of it, for one base and prime-power ES denominators.

## 5. Unconditional explicit bounds: what averaging over K does and does not give

**Lemma 5.1 (first-occurrence form; PROVED).** For a pair `(a,b)`, put `m = 4ab`. The admissible K, i.e. those with
`(−17^K mod m) | a+b`, `4ab ≤ 17^K + a + b`, and the side conditions `17∤cd`, lie in at most
`#{e | a+b : −e ∈ ⟨17⟩ ⊂ (ℤ/m)^×}` residue classes mod `ord_m(17)`, one class per `e`. The boxes of `(a,b)` in one
class are nested (M17 §6), so `T_P ≤ 2 Σ_{(a,b)} Σ_e 17^{(1−K_e)/2}`, where `K_e ≥ 13` is the first admissible element of the class of `e`.
*Proof.* `17^K ≡ −e (mod m)` fixes K mod `ord_m(17)`, and `d = (17^K+e)/m`, `c = (a+b)/e`. ∎

This is the same sum as `Σ_K 17^{(1−K)/2} NB_P(K)`, only reorganised. **Averaging over K gives no unconditional gain.**
Lemma 5.1 bounds the *number* of classes, but not the position of their first element `K_e`. That position is
a discrete logarithm of `−e` modulo `4ab`. Any unconditional statement placing `K_e` well above `log_17(4ab)` for
most `(a,b)` is again a count of ES solutions of `4/17^K` with small `d = (17^K+e)/(4ab)`, i.e. a bound on `D_P(K)`.
The separation by small order does not help either. Pairs with `ord_{4ab}(17) = L` satisfy `4ab | 17^L − 1`, so
`4ab ≤ 17^L`. They are finitely many for each L and live at levels `≲ L/2`, mostly inside the exact range. The
difficulty sits entirely with typical `m`, where `ord_m(17)` is large and nothing unconditional locates the
discrete log.

**Assessment 5.2 (precise obstruction).** Theorem 4.1 needs, for *every* odd `K ≥ 13`, a bound
`D_P(K) ≤ 1.41·17^{0.4K}` (or an equivalent trade-off from the table). The only unconditional route known (ET §3,
Lemma 2.1 here) bounds `D_P(K)` by `Σ_{regimes} Σ_{pairs ≤ X} #{divisors of M in a class}`. That sum has `≍ X log X`
terms with `X ≥ n^{2/5}`. Each term is bounded only by `τ(M)`, and Lenstra's O(1) applies only when the modulus
exceeds `M^{1/3}`, which fails for small pairs. With the explicit Nicolas–Robin bound
`τ(M) ≤ M^{1.5379 log 2 / log log M}`, the tail series converges only once `0.4 + 1.92/log log M < 0.5`, i.e.
`log log M > 19`, `K ≳ 10⁸`. Any *fixed finite* set of pairs `(a,d)` is harmless: e.g. `τ(M) ≤ C M^{1/4}` gives a convergent,
explicit contribution. The obstruction is uniformity over the `≍ n^{2/5}` pairs, i.e. an explicit *average* divisor-in-class
bound over the four ET families. That is the missing input, and it is of Shiu / Brun–Titchmarsh type for
divisor functions of polynomial values with explicit constants. I do not see how to prove it here. So the outcome
remains CONDITIONAL; **no unconditional sterile point.**
