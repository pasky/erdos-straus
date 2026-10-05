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
