# Haar → primes: where the local lemma does not transfer, and what replaces it

Task O30 (branch `haar-primes`). Labels follow the house rules (PROVED /
PROVED modulo a cited theorem / CONDITIONAL / Assessment / EVIDENCE). ES is
not solved here or anywhere; nothing below bears on whether `W(p)<∞`.
Notation: PO = `POINTWISE_OMEGA.md`, O2 = `POINTWISE_OMEGA2.md`, O3, O4
likewise; `𝓛=log T`, `log_j` = j-fold logarithm. A *system* is as in O3
Setting 5.0: independent coordinates `X_ℓ` (uniform on units mod
`ℓ^{e_ℓ}`, ℓ in a finite set 𝒫 of free primes), a finite family 𝓔 of
*events*, each a conjunction of vertex conditions `X_ℓ∈V` at the primes of
its support, `|supp E|≤k`; `F:=1[no event occurs]`; `S:=Σ_E P(E)`;
`w_ℓ:=Σ_{E∋ℓ}P(E)` (per-prime mass).

**Results at a glance (checkpoint 1; not yet reviewed).**

1. **Theorem 4.3** (PROVED modulo Thorner–Zaman and Elsholtz–Tao Prop
   1.4): `W(p) ≥ exp(c(log p)^{1/14})` for infinitely many Mordell-hard p;
   uniformly `log L_h(T) ≪ (log T)^{14}`. This replaces O4 Cor 3.1
   (`log W ≥ (1+o(1))log₂p·log₃p/log₄p`) and reaches the third target of
   O4 §4.4. The Haar side is `log(1/δ*) ≪ 𝓛^7/log𝓛` (O2 Thm 11.3); the prime side now
   costs its square.
2. **Theorem 4.4** (PROVED modulo Thorner–Zaman only): `log W(p) ≥
   (1/(2log2)−o(1))log₂p·log₃p` i.o. (was `log₂p·log₄p/log₅p`).
3. **Mechanism (§§3–4).** No push-down cascade, no levels, no codegree
   or hub hypothesis. The minorant is the Bazzi–Razborov–Wigderson
   one-sided ℓ² scheme (Lemma 3.1). Its error is an Efron–Stein tail
   (Thm 3.4), and a bit encoding plus Håstad's switching lemma (LMN)
   bounds that tail for every system of width `≤k` (Lemma 4.1).
4. **Diagnosis (§2; Assessment).** Heuristically, the Haar local lemma
   uses *suppression* (on good configurations, dense partial clusters are
   unlikely), while every alternating expansion (PO, O2–O4) *amplifies*
   on such clusters. That is where the codegree thresholds
   `(kL)^{−(i−1)}`, the worst-case circularity, and hence the `(k−1)!`
   cascade come from (§2.3). Lemma
   2.1 (locally minimal events) shows that the outer inclusion–exclusion
   is codegree-free; the trouble sits in the neighbourhood factors.
5. **Budget (§1, Lemma 1.1).** Within the old framework, `(log₂p)^{1+η}`
   needed `log K ≤ k^{O(1)}`; the new minorant has `log K = O(log 𝓛)`.
6. **Phase 2 (§6).** Exponent improved to 1/13 (superseded by
   POINTWISE_OMEGA9 Thm 2.2, 1/7; the 1/4 ceiling below concerns PO Thm 4.1
   only) (Thm 6.3:
   `W(p) ≥ exp(c(log p/log log p)^{1/13})`, mod TZ and ET). The cell
   bookkeeping is replaced by spectral norms (Lemma 6.1). §6.1 is a
   ledger of the losses. §6.4 proves that the q-ary decision-tree
   switching lemma fails even with small masses; the energy form ESW
   would give 1/11 only together with a q-ary ℓ¹ bound and a smaller
   quarantine (R30c M1; neither is proved). §6.5 (Assessment): for
   Brun/BRW-type minorants, routes through PO Thm 4.1 lose
   `log p ≳ S²·log z`; the present bookkeeping gives ≈1/9 with S only
   bounded by ET's S*, ≈1/6 with the observed S; the supported ceiling is
   1/4 (Prop 6.6: `log(1/δ) ≥ S1 ≫ 𝓛²`). (See POINTWISE_OMEGA9 for a
   transfer that avoids the square.)

Nothing here bears on whether `W(p)<∞`, i.e. on ES. The constants (Håstad,
TZ) are effective; no numerical instance is claimed.

## 0. Plan

1. §1: the exact budget. What size of minorant (ℓ¹ ratio, number of
   primes per modulus) a rate `log W ≥ (log₂p)^{1+η'}` needs, in terms of
   the number of levels k (PROVED bookkeeping).
2. §2: anatomy of the gap between the Haar local lemma (O2 Thm 11.3) and
   the prime-side minorants (O2–O4): the one step of each argument that
   has no counterpart in the other.
3. §3 onwards: constructions, and the obstruction.

## 1. The budget (PROVED bookkeeping on O4 Lemma 4.1)

O4 Lemma 4.1: if for Construction 2.0 (free primes `>y:=2T^{1/(k+1)}`,
supports `≤k`) one has a minorant as in PO Thm 4.1 with
`K=1+log(M_1/μ) ≤ e^X`, moduli on `≤e^X` free prime powers, and
`|Π∖Π_0|≤e^X`, then some hard `p>T` has `W(p)>T` and

```
log p ≤ C_1 e^X [2.52(k+1)T^{1/(k+1)} + e^{X+2}𝓛],   so   log₂p ≤ max(X + 𝓛/(k+1), 2X + log 𝓛) + O(log k).
```

**Lemma 1.1.** Fix `0<η<1/2`. Suppose that for all large T, with
`k:=⌈𝓛^η⌉`, a minorant as above exists with `X ≤ 𝓛^{1−η}/3`. Then for
infinitely many Mordell-hard p,

```
log W(p) ≥ (9/16)·(log₂p)^{1/(1−η)}.
```

(Within Lemma 4.1 alone, this is the only way the budget certifies the
rate: its bound is `≥𝓛/(k+1)` and `≥X`. This is a statement about the
certificate, not a lower bound for p. Review fix.)

*Proof.* With `X≤𝓛^{1−η}/3` and `k+1≥𝓛^η`: `log₂p ≤ 𝓛^{1−η}/3+𝓛^{1−η}+O(log𝓛)`
 `≤ (4/3+o(1))𝓛^{1−η}` for large T, i.e. `𝓛 ≥ ((3/4−o(1))log₂p)^{1/(1−η)}`,
and `(3/4)^{1/(1−η)} > 9/16` since `1/(1−η)<2`; `log W(p) ≥ 𝓛`. Distinct
T give distinct p (`p>T`). ∎

