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

**Status: work in progress (checkpoint 1 being written).**

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
log W(p) ≥ (1/2 − o(1))·(log₂p)^{1/(1−η)}.
```

Conversely, within Lemma 4.1, `log₂p ≥ 𝓛/(k+1)` and `log₂p ≥ X`, so a rate
`log W ≥ (log₂p)^{1/(1−η)}` forces `k ≳ 𝓛^η` and `X ≲ 𝓛^{1−η}`.

*Proof.* With `X≤𝓛^{1−η}/3` and `k+1≥𝓛^η`: `log₂p ≤ 𝓛^{1−η}/3+𝓛^{1−η}+O(log𝓛) ≤ 2𝓛^{1−η}`
for large T, i.e. `𝓛 ≥ (log₂p/2)^{1/(1−η)}`, and `log W(p) ≥ 𝓛`. Since
`1/(1−η)<2`, `2^{−1/(1−η)} ≥ 1/4`; the constant is immaterial. Distinct T
give distinct p (`p>T`). The converse is read off the display. ∎

**Consequence (what must be polynomial).** O4 Thm 1.1 gives
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

**2.3 Three facts about alternating expansions** (the first two PROVED,
the third PROVED about the parameter recursion).

1. *Precision.* `E F=δ≤1` while the order-j terms have total mass
   `≍S^j/j!`; so terms up to order `≍S+log(1/δ)` are needed and each must be
   exact or approximated to absolute precision `≪δ e^{−S}`.
2. *Reuse.* An order-j term pins the `≤kj` vertices of j events. The error
   of a truncation at order L is a moment of the active-prime count, and
   a new event may reuse any i pinned vertices. Bounding this moment
   needs codegrees `Δ_O ≲ (kL)^{−(|O|−1)}` (O2 Lemma 10.2), and this is
   real for the truncated moment, not an artefact of its proof (O2 §11.4,
   reviewer example D12).
3. *Circularity.* Markov pushes of heavy sets at thresholds
   `(kL)^{−(i−1)}` add mass `≥ Σ·(kL)^{i−1}/C`, while `L ≥ c·(mass)`;
   so in one family `S_fin ≥ S·(ckS_fin)^{i−1}/C` has no solution for
   large S. Hence separate levels, each truncated at its own mass, and
   exponents multiply along `k→k−1→…→2`: `(k−1)!` (O4 Thm 1.1, §4.1).

**2.4 Where the local lemma differs.** On a *good* configuration, a
partial cluster with large completion mass M is exponentially unlikely
(probability factor `≤e^{−M}`: suppression). An alternating expansion
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
dense clusters blow up. Both routes were checked and fail for the same
reason as O2–O4; Lemma 2.1 is recorded because it isolates the problem in
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

**Setting 3.0.** A system as in the header with events `E_1,…,E_m`
(fixed order), `A_i:=1_{E_i}`, `F_{<i}:=∏_{j<i}(1−A_j)`, `F=F_{<m+1}`.
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
log M_1(B) ≤ 3 log m + 8t log(N+1) + 2(3k+2t)·4𝓛 + 3.
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
Merging equal cells only lowers `M_1`. ∎

**Lemma 3.3 (twist; PROVED).** Assume `w_ℓ ≤ 1/(64k)` for all free ℓ
and `E[F−B] ≤ E F/100`. Then for every real primitive ψ of conductor
`f>1`, `gcd(f,Q)=1`, the twisted mean of B satisfies `|μ_ψ| ≤ μ/4`.

*Proof.* As O2 Thm 3.1 Step 4. `|μ_ψ| ≤ E|B−F| + |E[Fψ]|`. Fix a prime
`ℓ_0|f` and let `F'` be the indicator that no event avoiding `ℓ_0` occurs.
Then `F=F'·1[X_{ℓ_0}∉Forb]` with Forb determined by `X_{−ℓ_0}`, and
`|E[Fψ]| ≤ E[F'·P_{X_{ℓ_0}}(Forb)] ≤ Σ_{E∋ℓ_0} p_{ℓ_0}(E)·P(E∖ℓ_0 ∩ F')`.
The local lemma for the family defining `F'` (with `x_E=2P(E)`, every
neighbourhood sum `≤2k/(64k)=1/32`) and its conditional form
(Haeupler–Saha–Srinivasan) give `P(E∖ℓ_0 | F') ≤ e^{1/16}P(E∖ℓ_0)`. So
`|E[Fψ]| ≤ 1.07w_{ℓ_0}E F' ≤ 0.02 E F'`, and `E F ≥ (1−0.02)E F'`. With
`μ ≥ 0.99 E F`: `|μ_ψ| ≤ (0.01+0.021)E F ≤ μ/4`. ∎

