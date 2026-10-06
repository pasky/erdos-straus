# POINTWISE_MN2 — towards ADM_m (task O74, branch `side-agent/adm-m`)

Status: work in progress. Labels as in DISCOVERIES.md. Notation as in POINTWISE_MN.md (MN) and
POINTWISE_OMEGA13.md (O13). Fixed `m ≥ 4`, `m ≢ 0 (4)` (main case m = 5). Atoms `(M,D)`,
`M ≡ −1 (m)`, `A = (M+1)/m`, `D | A²`, event `n ≡ −mD (mod M)`. Constants may depend on m.

**Summary of this checkpoint.** (i) Three small structural facts that make ADM_m a cleaner
object (§1): positive success probability suffices; a fixed increasing order on the small prime
powers makes the forbidden fractions T-independent; the forbidden fraction is bounded by the mass of
the atoms completed at that step. (ii) A T-uniform bound for the completed-atom sums (§2, Lemma 2.1,
PROVED modulo Henriot's uniform Nair–Tenenbaum bound), giving: *after any prefix, the probability
that some later step has a large forbidden fraction is at most (prefix distortion) × ε(q_0), with
ε(q_0) → 0* (§3, Theorem 3.1). (iii) Why this does not close ADM_m: the plan "certified finite
prefix + moments" is circular, because the distortion of every prefix law that is controlled
pointwise grows faster than ε(q_0) decays (§4, Assessment + data). (iv) The exact missing input
(§5).

## 0. What has to be shown

ADM_m(K, Q_0) (MN §5): the prefixed admissible unit process (AUP) does not die and has per-prime
drift `Λ(ℓ) = ∏_{steps at ℓ}(1−f)^{−1} ≤ K` for every `ℓ ≤ Y`, with probability ≥ 7/8,
uniformly in T. MN Thm 5.1: ADM_m ⇒ Haar exponent 3 and `W_m(p) ≥ exp(c(log p)^{1/4}(log log p)^{−B})` i.o.

## 1. Three structural facts

**Lemma 1.1 (positive probability suffices; PROVED).** In MN Thm 5.1 the hypothesis
"probability ≥ 7/8" can be replaced by "probability ≥ s_0" for any fixed `s_0 > 0`; the constants
of the conclusion change by factors depending on s_0 only. The prefix law may be any law ν on
Type-II-hard classes mod Q_0 with density `≤ C_ν` w.r.t. Haar on `(Z/Q_0)^×` (MN uses the uniform
law on `H_m(Q_0)`, `C_ν = 1/δ_0`; a single deterministic hard class has `C_ν = φ(Q_0)`).

*Proof.* In the proof of MN Thm 5.1 the four bad events are: failure (`Λ > K` or death), a heavy
late prime, `cost > x`, `S_res > x`. The last three are bounded for the *stopped* process (on
which `Ψ ≥ 1`), whose expectations `E_cost`, `E_S` are bounded by the supermartingale, by
`η^{−2}Σ_{ℓ>Y}B_2^K(ℓ) = o(1)` (Y = 𝓛^{C_K+4}), and by Markov with `x = 4E/s_0`. So all bad events
together have probability `≤ (1 − s_0) + o(1) + s_0/4 + s_0/4 < 1` for large T, and a good
realisation exists with `log Q ≤ 4E_cost/s_0`, `S_res ≤ 4E_S/s_0`. For the prefix: the only use is
`E_ν[p_0(E)] ≤ C_ν P_H(E)` and `E_ν[Π_0] ≤ C_ν Π_0^{Haar}`, both immediate from the density
bound (for pairs, Haar reveals inside the prefix are exact martingale steps for Π, as in R63 §T51). ∎

**Order.** Let `𝒫` be the set of prime powers `q = ℓ^{a+1}` (`a ≥ 0`, `ℓ ∤ m`; primes of m never
divide an M). *Stage A* reveals the level `r mod ℓ^{a+1}` for every `q ∈ 𝒫`, `q_0 < q ≤ Z`, in
increasing order of q, each by the AUP rule (uniform among the non-forbidden lifts). The prefix is
everything with `q ≤ q_0`: `Q_0 = Q(q_0) := lcm{q ∈ 𝒫 : q ≤ q_0}`. *Stage B* is MN's adaptive
threshold rule for the remaining levels with `ℓ ≤ Y`. With `Z = 𝓛³(log𝓛)^{B}` the forced cost
is `Σ_{q≤Z} log ℓ = ψ(Z) ≪ 𝓛³(log𝓛)^B`, inside MN Thm 5.1's budget; forced steps are ordinary
steps for the supermartingale (like O13's forced steps at 3, 5, 7).

For `q = ℓ^{a+1} ∈ 𝒫` let `L(q) := lcm{q' ∈ 𝒫 : q' < q, ℓ ∤ q'}` and
`C_q := {(M,D) atom : M = q·M_1, M_1 | L(q)}` — the atoms completed at the stage-A step q.

**Lemma 1.2 (T-independence; PROVED).** At a stage-A step `q`, an atom is completed iff it lies in
`C_q`. `C_q` is finite and `max M ≤ q L(q)`. Hence for `T ≥ T(q) := max_{q'≤q} q'L(q')` the joint
law of the prefix and of stage A up to q does not depend on T.

*Proof.* Completed at q means `v_ℓ(M) = a+1` and every other prime power `p^b ‖ M` already revealed,
i.e. `p^b < q` in the increasing order (or `p^b | Q_0`, also `< q`). That is `M/q | L(q)`. The
forbidden set at q is a function of the revealed digits and of `C_q` only. Induct on q. ∎

**Lemma 1.3 (completion bound; PROVED).** At a step at level `(ℓ,a)` with N fibre lifts
(`N = ℓ−1` if `a = 0`, `N = ℓ` if `a ≥ 1`, ℓ odd; `N ∈ {1,2}` at ℓ = 2), let `Y` be the number of
completed atoms consistent with r on their revealed part. Then `f ≤ Y/N = Σ_{E completed} p_i(E)`.

*Proof.* Each forbidden lift is the class of at least one completed consistent atom. For such an
atom all digits except the new one are revealed and consistent, and the new digit is uniform over
N lifts under the fibre measure, so `p_i(E) = 1/N`; inconsistent completed atoms have `p_i = 0`. ∎

## 2. Completed-atom sums are T-uniform (Rankin + Henriot)

**Input (H) (Henriot, arXiv:1102.1643, Thm 5 / Cor 1; `sources/henriot-1102.1643.pdf` pp. 6–7).**
Let `Q_1, Q_2 ∈ Z[X]` with `Q = Q_1Q_2` primitive, of degree g, with irreducible factors `R_h` and
`D*` = discriminant of `Q* = ∏R_h`. Let `0<α,δ<1`, `A_0,B_0 ≥ 1`, `0<ε_0<α/(50g(g+1/δ))`,
`F ∈ M_2(A_0,B_0,ε_0)`. Uniformly in `x ≥ c_0‖Q‖^δ`, `x^α ≤ y ≤ x`:
`Σ_{x<t≤x+y}F(|Q_1(t)|,|Q_2(t)|) ≪ Δ_{D*}·y∏_{g<p≤x}(1−ρ(p)/p)·Σ_{n_1n_2≤x}F(n_1,n_2)ρ_{R_1}(n_1)ρ_{R_2}(n_2)/(n_1n_2)`,
with `c_0` and the implied constant depending only on `g, α, δ, A_0, B_0` (**not** on the
coefficients of Q). This is the uniform version of the NT input already used by O13 Lemma 3.3.
The constants are not explicit in the source.

For `q = ℓ^{a+1} ∈ 𝒫`, `j ∈ {1,2}`, `K_1 ≥ 1` put (`A = (qM_1+1)/m`)

```
S_j(q) := Σ_{M_1 | L(q), qM_1 ≡ −1 (m)}  τ(A²)^j · τ(M_1)^{j−1} · K_1^{ω(M_1)} / φ(M_1).
```

**Lemma 2.1 (PROVED modulo (H)).** For every `ε > 0`:
`S_j(q) ≪_{m,j,K_1,ε} q^{ε} + (log q)^{C_j}`, `C_j := 3^j − 1 + e·2^{j−1}K_1`, uniformly in `q ∈ 𝒫`.
The same bound holds with `M_1 | L(q)` replaced by "`M_1` is Y-smooth, `ℓ ∤ M_1`" if `log q` is
replaced by `log Y` in the second term and by `log(qY)` in the q^ε-term (any `Y ≥ q`).

*Proof.* (i) *Linear forms.* As `ℓ ∤ m`, `qM_1 ≡ −1 (m)` means `M_1 = c_2 + mt` (`t ≥ 0`,
`1 ≤ c_2 ≤ m`, `qc_2 ≡ −1 (m)`), and then `A = qt + c_1`, `c_1 = (qc_2+1)/m ≤ q+1`. With
`Q_1 = qX + c_1`, `Q_2 = mX + c_2`: `qc_2 − mc_1 = −1`, so both are primitive, coprime,
`D* = (qc_2−mc_1)² = 1`, `Δ_{D*} = 1`, `‖Q‖ ≤ (2q+1)·2m`. For `p > 2`, `ρ(p) = 2` if `p ∤ qm`
and `ρ(p) ≤ 1` otherwise; `ρ_{R_h}(n) ≤ 1`.
(ii) *Rankin.* `M_1 | L(q)` iff `u_q(M_1) = 1`, where `u_q` is the multiplicative indicator of
"every `p^b ‖ n` has `p ≠ ℓ`, `p^b < q`". Put `σ := min(1/log q, ε_0/2)`. On a block
`X < M_1 ≤ 2X`: `u_q(M_1) ≤ u_q(M_1)(M_1/X)^σ` and `1/φ(M_1) ≤ (M_1/φ(M_1))/X`.
(iii) *The function.* `F(n_1,n_2) := τ(n_1²)^j f_2(n_2)`,
`f_2(n) := u_q(n)τ(n)^{j−1}K_1^{ω(n)}(n/φ(n))n^σ`. Multiplicative; `τ(p^{2b})^j ≤ 9^b`;
`f_2(p^b) ≤ 2^b·K_1·2·e^b` (as `p < q` ⇒ `p^σ ≤ e`); `f_2(n) ≪_{ε_0} n^{ε_0/2}n^σ ≤ n^{ε_0}`.
So `F ∈ M_2(A_0, B_0, ε_0)` with `A_0 = 4eK_1 + 9`, `B_0 = B_0(K_1,ε_0)`, independent of q. Take
`g = 2`, `α = δ = 1/2`, `ε_0 = 1/1001`.
(iv) *Block bound.* For `x ≥ c_0(6qm)^{1/2}`, (H) with `y = x` gives
`Σ_{x<t≤2x}F(Q_1(t),Q_2(t)) ≪ x(log x)^{−2}·Σ_{n_1≤x}τ(n_1²)^j/n_1·Σ_{n_2}f_2(n_2)/n_2`
`≪ x(log x)^{3^j−2}·∏_{p<q}(1 + e2^{j−1}K_1/(p−1) + O(p^{−3/2})) ≪ x(log x)^{3^j−2}(log q)^{e2^{j−1}K_1}`
(the factor `∏_{p|qm}(1−1/p)/(1−2/p) ≪_m 1` as `ω(q) = 1`). A block `X < M_1 ≤ 2X` is covered by
`O(1)` such t-blocks with `x ≍ X/m`, so its contribution to `S_j(q)` is
`≪ X^{−1−σ}·X(log X)^{3^j−2}(log q)^{e2^{j−1}K_1}`.
(v) *Dyadic sum.* `Σ_{i≥0}2^{−iσ}(i+1)^{3^j−2} ≪ σ^{−(3^j−1)} ≪ (log q)^{3^j−1}`.
(vi) *Short range* `M_1 ≤ X_0 := 2m(c_0(6qm)^{1/2}+1) ≪ q^{1/2}`: here `A ≪ q^{3/2}`, so
`τ(A²)^jτ(M_1)^{j−1} ≪_ε q^{ε}`, and `Σ_{M_1|L(q)}K_1^{ω(M_1)}/φ(M_1) ≤ ∏_{p<q}(1+K_1Σ_b 1/φ(p^b)) ≪ (log q)^{2K_1}`;
absorb `(log q)^{2K_1}` into `q^ε`.
The Y-smooth variant: same proof with `σ := min(1/log Y, ε_0/2)` and `p < Y`. ∎

*Why Rankin is needed.* Without the weight `(M_1/X)^σ` each dyadic block contributes
`≍ (log X)/q`-size terms and the sum over the `≍ log L(q) ≍ q` blocks is not uniform; NT/Henriot
see the smoothness of `M_1` only through the Euler factor, not through Dickman decay.
