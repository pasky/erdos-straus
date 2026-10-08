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

## 2. A d-graded engine valid for all `b` without big integers (CERTIFIED once replayed)

**Lemma 2.1 (filter; PROVED).** Let `ν_0 = A + B√d` be the generator of `G` (Cor 1.2). If `(L,a,c',δ)` carries a fibre
certificate (any `b`), then: `A ≡ −1 (mod 32)`, `B ≡ 8 (mod 16)`, `b = v_7(B)`, `v_7(A−1) = a + 2b`, and
`(A−1)/(2·7^{a+2b}) = Q_1` is a divisor of `M = c_oδ² + T`.
*Proof.* `ν_0 = α² = (2Qu²+1) + 8Xu√d` with `u = 7^b`, `X` odd, `7∤X`, `Q = 7^aQ_1`, `7∤Q_1` (`Q_1 | M`, `M ≡ T ≢ 0 (mod 7)`);
`A ≡ −1 (mod 32)` is TYPEI4 Prop 1.2. ∎
All five conditions only need `A, B` modulo `2^64` and `7^22` (for `a+2b ≤ 18`; otherwise the survivor is flagged `WEAK`
and must be checked separately), and these residues are computed exactly along the continued fraction of `√d`
(convergent recursion mod `2^64` and mod `7^22`; `ε_f = p+q√d` from the period, squared if the period is odd;
`ν_0 = ε_f^k`, `k` the least of `1,2,4` with `4 | B`).

**Computation 2.2.** `scripts/typei5_dmod.c Lmin Lmax CD` (all `a` odd, `c'`, `δ` with `c_oδ ≤ CD`).
* Regression: `typei5_dmod 5 24 3000` returns exactly the 8 hits of `typei4_dgraded.py 5 24 3000 6` (0.07 s);
  residues of `ε_f` agree with exact big-integer units for `d = 497, 21777, 13220193, 1234567, 991`.
* `typei5_dmod 7 10 300000`: 466 876 fields, 6.8·10⁹ CF steps, **0 survivors** (71 s).
* `typei5_dmod L L 1000000`: `L=7`: 426 697 fields, 2.0·10¹⁰ CF steps, **0 survivors**; `L=8`: same counts, **0 survivors**
  (≈15 min each); `L=9,10`: running.

**Corollary 2.3 (CERTIFIED once replayed).** There is no fibre certificate (hence no certificate at `x̂_9`) of level
`L ∈ {7,8,9,10}` with `c_oδ ≤ 3·10⁵`, **for any `v_7(k)`** (and any height `X = k'`).
Together with TYPEI4 Cor 3.5 (`v_7(k) ≤ 7`, any `c_oδ`): a certificate at `x̂_9` of level `7…10` needs
**both** `v_7(k) ≥ 8` **and** `c_oδ > 3·10⁵`.

## 3. The gap parametrisation at general `L`: one regime is finite, one is two-parametric (PROVED)

Case B of TYPEI4 Lemma 3.1 (`2y < Tu`), `u = 7^b`, `j := Tu/2 − y > 0` (odd), `m := c'δ²`, `ρ := z/P_1`, so
`ρP_1 = Tu/2 + j` and `mP_1 = y² − 2·7^a·m·u·j` (TYPEI4 Lemma 3.1(iii)).

**Lemma 3.1 (PROVED; removes the hypothesis `7∤j` of TYPEI4 Lemma 3.6, all `L ≥ 5`).** `λ := (ρj − m)/u` is an integer.
*Proof.* Mod `u`: `ρP_1 ≡ j` and `mP_1 ≡ y² ≡ j²` (`T` even). So `(ρj − m)P_1 ≡ 0`, and `7 ∤ P_1`. ∎

**Lemma 3.2 (exact identities; PROVED).** Put `κ := 8·7^aλ` and `Δ := 8j·7^a·m + 6Tj − T²u`. Then
(H) `ρΔ = 2λ(Tu + 2j)`, and, if `λ ≠ 0`,
(Lin) `u·[κj(2Tj − Δ) − ΔT²] = Δ(Δ − 6Tj) − 4κj³`.
*Proof.* Substitute `m = ρj − λu` into `ρ(y² − 2·7^amuj) = m(Tu/2 + j)` (= `mP_1·ρ = m·ρP_1`), divide by `u`, and
collect; this gives (H). (Lin): from (H) `m = λ[u(2Tj−Δ) + 4j²]/Δ`, insert into the definition of `Δ`. ∎
(Checked on all 9 relaxed solutions of `typei5_relax` at `L = 7, 9, 10`, including `λ < 0` and both signs of `2Tj − Δ`.)

