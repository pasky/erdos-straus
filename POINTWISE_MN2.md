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
prefix + moments" appears circular, because the distortion of the natural prefix laws seems to
grow faster than ε(q_0) decays (§4, heuristic Assessment + data; not proved — wording softened by
reviewer R74 D3). (iv) The exact missing input
(§5).

## 0. What has to be shown

ADM_m(K, Q_0) (MN §5): the prefixed admissible unit process (AUP) does not die and has per-prime
drift `Λ(ℓ) = ∏_{steps at ℓ}(1−f)^{−1} ≤ K` for every `ℓ ≤ Y`, with probability ≥ 7/8,
uniformly in T. MN Thm 5.1: ADM_m ⇒ Haar exponent 3 and `W_m(p) ≥ exp(c(log p)^{1/4}(log log p)^{−B})` i.o.

## 1. Three structural facts

**Lemma 1.1 (positive probability suffices; PROVED as a modification of MN Thm 5.1's implication, which
is PROVED modulo the inputs of OMEGA13 Thm 3.4/5.1 — label clarified, applied by reviewer R74 D6).** In MN Thm 5.1 the hypothesis
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
(v) *Dyadic sum.* With `X = X_0 2^i`, `log X ≪ log q + i`, and
`Σ_{i≥0}2^{−iσ}(log q + i)^{3^j−2} ≪ σ^{−1}(log q)^{3^j−2} + σ^{−(3^j−1)} ≪ (log q)^{3^j−1}`
(corrected display, applied by reviewer R74 D7).
(vi) *Short range* `M_1 ≤ X_0 := 2m(c_0(6qm)^{1/2}+1) ≪ q^{1/2}`: here `A ≪ q^{3/2}`, so
`τ(A²)^jτ(M_1)^{j−1} ≪_ε q^{ε}`, and `Σ_{M_1|L(q)}K_1^{ω(M_1)}/φ(M_1) ≤ ∏_{p<q}(1+K_1Σ_b 1/φ(p^b)) ≪ (log q)^{2K_1}`;
absorb `(log q)^{2K_1}` into `q^ε`.
The Y-smooth variant: same proof with `σ := min(1/log Y, ε_0/2)` and `p < Y`. ∎

*Why Rankin is needed.* Without the weight `(M_1/X)^σ` each dyadic block contributes
`≍ (log X)/q`-size terms and the sum over the `≍ log L(q) ≍ q` blocks is not uniform; NT/Henriot
see the smoothness of `M_1` only through the Euler factor, not through Dickman decay.

## 3. After any prefix, the rest of ADM costs only the prefix distortion

Fix `θ ∈ (0,1)`, `K := (1−θ)^{−2}`, `q_0 ≥ 8`, a prefix law ν on hard classes mod `Q_0 = Q(q_0)`
with density `≤ C_ν`, and run stage A then stage B, stopped (MN Thm 5.1) before any step that
would make some `Λ(ℓ) > K`. For a prime ℓ let `a_ℓ` be its first post-prefix level
(`ℓ^{a_ℓ} ≤ q_0 < ℓ^{a_ℓ+1}`). A step at `(ℓ,a)` is **bad** if `a ∈ {a_ℓ, a_ℓ+1}` and `Y > θN`,
or `a ≥ a_ℓ+2` and `Y ≥ 1` (Y as in Lemma 1.3).

**Theorem 3.1 (PROVED modulo (H) and MN Thm 5.1(a),(d)).** For every `ε > 0` there is `c_1 = c_1(m,θ,ε)`
(not explicit: it contains the constants of (H), which are effective in principle but not given in
the source — "ineffective" corrected, applied by reviewer R74 D2) such that, uniformly in large T,

```
P(the process dies or is stopped)  ≤  P(some step is bad)  ≤  C_ν·( c_1 q_0^{−1/2+ε} + o_{T→∞}(1) ).
```

Consequently, if `C_ν c_1 q_0^{−1/2+ε} ≤ 1/4` for some admissible `(q_0,ν)`, then ADM_m(K, Q(q_0))
holds with success probability ≥ 1/2 (enough by Lemma 1.1), `K = (1−θ)^{−2}` (e.g. `K = 4`).