**Theorem 3.4 (PROVED implication, modulo Thorner–Zaman via PO Thm 4.1).**
Let `z≥2`, `k:=⌊𝓛/log z⌋`, and let Π be the output of O2 Lemma 11.2
started from `{ℓ≤z}` with `c_0:=1/(64k)`; let 𝓔 be the distinct surviving
events (supports ≤k, total mass `S≤S*`, `m≤T²` events). Suppose

```
EL(t):   energy(F^{(j)}; t) ≤ e^{−3S}/(100 m² (S+1))    for every j.
```

Then there is a Mordell-hard prime `p>T` with `W(p)>T` and

```
log p ≤ C·K·(log Q_Π + (3k+2t+2)𝓛 + K),     K := 4S* + C'(k+t)𝓛,
log Q_Π ≤ (π(z) + 64k²S*)𝓛 + 4.
```

*Proof.* The local lemma (O2 Thm 11.3's proof, neighbourhood sums
`≤2k c_0`) gives `δ:=E F ≥ e^{−2.2S}` on the class of one mod `Q_Π`. Lemma
3.1 with EL(t): `E[F−B] ≤ m²·S·e^{−3S}/(100m²(S+1)) ≤ δ/100`, so
`μ=E B ≥ 0.99δ`. Lemma 3.2 bounds `M_1` and the moduli (`N≤T`), Lemma 3.3
the twist; (I) (O2 Lemma 4.3 (I)) gives `B≤1[W>T]` on `n≡1 (Q_Π)`. Then PO
Thm 4.1, with the auxiliary prime `ℓ_0` as in O4 Thm 2.1, and
`|𝓑|≤kS*/c_0`. ∎

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
(Standard: Linial–Mansour–Nisan 1993; e.g. Lovett's notes, Lemma 3.3 and
Cor 3.4.)

(c) *Back to coordinates.* Put `g(x):=E[g̃(U) | π(U)=x]`. A character
`χ_S` (S a set of bits) involves the blocks of at most `|S|<d`
coordinates, and since the blocks are independent and π acts blockwise,
`E[χ_S | π(U)]` is a function of those coordinates. So g is a sum of
functions of `<d` coordinates. By Jensen (φ̃ is `π(U)`-measurable),
`E_{x∼π_*}(φ−g)² ≤ E(φ̃−g̃)²`. Finally each fibre has `⌊2^b/q⌋` or
`⌈2^b/q⌉` points, so the Haar density relative to `π_*` is
`≤∏_ℓ(1−q_ℓ2^{−b})^{−1} ≤ exp(2NT·2^{−b}) ≤ e^{1/2}`. Hence
`energy_{Haar}(φ;d) ≤ E_{Haar}(φ−g)² ≤ e^{1/2}2^{1−k_0} ≤ 4·2^{−k_0}`. ∎

**Corollary 4.2 (EL; PROVED).** In Theorem 3.4, EL(t) holds with

```
t := 2C_H·k·b·k_0,   k_0 := ⌈ 3S log₂e + log₂(400 m²(S+1)) ⌉,   b := ⌈log₂(4T²)⌉,
```

so `t ≤ C·k·𝓛·(S+𝓛)` (using `N≤T`, `m≤T²`). ∎

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
(Wigert, O2 Lemma 11.1): `t, K, log Q_Π ≤ S*^{1+o(1)}`, so
`log₂p ≤ (2log2+o(1))𝓛/log𝓛`, and `log𝓛 ~ log₃p`. ∎

**Comparison.** O4 Cor 3.1: `log W ≥ (1+o(1))log₂p·log₃p/log₄p` (mod TZ,
ET); O4 Cor 3.2: `log₂p·log₄p/log₅p` (mod TZ). Theorem 4.3 is the third
target of O4 §4.4 (declared "outside the method" there; it was outside
the *alternating-expansion* method), and matches the Haar side
`log(1/δ*)≪𝓛^7log𝓛` (O2 Thm 11.3) up to squaring: the transfer costs
`log p ≈ K·log Z` with both factors of Haar size. The heuristic truth is
`log W ≍ (log p)^{1/3}` (POINTWISE_SIZE §7).

**Why this escapes §2.** The error of the BRW minorant is an
*unconstrained* ℓ² error. The optimal junta approximation does not
alternate; on dense clusters it is small because F is small there
(suppression), and Håstad's lemma certifies this for *every* DNF of
bounded width, with no codegree, level or hub hypothesis. The width
`kb≍k𝓛` enters only linearly in t. Nothing about ES beyond (I), the
supports `≤k`, per-prime masses `≤1/(64k)`, and `S*` is used.