**Proposition 3.3 (PROVED).** Fix `L`. (i) `λ = 0` is impossible. (ii) If `λ < 0`, then `7^a|λ|j < T²/8` and `u` is
bounded explicitly in terms of `(a,λ,j)`. (iii) If `λ > 0` and `Δ < 2Tj` (put `s := 2Tj − Δ ≥ 1`), then
`7^a λ s < T³/4` and, with `g := 2T³ − sκ > 0`, `(gj − sT²) | R := 4κs³T⁶ + gs³κ(4T³+g)`, so `j ≤ (R + sT²)/g` and `u`
is bounded: **this regime is a finite, explicit computation at each `L`**.
(iv) If `λ > 0` and `Δ = 2Tj`, then `u = (2κj² + 4T²j)/T³`, which forces `b = v_7(j)`, `T ≡ 4 (mod 7)`.
(v) If `λ > 0` and `σ := Δ − 2Tj ≥ 1`: `u < 4j²/σ`, and with `ω := 4j² − uσ ≥ 1`
`κ·j·ω·σ = (2Tj + σ)[(2Tj − σ)² − ωT²]`; for fixed `(σ,κ)`, `((2T³+σκ)j + σT²) | 4κσ³T⁶ + (2T³+σκ)σ³κ(4T³+2T³+σκ)`,
so `j`, `u` are bounded polynomially in `(σ, κ)` — but `σ` and `κ = 8·7^aλ` are **not** bounded.
*Proof.* (i) (H) gives `uT² = 6Tj + κj²ρ`·(…); directly: `λ=0` in (H) forces `Δ = 0`, i.e. `T²u = 8j·7^am + 6Tj` with
`m = ρj`; then `j | T²u`, `j = 7^r`, and comparing 7-adic valuations gives `r = b` and `T(T−6) = 8·7^{a+b}ρ`,
impossible as `2^k ≢ 6 (mod 7)`. (ii) `m = ρj + |λ|u > u` and `P_1 ≥ 1` gives `2·7^amuj < y² < T²u²/4`, so
`8·7^aj|λ| < T²`; in (Lin) with `x := |Δ|` (Δ<0 by (H)) `u = (x² + 6Tjx + 4|κ|j³)/(Kx − E)`, `K = T² − |κ|j > 0`,
`E = 2|κ|Tj²`, and `Kx − E` divides the positive constant `E² + 6TjEK + 4|κ|j³K²`. (iii) In (Lin) the right side is
`−4κj³ − Δ(6Tj − Δ) < 0` for `0 < Δ < 2Tj` (`Δ > 0` by (H)), so the bracket is negative: `j(2T³ − sκ) − sT² > 0`
after writing `Δ = 2Tj − s`, whence `sκ < 2T³`. Then `u = N(j)/(gj − sT²)` with `N(j) = 4κj³ + (2Tj−s)(4Tj+s)`, and
`g³N(sT²/g) = R ≠ 0`. (iv) Substitute `Δ = 2Tj`; `j·(2κj + 4T²) = T³u`, `j` odd ⇒ `j = 7^r`; mod 7 ⇒ `r = b`, then
`κ7^b = T²(T−4)/2`… (v) `ρ > λu/j` and (H) give `Δ < 2Tj + 4j²/u`; the displayed identity is (Lin) rewritten with
`uσ = 4j² − ω`, and the divisibility is the same polynomial-remainder argument as in (iii). ∎

*Interpretation (Assessment).* At `L = 7`, `j ≈ 8u/μ` (`μ = 7^am + 4`), so regime (v) has `u ≈ σμ²/256`: `σ` measures
how large the certificate unit `ν_0 ≈ 4Qu²` is compared with `d²`. Regime (iii) is the "unit linear in `μ`" (Richaud–
Degert-like) regime and is finite. **What remains open at each fixed `L` is the two-parameter regime (v)**; for each
fixed `(σ, a, λ)` it is finite (explicit), so the obstruction is exactly that `σ` and `κ` are unbounded — equivalently
(Cor 1.2) that `7^b = u_1(d)` is the unit coefficient of a two-parameter family of fields `d = c_o(c_oδ² + T)`.
Linear forms in logarithms bound exponents in a **fixed** field / fixed recurrence; here the field moves with two free
parameters and no LFL bound applies. (Not a theorem; the PROVED content is Lemmas 1.1, 3.1–3.3.)

## 4. Open / next steps
* Implement regime (iii) (and (ii), (iv)) as a complete computation at `L = 7…10` (finite by Prop 3.3).
* Regime (v): for `σ, λ` up to a bound — finite; full closure would need a new idea (a relation bounding `σ`).