*Proof.* *No bad step ⇒ success.* Death is `f = 1 > θ`. If no step is bad then every ℓ has at most
two post-prefix levels with `0 < f ≤ θ` and `f = 0` elsewhere (Lemma 1.3), so `Λ(ℓ) ≤ K` and the
stopping rule never fires. So it suffices to bound `Σ_steps P(bad ∧ alive)`.
*First moments.* Let E be completed at a step at `(ℓ,a)` and `E^-` its restriction to `M/ℓ`
(`M_{E^-} = M_1ℓ^a`). On "alive", `1[E^- consistent] = p(E^-) ≤ p(E^-)Ψ(E^-)`, and
`Σ p Ψ` is a supermartingale up to the stopping time (MN Thm 5.1(a)); optional stopping
[reviewer R74 D5: MN Thm 5.1(a),(d) are stated for atoms, but their per-event computation uses
atom-ness only for `p_new = 0` at completed atoms (an inequality in the safe direction), so `p(F)Ψ(F)`
and the pair potential are supermartingales for every unit-class event F on quarantined
coordinates, in particular for the non-atom restrictions `E^-`] at the
(stopping) time of the step and the prefix bound give
`E[1[E^- cons]·1_alive] ≤ C_ν K^{ω(M_1)+1}/φ(M_1ℓ^a)`. Summing over `D | A²` and over `M_1`:
`E[Y·1_alive] ≤ C_ν K S_1(q)/φ(ℓ^a)` (Lemma 2.1 with `K_1 = K`; in stage B use the Y-smooth
variant, since an adaptive step may complete atoms with any revealed, hence Y-smooth, cofactor).
*Second moment at a = 0.* For `E, E'` completed at the same level-0 step,
`E[1[E^- cons]1[E'^- cons]1_alive] ≤ C_ν K^{ω(M_1)+ω(M_1')}φ(g)/(φ(M_1)φ(M_1'))`,
`g = gcd(M_1,M_1')` — this is O13 Lemma 3.2(d)'s pair potential with caps (MN Thm 5.1(d)): just
before the step both restrictions are fully revealed, so `Π = 1[both consistent]`, and
`Π_0^{Haar} ≤ φ(g)/(φ(M_1)φ(M_1'))`. Write `M_1 = gu`; `1/(φ(g)φ(u)) ≤ (M_1/φ(M_1))/φ(M_1)`,
`τ(A²)τ(A'²) ≤ (τ(A²)²+τ(A'²)²)/2`, `Σ_{u'|L(q)}K^{ω(u')}/φ(u') ≪ (log q)^{2K}`,
`Σ_{g|M_1}K^{ω(g)} ≤ τ(M_1)K^{ω(M_1)}`. Hence
`E[Y²1_alive] ≪ C_ν(log ℓ)^{2K}S_2(ℓ)` with `K_1 = 4K²`.
*Bad probabilities.* (a) `a = 0`, `ℓ > q_0`: Chebyshev,
`P ≤ C_ν(log ℓ)^{2K}S_2(ℓ)/(θ(ℓ−1))² ≪ C_ν ℓ^{−2+ε}`.
(b) `a ∈ {a_ℓ, a_ℓ+1}`, `a ≥ 1` (so `q = ℓ^{a+1} > q_0` with `a ≥ 1`): Markov,
`P ≤ C_ν K S_1(q)/(θℓφ(ℓ^a)) ≪ C_ν q^{−1+ε}`; the number of such q in `(x,2x]` is `≪ x^{1/2}`, so the
sum over `q > q_0` is `≪ C_ν q_0^{−1/2+ε}`.
(c) `a ≥ a_ℓ+2`: `P(Y ≥ 1) ≤ C_ν K S_1(q)/φ(ℓ^a) ≪ C_ν q^{ε}ℓ^{−a}`. If `ℓ > q_0` then `a ≥ 2`
and the sum over ℓ, a is `≪ C_ν q_0^{−1+2ε}`; if `ℓ ≤ q_0` then `ℓ^a ≥ ℓ^{a_ℓ+2} > ℓq_0`, and the sum
over a (geometric) and `ℓ ≤ q_0` is `≪ C_ν q_0^{−1+4ε}` (`Σ_{ℓ≤q_0}ℓ^{−1+2ε} ≪ q_0^{2ε}`; corrected,
applied by reviewer R74 D8).
(d) Stage B steps have `q > Z`; (a)–(c) with the Y-smooth variant give
`≪ C_ν(log Y)^{C}Y^{ε}Z^{−1/2+ε} = o(1)` as `Z = 𝓛³(log𝓛)^B → ∞`, `log Y ≍ log 𝓛`, provided
`ε < 3/(2(C_K+4))` (the `(qY)^ε` of the Y-smooth variant; added by reviewer R74 D8). ∎

*Remark (the level count).* "Two levels with `Y ≤ θN`, then `Y = 0`" is forced: for `ℓ > q_0` the
level-1 first moment `≍ (log ℓ)^C/ℓ` is not summable over primes, so level 1 must be allowed to
forbid; level 0 needs the second moment for the same reason (MN §6 (ii)).