**Consequence (what the old budget needed; Assessment).** O4 Thm 1.1 gives
`X ≈ log K ≈ (k−1)!·(log Ŝ+O(k))`. For `X ≤ 𝓛^{1−η}` with `k ≍ 𝓛^η` one
needs

```
log K ≤ k^{A}·(log Ŝ)^{O(1)}   for some fixed A   (then η = 1/(A+2) works under ET, log Ŝ ≍ log 𝓛).
```

* An exponential `log K ≈ C^k log Ŝ` is **not** enough: it gives
  `k ≈ log𝓛/log C` and only `log W ≥ c·log₂p·log₃p`, i.e. it removes
  the `log₄p` of O4 Cor 3.1 but no more.
* The budget is otherwise generous: K itself may be as large as
  `exp(𝓛^{1−η})`, i.e. `log(M_1/μ)` and the number of primes per
  modulus may be `T^{o(1)}`. So the obstacle is never the *size* of the
  minorant in absolute terms; it is that the cascade puts the factorial
  in the **exponent of Ŝ**: `log(M_1/μ) ≈ Ŝ^{(k−1)!}` (O4 Thm 1.1), while
  the target needs `Ŝ^{poly(k)}`.

## 2. Anatomy of the gap (what does not transfer, exactly)

**2.1 The Haar argument** (O2 Thm 11.3, O4 Prop 5.1) uses two steps:
(i) iterated quarantine (O2 Lemma 11.2: per-prime masses `w_ℓ≤c_0`
after adding `|𝓑|≤kS*/c_0` primes); (ii) the local lemma with
`x_E=2P(E)`, which needs **only** `w_ℓ≤1/(8k)`: no codegree, no
truncation. Its proof bounds the conditional probabilities
`P(E | no earlier event)` and multiplies them.

**2.2 The prime side** needs a *fixed* function `B ≤ F` (pointwise on all
residue vectors) that is a short combination of congruence cells: few
primes per cell (log-modulus), small `log(M_1/μ)` (PO Thm 4.1). Step (i)
transfers verbatim (O4 Thm 2.1). Step (ii) does not: a fixed low-junta
function cannot condition on "no earlier event". Every minorant used so far
(PO Brun; O2 support-truncated Bonferroni `B*_L`; O3/O4 multilevel
compositions) is an alternating expansion of `F=∏_E(1−1_E)`.

**2.3 Three features of alternating expansions** (Assessment: a
heuristic diagnosis of the *worst-case* budgets of O2–O4, not
impossibility statements; review fix).

1. *Precision.* In the Poisson-like regime the order-j terms have total
   mass `≍S^j/j!` while `E F=δ≈e^{−Θ(S)}`; so terms up to order `≍S+log(1/δ)` are needed and each must be
   exact or approximated to absolute precision `≪δ e^{−S}`.
2. *Reuse.* An order-j term pins the `≤kj` vertices of j events. The error
   of a truncation at order L is a moment of the active-prime count, and
   a new event may reuse any i pinned vertices. Bounding this moment
   needs codegrees `Δ_O ≲ (kL)^{−(|O|−1)}` (O2 Lemma 10.2), and this is
   real for the truncated moment, not an artefact of its proof (O2 §11.4,
   reviewer example D12).
