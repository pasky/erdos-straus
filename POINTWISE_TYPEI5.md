# The 7-power tower at the sign point `x̂_9` (task O92)

Status: work in progress (side agent O92, branch `side-agent/lfl-sign-point`). Not reviewed.
Builds on POINTWISE_TYPEI4.md (Prop 1.2 / (1.1), Cor 1.4 / (1.2), Lemma 3.1, Lemma 3.6).
Notation as there: a fibre certificate of level `L` is a solution of

```
16·P·X² − Q·u² = 1,  u = 7^b,  P = c'P_1,  Q = 7^a Q_1,  P_1Q_1 = M := c_oδ² + T,   (1.1)
c_o = 7^a c',  T = 2^{L−4},  d = PQ = c_o M,  a odd,  c', P_1, X, δ odd,  7 ∤ c'P_1X.
```

## 1. Every certificate unit is the minimal one: a Lehmer sequence argument (PROVED)

**Lemma 1.1 (PROVED).** Let `P, Q ≥ 1` be integers with `7 | Q`, `PQ` not a square. Let `(X_1,u_1)` be the
positive solution of `16PX² − Qu² = 1` with `u_1` minimal, and assume some solution has `u` odd. Then every positive solution has `u` of the form
`u_n = u_1·L_n` (`n ≥ 1` odd) with integers `L_n`, `L_1 = 1`, and **`u_n` is a power of 7 only if `n = 1`**.
In particular, for each `(P,Q)` with `7|Q` at most one `b` gives a solution of (1.1), namely `7^b = u_1`.

*Proof.* Put `s = 4X_1√P`, `r = u_1√Q`, `α = s + r`, `β = s − r`, so `αβ = s² − r² = 1`, `α > 1`.
(a) *If some solution has `u` odd, all positive solutions are odd powers of `α`.* For two solutions
`η = 4X√P + u√Q`, `η' = 4X'√P + u'√Q` (norm form `16PX² − Qu² = 1`; note `1/η' = 4X'√P − u'√Q`),
`η/η' = (16PXX' − Quu') + 4(X'u − Xu')√d` lies in the group `G := {A + 4B√d : A² − 16dB² = 1}`, which is infinite
cyclic (`d` not a square); let `ν_0 > 1` generate it. Conversely `α·(A + 4B√d) = (4X_1A + 4u_1BQ)√P + (16X_1BP + u_1A)√Q`
has the shape again. So the solutions are exactly the elements of `αG` of the shape, and those with `X, u > 0` are exactly
the elements `> 1` of `αG` (for `η > 1`: `4X√P = (η+η^{−1})/2 > 0`, `u√Q = (η−η^{−1})/2 > 0`). `α` is the smallest
of them. `α² = (16PX_1² + Qu_1²) + 8X_1u_1√d ∈ G`, so `α² = ν_0^m`, `m ≥ 1`. If `m ≥ 3`, `αν_0^{−1} = ν_0^{m/2−1}`
is an element of `αG` in `(1, α)`, i.e. a positive solution with smaller `u` (`u√Q = (η−η^{−1})/2` increases with `η`), contradicting minimality. If `m = 2`, `α = ν_0 ∈ ℤ[√d]`, so `√P = p ∈ ℤ` (`√P ∈ ℚ(√d)`, `Q ≠ 1/k²`) and every element of `αG = G` is `A + 4B√d = 4X√P + u√Q`
with `u = 4Bp` even — excluded by hypothesis. So `m = 1`, `G = ⟨α²⟩` and the positive solutions are
`α^n`, `n ≥ 1` odd.
(b) *Integrality.* `α^n = Σ_k C(n,k) s^{n−k} r^k`. For `n` odd, the terms with `k` even are integer multiples of
`4√P` (since `s^{n−k} = (4X_1)^{n−k}P^{(n−k−1)/2}√P`), the terms with `k` odd are integer multiples of `√Q`; so
`α^n = 4X_n√P + u_n√Q` with `u_n = u_1·L_n`, `L_n := Σ_{k odd} C(n,k) s^{n−k} r^{k−1}`, an integer polynomial in
`s² = 16PX_1²` and `r² = Qu_1²`.
(c) *`L_n ≡ n (mod 7)`.* `7 | Q` gives `r² ≡ 0` and `s² = 1 + r² ≡ 1 (mod 7)`; every term with `k ≥ 3` contains `r²`,
and the `k = 1` term is `n·s^{n−1} = n(s²)^{(n−1)/2} ≡ n`.
(d) *`L_7 ≡ 7 (mod 49)`.* `L_7 = 7s⁶ + 35s⁴r² + 21s²r⁴ + r⁶`; `v_7(35r²) ≥ 2`, `v_7(21r⁴) ≥ 3`, `v_7(r⁶) ≥ 3`, and
`7s⁶ ≡ 7 (mod 49)`. Also `L_7 ≥ 7s⁶ > 7` (`s² ≥ 16`).
(e) *Multiplicativity.* For odd `m, n`, `α^n` is again a solution with the same `(P,Q)`, and
`u_{mn} = u_n·L_m(α^n)`, so `L_{mn}(α) = L_n(α)·L_m(α^n)`. Each `L_m(·)` is `> 1` for `m ≥ 3` (it is `≥ m s^{m−1}`).
(f) Suppose `u_n = 7^b`, `n ≥ 3`. Then `u_1 | u_n` is a power of 7 and `L_n = 7^k`, `k ≥ 1`. Write `n = 7^r n'`, `7 ∤ n'`.
`L_{n'}(α) | L_n(α)` and `L_{n'} ≡ n' ≢ 0 (mod 7)` by (c), so `L_{n'} = 1`, `n' = 1`. Then
`L_{7^r}(α) = ∏_{i<r} L_7(α^{7^i})` and by (d) (applied to the solutions `α^{7^i}`, for which still `7 | Q`) each factor is
`7·w_i` with `w_i > 1`, `7 ∤ w_i`. So `L_n` is not a power of 7. ∎

