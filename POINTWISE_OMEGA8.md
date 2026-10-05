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