3. *Circularity.* Markov pushes of heavy sets at thresholds
   `(kL)^{−(i−1)}` add mass *at most* `Σ·(kL)^{i−1}·C` (Markov), and this
   is essentially attained at the first push (O2 Prop 11.4), while
   `L ≥ c·(mass)`. If the Markov bounds are saturated, a single family
   would need `S_fin ≳ S·(ckS_fin)^{i−1}`, which has no solution for large S
   (cf. O2 §10.5's warning: this concerns the worst-case budget only). Hence separate levels, each truncated at its own mass, and
   exponents multiply along `k→k−1→…→2`: `(k−1)!` (O4 Thm 1.1, §4.1).

**2.4 Where the local lemma differs** (heuristic). On a *good*
configuration, a partial cluster whose completions are many and weakly
correlated is exponentially unlikely (suppression). Completion mass alone
does not imply a factor `e^{−M}` (review counterexample: completions
`H∩Y∩Z_i` sharing Y); for single-vertex completions at distinct primes it
does, exactly. An alternating expansion
instead is evaluated on *all* configurations, and on such clusters its
error grows like `M^L/L!` (Bonferroni) or `C^M` (support truncation):
amplification. The local lemma's proof uses only upper bounds for
conditional probabilities (Haeupler–Saha–Srinivasan inflation); a
minorant needs *lower-tail suppression*, which O2–O4 never use. §§3–4
build a minorant whose error is controlled by quantities that do see the
suppression.

**2.5 A codegree-free outer level (Lemma 2.1, PROVED).** Order 𝓔. For
E∈𝓔 let `𝒩(E)` be the set of earlier events sharing a prime with E, and
`Φ_E:=∏_{E'∈𝒩(E)}(1−1_{E'})`. Put `N'':=Σ_E 1_EΦ_E` (locally minimal
occurring events). Then

* `F=1[N''=0]`, and events counted by N'' have pairwise disjoint supports;
* hence `E binom(N'',j) ≤ Σ_{disjoint j-sets}∏P(E) ≤ S^j/j!` for all j,
  with **no codegree hypothesis**, and Bonferroni in N'' gives
  `Σ_{j≤L}(−1)^j binom(N'',j) ≤ F` (L odd) with error `≤(L+1)S^{L+1}/(L+1)!`.

*Proof.* If some event occurs, the first occurring one is counted, so
`N''≥1`; conversely `N''≥1` implies an event occurs. If E′≺E share a prime
and both are counted, then `1_{E′}=1` kills `Φ_E`. Disjoint supports give
independence. Bonferroni is the identity
`Σ_{j≤L}(−1)^j binom(N,j)=(−1)^L binom(N−1,L)` for `N≥1`. ∎

So in the expansion of F the outer inclusion–exclusion costs nothing; all
codegree dependence sits in the neighbourhood factors `Φ_E`, which are not
low-junta. Replacing them by truncations reintroduces 2.3.2 (pinned sets
of `≍kL` vertices, precision `δe^{−S}` needed) or, with Brun's product
inequality over small blocks (precision only `1/S` needed), products of
local errors whose expectation is an event-level exponential moment that
dense clusters blow up. Both routes were checked and, as far as we could
see (Assessment), fail for the same reason as O2–O4; Lemma 2.1 is recorded because it isolates the problem in
the neighbourhood factors.

## 3. A minorant without truncation: the Bazzi–Razborov route

The construction below is the one-sided ℓ²-approximation scheme of
Bazzi (FOCS 2007) as simplified by Razborov (ACM TOCT 2009) with
Wigderson's deterministic choice; it was devised to show that
polylog-wise independence fools DNFs. We use it with the Haar measure on
residues and junta size (number of free primes) as "degree". The point is
that its error is an **unconstrained ℓ² approximation error**, i.e. an
Efron–Stein tail, and the optimal ℓ² approximation is not an alternating
expansion: it sees the suppression of §2.4.

**Setting 3.0.** A system as in the header in which every event
prescribes a **single value** of each coordinate of its support (vertex
sets are split into their full values mod `ℓ^{e_ℓ}`; this preserves
masses, supports and F, but multiplies the number of events), with events
`E_1,…,E_m` (fixed order), `A_i:=1_{E_i}`, `F_{<i}:=∏_{j<i}(1−A_j)`, `F=F_{<m+1}`.
For `E_j` with vertex assignment `σ_j` on `supp E_j`, let `F^{(j)}` be
`F_{<j}` restricted to `{X_{supp E_j}=σ_j}`, a function of the other
coordinates. For a function φ of independent coordinates, `φ=Σ_Uφ^{=U}`
is its Efron–Stein (Hoeffding) decomposition and

```
energy(φ;t) := Σ_{|U|>t} ‖φ^{=U}‖² = min{ E(φ−g)² : g a sum of functions each of ≤t coordinates }.
```

(Standard: the spaces `V_U` of functions of `X_U` orthogonal to all
functions of `X_{U'}`, `U'⊊U`, are mutually orthogonal and the junta-t
functions are `⊕_{|U|≤t}V_U`.)

**Lemma 3.1 (BRW minorant; PROVED).** Let `u_1,…,u_m` be arbitrary real
functions, `v_i:=Σ_{j<i}A_ju_j` and

```
B := 1 − Σ_{i≤m} A_i (1 − v_i)².
```

Then `B≤F` pointwise, and with `e_j:=F_{<j}−u_j`,

```
F − B = Σ_i A_i (Σ_{j<i} A_j e_j)²,     E[F−B] ≤ m² Σ_j E[A_j e_j²].
```

*Proof.* `1−F = Σ_i A_iF_{<i}` (first occurring event). Put
`f_{<i}:=1−F_{<i}=Σ_{j<i}A_jF_{<j}`. If `F_{<i}=1`, all `A_j=0` (j<i), so
`v_i=0` and `A_i(1−v_i)²=A_i=A_iF_{<i}`. If `F_{<i}=0` then
`A_i(1−v_i)² ≥ 0 = A_iF_{<i}` and `(1−v_i)²=(f_{<i}−v_i)²`. Summing,
`F−B = Σ_iA_i[(1−v_i)²−F_{<i}] = Σ_iA_i(f_{<i}−v_i)² ≥ 0`, and
`f_{<i}−v_i = Σ_{j<i}A_j(F_{<j}−u_j)`. Cauchy–Schwarz gives
`(Σ_{j<i}A_je_j)² ≤ m Σ_{j<i}A_je_j²`; drop `A_i≤1` and sum over i. ∎

Choose `u_j` := the Efron–Stein truncation at level t of `F^{(j)}`
(a function of the coordinates outside `supp E_j`). Then
`E[A_je_j²]=P(E_j)·energy(F^{(j)};t)`.

**Lemma 3.2 (size of B; PROVED).** Let N be the number of free primes,
`T≥ℓ^{e_ℓ}` for all of them, and `u_j` as above. Then B is a combination of
unit congruence cells, each on at most `3k+2t` free primes (so every
modulus d has `log d ≤ (3k+2t)𝓛`), with

```
log M_1(B) ≤ 3 log m + 4t log(N+1) + 4(3k+2t)𝓛 + 3.
```

*Proof.* `φ^{=U}=Σ_{W⊆U}(−1)^{|U∖W|}E[φ|X_W]`, so
`u=Σ_{|W|≤t}c_W E[φ|X_W]` with
`c_W=Σ_{i=0}^{t−|W|}(−1)^i binom(N−|W|,i)`, `|c_W|≤(N+1)^t`. For
`0≤φ≤1`, `E[φ|X_W]=Σ_{cells c on W}E[φ|c]1_c` has ℓ¹ mass `Eφ≤1`. Hence
`M_1(u)≤(N+1)^{2t}`. For cells `C,D` on coordinate sets `I,J`,
`P(C∩D) ≤ P(C)P(D)∏_{ℓ∈I∩J}φ(ℓ^{e_ℓ}) ≤ P(C)P(D)T^{|I∩J|}`, so
`M_1(fg) ≤ M_1(f)M_1(g)T^{min(junta)}`. Each term `A_iA_jA_{j'}u_ju_{j'}`
of B (and the lower-order ones) is a product of at most five such
factors on at most `3k+2t` primes; there are at most `m³+m²+m+1` of them.
Hence each term has `M_1 ≤ (N+1)^{4t}T^{4(3k+2t)}`: four successive
products, each inflating by at most `T^{3k+2t}`, and `M_1(u_j)≤(N+1)^{2t}`
twice. This gives the displayed bound (R30a D5). Merging equal cells only
lowers `M_1`. ∎

**Lemma 3.3 (twist; PROVED).** Assume `w_ℓ ≤ 1/(64k)` for all free ℓ
and `E[F−B] ≤ E F/100`. Then for every real primitive ψ of conductor
`f>1`, `gcd(f,Q)=1`, `f|d_i` for some i (PO Thm 4.1's quantifier; so all
primes of f are free coordinates), the twisted mean of B satisfies `|μ_ψ| ≤ μ/4`.

*Proof.* As O2 Thm 3.1 Step 4. Since ψ is primitive and f is odd
squarefree, `μ_ψ=E[Bψ]` for any cell representation of B, so
`|μ_ψ| ≤ E|B−F| + |E[Fψ]|`. Fix a prime
`ℓ_0|f` and let `F'` be the indicator that no event avoiding `ℓ_0` occurs.
Then `F=F'·1[X_{ℓ_0}∉Forb]` with Forb determined by `X_{−ℓ_0}`, and
`|E[Fψ]| ≤ E[F'·P_{X_{ℓ_0}}(Forb)] ≤ Σ_{E∋ℓ_0} p_{ℓ_0}(E)·P(E∖ℓ_0 ∩ F')`.
The local lemma for the family defining `F'` (with `x_E=2P(E)`, every
neighbourhood sum `≤2k/(64k)=1/32`) and its conditional form
(Haeupler–Saha–Srinivasan) give `P(E∖ℓ_0 | F') ≤ e^{1/16}P(E∖ℓ_0)`. So
`|E[Fψ]| ≤ 1.07w_{ℓ_0}E F' ≤ 0.02 E F'`, and `E F ≥ (1−0.02)E F'`. With
`μ ≥ 0.99 E F`: `|μ_ψ| ≤ (0.01+0.021)E F ≤ μ/4`. ∎

**Theorem 3.4 (PROVED implication, modulo Thorner–Zaman via PO Thm 4.1).**
Let `k:=⌊𝓛/log z⌋`, and let Π be the output of O2 Lemma 11.2
started from `{ℓ≤z}` with `c_0:=1/(64k)`; let 𝓔 be the distinct surviving
events, split into single values as in Setting 3.0 (supports ≤k, total
mass `S≤S*`, `m≤T^{k+2}` events: at most `T²` atoms, each split into at
most `∏_{ℓ|r}ℓ^{e_ℓ−v_ℓ(r)} ≤ T^k` events). Assume `7≤z≤T^{1/3}` (so
`k≥1`, `840|Q_Π`); if `m=0` the class of one mod `Q_Π` already works. Suppose

```
EL(t):   energy(F^{(j)}; t) ≤ e^{−3S}/(100 m² (S+1))    for every j.
```

Then there is a Mordell-hard prime `p>T` with `W(p)>T` and

```
log p ≤ C·K·(log Q_Π + 2(3k+2t+1)𝓛 + K),     K := 4S* + C'(k+t)𝓛,
log Q_Π ≤ (π(z) + 64k²S*)𝓛 + 4.
```

*Proof.* The local lemma (O2 Thm 11.3's proof, neighbourhood sums
`≤2k c_0`) gives `δ:=E F ≥ e^{−2.2S}` on the class of one mod `Q_Π`. Lemma
3.1 with EL(t): `E[F−B] ≤ m²·S·e^{−3S}/(100m²(S+1)) ≤ δ/100`, so
`μ=E B ≥ 0.99δ`. Lemma 3.2 bounds `M_1` and the moduli (`N≤T`), Lemma 3.3
the twist. (I) (O2 Lemma 4.3 (I)) gives `B≤1[W>T]` for every `n≡1 (Q_Π)`
coprime to all `d_i`. That is all PO Thm 4.1's proof uses: it evaluates B
only at primes `p≡1 (Q)`, `p>Q>T` (R30b D1). Then apply PO Thm 4.1 with the
auxiliary prime `ℓ_aux∈(R,2R]`, `R=max(T,max d_i)`, as in O4 Thm 2.1:
`log Z ≤ log Q_Π + log ℓ_aux + log max d_i ≤ log Q_Π + 2(3k+2t+1)𝓛`
(R30a/R30b D1–D2). Finally `|𝓑|≤kS*/c_0`. Splitting may create duplicate
single-value events; they are kept, since Lemma 3.1 and the local lemma do not
need distinctness and masses are unchanged (R30b D5). ∎

**Corollary 3.5 (rates under EL; PROVED implications).**
1. If EL(t) holds with `t ≤ (𝓛S*)^A`, take `z=𝓛²`. Then
   `log p ≤ (𝓛S*)^{O(A)}`. Modulo Elsholtz–Tao Prop 1.4
   (`S*≪𝓛^4log𝓛`): **`W(p) ≥ exp((log p)^{c/A})` for infinitely many
   Mordell-hard p.** Unconditionally (`log S* ≤ (log 2+o(1))𝓛/log𝓛`):
   `log W ≥ c_A·log₂p·log₃p` with `c_A>0`, which already beats O4 Cor 3.2
   (and Cor 3.1).
2. If EL(t) holds only with `t ≤ C_0^k(𝓛S*)^A`, take
   `log z ≍ (𝓛 log C_0)^{1/2}`: `log W(p) ≥ c(log₂p)²/log C_0` (mod ET).

*Proof.* Insert into Theorem 3.4; in 2, `log₂p ≲ max(log z, k log C_0)`
up to `O(log 𝓛)`. ∎

So the whole prime-side problem is reduced to an **Efron–Stein tail bound
for good-indicators of local-lemma systems**. No codegree hypothesis, no
level structure, and no push-down appear in Theorem 3.4.

## 4. EL holds: the switching lemma does the work (PROVED)

**Lemma 4.1 (bit encoding; PROVED).** Let φ be the good-indicator of a
system of events with at most k free primes each, on N coordinates
`X_ℓ` uniform on finite sets `G_ℓ` with `|G_ℓ|≤T`, possibly with some
coordinates pinned (so `F^{(j)}` is allowed). Let `b:=⌈log₂(4NT)⌉`. Then
for every integer `k_0≥1`,

```
energy(φ; 2C_H·k·b·k_0) ≤ 4·2^{−k_0},
```

where `C_H` is the absolute constant of Håstad's switching lemma in the
form `Pr_ρ[DT(f_ρ)≥s] ≤ (C_H p w)^s` for p-random restrictions of a
width-w DNF (Håstad 1986; `C_H=5` in O'Donnell, *Analysis of Boolean
Functions*, §4.4; any absolute constant suffices).

*Proof.* (a) *Encoding.* Enumerate `G_ℓ={g_0,…,g_{q−1}}` and let
`π_ℓ(u):=g_{⌊q·int(u)/2^b⌋}` for `u∈{0,1}^b`. Each fibre is an integer
interval, hence a disjoint union of `≤2b` subcubes of codimension `≤b`; a
vertex set `V⊆G_ℓ` has preimage a union of such subcubes. With U uniform
on `({0,1}^b)^N` and `φ̃:=φ∘π`, the function `1−φ̃` is an OR over events of
ANDs over `≤k` coordinates of ORs of width-`≤b` terms; distributing, it is
a DNF of width `≤w:=kb` (the number of terms is irrelevant).

(b) *Concentration (LMN with Håstad).* Take `p:=1/(2C_Hw)`. For a
p-random restriction ρ, `Pr[DT(f_ρ)≥k_0] ≤ 2^{−k_0}`. If `DT(f_ρ)<k_0`
then `f_ρ` has Fourier degree `<k_0`; and
`E_ρ W^{≥k_0}[f_ρ] = Σ_U Pr[|U∩I|≥k_0] f̂(U)²`, where for `|U|≥d:=k_0/p`
we have `Pr[Bin(|U|,p)≥k_0] ≥ Pr[Bin(|U|,p)≥⌊p|U|⌋] ≥ 1/2` (the median of
a binomial is `⌊np⌋` or `⌈np⌉`). Since `W^{≥k_0}[f_ρ]≤1`, this gives
`W^{≥d}[1−φ̃] ≤ 2·2^{−k_0}`; the same holds for φ̃. So the Fourier
truncation g̃ of φ̃ below degree d has `E(φ̃−g̃)² ≤ 2^{1−k_0}`.
(Linial–Mansour–Nisan 1993. Textbook form: O'Donnell, *Analysis of Boolean
Functions*, Lemma 4.21, which gives `3ε`-concentration up to degree `3k/δ`
via Chernoff. The median variant used here follows Kaas–Buhrman,
Statistica Neerlandica 34 (1980): the median of `Bin(n,p)` is `⌊np⌋` or
`⌈np⌉`. With O'Donnell's version, t gains a factor 3/2; R30a D3.)

(c) *Back to coordinates.* Put `g(x):=E[g̃(U) | π(U)=x]`. A character
`χ_S` (S a set of bits) involves the blocks of at most `|S|<d`
coordinates, and since the blocks are independent and π acts blockwise,
`E[χ_S | π(U)]` is a function of those coordinates. So g is a sum of
functions of `<d` coordinates. By Jensen (φ̃ is `π(U)`-measurable),
`E_{x∼π_*}(φ−g)² ≤ E(φ̃−g̃)²`. Finally each fibre has `⌊2^b/q⌋` or
`⌈2^b/q⌉` points, so the Haar density relative to `π_*` is
`≤∏_ℓ(1−q_ℓ2^{−b})^{−1} ≤ exp(2NT·2^{−b}) ≤ e^{1/2}` (in fact `≤e^{1/3}`; R30a). Hence
`energy_{Haar}(φ;d) ≤ E_{Haar}(φ−g)² ≤ e^{1/2}2^{1−k_0} ≤ 4·2^{−k_0}`. ∎

**Corollary 4.2 (EL; PROVED).** In Theorem 3.4, EL(t) holds with

```
t := 2C_H·k·b·k_0,   k_0 := ⌈ 3S log₂e + log₂(400 m²(S+1)) ⌉,   b := ⌈log₂(4T²)⌉,
```

so `t ≤ C·k·𝓛·(S+k𝓛)` (using `N≤T`, `m≤T^{k+2}`). ∎

**Theorem 4.3 (main; PROVED modulo Thorner–Zaman (PO Thm 3.1) and
Elsholtz–Tao Prop 1.4; effective if ET's constant is).** For infinitely
many Mordell-hard primes p,

```
W(p) ≥ exp( c·(log p)^{1/14} ).
```

Uniformly: for every large T there is a hard prime p with `W(p)>T` and
`log p ≤ C·𝓛^{14}`, i.e. `log L_h(T) ≪ (log T)^{14}`.

*Proof.* Theorem 3.4 with `z=𝓛²` (so `k≤𝓛/(2log𝓛)`) and Corollary 4.2.
Under ET, `S≤S*≪𝓛^4log𝓛` (O2 Lemma 11.1). Then `t≪𝓛^6`,
`K≪t𝓛+S*≪𝓛^7`, `log Q_Π ≤ (π(𝓛²)+64k²S*)𝓛+4 ≪ 𝓛^7/log𝓛`,
`log Z ≪ log Q_Π+t𝓛 ≪ 𝓛^7`, and PO Thm 4.1 gives `log p ≪ K·max(log Z,K) ≪ 𝓛^{14}`.
`W(p)>T=e^𝓛`. Distinct T give infinitely many p (`p>T`). ∎

**Theorem 4.4 (PROVED modulo Thorner–Zaman only; effective).** For
infinitely many Mordell-hard p, `log W(p) ≥ (1/(2log 2)−o(1))·log₂p·log₃p`.

*Proof.* As 4.3 with the unconditional `log S* ≤ (log2+o(1))𝓛/log𝓛`
(Wigert, O2 Lemma 11.1; derivation of the constant `log 2` in
POINTWISE_OMEGA9 Thm 2.3's proof): `t, K, log Q_Π ≤ 𝓛^{O(1)}(S*+1)`, so
`log₂p ≤ 2log S* + O(log𝓛) ≤ (2log2+o(1))𝓛/log𝓛`. Since `x/log x` is
increasing, this inverts to `𝓛 ≥ (1/(2log2)−o(1))·log₂p·log₃p`. ∎

**Comparison.** O4 Cor 3.1: `log W ≥ (1+o(1))log₂p·log₃p/log₄p` (mod TZ,
ET); O4 Cor 3.2: `log₂p·log₄p/log₅p` (mod TZ). Theorem 4.3 is the third
target of O4 §4.4 (declared "outside the method" there; it was outside
the *alternating-expansion* method), and matches the Haar side
`log(1/δ*)≪𝓛^7/log𝓛` (O2 Thm 11.3; R30a/b D4) up to squaring: the transfer costs
`log p ≈ K·log Z` with both factors of Haar size. The heuristic truth is
`log W ≍ (log p)^{1/3}` (POINTWISE_SIZE §7).

**Why this escapes §2.** The error of the BRW minorant is an
*unconstrained* ℓ² error. The optimal junta approximation does not
alternate; on dense clusters it is small because F is small there
(suppression), and Håstad's lemma certifies this for *every* DNF of
bounded width, with no codegree, level or hub hypothesis. The width
`kb≍k𝓛` enters only linearly in t. Nothing about ES beyond (I), the
supports `≤k`, per-prime masses `≤1/(64k)`, and `S*` is used.

## 5. Checks, scope, and what is not claimed

* `scripts/omega8_brw_check.py` (`data/omega8/brw_check.txt`): random
  systems on `(ℤ/5)^6`, `u_j` = Efron–Stein truncations. Over 40 trials,
  pointwise `B≤F` (max of `B−F` is 0), the identity of Lemma 3.1 holds to
  `5·10^{−15}`, and the bound `E[F−B] ≤ m²ΣP(E_j)energy_j` holds in all
  40.
* `scripts/omega8_levels.py` (`data/omega8/levels.txt`): exact level
  weights of toy good-indicators against event-level Bonferroni errors.
  In the hub toy the Bonferroni ℓ² error at full junta exceeds `δ`, while
  the optimal junta-3 error is `0.027δ`. This only illustrates §2.4
  (suppression against amplification); the toys are far too small to
  test asymptotics and nothing rests on them.
* **Inputs used:** PO Thm 4.1 (Thorner–Zaman), O2 Lemmas 11.1–11.2 and
  Lemma 4.3 (I), the local lemma with its conditional form
  (Haeupler–Saha–Srinivasan), Håstad's switching lemma with the
  Linial–Mansour–Nisan argument (textbook; constants as in O'Donnell
  §4.4, Lemma 4.21; Kaas–Buhrman for binomial medians), and Razborov's form of Bazzi's reduction (with
  Wigderson's choice). Elsholtz–Tao Prop 1.4 enters only through
  `S*≪𝓛^4log𝓛`.
* **Not claimed:** anything about ES; any optimality of the exponent
  1/14 (it is bookkeeping: `log p ≈ K·log Z`, each `≍𝓛^7`); any
  numerical instance.
* **Literature status of the method:** the Bazzi–Razborov–Braverman
  theory is standard in pseudorandomness ("bounded independence fools
  DNF/AC0"). Its use here is a transfer: Thorner–Zaman makes the primes
  `≡1 (Q)` a multiplicatively almost-t-wise-independent distribution on
  residue cells, and the BRW sandwich is exactly what PO Thm 4.1 consumes.
  We found no prior use of it in Erdős–Straus or in Ω-results of this
  type (not a literature search).

## 6. Phase 2: optimising the exponent 1/14

(This section was requested as "new §5"; it is numbered §6 so that the
reviewed numbering of §§1–5 is unchanged.)

### 6.1 Where the powers of 𝓛 go (ledger for Thm 4.3; under ET)

PO Thm 4.1 costs `log p ≍ K·max(log Z, K)`. With `z=𝓛²`, so that
`k≍𝓛/log𝓛`:

| quantity | source | size |
|---|---|---|
| `S ≤ S*` | O2 Lemma 11.1 with ET Prop 1.4 | `𝓛^4log𝓛` (EVIDENCE: actual `S≈0.05𝓛^{2.5}`) |
| `log(1/δ)` | local lemma, `δ≥e^{−2.2S}` | `≍S` |
| `k_0` | precision `e^{−3S}/m²` | `≍S+k𝓛 ≍ S` |
| width w | bit encoding: k coordinates × `b≈2log₂T` bits | `kb ≍ 𝓛²/log𝓛` |
| degree / junta `t=2C_Hwk_0` | switching lemma + LMN | `≍ w·S ≍ 𝓛^6` |
| `log M_1` | Lemma 3.2: `N^{t}` coefficient count and `T^{junta}` overlap inflation | `≍ t𝓛 ≍ 𝓛^7` |
| `log max d_i` | moduli on `≤3k+2t` primes `≤T` | `≍ t𝓛 ≍ 𝓛^7` |
| `log Q_Π` | `π(z)𝓛 + |𝓑|𝓛`, `|𝓑|≤64k²S*` | `≍ k²S*𝓛 ≍ 𝓛^7/log𝓛` |
| `K` | `log M_1 + log(1/δ)` | `𝓛^7` |
| `log p` | `K·log Z` | `𝓛^{14}` |

There are four independent losses beyond the Haar side's `𝓛^7/log𝓛`.
1. The factor 𝓛 in `log M_1`: an artefact of cell bookkeeping
   (Lemma 6.1 removes it).
2. The factor k in `|𝓑|`, from the crude per-prime threshold `1/(64k)`
   (not removed here: the log-weighted thresholds after Thm 6.3 do not
   suffice; R30c M1. An earlier draft cited a "Lemma 6.2" that does not exist.)
3. The factor `b≍𝓛` in the width, from the bit encoding (§6.4).
4. The square from `K·log Z`, intrinsic to PO Thm 4.1; and S itself,
   through ET.

**Lemma 6.1 (spectral bookkeeping; PROVED).** In Lemma 3.1 take `u_j :=`
the pull-back `g_j(x)=E[g̃_j(U) | π(U)=x]` of the Fourier truncation `g̃_j`
of `F̃^{(j)}` below degree d, where `w:=kb`, `p:=1/(4C_Hw)` and
`d:=k_0/p=4C_Hwk_0`. (Notation, R30c m2: in §6 the letter d without index is
this degree; moduli always carry an index, `d_i`, `max d_i`.) Here `F̃^{(j)}`
is encoded as a function of the coordinates **outside** `supp E_j` only, so
`g_j` depends only on those coordinates, as Lemma 3.1's identity
`E[A_je_j²]=P(E_j)E(F^{(j)}−g_j)²` requires (R30c m1). Then:
* `E_{Haar}[(F^{(j)}−g_j)²] ≤ e^{1/2}·2·4^{−k_0}`;
* B is a combination of unit cells, each on `≤3k+2d` free primes;
* `log M_1(B) ≤ 3log m + 2d·log(4C_Hw) + 4`.

So `log M_1` loses the factor `𝓛/log(k𝓛)` against Lemma 3.2.

*Proof.* The first claim is Lemma 4.1 with p replaced by `1/(4C_Hw)`:
`Pr[DT(f_ρ)≥k_0]≤4^{−k_0}`. *Spectral norm.* For a restriction
`ρ=(I,z)` and `S⊆I`, `f̂_ρ(S)=Σ_{T⊆I^c}f̂(S∪T)χ_T(z)`, so
`E_z f̂_ρ(S)=f̂(S)`. Hence
`Σ_S p^{|S|}|f̂(S)| ≤ E_ρ‖f̂_ρ‖_1 ≤ E_ρ 2^{DT(f_ρ)}`. The last step holds
because a depth-s tree has at most `2^s` leaves, each path indicator has
spectral norm 1, and `|f|≤1`. This is `≤Σ_{s≥0}2^s4^{−s}=2`. Therefore
`Σ_{|S|<d}|ĝ_j(S)| ≤ 2p^{−d} = 2(4C_Hw)^d`, where `ĝ_j(S)` are the Fourier
coefficients of the bit-level truncation `g̃_j` (R30c m2). *Cells.* Each pulled-back
character `χ̃_S:=E[χ_S | π(U)=·]` is a function of `<d` coordinates with
`|χ̃_S|≤1`. A product `A_iA_jA_{j'}χ̃_Sχ̃_{S'}` is a function h of at most
`3k+2d` coordinates with `|h|≤A_iA_jA_{j'}`. Its expansion over the cells
of those coordinates has ℓ¹ mass `E|h|≤1`, with no overlap inflation,
because the product is expanded as one function and not cell by cell.
Summing over `i,j,j'≤m` and over `S,S'`,
`M_1(B) ≤ 1+m+2m²·2(4C_Hw)^d+m³·4(4C_Hw)^{2d}`. ∎

**Theorem 6.3 (PROVED modulo Thorner–Zaman and ET Prop 1.4).** For
infinitely many Mordell-hard p,

```
W(p) ≥ exp( c·(log p / log log p)^{1/13} ),
```

uniformly `log L_h(T) ≪ 𝓛^{13}log𝓛`.

*Proof.* Theorem 3.4 with Lemma 6.1 in place of Lemma 3.2 and Lemma 4.1
(the twist Lemma 3.3 needs only `E[F−B]≤EF/100`; the extension to n
coprime to the moduli is unchanged). With `z=𝓛²`: `w=kb≪𝓛²/log𝓛`,
`k_0≪S*+k𝓛≪𝓛^4log𝓛`, so `d=4C_Hwk_0≪𝓛^6`. Then
`K ≤ 3log m+2d log(4C_Hw)+2.2S+6 ≪ 𝓛^6log𝓛`, and
`log Z ≤ log Q_Π+2(3k+2d+1)𝓛 ≪ 𝓛^7` (`log Q_Π≪𝓛^7/log𝓛` as before). So
`log p ≪ K·log Z ≪ 𝓛^{13}log𝓛`. ∎

So the factor 𝓛 in K is gone; `log Z` (moduli `≍T^{junta}`, plus `Q_Π`)
is now the larger factor. Lowering `|𝓑|` alone (item 2 of 6.1) cannot help
until the junta shrinks. Remark: log-weighted thresholds
`c_ℓ=log ℓ/(16𝓛)` satisfy the local lemma, because
`Σ_{ℓ∈supp E}c_ℓ≤1/16`. They give `Σ_{ℓ∈𝓑}log ℓ ≤ 16k𝓛S*`, but bad
primes `≤√T` still cost `e_ℓlog ℓ≤𝓛`, so `log Q_Π` improves only on the
part `>√T`; not pursued.

### 6.4 The bit-encoding width (Assessment, with a PROVED counterexample)

The degree is `d ≍ w·k_0` with `w=kb`. The factor `b≍2log₂T` appears
because a q-ary literal `X_ℓ=c` is a b-bit term. A **q-ary switching
lemma** of the form `Pr[DT_q(f_ρ)≥s] ≤ (Cpk)^s` would give
`d ≍ k·k_0`. Here ρ frees each coordinate with probability p and fixes the
others uniformly; `DT_q` is q-ary decision-tree depth, which bounds the
Efron–Stein degree. (The LMN step works verbatim for Efron–Stein in product
spaces (`E_z‖(f_{I,z})^{=S}‖² = Σ_{U∩I=S}‖f^{=U}‖²`). The result would
be `d≪𝓛^5`. Exponent `1/11` (`K≪𝓛^5log𝓛`, `log Z≪𝓛^6`) would need in
addition (a) a q-ary analogue of Lemma 6.1's ℓ¹ bound for Efron–Stein
truncations, `log M_1 ≪ d log𝓛` (ESW is an energy statement and gives no
ℓ¹ control; via Lemma 3.2 one gets only `K≍d𝓛≍𝓛^6`), and (b) a
quarantine with `|𝓑|≪kS*`, so that `log Q_Π≪𝓛^6`; neither is proved. With
ESW alone the bookkeeping gives `𝓛^{13}/log𝓛`, no real gain (R30c M1).)

*The decision-tree form is false, even with small masses (PROVED
example).* Take `N:=⌊q^{1/2}⌋` coordinates uniform on `[q]` and the
width-2 DNF f = "two coordinates coincide" (terms `X_i=c∧X_j=c`). The
per-coordinate mass is `(N−1)/q ≤ q^{−1/2}` and the total mass is
`≤1/2`. Let ρ free each coordinate with probability `p=1/(4C)` (any
`p<1/(2C)`; with `p=1/(2C)` and `k=2` the bound `(Cpk)^s` would be 1; R30c m3).
With probability `≥e^{−1/2}−o(1)` the fixed values are distinct, and then, for
`s` free coordinates, `f_ρ` = "a free value hits a fixed value or another
free value". An adversary answering fresh distinct values keeps `f_ρ`
undetermined until the last query (possible since `N+s<q`), so
`DT_q(f_ρ)=s`. With constant probability `s≥pN/2≍q^{1/2}`, which is not
`≤(C(pk+max w_ℓ))^s` for large q: that bound tends to 0 geometrically in s
(numerically `Pr[DT_q≥pN/2]≈0.61` against `≤10^{−3.5}` at q=10⁴, C=1;
R30c). ∎

But the decision depth overstates the complexity: heuristically, the energy
of `f_ρ` at level `≥s` is `≈(s²/q)^{s/2}`-small (pairwise-collision
structure), not ≈1 as the depth suggests; the exact Efron–Stein weights for
`q=49…144` decay in the level (R30c). This is evidence, not an argument
(R30c m4). So decision depth is the wrong measure for rare literals. LMN needs only an **energy
switching** statement,

```
(ESW)   E_ρ W^{≥s}[f_ρ] ≤ (C(pk+max_ℓ w_ℓ))^s,
```

where W is the Efron–Stein weight in the q-ary product space and f a
system's bad-indicator. ESW with LMN would give `d≍k·k_0`. ESW is
**open**. The example is plausibly consistent with it (exact level weights
decay; R30c m4), but no proof is given.

### 6.5 Ceilings of this route (Assessment)

* *The square.* PO Thm 4.1 needs `log x ≫ K·log Z`. For the BRW expansion as written (its constant
  cell has coefficient 1, so `M_1≥1`), `K≥1+log(1/μ)≥log(1/δ)≥S1` rigorously
  (Prop 6.6 and the remark after it; not for every cell representation —
  R34a); `log(1/δ)≈S` for
  multi-prime events is heuristic. Also `log Z ≳ (junta)·log z`, with junta
  `≳ S/log(junta/S)` for minorants of Brun/BRW type (heuristic, from the
  fundamental-lemma level requirement; no argument covers every minorant).
  So `log p ≳ S²·log z` for such minorants. This is the price of
  Thorner–Zaman's error `exp(−c log x/log q)` (R30c m5). POINTWISE_OMEGA9
  Thm 1.1 replaces PO Thm 4.1 by a transfer without the square.
* *Under ET* (`S≤𝓛^4log𝓛`): with S only bounded by `S*`, even an ideal
  junta `≍S` gives `log p ≈ S·S𝓛 ≈ 𝓛^9` (exponent `≈1/9`). This is what
  the bookkeeping yields, not a ceiling: ET bounds S from above. The
  supported ceiling of this route is via Prop 6.6: `S1≫𝓛²` gives
  `log p ≳ 𝓛^4·log z`, exponent `≤1/4` (Assessment; R30c m5). *With the empirical*
  `S≈𝓛^{2.5}` (EVIDENCE, PO §2): `≈𝓛^6` (exponent `≈1/6`). The heuristic
  truth `log W≍(log p)^{1/3}` (POINTWISE_SIZE §7) is out of reach of
  any transfer through PO Thm 4.1 with a Haar density `e^{−Θ(S)}`, unless
  `S` itself is `≪𝓛`; the Haar side's true size is
  `−log δ*≍𝓛^{2.3…2.6}` (EVIDENCE).
* *Remaining losses, ordered by size.*
  1. The width `kb≍𝓛²/log𝓛` in d. The bit part needs the energy
     switching statement ESW (6.4; the decision-tree form is false); the k part would need Fourier tails
     sensitive to the event-size distribution rather than to the maximal
     width.
  2. `S*` through ET: `𝓛^4log𝓛` against `𝓛^{2.5}` observed.
  3. The precision `k_0≍S`, forced by `δ≥e^{−2.2S}` being only a lower
     bound.

### 6.6 The Haar mass S cannot be `𝓛^{1+o(1)}` (PROVED modulo a standard divisor sum, sketched)

**Proposition 6.6.** Let Π be any quarantine set with
`|Π∩(T^{1/2},T]| ≤ T^{1/3}`; the iterated quarantine qualifies, since
`|𝓑|≤T^{o(1)}`. Then the surviving distinct-class single mass satisfies `S1(Π) ≫ 𝓛²`
(hence also `S ≥ S1` and `S_tot(Π) ≫ 𝓛²`).
This rests on the shifted-prime divisor bound

```
(D)   Σ_{p≤x, p≡3 (4)} τ(((p+1)/4)²) ≫ π(x)(log x)²,
```

which is standard; we use it on dyadic ranges (R30c m6):

```
(D')  Σ_{x/2<p≤x, p≡3 (4)} τ(((p+1)/4)²) ≫ (x/log x)(log x)²   (x large).
```

*Proof of (D') (standard; sketched as in Elsholtz–Tao §5).* `τ(n²)=Σ_{d|n}2^{ω(d)}`,
and for `p≡3 (4)`, `d|(p+1)/4 ⟺ p≡−1 (4d)`. Keep `d≤y:=x^{1/3}`. Write
`π^*(q):=#{x/2<p≤x: p≡−1 (q)}=π^*/φ(q)+E(q)` with `π^*:=π(x)−π(x/2)`. Main
term: `π^*Σ_{d≤y}2^{ω(d)}/φ(4d) ≥ (π^*/4)Σ_{d≤y}2^{ω(d)}/d ≫ π^*(log x)²`.
Error: by Cauchy–Schwarz, `Σ_{d≤y}2^{ω(d)}|E(4d)| ≤ (Σ_d4^{ω(d)}|E(4d)|)^{1/2}(Σ_d|E(4d)|)^{1/2}`;
Brun–Titchmarsh (`4d≤x^{1/2}`) gives `|E(4d)|≪x/(φ(d)log x)`, so the first
factor is `≪(x(log x)^3)^{1/2}`, and Bombieri–Vinogradov gives
`Σ_{q≤4x^{1/3}}|E(q)|≪x(log x)^{−A}` (inside the BV range; R34a). The error is `≪x(log x)^{(3−A)/2}`,
negligible. ∎

*Proof of the Proposition.* The atoms `(M,D)=(ℓ,D)` with M a free prime have `m=1`, so they
survive every class-of-one quarantine (`1|4D+1`). They are singles at ℓ
with classes `−4D mod ℓ`. The divisors `D≤A_ℓ=(ℓ+1)/4<ℓ` of `A_ℓ²` give
distinct nonzero classes (`4D∈[4,ℓ+1]`), exactly `(τ(A_ℓ²)+1)/2` of them. So the
distinct-class single mass is `S1 ≥ Σ_{ℓ∈(√T,T]∖Π, ℓ≡3 (4)} τ(A_ℓ²)/(2(ℓ−1))`. By (D')
on the dyadic ranges `(T/2^{j+1},T/2^j]`, `0≤j≤𝓛/(2log2)`, each range
contributes `≫ log(T/2^j)`, so the sum over all `ℓ∈(√T,T]` is
`≫ Σ_j (𝓛−j log 2) ≍ 𝓛²`. The at most `T^{1/3}` quarantined primes there remove
at most `T^{1/3}·τ*(T)²/√T = o(1)`. ∎

**Strengthening (PROVED modulo (D'); R30c m7).** The proof bounds the
distinct-event single mass, so `S ≥ S1 ≫ 𝓛²` for the distinct-event mass
S of Thm 3.4. Singles at distinct free primes are independent events, so
`δ = E F ≤ ∏_ℓ(1−g_ℓ) ≤ e^{−S1}` (`g_ℓ` the single mass at ℓ; δ the
density on the class of one mod `Q_Π`). Hence `log(1/δ) ≫ 𝓛²`; every
minorant `B≤F` has `μ≤δ`, and for the BRW expansion as written (`M_1≥1`)
`K ≥ 1+log(1/μ) ≫ 𝓛²`. This is **not** a bound for every cell
representation: e.g. F written as the sum of its disjoint good cells has
`M_1=μ`, `K=1` (with huge moduli) (R34a MAJOR 2).

**Consequence (Assessment; R30c m8).** In §6.5's bound `log p ≳ S²·log z`,
S is at least of order `𝓛²`; so through PO Thm 4.1 even an ideal junta
cannot go below `log p≈𝓛^4·log z`, exponent `≤1/4`. Task (b)'s hope
`S≪𝓛^{1+o(1)}` is a dead end. Splitting off the singles (Brun for them,
BRW for the multi-prime events) does not lower `log(1/μ)≥S1`; for
representations with `M_1≳1` (as BRW-type ones) K stays `≳𝓛²`, and only
`log Z` could shrink. (No universal statement over all representations is
claimed; R34a.) Also
`log Z ≥ log ℓ_aux > 𝓛`, so PO Thm 4.1's sufficient condition is never met
below `log p≈𝓛^4` on this route (with `K≫𝓛²` for BRW as written,
`K·max(log Z,K) ≥ K²`; R34b m3). (POINTWISE_OMEGA9 Thm 1.1 replaces the
condition by `log x ≫ (1+log(E|B|/μ))·log Z`, with no `log(1/μ)` or `M_1`.) The data of PO §2 are
for `y=√T`, where `S_{≥2}=0`.

## Replay

```
export PYTHONPATH=scripts
(ulimit -v 8000000; uv run python scripts/omega8_brw_check.py 40 1)   # ~1 min -> data/omega8/brw_check.txt
(ulimit -v 8000000; uv run python scripts/omega8_levels.py all)       # ~1 min -> data/omega8/levels.txt
```