**Corollary 1.2 (PROVED; b is a function of the field data).** A fibre certificate of level `L` is determined by
`(a, c', δ, P_1)` (with `P_1 | M`), and then `7^b = u_1(P,Q)` is the `√Q`-coefficient of the minimal solution, i.e.
`α² = ν_0` is the generator of `G = {A+4B√d : A²−16dB²=1}`. Since `G` has index `k ∈ {1,2,4}` in the norm-one units
of `ℤ[√d]` (the image of a unit in `(ℤ[√d]/4)^×`, a group of order 8, has order dividing 4 modulo `{±1}+4ℤ[√d]`),
**the certificate unit is `ε_f^k`, `k ∈ {1,2,4}`, with `ε_f` the fundamental norm-one unit of `ℤ[√d]`.**
This proves (and sharpens) TYPEI4 Obs 1.5 ("`m=1` in all examples"): `m ∈ {1,2,4}` always.
Consequently the d-graded engine `typei4_dgraded.py` (which tests `ε_f^m`, `m ≤ mmax`) is **complete for all `b`** as
soon as `mmax ≥ 4`.
*Proof.* Lemma 1.1 (hypotheses: `7 | Q` as `a ≥ 1`; `d` is not a square as `v_7(d) = a` is odd; `u = 7^b` odd).
The certificate is recovered from `(a,c',δ,P_1)` and `(X,u)` by TYPEI4 Prop 1.2, and `(X,u) = (X_1,u_1)`. ∎

**Computation 1.3 (CERTIFIED once replayed).** `typei4_dgraded.py 5 24 3000 6` (TYPEI4 replay) therefore shows:
*for `5 ≤ L ≤ 24` and `c_oδ ≤ 3000`, the only fibre certificates, for any `b`, are the 8 listed hits (all `L ≥ 11`).*
In particular **no fibre certificate at `L ∈ {7,…,10}` with `c_oδ ≤ 3000`, for any `v_7(k)`.**

*Remark 1.4 (what Lemma 1.1 does not do).* It does not bound `b` at fixed `L`: it only says that `b` is read off from
the unit of `d = c_o(c_oδ² + T)`. Assessment 4.2(c) of TYPEI4 (BHV, `n ≤ 30`) is superseded by `n = 1` (elementary).

## 2. Plan of the remaining sections (working notes)

* §3: a d-graded engine that needs no big integers: the generator `ν_0 = ε_f^k` of `G` computed **modulo `2^64` and
  `7^22`** along the continued fraction of `√d`; Lemma 1.1 makes "certificate ⟺ `ν_0 = α²` of the Legendre shape with
  `u = 7^b`" exact, and the 7-adic valuations `v_7(B) = b`, `v_7(A−1) = a+2b` are read off modulo `7^22`.
* §4: why linear forms in logarithms do not close the tower at fixed `L` (b is a function of the unit of a
  two-parameter family of fields; Lemma 3.6 of TYPEI4 = small-unit regime).