## 4. Why Theorem 3.1 does not close ADM_m: the prefix-distortion circularity (Assessment)

Theorem 3.1 reduces ADM_m to finding prefixes with `C_ν(q_0)·c_1 q_0^{−1/2+ε} ≤ 1/4`. Two facts
block the plan of the brief ("small primes by a fixed certified prefix, late primes by moments"):

1. **`c_1` is not explicit.** It contains the constants `c_0` and `≪` of (H) (effective in
   principle, but not given in the source). So no *explicit* `q_0` is available, and no finite
   computation based on the literature as it stands certifies that a given `q_0` is large enough
   (wording corrected, applied by reviewer R74 D2); and for any fixed explicit prefix the
   steps between `q_0` and the (unknown) range where Theorem 3.1's bound is `< 1` are not controlled
   by anything proved here. (Explicit Rankin + elementary divisor-in-AP bounds could replace (H) at
   the cost of enormous constants; the resulting `q_0` would be far beyond any certifiable prefix.)
2. **For the three natural prefix laws below, the distortion appears to grow faster than
   `q_0^{1/2}` (heuristic + data for `q_0 ≤ 19`; NOT proved, and not claimed for every prefix
   law — restricted by reviewer R74 D3).**
   [Reviewer R74 D4: the threshold `q_0^{1/2}` is an artefact of using Markov in case (b) of
   Thm 3.1's proof. An unverified reviewer sketch suggests that a second moment at levels `a ≥ 1`
   (shared `ℓ^a` part in the pair bound) gives `≪ C_ν q_0^{−1+ε}` there, so the relevant criterion
   would be `C_ν` vs `q_0^{1−ε}`; against `q_0^{−1}/δ` the data below grow only slowly (m = 6:
   0.26 → 0.34) and are inconclusive. The circularity therefore rests on the unproved heuristic
   `log(1/δ) ≍ (log q_0)³`.]
   * Uniform law on the hard set: `C_ν = 1/δ_m(Q(q_0))`. Data (`scripts/mn2_delta.py`, exact):

     | m | q_0 = 8 | 9 | 11 | 13 | 16 | 17 | 19 |
     |---|---|---|---|---|---|---|---|
     | 5: `1/δ` | 4 | 8 | 10.9 | 19.2 | 19.2 | 31.6 | 61.1 |
     | 5: `q_0^{−1/2}/δ` | 1.41 | 2.67 | 3.29 | 5.34 | 4.81 | 7.66 | 14.0 |
     | 7: `1/δ` | 3.2 | — | 4.10 | 7.09 | — | 10.6 | 14.4 |
     | 6: `1/δ` | — | — | 2.86 | 3.42 | — | 5.06 | 6.48 |

     (`δ_5(Q(8)) = 1/4` reproduces MN's `|H_5(840)| = 48/192`; for m = 6 the primes 2, 3 never divide M.)
     Heuristically `log(1/δ_m(Q(q_0))) ≍` the Haar mass of the atoms with `M | Q(q_0)`, which by
     Lemma-2.1-type sums is `≍ (log q_0)^3`, so `1/δ` grows faster than every power of `q_0`.
     (Not proved: it needs a lower bound for `1/δ`, i.e. an upper bound for the hard density.)
   * A single hard class (e.g. `r ≡ 1`): `C_ν = φ(Q(q_0)) = e^{(1+o(1))q_0}`.
   * The AUP itself as prefix: its distortion is `∏_{ℓ|M}Λ(ℓ)` along the path — bounding it is
     ADM_m on the range `≤ q_0` again.

So the density bound `E_ν[p_0(E)] ≤ C_ν P_H(E)` (MN's `1/δ_0`) is the lossy step: what Theorem 3.1's
proof really uses is `E_ν[1[E^- consistent]]` summed over the completed atoms of each later step.
**This is an assessment of a proof method, not an obstruction to ADM_m** (MN §6 numerics: no
deaths with the 2,3-adic prefix, max drift ≈ 4).

## 5. The exact missing input

For a prefix law ν on hard classes mod `Q(q_0)` and `q ∈ 𝒫`, `q > q_0`, let `S_j^ν(q)` be `S_j(q)`
with each term `τ(A²)^j(…)/φ(M_1)` replaced by its ν-weighted version
`Σ_{D|A²} E_ν[1[−mD ≡ r (mod gcd(M_1ℓ^a, Q_0))]]·φ(gcd(M_1ℓ^a,Q_0))/φ(M_1)·(…)`
(and the analogous pair sum for `j = 2`). The proof of Theorem 3.1 gives verbatim:

**Proposition 5.1 (PROVED modulo (H)).** If for some family `ν = ν_{q_0}` of hard prefix laws
`Σ_{q>q_0} [ S_2^ν(q)(log q)^{2K}/q² ·1[q prime] + S_1^ν(q)/q ·1[q not prime] + (the level-(≥a_ℓ+2) terms) ] → 0`
as `q_0 → ∞` (hypothesis **SI**; precise form, supplied by reviewer R74 D9 since the bracketed
terms above were left unspecified: with `E^ν_1(q) := Σ_{E ∈ C_q} K^{ω(M_1ℓ^a)}E_ν[p_0(E^-)]` and
`E^ν_2(ℓ) := Σ_{E,E' ∈ C_ℓ} K^{ω(M_1)+ω(M_1')}E_ν[Π_0(E^-,E'^-)]`, SI is
`Σ_{ℓ>q_0} E^ν_2(ℓ)/(θ(ℓ−1))² + Σ_{(b)} E^ν_1(q)/(θℓ) + Σ_{(c)} E^ν_1(q) → 0`, the three sums running
over the steps of cases (a), (b), (c) of Thm 3.1's proof; these are exactly the quantities that
proof bounds by `C_ν·(…)`), then ADM_m(K = (1−θ)^{−2}, Q(q_0)) holds for some `q_0`, with
success probability ≥ 1/2; with Lemma 1.1 and MN Thm 5.1 this gives
`W_m(p) ≥ exp(c(log p)^{1/4}(log log p)^{−B})` for infinitely many primes p, Type-II-hard modulo their
quarantine modulus, modulo (G), NT/(H), OMEGA10 Thm 3.4 and SI.

*Candidate: the class of one.* For `ν = δ_1` (`r ≡ 1 mod Q(q_0)`, hard by TRANSFER Lemma 5.1(ii);
no death and no drift in the prefix) the weight of a completed atom is
`φ(s)·1[s | mD+1]`, `s = gcd(M_1, Q_0)`. With `D = da²`, `A = dab` (O12 Lemma 2.1, `4 ↦ m`) one has
`s | mD+1 ⟺ s | a+b` and then `s | P := ma²d+1`; writing `b = cs − a`, `f = P/s`,
`qM_1/s = mdac − f`. Summed over `s | Q_0` the inflation becomes `τ(P_{q_0})` — the number of
`q_0`-smooth divisors of `P = ma²d+1` — exactly the smooth inflation of O13 Hypothesis M(Y), but
now inside the T-uniform completed-atom sums. Heuristically its mean is `(log q_0)^{O(1)}`
(Euler factor `∏_{p≤q_0}(1+ρ_P(p)/p)`), which would give SI for `ν = δ_1`. Proving it needs (H) in
each of the variables a, c, d with a regime split (largest variable as summation variable). Status:
**CONJECTURE (expected provable; not done).**

## 6. Status

| item | statement | label |
|---|---|---|
| Lemma 1.1 | MN Thm 5.1 needs only success probability ≥ s_0 > 0; any prefix law with bounded density | PROVED |
| Lemma 1.2 | increasing-order stage A: step laws are T-independent | PROVED |
| Lemma 1.3 | `f ≤ Y/N` = mass of completed atoms | PROVED |
| Lemma 2.1 | T-uniform completed-atom sums `S_j(q) ≪ q^ε + (log q)^{C_j}` | PROVED modulo (H) |
| Thm 3.1 | after any prefix: `P(fail) ≤ C_ν(c_1q_0^{−1/2+ε} + o(1))` | PROVED modulo (H), MN Thm 5.1(a),(d) (c_1 not explicit) |
| §4 | certified-prefix + moments plan looks circular (heuristic; threshold method-dependent, R74 D3/D4); `1/δ_m(Q(q_0))` data | Assessment (heuristic) + EVIDENCE (exact counts, independently reproduced R74) |
| Prop 5.1 | SI ⇒ ADM_m ⇒ exponent 1/4 for W_m | implication SI ⇒ ADM_m PROVED modulo (H); W_m consequence CONDITIONAL on SI, (G), NT/(H), OMEGA10 Thm 3.4 (R74 D1) |
| SI for class-one prefix | completed-atom smooth inflation `τ(P_{q_0})` | CONJECTURE |
| ADM_m | — | still OPEN (CONDITIONAL on SI) |

## Replay

```
cd scripts
(ulimit -v 8000000; timeout 1500 uv run python mn2_delta.py 5 8 9 11 13 16 17 19)   # §4 table, m=5
(ulimit -v 8000000; timeout 1500 uv run python mn2_delta.py 7 8 11 13 17 19)        # m=7
(ulimit -v 8000000; timeout 900  uv run python mn2_delta.py 6 11 13 17 19)          # m=6
```
